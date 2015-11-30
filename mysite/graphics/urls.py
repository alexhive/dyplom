from django.conf.urls import url
from django.conf.urls.static import static

from . import views

urlpatterns = [
    #url(r'^$', views.index, name='index'),
    url(r'^request/', views.GraphicRequest, name='index'),
    url(r'^graph/', views.GraphicRequest, name="graph" ),
    url(r'^draw_by_user_by_name/', views.returnForUserD3JS, name="returnForUserD3JS" ),
    url(r'^draw_by_winner_by_name/', views.returnForwinnerD3JS, name="returnForwinnerD3JS" ),
]