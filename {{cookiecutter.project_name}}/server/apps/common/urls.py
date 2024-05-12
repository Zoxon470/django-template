from django.urls import path

from server.apps.common.views import index

app_name = 'common'

urlpatterns = [
    path('', index, name='index'),
]
