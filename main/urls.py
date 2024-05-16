from django.urls import path
from . import views

app_name="main"

urlpatterns = [
    path('', views.main, name="main"),
    path('<int:question_id>/', views.detail, name="detail"),
    path('answer/create/<int:question_id>/', views.answer_create, name="answer_create"),
]