from django.conf.urls import url

from . import views

urlpatterns = [
    url(
        regex=r'^(?P<username>[\w.@+-]+)/$',
        view=views.GameDashboardView.as_view(),
        name='dashboard'
    ),
]
