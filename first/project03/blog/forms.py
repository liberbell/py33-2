from django import forms
from .models import Comment

class CommentCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    class Meta:
        model = Comment
        fields = ('name', 'text')