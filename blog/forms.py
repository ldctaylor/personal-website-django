from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']
        widgets = {
            # 'name': forms.TextInput(attrs={'class': 'col-sm-12'}),
            # 'email': forms.EmailInput(attrs={'class': 'col-sm-12'}),
            'comment': forms.Textarea(attrs={'class': 'form-control'}),
        }