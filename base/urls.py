"""urlconf for the base application"""

from django.conf.urls import include, patterns, url
from django.views.generic import TemplateView
from forms import SpikeGnodeRegistrationForm
from registration.backends.default.views import RegistrationView

urlpatterns = patterns(
    'base.views',
    url(r'^$', 'home', name='home'),
    url(r'^imprint$', TemplateView.as_view(template_name="base/imprint.html"), name='imprint'),
    url(r'^team$', TemplateView.as_view(template_name="base/team.html"), name='team'),
    url(r'accounts/register/$',
        RegistrationView.as_view(form_class=SpikeGnodeRegistrationForm),
        name='registration_register'),
    url(r'^accounts/', include('registration.backends.default.urls')), )
