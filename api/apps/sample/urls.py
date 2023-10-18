from django.urls import include, path

from .views import SampleView

urlpatterns = [path("", SampleView.as_view())]
