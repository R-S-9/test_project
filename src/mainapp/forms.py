from django import forms

from mainapp.models import News, Image


class AddNews(forms.ModelForm):
    class Meta:
        model = News
        fields = [
            'title',
            'content',
        ]


class AddImage(forms.ModelForm):
    img = forms.ImageField(
        required=False,
        label=Image._meta.get_field('img').verbose_name
    )

    class Meta:
        model = Image
        fields = [
            'img'
        ]
