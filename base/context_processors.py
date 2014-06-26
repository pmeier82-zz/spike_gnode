from django.contrib.sites.models import Site


def base(request):
    obj = Site.objects.get_current()
    return {
        'SITE_ID': obj.id,
        'SITE_NAME': obj.name,
    }
