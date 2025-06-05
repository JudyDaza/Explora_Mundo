import pandas as pd
import matplotlib.pyplot as plt

# Configurar estilo de los gráficos
plt.style.use('seaborn')

# Cargar datos
try:
    df = pd.read_csv('reservas.csv')
    print("\nDatos de reservas cargados correctamente:")
    print(df.head())
except FileNotFoundError:
    print("Error: No se encontró el archivo reservas.csv")
    exit()

# Procesamiento de datos
print("\nProcesando datos...")

# Agrupar por destino: total de reservas, personas e ingresos
resumen = df.groupby('destino').agg({
    'reserva_id': 'count',
    'personas': 'sum',
    'costo_total': 'sum'
}).rename(columns={
    'reserva_id': 'total_reservas',
    'personas': 'total_personas',
    'costo_total': 'total_ingresos'
}).sort_values('total_ingresos', ascending=False)

# Calcular ingresos promedio por reserva
resumen['ingreso_promedio'] = resumen['total_ingresos'] / resumen['total_reservas']

# Mostrar resumen
print("\nResumen de desempeño por destino:")
print(resumen)

# Gráfico 1: Reservas por destino
plt.figure(figsize=(10, 6))
resumen['total_reservas'].plot(kind='bar', color='#125936')
plt.title('Reservas por destino', fontsize=14)
plt.ylabel('Cantidad de reservas')
plt.xlabel('Destino')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('reservas_por_destino.png')
print("\nGráfico de reservas por destino generado: 'reservas_por_destino.png'")

# Gráfico 2: Ingresos por destino
plt.figure(figsize=(10, 6))
resumen['total_ingresos'].plot(kind='bar', color='#d52b1e')
plt.title('Ingresos por destino (COP)', fontsize=14)
plt.ylabel('Pesos colombianos')
plt.xlabel('Destino')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('ingresos_por_destino.png')
print("Gráfico de ingresos por destino generado: 'ingresos_por_destino.png'")

# Gráfico 3: Relación entre personas e ingresos
plt.figure(figsize=(10, 6))
plt.scatter(df['personas'], df['costo_total'], color='#125936', alpha=0.6)
plt.title('Relación entre número de personas y costo total', fontsize=14)
plt.xlabel('Número de personas')
plt.ylabel('Costo total (COP)')
plt.grid(True)
plt.tight_layout()
plt.savefig('relacion_personas_ingresos.png')
print("Gráfico de relación personas-ingresos generado: 'relacion_personas_ingresos.png'")

# Mostrar todos los gráficos
plt.show()

# Exportar resumen a Excel
resumen.to_excel('resumen_destinos.xlsx')
print("\nResumen exportado a Excel: 'resumen_destinos.xlsx'")