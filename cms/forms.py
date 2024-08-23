from django import forms
from .models import Post
from tinymce.widgets import TinyMCE

class PostForm(forms.ModelForm):
    detail = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))

    class Meta:
        model = Post
        fields = ['title', 'image', 'snapshot', 'detail']

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        # You can still customize the form layout here, but without using FormHelper
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
