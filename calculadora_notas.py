from flask import Flask, render_template, request

# Variables
letra_num = {"AD":4, "A":3, "B":2, "C":1}

# Crear app web
app = Flask (__name__)
# Definimos la ruta principal "/"
# GET → mostrar la página
# POST → recibir datos del formulario
@app.route("/", methods=["GET", "POST"])
def index():
    resultado = ""  # Variable para mostrar el promedio final
    if request.method == "POST":
        # Obtenemos la lista de notas enviadas desde el formulario
        # getlist() sirve para recoger varias notas con el mismo nombre "nota"
        notas = [letra_num[n.upper()] for n in request.form.getlist("nota") if n.strip() != ""]
        # ================ 
        # Calcular la nota
        # ================
        if notas:
            promedio = sum(notas)/len(notas)
            if promedio >= 3.5:
                resultado = "AD"
            if promedio >= 2.5 and promedio <= 3.49:
                resultado = "A"
            if promedio >= 1.5 and promedio <= 2.49:
                resultado = "B"
            if promedio <= 1.49:
                resultado = "C"
    # Renderizamos la página HTML y enviamos la variable resultado
    return render_template("index.html", resultado=resultado)

# Ejecutamos la app
if __name__ == "__main__":
    # host="0.0.0.0" → accesible desde el navegador de tu celular
    # port=5000 → puerto donde se ejecuta la app
    app.run(host="0.0.0.0", port=5000, debug=True)
                                     
    