import os
import shutil

def recuperador_atomico_original():
    # 1. Configuración de las rutas directas
    ruta_origen = os.path.expanduser("~")  # Carpeta de usuario (C:\Users\TuUsuario)
    ruta_destino = "C:\\Recuperado_Atomico"
    
    # 2. Extensiones que vamos a rescatar
    extensiones_objetivo = ('.doc', '.docx', '.xls', '.xlsx', '.ppt', '.pptx', '.pdf')
    
    print("[*] INICIANDO ESCANEO ATÓMICO...")
    print(f"[*] Buscando en: {ruta_origen}")
    print(f"[*] Guardando en: {ruta_destino}\n")
    
    # Crear la carpeta de destino si no existe
    if not os.path.exists(ruta_destino):
        os.makedirs(ruta_destino)
        
    contador = 0
    
    # 3. El motor de búsqueda original (Simple y veloz)
    for raiz, directorios, archivos in os.walk(ruta_origen):
        # Filtros de seguridad para no entrar en bucles infinitos
        if "Recuperado_Atomico" in raiz or "AppData" in raiz:
            continue
            
        for archivo in archivos:
            # Comprobar si el archivo tiene la extensión que buscamos
            if archivo.lower().endswith(extensiones_objetivo):
                ruta_completa_archivo = os.path.join(raiz, archivo)
                
                try:
                    # Copia directa manteniendo metadatos nativos
                    shutil.copy2(ruta_completa_archivo, ruta_destino)
                    contador += 1
                    # Un print simple en la consola para saber que está vivo
                    print(f"[RESCATADO] -> {archivo}")
                    
                except Exception:
                    # Si el archivo está bloqueado por el sistema, lo salta sin frenar
                    continue
                    
    print("\n[🏆] OPERACIÓN TERMINADA CON ÉXITO")
    print(f"[🏆] Se han respaldado {contador} archivos en el búnker.")

if __name__ == "__main__":
    recuperador_atomico_original()