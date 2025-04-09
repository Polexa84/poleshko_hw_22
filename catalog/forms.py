from django import forms
from .models import Product

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

FORBIDDEN_WORDS = [  # Список запрещенных слов
    'казино', 'криптовалюта', 'крипта',
    'биржа', 'дешево', 'бесплатно',
    'обман', 'полиция', 'радар'
]

class ProductForm(forms.ModelForm):
    """
    Форма для создания и обновления продукта.
    Использует ModelForm для автоматического создания полей на основе модели Product.
    """
    honeypot = forms.CharField(required=False,
                                widget=forms.HiddenInput,
                                label="Оставьте это поле пустым") # Защита от спама
    class Meta:
        model = Product  # Указываем модель, с которой связана форма
        fields = ['name', 'description', 'image', 'category', 'purchase_price']  # Список полей, которые будут отображаться в форме

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),  # Для загрузки файлов
            'category': forms.Select(attrs={'class': 'form-control'}),
            'purchase_price': forms.NumberInput(attrs={'class': 'form-control'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name != 'honeypot':
                if field_name in self.errors:
                    self.fields[field_name].widget.attrs['class'] = field.widget.attrs.get('class', '') + ' is-invalid'

    def clean_name(self):
        """
        Валидация поля 'name'.
        Проверяет, не содержит ли название продукта запрещенные слова.
        Приводит название к нижнему регистру для регистронезависимой проверки.
        """
        name = self.cleaned_data['name'].lower()  # Получаем название продукта и приводим к нижнему регистру
        for word in FORBIDDEN_WORDS:  # Перебираем список запрещенных слов
            if word in name:  # Проверяем, содержится ли запрещенное слово в названии
                raise forms.ValidationError(f"Недопустимое слово '{word}' в названии продукта.")  # Выбрасываем исключение, если запрещенное слово найдено
        return self.cleaned_data['name']  # Возвращаем очищенное название, если все проверки пройдены

    def clean_description(self):
        """
        Валидация поля 'description'.
        Проверяет, не содержит ли описание продукта запрещенные слова.
        Приводит описание к нижнему регистру для регистронезависимой проверки.
        """
        description = self.cleaned_data['description'].lower()  # Получаем описание продукта и приводим к нижнему регистру
        for word in FORBIDDEN_WORDS:  # Перебираем список запрещенных слов
            if word in description:  # Проверяем, содержится ли запрещенное слово в описании
                raise forms.ValidationError(f"Недопустимое слово '{word}' в описании продукта.")  # Выбрасываем исключение, если запрещенное слово найдено
        return self.cleaned_data['description']  # Возвращаем очищенное описание, если все проверки пройдены

    def clean_purchase_price(self):
        """
        Валидация поля 'purchase_price'.
        Проверяет, что цена продукта не может быть отрицательной.
        """
        price = self.cleaned_data['purchase_price']  # Получаем значение поля 'purchase_price'
        if price <= 0:  # Если цена отрицательная
            raise forms.ValidationError("Цена не может быть отрицательной или равна нулю.")  # Выбрасываем исключение с сообщением об ошибке
        return price  # Возвращаем очищенное значение поля 'purchase_price'

    def clean_honeypot(self):
        """
        Валидация поля 'honeypot'.
        Проверяет, что поле 'honeypot' должно быть пустым (защита от спама).
        """
        if self.cleaned_data['honeypot']:  # Если поле 'honeypot' заполнено
            raise forms.ValidationError("Это поле должно быть пустым.")  # Выбрасываем исключение с сообщением об ошибке
        return self.cleaned_data['honeypot']  # Возвращаем очищенное значение поля 'honeypot'