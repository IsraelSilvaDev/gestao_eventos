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
    path('dashboard/estatisticas/', views.estatisticas_dashboard_view, name='estatisticas'),
    path('dashboard/evento/<int:evento_id>/', views.detalhe_evento_dashboard_view, name='detalhe_evento'),

    # URLS  Criar Evento
    path('dashboard/criar/', views.criar_evento_view, name='criar_evento'),
    path('dashboard/evento/<int:evento_id>/editar/', views.editar_evento_view, name='editar_evento'),
    
    # URLs de Convites
    path('dashboard/evento/<int:evento_id>/convites/', views.gerenciar_convites_view, name='gerenciar_convites'),
    path('dashboard/evento/<int:evento_id>/convites/criar/', views.criar_convites_multiplos_view, name='criar_convites_multiplos'),
    path('dashboard/convite/<int:convite_id>/excluir/', views.excluir_convite_view, name='excluir_convite'),
    path('dashboard/convite/<int:convite_id>/link/', views.gerar_link_convite_view, name='gerar_link_convite'),
]