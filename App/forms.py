from django import forms


class CursoFormulario(forms.Form):

    #Especificar los campos
    curso = forms.CharField()
    grupo = forms.IntegerField()


class ProfesorFormulario(forms.Form):   
    nombre= forms.CharField(max_length=30)
    apellido= forms.CharField(max_length=30)
    email= forms.EmailField()
    area= forms.CharField(max_length=30)