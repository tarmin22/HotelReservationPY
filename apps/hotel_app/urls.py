from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^$', views.index),
    url(r'^rooms$', views.rooms),
    url(r'^rooms/(?P<id>\d+)$', views.room_info),
    url(r'^reservation$', views.reservation),
    url(r'^calculate_subtotal$', views.calculate_subtotal),
    url(r'^total_cost$', views.total_cost),
    url(r'^payment$', views.payment),
    url(r'^enter_payment$', views.enter_payment),
    url(r'^confirmation$', views.confirmation),
    url(r'^cancel$', views.cancel),
    url(r'^change$', views.change),
    url(r'^enter_reservation$', views.enter_reservation),
    url(r'^success/(?P<id>\d+)$', views.success),
    url(r'^update$', views.update),
    url(r'^lookup$', views.lookup),
    url(r'^existing/(?P<id>\d+)$', views.existing),
    url(r'^delete/(?P<id>\d+)$', views.delete),
    url(r'^edit/(?P<id>\d+)$', views.edit),
    url(r'^reupdate$', views.reupdate),    
    url(r'^update_reservation$', views.update_reservation),    
]