from django import template

register = template.Library()

@register.simple_tag(name='cart_subtotal')
def cart_subtotal(ordered_items):
    return sum(item.product.price * item.quantity for item in ordered_items.added_items.all())