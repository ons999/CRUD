from django.contrib import admin
from django.urls import path
from . import views
from django.shortcuts import render
urlpatterns = [
    #path('admin/', admin.site.urls),
    path('',views.add_show),
    path('thank-you/', lambda request: render(request, 'crudproject/thank_you.html'), name='thank_you'),  # Simple thank-you page
    path('delete/<int:id>/',views.delete_data,name='deletedata'),
     path('update/<int:id>/',views.update_data,name='updatedata'),

]
