from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import ttk
import sqlite3
import networkx as nx
import matplotlib.pyplot as plt

#miConexion=sqlite3.connect("JorgeShop")
#miCursor=miConexion.cursor()
conn = sqlite3.connect('JorgeShop.db')
cursor = conn.cursor()

def conexionBBDD():
    
        messagebox.showinfo("Ingreso","Se ah ingresado correctamente")


def salirAplicacion():
    valor=messagebox.askquestion("Salir","Desea salir de la app?")
    if valor=="yes":
        root.destroy()

def ventana_cliente():
    cliente_window = tk.Toplevel(root)
    cliente_window.title("Crear Cliente")
    cliente_window.geometry('200x200')

    labeldni = ttk.Label(cliente_window, text="DNI:")
    labeldni.grid(row=0, column=0, sticky="W")

    entradadni = ttk.Entry(cliente_window,textvariable=miDni)
    entradadni.grid(row=0, column=1, sticky="EW")
    

    labelnomb = ttk.Label(cliente_window, text="Nombre:")
    labelnomb.grid(row=1, column=0, sticky="W")

    entradanomb = ttk.Entry(cliente_window,textvariable=miNombre)
    entradanomb.grid(row=1, column=1, sticky="EW")

    
    # Añadimos los botones
    button1 = ttk.Button(cliente_window, text="Borrar", command=borrar_cliente)
    button1.grid(row=2, column=0, sticky="EW")

    button2 = ttk.Button(cliente_window, text="Modificar", command=actualizar_cliente)
    button2.grid(row=2, column=1, sticky="EW")

    button3 = ttk.Button(cliente_window, text="Crear",command=crear_cliente)
    button3.grid(row=3, column=0, sticky="EW")

    button4 = ttk.Button(cliente_window, text="Limpiar", command=limpiarCampos)
    button4.grid(row=3, column=1, sticky="EW")

    button5 = ttk.Button(cliente_window, text="Listar clientes", command=listar_clientes)
    button5.grid(row=3, column=1, sticky="EW")

def ventana_ordenes():
    orden_window = tk.Toplevel(root)
    orden_window.title("Generar ordenes")
    orden_window.geometry('200x200')
    
    # Combobox para seleccionar el distrito de destino
    cursor.execute("SELECT id_localidad FROM localidad")
    distritos = [distrito[0] for distrito in cursor.fetchall()]
    distrito_combobox = ttk.Combobox(orden_window, values=distritos)
    distrito_combobox.grid(row=3, column=1)
    DistritoO = distrito_combobox.get()
        
    cursor.execute("SELECT dni FROM cliente")
    dni = [dni[0] for dni in cursor.fetchall()]
    dni_combobox = ttk.Combobox(orden_window, values=dni)
    dni_combobox.grid(row=0, column=1)
    DNIO = dni_combobox.get()

    cursor.execute("SELECT id_producto FROM producto")
    producto = [producto[0] for producto in cursor.fetchall()]
    producto_combobox = ttk.Combobox(orden_window, values=producto)
    producto_combobox.grid(row=1, column=1)
    ProductoO = producto_combobox.get()

    labelcliente = ttk.Label(orden_window, text="DNI:")
    labelcliente.grid(row=0, column=0, sticky="W")
    
    labelproducto = ttk.Label(orden_window, text="Producto:")
    labelproducto.grid(row=1, column=0, sticky="W")

    labelcant = ttk.Label(orden_window, text="Cantidad:")
    labelcant.grid(row=2, column=0, sticky="W")

    entradacant = ttk.Entry(orden_window,textvariable=miCantidadO)
    entradacant.grid(row=2, column=1, sticky="EW")
    
    labellocalidad = ttk.Label(orden_window, text="Localidad")
    labellocalidad.grid(row=3, column=0, sticky="W")

    # Añadimos los botones
    button3 = ttk.Button(orden_window, text="Crear",command=crear_orden)
    button3.grid(row=4, column=1, sticky="EW")

    button4 = ttk.Button(orden_window, text="Limpiar", command=limpiarCampos)
    button4.grid(row=5, column=1, sticky="EW")

    button5 = ttk.Button(orden_window, text="Listar ordenes", command=listar_orden)
    button5.grid(row=6, column=1, sticky="EW")

def ventana_producto():
    producto_window = tk.Toplevel(root)
    producto_window.title("Crear Producto")
    producto_window.geometry("400x200")

    labelproducto = ttk.Label(producto_window, text="ID Producto:")
    labelproducto.grid(row=0, column=0, sticky="W")

    entradaidprod = ttk.Entry(producto_window,textvariable=miIdProducto)
    entradaidprod.grid(row=0, column=2, sticky="EW")
    
    labelnombprod = ttk.Label(producto_window, text="Nombre del producto:")
    labelnombprod.grid(row=1, column=0, sticky="W")

    entradanombprod = ttk.Entry(producto_window,textvariable=miProducto)
    entradanombprod.grid(row=1, column=2, sticky="EW")
    
    labelprecio = ttk.Label(producto_window, text="Precio:")
    labelprecio.grid(row=2, column=0, sticky="W")

    entradaprecio = ttk.Entry(producto_window,textvariable=miPrecio)
    entradaprecio.grid(row=2, column=2, sticky="EW")
    
    # Añadimos los botones
    button1 = ttk.Button(producto_window, text="Borrar",command=borrar_producto)
    button1.grid(row=3, column=0, sticky="EW")

    button2 = ttk.Button(producto_window, text="Modificar", command=actualizar_producto)
    button2.grid(row=3, column=2, sticky="EW")

    button3 = ttk.Button(producto_window, text="Crear", command=crear_producto)
    button3.grid(row=4, column=0, sticky="EW")

    button4 = ttk.Button(producto_window, text="Limpiar", command=limpiarCampos)
    button4.grid(row=4, column=2, sticky="EW")

    button5= ttk.Button(producto_window, text="Listar Productos", command=listar_productos)
    button5.grid(row=5, column=1, sticky="EW")

def ventana_localidad():
    localidad_window = tk.Toplevel(root)
    localidad_window.title("Crear Localidad")

    labelnombloc = ttk.Label(localidad_window, text="Nombre:")
    labelnombloc.grid(row=0, column=0, sticky="W")

    entradanombloc= ttk.Entry(localidad_window,textvariable=miLocalidad)
    entradanombloc.grid(row=0, column=1, sticky="EW")

    labelorigen = ttk.Label(localidad_window, text="Origen:")
    labelorigen.grid(row=1, column=0, sticky="W")

    entradaorigen = ttk.Entry(localidad_window,textvariable=miOrigen)
    entradaorigen.grid(row=1, column=1, sticky="EW")
    
    labeldist = ttk.Label(localidad_window, text="Distancia:")
    labeldist.grid(row=2, column=0, sticky="W")

    entradadist = ttk.Entry(localidad_window,textvariable=miDistancia)
    entradadist.grid(row=2, column=1, sticky="EW")

    # Añadimos los botones
    button1 = ttk.Button(localidad_window, text="Borrar", command=borrar_localidad)
    button1.grid(row=3, column=0, sticky="EW")

    button2 = ttk.Button(localidad_window, text="Modificar", command=actualizar_localidad)
    button2.grid(row=3, column=1, sticky="EW")

    button3 = ttk.Button(localidad_window, text="Crear", command=crear_localidad)
    button3.grid(row=4, column=0, sticky="EW")

    button4 = ttk.Button(localidad_window, text="Limpiar", command=limpiarCampos)
    button4.grid(row=4, column=1, sticky="EW")

    button5= ttk.Button(localidad_window, text="Listar Localidades", command=listar_localidad)
    button5.grid(row=5, column=1, sticky="EW")

    


def limpiarCampos():
    miDni.set("")
    miNombre.set("")
    miDistancia.set("")
    miIdProducto.set("")
    miOrigen.set("")
    miPrecio.set("")
    miLocalidad.set("")
    miProducto.set("")
   
def listar_productos():
    miConexion = sqlite3.connect("JorgeShop.db")
    miCursor = miConexion.cursor()
    miCursor.execute("SELECT * FROM producto ORDER BY id_producto ASC") 
    productos = miCursor.fetchall()
    miConexion.close()
    
    ventana_lista = tk.Toplevel(root)
    ventana_lista.title("Lista de Productos")

    lista_productos = ttk.Treeview(ventana_lista, columns=("ID", "Nombre", "Precio"))
    lista_productos.heading("#1", text="ID")
    lista_productos.heading("#2", text="Nombre")
    lista_productos.heading("#3", text="Precio")
    
    for producto in productos:
        lista_productos.insert("", "end", values=producto)
    
    lista_productos.pack()

def listar_localidad():
    miConexion = sqlite3.connect("JorgeShop.db")
    miCursor = miConexion.cursor()
    miCursor.execute("SELECT * FROM localidad") 
    localidades = miCursor.fetchall()
    miConexion.close()
    
    ventana_lista = tk.Toplevel(root)
    ventana_lista.title("Lista de localidades")

    lista_localidades = ttk.Treeview(ventana_lista, columns=("ID", "Nombre","Origen","Distancia"))
    lista_localidades.heading("#1", text="id")
    lista_localidades.heading("#2", text="Nombre")
    lista_localidades.heading("#3", text="origen")
    lista_localidades.heading("#4", text="distancia")
   
    
    for localidad in localidades:
        lista_localidades.insert("", "end", values=localidad)
    
 
    lista_localidades.pack()

def listar_clientes():
    miConexion = sqlite3.connect("JorgeShop.db")
    miCursor = miConexion.cursor()
    miCursor.execute("SELECT * FROM cliente") 
    clientes = miCursor.fetchall()
    miConexion.close()
    
    ventana_lista = tk.Toplevel(root)
    ventana_lista.title("Lista de clientes")

    lista_clientes = ttk.Treeview(ventana_lista, columns=("DNI", "Nombre"))
    lista_clientes.heading("#1", text="DNI")
    lista_clientes.heading("#2", text="Nombre")
   
    
    for cliente in clientes:
        lista_clientes.insert("", "end", values=cliente)
    
 
    lista_clientes.pack()

def crear_orden():
    # Conecta a la base de datos
    miConexion = sqlite3.connect("JorgeShop.db")
    miCursor = miConexion.cursor()
    
    # Obtiene los valores de los campos
    dni = dni_combobox.get()
    nombreloc = distrito_combobox.get()
    producto = producto_combobox.get()
    cantidad = miCantidadO.get()

    if not nombreloc or not dni or not cantidad or not producto:
        error = messagebox.showerror("Error", "Debes completar todos los campos")
    else:
        # Inserta los valores en la base de datos, sin especificar el campo ID
        miCursor.execute("INSERT INTO orden (id_producto, dni_cliente, id_districto, cantidad) VALUES (?, ?, ?, ?)", (ProductoO, DNIO, DistritoO, cantidad))
        miConexion.commit()
        messagebox.showinfo("Orden registrada", "Registro ingresado")
  

def listar_orden():
    pass



def crear_localidad():
    # Conecta a la base de datos (asegúrate de que esta parte esté completa)
    miConexion = sqlite3.connect("JorgeShop.db")
    miCursor = miConexion.cursor()
    
    # Obtiene los valores de los campos
    nombreloc = miLocalidad.get()
    origen = miOrigen.get()
    distancia = miDistancia.get()
    
    # Verifica si los campos están vacíos
    if not nombreloc or not origen or not distancia:
        error = messagebox.showerror("Error", "Debes completar todos los campos")
    else:
        # Inserta los valores en la base de datos, sin especificar el campo ID
        miCursor.execute("INSERT INTO localidad (nombre, origen, distancia) VALUES (?, ?, ?)", (nombreloc, origen, distancia))
        miConexion.commit()
        messagebox.showinfo("Localidad", "Registro ingresado")
    

def actualizar_localidad():
    miConexion = sqlite3.connect("JorgeShop.db")
    miCursor = miConexion.cursor()
    try:
        # Utiliza marcadores de posición y una tupla de parámetros
        miCursor.execute("UPDATE localidad SET origen=?,distancia=? WHERE nombre=?", (miOrigen.get(),miDistancia.get(),miLocalidad.get()))
        if miCursor.rowcount == 0:
            messagebox.showerror("Error", "Nombre inexistente")
        else:
            miConexion.commit()
            messagebox.showinfo("Localidad", "Registro Actualizado")
    except:
        messagebox.showerror("Fatal", "Error en la actualización")

def borrar_localidad():
    miConexion = sqlite3.connect("JorgeShop.db")
    miCursor = miConexion.cursor()
    try:
        # Utiliza la sentencia DELETE con un marcador de posición
        miCursor.execute("DELETE FROM localidad WHERE nombre=?", (miLocalidad.get(),))
        if miCursor.rowcount == 0:
            messagebox.showerror("Error", "Localidad inexistente")
        else:
            miConexion.commit()
            messagebox.showinfo("Localidad", "Registro Borrado")
    except:
        messagebox.showerror("Fatal", "No se pudo borrar el registro")

def crear_producto():
    # Conecta a la base de datos (asegúrate de que esta parte esté completa)
    miConexion = sqlite3.connect("JorgeShop.db")
    miCursor = miConexion.cursor()
    
    # Obtiene los valores de los campos
    idprod= miIdProducto.get()
    nombre = miProducto.get()
    precio=miPrecio.get()

    
    # Verifica si los campos están vacíos
    if not idprod or not nombre or not precio:
        error=messagebox.showerror("Error", "Debes completar todos los campos")

    else:
        # Inserta los valores en la base de datos
        miCursor.execute("INSERT INTO producto VALUES (?, ?, ?)", (idprod, nombre,precio))
        miConexion.commit()
        messagebox.showinfo("Producto", "Registro ingresado")

def actualizar_producto():
    miConexion = sqlite3.connect("JorgeShop.db")
    miCursor = miConexion.cursor()
    try:
        # Utiliza marcadores de posición y una tupla de parámetros
        miCursor.execute("UPDATE producto SET nombre=?, precio=? WHERE id_producto=?", (miProducto.get(), miPrecio.get(), miIdProducto.get()))
        if miCursor.rowcount == 0:
            messagebox.showerror("Error", "ID inexistente")
        else:
            miConexion.commit()
            messagebox.showinfo("Producto", "Registro Actualizado")
    except:
        messagebox.showerror("Fatal", "Error en la actualización")

def borrar_producto():
    miConexion = sqlite3.connect("JorgeShop.db")
    miCursor = miConexion.cursor()
    try:
        # Utiliza la sentencia DELETE con un marcador de posición
        miCursor.execute("DELETE FROM producto WHERE id_producto=?", (miIdProducto.get(),))
        if miCursor.rowcount == 0:
            messagebox.showerror("Error", "ID inexistente")
        else:
            miConexion.commit()
            messagebox.showinfo("Producto", "Registro Borrado")
    except:
        messagebox.showerror("Fatal", "No se pudo borrar el registro")

def crear_cliente():
    # Conecta a la base de datos (asegúrate de que esta parte esté completa)
    miConexion = sqlite3.connect("JorgeShop.db")
    miCursor = miConexion.cursor()
    
    # Obtiene los valores de los campos
    dni = miDni.get()
    nombre = miNombre.get()
    
    # Verifica si los campos están vacíos
    if not dni or not nombre:
        error=messagebox.showerror("Error", "Debes completar todos los campos")

    else:
        # Inserta los valores en la base de datos
        miCursor.execute("INSERT INTO cliente VALUES (?, ?)", (dni, nombre))
        miConexion.commit()
        messagebox.showinfo("Cliente", "Registro ingresado")

def actualizar_cliente():
    miConexion = sqlite3.connect("JorgeShop.db")
    miCursor = miConexion.cursor()
    try:
        # Utiliza marcadores de posición y una tupla de parámetros
        miCursor.execute("UPDATE cliente SET nombre=? WHERE dni=?", (miNombre.get(),miDni.get()))
        if miCursor.rowcount == 0:
            messagebox.showerror("Error", "DNI inexistente")
        else:
            miConexion.commit()
            messagebox.showinfo("Producto", "Registro Actualizado")
    except:
        messagebox.showerror("Fatal", "Error en la actualización")

def borrar_cliente():
    miConexion = sqlite3.connect("JorgeShop.db")
    miCursor = miConexion.cursor()
    try:
        # Utiliza la sentencia DELETE con un marcador de posición
        miCursor.execute("DELETE FROM cliente WHERE DNI=?", (miDni.get(),))
        if miCursor.rowcount == 0:
            messagebox.showerror("Error", "DNI inexistente")
        else:
            miConexion.commit()
            messagebox.showinfo("Cliente", "Registro Borrado")
    except:
        messagebox.showerror("Fatal", "No se pudo borrar el registro")

def mostrar_grafo():
    G = nx.Graph()
    cursor.execute("SELECT Nombre, Origen, Distancia FROM localidad")
    distritos = cursor.fetchall()
    for distrito in distritos:
        G.add_node(distrito[0])
        G.add_edge(distrito[0], distrito[1], weight=distrito[2])
    
    pos = nx.spring_layout(G)
    labels = nx.get_edge_attributes(G, 'weight')
    
    plt.figure(figsize=(8, 8))
    nx.draw(G, pos, with_labels=True, node_size=3000, node_color='lightblue')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.title("Grafo de Distritos")
    plt.axis('off')
    plt.show()

root = Tk()

miDni=StringVar()
miNombre=StringVar()
miLocalidad=StringVar()
miOrigen=StringVar()
miDistancia=StringVar()
miIdProducto=StringVar()
miProducto=StringVar()
miPrecio=StringVar()
DNIO=StringVar()
ProductoO=StringVar()
miCantidadO=StringVar()
DistritoO=StringVar()
dni_combobox=StringVar()
distrito_combobox =StringVar()
producto_combobox=StringVar()


bg_image = Image.open("imagen_fondo_jorgeshop.jpeg")  # Reemplaza "ruta_de_tu_imagen.jpg" con la ubicación de tu imagen de fondo
bg_photo = ImageTk.PhotoImage(bg_image)
background_label = Label(root, image=bg_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

root.geometry("500x450")
root.title("Tienda")
barraMenu=Menu(root)
root.config(menu=barraMenu,width=300,height=300)

#añado elementos al menu
bbddMenu=Menu(barraMenu,tearoff=0)
bbddMenu.add_command(label="Conectar",command=conexionBBDD)
bbddMenu.add_command(label="Salir",command=salirAplicacion)

#añado elementos al menu
'''crudMenu=Menu(barraMenu,tearoff=0)
crudMenu.add_command(label="Insertar",command=crear)
crudMenu.add_command(label="Actualizar",command=actualizar)
crudMenu.add_command(label="Eliminar")
crudMenu.add_command(label="Consultar",command=leer)'''

#añado elementos al menu

#añado cada elemento al menu
barraMenu.add_cascade(label="Ingreso",menu=bbddMenu)
barraMenu.add_cascade(label="Clientes",command=ventana_cliente)
barraMenu.add_cascade(label="Productos",command=ventana_producto)
barraMenu.add_cascade(label="Ordenes", command=ventana_ordenes)
barraMenu.add_cascade(label="Localidades",command=ventana_localidad)
barraMenu.add_cascade(label="Mostrar rutas",command=mostrar_grafo)

#añado otro frame
miFrame=Frame(root)
miFrame.pack()

#agrego los botones con otro frame
miFrame2=Frame(root)
miFrame2.pack()

def mostrar_grafo():
    G = nx.Graph()
    cursor.execute("SELECT Nombre, Origen, Distancia FROM localidad")
    distritos = cursor.fetchall()
    for distrito in distritos:
        G.add_node(distrito[0])
        G.add_edge(distrito[0], distrito[1], weight=distrito[2])
    
    pos = nx.spring_layout(G)
    labels = nx.get_edge_attributes(G, 'weight')
    
    plt.figure(figsize=(8, 8))
    nx.draw(G, pos, with_labels=True, node_size=2000, node_color='lightblue')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.title("Grafo de Distritos")
    plt.axis('off')
    plt.show()





































root.mainloop()

