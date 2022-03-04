from django import forms


class AddLinkForm(forms.Form):
    received_url = forms.URLField(
        max_length=100, label='URL-адрес, который нужно укоротить'
    )
    short_url = forms.CharField(
        max_length=100, label='Название укороченной ссылки', required=False
    )

class SerchLinkForm(forms.Form):
    link = forms.CharField(
        max_length=100, label='Название ссылки которую нужно найти', required=False
    )