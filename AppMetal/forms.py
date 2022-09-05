from django import forms
 
class IngresantesForm(forms.Form):
    nombre= forms.CharField(max_length=50)
    apellido= forms.CharField(max_length=50)

class GraduadosForm(forms.Form):
    nombre= forms.CharField(max_length=50)
    apellido= forms.CharField(max_length=50)

class BandasForm(forms.Form):
    nombre= forms.CharField(max_length=50)
    asignado= forms.IntegerField()
    