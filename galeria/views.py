# Create your views here.
from django.shortcuts import render, get_object_or_404
from galeria.models import Fotografia

# view da pagina principal
def index(request):
    fotografias = Fotografia.objects.order_by('data_fotografia').filter(publicada=True)
    return render(request, 'galeria/index.html', {"cards": fotografias})

# view da imagem
def imagem(request, foto_id):
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    return render(request, 'galeria/imagem.html',{"fotografia": fotografia})
    