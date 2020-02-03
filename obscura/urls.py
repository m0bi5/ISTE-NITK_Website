from django.urls import path,include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    path('',views.login,name='login'),
    #path('<team>/snek/',views.snake,name='hextris'),
    #path('<team>/lostp/',views.maze,name='astray'),
    #path('<team>/fbird/',views.fbird,name='fbird'),
    #path('<team>/un_med/',views.un_med,name='un_med'),
    #path('<team>/un_hard/',views.un_hard,name='un_hard'),
    #path('<team>/instructions/',views.instructions,name='instructions'),
    #path('<team>/mini_games/',views.mini_games,name='mini_games'),
    #path('<team>/',views.home,name='obs'),
    #path('<team>/quests/',views.quests_menu, name='quests_menu'),
    #path('<team>/easy/<id>',views.easy,name='easy'),
    #path('<team>/med/<id>',views.med,name='medium'),
    #path('<team>/hard/<id>',views.hard,name='hard'),
    #path('<team>/lboard',views.lboard,name='lboard')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
