# Projeto Final - Profissão: Cientista de Dados

Este repositório contém o projeto final desenvolvido como parte do curso "Profissão: Cientista de Dados" oferecido pela Escola Britânica de Artes Criativas (EBAC). O objetivo principal do projeto é criar um modelo de credit scoring para cartão de crédito, utilizando dados de 15 safras e considerando 12 meses de performance.

## Visão Geral do Projeto

O projeto abrange as seguintes etapas:

1. **Desenho Amostral:**
   
   - Utilização de 15 safras.
   - Análise baseada em 12 meses de performance.

2. **Variáveis e Pré-processamento:**
   
   - Seleção e modificação de variáveis utilizando a abordagem WOE (Weight of Evidence).
   - Tratamento de nulos através de uma pipeline no sklearn.
   - Remoção de outliers com EllipticEnvelope.
   - Seleção de variáveis usando RandomForestClassifier.
   - Aplicação de PCA para redução a 5 componentes.
   - Criação de variáveis dummy.

3. **Modelos Utilizados:**
   
   - Regressão Logística (statsmodels).
   - Pipeline no sklearn com tratamento de nulos, remoção de outliers, seleção de variáveis, PCA e criação de variáveis dummy.
   - Modelo "lightgbm" treinado utilizando o Pycaret.

4. **Validação Out of Time (OOT):**
   
   - Criação de uma base de teste com os três últimos meses para validação OOT.

5. **Aplicação Web (Streamlit):**
   
   - Disponibilidade de um arquivo "projeto_final.py" de Streamlit.
   - Permite carregar a base de dados e gerar uma planilha com os valores previstos.
     
https://github.com/brunoperdigao/Projetos-EBAC-Cientista-de-Dados/assets/57102715/c36844d5-0f48-4da6-9511-6e75a4492f00



## Estrutura do Repositório

- `data/`: Armazena os conjuntos de dados utilizados no projeto.
- `models/`: Contém os modelos salvos.
- `notebooks/`: Contém os notebooks do Jupyter utilizados durante o desenvolvimento.
- `streamlit/`: Contém o arquivo ".py" para a aplicação web utilizando Streamlit.

## Como Executar a Aplicação Web

1. Certifique-se de ter o Python instalado no seu ambiente.
2. Instale as dependências executando `pip install -r requirements.txt`.
3. Navegue até o diretório `streamlit/` e execute `streamlit run credit_scoring_app.py`.

Isso abrirá a aplicação no navegador padrão, permitindo a interação com a base de dados e visualização dos valores previstos.



## Agradecimentos

Agradeço à EBAC pela oportunidade de aprendizado e formação.
