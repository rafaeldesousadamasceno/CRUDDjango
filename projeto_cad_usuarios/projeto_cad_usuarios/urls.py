from django.urls import path
from app_cad_usuarios import views

urlpatterns = [
    # ESTRUTURA(ROTA, VIEW, NOME_REFERÊNCIA)
    path('', views.home, name='home'),
    path('usuarios/', views.usuarios, name='listagem_usuarios')
]
