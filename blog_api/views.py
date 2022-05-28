from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from blog.models import Note
from blog_api import serializers, filters


class NoteListCreateAPIView(APIView):
    def get(self, request):
        notes = Note.objects.all()
        serializer = serializers.NoteSerializer(
            instance=notes,
            many=True,  # Для обработки множества значений, т.к. notes содержит все объекты.
        )
        return Response(data=serializer.data)

    def post(self, request):
        serializer = serializers.NoteSerializer(
            data=request.data
        )
        serializer.is_valid(raise_exception=True)  # Проверка по признакам, указанным в модели.
        serializer.save(author=request.user)
        return Response(data=serializer.data, status=201)


class PublicNoteListAPIView(ListAPIView):
    """/notes/public"""
    queryset = Note.objects.all()  # .filter(public=True) not recommended queryset ~ SQL Query
    serializer_class = serializers.NoteSerializer

    def get_queryset(self):  # Для получения фильтрованых данных. Динамический фильтр.
        queryset = super().get_queryset()
        return queryset.filter(public=True)

    def filter_queryset(self, queryset):
        return filters.note_filter_by_author_id(
            queryset,
            author_id=self.request.query_params.get("author_id", None)
        )

