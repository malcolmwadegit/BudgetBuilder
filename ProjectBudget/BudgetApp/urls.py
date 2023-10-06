from django.urls import path
from . import views
from django.urls import path 
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.home, name = "home" ),
    path('newbudget/', views.new_budget, name = "newbudget"),
    path('newcategory/', views.new_category, name = "newcategory"), 
    path('newitem/', views.new_line_item, name = "newitem"),  
]


# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)