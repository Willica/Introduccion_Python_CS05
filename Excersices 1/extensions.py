nombre_archivo = input("Nombre de archivo: ")
nombre_archivo = nombre_archivo.lower().strip()

if ".jpg" in nombre_archivo:
    print("image/jpg")
elif ".png" in nombre_archivo:
    print("image/png")
elif ".jpeg" in nombre_archivo:
    print("image/jpeg")
elif ".gif" in nombre_archivo:
    print("image/gif")
elif ".pdf" in nombre_archivo:
    print("application/pdf")
elif ".txt" in nombre_archivo:
    print("application/txt")
elif ".zip" in nombre_archivo:
    print("application/zip")
else:
    print("Application/octet-stream")
