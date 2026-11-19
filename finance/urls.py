from django.urls import path

from finance.views import cartoes_parcelas, index, planejamento_mensal, receitas_despesas


urlpatterns = [
    path('', index),
    path('cartoes_parcelas/', cartoes_parcelas, name='cartoes_parcelas'),
    path('planejamento_mensal/', planejamento_mensal, name='planejamento_mensal'),
    path('receitas_despesas/', receitas_despesas, name='receitas_despesas'),
]
