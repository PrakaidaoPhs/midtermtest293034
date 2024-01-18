from django.urls import path
from . import views
urlpatterns = [
    # path('',views.home),
    path('',views.list),
    path('add',views.add),
    path('edit',views.edit),
    path('manage',views.manage),
    path('list',views.list),
    path('delete/<int:pk>',views.delete_place),
]