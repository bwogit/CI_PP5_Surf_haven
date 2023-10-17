# 3rd Party Imports
from django import template
# Internals
register = template.Library()


@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    return price * quantity
