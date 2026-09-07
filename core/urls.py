from django.urls import path
from . import views

urlpatterns = [
    path('',                  views.home,             name='home'),
    path('register/',         views.register,         name='register'),
    path('login/',            views.user_login,       name='user_login'),
    path('admin-login/',      views.admin_login,      name='admin_login'),
    path('dashboard/',        views.dashboard,        name='dashboard'),
    path('admin-dashboard/',  views.admin_dashboard,  name='admin_dashboard'),
    path('add-material/',     views.add_material,     name='add_material'),
    path('results/',          views.view_results,     name='results'),
    path('history/',          views.result_history,   name='history'),
    path('logout/',           views.logout_view,      name='logout'),
]
