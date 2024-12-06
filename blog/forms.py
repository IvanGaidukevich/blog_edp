from django import forms
from blog.models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

    author = forms.IntegerField(widget=forms.HiddenInput(), required=False)