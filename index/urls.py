from django.urls import path

from . import views

app_name = 'index'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('check_in', views.CheckInView.as_view(), name='check_in'),
    path('fast_check_in', views.FastCheckInView.as_view(), name='fast_check_in'),
    # path('comment/item/<int:item_id>/<int:comment_id>', views.ReplyView.as_view(), name='reply'),
]
