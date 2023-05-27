from django import template

register = template.Library()

@register.tag
def extract_filename(value):
    return value.split('/')[-1]

