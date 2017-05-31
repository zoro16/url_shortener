from django.conf.urls import url
from shortener.views import Home


urlpatterns = [
    url(r'^$', Home.as_view(), name="home-page")
]
