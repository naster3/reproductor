import tkinter as tk
from tkinter import filedialog, Label
import pygame
import os

class ReproductorMusica:
    def __init__(self, ventana,carpeta_musica):
        self.ventana = ventana
        self.ventana.title("Reproductor de música")
        self.ventana.geometry("400x400")
         # Crear el cuadro de lista para la música
        self.listbox_musica = tk.Listbox(self.ventana, width=50)
        # Posicionar el cuadro de lista
        self.listbox_musica.pack(pady=10)
        # Crear los botones para cargar y reproducir archivos de música
        boton_cargar = tk.Button(ventana, text="Cargar música", command=self.cargar_musica)
        boton_cargar.pack()
        hori=["horizontal"]
        #modulador de volumen
        volumen= tk.Scale(ventana, from_=0, to=100,orient=hori,command=self.set_volumen)
        volumen.pack()
        #boton pausar
        boton_pausar= tk.Button(ventana, text="pausar", command=self.pausar)
        boton_pausar.pack()
        #boton play
        boton_reproducir = tk.Button(ventana, text="Reproducir", command=self.reproducir_musica)
        boton_reproducir.pack()
        # Crear la etiqueta para mostrar la ruta seleccionada
        self.label_ruta = Label(ventana, text="")
        self.label_ruta.pack()
        # Crear el botón para seleccionar carpeta
        boton_carpeta = tk.Button(ventana, text="Seleccionar carpeta", command=self.buscar_carpeta)
        boton_carpeta.pack(pady=20)
        left=['left']
        right=['right']
        # Crear el botón de "Siguiente canción"
        boton_siguiente = tk.Button(ventana,justify=left, text="Siguiente canción", command=self.siguiente_cancion)
        boton_siguiente.pack(side="left",padx=30)
        #boton_siguiente.grid(row=0,column=2)
        # Crear el botón de "Canción anterior"
        boton_anterior = tk.Button(ventana,justify=right, text="Canción anterior", command=self.anterior_cancion)
        boton_anterior.pack(side="right",padx=30)

        # Configurar el reproductor de música
        pygame.init()
        pygame.mixer.music.set_volume(0.5)

    def cargar_musica(self):
        # Abrir un diálogo de archivo para seleccionar una canción
        archivo = filedialog.askopenfilename()
        if archivo:
            self.archivo_musica = archivo
            self.mensaje=tk.Label(ventana,text="cancion cargada").pack()
            
    # Cargar la canción seleccionada y reproducirla
    def reproducir_musica(self):
        
        pygame.mixer.music.load(self.archivo_musica)
        pygame.mixer.music.play()
        
    #pausar la reproduccion
    def pausar(self):
         pygame.mixer.music.stop()
         
    #modulacion de volumen 
    def set_volumen(self, volumen):  
        pygame.mixer.music.set_volume(int(volumen) / 100)
        
    def buscar_carpeta(self):
        # Mostrar el cuadro de diálogo para seleccionar carpeta
        carpeta_musica = filedialog.askdirectory()
        carpeta_musica = [archivo for archivo in os.listdir(carpeta_musica) if archivo.endswith('.mp3')]
        for archivo in carpeta_musica:
            self.listbox_musica.insert(tk.END, archivo)
         # Actualizar la etiqueta con la ruta seleccionada
        self.label_ruta.config(text='archivos cargados')
        
    def siguiente_cancion(self):
        if self.listbox_musica < len(self.listbox_musica) - 1:
            self.listbox_musica += 1
            self.reproducir_musica()

    def anterior_cancion(self):
        if self.listbox_musica > 0:
            self.listbox_musica -= 1
            self.reproducir_musica()  
# Crear la ventana principal y el reproductor de música
ventana = tk.Tk()
lista_musica = ReproductorMusica(ventana,carpeta_musica='')
# Ejecutar el bucle principal de la ventana
ventana.mainloop()

