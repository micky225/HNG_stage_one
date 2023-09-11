from django.urls import re_path as url
from .views import StageOne

urlpatterns = [
    url(r'api', StageOne.as_view())
]