from django.urls import path

from .views import *

urlpatterns = [
    # path('', BookListApiView.as_view()),
    # path('updatedelete/<int:pk>/', RetrieveUpdateDestroyApiView.as_view()),
    path('', ListAPIView.as_view()),
    path('<int:pk>/', DetailAPIView.as_view())
]