from mongoengine import Document, StringField, URLField, EnumField, ReferenceField
from .enums import CategoryEnum, SeasonEnum, TypeEnum
from user.models import Profile  # Import the Profile model


class Item(Document):
    user = ReferenceField(
        Profile, required=True, reverse_delete_rule=2
    )  # Link to Profile
    category = EnumField(CategoryEnum, required=True)
    color = StringField(required=True)
    season = EnumField(SeasonEnum, required=True)
    type = EnumField(TypeEnum, required=True)
    pattern = StringField(required=True)
    material = StringField(required=True)
    description = StringField()
    image = URLField(required=True)  # Storing image as a URL

    def __str__(self):
        return f"{self.user.username}: {self.category.value} - {self.color} - {self.type.value}"
