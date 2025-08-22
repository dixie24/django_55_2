from django import forms    
from posts.models import Post

class PostForm(forms.ModelForm):
    title = forms.CharField(max_length=256)
    content = forms.CharField(max_length=512)
    image = forms.ImageField(required=False)
    
    def clean_title(self):
        cleaned_data = super().clean()
        title = cleaned_data.get("title")
        if title.lower() == "javascript":
            raise forms.ValidationError("Title cannot be 'javascript'.")
        return title
    
    
    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get("title")
        content = cleaned_data.get("content")
        if title and content and (title.lower() == content.lower()):
            raise forms.ValidationError("Title and content cannot be the same.")
        return cleaned_data