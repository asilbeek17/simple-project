from django.forms import ModelForm
from app.models import Post


class ProductModelForm(ModelForm):

    class Meta:
        model = Post
        fields = '__all__'
        exclude = ()
