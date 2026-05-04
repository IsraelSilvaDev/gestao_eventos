from django.contrib import admin
from .models import Evento, Resposta, Convite, Acompanhante


class ConviteInline(admin.TabularInline):
    model = Convite
    extra = 3
    readonly_fields = ('codigo_acesso',)


@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'data', 'local', 'organizador')
    inlines = [ConviteInline]


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


@admin.register(Convite)
class ConviteAdmin(admin.ModelAdmin):
    list_display = ('codigo_acesso', 'get_evento', 'nome_destinatario', 'get_status_resposta')
    search_fields = ('codigo_acesso', 'nome_destinatario', 'evento__nome')

    def get_evento(self, obj):
        return obj.evento.nome
    get_evento.short_description = 'Evento'

    def get_status_resposta(self, obj):
        if hasattr(obj, 'resposta'):
            return obj.resposta.status
        return 'Pendente'
    get_status_resposta.short_description = 'Status'