from django import template

register = template.Library()

@register.simple_tag(name='order_status')
def order_status(status):
    status = status - 1
    status_array = ["Confirmed", "Processed", "Delivered", "Cancelled"]
    return status_array[status]

