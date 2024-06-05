from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='home'),
    path('hesabim/', views.hesabim, name='hesap'),
    path('category/<str:category_name>/', views.category_detail, name='category_detail'),
    path('sozlesme/', views.sozlesme, name='sozlesme'),
    path('hakkimizda/', views.about_view, name='about'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
