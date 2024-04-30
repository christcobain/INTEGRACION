from django import forms
from .models import Category, Product
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError  

class RegisterForm(UserCreationForm):
    email = forms.EmailField( label='Email')
    username = forms.CharField(label='username', min_length=5, max_length=150)  
    age = forms.IntegerField(label='Edad',min_value=0)
    phone = forms.IntegerField(label='Telefono')
    address = forms.CharField(label='Dirección')
    image = forms.ImageField(label='Foto')
    
    class Meta:
        model = User
        fields = ['username','email','password1','age','phone','address','image']
     
    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field.widget.attrs.get('class'):
                field.widget.attrs['class'] += ' form-control'
            else:
                field.widget.attrs['class']='form-control'

    def save(self, commit = True):  
        user = User.objects.create_user(  
            self.cleaned_data['username'],  
            self.cleaned_data['email'],  
            self.cleaned_data['password1']  
        )  
        return user 




class CreateNewProduct(forms.Form):
    SELECTION_TYPE = (
        ('L', 'LITROS'),
        ('M', 'METROS'),
        ('V', 'VOLUMEN'),
        ('U', 'UNIDAD'),
    )

    code = forms.CharField(label = " Codigo " , max_length = 10 )
    name = forms.CharField(label="Nombre")
    description = forms.CharField(label = " Descripcion de tarea ", widget=forms.Textarea)
    price_unit = forms.FloatField() 
    quantity = forms.FloatField()
    type_product = forms.ChoiceField(choices=SELECTION_TYPE)
    category = forms.ModelMultipleChoiceField(
        queryset= Category.objects.all(), widget=forms.CheckboxSelectMultiple
    )
    def __init__(self, *args, **kwargs):
        super(CreateNewProduct, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field.widget.attrs.get('class'):
                field.widget.attrs['class'] += ' form-control'
            else:
                field.widget.attrs['class']='form-control'
    def save(self):
        cleaned_data = self.cleaned_data