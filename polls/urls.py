from django.urls import path
#from views import episode_bcs
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('episode_bcs/int:<episode_id>', views.episode_bcs, name='episode_bcs'), 
    path('character/int:<char_id>', views.character, name='character'),
    path('search_results/', views.search_results, name='search_results'),
    path('episodesbb/int:<i>', views.episodesbb, name='episodesbb'),
    path('episodesbcs/int:<j>', views.episodesbcs, name='episodesbcs'),
]