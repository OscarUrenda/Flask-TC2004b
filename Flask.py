from flask import Flask, redirect, url_for, render_template, request
import pickle
app = Flask(__name__)

regr = open("modeloSVR_pickle", "rb")
mm = pickle.load(regr)
regr.close()

def prediccion(calidad,dureza,produccion):
    res = mm.predict([[calidad,dureza,produccion]])
    return res.round(5)


@app.route("/Home", methods=['POST','GET'])
def home():
    if request.method == "POST":
        calidad = float(request.form["calidad"])
        dureza = float(request.form["dureza"])
        produccion = float(request.form["produccion"])
        
        predecir = prediccion(calidad,dureza,produccion)
        return render_template("index.html", costo = predecir[0][0], ee=predecir[0][1],
                               ec= predecir[0][2], calidad=calidad, dureza=dureza, produccion=produccion)
    else:
        return render_template("index.html")

@app.route("/Exploración")
def Exploración():
    return render_template("Exploración.html")

@app.route("/Preprocesamiento")
def Preprocesamiento():
    return render_template("Preprocesamiento.html")

@app.route("/Modelación")
def Modelación():
    return render_template("Modelación.html")

@app.route("/Evaluación")
def Evaluación():
    return render_template("Evaluación.html")

if __name__ == "__main__":
    app.run()   