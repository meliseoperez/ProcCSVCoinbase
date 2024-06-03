import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk

# Declaro clase que maneja la interfaz gráfica del usuario
class MainView:
    # Defino método constructor que inicializa la instancia de 'MainView'
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller

        # Creo un 'Notebook' para contener las pestañas
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill="both", expand=True)

        # Pestaña para los datos del CSV
        self.csv_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.csv_tab, text='Datos CSV')

        # Pestaña para los resultados del análisis
        self.analysis_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.analysis_tab, text='Análisis')

        # Botón para cargar el archivo CSV dentro de la pestaña de datos CSV
        self.load_button = tk.Button(self.csv_tab, text="Cargar archivo CSV", command=self.load_file)
        self.load_button.pack(pady=20)

        # Sección para la tabla de datos en la pestaña de CSV
        self.table_frame = tk.Frame(self.csv_tab)
        self.table_frame.pack(fill="both", expand=True)

        # Scrollbars para la tabla de datos CSV
        self.canvas = tk.Canvas(self.table_frame)
        self.scroll_y = tk.Scrollbar(self.table_frame, orient="vertical", command=self.canvas.yview)
        self.scroll_x = tk.Scrollbar(self.table_frame, orient="horizontal", command=self.canvas.xview)
        self.canvas.configure(yscrollcommand=self.scroll_y.set, xscrollcommand=self.scroll_x.set)

        self.scroll_y.pack(side="right", fill="y")
        self.scroll_x.pack(side="bottom", fill="x")
        self.canvas.pack(side="left", fill="both", expand=True)

        self.table = tk.Frame(self.canvas)
        self.canvas.create_window((0, 0), window=self.table, anchor="nw")

        self.table.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )

        # Sección para el texto de análisis en la pestaña de Análisis
        self.analysis_frame = tk.Frame(self.analysis_tab)
        self.analysis_frame.pack(fill="both", expand=True)
        self.analysis_text = tk.Text(self.analysis_frame, wrap="word")
        self.analysis_text.pack(fill="both", expand=True)

    # Defino método que se ejecuta cuando el usuario hace clic en el botón para cargar un archivo
    def load_file(self):
        # Abro un cuadro de diálogo para seleccionar un archivo, filtrando solo archivos CSV. la ruta del
        # archivo se almacena en 'file_path'
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        # Verifico si se ha seleccionado un archivo
        if file_path:
            # Inicio un bloque para manejar posibles errores
            try:
                # Llamo al método 'load_file' del controlador con la ruta del archivo seleccionado
                self.controller.load_file(file_path)
            # Capturo cualquier excepción que ocurra    
            except Exception as e:
                # Muestra un cuadro de error si ocurre una excepción
                messagebox.showerror("ERROR", f"No se pudo cargar el archivo: {e}")

    # Defino un método llamado que recibe un DataFrame y lo muestra en la interfaz
    def show_data(self, data_frame):
        # Itera sobre los widgets hijos del marco table_frame
        for widget in self.table.winfo_children():
            # Elimina cada widget hijo para limpiar el contenido actual de la tabla
            widget.destroy() 

        # Itera sobre las columnas del DataFrame
        for col_num, column in enumerate(data_frame.columns):
            # Crea una etiqueta ('Label') para el encabezado de la columna con un borde sólido
            header = tk.Label(self.table, text=column, borderwidth=1, relief="solid") 
            # Coloca el encabezado en la primera fila ('row=0') y la columna correspondiente ('col_num')
            header.grid(row=0, column=col_num, sticky="nsew")

        # Itera sobre las filas del DataFrame
        for row_num, row in data_frame.iterrows():
            # Itera sobre los valores de cada fila del DataFrame
            for col_num, value in enumerate(row):
                # Crea una etiqueta ('Label') para cada celda con borde sólido
                cell = tk.Label(self.table, text=value, borderwidth=1, relief="solid")
                # Coloca la celda en la fila correspondiente (después de la fila de encabezado) y la columna
                # correspondiente
                cell.grid(row=row_num + 1, column=col_num, sticky="nsew")
        # Itera sobre las columnas del DataFrame 
        for col_num in range(len(data_frame.columns)):
            # Configura cada columna para que se expanda igualmente
            self.table.columnconfigure(col_num, weight=1)

    # Defino un método que recibe un texto de análisis y lo muestra en la interfaz    
    def show_analysis(self, analysis_text):
       # Limpio el contenido actual del texto de análisis
       self.analysis_text.delete(1.0, tk.END)
       # Inserto el nuevo texto de análisis
       self.analysis_text.insert(tk.END, analysis_text)
