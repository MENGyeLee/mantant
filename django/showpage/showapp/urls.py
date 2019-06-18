from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^main/$',views.main),
    url(r'^db$',views.db),
    url(r'^tq$',views.tq),
    url(r'^jd$',views.jd),
    url(r'^tb$',views.tb),
]

