from django.http import HttpResponse, HttpResponseRedirect, Http404, JsonResponse
from django.shortcuts import render,redirect
from django.urls import reverse
from django.views.generic import TemplateView,ListView
from django.views import View
from django.contrib.auth.models import User
import requests
import json
from web.models import *
from web.forms import *
from rest_framework.views import APIView
from rest_framework.response import Response
from web.functions import *
#authentication helpers
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from django.contrib.auth import authenticate,logout, login
from django.contrib import messages


# Admin Dash starts


class index(APIView):
    def get(self, request):

        return redirect(reverse('viewscat'))

class loginpg(APIView):
    authentication_classes=[SessionAuthentication,BasicAuthentication]
    def get(self, request):
        if request.user.is_authenticated:
            return redirect(reverse('viewscat'))
        form=LoginForm()
        return render(request, 'web/login.html',{'form':form})

    def post(self,request):
        form=LoginForm(request.POST)
        user = authenticate(username=request.POST['name'],password=request.POST['password'])
        if user is not None:
            login(request, user)
            profile=Profile.objects.get(user=user)
            if profile.is_admin:
                return redirect(reverse('admin_home'))
            if profile.is_sales:
                return redirect(reverse('service_home'))
        
        return render(request, 'web/login.html',{'form':form})





class addscat(APIView):
    authentication_classes=[SessionAuthentication,BasicAuthentication]
    def get(self, request):
        if request.user.is_anonymous:
            return redirect(reverse('signin'))
        profile=Profile.objects.get(user=self.request.user)
        if not profile.is_admin:
            return redirect(reverse('service_home'))
        form=SalesExecForm()
        return render(request, 'web/addscat.html',{'form':form})

    def post(self,request):
        if request.user.is_anonymous:
            return redirect(reverse('signin'))
        profile=Profile.objects.get(user=self.request.user)
        if not profile.is_admin:
            return redirect(reverse('service_home'))
        form=SalesExecForm(request.data)
        if form.is_valid():
            if request.data['password'] != request.data['confirm_password']:
                return render(request, 'web/addscat.html',{'form' : form, 'message' : "Passwords don't match"})
            try:
                user=User.objects.create_user(username=request.data['username'],
                password=request.data['password'])
            except:
                return render(request, 'web/addscat.html',{'form' : form, 'message' : "Passwords don't match"})

            profile=Profile(user=user,is_sales=True,phone=request.data['phonenumber'])

            profile.save()
            if request.data['percentage']:
                profile.percentage=request.data['percentage']
                profile.save()
            return redirect(reverse('viewscat'))
        


class viewscat(ListView):
    authentication_classes=[SessionAuthentication,BasicAuthentication]
    template_name='web/viewscat.html'
    paginate_by=10


    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['user'] = self.request.user
        return context

    
    def get_queryset(self):
        return Profile.objects.filter(is_sales=True).order_by('-id')


    def get(self,*args, **kwargs):
        if self.request.user.is_anonymous:
            return redirect(reverse('signin'))
        profile=Profile.objects.get(user=self.request.user)
        if not profile.is_admin:
            return redirect(reverse('service_home'))
        return super().get(*args, **kwargs)



class activity(APIView):
    authentication_classes=[SessionAuthentication,BasicAuthentication] 
    def get(self, request,*args,**kwargs):
        if self.kwargs['id']==0:
            form=ActivitiesForm()
        else:
            activity=Activities.objects.get(pk=self.kwargs['id'])
            form=ActivitiesForm(instance=activity)
        return render(request, 'web/activity.html',{'form' : form})

    def post(self, request,*args,**kwargs):
        if self.kwargs['id']==0:
            form=ActivitiesForm(request.POST)
        else:
            activity=Activities.objects.get(pk=self.kwargs['id'])
            form=ActivitiesForm(request.POST,instance=activity)
        if form.is_valid():
            form.save()
            return redirect(reverse('viewact'))
        return render(request, 'web/activity.html',{'form' : form})


class salesup(APIView):
    def get(self, request):
        return render(request, 'web/salesupdate.html')


class nonconvert(APIView):
    def get(self, request):
        return render(request, 'web/nonconvert.html')


class notify(APIView):
    def get(self, request):
        try:
            notification=Notification.objects.get(pk=1)
            form=NotificationForm(instance=notification)
        except:
            form=NotificationForm()
            notification=None
        return render(request, 'web/notify.html',{'form': form,'notify': notification})
    
    def post(self,request):
        try:
            notification=Notification.objects.get(pk=1)
            form=NotificationForm(request.POST,instance=notification)
        except:
            form=NotificationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Notification has been successfully updated..')
            return redirect(reverse('notify'))
    

class addloc(APIView):
    authentication_classes=[SessionAuthentication,BasicAuthentication]
    def get(self, request,*args,**kwargs):
        if request.user.is_anonymous:
            return redirect(reverse('signin'))
        profile=Profile.objects.get(user=self.request.user)
        if not profile.is_admin:
            return redirect(reverse('service_home'))
        if self.kwargs['id']==0:
            form=LocationForm()
        else:
            activity=Location.objects.get(pk=self.kwargs['id'])
            form=LocationForm(instance=activity)
        return render(request, 'web/addloc.html',{'form' : form})

    def post(self, request,*args,**kwargs):
        if self.kwargs['id']==0:
            form=LocationForm(request.POST)
        else:
            activity=Location.objects.get(pk=self.kwargs['id'])
            form=LocationForm(request.POST,instance=activity)
        if form.is_valid():
            form.save()
            return redirect(reverse('editloc'))
        return render(request, 'web/addloc.html',{'form' : form})


class editloc(ListView):
    authentication_classes=[SessionAuthentication,BasicAuthentication]
    template_name='web/editloc.html'
    paginate_by=10


    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['user'] = self.request.user
        return context

    
    def get_queryset(self):
        return Location.objects.all().order_by('-id')


    def get(self,*args, **kwargs):
        if self.request.user.is_anonymous:
            return redirect(reverse('signin'))
        profile=Profile.objects.get(user=self.request.user)
        if not profile.is_admin:
            return redirect(reverse('service_home'))
        return super().get(*args, **kwargs)




class addservice(APIView):
    authentication_classes=[SessionAuthentication,BasicAuthentication]
    def get(self, request,*args,**kwargs):
        if request.user.is_anonymous:
            return redirect(reverse('signin'))
        profile=Profile.objects.get(user=self.request.user)
        if not profile.is_admin:
            return redirect(reverse('service_home'))

        if self.kwargs['id']==0:
            form=ServiceForm()
        else:
            activity=Services.objects.get(pk=self.kwargs['id'])
            form=ServiceForm(instance=activity)
        return render(request, 'web/addservice.html',{'form' : form})

    def post(self, request,*args,**kwargs):
        if request.user.is_anonymous:
            return redirect(reverse('signin'))
        if self.kwargs['id']==0:
            form=ServiceForm(request.POST)
        else:
            activity=Services.objects.get(pk=self.kwargs['id'])
            form=ServiceForm(request.POST,instance=activity)
        if form.is_valid():
            form.save()
            return redirect(reverse('viewservice'))
        return render(request, 'web/addservice.html',{'form' : form})




class viewservice(ListView):
    authentication_classes=[SessionAuthentication,BasicAuthentication]
    template_name='web/viewservice.html'
    paginate_by=10


    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['user'] = self.request.user
        return context

    
    def get_queryset(self):
        return Services.objects.all().order_by('-id')


    def get(self,*args, **kwargs):
        if self.request.user.is_anonymous:
            return redirect(reverse('signin'))
        profile=Profile.objects.get(user=self.request.user)
        if not profile.is_admin:
            return redirect(reverse('service_home'))
        return super().get(*args, **kwargs)




class viewact(ListView):
    authentication_classes=[SessionAuthentication,BasicAuthentication]
    template_name='web/editact.html'
    paginate_by=10


    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['user'] = self.request.user
        return context

    
    def get_queryset(self):
        return Activities.objects.all().order_by('service')


    def get(self,*args, **kwargs):
        if self.request.user.is_anonymous:
            return redirect(reverse('signin'))
        profile=Profile.objects.get(user=self.request.user)
        if not profile.is_admin:
            return redirect(reverse('service_home'))
        return super().get(*args, **kwargs)





class adminconsix(APIView):
    authentication_classes=[SessionAuthentication,BasicAuthentication]
    def get(self, request):
        return render(request, 'web/adminconsix.html')




# Edit routes:


class adminconv(ListView):
    authentication_classes=[SessionAuthentication,BasicAuthentication]
    template_name='web/adminconv.html'
    paginate_by=10


    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['profile'] = Profile.objects.get(user=self.request.user)
        context['id'] = self.kwargs['id']
        if self.kwargs['id']==0:
            sales=Sales.objects.all()
        if self.kwargs['id']==1:
            sales=Sales.objects.filter(has_closed=True)
        if self.kwargs['id']==2:
            sales=Sales.objects.filter(has_closed=False)
        context['converted'],context['non_converted'],context['totalsale']=get_sales_data(sales)
        return context

    
    def get_queryset(self):
        if self.kwargs['id']==0:
            return Sales.objects.all().order_by('-id')
        if self.kwargs['id']==1:
            return Sales.objects.filter(has_closed=True).order_by('-id')
        if self.kwargs['id']==2:
            return Sales.objects.filter(has_closed=False).order_by('-id')


    def get(self,*args, **kwargs):
        if self.request.user.is_anonymous:
            return redirect(reverse('signin'))
        profile=Profile.objects.get(user=self.request.user)
        if not profile.is_admin:
            return redirect(reverse('service_home'))
        return super().get(*args, **kwargs)


class adminconsix(APIView):
    def get(self, request):
        return render(request, 'web/adminconsix.html')


class admincontwe(APIView):
    def get(self, request):
        return render(request, 'web/admincontwe.html')


class errorpage(APIView):
    def get(self, request):
        return render(request, 'web/errorpage.html')


class editscat(APIView):
    authentication_classes=[SessionAuthentication,BasicAuthentication]
    def get(self, request, id):
        if request.user.is_anonymous:
            return redirect(reverse('signin'))
        profile=Profile.objects.get(user=self.request.user)
        if not profile.is_admin:
            return redirect(reverse('service_home'))
        user=User.objects.get(pk=id)
        profile=Profile.objects.get(user=user)
        form1=PassForm()
        form2=PercentageForm(initial={'percentage' : profile.percentage, 'phonenumber' : profile.phone})
        context = {
            'form1' : form1,
            'form2' : form2,
            'user'  : user,
        }
        return render(request, 'web/editscat.html',context=context)


class passupdate(APIView):
    authentication_classes=[SessionAuthentication,BasicAuthentication]
    def post(self,request,id):
        if request.user.is_anonymous:
            return redirect(reverse('signin'))
        profile=Profile.objects.get(user=self.request.user)
        if not profile.is_admin:
            return redirect(reverse('service_home'))

        form=PassForm(request.POST)
        if form.is_valid():             
            if request.POST['password'] == request.POST['confirm_password']:
                user=User.objects.get(pk=id)
                user.set_password(request.POST['password'])
                user.save()
                return redirect(reverse('viewscat'))
        return redirect(reverse('errorpg'))

class percentageupdate(APIView):
    authentication_classes=[SessionAuthentication,BasicAuthentication]
    def post(self,request,id):
        if request.user.is_anonymous:
            return redirect(reverse('signin'))
        profile=Profile.objects.get(user=self.request.user)
        if not profile.is_admin:
            return redirect(reverse('service_home'))
        form=PercentageForm(request.POST)
        if form.is_valid():             
            user=User.objects.get(pk=id)
            profile=Profile.objects.get(user=user)
            profile.phone=request.POST['phonenumber']
            profile.percentage=request.POST['percentage']
            profile.save()
            return redirect(reverse('viewscat'))
        return redirect(reverse('errorpg'))

# Admin End


# Service Dash starts


class serviceform(APIView):
    authentication_classes=[SessionAuthentication,BasicAuthentication]
    def get(self, request,id):
        if request.user.is_anonymous:
            return redirect(reverse('signin'))
        if id==0:
            form = SalesForm()
        else:
            try:
                obj=Sales.objects.get(pk=id)
            except:
                return redirect(reverse('errorpg'))
            form=SalesForm(instance=obj)
        return render(request, 'web/service/serviceform.html', {'form': form})

    def post(self, request,id):
        if request.user.is_anonymous:
            return redirect(reverse('signin'))
        if id==0:
            form = SalesForm(request.POST)
        else:
            try:
                obj=Sales.objects.get(pk=id)
            except:
                return redirect(reverse('errorpg'))
            form=SalesForm(request.POST,instance=obj)
        if form.is_valid():
            obj=form.save(commit=False)
            if id==0:
                obj.user=request.user
            obj.save()
            form.save_m2m()
            
            
            return redirect(reverse('pdf',kwargs={'id':obj.id}))


class servicehome(APIView):
    authentication_classes=[SessionAuthentication,BasicAuthentication]
    def get(self, request):
        if request.user.is_anonymous:
            return redirect(reverse('signin'))
        profile=Profile.objects.get(user=self.request.user)
        if not profile.is_sales:
            return redirect(reverse('errorpg'))
        try:
            notify=Notification.objects.get(pk=1)
        except:
            notify=None
        return render(request, 'web/service/servicehome.html',{'notify': notify})


class salesview(APIView):
    def get(self, request):
        return render(request, 'web/service/salesview.html')


class servicesalepage(ListView):
    authentication_classes=[SessionAuthentication,BasicAuthentication]
    template_name='web/service/servicesalepage.html'
    paginate_by=10


    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['profile'] = Profile.objects.get(user=self.request.user)
        context['id'] = self.kwargs['id']
        if self.kwargs['id']==0:
            sales=Sales.objects.filter(user=self.request.user)
        if self.kwargs['id']==1:
            sales=Sales.objects.filter(user=self.request.user,has_closed=True)
        if self.kwargs['id']==2:
            sales=Sales.objects.filter(user=self.request.user,has_closed=False)
        context['converted'],context['non_converted'],context['totalsale']=get_sales_data(sales)
        return context

    
    def get_queryset(self):
        if self.kwargs['id']==0:
            return Sales.objects.filter(user=self.request.user).order_by('-id')
        if self.kwargs['id']==1:
            return Sales.objects.filter(user=self.request.user,has_closed=True).order_by('-id')
        if self.kwargs['id']==2:
            return Sales.objects.filter(user=self.request.user,has_closed=False).order_by('-id')


    def get(self,*args, **kwargs):
        if self.request.user.is_anonymous:
            return redirect(reverse('signin'))
        profile=Profile.objects.get(user=self.request.user)
        if not profile.is_sales:
            return redirect(reverse('errorpg'))
        return super().get(*args, **kwargs)



class pagepdfterms(APIView):
    authentication_classes=[SessionAuthentication,BasicAuthentication]
    def get(self, request,*args, **kwargs):
        if request.user.is_anonymous:
            return redirect(reverse('signin'))
        profile=Profile.objects.get(user=self.request.user)
        if not profile.is_sales:
            return redirect(reverse('errorpg'))
        try:
            sales=Sales.objects.get(pk=self.kwargs['id'])
        except:
            return redirect(reverse('errorpg'))
        if True:
            s=sale(sales)
            s.update()
            sales=Sales.objects.get(pk=self.kwargs['id'])
        return render(request, 'web/service/pagepdfterms.html',{ 'sale' : sales })


class perfomance(APIView):
    authentication_classes=[SessionAuthentication,BasicAuthentication]
    def get(self, request):
        return render(request, 'web/service/perfomance.html')


class perfsix(APIView):
    def get(self, request):
        return render(request, 'web/service/perfsix.html')


class perftwe(APIView):
    def get(self, request):
        return render(request, 'web/service/perftwe.html')


class tagsview(ListView):
    authentication_classes=[SessionAuthentication,BasicAuthentication]
    template_name='web/service/tagsview.html'
    paginate_by=10


    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['user'] = self.request.user
        return context

    
    def get_queryset(self):
        return Activities.objects.all().order_by('service')


    def get(self,*args, **kwargs):
        if self.request.user.is_anonymous:
            return redirect(reverse('signin'))
        profile=Profile.objects.get(user=self.request.user)
        if not profile.is_sales:
            return redirect(reverse('errorpg'))
        return super().get(*args, **kwargs)




class convsix(APIView):
    def get(self, request):
        return render(request, 'web/service/convsix.html')


class convtwe(APIView):
    def get(self, request):
        return render(request, 'web/service/convtwe.html')



#helperss

class approve(APIView):
    authentication_classes=[SessionAuthentication,BasicAuthentication]
    def post(self,request,*args,**kwargs):
        if request.user.is_anonymous:
            return redirect(reverse('signin'))
        profile=Profile.objects.get(user=self.request.user)
        if not profile.is_admin:
            return redirect(reverse('service_home'))

        try:
            cat=Sales.objects.get(pk=self.kwargs['id'])
            cat.has_closed=True
            cat.save()
            return Response({'result' : True})
        except:
            return Response({'result' : False})


class deleteService(APIView):
    authentication_classes=[SessionAuthentication,BasicAuthentication]
    def post(self,request,*args,**kwargs):
        if request.user.is_anonymous:
            return redirect(reverse('signin'))
        profile=Profile.objects.get(user=self.request.user)
        if not profile.is_admin:
            return redirect(reverse('service_home'))

        try:
            cat=Services.objects.get(pk=self.kwargs['id'])
            cat.delete()
            return Response({'result' : True})
        except:
            return Response({'result' : False})


class deleteLocation(APIView):
    authentication_classes=[SessionAuthentication,BasicAuthentication]
    def post(self,request,*args,**kwargs):
        if request.user.is_anonymous:
            return redirect(reverse('signin'))
        profile=Profile.objects.get(user=self.request.user)
        if not profile.is_admin:
            return redirect(reverse('service_home'))

        try:
            cat=Location.objects.get(pk=self.kwargs['id'])
            cat.delete()
            return Response({'result' : True})
        except:
            return Response({'result' : False})

class deleteActivities(APIView):
    authentication_classes=[SessionAuthentication,BasicAuthentication]
    def post(self,request,*args,**kwargs):
        if request.user.is_anonymous:
            return redirect(reverse('signin'))
        profile=Profile.objects.get(user=self.request.user)
        if not profile.is_admin:
            return redirect(reverse('service_home'))

        try:
            cat=Activities.objects.get(pk=self.kwargs['id'])
            cat.delete()
            return Response({'result' : True})
        except:
            return Response({'result' : False})


class deleteSales(APIView):
    authentication_classes=[SessionAuthentication,BasicAuthentication]
    def post(self,request,*args,**kwargs):
        if request.user.is_anonymous:
            return redirect(reverse('signin'))
        profile=Profile.objects.get(user=self.request.user)
        if not profile.is_admin:
            return redirect(reverse('service_home'))

        try:
            cat=Sales.objects.get(pk=self.kwargs['id'])
            cat.delete()
            return Response({'result' : True})
        except:
            return Response({'result' : False})


class deleteExec(APIView):
    authentication_classes=[SessionAuthentication,BasicAuthentication]
    def post(self,request,*args,**kwargs):
        if request.user.is_anonymous:
            return redirect(reverse('signin'))
        profile=Profile.objects.get(user=self.request.user)
        if not profile.is_admin:
            return redirect(reverse('service_home'))
        try:
            profile=Profile.objects.get(pk=self.kwargs['id'])
            profile.is_sales=False
            profile.save()
            return Response({'result' : True})
        except:
            return Response({'result' : False})



class logoutpg(APIView):
    authentication_classes=[SessionAuthentication,BasicAuthentication]
    def get(self,request):
        logout(request)
        return redirect(reverse('signin'))


