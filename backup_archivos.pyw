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
            registrar_log(f"Archivo copiado: {ruta_origen} -> {ruta_destino}")
        else:
            print(f"Archivo no encontrado: {ruta_origen}")
            registrar_log(f"Archivo no encontrado: {ruta_origen}")

        
def copiar_carpeta_completa(origen, destino):
    try:
        nombre_carpeta = os.path.basename(origen.rstrip("\\/"))
        destino_final = os.path.join(destino, nombre_carpeta)

        # Crear carpeta si no existe
        if not os.path.exists(destino_final):
            os.makedirs(destino_final)

        # Copiar archivos y subdirectorios
        for dirpath, subdirs, files in os.walk(origen):
            # Ruta relativa desde la carpeta origen
            rel_path = os.path.relpath(dirpath, origen)
            destino_dir = os.path.join(destino_final, rel_path)

            if not os.path.exists(destino_dir):
                os.makedirs(destino_dir)

            for archivo in files:
                origen_arch = os.path.join(dirpath, archivo)
                destino_arch = os.path.join(destino_dir, archivo)
                shutil.copy2(origen_arch, destino_arch)

        print(f"Carpeta copiada (sobrescribiendo archivos si existían): {origen} -> {destino_final}")
        registrar_log(f"Carpeta copiada: {origen} -> {destino_final}")

    except Exception as e:
        print(f"Error al copiar carpeta: {e}")
        registrar_log(f"Error al copiar carpeta: {e}")




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
    archivos_sin_fecha = [
        "LISTADO DE COBRANZAS.xlsx",
        "TARJETAS_CORPORATIVAS.xlsx",
        "NUMEROS DE CHEQUES.xlsx"
    ]

    copiar_archivos_con_control(origen, destino, archivos_con_fecha, archivos_sin_fecha)

def backup_carpeta_sincronizados():
    origen = "C:/Users/jalvaredo/OneDrive - CV CONTROL SA/SINCRONIZADOS"
    destino = "//MATEO01/Users/JAlvaredo/Cvserver - Documentos Office"
    archivos_con_fecha = ["RECIBOS CALCULOS.xlsx"]
    archivos_sin_fecha = ["BANK deposito-CAJAS.xlsx",
                          "DNI.xls",
                          "GALICIA.doc",
                          "PAGOS AL EXTERIOR-2022.xlsx",
                          "PLANILLA-FACTURAS.xlsx",
                          "PLANILLA RENDICION VIATICOS.xlsx",
                          "selladOS.xlsx",
                          "VISA CORPORATE LIMITES.xlsx",
                          "CALCULOS.xls",
                          "CASA EL TUCUMANO.docx",
                          "DATOS BANCARIOS BANCO SABADELL.docx",
                          "hoja_membretada.docx",
                          "LIBRETIK.doc",
                          "NOTA CON CON LOGO.docx"
    ]
    copiar_archivos_con_control(origen, destino, archivos_con_fecha, archivos_sin_fecha)


def copiar_carpeta_dni():
    # Copia completa de la carpeta como respaldo adicional
    carpeta_origen = "C:/Users/jalvaredo/OneDrive - CV CONTROL SA/SINCRONIZADOS/DNI"
    carpeta_destino = "//Mateo01/Users/JAlvaredo/Cvserver - Documentos Office"
    copiar_carpeta_completa(carpeta_origen, carpeta_destino)
    
def copiar_carpeta_reclamos_prov_exterior():
    # Copia completa de la carpeta como respaldo adicional
    carpeta_origen = "C:/Users/jalvaredo/OneDrive - CV CONTROL SA/SINCRONIZADOS/STATEMENTS RECLAMOS PROV EXTERIOR"
    carpeta_destino = "//Mateo01/Users/JAlvaredo/Cvserver - Documentos Office"
    copiar_carpeta_completa(carpeta_origen, carpeta_destino)

def copiar_carpeta_firma_digital():
    # Copia completa de la carpeta como respaldo adicional
    carpeta_origen = "C:/Users/jalvaredo/OneDrive - CV CONTROL SA/SINCRONIZADOS/firma digital"
    carpeta_destino = "//Mateo01/Users/JAlvaredo/Cvserver - Documentos Office"
    copiar_carpeta_completa(carpeta_origen, carpeta_destino)


def registrar_log(mensaje):
    log_dir = "logs"
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    log_path = os.path.join(log_dir, "backup_log.txt")
    timestamp = datetime.now().strftime("[%d-%m-%Y %H:%M:%S]")
    with open(log_path, "a", encoding="utf-8") as f:
        f.write(f"{timestamp} {mensaje}\n")




def main():
    bakup_bancos()
    backup_carpeta_sincro()
    backup_carpeta_sincronizados()
    copiar_carpeta_dni()
    copiar_carpeta_reclamos_prov_exterior()
    copiar_carpeta_firma_digital()
    

if __name__ == '__main__':
    main()

