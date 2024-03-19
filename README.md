# README

## Descripción del Proyecto:

Este proyecto está diseñado para leer información desde un archivo de Excel en formato `.xls`, extraer datos de columnas específicas, almacenar esa información en un array y luego enviar correos electrónicos personalizados utilizando los datos extraídos.

### Archivos Incluidos:
- `main.py`: Contiene el script principal para enviar correos electrónicos personalizados.
- `extract_names.py`: Incluye la función para extraer información del archivo de Excel.
- `prueba.xls`: Archivo de Excel que contiene datos sobre clientes y sus direcciones de correo electrónico correspondientes.
- `dotenv`: Archivo de variables de entorno para almacenar información sensible como contraseñas de forma segura.

### Dependencias:
- `pandas`: Una potente biblioteca de manipulación de datos en Python utilizada para leer archivos de Excel.
- `dotenv`: Utilizado para cargar variables de entorno desde un archivo `.env`.
- `smtplib`: Biblioteca para enviar correos electrónicos desde un script de Python.
- `ssl`: Proporciona soporte SSL para comunicación de correo electrónico segura.

### Instalación:

Antes de ejecutar el script, asegúrate de instalar las dependencias requeridas usando pip:

```bash
pip install pandas python-dotenv
```

### Uso:

1. Asegúrate de que el archivo de Excel (`prueba.xls`) se encuentre en el directorio `excel`.
2. Configura un archivo `.env` en el directorio raíz con la siguiente estructura:

```
PASSWORD=API_KEY_de_tu_correo_electrónico
```

Reemplaza `API_KEY_de_tu_correo_electrónico` por la API key de aplicación dada por tu proveedor de Email (En este caso Google -> https://support.google.com/accounts/answer/185833?hl=es)

3. Ejecuta el script `main.py` para enviar correos electrónicos personalizados a los clientes listadas en el archivo de Excel.


```bash
python main.py
```

4. Sé paciente, puede tomar un tiempo.

### Notas Importantes:

- El script asume que el archivo de Excel tiene dos columnas: "Colegio" y "Correo".
- Si la dirección de correo electrónico para una correo es "-", el script omitirá el envío de un correo electrónico a esa dirección. Ello significa que no había información de correo en base de datos.
- Asegúrate de que la cuenta de correo electrónico del remitente permita el acceso a aplicaciones menos seguras o utilice la autenticación de dos factores con una contraseña de aplicación.
- Este script está específicamente diseñado para funcionar con archivos de Excel en formato `.xls`. Si tienes archivos de Excel en otros formatos, pueden ser necesarias modificaciones adicionales.
