from flask import Flask, request, render_template, redirect, url_for

app=Flask(__name__)

usuarios=[]
id_contador=1

@app.route("/", methods=['GET','POST'])
def crud():
    print(usuarios)
    global id_contador
    if request.method=="POST":
        nombre=request.form["nombre"]
        correo=request.form["correo"]
        usuarios.append({"id": id_contador, "nombre": nombre, "correo": correo})
        id_contador+=1
        print(usuarios)
    eliminar_id=request.args.get("eliminar")
    if eliminar_id:
        for diccionario in usuarios:
            if str(diccionario["id"])==eliminar_id:
                usuarios.remove(diccionario)
                break
    return render_template("crud.html", usuarios=usuarios)
    

#Ruta para editar la informacion de un usuario
@app.route("/update/<int:id>", methods=['GET', 'POST']) 
def update(id):
    
    #TODO: capturar eñ usuario a editar
    for diccionario in usuarios: #Para cada diccionario dentro de lista evalue:    
        if diccionario["id"]==id: #Si el id convertido a string es igual al id que me pasan por parametro
            usuario_a_editar=diccionario #Hemos identificado los datos del usuario a editar
            break
    
    #TODO: actualizar la informacion del usuario seleccionado
    if request.method=="POST":
        usuario_a_editar["nombre"]=request.form.get("nombre") #el nombre nuevo sera el que llegue por un nuevo formulario
        usuario_a_editar["correo"]=request.form.get("correo") #el correo nuevo sera el que llegue por un nuevo formulario
        
        return redirect(url_for("crud")) #Redireccione la aplicacion a la ruta de la funcion crud
    
    return render_template('editar.html', usuario_a_editar=usuario_a_editar) 
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
if __name__=="__main__":
    app.run(debug=True)