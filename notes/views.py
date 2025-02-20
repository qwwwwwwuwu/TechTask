from rest_framework import generics
from rest_framework import generics, permissions, status
from .models import Note
from .serializers import NoteSerializer
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
import logging

        
from django.shortcuts import render

def home(request):
     return render(request, 'home.html')  


logger = logging.getLogger(__name__)

class NoteListCreateView(generics.ListCreateAPIView):
        # ...
    def perform_create(self, serializer):
        logger.info(f"User {self.request.user.username} creating a new note.")
        serializer.save(owner=self.request.user)




class NoteListCreateView(generics.ListCreateAPIView):
    serializer_class = NoteSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return Note.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class NoteRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = NoteSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return Note.objects.filter(owner=self.request.user)

    def get_object(self):
        queryset = self.get_queryset()
        note_id = self.kwargs['pk']  # Use 'pk' instead of 'id'
        return get_object_or_404(queryset, pk=note_id)
