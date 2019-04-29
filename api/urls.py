from django.conf.urls import url
from .views import alpha, beta

urlpatterns = [
  url(r'^a/?$', alpha.View_A.as_view(), name='view_a'),
  url(r'^b/?$', beta.view_b, name='view_b'),
]