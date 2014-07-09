"""forms for the base application"""

from registration.forms import RegistrationForm
from django import forms


class SpikeGnodeRegistrationForm(RegistrationForm):
    is_human = forms.ChoiceField(label="Are you human?:", choices=((True, "YES"), (False, "NO")))
