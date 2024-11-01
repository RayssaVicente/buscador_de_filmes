from django.shortcuts import render
from django.http import JsonResponse

def home(request):
    return render(request, 'movies/index.html')

def filmes_lista(request):
    filmes = [
        {
            "titulo": "Capitão América: O primeiro Vingador",
            "imagem": "https://via.placeholder.com/150",
            "ano": 2011
        },
        {
            "titulo": "Capitã Marvel",
            "imagem": "https://via.placeholder.com/150",
            "ano": 2019
        },
        {
            "titulo": "Homem de Ferro",
            "imagem": "https://via.placeholder.com/150",
            "ano": 2008
        },
        {
            "titulo": "Homem de Ferro 2",
            "imagem": "https://via.placeholder.com/150",
            "ano": 2010
        },
        {
            "titulo": "Hulk",
            "imagem": "https://via.placeholder.com/150",
            "ano": 2008
        },
        {
            "titulo": "Thor",
            "imagem": "https://via.placeholder.com/150",
            "ano": 2011
        },
        {
            "titulo": "Os Vingadores",
            "imagem": "https://via.placeholder.com/150",
            "ano": 2012
        }
    ]

    
    search_query = request.GET.get('search', '').lower()
    if search_query:
        filmes = [filme for filme in filmes if search_query in filme['titulo'].lower()]

    return JsonResponse(filmes, safe=False)
