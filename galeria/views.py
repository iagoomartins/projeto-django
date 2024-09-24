# Create your views here.
from django.shortcuts import render


# view da pagina principal
def index(request):
    return render(request, 'galeria/index.html')

# view da imagem
def imagem(request):
    return render(request, 'galeria/imagem.html')