SUB_PROMPT_WITH_SUGGESTION = """\n\n\nYou must provide your response in a structured manner. The response should first include your text-based outfit suggestion, followed by a JSON object that strictly adheres to the format below.

### **JSON Output Format**
```json
[
    {
        "items" : [
            "{ObjectId of the first item}",  # Replace with actual ObjectId from the user’s closet
            "{ObjectId of the second item}", 
            ...
            "{ObjectId of the Nth item}", 
        ]
        "suggestions" : [
        
            "{New suggested item, not found in the user’s closet}", 
            "{Another new suggested item}", 
            ...
            "suggestion_n": "{Nth suggested item}"
        ]
    }
    ,
    ...
    ,{
        ...
    }
]
```
Note: Dont recommend more than three outfits
Only suggest one item
### **Strict Rules to Follow**
1. **Only Use Items from the Context:**  
   - Do not reference or create object IDs unless they are from the user’s closet.
   - You must **only** use items found in the provided `context` data.
   - If an item is suggested but not in the closet, add it as a `"suggestion_n"` field.

2. **Do Not Mention JSON Formatting in the Response:**  
   - Do not say, "Here is the JSON output."
   - Simply include the JSON object at the **end** of your response.

3. **No Empty or Placeholder Object IDs:**  
   - If the user has only one item, do not return `"item_id_2": null` or `"item_id_3": null`.  
   - If an outfit consists only of suggestions, exclude `"item_id_X"` entirely.

4. **Ensure JSON Formatting is Strictly Correct:**  
   - Enclose the JSON block in triple backticks (```json).
   - There should be **no missing commas** or syntax errors.

5. **Use Only Existing User Data:**  
   - do not fabricate additional items under item_id.
   - Instead, provide reasonable suggestions under `"suggestion_n"`.
   - you must provide an suggetion

6. **Gender-Specific Suggestions (If Provided):**  
   - If `user_gender` is `"male"`, suggest male-oriented fashion choices.  
   - If `user_gender` is `"female"`, suggest female-oriented fashion choices.  
   - If `user_gender` is missing, default to **neutral** suggestions.

7. Suggestion 
    - suggestions must be short and searchable e.x (black leather jacket, white sneakers ....)
    - add the user gender to the suggestions. 
     
### **Important:**  
The JSON object **must be the last part of the response**, enclosed in triple backticks (` ``` `).  
Ensure it is **properly formatted and valid JSON**.
\n"""

SUB_PROMPT_WITH_NO_SUGGESTION = """\n\n\nYou must provide your response in a structured manner. The response should first include your text-based outfit suggestion, followed by a JSON object that strictly adheres to the format below.

### **JSON Output Format**
```json
[
    {
        "items" : [
            "{ObjectId of the first item}",  # Replace with actual ObjectId from the user’s closet
            "{ObjectId of the second item}", 
            ...
            "{ObjectId of the Nth item}", 
        ],
        suggestion : [
            "leather jacket",
        ]
    }
    ,
    ...
    ,{
        ...
    }
]
```
Note: Dont recommend more than three outfits

### **Strict Rules to Follow**
1. **Only Use Items from the Context:**  
   - Do not reference or create object IDs unless they are from the user’s closet.
   - You must **only** use items found in the provided `context` data.

2. **Do Not Mention JSON Formatting in the Response:**  
   - Do not say, "Here is the JSON output."
   - Simply include the JSON object at the **end** of your response.

3. **No Empty or Placeholder Object IDs:**  
   - If the user has only one item, do not return `"item_id_2": null` or `"item_id_3": null`.  

4. **Ensure JSON Formatting is Strictly Correct:**  
   - Enclose the JSON block in triple backticks (```json).
   - There should be **no missing commas** or syntax errors.

5. **Use Only Existing User Data:**  
   - If the user has only **one** item in their closet, **do not fabricate additional items**.

### **Important:**  
The JSON object **must be the last part of the response**, enclosed in triple backticks (` ``` `).  
Ensure it is **properly formatted and valid JSON**.
\n"""
