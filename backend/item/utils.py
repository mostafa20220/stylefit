import requests
from PIL import Image
from io import BytesIO
from google import genai
import json
import re

from dotenv import load_dotenv
import os

load_dotenv()
genai_key = os.getenv("GEMINI_API")

PROMPT = """
```
Generate a JSON object representing a clothing item with the following structure.  

### **JSON Structure:**  
```json
{ 
    "category": "accessory | top | bottom | dress | footwear | outerwear | shoes | accessories | bags | jewelry | hats | scarves | belts | socks | underwear | swimwear | activewear | sleepwear | other",  
    "color": "<A relevant color based on common clothing colors>",  
    "season": "summer | winter | spring | fall | all",  
    "type": "formal | semi-formal | casual | sports | business | party | beach | other",  
    "pattern": "<A common clothing pattern such as Solid, Striped, Plaid, Floral>",  
    "material": "<A common clothing material such as Cotton, Polyester, Silk, Wool>",  
    "description": "<A short, well-written description of the clothing item>",  
    
}
```

### **Constraints:**  
1. **Strict Enum Compliance:**  
   - The values for `"category"`, `"season"`, and `"type"` **must strictly** match the predefined enums.  
   - If the category is missing or unclear, choose from the **CategoryEnum** list.  
   - If the season is missing, default to **"other"** instead of generating a random value.  
   - If the type is missing, default to **"other"**.  

2. **Data Generation Rules:**  
   - `"color"`: Must be a valid color name (e.g., "red", "blue", "beige").  
   - `"pattern"`: Choose from common patterns (e.g., "solid", "striped", "plaid", "floral", "printed").  
   - `"material"`: Choose from standard materials (e.g., "cotton", "polyester", "silk", "wool", "linen").  
   - `"description"`: Should be **concise** and **descriptive**. Example:  
     - *"A lightweight cotton summer dress with a floral pattern, perfect for warm days."*  
    

3. **Output Format:**  
   - **Return the response as a JSON object only, with no additional text or explanation.**  
   - Ensure all values are properly quoted and formatted as a valid JSON.  

### **Example Output:**  
```json
{
    "category": "dress",
    "color": "blue",
    "season": "summer",
    "type": "casual",
    "pattern": "floral",
    "material": "cotton",
    "description": "A lightweight cotton summer dress with a floral pattern, perfect for warm days.",
}
```
```
"""


def get_genai_response(prompt, context=PROMPT):
    # Send to Gemini API
    client = genai.Client(api_key=genai_key)
    # prompt = PROMPT + f"\nHere is IMAGE_URL {image_url}\n"
    # prompt += f"\nHere is the ID for the JSON Object {user_id}\n"
    response = client.models.generate_content(
        model="gemini-2.0-flash", contents=[prompt, context]
    )

    return response


def download_image(image_url):
    # Download image from URL
    response = requests.get(image_url)
    if response.status_code == 200:
        image = Image.open(BytesIO(response.content))
        print(type(image))
        return image
    else:
        print("Failed to download image")


def generate_item_schema(response_text):
    match = re.search(r"```json\s*(\{.*\})\s*```", response_text, re.DOTALL)

    if match:
        json_obj = json.loads(match.group(1))
        return json_obj
    else:
        print("Failed to match regex expression, check the response back")
        # TODO: log response in some file
        return None


def convert_uploaded_file_to_pil(uploaded_file):
    image = Image.open(uploaded_file)
    return image


def item_generator(uploaded_img, image_url, user_id):

    image = convert_uploaded_file_to_pil(uploaded_img)

    response = get_genai_response(prompt=image)

    print(response)

    newItem = generate_item_schema(response.text)
    newItem["image"] = image_url
    newItem["user"] = user_id

    return newItem


if __name__ == "__main__":
    download_image(
        "https://res.cloudinary.com/dyulsrqq6/image/upload/v1742127980/l5zngyliewelflpdwcxw.webp"
    )
