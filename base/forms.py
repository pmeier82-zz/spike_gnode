"""forms for the base application"""

from registration.forms import RegistrationForm
from django import forms


class ExRegistrationForm(RegistrationForm):
    is_human = forms.ChoiceField(label="Are you human?:")
