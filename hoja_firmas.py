
import pandas as pd

def process_students(file_path):
    df = pd.read_csv(file_path, sep=';', skipinitialspace=True)
    df.columns = [col.strip() for col in df.columns]
    df = df.sort_values(by='Nombre')
    return df

def format_groups(df, group_size=8):
    output = []
    for i in range(0, len(df), group_size):
        group_df = df.iloc[i : i + group_size]
        output.append(f"GRUPO {(i // group_size) + 1}")
        output.append(f"{'Nombre':<20} | {'Apellidos':<20} | {'Lunes':<10} | {'Jueves':<10}")
        output.append("-" * 70)
        for _, row in group_df.iterrows():
            output.append(f"{str(row['Nombre']):<20} | {str(row['Apellido(s)']):<20} | {'__________':<10} | {'__________':<10}")
        output.append("\n")
    return "\n".join(output)

if __name__ == '__main__':
    df = process_students('pokemons_participantes_curso.csv')
    sheet = format_groups(df)
    with open('hoja_firmas.txt', 'w') as f:
        f.write(sheet)
    print("Hoja de firmas generada en 'hoja_firmas.txt'")
