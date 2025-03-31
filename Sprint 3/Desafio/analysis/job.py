import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# =============================================
# CONFIGURAÇÕES GERAIS
# =============================================
sns.set_theme(style="darkgrid")
plt.rcParams["font.family"] = "DejaVu Sans"
plt.rcParams["axes.titlesize"] = 16
plt.rcParams["axes.labelsize"] = 12
COLOR_PALETTE = sns.color_palette("viridis")

# =============================================
# FUNÇÃO DE PROCESSAMENTO DE DADOS
# =============================================
def process_data(csv_path):
    """Carrega e prepara os dados"""
    df = pd.read_csv(csv_path)
    
    # Converter colunas numéricas
    numeric_cols = ["Actual gross", "Adjusted gross (in 2022 dollars)", "Average gross"]
    for col in numeric_cols:
        df[col] = df[col].astype(str).str.replace("[^\d.]", "", regex=True)
        df[col] = pd.to_numeric(df[col], errors="coerce")
    
    # Calcular faturamento por show ajustado
    df["Per Show Adjusted"] = df["Adjusted gross (in 2022 dollars)"] / df["Shows"]
    
    return df

# =============================================
# RESPOSTAS DAS QUESTÕES (Q1-Q3)
# =============================================
def answer_questions(df):
    """Responde às questões analíticas"""
    # Q1 - Artista mais frequente com maior média
    artist_stats = df.groupby("Artist").agg(
        Appearances=("Rank", "count"),
        Avg_Actual_Gross=("Actual gross", "mean"),
    ).reset_index()
    q1 = artist_stats.sort_values(["Appearances", "Avg_Actual_Gross"], ascending=[False, False]).iloc[0]

    # Q2 - Turnê com maior média em um único ano
    single_year = df[df["Start year"] == df["End year"]]
    q2 = single_year.loc[single_year["Average gross"].idxmax()]

    # Q3 - Top 3 shows mais lucrativos
    q3 = df.sort_values("Per Show Adjusted", ascending=False).head(3)
    
    return q1, q2, q3

# =============================================
# GERAÇÃO DE GRÁFICOS (Q4-Q5)
# =============================================
def generate_visualizations(df, top_artist):
    """Gera visualizações profissionais"""
    # --------------- Q4 (Gráfico de Linhas) ---------------
    plt.figure(figsize=(12, 6))
    artist_data = df[df["Artist"] == top_artist].sort_values("Start year")
    
    ax = sns.lineplot(
        x="Start year",
        y="Actual gross",
        data=artist_data,
        marker="o",
        markersize=10,
        linewidth=2.5,
        color="#2ecc71"
    )
    
    # Formatação
    plt.title(f"Evolução do Faturamento - {top_artist}\n", pad=20)
    ax.set(
        xlabel="Ano", 
        ylabel="Faturamento (USD)",
        xticks=artist_data["Start year"].unique(),
        ylim=(0, artist_data["Actual gross"].max() * 1.1)
    )
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f"${x/1e6:,.0f}M"))
    
    # Anotações
    for x, y in zip(artist_data["Start year"], artist_data["Actual gross"]):
        ax.text(
            x, y * 1.02,  
            f"${y/1e6:,.0f}M", 
            ha="center", 
            va="bottom",
            fontsize=10,
            fontweight="bold"
        )
    
    plt.savefig("/app/data/Q4.png", dpi=300, bbox_inches="tight")
    plt.close()

    # --------------- Q5 (Gráfico de Barras) ---------------
    plt.figure(figsize=(12, 6))
    top_artists = df.groupby("Artist")["Shows"].sum().nlargest(5).reset_index()
    
    ax = sns.barplot(
        x="Artist",
        y="Shows",
        data=top_artists,
        palette=COLOR_PALETTE,
        edgecolor="black",
        width=0.7
    )
    
    # Formatação
    plt.title("Top 5 Artistas por Total de Shows\n", pad=20)
    ax.set(
        xlabel="", 
        ylabel="Total de Shows",
        ylim=(0, top_artists["Shows"].max() * 1.1)
    )
    plt.xticks(rotation=25, ha="right", fontsize=12)
    
    # Anotações
    for p in ax.patches:
        ax.annotate(
            f"{int(p.get_height())}",
            (p.get_x() + p.get_width() / 2., p.get_height()),
            ha="center", 
            va="center",
            xytext=(0, 10),
            textcoords="offset points",
            fontsize=12,
            fontweight="bold"
        )
    
    plt.savefig("/app/data/Q5.png", dpi=300, bbox_inches="tight")
    plt.close()

# =============================================
# SALVAMENTO DAS RESPOSTAS
# =============================================
def save_answers(q1, q2, q3):
    """Salva as respostas em formato texto"""
    with open("/app/data/respostas.txt", "w", encoding="utf-8") as f:
        f.write(f"Q1:\n--- {q1['Artist']} (Aparições: {q1['Appearances']}, ")
        f.write(f"Média: ${q1['Avg_Actual_Gross']/1e6:,.1f}M\n\n")
        
        f.write(f"Q2:\n--- {q2['Tour title']} ({q2['Start year']}), ")
        f.write(f"Média/Show: ${q2['Average gross']/1e6:,.1f}M\n\n")
        
        f.write("Q3:\n")
        for _, row in q3.iterrows():
            f.write(f"--- {row['Artist']}: {row['Tour title']} ")
            f.write(f"(USD ${row['Per Show Adjusted']/1e6:,.1f}M/show)\n")

# =============================================
# EXECUÇÃO PRINCIPAL
# =============================================
if __name__ == "__main__":
    print("🚀 Iniciando processamento...")
    try:
        # Carregar e processar dados
        df = process_data('/app/data/csv_limpo.csv')  # Lê do subdiretório
        
        # Gerar respostas
        q1, q2, q3 = answer_questions(df)
        
        # Criar visualizações
        generate_visualizations(df, q1["Artist"])
        
        # Salvar resultados
        save_answers(q1, q2, q3)
        
        print("✅ Concluído com sucesso!")
        print("Arquivos gerados:")
        print("- Q4.png (Gráfico de evolução)")
        print("- Q5.png (Gráfico de comparação)")
        print("- respostas.txt")
        
    except Exception as e:
        print(f"❌ Erro: {str(e)}")