from django.urls import path
from app import views

urlpatterns = [
    path('', views.index, name="Home"),
    path('intensity', views.chart_intensity, name="intensity"),
    path('likelihood', views.chart_likelihood, name="likelihood"),
    path('relevance', views.chart_relevance, name="relevance"),
    path('country', views.chart_country, name="country"),
    path('topic', views.chart_topic, name="topic"),
    path('region', views.chart_region, name="region"),
    path('country', views.chart_country, name="country"),
]
