from django import template
from django.contrib.humanize.templatetags.humanize import intcomma

register = template.Library()

@register.filter
def format_currency(value):
    formatted_value = intcomma(value)
    return f"${formatted_value}".replace(",", ".")