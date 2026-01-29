from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['content', 'image']
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': '¿Qué estás pensando?'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={
                'placeholder': 'Escribe tu comentario...',
                'rows': 3,
                'style': 'width: 100%; padding: 10px; border: 1px solid #eff3f4; border-radius: 10px; font-family: inherit; font-size: 15px; resize: none;'
            }),
        }
        labels = {
            'content': '',
        }
