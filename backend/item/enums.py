from enum import Enum

class CategoryEnum(str, Enum):
    ACCESSORY = "accessory"
    TOP = "top"
    BOTTOM = "bottom"
    DRESS = "dress"
    FOOTWEAR = "footwear"
    OUTERWEAR = "outerwear"
    SHOES = "shoes"
    ACCESSORIES = "accessories"
    BAGS = "bags"
    JEWELRY = "jewelry"
    HATS = "hats"
    SCARVES = "scarves"
    BELTS = "belts"
    SOCKS = "socks"
    UNDERWEAR = "underwear"
    SWIMWEAR = "swimwear"
    ACTIVEWEAR = "activewear"
    SLEEPWEAR = "sleepwear"
    OTHER = "other"  # For items that don't fit into the above categories

class SeasonEnum(str , Enum):
    SUMMER = "summer"
    WINTER = "winter"
    SPRING = "spring"
    FALL = "fall"
    ALL = "all"

class TypeEnum(str , Enum):
    FORMAL = "formal"
    SEMI_FORMAL = "semi-formal"
    CASUAL = "casual"
    SPORTS = "sports"
    BUSINESS = "business"
    PARTY = "party"
    BEACH = "beach"
    OTHER = "other"  # For items that don't fit into the above types