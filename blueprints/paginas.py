from flask import Flask,Blueprint,render_template

Paginas_site =  Blueprint("Paginas_site",__name__)

@Paginas_site.route("/graficos")
def Acessargraficos():
    return render_template("graficos.html")
