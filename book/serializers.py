from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import *


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ("id","title", "subtitle", "author", "isbn", "price")

    # def validate(self, data):
    #     title = data.get("title", None)
    #     author = data.get("author", None)
    #     if not title.isalpha():
    #         raise ValidationError(
    #             {
    #                 "status": False,
    #                 "message": "Kitob sarlavhasi harflardan iborat bo'lishi kerak!"
    #             }
    #         )
    #
    #     if Book.objects.filter(title=title, author=author).exists():
    #         raise ValidationError(
    #             {
    #                 "status": False,
    #                 "message": "Kitob va Muallif bir xil bo'lmasligi kerak!"
    #             }
    #         )
    #
    #     return data
