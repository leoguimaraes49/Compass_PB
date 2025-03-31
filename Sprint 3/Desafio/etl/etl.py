import pandas as pd
import re

def clean_tour_title(title):
    #Separar palavras coladas (ex: "ErasTour" → "Eras Tour", "Cartershow" → "Carter Show")
    title = re.sub(
        r'(?<=[a-zÀ-ÿ])(?=[A-ZÀ-Ÿ])|(?<=[A-ZÀ-Ÿ]{2})(?=[A-ZÀ-Ÿ][a-zÀ-ÿ])', 
        ' ', 
        title
    )
    
    # Passo 2: Remover caracteres não alfabéticos no final (ex: "Tour a" → "Tour")
    title = re.sub(r'[^a-zA-ZÀ-ÿ&]\s*$', '', title)
       
    # Padronizar espaços e remover caracteres especiais
    title = re.sub(r'[^a-zA-ZÀ-ÿ&()\- ]', ' ', title)
    title = re.sub(r'\s+', ' ', title).strip()

    title = re.sub(r'\s[a-zA-ZÀ-ÿ]\s*$', '', title)  # Remove letras isoladas no final
    
    return title

def clean_data(input_path, output_path):
    # Ler CSV com codificação UTF-8
    df = pd.read_csv(input_path, encoding='utf-8')

    # Renomear colunas
    df = df.rename(columns={
        'Adjustedgross (in 2022 dollars)': 'Adjusted gross (in 2022 dollars)',
        'Year(s)': 'Years'
    })

    # Limpar colunas numéricas
    numeric_columns = ['Actual gross', 'Adjusted gross (in 2022 dollars)', 'Average gross']
    for col in numeric_columns:
        df[col] = df[col].astype(str).str.replace(r'[^\d.]', '', regex=True)
        df[col] = pd.to_numeric(df[col], errors='coerce').astype(float)

    # Tratar "Shows" como inteiro
    df['Shows'] = df['Shows'].astype(int)

    # Separar anos
    df[['Start year', 'End year']] = df['Years'].str.split('-', expand=True)
    df['End year'] = df['End year'].fillna(df['Start year']).astype(int)
    df['Start year'] = df['Start year'].astype(int)

    # Aplicar limpeza automática
    df['Tour title'] = df['Tour title'].apply(clean_tour_title)
    df['Artist'] = df['Artist'].str.replace(r'[^a-zA-ZÀ-ÿ ]', '', regex=True)

    # Selecionar colunas
    df = df[[
        'Rank', 'Actual gross', 'Adjusted gross (in 2022 dollars)',
        'Artist', 'Tour title', 'Shows', 'Average gross',
        'Start year', 'End year'
    ]]

    # Salvar CSV
    df.to_csv(output_path, index=False, float_format='%.1f', encoding='utf-8-sig')

if __name__ == "__main__":
    clean_data('dados.csv', '/app/data/csv_limpo.csv')  # Salva no subdiretório