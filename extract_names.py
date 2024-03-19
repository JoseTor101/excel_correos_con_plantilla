import pandas as pd

def info_colegios():
    # Cargar el archivo Excel en un DataFrame
    try:
        #sheet_name -> Nombre de hoja, generalmente "Hoja1"
        """df = pd.read_excel("excel/base_colegios.xls", sheet_name="base_colegios")
        print("DataFrame cargado exitosamente:")
        print(df)
        """
        df = pd.read_excel("excel/prueba.xls", sheet_name="Hoja1")
        print("DataFrame cargado exitosamente:")
    except Exception as e:
        print("Error cargando el DataFrame:", e)
        exit()
    # Obtener los nombres de las columnas
    column_names = df.columns.tolist()

    # Obtener las posiciones de los encabezados deseados
    posicion_encabezado1 = column_names.index("Colegio")
    posicion_encabezado2 = column_names.index("Correo")

    # Extraer y limpiar los datos de las columnas deseadas
    array_nombres_colegios = [nombre.strip() for nombre in df["Colegio"].tolist()]
    array_correos_colegios = [correo.strip() for correo in df["Correo"].tolist()]

    for i in range(len(array_correos_colegios)):
        print(f"{array_nombres_colegios[i]} -> {array_correos_colegios[i]}")
    
    return {"colegios": array_nombres_colegios, "correos": array_correos_colegios }
