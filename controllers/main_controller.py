import tkinter as tk
from views.main_view import MainView
from models.data_model import DataModel

class MainController:
    def __init__(self):#Método contructor 
        #Crea una instancia de la ventana principal de tkinter y l asigna a 'self.root'
        self.root = tk.Tk()

        #Establece el título
        self.root.title("Cripto Impuestos")
        #Crea una nueva instancia del modelo de dato
        self.model = DataModel()
        #Crea una una instancia de la vista principal, pasándole
        #la ventana principal y el controlador mismo
        self.view = MainView(self.root, self)

    #Defino un méntodo run que se encargará de inciar la aplicación
    def run(self):
        #inicial el bucle principal de 'tkinter', que mantiene la aplicación
        #abierta y esperando eventos de usuario
        self.root.mainloop()
    
    #Define un meodo que toma como parámetro 'file_path'
    #que representa la ruat del archivo que se va a cargar
    def load_file(self, file_path):
        #llama al método 'load_data' del modelo ('self.model') para cargar
        #los datos del archivo especificado por 'file_path'. EL resultado se 
        #almacena  en 'data_frame'
        data_frame = self.model.load_data(file_path)
        #llama al metodo 'show_data' para mostrar los datos cargados en la interfaz de usuario
        self.view.show_data(data_frame)
        #Llama al método 'analyze_data' del modelo('self.model') para analizar los datos
        #y obtener un texto con los resultados del análisis. El resultado se almacean en 'analysis_text'
        analysis_text = self.model.analyze_data(data_frame)
        #Llama al método 'show_analysis_text' de la vista('self.view') para mostrar el texto del análisis
        #en la interfaz de usuario
        self.view.show_analysis(analysis_text)
    
    