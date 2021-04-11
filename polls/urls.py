from django.urls import path
#from views import episode_bcs
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    #path('breakingbad/', views.breakingbad, name='breakingbad'),
    path('episode_bcs/int:<episode_id>', views.episode_bcs, name='episode_bcs'), 
    path('character/int:<char_id>', views.character, name='character'),
]