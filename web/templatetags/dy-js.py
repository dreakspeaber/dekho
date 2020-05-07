from django.utils.safestring import mark_safe
from django.template import Library
from web.models import *
from django.contrib.auth.models import User

import json


register = Library()


@register.filter(is_safe=True)
def js(obj):
    return mark_safe(json.dumps(obj))

@register.filter(is_safe=True)
def saleprice(uid,id):
    user=User.objects.get(pk=id)
    price=0
    sales=Sales.objects.filter(user=user)
    for sale in sales:
        price+=sale.price
    return "{:,}".format(price) + 'Rs'