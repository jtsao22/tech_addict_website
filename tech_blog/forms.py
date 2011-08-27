from google.appengine.ext.db import djangoforms
from models import Post

class PostForm(djangoforms.ModelForm):
    class Meta:
        model = Post
        exclude = ['published']
