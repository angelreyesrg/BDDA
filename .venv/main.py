from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text

# Crear la aplicación Flask
app = Flask(__name__)

# Configuración de la base de datos
DATABASE_URL = "postgresql://postgres:1234@localhost:5432/web"
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL

# Inicializar la base de datos
db = SQLAlchemy(app)

# Rutas
@app.route("/")
def index(name=None):
    return render_template('index.html')

@app.route("/crear", methods=["GET", "POST"])
def crear(name=None):
    if request.method == "POST":
        nombre_usuario = request.form['nombre_usuario']
        correo_electronico = request.form['correo_electronico']
        contrasena = request.form['contrasena']

        # Consulta SQL para insertar el nuevo usuario
        sql = text("""
            INSERT INTO usuarios (nombre_usuario, correo_electronico, contrasena, fecha_creacion)
            VALUES (:nombre_usuario, :correo_electronico, :contrasena, NOW())
        """)

        try:
            # Ejecutar la consulta
            db.session.execute(sql, {
                'nombre_usuario': nombre_usuario,
                'correo_electronico': correo_electronico,
                'contrasena': contrasena
            })
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            flash(f'Error al crear el usuario: {str(e)}', 'danger')

    return render_template('crear.html')

@app.route("/consultar")
def consultar(name=None):
    return render_template('consultar.html')

@app.route("/actualizar")
def actualizar(name=None):
    return render_template('actualizar.html')

@app.route("/borrar")
def borrar(name=None):
    return render_template('borrar.html')

# Inicializar el servidor
if __name__ == "__main__":
    app.run(debug=True)
