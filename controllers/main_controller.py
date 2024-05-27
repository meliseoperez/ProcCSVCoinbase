import tkinter as tk
from views.main_view import MainView
from models.data_model import DataModel

class MainController:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Cripto Impuestos")
        self.model = DataModel()
        self.view = MainView(self.root, self)

    def run(self):
        self.root.mainloop()
    
    def load_file(self, file_path):
        data_frame = self.model.load_data(file_path)
        self.view.show_data(data_frame)
        analysis_text = self.model.analyze_data(data_frame)
        self.view.show_analysis(analysis_text)
    
    