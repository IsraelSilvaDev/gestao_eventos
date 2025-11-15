from django import forms
from .models import Resposta

class CodigoAcessoForm(forms.Form):
    """Formulário para o convidado inserir o código do evento."""
    codigo = forms.CharField(
        label="Código de Acesso do Evento", 
        max_length=8,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ABC12345'})
        
    )

class RespostaForm(forms.ModelForm):
    """Formulário para o convidado preencher o RSVP."""
    
    # Adicionamos a escolha de status diretamente no formulário para torná-la obrigatória e clara
    status = forms.ChoiceField(
        choices=Resposta.STATUS_CHOICES,
        widget=forms.RadioSelect(attrs={'class': 'btn-check'}),
        label="Você irá ao evento?"
        
    )

    class Meta:
        model = Resposta
        fields = ['nome_principal', 'status', 'total_pessoas', 'observacoes']
        labels = {
            'nome_principal': 'Seu Nome Completo',
            'total_pessoas': 'Número Total de Pessoas (incluindo você)',
            'observacoes': 'Observações (ex: restrições alimentares, horário de chegada)',
        }
        widgets = {
            'nome_principal': forms.TextInput(attrs={'class': 'form-control'}),
            'total_pessoas': forms.NumberInput(attrs={'class': 'form-control', 'min': '1'}),
            'observacoes': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

    def clean(self):
        """
        Limpa os dados do formulário.
        Se o status for 'declinado', zera o total_pessoas.
        """
        cleaned_data = super().clean()
        status = cleaned_data.get("status")
        
        if status == 'declinado':
            # Se declinou, forçamos o total de pessoas para 0
            cleaned_data['total_pessoas'] = 0
        elif cleaned_data.get('total_pessoas', 0) < 1:
            # Se confirmou, garante que o número seja pelo menos 1
             raise forms.ValidationError("O número total de pessoas deve ser pelo menos 1.")

        return cleaned_data