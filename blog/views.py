from django.shortcuts import render, get_object_or_404
from django.views import View
from django.http import HttpRequest, HttpResponse, JsonResponse
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView

from .models import Note


class NoteListCreateAPIView(APIView):
    def get(self, request: Request) -> Response:
        objects = Note.objects.all()
        list_obj = []
        for note in objects:
            list_obj.append({
                'id': note.id,
                'title': note.title,
                'text': note.message,
                'public': note.public,
                'created': note.created_at,
                'updated': note.updated_at
            })
        return Response(list_obj)

    def post(self, request: Request) -> Response:
        new_note = Note.objects.create(
            title=request.data['title'],
            message=request.data['text'],
            public=request.data['public'],
        )
        resp = {
            'id': new_note.id,
            'title': new_note.title,
            'text': new_note.message,
            'public': new_note.public,
            'created': new_note.created_at,
            'updated': new_note.updated_at
        }
        return Response(resp)


class NoteDetailAPIView(APIView):
    def get(self, request: Request, page) -> Response:
        obj = get_object_or_404(Note, id=page)
        resp = {
            'id': obj.id,
            'title': obj.title,
            'text': obj.message,
            'public': obj.public,
            'created': obj.created_at,
            'updated': obj.updated_at
        }
        return Response(resp)

    def put(self, request: Request, page) -> Response:
        obj = get_object_or_404(Note, id=page)
        obj.title = request.data['title']
        obj.message = request.data['text']
        obj.public = request.data['public']
        obj.save()

        resp = {
            'id': obj.id,
            'title': obj.title,
            'text': obj.message,
            'public': obj.public,
            'created': obj.created_at,
            'updated': obj.updated_at
        }
        return Response(resp)
