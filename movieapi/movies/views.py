from django.shortcuts import render
from django.http import JsonResponse

def home(request):
    return render(request, 'movies/index.html')

def filmes_lista(request):
    filmes = [
        {
            "titulo": "Capitão América: O primeiro Vingador",
            "imagem": "https://br.web.img3.acsta.net/r_1920_1080/medias/nmedia/18/84/69/36/19774937.jpg",
            "ano": 2011
        },
        {
            "titulo": "Capitã Marvel",
            "imagem": "https://br.web.img2.acsta.net/r_1920_1080/img/35/ca/35ca03a8520c42c999c1d01ae1598b1b.jpg",
            "ano": 2019
        },
        {
            "titulo": "Homem de Ferro",
            "imagem": "https://br.web.img3.acsta.net/r_1920_1080/img/30/23/30232de235a8bca8533f5ddb06fef0dd.jpg",
            "ano": 2008
        },
        {
            "titulo": "Homem de Ferro 2",
            "imagem": "https://br.web.img2.acsta.net/r_1920_1080/img/93/52/93525b1f4241c37489914ec1e990e3cd.jpg",
            "ano": 2010
        },
        {
            "titulo": "Hulk",
            "imagem": "https://br.web.img2.acsta.net/r_1920_1080/medias/nmedia/18/65/69/21/18949753.jpg",
            "ano": 2008
        },
        {
            "titulo": "Thor",
            "imagem": "https://br.web.img3.acsta.net/r_1920_1080/medias/nmedia/18/77/96/35/19701393.jpg",
            "ano": 2011
        },
        {
            "titulo": "Os Vingadores",
            "imagem": "https://br.web.img3.acsta.net/r_1920_1080/img/ac/73/ac73fdd7ee4a9eaea1b19f8ec1400382.jpg",
            "ano": 2012
        }
    ]

    
    search_query = request.GET.get('search', '').lower()
    if search_query:
        filmes = [filme for filme in filmes if search_query in filme['titulo'].lower()]

    return JsonResponse(filmes, safe=False)
