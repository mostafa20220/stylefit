
from bson import ObjectId
import json

def extract_json_from_response(response_text: str) -> dict:
    """
    Extracts JSON from the response text that contains both text and a JSON block.

    Args:
       response_text (str): The complete response text from the GenAI model

    Returns:
       dict: Parsed JSON object containing outfit information

    Raises:
       ValueError: If no valid JSON is found in the response
    """
    try:
        # Find the last occurrence of ```json and the following ```
        json_start = response_text.rindex("```json")
        json_end = response_text.rindex("```")

        # Extract the JSON string (excluding the ```json and ``` markers)
        json_str = response_text[json_start + 7 : json_end].strip()

        # Parse the JSON string into a Python dictionary
        outfits_data = json.loads(json_str)

        return outfits_data

    except (ValueError, json.JSONDecodeError) as e:
        raise ValueError(f"Failed to extract valid JSON from response: {str(e)}")
