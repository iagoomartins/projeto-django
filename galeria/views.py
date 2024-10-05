# Create your views (rotas) here.
from django.shortcuts import render, get_object_or_404
from galeria.models import Fotografia

# rota da pagina principal
def index(request):

    """ buscar no banco de dados e mostrar todos os cards na pág. principal
        por ordem de data mais recente """                                      
    fotografias = Fotografia.objects.order_by('data_fotografia').filter(publicada=True)
    return render(request, 'galeria/index.html', {"cards": fotografias})

# rota da imagem
def imagem(request, foto_id):
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    return render(request, 'galeria/imagem.html',{"fotografia": fotografia})
    
# rota do mecanismo de busca
def buscar(request):
    fotografias = Fotografia.objects.order_by('data_fotografia').filter(publicada=True)

    if 'buscar' in request.GET:
        nome_a_buscar = request.GET['buscar']
        if nome_a_buscar:
            fotografias = fotografias.filter(nome__icontains=nome_a_buscar)

    return render(request, 'galeria/buscar.html', {"cards": fotografias})
