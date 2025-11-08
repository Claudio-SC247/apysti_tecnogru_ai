"""
Elabore una aplicación que permita simular el uso de pandas para visualizar algunas estadísticas (ud. 
defina lo que desea medir para visualizarlas) con respecto a una encuesta, relacionada a preferencias de 
supermercados en Piura.
"""
import pandas as pd
import matplotlib.pyplot as plt

# Cargar los datos de la encuesta
df = pd.read_csv('encuesta.csv')

# Mostrar las primeras filas para verificar
print("Vista previa de los datos:")
print(df.head())

# -------------------------------
                                                # CONSULTA 1: Preferencias generales
# -------------------------------
preferencias = df['Supermercado de Preferencia'].value_counts()
print("\nPreferencias por centro comercial:")
print(preferencias)

# Crear texto automático para la leyenda
leyenda_texto = "Leyenda:\n"
for supermercado, cantidad in preferencias.items():
    leyenda_texto += f"{supermercado}: {cantidad}\n"

# Gráfico de barras
preferencias.plot(kind='bar', color='skyblue')
plt.title('Supermercado preferido por los usuarios - Piura')
plt.xlabel('Supermercado')
plt.ylabel('Número de votos')
plt.xticks(rotation=45)
# Leyenda explicativa dentro del gráfico
plt.text(len(preferencias) - 0, max(preferencias)*0.7,  #-1,0.9
        leyenda_texto,
        fontsize=9,
        bbox=dict(facecolor='white', alpha=0.7))

plt.tight_layout()
plt.show()

# -------------------------------
                                                        # CONSULTA 2: Distribución de edades
# -------------------------------
if 'Edad' not in df.columns:
    print("\n⚠️ No se encontró la columna 'Edad' en el archivo CSV.")
    print("Columnas disponibles:", df.columns.tolist())
    exit()
conteo_edades = df['Edad'].value_counts().sort_index()
print("\nDistribución de edades:")
print(conteo_edades)
#Graficar en circular (pie chart)
colores = plt.cm.Paired.colors  # paleta de colores
plt.figure(figsize=(7, 7))
plt.pie(
    conteo_edades,
    labels=conteo_edades.index,
    autopct='%1.1f%%',
    startangle=90,
    colors=colores,
    wedgeprops={'edgecolor': 'white'}
)
plt.title("Distribución por rango de edad - Encuesta Piura")
plt.legend(
    title="Rangos de edad",
    loc="upper right",
    bbox_to_anchor=(1.3, 1)
)
plt.tight_layout()
plt.show()
#Leyenda / resumen de datos
print("\nResumen general:")
print(f"Total de encuestados: {len(df)}")
print(f"Rangos de edad detectados: {len(conteo_edades)}")
print(f"Rango más frecuente: {conteo_edades.idxmax()} ({conteo_edades.max()} personas)")

# -------------------------------
                                        # CONSULTA 3: Personas femeninas y masculinas en total y por supermercado
# -------------------------------
if 'Género' not in df.columns:
    print("\n⚠️ No se encontró la columna 'Género' en el archivo CSV.")
    print("Columnas disponibles:", df.columns.tolist())
    exit()
genero_supermercado = df.groupby(['Supermercado de Preferencia', 'Género']).size().unstack(fill_value=0)
print("\nNúmero de personas por género y supermercado:")    
print(genero_supermercado)
genero_supermercado.plot(kind='bar', stacked=True, color=['lightcoral', 'lightskyblue'])
plt.title('Número de personas por género y supermercado - Piura')
plt.xlabel('Supermercado')
plt.ylabel('Número de personas')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
# -------------------------------
                                        # CONSULTA 4: Consulta personalizada (ejemplo)
# -------------------------------
