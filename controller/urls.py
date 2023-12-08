from django.urls import path , include

from . import views
urlpatterns = [
    path('UpdateRelay', views.UpdateRelay.as_view()),
    path('Login', views.Login.as_view()),
    path('InsertData', views.InsertData.as_view()),
    path('GetAllData', views.GetAllData.as_view()),
    path('SendNotification', views.SendNotification.as_view()),
]