from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

import user.views
from item.models import Item
from item.utils import get_genai_response

from item.serializers import ItemSerializer
from .serializers import OutfitSerializer
from .sub_prompts import SUB_PROMPT_WITH_SUGGESTION, SUB_PROMPT_WITH_NO_SUGGESTION
from utils.utils import extract_json_from_response



@api_view(["POST"])
def chat(request):
    # user closet -> mongo db with
    closet = Item.objects.filter(user=request.user)
    serializer = ItemSerializer(closet, many=True)
    context = [{"user_gender": request.user.gender}, serializer.data]


    # message that is going to be sent to gemini (AI_MODEL)
    prompt = request.data.get("prompt")

    # Default to False if not provided
    suggest_new_items = request.data.get("suggest", False)

    if suggest_new_items:
        prompt += SUB_PROMPT_WITH_SUGGESTION
    else:
        prompt += SUB_PROMPT_WITH_NO_SUGGESTION


    # print("prompt: ", prompt)
    # print("context :", context)

    response = get_genai_response(prompt=prompt, context=str(context))
    outfits = extract_json_from_response(response.text)
    print(outfits)

    serialized_outfits = OutfitSerializer(outfits, context={"user_gender" : request.user.gender}, many=True).data

    return Response(serialized_outfits, status=status.HTTP_200_OK)
