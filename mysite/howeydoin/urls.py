from . import views
from django.urls import path

app_name = 'home'

urlpatterns = [
    path('', views.index, name="index"),
    path('<int:item_id>', views.detail, name="detail"),
    path('recipes/', views.allrecipes, name="allrecipes"),
    path('aboutus/', views.aboutus, name="aboutus"),
    path('download/<int:id>/', views.download, name="download"),
    path('questions', views.questions, name="questions"),
    path('add', views.create_item, name='create_item'),
]