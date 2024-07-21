from django.urls import path

from . import views

app_name = 'manage'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('vendor_list', views.VendorListView.as_view(), name='vendor_list'),
    path('vendor_list/vendor', views.VendorFormView.as_view(), name='vendor_form'),
    path('event_list', views.EventListView.as_view(), name='event_list'),
    path('event_list/event', views.EventFormView.as_view(), name='event_form'),
    path('event_list/vendor_list', views.EventVendorListView.as_view(), name='event_vendor_list'),
]
