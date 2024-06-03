import pandas as pd

#Clase mara manejo de de datos
class DataModel:
    #Define un método llamado 'load_data' 
    #Toma cómo parámetro 'file_path' que representa la ruta del archivo que 
    #se va a cargar
    def load_data(self, filepath):
        try:
            #Usa pandas para leer un archivo CSV ubicado en 'file_apth', omitiendo 
            #las tres primeras filas del arhcivo. El resultado se almaace en 'data_frame'
            data_frame = pd.read_csv(filepath, skiprows=3)
            return data_frame
        except Exception as e:
            #Lanza una nueva excepción con un mensaje personalizado,
            #incluyendo el mensaje de error original
            raise Exception(f"No se pudo cargar el archivo: {e}")
    
    def analyze_data(self,data_frame):
        #Convierte la columna Timestamp del DataFrame a objetos fecha y hora de padas
        data_frame['Timestamp']  = pd.to_datetime(data_frame['Timestamp'])
        #Crea una nueva columna de 'Year' en el DataFrame, extrayendo el año de la columna 'Timestamp'
        data_frame['Year'] = data_frame['Timestamp'].dt.year
        data_frame['Month'] = data_frame['Timestamp'].dt.month       
        #Agrupa los datos por año y mes, y calcula la suma ede la columana 'Subtotal' para cada grupo 
        #y el resultado se almacena se almacena en mnthly_profit
        monthly_profit = data_frame.groupby(['Year','Month'])['Subtotal'].sum()
        #Agrupa los datos por año, y calcula la suma de la columna 'Subtotal' para cada año
        #El resultado se almacena en  'yearly_profit'
        yearly_profit = data_frame.groupby(['Year'])['Subtotal'].sum()
        #inicializa una cadena de texto con el título 'Balance de beneficios'
        analysis_text = "Balance de beneficios:\n\n"
        analysis_text += "Por mes:\n"
        #Convierte el DataFrame 'montly_profit' a una cadena de texto y la agreaga a 'analysis_text'
        analysis_text += monthly_profit.to_string()
        analysis_text += "\n\nPor años:\n"
        analysis_text += yearly_profit.to_string()

        return analysis_text