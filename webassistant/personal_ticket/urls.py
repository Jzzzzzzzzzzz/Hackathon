from django.urls import path
from .views import *

urlpatterns = [
    path('', profile_ticket_list, name="profile_ticket_list"),
    path('ticket/<int:ticket_id>/close/', close_ticket, name='close_ticket'),
    path("create_ticket/",create_ticket,name="create_ticket"),
    path('ticket/<int:ticket_id>/', ticket_detail_view, name='ticket_detail'),


]