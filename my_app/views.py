from rest_framework import serializers
from django.shortcuts import render
from rest_framework.generics import DestroyAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from my_app.models import Note
from my_app.serializers import NoteSerializer


# Create your views here.

class IndexView(APIView):
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]

    def get(self, request):
        print(request.user)
        return Response({'message': 'success'})

    def post(self, request):

        return Response({'message': 'post worked'})

class NoteView(APIView):
    def get(self, request):
        notes = Note.objects.all()
        note_list = []
        for note in notes:
            note_list.append({
                'id': note.id,
                'title': note.name,
                'description': note.description,
                'status': 'done' if note.done else 'in process'
            })
        return Response({'notes': note_list})

class NotesCreateView(APIView):
    def post(self, request):
        note_serializer = NoteSerializer(data =request.data)
        if note_serializer.is_valid():
            note = Note.objects.create(**note_serializer.data)
            note = NoteSerializer(note)
            return Response(note.data)
        return Response('Неверные данные для запроса', status=422)

# class NoteListView(ListAPIView):
#     queryset = Note.objects.all()
#     serializer_class = NoteSerializer


class NotesReadView(APIView):
    def get(self, request):
        notes = Note.objects.all()
        notes_serializer = NoteSerializer(notes, many=True)

        return Response(notes_serializer.data)

class NotesUpdateView(UpdateAPIView):
    def put(self, request, pk):
        note = Note.objects.get(id=pk)
        note_serializer = NoteSerializer(note, data=request.data)
        if note_serializer.is_valid():
            note_serializer.save()
            return Response(note_serializer.data)
        return Response('Неверные данные для запроса', status=422)

class NotesDeleteView(DestroyAPIView):
    queryset = Note.objects.all()


class MakeNoteDoneView(APIView):
    def put(self, request, pk):
        note = Note.objects.get(id=pk)
        note.done = True
        note.save()
        return Response({'message': 'Note marked as done'})