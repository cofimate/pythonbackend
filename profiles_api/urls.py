from django.urls import path, include

from rest_framework.routers import DefaultRouter

from profiles_api import views

router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, basename='hello-viewset')

"""     path('hello-view', views.HelloViewSet.as_view()),   """

urlpatterns = [
    path('', include(router.urls)),
]
