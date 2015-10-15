from django.conf.urls import url

from whatpageofsearchamion import views

urlpatterns = [
    url(r'^$',views.create_search),
]
