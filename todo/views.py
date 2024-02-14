from django.shortcuts import render

from rest_framework import viewsets, views

from todo.serializers import TodoSerializer
from todo.models import TodoEntry


class TodoViewSet(viewsets.ModelViewSet):
    """
    This covers the basic once.
    Todoviewset covers:
    Get with filters,
    Post
    Patch
    Delete
    """
    queryset = TodoEntry.objects.all()
    serializer_class = TodoSerializer
    pagination_class = None

# class TodoBulkUpdateView(views.APIView):
#     serializer_class = 

#     def post(self, request, *args, **kwargs):

