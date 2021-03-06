from django.conf.urls import url
from django.conf.urls.static import static

import views

urlpatterns = [
    #url(r'^$', views.index, name='index'),
    url(r'^user/', views.RESTUser),
    url(r'^purchase/', views.RESTPurchase),
    url(r'^winner/', views.RESTWinner),
    url(r'^graph_from_name/', views.UserdataToWinner),
    url(r'^userToWinner/', views.UserdataToWinner, name="UserdataToWinner" ),
    url(r'^winnerToUser/', views.WinnerToUser, name="WinnerToUser" ),
    url(r'^winnerToConcreteUser/', views.WinnerToConcreteUser, name="WinnerToUser" ),
    url(r'^userAutocomplete/', views.UserAutocomplete, name="WinnerToUser" ),
	url(r'^winnerAutocomplete/', views.WinnerAutocomplete, name="WinnerToUser" ),
    url(r'^getTable/', views.getWinnerTable, name="getWinnerTable" ),
]