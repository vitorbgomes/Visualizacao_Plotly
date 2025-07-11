📊 Dashboard Interativo de E-commerce com Dash e Plotly
🚀 Descrição do Projeto
Este projeto apresenta um dashboard interativo para análise de dados de e-commerce, desenvolvido com Dash e Plotly em Python. O objetivo é transformar dados brutos de vendas, avaliações e características de produtos em insights visuais claros e estratégicos para a tomada de decisão.

O dashboard permite explorar diferentes aspectos do negócio, como o desempenho de marcas, as preferências de materiais pelos clientes, a sazonalidade de produtos, a relação entre preço e volume de vendas, entre outros. As visualizações foram cuidadosamente escolhidas para entregar valor real ao gestor, indo além de gráficos genéricos e facilitando a identificação de oportunidades e gargalos operacionais.

✨ Funcionalidades Principais
O dashboard oferece uma análise completa através dos seguintes gráficos interativos:

Top 10 Marcas por Quantidade Vendida: Identifica facilmente as marcas que são líderes de venda.

Top 10 Materiais por Nota Média: Descobre quais materiais são mais bem avaliados pelos clientes, indicando preferências de qualidade.

Relação entre Preço e Quantidade Vendida: Analisa o impacto do preço nas vendas e identifica padrões de consumo.

Distribuição de Produtos por Temporada: Visualiza a sazonalidade dos produtos para otimizar estoques e campanhas de marketing.

Relação entre Número de Avaliações e Nota Média: Avalia a confiança e a reputação dos produtos com base no feedback dos usuários.

Cada gráfico é totalmente interativo, permitindo aplicar zoom, selecionar dados específicos e filtrar informações diretamente pelo navegador.

🛠️ Como Usar
Para executar este projeto localmente, siga os passos abaixo.

Pré-requisitos
Python 3.8 ou superior

pip (gerenciador de pacotes do Python)

Instalação
Clone o repositório:

bash
git clone https://github.com/seu-usuario/nome-do-repositorio.git
cd nome-do-repositorio
Crie e ative um ambiente virtual (recomendado):

bash
# Para Windows
python -m venv .venv
.\.venv\Scripts\activate

# Para macOS/Linux
python3 -m venv .venv
source .venv/bin/activate
Instale as dependências:

bash
pip install -r requirements.txt
Execute a aplicação:

Certifique-se de que o arquivo ecommerce_estatistica.csv está na raiz do projeto.

Inicie o servidor Dash:

bash
python app.py
Acesse o dashboard:
Abra seu navegador e acesse o endereço http://127.0.0.1:8050/.