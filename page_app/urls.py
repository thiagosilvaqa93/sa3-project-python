from django.urls import path
from page_app.views import index, contato, sobre

urlpatterns = [
    path('', index), # URL padrão que direciona para a view index

    path('contato/', contato), # URL que direciona para a view contato

    path('about/', sobre), # URL que direciona para a view sobre
]
