#Implemente un programa que solicite al usuario el nombre de un archivo y luego genere el tipo de
#archivo MIME correspondiente. Si el nombre del archivo termina en cualquiera de estos sufijos (sin
#importar el uso de mayúsculas y minúsculas) :
#- .gif
#- .jpg
#- .jpeg
#- .png
#- .pdf
#- .txt
#- .zip
#Si el nombre del archivo termina con algún otro sufijo que no se encuentra en la lista o no tiene
#ningún sufijo, en su lugar su programa deberá devolver application/octet-stream.

def obtener_tipo_mime(nombre_archivo):
    tipos_mime = {
        '.gif': 'image/gif',
        '.jpg': 'image/jpeg',
        '.jpeg': 'image/jpeg',
        '.png': 'image/png',
        '.pdf': 'application/pdf',
        '.txt': 'text/plain',
        '.zip': 'application/zip'
    }

    # Obtener la extensión del archivo
    extension = nombre_archivo.lower().split('.')[-1]

    # Obtener el tipo MIME correspondiente
    tipo_mime = tipos_mime.get('.' + extension, 'application/octet-stream')

    return tipo_mime

def main():
    nombre_archivo = input("Ingrese el nombre del archivo: ")
    tipo_mime = obtener_tipo_mime(nombre_archivo)
    print("El tipo MIME del archivo es:", tipo_mime)

if __name__ == "__main__":
    main()