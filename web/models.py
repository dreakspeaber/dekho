from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from sortedm2m.fields import SortedManyToManyField




class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile_user')
    is_admin=models.BooleanField(blank=True,default=False)
    is_sales=models.BooleanField(blank=True,default=True)
    phone=models.CharField(blank=True,default="",max_length=15)
    percentage=models.PositiveIntegerField(default=10,blank=True)
    time = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return f"{self.user}"



class Services(models.Model):
    name=models.CharField(max_length=20)

    def __str__(self):
        return f"{self.name}"



class Location(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"


class Activities(models.Model):
    name = models.CharField(max_length=100)
    loc = models.ForeignKey(Location,on_delete=models.CASCADE,related_name='activities_location')
    service = models.ForeignKey(Services,on_delete=models.CASCADE,related_name='activities_service')
    price = models.PositiveIntegerField()
    render_tag = models.TextField()


    def __str__(self):
        return f"{self.name}"




class D6(models.Model):
    customer=models.CharField(max_length=100)
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='d6_user')
    day1=SortedManyToManyField(Activities,related_name='d6_day1_activities')
    day2=models.ManyToManyField(Activities,blank=True,related_name='d6_day2_activities')
    day3=models.ManyToManyField(Activities,blank=True,related_name='d6_day3_activities')
    day4=models.ManyToManyField(Activities,blank=True,related_name='d6_day4_activities')
    day5=models.ManyToManyField(Activities,blank=True,related_name='d6_day5_activities')
    day6=models.ManyToManyField(Activities,blank=True,related_name='d6_day6_activities')
    has_closed=models.BooleanField(blank=True,default=False)
    price=models.PositiveIntegerField(blank=True,default=0)
    


    def __str__(self):
        return f"{self.user}"


class TesterPackage(models.Model):
    day1=SortedManyToManyField(Activities,related_name='tester_activities')
    day2=SortedManyToManyField(Activities,blank=True,related_name='tester2_activities')
    
    


class Sales(models.Model):
    customer=models.CharField(max_length=100)
    heading=models.CharField(max_length=100,default="")
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='sales_user')        
    price=models.PositiveIntegerField(default=0,blank=True)
    cut=models.PositiveIntegerField(default=0,blank=True)
    time = models.DateTimeField(default=datetime.now, blank=True)
    has_closed=models.BooleanField(default=False,blank=True)


    def _get_date(self):
        prtime = datetime.now()
        if self.time.day == prtime.day:
            return str(prtime.hour - self.time.hour) + " hours ago"
        else:
            if self.time.month == prtime.month:
                return str(prtime.day - self.time.day) + " days ago"
            else:
                if self.time.year == prtime.year:
                    return str(prtime.month - self.time.month) + " months ago"
        return self.time

    def _get_price(self):
        price=self.price
        return "{:,}".format(price) + 'Rs'
    
    get_date = property(_get_date)
    get_price = property(_get_price)


for x in range(1,11):
        var='loc' + str(x)
        var_name=var + '_loc'
        vard='activities' + str(x)
        vard_name=vard + '_loc'
        Sales.add_to_class('loc%s' %str(x),models.ForeignKey(Location,blank=True,null=True,on_delete=models.CASCADE,related_name=var_name))
        Sales.add_to_class('activities%s' %str(x), SortedManyToManyField(Activities,blank=True,related_name=var_name))



class Notification(models.Model):
    content=models.TextField()