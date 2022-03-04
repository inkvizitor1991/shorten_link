from django import template
from link.models import Link


register = template.Library()

@register.simple_tag()
def get_links():
    return Link.objects.order_by('-created_at')