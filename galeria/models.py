from django.db import models
from datetime import datetime

# Create your models here.
# modelos (tabelas) para banco de dados
"""
Para mudar / excluir / adicionar / novas colunas de uma tabela, basta:
    - adicionar uma variavel na classe Fotografia (exemplo), colocar suas características, (ex: Charfield) e fazer uma
    Migration no terminal. 
"""

OPCOES_CATEGORIAS = [
    ('NEBULOSA', 'Nebulosa'),
    ('ESTRELA', 'Estrela'),
    ('GALAXIA', 'Galáxia'),
    ('PLANETA', 'Planeta'),
]


class Fotografia(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    legenda = models.CharField(max_length=200, null=False, blank=False)
    categoria = models.CharField(max_length=100, choices=OPCOES_CATEGORIAS, default='')
    descricao = models.TextField(null=False, blank=False)
    foto = models.ImageField(upload_to='fotos/%Y/%m/%d', blank=True)
    publicada = models.BooleanField(default=False)
    data_fotografia = models.DateTimeField(default=datetime.now, blank=False)
    
    def __str__(self):
        return f'Nome: {self.nome}'

