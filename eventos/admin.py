from django.contrib import admin
from .models import Evento, Resposta, Convite, Acompanhante

# Facilidade para gerar VÁRIOS códigos (convites) dentro do próprio evento
class ConviteInline(admin.TabularInline):
    model = Convite
    extra = 3 # Quantos convites em branco vão aparecer de uma vez
    readonly_fields = ('codigo_acesso',)

@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'data', 'local', 'organizador')
    inlines = [ConviteInline]
    # O código original mantido aqui de get_queryset, save_model, etc...

class AcompanhanteInline(admin.TabularInline):
    model = Acompanhante
    extra = 0
    can_delete = False
    readonly_fields = ('nome_completo', 'documento')

@admin.register(Resposta)
class RespostaAdmin(admin.ModelAdmin):
    list_display = ('nome_principal', 'get_evento', 'status', 'total_pessoas', 'data_resposta')
    inlines = [AcompanhanteInline]

    def get_evento(self, obj):
        return obj.convite.evento.nome
    get_evento.short_description = 'Evento'