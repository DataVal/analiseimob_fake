# Análise de Dados Imobiliários

## Introdução
Este projeto tem como objetivo realizar uma análise exploratória de dados (EDA) em um conjunto de dados imobiliários. Durante a análise, foram aplicadas técnicas de tratamento de dados, detecção de outliers, otimização de tipos de dados para melhor performance e exploração visual dos dados.
Contudo por conta da limitação da ferramenta que gerou o dataset, foram encontradas limitações, principalmente em relação a aletoriedade dos dados, o que você perceberá que acabou comprometendo as etapas finais.

## Tecnologias Utilizadas
- **Python**
- **Pandas** (Manipulação de dados)
- **Matplotlib** e **Seaborn** (Visualização de dados)
- **NumPy** (Cálculos matemáticos)
- **SciPy** (Cálculo de outliers via Z-score)

## Estrutura do Projeto

O código principal está contido no arquivo `analiseimobiliaria.ipynb`.
O código que utilizei enquanto aprendia os recursos que listei acima está descrito no arquivo `analiseimobiliaria.py`.
Uma versão otimizada, refatorada e modularizada foi feita com ajuda do ChatGPT caso queira ver algo mais sucinto, está no arquivo `analiseimob_refatoradaIA.py`.


A estrutura da análise segue os seguintes passos:

1. **Carregamento dos Dados**
   - Importação do dataset
   - Visualização inicial das informações do dataframe

2. **Tratamento de Dados**
   - Remoção de colunas desnecessárias
   - Identificação e tratamento de valores ausentes

3. **Otimização dos Tipos de Dados**
   - Conversão de colunas para tipos mais eficientes (int32, category, bool, datetime64)
   - Avaliação do impacto na memória (redução de quase 70%)

4. **Identificação de Outliers**
   - Uso do método IQR (Intervalo Interquartil)
   - Uso do Z-score
   - Visualização com boxplots
     PS: Aqui comecei a notar os problemas do dataset

5. **Análise Exploratória dos Dados (EDA)**
   - Distribuição dos preços por tipo de imóvel
   - Correlação entre variáveis
   - Visualizações com scatterplots e heatmaps
     PS: EDA foi parcialmente comprometida pelos motivos que deixei claro no início

## Principais Descobertas
- O dataset não apresentava valores nulos (gerado artificialmente).
- A troca de tipos de colunas reduziu em quase **70%** o consumo de memória.
- Não foram encontrados outliers significativos.
- As distribuições dos valores eram extremamente simétricas, sugerindo que os dados não eram realistas o suficiente para uma EDA aprofundada.
- Correlações esperadas foram confirmadas, como:
  - Maior número de quartos tendendo a aumentar o valor do imóvel.
  - Maior área resultando em valores mais altos.

## Aprendizados e Considerações Finais
- O projeto serviu como um excelente exercício para consolidar conhecimentos em Pandas, Seaborn, Matplotlib, NumPy e SciPy.
- Foi possível entender a importância da otimização de tipos de dados para desempenho.
- Para futuras análises, será interessante utilizar datasets mais realistas.

## Referências
Os dados foram gerados utilizando a ferramenta [Gerador de Dados Falsos](https://gerador-dados-falsos.streamlit.app) criada por Daniel Castro. Todos os créditos ao autor.

## Como Executar o Projeto
1. Clone este repositório:
   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   ```
2. Instale as dependências necessárias:
   ```bash
   pip install pandas matplotlib seaborn numpy scipy
   ```
3. Execute o notebook em um ambiente como Jupyter Notebook ou Google Colab.

