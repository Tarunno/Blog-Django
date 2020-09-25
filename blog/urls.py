from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('single/', views.single, name='single'),
    path('single/<int:id>', views.single, name='single'),
    path('single/<int:id>/del/<int:del_id>', views.delete_comment, name='delete_comment'),
    path('single/<int:id>/like/<int:user>', views.like, name='like'),
    path('single/<int:id>/unlike/<int:user>', views.unlike, name='unlike')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
