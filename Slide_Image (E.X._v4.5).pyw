
# -*- coding: utf-8 -*-
#!/usr/bin/env python
'''
Desarrollado por: 👉 Cristian M. Veliz Cano ✔
Versión del Soft: 👉 V-03 (E.X._v4.5)
Nombre del Soft: ✨ Slide Image Viewer ✨
✨ Visor Universal de Imágenes Multi-Formato ✨

✨ Slide Image Viewer ✨

✅ Este Soft-Ware fue diseñado para facilitar la visualización,
navegación y gestión de imágenes desde múltiples fuentes de datos
en una interfaz gráfica limpia, minimalista y altamente funcional.

⚙️ El funcionamiento del Programa es Directo:

📄 El Usuario puede cargar imágenes desde archivos locales,
bases de datos SQLite BLOB, recursos QRC compilados de PyQt,
o archivos JSON con datos Base64, todo desde una única ventana.

⭐ El Soft-Ware permite trabajar con:

✔ Archivos Individuales de Imagen (Drag & Drop soportado)
✔ Directorios Completos (incluyendo subcarpetas recursivas)
✔ Bases de Datos SQLite (detección automática de tablas BLOB)
✔ Recursos QRC de PyQt (resources_rc.py + .qrc sin extraer)
✔ Archivos JSON (Base64, URLs remotas o rutas locales)
✔ Slideshow automático con temporizador configurable (5s)
✔ Navegación intuitiva (teclado, botones y rueda del mouse)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📌 Nota Importante:

➜ Este Soft-Ware trabaja completamente de forma Local.

✔ No requiere conexión a Internet (excepto para URLs en JSON).
✔ No utiliza Servicios Externos obligatorios.
✔ No transmite Información.
✔ No realiza Sincronizaciones Remotas.

💯% OFF-LINE para todas las funciones principales.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

⌨️ Atajos del Teclado:

📎 F1
• Para mostrar información del software.

📎 CTRL+I
• Cargar archivos de imagen individuales.

📎 CTRL+C
• Cargar imágenes desde una carpeta.

📎 CTRL+D
• Cargar imágenes desde directorio (recursivo).

📎 CTRL+B
• Cargar imágenes desde Base de Datos SQLite BLOB.

📎 CTRL+R
• Explorar y cargar recursos QRC de PyQt5/6.

📎 CTRL+J
• Cargar imágenes desde archivo JSON (Base64/URLs).

📎 CTRL+C (sobre imagen)
• Copiar la imagen actual al portapapeles.

📎 ← → (Flechas)
• Navegar entre imágenes (anterior/siguiente).

📎 Rueda del Mouse
• Navegación rápida (arriba=anterior, abajo=siguiente).

📎 Click Mouse / Espacio
• Pausar/Reanudar el slideshow automático.

📎 ESC
• Cierra inmediatamente el Soft-Ware.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📌 Licencia:

MIT License

Copyright (c) 2026 Cristian M. Veliz Cano

Se concede permiso, de forma gratuita, a cualquier persona
que obtenga una copia de este software y de los archivos de
documentación asociados, para utilizar el Software sin
restricción, incluyendo sin limitación los derechos de uso,
copia, modificación, fusión, publicación, distribución,
sublicencia y/o venta de copias del Software.

EL SOFTWARE SE PROPORCIONA "TAL CUAL",
SIN GARANTÍA DE NINGÚN TIPO.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📦 De Caracter Gratuito, Portable,
🎭 Open-Source, Didáctico y Free-Code.

🛠️ Diseñado para Visualización Rápida,
Desarrollo de Software, Testing de Recursos
y Administración de Assets Gráficos.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📌 Estructura Interna de Datos:

➜ Tupla de Imagen: (tipo, nombre, datos)
➜ • tipo: 'file' | 'blob' | 'qrc' | 'json'
➜ • nombre: str (nombre de archivo para mostrar)
➜ • datos: str (ruta) | bytes (BLOB) | str (recurso Qt)

➜ Sistema de Renderizado Unificado:
➜ • Soporte QPixmap nativo de Qt
➜ • Escalado automático manteniendo aspecto
➜ • Cacheo en memoria de pixmaps actuales

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

"Un Visor Universal que une Archivos Locales, Bases de Datos,
Recursos Compilados y JSON en una sola ventana fluida."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📁 class ImageSlider:
   ├── def initUI(self)...
   ├── def load_from_blob(self)...
   ├── def load_from_qrc(self)...
   ├── def load_from_database(self)...
   ├── def load_from_qrc_list(self)...
   ├── def update_image(self)...
   ├── def next_image(self)...
   ├── def previous_image(self)...
   ├── def add_images(self)...
   ├── def add_images_carpeta(self)...
   ├── def add_images_directorys(self)...
   ├── def In_Im_Extern_Path(self)...
   ├── def create_context_menu(self)...
   ├── def prompt_load_database(self)...
   ├── 
   ├── def prompt_load_qrc(self):
   │     """Explorador de QRC..."""
   │     # ... código completo ...
   │
   └── def dragEnterEvent(self)...

Soft´Ware:
https://mega.nz/file/blUzTbCL#wKzzycnLwcLQ9LssR6sumWGEf2gIj8z_cdq7E81ioSY
'''
##=========================================================================================
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QApplication, QLabel, QMainWindow, QMenu, QAction, 
    QFileDialog, QVBoxLayout, QWidget, QPushButton, QMessageBox, QShortcut)
from PyQt5.QtGui import QPixmap, QDragEnterEvent, QDropEvent, QFont, QPalette, QIcon, QKeySequence
from PyQt5.QtCore import QTimer, Qt, QMimeData, QFile, QIODevice

import sys, os
import sqlite3
import xml.etree.ElementTree as ET

import json
import base64
import re
import urllib.request
import tempfile
from io import BytesIO

from PIL import Image
import pillow_jxl
from pillow_jxl import Decoder

##====================================================================================
# --- Clase para manejo de rutas de recursos ---
##====================================================================================
class Path:
    @staticmethod
    def resource_path(relative_path):
        try:
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")
        return os.path.join(base_path, relative_path)

    # =========================
    # ✨ Devuelve, la Dirección Exacta de Cualquier, Archivo dentro de la App-Desk
    # =========================

    @staticmethod
    def resource_path_app():
        try:
            path_app = getattr(sys, "_MEIPASS", os.path.abspath(os.path.dirname(__file__)))
        except Exception as e:
            print(e)
        return path_app

##====================================================================================
# --- Clase Principal ---
##====================================================================================
class ImageSlider(QMainWindow):
    def __init__(self, in_im=None, master=None):
        super().__init__(master)
        self.in_im = in_im
        self.images = []
        self.current_index = 0
        self.current_pixmap = None
        self.paused = False
        self.Full_Screnn_Window = False
        
        self.timer = QTimer()
        self.timer.timeout.connect(self.next_image)
        self.timer.start(5000)
        
        self.initUI()
        if self.in_im:
            self.In_Im_Extern_Path()

    def initUI(self):
        self.setWindowTitle('Slide_Image (E.X._v4.5)')
        self.center_on_screen()
        
        # Icono
        self.Ico_app = Path.resource_path('Ico\\1.png')
        self.setWindowIcon(QtGui.QIcon(self.Ico_app))
        
        # Paleta negra
        p = self.palette()
        p.setColor(QPalette.Window, Qt.black)
        self.setPalette(p)
        
        # Widget central
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        
        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.central_widget.setLayout(self.layout)
        
        # Label para imágenes
        self.label = QLabel(self)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setScaledContents(True)
        self.layout.addWidget(self.label)
        
        # Botones navegación
        self.left_button = QPushButton('<', self)
        self.left_button.setStyleSheet("background-color: rgba(0, 0, 0, 150); color: white; border-radius: 25px;")
        self.left_button.setFont(QFont('Arial', 20, QFont.Bold))
        self.left_button.clicked.connect(self.previous_image)
        self.left_button.setFixedSize(50, 50)
        
        self.right_button = QPushButton('>', self)
        self.right_button.setStyleSheet("background-color: rgba(0, 0, 0, 150); color: white; border-radius: 25px;")
        self.right_button.setFont(QFont('Arial', 20, QFont.Bold))
        self.right_button.clicked.connect(self.next_image)
        self.right_button.setFixedSize(50, 50)
        
        # Drag & Drop
        self.setAcceptDrops(True)
        self.create_context_menu()

        # Atajo Ctrl + I ☑️ Ingresar Archivos por Selección, Simple  ↔  (Ctrl+I)
        info_software = QShortcut(QKeySequence('Ctrl+I'), self)
        info_software.activated.connect(self.add_images)

        # Atajo Ctrl + C ☑️ Ingresar Archivos por Carpeta  ↔  (Ctrl+C)
        key_info_software = QShortcut(QKeySequence('Ctrl+C'), self)
        key_info_software.activated.connect(self.add_images_carpeta)

        # Atajo Ctrl + D ☑️ Ingresar Archivos por Directorio  ↔  (Ctrl+D)
        self.shortcut = QShortcut(QKeySequence("Ctrl+D"), self)
        self.shortcut.activated.connect(self.add_images_directorys)

        # Atajo Ctrl + B ☑️ Ingresar Archivos por Base de Datos  ↔  (Ctrl+B)
        self.shortcut = QShortcut(QKeySequence("Ctrl+B"), self)
        self.shortcut.activated.connect(self.prompt_load_database)

        # Atajo Ctrl + R ☑️ Ingresar Archivos por Explorar QRC  ↔  (Ctrl+R)
        self.shortcut = QShortcut(QKeySequence("Ctrl+R"), self)
        self.shortcut.activated.connect(self.prompt_load_qrc)

        # Atajo Ctrl + J ☑️ Ingresar Archivos por Resources JSON  ↔  (Ctrl+J)
        self.shortcut = QShortcut(QKeySequence("Ctrl+J"), self)
        self.shortcut.activated.connect(self.prompt_load_json)

        # Atajo Ctrl + F1 ✔️ Información del Soft-Ware  ↔  (F1)
        self.shortcut = QShortcut(QKeySequence("F1"), self)
        self.shortcut.activated.connect(self.info_app)

        # Atajo Ctrl + K ✔️ Información Teclas de Atajos  ↔  (Ctrl+K)
        self.shortcut = QShortcut(QKeySequence("Ctrl+K"), self)
        self.shortcut.activated.connect(self.info_keys)

        # Atajo Ctrl + S ✔️ Guarda la Imagen no Importa de donde la este Cargando  ↔  (Ctrl+S)
        self.shortcut = QShortcut(QKeySequence("Ctrl+S"), self)
        self.shortcut.activated.connect(self.Guardar_Imagen)

        # Atajo Ctrl + L ✔️ Limpia y Restaura a Valores de Innicio Todo  ↔  (Ctrl+L)
        self.shortcut = QShortcut(QKeySequence("Ctrl+L"), self)
        self.shortcut.activated.connect(self.cleanear)

        # Atajo F11 ✔️ Full Screen Window  ↔  (F11)
        self.shortcut = QShortcut(QKeySequence("F11"), self)
        self.shortcut.activated.connect(self.Pantalla_Completa)

        # Info Sobre el Soft´Ware
        self.info_app()

    # ============================================================
    # MÉTODOS DE CARGA (Con la Ruedita de el mMuse)
    # ============================================================
    def wheelEvent(self, event):
	    if event.angleDelta().y() > 0:
	        self.previous_image()
	    else:
	        self.next_image()

    # ============================================================
    # MÉTODOS DE CARGA (BLOB, QRC, Archivos)
    # ============================================================
    def load_from_blob(self, blob_data, name=""):
        """Carga imagen desde bytes, detectando JXL automáticamente"""
        try:
    
            # Detectar si es JXL por el nombre o magic bytes
            if name.lower().endswith('.jxl') or blob_data[:2] == b'\xff\x0a':
                return self.load_from_jxl(blob_data)

            pixmap = QPixmap()
            if pixmap.loadFromData(blob_data):
                return pixmap

        except Exception as e:
            print(f"Error BLOB: {e}")
        return None

    def load_from_qrc(self, resource_path):
        try:
            file = QFile(resource_path)
            if file.open(QIODevice.ReadOnly):
                data = file.readAll()
                file.close()
                pixmap = QPixmap()
                if pixmap.loadFromData(data):
                    return pixmap
        except Exception as e:
            print(f"Error QRC: {e}")
        return None

    # ============================================================
    # MÉTODO PARA CARGAR JXL (NUEVO - INTEGRACIÓN DEL PARCHE)
    # ============================================================
    def load_from_jxl(self, ruta):
        """Cargar imagen JXL desde archivo"""
        try:
            with open(ruta, "rb") as archivo:
                datos_jxl = archivo.read()
            
            # Reutilizar el método de bytes
            return self._load_jxl_from_bytes(datos_jxl)
                
        except Exception as e:
            print(f"Error cargando JXL archivo: {e}")
        return None
    
    def _load_jxl_from_bytes(self, blob_data):
        """Cargar JXL desde bytes (BLOB) - CORREGIDO"""
        try:
            from pillow_jxl import Decoder
            
            decoder = Decoder(parallel=True)
            info, pixels = decoder(blob_data)  # blob_data es bytes, no string
            
            if info.mode not in ("RGB", "RGBA", "L", "LA"):
                raise ValueError(f"Modo JXL no soportado: {info.mode}")
            
            imagen = Image.frombytes(info.mode, (info.width, info.height), pixels)
            
            # Convertir a PNG en memoria
            buffer = BytesIO()
            imagen.save(buffer, format="PNG")
            datos_png = buffer.getvalue()
            
            pixmap = QPixmap()
            if pixmap.loadFromData(datos_png, "PNG"):
                return pixmap
                
        except Exception as e:
            print(f"Error cargando JXL bytes: {e}")
        return None

    def load_from_blob(self, blob_data, name=""):
        """Carga imagen desde bytes, detectando JXL automáticamente"""
        try:
            # Detectar si es JXL por el nombre o magic bytes
            if name.lower().endswith('.jxl') or (blob_data[:2] == b'\xff\x0a'):
                return self._load_jxl_from_bytes(blob_data)  # <-- Llama al de bytes, no al de archivo

            pixmap = QPixmap()
            if pixmap.loadFromData(blob_data):
                return pixmap

        except Exception as e:
            print(f"Error BLOB: {e}")
        return None

    def load_from_database(self, db_path, table="images", blob_col="image_data", name_col="filename"):
        self.images.clear()
        self.current_index = 0
        
        try:
            conn = sqlite3.connect(db_path)
            cur = conn.cursor()
            cur.execute(f"SELECT {name_col}, {blob_col} FROM {table}")
            
            for name, blob in cur.fetchall():
                if blob:
                    self.images.append(('blob', name, blob))
            
            conn.close()

            self.mousePressEvent()
            self.update_image()
            QMessageBox.information(self, "Éxito", f"Cargadas {len(self.images)} imágenes de DB")
            
        except Exception as e:
            QMessageBox.critical(self, "Error DB", str(e))

    def load_from_qrc_list(self, qrc_paths):
        self.images.clear()
        self.current_index = 0
        
        for path in qrc_paths:
            self.images.append(('qrc', path.split('/')[-1], path))
        
        self.mousePressEvent()
        self.update_image()

    def update_image(self):
        if not self.images or self.current_index >= len(self.images):
            self.label.setText("Arrastra imágenes o usa el menú derecho")
            return
        
        img_type, name, data = self.images[self.current_index]
        ImageSlider.Actualizando_Title(self)
        
        # Cargar según tipo
        if img_type == 'file':
            #pixmap = QPixmap(data)
            # Detectar JXL
            if name.lower().endswith('.jxl'):
                pixmap = self.load_from_jxl(data)
            else:
                pixmap = QPixmap(data)
        elif img_type == 'blob':
            pixmap = self.load_from_blob(data, name)
        elif img_type == 'qrc':
            pixmap = self.load_from_qrc(data)
        elif img_type == 'json':
            # Detectar si es JXL por magic bytes o nombre
            if name.lower().endswith('.jxl') or (isinstance(data, bytes) and data[:2] == b'\xff\x0a'):
                pixmap = self._load_jxl_from_bytes(data)
            else:
                pixmap = self.load_from_blob(data, name)

        elif img_type == 'jxl':  # Nuevo tipo
            pixmap = self.load_from_jxl(data)
        else:
            pixmap = None
        
        if pixmap and not pixmap.isNull():
            scaled = pixmap.scaled(
                self.label.width(), self.label.height(),
                Qt.KeepAspectRatio, Qt.SmoothTransformation
            )
            self.label.setPixmap(scaled)
            self.current_pixmap = pixmap
            
            # Actualizar título (agregar 'json' al diccionario)
            total = len(self.images)
            tipo_str = {
                'file': 'ARCH', 
                'blob': 'DB', 
                'qrc': 'QRC',
                'json': 'JSON'
            }[img_type]
            status = "Slide_Image (E.X._v4.5) || ▶" if self.timer.isActive() else "⏸"
            self.setWindowTitle(f"{status} [{tipo_str}] {self.current_index+1}/{total} | {name[:30]}")
        else:
            self.label.setText(f"Error cargando: {name}")

    # ============================================================
    # NAVEGACIÓN (next/previous)
    # ============================================================
    def next_image(self):
        if self.images:
            self.current_index = (self.current_index + 1) % len(self.images)
            self.update_image()

    def previous_image(self):
        if self.images:
            self.current_index = (self.current_index - 1) % len(self.images)
            self.update_image()

    # ============================================================
    # CARGA DE ARCHIVOS (file system)
    # ============================================================
    def add_images(self):
        files, _ = QFileDialog.getOpenFileNames(
            self, "Seleccionar Imágenes", "", 
            "Imágenes (*.png *.jpg *.jpeg *.bmp *.gif *.ico *.webp *.jxl)"
        )
        for f in files:
            self.images.append(('file', os.path.basename(f), f))
        
        self.mousePressEvent()
        self.update_image()

    def add_images_carpeta(self):
        folder = QFileDialog.getExistingDirectory(self, "Seleccionar Carpeta")
        if folder:
            exts = ('.png', '.jpg', '.jpeg', '.bmp', '.gif', '.webp', '.ico', '.jxl')
            for f in os.listdir(folder):
                if f.lower().endswith(exts):
                    full = os.path.join(folder, f)
                    self.images.append(('file', f, full))
            
            self.mousePressEvent()
            self.update_image()

    def add_images_directorys(self):
        folder = QFileDialog.getExistingDirectory(self, "Seleccionar Directorio")
        if folder:
            exts = ('.png', '.jpg', '.jpeg', '.bmp', '.gif', '.webp', '.ico', '.jxl')
            for dirpath, _, files in os.walk(folder):
                for f in files:
                    if f.lower().endswith(exts):
                        full = os.path.join(dirpath, f)
                        self.images.append(('file', f, full))

            self.mousePressEvent()
            self.update_image()

    def In_Im_Extern_Path(self):
        if not self.in_im:
            return
        folder = os.path.dirname(self.in_im) if os.path.isfile(self.in_im) else self.in_im
        exts = ('.png', '.jpg', '.jpeg', '.bmp', '.gif', '.webp', '.ico', '.jxl')
        if os.path.isdir(folder):
            for f in os.listdir(folder):
                if f.lower().endswith(exts):
                    full = os.path.join(folder, f)
                    self.images.append(('file', f, full))

        self.mousePressEvent()
        self.update_image()

    # ============================================================
    # Metodo para Acortar el Titulo si este fuera muy Largo (Alternativo)
    # ============================================================
    def acortando_title(self, text, length=60):

        name, ext = os.path.splitext(text)

        if text:

            if len(text) <= length:
                return text

            else:
                return f"{' '.join(text[:length+1].split(' ')[0:-1])} ....{ext}"
    # ============================================================
    # Metodo para Colocar en el Titulo Lo Que Deseemos que Hira, en este Caso el Titulo del Video
    # ============================================================
    def Actualizando_Title(self):

        if self.images == [] or self.images == "":
            pass

        else:

        	self.setWindowTitle("Slide_Image (E.X._v4.5) || ▶")

    # ============================================================
    # UI Y EVENTOS
    # ============================================================
    def create_context_menu(self):
        self.context_menu = QMenu(self)
        
        self.Ico_Menu = Path.resource_path('Ico\\jpeg.png')
        self.context_menu.addAction(QIcon(self.Ico_Menu), "📎 Archivos (Ctrl+I)", self.add_images).setShortcut('Ctrl+I')
        self.context_menu.addAction(QIcon(self.Ico_Menu), "📂 Carpeta (Ctrl+C)", self.add_images_carpeta).setShortcut('Ctrl+C')
        self.context_menu.addAction(QIcon(self.Ico_Menu), "📁 Directorio (Ctrl+D)", self.add_images_directorys).setShortcut('Ctrl+D')
        self.context_menu.addSeparator()
        self.context_menu.addAction(QIcon(self.Ico_Menu), "☁️ Base de Datos (Ctrl+B)", self.prompt_load_database).setShortcut('Ctrl+B')
        self.context_menu.addAction(QIcon(self.Ico_Menu), "☢️ Explorar QRC (Ctrl+R)", self.prompt_load_qrc).setShortcut('Ctrl+R')
        self.context_menu.addAction(QIcon(self.Ico_Menu), "☣️ Resources JSON (Ctrl+J)", self.prompt_load_json).setShortcut('Ctrl+J')
        self.context_menu.addSeparator()

        self.Ico_Menu = Path.resource_path('Ico\\2.png')
        self.context_menu.addAction(QIcon(self.Ico_Menu), "📍 Información del Soft-Ware (F1)", self.info_app).setShortcut('F1')
        self.context_menu.addAction(QIcon(self.Ico_Menu), "📍 Información Teclas de Atajos (Ctrl+K)", self.info_keys).setShortcut('Ctrl+K')
        self.context_menu.addSeparator()
        self.context_menu.addAction(QIcon(self.Ico_Menu), "📥 Guarda la Imagen (Ctrl+S)", self.Guardar_Imagen).setShortcut('Ctrl+S')
        self.context_menu.addAction(QIcon(self.Ico_Menu), "💨 Limpia y Restaura (Ctrl+L)", self.cleanear).setShortcut('Ctrl+L')
        self.context_menu.addAction(QIcon(self.Ico_Menu), "💻 Full Screnn Window (F11)", self.Pantalla_Completa).setShortcut('F11')
        self.context_menu.addSeparator()
        self.context_menu.addAction(QIcon(self.Ico_Menu), 'O Solo Arrastra y Suelta...')
        self.context_menu.addAction(QIcon(self.Ico_Menu), '[F11] Toogle [ESC] si esta Full')
        self.context_menu.addSeparator()

        self.Ico_Menu = Path.resource_path('Ico\\Salir.png')
        self.context_menu.addAction(QIcon(self.Ico_Menu), "❌ Cerrar (ESC)", self.close).setShortcut('Esc')
        
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(
            lambda pos: self.context_menu.exec_(self.mapToGlobal(pos))
        )

    def info_app(self):

        msn = '''
→ Este soft, es un Ejemplo tanto, en el Ingreso como en la Lectura, de distintos, Archivos, Pudiendo:
✓ Ingresar, Archivos, de 5 Formas Distintas, siendo la primera:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
• El Ingreso, por Menú Contextual, al Escoger, [Abrir con...]        
• El Segundo, Ingreso, es, con Drag & Drop, el cual es solamente, de Arrastrar y Soltar,        
• El Tercer Ingreso, es en Selección, Simple, es decir, Se seleccionan Archivos, de forma Normal,        
    • Con Soporte JXL (JPEG XL) con pillow_jxl - Tambien con (BLOB FILES)
• El Cuarto Ingreso, es por Carpeta, (Se Seleccióna, una Carpeta, Especifica, y 
  todo dentro de Si es Ingresado de Forma Automatica, sin Sub-Directrios, Dentro 
  de si)        
• El Quinto, Ingreso, es por Directorio (Se Selecciona, de forma, Normal, una 
  Carpeta la, cual está Tendra, dentro de si, Varias, Carpetas, más, con el mismo 
  Archivo, a ser Integrado y el Soft, Automaticamente, Ingresara, todos, los 
  Archivos, afines, dentro de si.)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
• Los que estaban al Pendiente, para este Ejemplo: 
  ☑️ 1ra) Carga directa de imágenes BLOB desde SQLite.
  ☑️ 2da) Carga directa de imágenes QRC: Selecciona resources_rc.py + su .qrc
  ☑️ 3ra) Carga imágenes desde JSON: Base64, URLs locales, o Data URIs
  ☑️ 4ta) Soporte JXL (JPEG XL) con pillow_jxl - Tambien con (BLOB FILES)
  ☑️ 5ta) Soporte JXL (JPEG XL) con pillow_jxl - Tambien con (JSON)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📎 Distribución: 
    → Gratuita, Open-Source, con Fines Eticos, y Para Estudio...

✔️ Información del Soft-Ware  ↔  (F1)"
✔️ Información Teclas de Atajos  ↔  (Ctrl+K)"
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📥 Guarda la Imagen no Importa de donde la este Cargando  ↔  (Ctrl+S)
💨 Limpia y Restaura a Valores de Innicio Todo  ↔  (Ctrl+L)
✔️ Full Screen Window  ↔  (F11)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

        '''

        QMessageBox.information(self,
                    "✓ INFO App", f"{msn}"
                )

    def info_keys(self):

        msn = ''' 
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🎯 Teclas de Atajo de en Teclado:

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

(Ctrl+I)  ↔  ☑️ Ingresar Archivos por Selección, Simple
(Ctrl+C)  ↔  ☑️ Ingresar Archivos por Carpeta
(Ctrl+D)  ↔  ☑️ Ingresar Archivos por Directorio
        
(Ctrl+B)  ↔  ☑️ Ingresar Archivos por Base de Datos
(Ctrl+R)  ↔  ☑️ Ingresar Archivos por Explorar QRC
(Ctrl+J)  ↔  ☑️ Ingresar Archivos por Resources JSON
       
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

TIPS:

(Ctrl+S)  ↔  📥 Guarda la Imagen no Importa de donde la este Cargando
(Ctrl+L)  ↔  💨 Limpia y Restaura a Valores de Innicio Todo
(F11)  ↔  ✔️ Full Screen Window

📌 En Caso de Que este Full Screen [F11] Toogle -| O |- [ESC]
     Pero si la Pantalla está Normal [ESC], Cierra la App.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🔥 Desarrollado, por: Cristian M. Veliz Cano.
🔥 Correo @: cristianvel2015mvc@gmail.com
📱 WhatsApp[ONLY-MESSAGE]: (+502) 4833-7746

(F1)  ↔  ✔️ Información del Soft-Ware
(Ctrl+K)  ↔  "✔️ Información Teclas de Atajos
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

        '''

        QMessageBox.information(self,
                    "✓ TECLAS DE ATAJO", f"{msn}"
                )

    ## Carga directa de imágenes BLOB desde SQLite.
    def prompt_load_database(self):
        """
        Carga directa de imágenes BLOB desde SQLite.
        Selecciona la BD y carga todas las imágenes automáticamente al visor.
        """
        # 1. Seleccionar base de datos
        db_path, _ = QFileDialog.getOpenFileName(
            self,
            "Seleccionar Base de Datos SQLite",
            "",
            "SQLite (*.db *.sqlite *.sqlite3);;Todos los archivos (*)"
        )
        if not db_path:
            return
        
        try:
            import sqlite3
            
            # 2. Conectar y detectar estructura automáticamente
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()
            
            # Obtener tablas
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
            tables = [t[0] for t in cursor.fetchall()]
            
            if not tables:
                QMessageBox.warning(self, "BD Vacía", "La base de datos no contiene tablas.")
                return
            
            # 3. Buscar tabla con imágenes (prioridad: images, imagenes, fotos, etc.)
            tabla = None
            columnas = []
            
            candidatas = [t for t in tables if t.lower() in ['images', 'imagenes', 'fotos', 'pictures', 'gallery', 'photos']]
            tablas_revisar = candidatas if candidatas else tables
            
            for t in tablas_revisar:
                try:
                    cursor.execute(f"PRAGMA table_info({t})")
                    cols = cursor.fetchall()
                    # Buscar tabla que tenga columna BLOB o similar
                    tiene_blob = any('blob' in c[2].lower() or c[2].upper() == 'BLOB' for c in cols)
                    if tiene_blob:
                        tabla = t
                        columnas = cols
                        break
                except:
                    continue
            
            if not tabla:
                QMessageBox.warning(self, "Sin imágenes", "No se encontró tabla con datos BLOB.")
                conn.close()
                return
            
            # 4. Detectar columnas automáticamente
            col_nombre = None
            col_blob = None
            
            for col in columnas:
                col_name = col[1]
                col_type = col[2].upper()
                
                # Detectar columna de nombre
                if any(k in col_name.lower() for k in ['name', 'nombre', 'filename', 'file', 'titulo', 'title']):
                    col_nombre = col_name
                # Detectar columna BLOB
                elif 'BLOB' in col_type:
                    col_blob = col_name
            
            # Si no detectó nombre, usar primera columna de texto
            if not col_nombre:
                for col in columnas:
                    if 'TEXT' in col[2].upper() or 'VARCHAR' in col[2].upper():
                        col_nombre = col[1]
                        break
            
            # Si no detectó blob, buscar cualquier columna que pueda ser blob
            if not col_blob:
                for col in columnas:
                    if 'BLOB' in col[2].upper() or 'DATA' in col[1].upper():
                        col_blob = col[1]
                        break
            
            if not col_blob:
                QMessageBox.warning(self, "Error", "No se encontró columna BLOB en la tabla.")
                conn.close()
                return
            
            # Usar defaults si no hay nombre
            if not col_nombre:
                col_nombre = col_blob  # usar el blob como fallback
            
            # 5. Cargar TODAS las imágenes directamente
            cursor.execute(f"SELECT {col_nombre}, {col_blob} FROM {tabla}")
            registros = cursor.fetchall()
            
            conn.close()
            
            if not registros:
                QMessageBox.warning(self, "Sin Datos", "La tabla no contiene registros.")
                return
            
            # 6. Cargar en el visor (VERIFICACIÓN CORREGIDA CON SOPORTE JXL)
            self.images.clear()
            self.current_index = 0
            
            for nombre, blob_data in registros:
                if blob_data and isinstance(blob_data, (bytes, memoryview)):
                    display_name = str(nombre) if nombre else f"imagen_{len(self.images)+1}.jpg"
                    
                    # ✅ VERIFICACIÓN CORREGIDA: Detecta si es imagen válida (incluye JXL)
                    if self._is_valid_image_blob(blob_data, display_name):
                        self.images.append(('blob', display_name, blob_data))
            
            if self.images:
                self.mousePressEvent()
                self.update_image()
                QMessageBox.information(self, "BD Cargada", 
                    f"🗃️ {len(self.images)} imágenes cargadas de '{tabla}'\n"
                    f"💾 Columnas: {col_nombre}, {col_blob}\n"
                    f"📁 {os.path.basename(db_path)}")
            else:
                QMessageBox.warning(self, "Sin Imágenes", 
                    "No se encontraron imágenes válidas en la base de datos.")
                
        except sqlite3.Error as e:
            QMessageBox.critical(self, "Error SQLite", f"Error en base de datos:\n{str(e)}")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error inesperado:\n{str(e)}")

        finally:
            self.mousePressEvent()
            self.update_image()

    # ============================================================
    # MÉTODO NUEVO: Verificación universal de imágenes (incluye JXL)
    # ============================================================
    def _is_valid_image_blob(self, blob_data, filename=""):
        """
        Verifica si un BLOB es una imagen válida (PNG, JPG, BMP, GIF, WEBP, JXL, etc.)
        """
        try:
            # Si tiene extensión JXL o magic bytes de JXL
            if filename.lower().endswith('.jxl') or blob_data[:2] == b'\xff\x0a':
                # Verificar que pillow_jxl pueda decodificarlo
                try:
                    from pillow_jxl import Decoder
                    decoder = Decoder()
                    info, _ = decoder(blob_data)
                    return True
                except:
                    return False
            
            # Para otros formatos, usar QPixmap
            test_pixmap = QPixmap()
            if test_pixmap.loadFromData(blob_data):
                return True
                
        except Exception as e:
            print(f"Error verificando imagen: {e}")
        
        return False

    ## Explorador de QRC: Selecciona resources_rc.py + su .qrc
    def prompt_load_qrc(self):
	    """
	    Explorador de QRC: Selecciona resources_rc.py + su .qrc 
	    y carga todas las imágenes directamente en memoria (sin extraer)
	    """
	    
	    # 1. Seleccionar el resources_rc.py
	    rc_file, _ = QFileDialog.getOpenFileName(
	        self,
	        "Seleccionar resources_rc.py compilado",
	        "",
	        "Python Module (*.py)"
	    )
	    if not rc_file:
	        return
	    
	    # 2. Buscar el QRC asociado (mismo nombre)
	    base = os.path.splitext(rc_file)[0]
	    qrc_file = base + ".qrc"
	    
	    # Si no existe, pedirlo
	    if not os.path.exists(qrc_file):
	        qrc_file, _ = QFileDialog.getOpenFileName(
	            self,
	            "Seleccionar archivo QRC (XML)",
	            os.path.dirname(rc_file),
	            "QRC Files (*.qrc)"
	        )
	    
	    if not qrc_file or not os.path.exists(qrc_file):
	        QMessageBox.warning(self, "Se necesita QRC", 
	            "Necesito el archivo .qrc para saber qué imágenes contiene el módulo.")
	        return
	    
	    # 3. Parsear el QRC para obtener lista de recursos
	    import xml.etree.ElementTree as ET
	    
	    try:
	        tree = ET.parse(qrc_file)
	        root = tree.getroot()
	        
	        resource_paths = []  # Lista de paths Qt: :/prefijo/ruta/imagen.png
	        
	        for qresource in root.findall('qresource'):
	            prefix = qresource.get('prefix', '')
	            if prefix and not prefix.startswith('/'):
	                prefix = '/' + prefix
	            
	            for file_elem in qresource.findall('file'):
	                file_path = file_elem.text
	                if file_path:
	                    # Construir path Qt completo
	                    qt_path = f":{prefix}/{file_path}" if prefix else f":/{file_path}"
	                    resource_paths.append(qt_path)
	        
	    except Exception as e:
	        QMessageBox.critical(self, "Error QRC", f"No se pudo leer el XML:\n{str(e)}")
	        return
	    
	    if not resource_paths:
	        QMessageBox.warning(self, "Vacio", "El QRC no contiene archivos.")
	        return
	    
	    # 4. Importar el resources_rc.py para registrar recursos en Qt
	    import importlib.util
	    
	    module_name = f"qrc_viewer_{os.path.basename(base)}"
	    try:
	        spec = importlib.util.spec_from_file_location(module_name, rc_file)
	        module = importlib.util.module_from_spec(spec)
	        spec.loader.exec_module(module)
	    except Exception as e:
	        QMessageBox.critical(self, "Error", f"No se pudo cargar el módulo:\n{str(e)}")
	        return
	    
	    # 5. Cargar imágenes en el visor (solo las que son imágenes)
	    self.images.clear()
	    self.current_index = 0
	    
	    image_exts = ('.png', '.jpg', '.jpeg', '.bmp', '.gif', '.webp', '.ico', '.svg', '.tiff', '.jxl')
	    
	    for qt_path in resource_paths:
	        # Verificar si es imagen por extensión
	        ext = os.path.splitext(qt_path)[1].lower()
	        if ext in image_exts:
	            # Nombre para mostrar (solo el archivo, no el path completo)
	            display_name = os.path.basename(qt_path)
	            self.images.append(('qrc', display_name, qt_path))
	    
	    if self.images:
	    	self.mousePressEvent()
	    	self.update_image()
	    	QMessageBox.information(self, "QRC Cargado", 
	            f"📦 {len(self.images)} imágenes listas para visualizar\n"
	            f"💾 Sin extraer archivos, todo en memoria")

	    	self.mousePressEvent()
	    	self.update_image()

	    else:
	        QMessageBox.warning(self, "Sin imágenes", 
	            "El QRC no contiene imágenes reconocibles.")

    ## Carga imágenes desde JSON: Base64, URLs locales, o Data URIs (CON VERIFICACIÓN JXL)
    def prompt_load_json(self):
        """Carga imágenes desde JSON: Base64, URLs locales, o Data URIs"""
        
        json_path, _ = QFileDialog.getOpenFileName(
            self, "Seleccionar JSON", "", "JSON (*.json)"
        )
        if not json_path:
            return
        
        base_dir = os.path.dirname(json_path)
        
        try:
            with open(json_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            self.images.clear()
            self.current_index = 0
            
            # Buscar imágenes recursivamente en cualquier estructura
            def buscar_imagenes(obj):
                """Busca imágenes en cualquier parte del JSON"""
                if isinstance(obj, dict):
                    # Caso 1: Base64 directo (formato Image JSON Manager)
                    if 'data' in obj and isinstance(obj['data'], str):
                        nombre = obj.get('nombre') or obj.get('name') or f"img_{len(self.images)+1}.png"
                        try:
                            b64 = obj['data']
                            # Limpiar Data URI si existe (data:image/png;base64,...)
                            if ',' in b64:
                                b64 = b64.split(',')[1]
                            
                            blob = base64.b64decode(b64)
                            
                            # ✅ VERIFICACIÓN: Detecta formato real (incluye JXL)
                            if self._is_valid_image_blob(blob, nombre):
                                # Detectar si es JXL para poner extensión correcta
                                if blob[:2] == b'\xff\x0a' and not nombre.lower().endswith('.jxl'):
                                    nombre += '.jxl'
                                self.images.append(('json', nombre, blob))
                                
                        except Exception as e:
                            print(f"Error decodificando base64: {e}")
                    
                    # Caso 2: URL o Path local
                    for key in ['url', 'path', 'src', 'file', 'ruta']:
                        if key in obj and isinstance(obj[key], str):
                            img_path = obj[key]
                            
                            # Si es URL absoluta, descargar
                            if img_path.startswith(('http://', 'https://')):
                                try:
                                    img_data = urllib.request.urlopen(img_path, timeout=5).read()
                                    nombre = os.path.basename(img_path) or f"web_{len(self.images)}.jpg"
                                    
                                    # Verificar que sea imagen válida (incluye JXL)
                                    if self._is_valid_image_blob(img_data, nombre):
                                        self.images.append(('json', nombre, img_data))
                                except Exception as e:
                                    print(f"Error descargando URL: {e}")
                            
                            # Si es ruta relativa/absoluta local
                            else:
                                if not os.path.isabs(img_path):
                                    img_path = os.path.join(base_dir, img_path)
                                
                                if os.path.exists(img_path):
                                    # Detectar JXL por extensión
                                    if img_path.lower().endswith('.jxl'):
                                        try:
                                            with open(img_path, 'rb') as f:
                                                jxl_data = f.read()
                                            if self._is_valid_image_blob(jxl_data, img_path):
                                                self.images.append(('jxl', os.path.basename(img_path), img_path))
                                        except:
                                            pass
                                    else:
                                        # Verificar otros formatos
                                        test = QPixmap()
                                        if test.load(img_path):
                                            self.images.append(('file', os.path.basename(img_path), img_path))
                    
                    # Recursión en sub-objetos
                    for v in obj.values():
                        buscar_imagenes(v)
                        
                elif isinstance(obj, list):
                    for item in obj:
                        buscar_imagenes(item)
            
            # Iniciar búsqueda
            buscar_imagenes(data)
            
            if self.images:
                self.mousePressEvent()
                self.update_image()
                
                # Contar tipos para mensaje detallado
                tipos = {}
                for tipo, _, _ in self.images:
                    tipos[tipo] = tipos.get(tipo, 0) + 1
                
                msg = f"📄 {len(self.images)} imágenes encontradas\n\n"
                msg += "Desglose:\n"
                for tipo, cantidad in tipos.items():
                    emoji = {'json': '📄', 'file': '📁', 'jxl': '🖼️', 'blob': '💾'}.get(tipo, '📎')
                    msg += f"  {emoji} {tipo.upper()}: {cantidad}\n"
                
                QMessageBox.information(self, "JSON Cargado", msg)
            else:
                QMessageBox.warning(self, "Sin imágenes", 
                    "No se encontraron imágenes. Formatos soportados:\n"
                    "• Base64: {\"data\": \"iVBORw0KGgo...\", \"nombre\": \"img.png\"}\n"
                    "• Base64 JXL: {\"data\": \"...\", \"nombre\": \"img.jxl\"}\n"
                    "• Archivo: {\"path\": \"imagen.png\"}\n"
                    "• Archivo JXL: {\"path\": \"imagen.jxl\"}\n"
                    "• URL: {\"url\": \"http://...\"}")
                
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error al cargar JSON:\n{str(e)}")

    def dragEnterEvent(self, event: QDragEnterEvent):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dropEvent(self, event: QDropEvent):
        for url in event.mimeData().urls():
            if url.isLocalFile():
                path = url.toLocalFile()
                if path.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif', '.webp', '.ico', '.jxl')):
                    self.images.append(('file', os.path.basename(path), path))
        self.mousePressEvent()
        self.update_image()

    def mousePressEvent(self, event=None):
        if self.timer.isActive():
            self.timer.stop()
            self.paused = True
            ImageSlider.Actualizando_Title(self)
        else:
            self.timer.start(5000)
            self.paused = False
            ImageSlider.Actualizando_Title(self)
        self.update_image()

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.left_button.move(25, self.height() // 2 - 25)
        self.right_button.move(self.width() - 75, self.height() // 2 - 25)
        if self.images:
            self.mousePressEvent()
            self.update_image()

    def center_on_screen(self):
        screen = QApplication.primaryScreen().availableGeometry()
        self.setGeometry((screen.width() - 800) // 2, (screen.height() - 600) // 2, 800, 600)

    # ============================================================
    # MÉTODOS DE COPIAR AL PORTAPAPELES, LA IMAGEN CON CRTL+C, CERRAR APP, (ATRAS -|- ADELANTE)
    # ============================================================
    def keyPressEvent(self, event):

        if event.key() == Qt.Key_Escape:
            if self.Full_Screnn_Window:
                self.Pantalla_Completa()
            else:
                self.close()

        elif event.key() == Qt.Key_Left:
            self.previous_image()

        elif event.key() == Qt.Key_Right:
            self.next_image()

        elif event.key() == Qt.Key_C and event.modifiers() == Qt.ControlModifier:
	        if self.current_pixmap:
	            QtWidgets.QApplication.clipboard().setPixmap(self.current_pixmap)
	            QMessageBox.information(self, "Copiado", "📋 Imagen copiada al portapapeles")

    # ============================================================
    # MÉTODOS PARA (📥 Guardar la Imagen no Importa de donde la este Cargando  ↔  (Ctrl+S))
    # ============================================================
    def Guardar_Imagen(self):

        if not self.images or self.current_index >= len(self.images):
            self.label.setText("Arrastra imágenes o usa el menú derecho")
            return        

        nombre_path, _ = QFileDialog.getSaveFileName(self, "Guardar como", "",(
            "PNG(* .png) ;; JPG(* .jpg) ;; ICO(* .ico) ;; BMP(* .bmp) ;; All Files(*.*)"))
        
        if nombre_path:
            if self.current_pixmap:

                self.current_pixmap.save(nombre_path, "PNG")

                if self.current_pixmap:
                    QMessageBox.information(self, "Guardar gráfico", "Gráfico guardado con éxito.", QMessageBox.Ok)
                else:
                    QMessageBox.critical(self, "Guardar gráfico", "Error al guardar el gráfico.", QMessageBox.Ok)

    # ============================================================
    # MÉTODOS PARA (✔️ Limpiar y Restaurar a Valores de Innicio Todo  ↔  (Ctrl+L)
    # ============================================================
    def cleanear(self):

        self.in_im = ""
        self.images = []
        self.current_index = 0
        self.current_pixmap = None
        self.paused = False

        self.mousePressEvent()
        self.setWindowTitle('Slide_Image (E.X._v4.5)')

        pixmap = QPixmap("")
        self.label.setPixmap(pixmap)

    # ============================================================
    # MÉTODO PARA (✔️ Full Screen Window  ↔  (F11)
    # ============================================================
    def Pantalla_Completa(self):
        """Alternar modo pantalla completa"""
        if not self.Full_Screnn_Window:
            self.Full_Screnn_Window = True
            self.showFullScreen()
        else:
            self.Full_Screnn_Window = False
            self.Esconder = False
            self.showNormal()

# ============================================================
# MAIN - CORREGIDO: High DPI ANTES de QApplication
# ============================================================
if __name__ == '__main__':
    # ✅ ESTO VA PRIMERO (antes de QApplication)
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)
    
    # ✅ DESPUÉS creamos la app
    app = QApplication(sys.argv)
    
    in_im = sys.argv[1] if len(sys.argv) > 1 else None
    ex = ImageSlider(in_im)
    ex.show()
    sys.exit(app.exec_())