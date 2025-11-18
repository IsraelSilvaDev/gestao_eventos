import uuid
from django.db import models
from django.contrib.auth.models import User

# Função para gerar um código de acesso único
def gerar_codigo_acesso():
    """Gera um código alfanumérico único de 8 dígitos."""
    return uuid.uuid4().hex[:8].upper()

class Evento(models.Model):
    # O organizador é um usuário logado
    organizador = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Organizador")
    nome = models.CharField(max_length=200, verbose_name="Nome do Evento")
    data = models.DateTimeField(verbose_name="Data e Hora")
    local = models.CharField(max_length=300, verbose_name="Local")
    descricao = models.TextField(blank=True, null=True, verbose_name="Descrição")
    codigo_acesso = models.CharField(
        max_length=8, 
        unique=True, 
        default=gerar_codigo_acesso, 
        verbose_name="Código de Acesso"
    )

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Evento"
        verbose_name_plural = "Eventos"

class Resposta(models.Model):
    STATUS_CHOICES = (
        ('confirmado', "Sim, irei"),
        ('declinado', "Não poderei ir"),
    )

    evento = models.ForeignKey(Evento, on_delete=models.CASCADE, related_name="respostas", verbose_name="Evento")
    nome_principal = models.CharField(max_length=200, verbose_name="Nome do Convidado Principal")
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, verbose_name="Status")
    total_pessoas = models.PositiveIntegerField(default=1, verbose_name="Total de Pessoas")
    observacoes = models.TextField(blank=True, null=True, verbose_name="Observações")
    data_resposta = models.DateTimeField(auto_now_add=True, verbose_name="Data da Resposta")

    def __str__(self):
        return f"{self.nome_principal} - {self.evento.nome}"
    
    class Meta:
        verbose_name = "Resposta"
        verbose_name_plural = "Respostas"