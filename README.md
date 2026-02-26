Tarea 1 . Tardé 5 minutos
Tarea 2. Tardé 8 minutos.
Tarea 3. Tardé 5 minutos
1.Esta tarea se organiza de la siguiente forma:

hoja_firmas.py: El script principal que procesa los datos y genera la hoja.
test_hoja_firmas.py: Suite de tests unitarios para verificar la lógica de negocio.
hoja_firmas.txt: El resultado final con los alumnos agrupados de 8 en 8.
.gitignore: Archivo para configurar qué archivos ignorar en Git.

2. Estructura del Código y Control de Versiones
Para poner el código bajo control de versiones, se seguirían estos comandos en la terminal:


git init
git add hoja_firmas.py test_hoja_firmas.py .gitignore README.md
git commit -m "Initial commit: Generador de hojas de firmas con agrupación y tests"

3. Código del Script (hoja_firmas.py
import pandas as pd

def leer_y_ordenar(ruta_archivo):
    # Leemos el CSV manejando espacios tras el delimitador ';'
    df = pd.read_csv(ruta_archivo, sep=';', skipinitialspace=True)
    df.columns = [col.strip() for col in df.columns]
    # Ordenamos alfabéticamente por Nombre
    df = df.sort_values(by='Nombre')
    return df

def generar_hoja_texto(df, tamano_grupo=8):
    lineas = []
    num_alumnos = len(df)
    
    for i in range(0, num_alumnos, tamano_grupo):
        num_grupo = (i // tamano_grupo) + 1
        grupo_df = df.iloc[i : i + tamano_grupo]
        
        lineas.append(f"--- GRUPO {num_grupo} ---")
        lineas.append(f"{'Nombre':<20} | {'Apellidos':<25} | {'Lunes':<10} | {'Jueves':<10}")
        lineas.append("-" * 75)
        
        for _, row in grupo_df.iterrows():
            nombre = str(row['Nombre'])[:20]
            apellidos = str(row['Apellido(s)'])[:25]
            lineas.append(f"{nombre:<20} | {apellidos:<25} | {'__________':<10} | {'__________':<10}")
        
        lineas.append("\n" + "="*75 + "\n")
        
    return "\n".join(lineas)

if __name__ == '__main__':
    datos = leer_y_ordenar('pokemons_participantes_curso.csv')
    hoja = generar_hoja_texto(datos)
    with open('hoja_firmas.txt', 'w', encoding='utf-8') as f:
        f.write(hoja)
    print("Hoja de firmas generada con éxito.")

  4. Tests Unitarios (test_hoja_firmas.py)

     import unittest
import pandas as pd
import os
from hoja_firmas import leer_y_ordenar, generar_hoja_texto

class TestHojaFirmas(unittest.TestCase):
    def setUp(self):
        self.test_csv = 'test_temp.csv'
        with open(self.test_csv, 'w') as f:
            f.write("Nombre; Apellido(s)\nZetta; Last\nAlpha; First\nBeta; Second")
            
    def tearDown(self):
        if os.path.exists(self.test_csv):
            os.remove(self.test_csv)

    def test_ordenacion(self):
        df = leer_y_ordenar(self.test_csv)
        self.assertEqual(df.iloc[0]['Nombre'], 'Alpha')
        self.assertEqual(df.iloc[-1]['Nombre'], 'Zetta')

    def test_agrupacion_ocho(self):
        # Creamos un DF de 10 alumnos para probar que hace 2 grupos
        df = pd.DataFrame({'Nombre': range(10), 'Apellido(s)': range(10)})
        hoja = generar_hoja_texto(df, tamano_grupo=8)
        self.assertIn("GRUPO 1", hoja)
        self.assertIn("GRUPO 2", hoja)

if __name__ == '__main__':
    unittest.main()
5. Resultado Generado

--- GRUPO 1 ---
Nombre               | Apellidos                 | Lunes      | Jueves    
---------------------------------------------------------------------------
Abra                 | Julius                    | __________ | __________
Aebadius             | Sulpicius                 | __________ | __________
Aemilius             | Vibius                    | __________ | __________
Aerodactyl           | Sicinius                  | __________ | __________
Alakazam             | Claudius                  | __________ | __________
Arbok                | Cornelius                 | __________ | __________
Arcanine             | Octavius                  | __________ | __________
Articuno             | Verginius                 | __________ | __________

===========================================================================
