from posts.models import Post
from django.forms import ModelForm
from django.core.exceptions import ValidationError


BADWORDS = ("meapilas","abollao", "abrazafarolas" , "afinabanjos", "diseñata", "aparcabicis", "tuercebotas")


class PostForm(ModelForm):


    class Meta:
        model = Post
        exclude = ['owner']

        #validacion del formulario
    def clean(self):
        """
        Valida que la descripción no contenga ninguna palabrota
        :return: diccionario con los datos limpios y validados
        """
        cleaned_data = super().clean()
        description = cleaned_data.get('description', '')
        for badword in BADWORDS:
            if badword in description:
                raise ValidationError("La palabra {0} no está permitida". format(badword))
        return cleaned_data