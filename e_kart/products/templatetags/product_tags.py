from django import template

register = template.Library()

@register.filter(name='chunk_products')
def chunk_products(products_datalist, chunk_size):
    # Splits the list of products into chunks of chunk_size.
    chunk = []
    i=0
    for product in products_datalist:
        chunk.append(product)
        i += 1
        if i == chunk_size:
            yield chunk
            i = 0
            chunk = []
    if chunk:
        yield chunk
