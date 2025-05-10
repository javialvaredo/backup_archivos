# Backup de Archivos con Control de Fecha y Hora

Este script en Python permite realizar copias de seguridad de archivos desde tres carpetas distintas hacia una carpeta destino compartida en red. A algunos archivos se les agrega la fecha y la hora al nombre para evitar sobrescribir versiones anteriores.

## 📂 Estructura del Script

El script realiza copias desde las siguientes carpetas de origen:

- `SINCRO/BANCOS`
- `SINCRO`
- `SINCRONIZADOS`

Hacia esta carpeta de destino:

- `//MATEO01/Users/JAlvaredo/Cvserver - Documentos Office`

### 📁 Tipos de archivos

- **Archivos con control de fecha**: si ya existen en destino, se copia una nueva versión agregando la fecha y hora al nombre.
- **Archivos sin control de fecha**: se sobrescriben directamente si ya existen en destino.

## 🧠 Funciones principales

- `copiar_archivos_con_control(origen, destino, con_fecha, sin_fecha)`:  
  Función base que copia archivos desde una carpeta origen hacia destino, aplicando control de nombre con timestamp si es necesario.

- `bakup_bancos()`:  
  Copia desde la carpeta `SINCRO/BANCOS`.

- `backup_carpeta_sincro()`:  
  Copia desde la carpeta `SINCRO`.

- `backup_carpeta_sincronizados()`:  
  Copia desde la carpeta `SINCRONIZADOS`.

## 🕒 Formato del timestamp

Los archivos con control de fecha llevan este formato agregado al nombre:

