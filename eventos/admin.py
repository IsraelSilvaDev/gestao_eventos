from django.contrib import admin
from .models import Evento, Resposta

# Para mostrar as respostas dentro da página do evento no Admin
class RespostaInline(admin.TabularInline):
    model = Resposta
    extra = 0 # Não mostra formulários extras em branco
    readonly_fields = ('nome_principal', 'status', 'total_pessoas', 'observacoes', 'data_resposta') # Apenas leitura no admin
    can_delete = False # Não permite deletar respostas por aqui

@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'data', 'local', 'codigo_acesso', 'organizador')
    list_filter = ('organizador', 'data')
    search_fields = ('nome', 'codigo_acesso')
    
    # Adiciona o inline das respostas na página de detalhes do evento
    inlines = [RespostaInline]

    # --- Permissões e Facilidades ---

    def save_model(self, request, obj, form, change):
        """Ao salvar um novo evento, define o organizador como o usuário logado."""
        if not obj.pk: # Se é um novo objeto
            obj.organizador = request.user
        super().save_model(request, obj, form, change)

    def get_queryset(self, request):
        """Filtra os eventos para que superusuários vejam tudo, mas staff (organizadores) vejam apenas os seus."""
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        # Filtra para mostrar apenas eventos do usuário 'staff' logado
        return qs.filter(organizador=request.user)

    def get_form(self, request, obj=None, **kwargs):
        """Remove o campo 'organizador' do formulário de criação/edição."""
        form = super().get_form(request, obj, **kwargs)
        # Usuários staff não-superusuários não devem poder trocar o organizador
        if not request.user.is_superuser:
            form.base_fields.pop('organizador', None)
        return form

# Registra o modelo Resposta para ser visível no admin (opcional, mas bom para debug)
@admin.register(Resposta)
class RespostaAdmin(admin.ModelAdmin):
    list_display = ('nome_principal', 'evento', 'status', 'total_pessoas', 'data_resposta')
    list_filter = ('evento', 'status')
    search_fields = ('nome_principal',)