"""
URL configuration for Recruitments project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from forms import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('new_form/', views.new_form, name='new_form'),
    path('new_form/<int:form_id>/', views.new_form, name='new_form'),
    # path('new_form_submit/', views.form_submit, name='new_form_submit'),
    path('form/<int:form_id>', views.form_view, name='form_view'),
    path('form/<int:form_id>/entries/', views.form_entries, name='form_entries'),
    path('form/<int:form_id>/entries/export/', views.form_entries_export, name='form_entries_export'),
    path('all_forms/', views.all_forms, name='all_forms'),
    path('create_form/', views.create_form, name='create_form'),
    path('form_details/<int:form_id>/', views.form_detail, name='form_details'),
    path('edit_form_fields/<int:form_id>/', views.edit_form_fields, name='edit_form_fields'),
    path('', views.home, name='home'),
    path('all-entries/', views.all_entries, name='all_entries'),
    path('entry/<int:entry_id>/', views.entry_detail, name='entry_detail'),
    path('entry/delete/<int:entry_id>/', views.delete_entry, name='delete_entry'),
    path('entry/<int:entry_id>/notes/', views.save_notes, name='edit_entry_notes'),
    path('entry/<int:entry_id>/feedback/', views.save_feedback, name='edit_entry_feedback'),
    path('entry/<int:entry_id>/status/', views.change_form_status, name='change_status'),
    path('accounts/', include('allauth.urls')),
    path('user_social', views.user_social, name='user_social'),
    path('close/', views.close, name='close'),

]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)