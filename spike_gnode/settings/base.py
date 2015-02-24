# -*- coding: utf-8 -*-

import os
import logging
from django.core.exceptions import ImproperlyConfigured


def get_env_setting(setting):
    """ Get the environment setting or return exception """
    try:
        return os.environ[setting]
    except KeyError:
        raise ImproperlyConfigured("Set the {} env variable!".format(setting))

# Your project root
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__) + "../../../")

SUPPORTED_NONLOCALES = ["media", "admin", "static"]

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = "en-gb"

# Defines the views served for root URLs.
ROOT_URLCONF = "spike_gnode.urls"

# Application definition
INSTALLED_APPS = (
    # Django contrib apps
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.admin",
    "django.contrib.humanize",
    "django.contrib.syndication",
    "django.contrib.staticfiles",
    "django.contrib.sites",
    # Third-party apps, patches, fixes
    "captcha",
    "djcelery",
    "debug_toolbar",
    "compressor",
    "registration",
    "bootstrap3",
    # rest framework
    # "rest_framework",
    # "rest_framework.authtoken",
    # base and initial data
    "base",
    "initial_data",
)

# Place bcrypt first in the list, so it will be the default password hashing
# mechanism
PASSWORD_HASHERS = (
    "django.contrib.auth.hashers.BCryptSHA256PasswordHasher",
    "django.contrib.auth.hashers.BCryptPasswordHasher",
    "django.contrib.auth.hashers.PBKDF2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher",
    "django.contrib.auth.hashers.SHA1PasswordHasher",
    "django.contrib.auth.hashers.MD5PasswordHasher",
    "django.contrib.auth.hashers.CryptPasswordHasher",
)

# Sessions
#
# By default, be at least somewhat secure with our session cookies.
SESSION_COOKIE_HTTPONLY = True

# Set this to true if you are using https
SESSION_COOKIE_SECURE = False

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.example.com/media/"
MEDIA_ROOT = os.path.join(PROJECT_ROOT, "media")

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.example.com/media/", "http://example.com/media/"
MEDIA_URL = "/media/"

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.example.com/static/"
STATIC_ROOT = os.path.join(PROJECT_ROOT, "static")

# URL prefix for static files.
# Example: "http://media.example.com/static/"
STATIC_URL = "/static/"

# Additional locations of static files
STATICFILES_DIRS = (
# Put strings here, like "/home/html/static" or "C:/www/django/static".
# Always use forward slashes, even on Windows.
# Don't forget to use absolute paths, not relative paths.
)

# load up internationalization, localization and timezones machinery.
USE_I18N = True
USE_L10N = True
USE_TZ = True

# refer to http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
TIME_ZONE = "Europe/Berlin"

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
    "compressor.finders.CompressorFinder",
)

MIDDLEWARE_CLASSES = [
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

TEMPLATE_CONTEXT_PROCESSORS = [
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.media",
    "django.core.context_processors.request",
    "django.core.context_processors.i18n",
    "django.core.context_processors.static",
    "django.core.context_processors.csrf",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",
    "base.context_processors.base",
]

TEMPLATE_DIRS = (
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(PROJECT_ROOT, "templates"),
)

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    "django.template.loaders.filesystem.Loader",
    "django.template.loaders.app_directories.Loader",
)

TEST_RUNNER = "django.test.runner.DiscoverRunner"


def custom_show_toolbar(request):
    """Only show the debug toolbar to users with the superuser flag."""
    return request.user.is_superuser


DEBUG_TOOLBAR_CONFIG = {
    "INTERCEPT_REDIRECTS": False,
    "SHOW_TOOLBAR_CALLBACK": "spike_gnode.settings.base.custom_show_toolbar",
    "HIDE_DJANGO_SQL": True,
    "TAG": "body",
    "SHOW_TEMPLATE_CONTEXT": True,
    "ENABLE_STACKTRACES": True,
}

# DEBUG_TOOLBAR_PANELS = (
# #'debug_toolbar_user_panel.panels.UserPanel',
#     'debug_toolbar.panels.version.VersionDebugPanel',
#     'debug_toolbar.panels.timer.TimerDebugPanel',
#     'debug_toolbar.panels.settings_vars.SettingsVarsDebugPanel',
#     'debug_toolbar.panels.headers.HeaderDebugPanel',
#     'debug_toolbar.panels.request_vars.RequestVarsDebugPanel',
#     'debug_toolbar.panels.template.TemplateDebugPanel',
#     'debug_toolbar.panels.sql.SQLDebugPanel',
#     'debug_toolbar.panels.signals.SignalDebugPanel',
#     'debug_toolbar.panels.logger.LoggingPanel',
# )

# Specify a custom user model to use
#AUTH_USER_MODEL = 'accounts.MyUser'

FILE_UPLOAD_PERMISSIONS = 0o0664

# The WSGI Application to use for runserver
WSGI_APPLICATION = "spike_gnode.wsgi.application"

# Define your database connections
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.",
        "NAME": "",
        "USER": "",
        "PASSWORD": "",
        "HOST": "",
        "PORT": "",
        # "OPTIONS": {
        #    "init_command": "SET storage_engine=InnoDB",
        #    "charset": "utf8",
        #    "use_unicode": True,
        # },
        "TEST_CHARSET": "utf8",
        "TEST_COLLATION": "utf8_general_ci",
    },
    # "slave": {
    #     ...
    # },
}

# Uncomment this and set to all slave DBs in use on the site.
# SLAVE_DATABASES = ["slave"]

# Recipients of traceback emails and other notifications.
ADMINS = (
# ("Your Name", "your_email@domain.com"),
)
MANAGERS = ADMINS

# SECURITY WARNING: don't run with debug turned on in production!
# Debugging displays nice error messages, but leaks memory. Set this to False
# on all server instances and True only for development.
DEBUG = TEMPLATE_DEBUG = False

# True on development/master and False on stage/prod.
DEV = False

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []

# SECURITY WARNING: keep the secret key used in production secret!
# Hardcoded values can leak through source control.
# This is an example method of getting the value from an environment setting.
# Uncomment to use, and then make sure you set the SECRET_KEY environment variable.
# This is good to use in production, and on services that support it such as Heroku.
SECRET_KEY = get_env_setting("SECRET_KEY")

# RECAPTCHA
RECAPTCHA_PUBLIC_KEY = get_env_setting("RECAPTCHA_PUBLIC_KEY")
RECAPTCHA_PRIVATE_KEY = get_env_setting("RECAPTCHA_PRIVATE_KEY")
RECAPTCHA_USE_SSL = True

# Uncomment these to activate and customize Celery:
# CELERY_ALWAYS_EAGER = False  # required to activate celeryd
# BROKER_HOST = 'localhost'
# BROKER_PORT = 5672
# BROKER_USER = 'django'
# BROKER_PASSWORD = 'django'
# BROKER_VHOST = 'django'
# CELERY_RESULT_BACKEND = 'amqp'

INTERNAL_IPS = ("127.0.0.1")
SITE_ID = 1

# Enable this option for memcached
CACHE_BACKEND = "memcached://127.0.0.1:11211/"

# Set this to true if you use a proxy that sets X-Forwarded-Host
#USE_X_FORWARDED_HOST = False

SERVER_EMAIL = "spike-dev@gnode.org"
DEFAULT_FROM_EMAIL = "spike-dev@gnode.org"
SYSTEM_EMAIL_PREFIX = "[gnode-spike]"

## Log settings
LOG_LEVEL = logging.INFO
HAS_SYSLOG = True
SYSLOG_TAG = "http_app_gnode_spike"  # Make this unique to your project.
# Remove this configuration variable to use your custom logging configuration
LOGGING_CONFIG = None
LOGGING = {
    "version": 1,
    "loggers": {
        "spike_gnode": {
            "level": "DEBUG"
        }
    }
}

# Common Event Format logging parameters
# CEF_PRODUCT = "Spike G-Node"
# CEF_VENDOR = "German Neuroinformatics Node"
# CEF_VERSION = "0"
# CEF_DEVICE_VERSION = "0"

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
DEFAULT_FILE_STORAGE = "base.storage.HashedFileSystemStorage"

ACCOUNT_ACTIVATION_DAYS = 7
REGISTRATION_AUTO_LOGIN = True
