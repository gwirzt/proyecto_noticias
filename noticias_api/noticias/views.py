from django.shortcuts import render
import requests
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.conf import settings
from .models import Article
from .serializers import ArticleSerializer


@api_view(['POST'])
def external_news(request):
    url = 'https://newsapi.org/v2/everything'
    keywords_list = request.data.get('keywords', [])  # Obtener lista de palabras clave del JSON
    if not keywords_list:
        return Response({"error": "No keywords provided"}, status=400)
    
    keywords = ' OR '.join(keywords_list)  # Convertir lista de palabras clave a cadena separada por OR
   
    params = {
        'q': keywords,  # Cambia este término de búsqueda según tus necesidades
        'apiKey': settings.NEWS_API_KEY
    }
    response = requests.get(url, params=params)
    articles = response.json().get('articles', [])
    return Response(articles)


@api_view(['GET', 'POST'])
def internal_news(request):
    if request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    elif request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)

# Create your views here.
