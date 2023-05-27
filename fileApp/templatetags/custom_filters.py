from django import template

register = template.Library()

print("-"*20+"\nHello\n"+"-"*20)

@register.filter(name="extract_filename")
def extract_filename(value):
    return value.split('/')[-1]