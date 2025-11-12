from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    """Form for creating and updating comments. """
    class Meta:
        model = Comment
        fields = ('body',)