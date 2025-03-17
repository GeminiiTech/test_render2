from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Note
from .serializers import NoteSerializer

# Create your views here.

class NoteView(APIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

    def get(self, request):
        notes = Note.objects.all()
        serializer = NoteSerializer(notes, many=True)
        return Response(serializer.data,status.HTTP_200_OK)
    
    def post(self, request):
        serializer = NoteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)



# asgiref==3.8.1
# dj-database-url==2.3.0
# Django==5.1.7
# django-cors-headers==4.7.0
# djangorestframework==3.15.2
# djangorestframework_simplejwt==5.5.0
# gunicorn==23.0.0
# packaging==24.2
# psycopg2-binary==2.9.10
# PyJWT==2.9.0
# python-dotenv==1.0.1
# sqlparse==0.5.3
# typing_extensions==4.12.2
# tzdata==2025.1
