from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(
        label="Ваше имя",
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})  # Добавляем класс Bootstrap
    )
    email = forms.EmailField(
        label="Ваш email",
        widget=forms.EmailInput(attrs={'class': 'form-control'})  # Добавляем класс Bootstrap
    )
    message = forms.CharField(
        label="Сообщение",
        widget=forms.Textarea(attrs={'class': 'form-control'})  # Добавляем класс Bootstrap
    )