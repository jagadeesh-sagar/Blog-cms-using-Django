from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views


urlpatterns = [
                  path('', views.Home.as_view(), name='Home'),
                  path('blog/', views.Blog.as_view(), name='Blog'),
                  path('post/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
