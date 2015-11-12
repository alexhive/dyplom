from django.conf.urls import url
from django.conf.urls.static import static

from . import views

urlpatterns = [
    #url(r'^$', views.index, name='index'),
    url(r'^request/', views.GraphicRequest, name='index'),
    url(r'^graph/', views.GraphicRequest, name="graph" ),
    url(r'^draw_by_name/', views.returnD3JS, name="graphByName" ),
]