from django.shortcuts import render
from decouple import config
# Create your views here.
from rest_framework.response import Response
from rest_framework.decorators import api_view
from api.apps import faiss_search

@api_view('GET')
def get_images(request):
    query = request.query_params.get('query')
    count = request.query_params.get('count')
    image_documents = faiss_search.mongo_search(query,count)
    return Response({
        'images': image_documents
    })