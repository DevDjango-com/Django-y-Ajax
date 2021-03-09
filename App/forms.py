from django import forms 
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        # exclude = ['author', 'actualizar', 'creado', ]
        fields = ['texto']
        widgets = {
            'text': forms.TextInput(attrs={
                'id': 'post-texto', 
                'required': True, 
                'placeholder': 'Escribe algo...'
            }),
        }