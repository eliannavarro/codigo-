from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/crear_usuario", methods=["POST"])
def crear_usuario():
    # Obtener los datos en formato JSON de la solicitud
    datos = request.get_json()
    nombre = datos.get("nombre")
    edad = datos.get("edad")

    # Crear una respuesta
    respuesta = {
        "mensaje": f"Usuario {nombre} de {edad} años creado exitosamente."
    }
    return jsonify(respuesta)

if __name__ == "__main__":
    app.run()