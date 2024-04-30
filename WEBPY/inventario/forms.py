from django import forms
from .models import Usuario
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate

class RegistroForm(UserCreationForm):
    nombres = forms.CharField(label='Nombres')
    apellidos = forms.CharField(label='Apellidos')
    email = forms.EmailField(max_length=255)
    dni = forms.CharField(max_length=88)
        # unidadOrganica = forms.CharField(max_length=10)
        # sede = forms.CharField(max_length=10)
        # estado = forms.CharField(max_length=10)
        # rol = forms.CharField(max_length=10)
    class Meta:
        model = Usuario  # Use your custom user model if applicable
        fields = ['nombres','apellidos','username','email']  # Customize fields

    def __init__(self, *args, **kwargs):
        super(RegistroForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field.widget.attrs.get('class'):
                field.widget.attrs['class'] += ' form-control'
            else:
                field.widget.attrs['class']='form-control'


class LoginForm(forms.Form):
    username = forms.CharField(label='Username')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError('Usuario o contraseña incorrectos.')
            elif not user.is_active:
                raise forms.ValidationError('Este usuario está inactivo.')
        
        return cleaned_data


# class RegisterForm(UserCreationForm):
#     email = forms.EmailField( label='Email')
#     username = forms.CharField(label='username', min_length=5, max_length=150)  
#     age = forms.IntegerField(label='Edad',min_value=0)
#     phone = forms.IntegerField(label='Telefono')
#     address = forms.CharField(label='Dirección')
#     image = forms.ImageField(label='Foto')
    
#     class Meta:
#         model = User
#         fields = ['username','email','password1','age','phone','address','image']
     
#     def __init__(self, *args, **kwargs):
#         super(RegisterForm, self).__init__(*args, **kwargs)
#         for field_name, field in self.fields.items():
#             if field.widget.attrs.get('class'):
#                 field.widget.attrs['class'] += ' form-control'
#             else:
#                 field.widget.attrs['class']='form-control'

#     def save(self, commit = True):  
#         user = User.objects.create_user(  
#             self.cleaned_data['username'],  
#             self.cleaned_data['email'],  
#             self.cleaned_data['password1']  
#         )  
#         return user 




# class CreateNewProduct(forms.Form):
#     SELECTION_TYPE = (
#         ('L', 'LITROS'),
#         ('M', 'METROS'),
#         ('V', 'VOLUMEN'),
#         ('U', 'UNIDAD'),
#     )

#     code = forms.CharField(label = " Codigo " , max_length = 10 )
#     name = forms.CharField(label="Nombre")
#     description = forms.CharField(label = " Descripcion de tarea ", widget=forms.Textarea)
#     price_unit = forms.FloatField() 
#     quantity = forms.FloatField()
#     type_product = forms.ChoiceField(choices=SELECTION_TYPE)
#     category = forms.ModelMultipleChoiceField(
#         queryset= CaAtegory.objects.all(), widget=forms.CheckboxSelectMultiple
#     )
#     def __init__(self, *args, **kwargs):
#         super(CreateNewProduct, self).__init__(*args, **kwargs)
#         for field_name, field in self.fields.items():
#             if field.widget.attrs.get('class'):
#                 field.widget.attrs['class'] += ' form-control'
#             else:
#                 field.widget.attrs['class']='form-control'
#     def save(self):
#         cleaned_data = self.cleaned_data