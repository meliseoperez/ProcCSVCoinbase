import pandas as pd

# Clase para manejo de datos
class DataModel:
    # Define un método llamado 'load_data'
    # Toma como parámetro 'file_path' que representa la ruta del archivo que
    # se va a cargar
    def load_data(self, filepath):
        try:
            # Usa pandas para leer un archivo CSV ubicado en 'file_apth', omitiendo
            # las tres primeras filas del arhcivo. El resultado se almacena en 'data_frame'
            data_frame = pd.read_csv(filepath, skiprows=3)
            return data_frame
        except Exception as e:
            # Lanza una nueva excepción con un mensaje personalizado,
            # incluyendo el mensaje de error original
            raise Exception(f"No se pudo cargar el archivo: {e}")

    def analyze_data(self, data_frame):
        # Convierte la columna Timestamp del DataFrame a objetos fecha y hora de pandas
        data_frame['Timestamp'] = pd.to_datetime(data_frame['Timestamp'])
        # Crea una nueva columna de 'Year' en el DataFrame, extrayendo el año de la columna 'Timestamp'
        data_frame['Year'] = data_frame['Timestamp'].dt.year
        # Crea una nueva columna de 'Month' en el DataFrame, extrayendo el mes de la columna 'Timestamp'
        data_frame['Month'] = data_frame['Timestamp'].dt.month

        # Agrupa los datos por año, mes, tipo de operación, asset e ID, y calcula la suma de la columna 'Subtotal' para cada grupo
        # El resultado se almacena en 'monthly_profit_by_group'
        monthly_profit_by_group = data_frame.groupby(['Year', 'Month', 'Transaction Type', 'Asset', 'ID'])['Subtotal'].sum()

        

        # Restablece el índice de 'monthly_profit_by_group' para que el 'Year', 'Month', 'Transaction Type', 'Asset' e 'ID' sean las columnas
        monthly_profit_by_group = monthly_profit_by_group.reset_index()

        # Inicializa una cadena de texto con el título 'Balance de beneficios'
        analysis_text = "Balance de beneficios:\n\n"

        # Convierte el DataFrame 'monthly_profit_by_group' a una cadena de texto y la agrega a 'analysis_text'
        analysis_text += monthly_profit_by_group.to_string()

        return analysis_text