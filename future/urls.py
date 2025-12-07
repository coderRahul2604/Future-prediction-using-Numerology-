from django.contrib import admin
from django.urls import path
from future import views

urlpatterns = [

    path('dateInfo1/', views.dateInfo1),
    path('dateInfo2/', views.dateInfo2),
    path('dateInfo3/', views.dateInfo3),
    path('dateInfo4/', views.dateInfo4),
    path('dateInfo1/numberinfo1/', views.numberinfo1),
    path('dateInfo2/numberinfo2/', views.numberinfo2),
    path('dateInfo3/personalYear/', views.numberinfo3),
    path('dateInfo4/loShuGrid/', views.loShuGrid),

]