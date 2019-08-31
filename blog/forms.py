from django import forms
from blog.models import Post, Comment

class PostForm(forms.ModelForm):

    class Meta():
        model = Post
        fields = ('title', 'text', 'author')

        widgets = {
            'title': forms.TextInput(attrs = {
                'placeholder': 'Title'
            }),
            'text': forms.Textarea(attrs = {
                'class': 'summernote',
                'placeholder': 'Text'
            })
        }

class CommentForm(forms.ModelForm):

    class Meta():
        model = Comment
        fields = ('author', 'text')

        widgets = {
            'author': forms.TextInput(attrs = {
                'placeholder': 'Author'
            }),
            'text': forms.Textarea(attrs = {
                'placeholder': 'Text'
            })
        }

