#################################################################################
# Copyright (C) 2026 Binryan-void
#
# Este programa es software libre: puedes redistribuirlo y/o modificarlo
# bajo los terminos de la Licencia Publica General GNU publicada por la 
# Free Software Foundation, ya sea la version 3 de la Licencia o 
# (a tu eleccion) cualquier version posterior
#
# Este programa se distribuye con la esperanza de que sea util, pero 
# SIN GARANTIA ALGUNA; ni siquiera garantia implicita de 
# MERCANTILIDAD o APTITUD PARA UN PROPOSITO DETERMINADO.
# Consulte la Licencia Publica General GNU para obtener mas detalles.
#
# Deberias haber recibido una copia de la Licencia Publica General GNU 
# junto con este programa. Si no es asi, consulta <https://www.gnu.org/licenses/>.
##################################################################################

import subprocess
import time
import sqlite3
import os
db_dir = 'db'
if not os.path.exists(db_dir):
    os.makedirs(db_dir)
conn = sqlite3.connect(os.path.join(db_dir, 'golden_data.db'))
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS golden (
    id INTEGER PRIMARY KEY,
    producto TEXT NOT NULL,
    precio INTEGER NOT NULL
    )
''')
def nuevo():
    cursor.execute("DELETE FROM golden WHERE 1=1;")
    conn.commit()
z = input("quieres empezar un nuevo dia? (s/n) ")
if z == 's':
    nuevo()
while True:
    productos = {
        "1": {"nombre": "clasica", "precio": 70},
        "2": {"nombre": "terminator", "precio": 80},
        "3": {"nombre": "gordoburger", "precio": 90},
        "4": {"nombre": "calceburger", "precio": 100},
        "5": {"nombre": "falta_boca", "precio": 120},
        "6": {"nombre": "hawaiana", "precio": 100},
        "7": {"nombre": "la_choriada", "precio": 100},
        "8": {"nombre": "papas_fritas", "precio": 50},
        "9": {"nombre": "aros_cebolla", "precio": 50},
        "10": {"nombre": "refresco", "precio": 25},
        "11": {"nombre": "quesicarne", "precio": 80},
        "12": {"nombre": "burrito_ca", "precio": 35},
        "13": {"nombre": "burrito_bb", "precio": 40},
        "14": {"nombre": "tacos", "precio": 90},
        "15": {"nombre": "consome", "precio": 70},
        "16": {"nombre": "dogogolden", "precio": 50},
        "17": {"nombre": "dogochiquilin", "precio": 55}
    }
    pedido = 0
    while True:
        subprocess.run(["clear"])
        print("\nselecciona el producto:")
        for clave, info in productos.items():
            print(f"{clave} = {info['nombre']} |${info['precio']}|")
        print("0 = terminar")
        x = input()
        if x == '0':break
        if x in productos:
            producto = productos[x]
            print(producto["nombre"])
            cursor.execute("INSERT INTO golden (producto, precio) VALUES (?, ?)", (producto["nombre"], producto["precio"]))
            conn.commit()
            time.sleep(0.35)
            pedido += producto["precio"]
            subprocess.run(["clear"])
        else:
            print("ERROR opcion no disponible")
            time.sleep(0.5)
            subprocess.run(["clear"])
        
    cursor.execute("SELECT SUM(precio) FROM golden")
    total = cursor.fetchone()[0] or 0 
    print(f"el total es: ${pedido}")
    y = input("quieres ver el total de ventas del dia? (s/n) ")
    if y == 's': print(f"${total}")
    rp = input("quieres volver a usar el programa? (s/n) ")
    if rp == 'n': break
conn.close()
