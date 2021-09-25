from logging import debug
from os import fsencode
from flask import Flask,request,jsonify
from flask_mysqldb import MySQL
from flask_cors import CORS


app=Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'login'


mysql=MySQL(app)

CORS(app)

@app.route('/users',methods=["POST"])
def createUser():
    print(request.json)
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO usuarios(name,email, password) VALUES (%s, %s,%s)", (request.json["name"],request.json["email"],request.json["password"]))
    mysql.connection.commit()
    cur.close()
    print("usuario creado satisfactorio")
    return jsonify(request.json)
    

@app.route('/users',methods=["GET"])
def getUsers():

    usuarios=[]
    cur=mysql.connection.cursor()
    
    cur.execute("SELECT * FROM usuarios")
    data = cur.fetchall()
   
    for dat in data:
        usuarios.append(
        {
        "id":str(dat[0]),
        "name":dat[1],
        "email":dat[2],
        "password":dat[3]
        })
       
    return (jsonify(usuarios))

@app.route('/user/<id>',methods=["GET"])
def getUser(id):
     
    cur=mysql.connection.cursor()
    
    cur.execute("SELECT * FROM usuarios where id=%s",id)

    data = cur.fetchall()
    cur.close()
   
    return jsonify(data)

@app.route('/users/<id>',methods=["DELETE"])
def deleteUser(id):

    cur=mysql.connection.cursor()
    
    cur.execute("DELETE FROM usuarios where id=%s",id)

    mysql.connection.commit()
    cur.close()

    return jsonify("eliminado")


@app.route('/users/<id>',methods=["PUT"])
def updateUser(id):

    cur=mysql.connection.cursor()
    cur.execute("UPDATE usuarios set name=%s,password=%s where id=%s",(request.json["name"],request.json["password"],id))
    
    mysql.connection.commit()
    cur.close()
    
    return jsonify("dato actualizado")


@app.route("/login" , methods=["POST"])
def login():
    #se recibe archivo en formato json por peticion POST
    json = request.json
    #se guarda en variables el valor de cada clave
    email = json["email"]
    password = json["password"]
  
    # Empieza la conexion a base de datos
    cursor = mysql.connection.cursor()
    cursor.execute(
        'SELECT * FROM usuarios WHERE email=%s and password=%s', (email,password))
    datosUser = cursor.fetchall()
    cursor.close()
    # Se valida contraseña
    if (len(datosUser) > 0):
            msj = "Login Exitoso!"
            print(msj)
            resp = jsonify("Login Exitoso!")
            return resp
    else:
            resp = jsonify("Email o contraseña Invalido")
            return resp
   



if __name__=='__main__':
    app.run(debug=True)