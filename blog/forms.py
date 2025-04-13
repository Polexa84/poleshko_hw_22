from django import forms
from .models import BlogPost  # Импортируем модель BlogPost

class PostForm(forms.ModelForm):
    """
    Форма для создания и редактирования постов блога.
    """
    class Meta:
        model = BlogPost  # Указываем модель, с которой связана форма
        fields = ['title', 'content', 'preview', 'is_published']  # Список полей, которые будут отображаться в форме
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),  # Текстовое поле с классом Bootstrap
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),  # Текстовая область с классом Bootstrap
            'preview': forms.FileInput(attrs={'class': 'form-control'}),  # Поле для загрузки файлов с классом Bootstrap
            'is_published': forms.CheckboxInput(attrs={'class': 'form-check-input'}),  # Чекбокс с классом Bootstrap
        }

    def __init__(self, *args, **kwargs):
        """
        Инициализация формы.
        Добавляет стили Bootstrap к полям формы.
        """
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():  # Перебираем все поля формы
            field.widget.attrs['class'] = field.widget.attrs.get('class', '') + ' form-control'  # Добавляем класс form-control
            if field_name in self.errors:  # Если поле содержит ошибки
                field.widget.attrs['class'] += ' is-invalid'  # Добавляем класс is-invalid для отображения ошибок
            field.label = f'{field.label}' # Добавляем класс form-label к label