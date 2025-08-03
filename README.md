# StyleFit

StyleFit is a smart outfit suggestion system that helps users organize their wardrobe, categorize clothing items, and receive personalized outfit recommendations based on seasons, occasions, and personal style.

## Key Features

### 👕 Clothing Categorization
- Store and manage clothing items by **Category** (Accessory, Top, Bottom, Dress, Footwear)
- Support for various **Materials** (Cotton, Linen, Denim, Wool, etc.)
- Identify **Patterns** (Solid, Striped, Checked, Floral, etc.)

### 🎨 Smart Color & Season Matching
- Classify outfits based on **Color** (Red, Blue, Black, etc.)
- Tag outfits according to **Seasons** (Summer, Winter, Spring, Autumn)
- Suggest outfits that match seasonal trends

### 🎭 Occasion-Based Outfit Suggestions
- Categorize outfits by **Type** (Formal, Semi-Formal, Casual)
- Get style recommendations tailored to specific events

### 🖼️ Image Storage & Representation
- Store outfit images in **JSON format** for seamless integration with Django and MongoDB
- Efficient image management with metadata for quick retrieval

### 🛠️ Tech Stack
- **Backend:** Django, Django REST Framework
- **Database:** MongoDB
- **Mobile:** React Native
<!-- - **Authentication:** Django Allauth or JWT-based login (optional feature) -->

## Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/stylefit.git
   cd stylefit
   ```
2. **Create a virtual environment and install dependencies:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   pip install -r requirements.txt
   ```
3. **Set up MongoDB:**
   - Install MongoDB and start the service
   - Configure the database connection in Django settings

4. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

## Example JSON Representation
```json
{
    "Id": "1a2b3c",
    "Category": "top",
    "Color": "blue",
    "Season": "summer",
    "Type": "casual",
    "Pattern": "solid",
    "Material": "cotton",
    "Description": "Lightweight blue t-shirt for summer",
    "Image": "path/to/image.jpeg"
}
```

## Future Enhancements
- AI-powered outfit suggestions based on user preferences
- Integration with e-commerce platforms for style inspiration
- Social sharing of outfit combinations

## Contributing
Pull requests are welcome! If you'd like to contribute, feel free to fork the repository and submit a PR.

## License
MIT License © 2025 StyleFit
