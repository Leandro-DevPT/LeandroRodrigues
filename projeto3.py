import os
import pandas as pd
from datetime import datetime

# ==========================================
# Projeto: Script em Python
# Especificação: Processamento básico de dados
# e automação de tarefas repetitivas.
# ==========================================

# Função para carregar dados CSV
def carregar_dados(caminho_arquivo):
    if os.path.exists(caminho_arquivo):
        try:
            df = pd.read_csv(caminho_arquivo)
            print(f"Arquivo '{caminho_arquivo}' carregado com sucesso!\n")
            return df
        except Exception as e:
            print(f"Erro ao carregar arquivo: {e}")
    else:
        print("Arquivo não encontrado!")
    return None

# Função de limpeza de dados (remoção de nulos e duplicados)
def limpar_dados(df):
    df_limpo = df.dropna().drop_duplicates()
    print("Dados limpos (nulos e duplicados removidos).\n")
    return df_limpo

# Função para gerar estatísticas básicas
def estatisticas_basicas(df):
    print("===== Estatísticas Básicas =====")
    print(df.describe(include='all'))
    print("\n")

# Função para salvar os dados processados
def salvar_dados(df, nome_arquivo="dados_processados.csv"):
    df.to_csv(nome_arquivo, index=False)
    print(f"Arquivo salvo como {nome_arquivo}\n")

# Automação simples: gerar log de execução
def gerar_log(mensagem, nome_arquivo="log_execucao.txt"):
    with open(nome_arquivo, "a", encoding="utf-8") as f:
        f.write(f"[{datetime.now()}] {mensagem}\n")
    print("Log atualizado.\n")

# Execução principal
def main():
    caminho = "dados.csv"  # Nome do arquivo de entrada

    # Carregar
    df = carregar_dados(caminho)
    if df is None:
        return

    # Limpar
    df = limpar_dados(df)

    # Estatísticas
    estatisticas_basicas(df)

    # Salvar
    salvar_dados(df)

    # Registrar no log
    gerar_log("Processamento concluído com sucesso!")


if __name__ == "__main__":
    main()
