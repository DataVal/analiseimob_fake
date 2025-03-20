# -*- coding: utf-8 -*-
""" Análise de Dados Imobiliários """

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy.stats import zscore

# ------------------------------ 1️⃣ Carregamento dos Dados ------------------------------

def carregar_dados(caminho):
    """Carrega o dataset e exibe as primeiras informações"""
    df = pd.read_csv(caminho)
    print("📌 Primeiras Linhas:")
    print(df.head(), "\n")
    print("📌 Informações Gerais:")
    print(df.info(), "\n")
    print("📌 Estatísticas Básicas:")
    print(df.describe(), "\n")
    return df

# ------------------------------ 2️⃣ Limpeza de Dados ------------------------------

def limpar_dados(df):
    """Remove colunas irrelevantes e trata valores ausentes"""
    colunas_para_remover = ["CPF", "Endereço do Imóvel"]
    df.drop(columns=colunas_para_remover, inplace=True)

    # Remover linhas com valores nulos
    df.dropna(inplace=True)

    return df

# ------------------------------ 3️⃣ Otimização de Tipos ------------------------------

def otimizar_tipos(df):
    """Converte colunas para tipos mais eficientes e reduz o uso de memória"""

    # Medir memória antes
    memoria_antes = df.memory_usage(deep=True).sum() / 1024**2

    # Conversões numéricas
    colunas_int = ["Área do Imóvel (m²)", "Valor do Imóvel", "Número de Quartos",
                   "Número de Banheiros", "Valor do Condomínio", "Ano de Construção"]
    df[colunas_int] = df[colunas_int].astype("int32")

    # Conversões booleanas
    colunas_binarias = ["Tem Piscina?", "Tem Garagem?", "Tem Elevador?", "Condomínio Fechado?"]
    df[colunas_binarias] = df[colunas_binarias].apply(lambda x: x.map({"Sim": True, "Não": False}))
    df[colunas_binarias] = df[colunas_binarias].astype("bool")

    # Conversões categóricas
    colunas_categoricas = ["Tipo de Imóvel", "Tipo de Oferta"]
    df[colunas_categoricas] = df[colunas_categoricas].astype("category")

    # Conversão de datas
    df["Data da Última Reforma"] = pd.to_datetime(df["Data da Última Reforma"], errors="coerce")

    # Medir memória depois
    memoria_depois = df.memory_usage(deep=True).sum() / 1024**2
    economia = ((memoria_antes - memoria_depois) / memoria_antes) * 100
    print(f"📉 Redução de memória: {economia:.2f}%")

    return df

# ------------------------------ 4️⃣ Identificação de Outliers ------------------------------

def detectar_outliers(df, coluna):
    """Identifica outliers usando o método do IQR"""
    Q1 = df[coluna].quantile(0.25)
    Q3 = df[coluna].quantile(0.75)
    IQR = Q3 - Q1

    limite_inferior = Q1 - 1.5 * IQR
    limite_superior = Q3 + 1.5 * IQR

    outliers = df[(df[coluna] < limite_inferior) | (df[coluna] > limite_superior)]
    print(f"⚠️ Outliers na coluna {coluna}: {outliers.shape[0]}")

    return outliers

def plotar_boxplot(df, coluna):
    """Plota um boxplot para visualizar outliers"""
    plt.figure(figsize=(10, 5))
    sns.boxplot(x=df[coluna])
    plt.title(f"Boxplot de {coluna}")
    plt.show()

# ------------------------------ 5️⃣ Análise Exploratória (EDA) ------------------------------

def analisar_precos(df):
    """Analisa a distribuição dos preços por tipo de imóvel"""
    plt.figure(figsize=(12, 6))
    sns.boxplot(x="Tipo de Imóvel", y="Valor do Imóvel", data=df)
    plt.xticks(rotation=45)
    plt.title("Distribuição dos preços por tipo de imóvel")
    plt.show()

    plt.figure(figsize=(12, 6))
    sns.barplot(x="Tipo de Imóvel", y="Valor do Imóvel", data=df, estimator=np.mean, errorbar=None)
    plt.xticks(rotation=45)
    plt.title("Média de preços por tipo de imóvel")
    plt.show()

def analisar_correlacao(df):
    """Plota um heatmap para visualizar a correlação entre variáveis"""
    plt.figure(figsize=(10,6))
    sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm", fmt=".2f")
    plt.title("Mapa de Correlação")
    plt.show()

def scatterplot_variaveis(df, x, y):
    """Plota um scatterplot para analisar relações entre variáveis"""
    plt.figure(figsize=(10,6))
    sns.scatterplot(x=x, y=y, data=df)
    plt.title(f"Relação entre {x} e {y}")
    plt.show()

# ------------------------------ 6️⃣ Execução ------------------------------

if __name__ == "__main__":
    # Caminho do dataset
    caminho_arquivo = "/content/sample_data/dados_falsos_Imobiliário.csv"

    # Carregamento e limpeza
    df = carregar_dados(caminho_arquivo)
    df = limpar_dados(df)

    # Otimização de tipos
    df = otimizar_tipos(df)

    # Identificação de outliers
    outliers_valor = detectar_outliers(df, "Valor do Imóvel")
    plotar_boxplot(df, "Valor do Imóvel")

    # Análise Exploratória
    analisar_precos(df)
    analisar_correlacao(df)
    scatterplot_variaveis(df, "Área do Imóvel (m²)", "Valor do Imóvel")
    scatterplot_variaveis(df, "Número de Quartos", "Valor do Imóvel")
