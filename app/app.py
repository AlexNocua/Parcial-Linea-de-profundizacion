from flask import Flask, render_template, request, redirect, url_for
from conection import *
from operario import Operario
from producto import Producto


db = Conexion()
app = Flask(__name__)
operaio1 = None
producto1 = None
error = ''

# registrar Operarios los operarios registrados
# esta funcionando


@app.route('/guardar_operario', methods=['POST'])
def guardarOperario():
    operario = db['operarios']
    nombre = request.form['r_n_operaerio']
    correo = request.form['r_c_operaerio']
    contraseña = request.form['r_p_operaerio']
    if nombre and correo and contraseña:
        operario1 = Operario(nombre, correo, contraseña)
        operario.insert_one(operario1.formato_doc())
        return redirect(url_for('login'))

    else:
        return "Error"


# iniciar secion
# funcionando
@app.route('/iniciarSesion', methods=['POST'])
def iniciarSesion():
    operarios = db['operarios']
    correo = request.form['e_operario']
    contraseña = request.form['p_operario']
    operario = operarios.find_one({
        'correo': correo,
                                  'password': contraseña})
    # print(correo, contraseña, '#####################')
    if operario:
        return redirect(url_for('form'))
    else:

        return redirect(url_for('login'))


# guardar los productos
@app.route('/guardar_producto', methods=['POST'])
def agregarProducto():
    productos = db['productos']
    n_producto = request.form['n_producto']
    v_producto = request.form['v_producto']
    c_producto = request.form['c_producto']

    if n_producto and v_producto and c_producto:
        producto1 = Producto(n_producto, v_producto, c_producto)
        productos.insert_one(producto1.formato_doc())
        return redirect(url_for('form'))

    else:
        return "Error"


# rutas de redireccion dios mio
@app.route('/')
def login():

    return render_template('login.html')


# eliminar el producto
# eliminar_producto/{{nombre_producto }}
@app.route('/eliminar_producto/<string:nombre_producto>')
def eliminar(nombre_producto):
    productos = db['productos']

    result = productos.delete_one({'nombre_producto': nombre_producto})
    if result.deleted_count == 1:
        return redirect(url_for('form'))
    else:
        return redirect(url_for('form'))


# editarProducto
@app.route('/editar_producto', methods=['POST'])
def editar():
    productos = db['productos']
    nombre_producto = request.form['nombre_producto']
    nuevo_nombre = request.form['nuevo_nombre']
    nuevo_valor = request.form['nuevo_valor']
    nueva_cantidad = request.form['nueva_cantidad']
    if nombre_producto and nuevo_nombre and nuevo_valor and nueva_cantidad:
        resultado = productos.update_one({'nombre_producto': nombre_producto}, {"$set": {'nombre_producto': nuevo_nombre,
                                                                                         'valor_producto': nuevo_valor,
                                                                                         'cantidad_producto': nueva_cantidad}})
        if resultado.modified_count > 0:
            return redirect(url_for('form'))


@app.route('/form')
def form():
    productos = db['productos'].find()
    # rednerizado con jinja2
    return render_template('form_register.html', productos=productos)


@app.route('/base')
def base():

    return render_template('base.html')


if __name__ == '__main__':
    app.run(debug=True, port=5555)
