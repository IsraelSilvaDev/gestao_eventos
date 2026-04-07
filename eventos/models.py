import uuid
from django.db import models
from django.contrib.auth.models import User

def gerar_codigo_acesso():
    return uuid.uuid4().hex[:8].upper()

class Evento(models.Model):
    organizador = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Organizador")
    nome = models.CharField(max_length=200, verbose_name="Nome do Evento")
    data = models.DateTimeField(verbose_name="Data e Hora")
    local = models.CharField(max_length=300, verbose_name="Local")
    descricao = models.TextField(blank=True, null=True, verbose_name="Descrição")
    # O campo codigo_acesso foi removido daqui!

    def __str__(self):
        return self.nome

# NOVO MODELO: Convite
class Convite(models.Model):
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE, related_name="convites", verbose_name="Evento")
    nome_destinatario = models.CharField(max_length=200, verbose_name="Nome do Destinatário", help_text="Ex: Família Silva (Opcional)", blank=True, null=True)
    codigo_acesso = models.CharField(max_length=8, unique=True, default=gerar_codigo_acesso, verbose_name="Código Único do Convite")

    def __str__(self):
        return f"Convite: {self.codigo_acesso} - {self.evento.nome}"

class Resposta(models.Model):
    STATUS_CHOICES = (
        ('confirmado', "Sim, irei"),
        ('declinado', "Não poderei ir"),
    )
    # Relacionamento 1 para 1: Um convite/código só pode ter UMA resposta
    convite = models.OneToOneField(Convite, on_delete=models.CASCADE, related_name="resposta", verbose_name="Convite", blank=True, null=True)
    nome_principal = models.CharField(max_length=200, verbose_name="Nome do Convidado Principal")
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, verbose_name="Status")
    total_pessoas = models.PositiveIntegerField(default=1, verbose_name="Total de Pessoas")
    observacoes = models.TextField(blank=True, null=True, verbose_name="Observações")
    data_resposta = models.DateTimeField(auto_now=True, verbose_name="Data da Resposta") # auto_now atualiza na edição

    def __str__(self):
        return self.nome_principal

# NOVO MODELO: Acompanhantes
class Acompanhante(models.Model):
    resposta = models.ForeignKey(Resposta, on_delete=models.CASCADE, related_name="acompanhantes")
    nome_completo = models.CharField(max_length=200, verbose_name="Nome Completo do Acompanhante")
    documento = models.CharField(max_length=50, verbose_name="Documento com Foto (RG/CPF)")

    def __str__(self):
        return self.nome_completo