from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash


# Crear la aplicación Flask
app = Flask(__name__)

# Configuración de la base de datos
DATABASE_URL = "postgresql://postgres:1234@localhost:5432/postgres"
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL

# Establecer la clave secreta para la sesión
app.secret_key = "\x83\xeb\x05jp\xd3\x16\xed\xac\x86\xa8\xf2%\x9b\x91_9*\xd0\xbbo\x05\xcch"

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

        # Encriptar la contraseña utilizando bcrypt
        contrasena_encriptada = generate_password_hash(contrasena)

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
                'contrasena': contrasena_encriptada
            })
            db.session.commit()
            flash('Usuario creado exitosamente', 'success')
            return render_template('index.html')
        except Exception as e:
            db.session.rollback()
            flash(f'Error al crear el usuario: {str(e)}', 'danger')
            print(f"Error al crear el usuario: {str(e)}")  # Imprimir el error en la consola
            return render_template('index.html')
    else:
        return render_template('crear.html')


@app.route("/iniciar", methods=["GET", "POST"])
def iniciar(name=None):
    if request.method == "POST":
        nombre_usuario = request.form['nombre_usuario']
        contrasena = request.form['contrasena']

        # Consulta SQL para buscar el usuario por nombre de usuario
        sql = text("""
            SELECT id, contrasena FROM usuarios WHERE nombre_usuario = :nombre_usuario
        """)

        try:
            # Ejecutar la consulta
            result = db.session.execute(sql, {'nombre_usuario': nombre_usuario, 'contrasena':contrasena}).fetchone()
            if result:
                # Comparar la contraseña encriptada almacenada con la contraseña ingresada
                user_id, contrasena_encriptada = result
                if check_password_hash(contrasena_encriptada, contrasena):
                    flash('Inicio de sesión exitoso.', 'success')
                    session['user_id'] = user_id  # Guardar el ID del usuario en la sesión
                    return render_template('index.html')  # Redirigir a la página principal
                else:
                    flash('Contraseña incorrecta.', 'danger')
                    return render_template('index.html')
            else:
                flash('Usuario no encontrado.', 'danger')
                return render_template('index.html')

        except Exception as e:
            flash(f'Error al iniciar sesión: {str(e)}', 'danger')
            return render_template('index.html')
    else:
        return render_template('iniciar.html')

@app.route("/cerrar")
def logout():
    try:
        if session['user_id']:
            session.pop('user_id', None)  # Eliminar el ID de usuario de la sesión
            flash('Has cerrado sesión', 'info')
            return render_template('index.html')
        else:
            flash('No hay sesión iniciada', 'info')
            return render_template('index.html')
    except Exception as e:
        flash(f'No hay sesion iniciada.', 'info')
        return render_template('index.html')

# Inicializar el servidor
if __name__ == "__main__":
    app.run(debug=True)
