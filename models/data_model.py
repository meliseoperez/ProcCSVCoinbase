import pandas as pd

class DataModel:
    def load_data(self, filepath):
        try:
            data_frame = pd.read_csv(filepath, skiprows=3)
            return data_frame
        except Exception as e:
            raise Exception(f"No se pudo cargar el archivo: {e}")
    
    def analyze_data(self,data_frame):
        data_frame['Timestamp']  = pd.to_datetime(data_frame['Timestamp'])
        data_frame['Year'] = data_frame['Timestamp'].dt.year
        data_frame['Month'] = data_frame['Timestamp'].dt.month       

        monthly_profit = data_frame.groupby(['Year','Month'])['Subtotal'].sum()
        yearly_profit = data_frame.groupby(['Year'])['Subtotal'].sum()

        analysis_text = "Balance de beneficios:\n\n"
        analysis_text += "Por mes:\n"
        analysis_text += monthly_profit.to_string()
        analysis_text += "\n\nPor años:\n"
        analysis_text += yearly_profit.to_string()

        return analysis_text