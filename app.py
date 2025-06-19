from flask import Flask, render_template, request
from funciones.funcion_modelo_con_inputs import resultados_modelo
from funciones.funcion_modelo_con_inputs import resultados_modelo2
from funciones.funcion_modelo_con_inputs import resultados_modelo3
from funciones.funcion_modelo_con_inputs import resultados_modelo4
import csv
import os
from flask import redirect, flash, session
from datetime import datetime
import pandas as pd


import joblib


RUTA_CSV_USUARIOS = 'usuarios.csv'

app = Flask(__name__)
app.secret_key = 'clave-secreta-para-sesiones'  # Requerido si usas sesiones o flash


@app.route("/", methods=["GET", "POST"])
def index():

    return render_template("index.html")


@app.route("/modelo_tipos_disciplinas", methods=["GET", "POST"])
def info():
    data = {}

    if request.method == "POST":
        data["cliente"] = request.form.get("cliente", "")
        data["proveedores"] = request.form.get("proveedores", "")
        data["HH"] = request.form.get("HH", "")
        data["entregables"] = request.form.get("entregables", "")
        data["precio_propuesta"] = request.form.get("precio_propuesta", "")
        data["precio_keypro"] = request.form.get("precio_keypro", "")
        data["disciplinas"] = request.form.get("disciplinas", "").split(',')
        print("Datos recibidos:", data)
        modelo = joblib.load("modelo_hh_sintarifas.pkl")
        print(int(data["disciplinas"][0]))
        resultado = resultados_modelo3(modelo, int(data["precio_propuesta"]), int(data["precio_keypro"]), int(data["entregables"]), 1,int(data["HH"]),
                                       int(data["disciplinas"][0]), int(data["disciplinas"][1]), int(data["disciplinas"][2]), int(data["disciplinas"][3]),
                                         int(data["disciplinas"][4]),int(data["disciplinas"][5]), int(data["disciplinas"][6]), int(data["disciplinas"][7]),
                                           int(data["disciplinas"][8]), int(data["disciplinas"][9]), int(data["disciplinas"][10]), int(data["disciplinas"][11]),
                                             int(data["disciplinas"][12]))
        return render_template("resultado.html", resultado=resultado)
       

    return render_template("modelo_tipos_disciplinas.html")

@app.route("/modelo_con_todo", methods=["GET", "POST"])
def ayuda():

    #if request.method == "GET":
    tipo_usuario = session.get("usuario", "invitado")  # por defecto
    return render_template("modelo_con_todo.html", tipo_usuario=tipo_usuario)
    
    data = {}
    if request.method == "POST":
        data["cliente"] = request.form.get("cliente", "")
        data["proveedores"] = request.form.get("proveedores", "")
        data["HH"] = request.form.get("HH", "")
        data["entregables"] = request.form.get("entregables", "")
        data["precio_propuesta"] = request.form.get("precio_propuesta", "")
        data["precio_keypro"] = request.form.get("precio_keypro", "")
        data["disciplinas"] = request.form.get("disciplinas", "").split(',')

        data["tarifa_jefeproyecto"] = request.form.get("tarifa_jefeproyecto", "")
        data["tarifa_consultor"] = request.form.get("tarifa_consultor", "")
        data["tarifa_ingsenior"] = request.form.get("tarifa_ingsenior", "")
        data["tarifa_jefedisciplina"] = request.form.get("tarifa_jefedisciplina", "")
        data["tarifa_ingenieroA"] = request.form.get("tarifa_ingenieroA", "")
        data["tarifa_ingenieroB"] = request.form.get("tarifa_ingenieroB", "")
        data["tarifa_proyectista"] = request.form.get("tarifa_proyectista", "")
        data["tarifa_dibujante"] = request.form.get("tarifa_dibujante", "")
        data["tarifa_controldocumentos"] = request.form.get("tarifa_controldocumentos", "")
        data["tarifa_controlproyectos"] = request.form.get("tarifa_controlproyectos", "")
        data["tarifa_calidad"] = request.form.get("tarifa_calidad", "")

    
        data["hh_jefeproyecto"] = request.form.get("hh_jefeproyecto", "")
        data["hh_ingenierosenior"] = request.form.get("hh_ingenierosenior", "")
        data["hh_liderdisciplina"] = request.form.get("hh_liderdisciplina", "")
        data["hh_ingenieroA"] = request.form.get("hh_ingenieroA", "")
        data["hh_proyectistaA"] = request.form.get("hh_proyectistaA", "")
        data["hh_controldocumentos"] = request.form.get("hh_controldocumentos", "")
        data["hh_controlproyecto"] = request.form.get("hh_controlproyecto", "")
    

        data["disciplinas"] = [
                request.form.get("hh_mecanica", ""),
                request.form.get("hh_piping", ""),
                request.form.get("hh_electricidad", ""),
                request.form.get("hh_estructural", ""),
                request.form.get("hh_estudiosygeneral", ""),
                request.form.get("hh_instrumentacion", ""),
                request.form.get("hh_hormigones", ""),
                request.form.get("hh_general", ""),
                request.form.get("hh_hidraulica", ""),
                request.form.get("hh_estudiosdisciplinarios", ""),

                request.form.get("hh_civil", ""),
                request.form.get("hh_ips", ""),
                request.form.get("hh_terreno", "")
                
                ]
        
        modelo = joblib.load("modelo_tarifa_hh_disciplinas.pkl")
        """modelo, precio_total_propuesta, precio_keypro, entr, cliente, hh, mecanica,piping, electricidad, estrutural,
                        estudiosygeneral, instrumentacion, hormigones, general, hidraulica, estudiosdisciplinarios, civil, ips, terreno,
                            tfa_jefeproyecto, tfa_consultor, tfa_ingsenior, tfa_jefedisciplina, tfa_ingA, tfa_ingB, tfa_proyectista,
                            tfa_dibujante, tfa_controldctos, tfa_controlproyectos, tfa_calidad, hh_jefeproyecto, hh_ingsenior,
                            hh_liderdisciplina, hh_ingA, hh_proyectistaA, hh_controldoc, hh_controlproyecto"""
        print("MECANICA")
        print(data)
        


        resultado = resultados_modelo4(modelo, int(data["precio_propuesta"]), int(data["precio_keypro"]), int(data["entregables"]), 1,int(data["HH"]),
                                        int(data["disciplinas"][0]), int(data["disciplinas"][1]), int(data["disciplinas"][2]), int(data["disciplinas"][3]),
                                            int(data["disciplinas"][4]),int(data["disciplinas"][5]), int(data["disciplinas"][6]), int(data["disciplinas"][9]),
                                            int(data["disciplinas"][8]), int(data["disciplinas"][9]), int(data["disciplinas"][10]), int(data["disciplinas"][11]),
                                                int(data["disciplinas"][12]), int(data["tarifa_jefeproyecto"]), int(data["tarifa_consultor"]),
                                                int(data["tarifa_ingsenior"]), int(data["tarifa_jefedisciplina"]), int(data["tarifa_ingenieroA"]),
                                                int(data["tarifa_ingenieroB"]), int(data["tarifa_proyectista"]), int(data["tarifa_dibujante"]), int(data["tarifa_controldocumentos"]),
                                                int(data["tarifa_controlproyectos"]), int(data["tarifa_calidad"]), int(data["hh_jefeproyecto"]),int(data["hh_ingenierosenior"]), 
                                                int(data["hh_liderdisciplina"]), int(data["hh_ingenieroA"]),int(data["hh_proyectistaA"]), int(data["hh_controldocumentos"]),
                                                int(data["hh_controlproyecto"]) )
        #ojo aca que no arregle bien el tema de general y estudios disiplinarios, creo que tendre que entrenar el modelo de nuevo
        if session.get("usuario") != "invitado":
            campos_a_guardar = {
        "usuario": session["usuario"],
        "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),

        "cliente": request.form.get("cliente", ""),
        "proveedores": request.form.get("proveedores", ""),
        "HH": request.form.get("HH", ""),
        "entregables": request.form.get("entregables", ""),
        "precio_propuesta": request.form.get("precio_propuesta", ""),
        "precio_keypro": request.form.get("precio_keypro", ""),
        "tarifa_jefeproyecto": request.form.get("tarifa_jefeproyecto", ""),
        "tarifa_consultor": request.form.get("tarifa_consultor", ""),
        "tarifa_ingsenior": request.form.get("tarifa_ingsenior", ""),
        "tarifa_jefedisciplina": request.form.get("tarifa_jefedisciplina", ""),
        "tarifa_ingenieroA": request.form.get("tarifa_ingenieroA", ""),
        "tarifa_ingenieroB": request.form.get("tarifa_ingenieroB", ""),
        "tarifa_proyectista": request.form.get("tarifa_proyectista", ""),
        "tarifa_dibujante": request.form.get("tarifa_dibujante", ""),
        "tarifa_controldocumentos": request.form.get("tarifa_controldocumentos", ""),
        "tarifa_controlproyectos": request.form.get("tarifa_controlproyectos", ""),
        "tarifa_calidad": request.form.get("tarifa_calidad", ""),
        "hh_jefeproyecto": request.form.get("hh_jefeproyecto", ""),
        "hh_ingenierosenior": request.form.get("hh_ingenierosenior", ""),
        "hh_liderdisciplina": request.form.get("hh_liderdisciplina", ""),
        "hh_ingenieroA": request.form.get("hh_ingenieroA", ""),
        "hh_proyectistaA": request.form.get("hh_proyectistaA", ""),
        "hh_controldocumentos": request.form.get("hh_controldocumentos", ""),
        "hh_controlproyecto": request.form.get("hh_controlproyecto", ""),
        "hh_mecanica": request.form.get("hh_mecanica", ""),
        "hh_piping": request.form.get("hh_piping", ""),
        "hh_electricidad": request.form.get("hh_electricidad", ""),
        "hh_estructural": request.form.get("hh_estructural", ""),
        "hh_estudiosygeneral": request.form.get("hh_estudiosygeneral", ""),
        "hh_instrumentacion": request.form.get("hh_instrumentacion", ""),
        "hh_hormigones": request.form.get("hh_hormigones", ""),
        "hh_general": request.form.get("hh_general", ""),
        "hh_hidraulica": request.form.get("hh_hidraulica", ""),
        "hh_estudiosdisciplinarios": request.form.get("hh_estudiosdisciplinarios", ""),
        "hh_civil": request.form.get("hh_civil", ""),
        "hh_ips": request.form.get("hh_ips", ""),
        "hh_terreno": request.form.get("hh_terreno", "")
        
    }

        with open("historial_usuarios.csv", mode="a", newline='') as archivo:
            escritor = csv.DictWriter(archivo, fieldnames=campos_a_guardar.keys())
            if archivo.tell() == 0:
                escritor.writeheader()
            escritor.writerow(campos_a_guardar)
        return render_template("resultado.html", resultado=resultado)
     #"UF/HH", "UF/Entr.","UF", "Entr.", "Contrato Marco_x","Cliente_x","Total\n$;UF/USD", "HH","$;UF;USD", "UF3", "TIPO DE INGENIERÍA",
         #         "tarifa jefe proyecto CLP","tarifa consultor CLP","tarifa ingeniero senior CLP",	"tarifa jefe disciplina CLP",	
          #        "tarifa ingeniero A CLP",	"tarifa ingeniero B CLP","tarifa proyectista CLP","tarifa dibujante CLP","tarifa control documentos CLP",
           #             	"tarifa control de proyectos CLP",	"tarifa calidad CLP", "HH totales jefe proyecto",	"HH totales ingeniero senior",	"HH totales lider de disciplina", 	
            #                "HH totales ingeniero A", "HH totales proyectista A", "HH totales control documentos", "HH totales control proyecto",
             #               "Total HH mecanica", "Total HH piping", "Total HH electricidad","Total HH estructural", "Total HH estudios y general",	
              #               "Total HH instrumentacion", "Total HH hormigones",	"Total HH general",	"Total HH hidraulica",	"Total HH estudios disciplinarios",
               #                  	"Total HH civil",	"Total HH IPS",	"Total HH terreno"

    return render_template("modelo_con_todo.html")


@app.route("/autenticacion", methods=["POST"])
def autenticacion():
    accion = request.form.get("action")

    if accion == "guest":
        session["usuario"] = "invitado"
        flash("Has ingresado como invitado.", "info")
        return redirect("/modelo_con_todo") 

    username = request.form.get("username")
    password = request.form.get("password")

    if not username or not password:
        flash("Faltan campos obligatorios.", "error")
        return redirect("/")

    if not os.path.exists(RUTA_CSV_USUARIOS):
        flash("No hay usuarios registrados.", "error")
        return redirect("/")

    with open(RUTA_CSV_USUARIOS, newline='') as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            if fila["username"] == username and fila["password"] == password:
                session["usuario"] = username  # podrías guardar también más info
                flash(f"Bienvenido, {username}", "success")
                return redirect("/modelo_con_todo")  

    flash("Usuario o contraseña incorrectos.", "error")
    return redirect("/")


@app.route("/crear_cuenta", methods=["POST"])
def crear_cuenta():
    nuevo_usuario = request.form.get("new_username")
    nueva_contra = request.form.get("new_password")

    if not nuevo_usuario or not nueva_contra:
        flash("Debes completar todos los campos.", "error")
        return redirect("/")

    # Si el archivo no existe, crearlo con cabecera
    existe = os.path.exists(RUTA_CSV_USUARIOS)
    with open(RUTA_CSV_USUARIOS, mode='a', newline='') as archivo:
        campos = ["username", "password"]
        escritor = csv.DictWriter(archivo, fieldnames=campos)
        if not existe:
            escritor.writeheader()
        escritor.writerow({"username": nuevo_usuario, "password": nueva_contra})

    
    session["usuario"] = nuevo_usuario
    flash("Cuenta creada exitosamente. Ahora puedes iniciar sesión.", "success")
    return redirect("/modelo_con_todo")
    
@app.route("/historial")
def historial():
    usuario = session.get("usuario", "invitado")
    if usuario == "invitado":
        flash("Los invitados no tienen historial.", "error")
        return redirect("/modelo_con_todo")

    try:
        df = pd.read_csv("historial_usuarios.csv")
    except FileNotFoundError:
        df = pd.DataFrame()

    df_usuario = df[df["usuario"] == usuario]

    if df_usuario.empty:
        return render_template("historial.html", registros=[], resumen={})

    # Orden por fecha descendente
    df_usuario = df_usuario.sort_values("fecha", ascending=False)

    # Cálculo de resumen (ejemplo con columnas numéricas)
    columnas_numericas = [
        "precio_propuesta", "precio_keypro", "HH", "entregables",
        "hh_jefeproyecto", "hh_ingenierosenior", "hh_liderdisciplina",
        "hh_ingenieroA", "hh_proyectistaA", "hh_controldocumentos", "hh_controlproyecto"
    ]

    resumen = {}
    for col in columnas_numericas:
        if col in df_usuario.columns:
            try:
                df_usuario[col] = pd.to_numeric(df_usuario[col], errors="coerce")
                resumen[col] = {
                    "promedio": round(df_usuario[col].mean(skipna=True), 2),
                    "total": df_usuario[col].sum(skipna=True)
                }
            except Exception:
                pass

    return render_template("historial.html", registros=df_usuario.to_dict(orient="records"), resumen=resumen)

if __name__ == "__main__":
    app.run(debug=True)
