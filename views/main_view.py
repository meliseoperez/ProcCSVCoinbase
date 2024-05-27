import tkinter as tk
from tkinter import filedialog, messagebox

class MainView:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller

        self.load_button = tk.Button(root, text="Cargar archivo CSV", command=self.load_file)
        self.load_button.pack(pady=20)

        self.table = tk.Frame(self.root)
        self.table.pack(fill="both", expand=True)

    def load_file(self):
        file_path =  filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if file_path:
            try:
                self.controller.load_file(file_path)
            except Exception as e:
                messagebox.showerror("ERROR",f"No se pudo cargar el archivo: {e}")

    def show_data(self, data_frame):
        for widget in self.table.winfo_children():
            widget.destroy() 

        for col_num, column in enumerate(data_frame.columns):
            header = tk.Label(self.table, text=column, borderwidth=1, relief="solid") 
            header.grid(row=0, column=col_num, sticky="nsew")

        for row_num, row in data_frame.iterrows():
            for col_num, value in enumerate(row):
                cell = tk.Label(self.table, text=value, bordewidth=1, relief="solid")
                cell.grid(row=row_num + 1, column=col_num, sticky="nsew")
        
        for col_num in range(len(data_frame.columns)):
            self.table.columnconfigure(col_num, weight=1)
        
    def show_analysis(self, analysis_text):
        analysis_label = tk.Label(self.root, text=analysis_text, justify="left")
        analysis_label.pack(pady=20)
    




