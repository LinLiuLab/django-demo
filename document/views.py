from django.views.decorators.http import require_http_methods
from .service import DocumentService
from django.http import JsonResponse
import json

from django.views.decorators.csrf import csrf_exempt

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .service import DocumentService


class DocumentList(APIView):
    """
    API endpoint that allows documents to be viewed and created.
    """
    def get(self, request):
        """
        Retrieve all documents.
        """
        return JsonResponse(DocumentService.get_all_documents())

    def post(self, request):
        """
        Create a new document.
        """
        title = request.data.get('title')
        content = request.data.get('content')
        published = request.data.get('published')
        return JsonResponse(DocumentService.create_document(title, content, published))

class DocumentDetail(APIView):
    """
    API endpoint that allows documents to be viewed, updated and deleted.
    """
    def get(self, request, id):
        """
        Retrieve a specific document by id.
        """
        return JsonResponse(DocumentService.get_document(id))

    def put(self, request, id):
        """
        Update a specific document by id.
        """
        title = request.data.get('title')
        content = request.data.get('content')
        published = request.data.get('published')
        return JsonResponse(DocumentService.update_document(id, title, content, published))

    def delete(self, request, id):
        """
        Delete a specific document by id.
        """
        return JsonResponse(DocumentService.delete_document(id))


