from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # URLs Públicas
    path('', views.home_view, name='home'),
    path('evento/<str:codigo_acesso>/', views.responder_evento_view, name='responder_evento'),
    path('sucesso/', views.sucesso_view, name='sucesso'),

    # URLs de Autenticação (Organizador)
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # URLs do Dashboard (Organizador)
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('dashboard/evento/<int:evento_id>/', views.detalhe_evento_dashboard_view, name='detalhe_evento'),
]