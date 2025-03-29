from django.urls import path
from.import views

from django.contrib import admin




urlpatterns = [
    path('', views.index, name='index'),
    path('about',views.about, name='about'),
    path('postypauchim',views.postypauchim, name='postypauchim'),
    path('roditeli',views.roditeli, name='roditeli'),
    path('registr',views.registr, name='registr'),
    path('vxod',views.vxod, name='vxod'),
    path('ychiteluam',views.ychiteluam, name='ychiteluam'),
    path('contakt',views.contakt, name='contakt'),

    path('admin/', admin.site.urls)

] 

