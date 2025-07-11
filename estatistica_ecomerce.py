import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html

# Carregar dados
df = pd.read_csv('ecommerce_estatistica.csv')
if 'Unnamed: 0' in df.columns:
    df = df.drop('Unnamed: 0', axis=1)

# Top 10 Marcas por Quantidade Vendida
marca_vendas = df.groupby('Marca')['Qtd_Vendidos_Cod'].sum().sort_values(ascending=False).head(10)

# Top 10 Materiais por Nota Média
nota_material = df.groupby('Material')['Nota'].mean().sort_values(ascending=False).head(10)

# Distribuição de produtos por Temporada
temporada_counts = df['Temporada'].value_counts()

# Iniciar o app Dash
app = Dash(__name__)

app.layout = html.Div([
    html.H1('Dashboard E-commerce: Insights Reais'),

    # Gráfico 1: Barras - Top Marcas por Vendas
    dcc.Graph(
        figure=px.bar(
            x=marca_vendas.index, y=marca_vendas.values,
            title='Top 10 Marcas por Quantidade Vendida',
            labels={'x': 'Marca', 'y': 'Quantidade Vendida'},
            color=marca_vendas.values, color_continuous_scale='Blues'
        )
    ),

    # Gráfico 2: Barras - Nota Média por Material
    dcc.Graph(
        figure=px.bar(
            x=nota_material.index, y=nota_material.values,
            title='Top 10 Materiais por Nota Média',
            labels={'x': 'Material', 'y': 'Nota Média'},
            color=nota_material.values, color_continuous_scale='Viridis'
        )
    ),

    # Gráfico 3: Dispersão - Preço x Quantidade Vendida
    dcc.Graph(
        figure=px.scatter(
            df, x='Preço', y='Qtd_Vendidos_Cod',
            title='Relação entre Preço e Quantidade Vendida',
            labels={'Preço': 'Preço (R$)', 'Qtd_Vendidos_Cod': 'Quantidade Vendida'},
            color='Nota', size='N_Avaliações', hover_data=['Título'],
            color_continuous_scale='Plasma'
        )
    ),

    # Gráfico 4: Pizza - Produtos por Temporada
    dcc.Graph(
        figure=px.pie(
            names=temporada_counts.index, values=temporada_counts.values,
            title='Distribuição de Produtos por Temporada',
            color_discrete_sequence=px.colors.sequential.RdBu
        )
    ),

    # Gráfico 5: Dispersão - Número de Avaliações x Nota Média
    dcc.Graph(
        figure=px.scatter(
            df, x='N_Avaliações', y='Nota',
            title='Relação entre Número de Avaliações e Nota Média',
            labels={'N_Avaliações': 'Número de Avaliações', 'Nota': 'Nota Média'},
            color='Gênero', hover_data=['Título'],
            opacity=0.6
        )
    ),
])

if __name__ == '__main__':
    app.run(debug=True)
