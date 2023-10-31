from django.shortcuts import render, get_object_or_404
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Note
from .serializers import NoteSerializer


class NoteViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]
    def list(self, request):
        queryset = Note.objects.filter(owner=request.user)
        serializer = NoteSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk):
        queryset = Note.objects.all()
        note = get_object_or_404(queryset, pk=pk, owner=request.user)
        serializer = NoteSerializer(note)
        return Response(serializer.data)
    
    def create(self, request):
        serializer = NoteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, pk):
        queryset = Note.objects.all()
        note = get_object_or_404(queryset, pk=pk, owner=request.user)
        note.delete()
        return Response({"Note deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
    
    def partial_update(self, request, pk):
        queryset = Note.objects.all()
        note = get_object_or_404(queryset, pk=pk, owner=request.user)
        serializer = NoteSerializer(note, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)