from django import forms
from products.widgets import CustomClearableFileInput
from .models import BlogPost


class BlogPostForm(forms.ModelForm):

    class Meta:
        model = BlogPost
        fields = ('title', 'image', 'content',)

    image = forms.ImageField(label='Image', required=True,
                             widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        """
        Function sets placeholders, adds auto-focus to top field
        and assigns all fields a class
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'title': 'Title',
            'image': 'Image',
            'content': 'Blog Content',
        }

        self.fields['title'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'image':
                self.fields[field].widget.attrs['placeholder'] = (
                    placeholders[field])
            self.fields[field].widget.attrs['class'] = 'blog-form-input'