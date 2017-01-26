from django import forms

from .models import Customer


class ProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
        self.fields['email'].required = True
        self.fields['phone_number'].required = True

    class Meta:
        model = Customer
        fields = [
            "first_name",
            "last_name",
            "phone_number",
            "email"
        ]
