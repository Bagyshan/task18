from django.urls import path
from snippets import views

urlpatterns = [
    path('without_pk/', views.snippet_list),
    path('with_pk/<int:pk>/', views.snippet_detail)
]