from django.urls import path, include, re_path
from web import views

urlpatterns = [
    # Main Dash
    path('', views.index.as_view(),name='admin_home'),
    path('login/', views.loginpg.as_view(),name='signin'),
    # path('signup/', views.signup.as_view()),
    path('addscat/', views.addscat.as_view()),
    path('viewscat/', views.viewscat.as_view(),name='viewscat'),
    path('<int:id>/activity/', views.activity.as_view(),name='activity'),
    path('salesup/', views.salesup.as_view()),
    path('nonconvert/', views.nonconvert.as_view()),
    path('notify/', views.notify.as_view(),name='notify'),
    path('<int:id>/addloc/', views.addloc.as_view(),name='addloc'),
    path('editloc/', views.editloc.as_view(),name='editloc'),
    path('<int:id>/addservice/', views.addservice.as_view(),name='addservice'),
    path('viewservice/', views.viewservice.as_view(),name='viewservice'),

    path('<int:id>/adminconv/', views.adminconv.as_view(),name='adminconv'),
    path('adminconsix/', views.adminconsix.as_view()),
    path('admincontwe/', views.admincontwe.as_view()),

    path('errorpage/', views.errorpage.as_view(),name='errorpg'),



    # Main Edit Routes

    path('viewact/', views.viewact.as_view(),name='viewact'),
    path('<int:id>/editscat/', views.editscat.as_view(),name='editscat'),
    path('<int:id>/passupdate/', views.passupdate.as_view(),name='passupdate'),
    path('<int:id>/percentageupdate/', views.percentageupdate.as_view(),name='percentageupdate'),




    # Service Exe Dash

    path('<int:id>/serviceform/', views.serviceform.as_view(),name='salesform'),
    path('servicehome/', views.servicehome.as_view(),name='service_home'),
    path('salesview/', views.salesview.as_view()),

    path('<int:id>/pagepdfterms/', views.pagepdfterms.as_view(),name='pdf'),

    path('tagsview/', views.tagsview.as_view()),

    # Perfomance routes
    path('perfomance/', views.perfomance.as_view()),
    path('perfsix/', views.perfsix.as_view()),
    path('perftwe/', views.perftwe.as_view()),

    # Converted sale routes
    path('<int:id>/servicesalepage/', views.servicesalepage.as_view(),name='servicepage'),
    path('convsix/', views.convsix.as_view()),
    path('convtwe/', views.convtwe.as_view()),


    #helpers

    path('logout', views.logoutpg.as_view(),name='logoutpg'),
    path('<int:id>/approve', views.approve.as_view(),name='approve'),
    path('<int:id>/deletelocation', views.deleteLocation.as_view(),name='deleteLocation'),
    path('<int:id>/deleteservice', views.deleteService.as_view(),name='deleteService'),
    path('<int:id>/deleteactivity', views.deleteActivities.as_view(),name='deleteActivities'),
    path('<int:id>/deletesales', views.deleteSales.as_view(),name='deleteSales'),
    path('<int:id>/deleteexec',views.deleteExec.as_view(),name='deleteExec'),
    


]
