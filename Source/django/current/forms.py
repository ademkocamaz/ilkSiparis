from django import forms
from current._model.current import Current


class CurrentForm(forms.ModelForm):
    class Meta:
        model = Current
        fields = [
            field.name
            for field in Current._meta.fields
            if field.name not in ("edited, created, user")
        ]
