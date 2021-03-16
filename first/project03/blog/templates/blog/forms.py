from django import forms
from .models import Comment

class CommentCreateForm(forms.Model):
    class Meta:
        model = Comment
        fields = '__all__'