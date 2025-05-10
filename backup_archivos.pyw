import os
import shutil
from datetime import datetime

def copiar_archivos_con_control(origen, destino, con_fecha, sin_fecha):
    if not os.path.exists(destino):
        os.makedirs(destino)

    # Unir ambas listas para evitar repetir código
    todos_los_archivos = con_fecha + sin_fecha

    for archivo in todos_los_archivos:
        ruta_origen = os.path.join(origen, archivo)

        if os.path.isfile(ruta_origen):
            #separa nombre y extension
            nombre, extension = os.path.splitext(archivo)
            ruta_destino = os.path.join(destino, archivo)

            # Si el archivo está en la lista con fecha y ya existe, agregar timestamp
            if archivo in con_fecha and os.path.exists(ruta_destino):
                #timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                timestamp = datetime.now().strftime("%d-%m-%y_%H.%M.%S")
                
                nuevo_nombre = f"{nombre}_{timestamp}{extension}"
                ruta_destino = os.path.join(destino, nuevo_nombre)

            # Copiar el archivo
            shutil.copy2(ruta_origen, ruta_destino)
            print(f"Copiado: {ruta_origen} -> {ruta_destino}")
        else:
            print(f"Archivo no encontrado: {ruta_origen}")

def bakup_bancos():
    origen = "C:/Users/jalvaredo/OneDrive - CV CONTROL SA/SINCRO/BANCOS"
    destino = "//MATEO01/Users/JAlvaredo/Cvserver - Documentos Office"
    archivos_con_fecha = ["BANCOS actualizado.xlsm"]
    archivos_sin_fecha = []
    copiar_archivos_con_control(origen, destino, archivos_con_fecha, archivos_sin_fecha)


def backup_carpeta_sincro():
    origen = "C:/Users/jalvaredo/OneDrive - CV CONTROL SA/SINCRO"
    destino = "//MATEO01/Users/JAlvaredo/Cvserver - Documentos Office"
    archivos_con_fecha = ["COBRANZAS CLAVES.xlsx"]
    archivos_sin_fecha = ["LISTADO DE COBRANZAS.xlsx", "TARJETAS_CORPORATIVAS.xlsx" ]
    copiar_archivos_con_control(origen, destino, archivos_con_fecha, archivos_sin_fecha)

def backup_carpeta_sincronizados():
    origen = "C:/Users/jalvaredo/OneDrive - CV CONTROL SA/SINCRONIZADOS"
    destino = "//MATEO01/Users/JAlvaredo/Cvserver - Documentos Office"
    archivos_con_fecha = ["RECIBOS CALCULOS.xlsx"]
    archivos_sin_fecha = ["BANK deposito-CAJAS.xlsx"]
    copiar_archivos_con_control(origen, destino, archivos_con_fecha, archivos_sin_fecha)


def main():
    bakup_bancos()
    backup_carpeta_sincro()
    backup_carpeta_sincronizados()
    

if __name__ == '__main__':
    main()

