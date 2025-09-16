from django.urls import path

from lookapp.views import HomePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),

]
