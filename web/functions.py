from web.models import *
from datetime import datetime

class sale:
    def __init__(self,sales):
        self.sales=sales

    def update(self):
        sales=self.sales
        price=0
        if sales.activities1.all():
            for activity in sales.activities1.all():
                price =price+activity.price
        if sales.activities2.all():
            for activity in sales.activities2.all():
                price =price+activity.price
        percentage=Profile.objects.get(user=sales.user).percentage
        cut=percentage/100 * price
        sales.cut=cut
        sales.price=price+cut
        sales.save()
        return True



def get_sales_data(sales):
    converted=0
    non_converted=0
    totalsale=0
    for sale in sales:
        if sale.has_closed:
            converted+=1
            totalsale+=sale.price
        else:
            non_converted+=1
    return converted,non_converted,totalsale


    
class get_data:
    def __init__(self,user):
        self.profile=Profile.objects.get(user=user)
        self.user=user

    def last_month(self):
        now=datetime.now()
        now.month=now.month-1
        return Sales.objects.filter(time__gt=now,user=self.user).order_by('-time')

    def last6_month(self):
        now=datetime.now()
        now.month=now.month-6
        return Sales.objects.filter(time__gt=now,user=self.user).order_by('-time')

    def last12_month(self):
        now=datetime.now()
        now.month=now.month-12
        return Sales.objects.filter(time__gt=now,user=self.user).order_by('-time')



