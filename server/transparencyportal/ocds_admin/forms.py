from django import forms
from django.core.exceptions import ValidationError

class UploadFileForm(forms.Form):
    def validate_file_extension(value):
        if not value.name.endswith('.xlsx'):
            raise ValidationError(u'Le type de fichier n\'est pas pris en charge')

    file = forms.FileField(label="Fichier à importer", validators=[validate_file_extension])
