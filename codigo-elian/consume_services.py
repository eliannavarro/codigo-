import requests

# URL base de tu servicio web
base_url = "https://tiempo-yvgt.onrender.com"

def obtener_mensaje_bienvenida():
    """Obtiene el mensaje de bienvenida desde el servicio web"""
    url = f"{base_url}/"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print("Mensaje de bienvenida:")
            print(response.json())
        else:
            print("Error al obtener el mensaje de bienvenida")
    except requests.exceptions.RequestException as e:
        print(f"Error en la solicitud: {e}")

def obtener_saludo(nombre):
    """Obtiene un saludo personalizado desde el servicio web"""
    url = f"{base_url}/saludo/{nombre}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"Saludo para {nombre}:")
            print(response.json())
        else:
            print(f"Error al obtener el saludo para {nombre}")
    except requests.exceptions.RequestException as e:
        print(f"Error en la solicitud: {e}")

def obtener_clima(ciudad):
    """Obtiene los datos del clima para una ciudad específica desde el servicio web"""
    url = f"{base_url}/clima/{ciudad}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"Datos del clima para {ciudad}:")
            print(response.json())
        else:
            print(f"Error al obtener los datos del clima para {ciudad}")
    except requests.exceptions.RequestException as e:
        print(f"Error en la solicitud: {e}")

if __name__ == "__main__":
    # Pruebas de los servicios
    obtener_mensaje_bienvenida()
    obtener_saludo("Juan")
    obtener_clima("London")
    obtener_clima("NonExistentCity")