from django import forms
from .models import Inscrito, Institucion


class FormInscripcion(forms.ModelForm):
    class Meta:
        model = Inscrito
        fields = [
            "nombre",
            "telefono",
            "institucion",
            "hora",
            "estado",
            "observaciones",
        ]
        widgets = {
            "nombre": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Tu nombre"}),
            "telefono": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Tu telefono"}
            ),
            "institucion": forms.Select(
               attrs={"class": "form-control", "placeholder": "Elige una institucion"}
            ),
            "hora": forms.TimeInput(
                
                attrs={"class": "form-control", "placeholder": "Elige una hora", "type": "time"}
            ),
            "estado": forms.Select(
                attrs={"class": "form-control", "placeholder": "Elige un estado"}
            ),
            "observaciones": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "Ingresa observaciones si corresponde",
                }
            ),
        }
        labels = {
            "nombre": "Nombre",
            "telefono": "Telefono",
            "institucion": "Institucion",
            "hora": "Hora",
            "estado": "Estado",
            "observaciones": "Observaciones",
        }
        

    def clean_institucion(self):
        institucion = self.cleaned_data.get("institucion")
        print(institucion)
        if institucion == "Sin institucion disponible":
            raise forms.ValidationError("Como no hay instituciones agregadas, no puedes inscribirte")
        return institucion

class FormActualizarInscripcion(forms.ModelForm):
    class Meta:
        model = Inscrito
        fields = [
            "nombre",
            "telefono",
            "institucion",           
            "hora",
            "estado",
            "observaciones",
        ]
        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control", "placeholder": "Tu nombre"}),
            "telefono": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Tu telefono"}
            ),
            "institucion": forms.Select(
                attrs={"class": "form-control", "placeholder": "Elige una institucion"}
            ),
            "hora": forms.TimeInput(
                attrs={"class": "form-control", "placeholder": "Elige una hora", "type": "time"}
            ),
            "estado": forms.Select(
                attrs={"class": "form-control", "placeholder": "Elige un estado"}
            ),
            "observaciones": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "Ingresa observaciones si corresponde",
                }
            ),
            
        }
        labels = {
            "nombre": "Nombre",
            "telefono": "Telefono",
            "institucion": "Institucion",
            "hora": "Hora",
            "estado": "Estado",
            "observaciones": "Observaciones",
        }
