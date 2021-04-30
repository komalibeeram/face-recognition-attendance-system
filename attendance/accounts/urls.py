from django.urls import path
from . import views
from .views import home
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
app_name = 'accounts'
urlpatterns =[
    path('home-page/', views.home, name='home-page'),
    path('profile/', views.profile, name='profile'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)