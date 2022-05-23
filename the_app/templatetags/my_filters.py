from django import template

register = template.Library()
@register.filter()

def is_not_numeric(value):
    if value == None:
    	return True
    return False
  