from django.urls import path
from .views import CatList,Catdetail
urlpatterns = [
    path('',CatList.as_view(),name="cat_list"),
    path('<int:pk>',Catdetail.as_view(),name="cat_detail"),
]