from django.conf.urls import url
from . import views
from shop.views import NewView, BasicView, SaleView
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^shop/', views.shopping, name='shopping'),
    url(r'^search-new/', login_required(redirect_field_name='', login_url='/login')(NewView.as_view())),
    url(r'^search-basic/', login_required(redirect_field_name='', login_url='/login')(BasicView.as_view())),
    url(r'^search-sale/', login_required(redirect_field_name='', login_url='/login')(SaleView.as_view())),
    url(r'^reg/', views.registration, name='registration'),
    url(r'^login/', views.log, name='login'),
    url(r'^logout/', views.logout_view, name='logout'),
    url(r'^login/$', auth_views.login),
]