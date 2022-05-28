from rest_framework import serializers
from blog.models import Note


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note  # Модель для обработки.
        fields = '__all__'  # Отображение всех полей.
        # fields = ('id', 'author',...) Отображение конкретных полей.
        # exclude = ('id', 'author',...) Отображение за исключением.
        read_only_fields = ('author',)
