from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from project import views
from project.views import home_view, product_detail_view, category_detail_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('product/<int:product_id>/', product_detail_view, name='product_detail'),
    path('category/<int:category_id>/', category_detail_view, name='category_detail'),
    path('product/<int:product_id>/like/', views.toggle_like, name='toggle_like'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)