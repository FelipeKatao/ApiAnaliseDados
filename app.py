from flask import Flask
from view.data_views import DataRoutes

app = Flask(__name__)
DataRoute_= DataRoutes()

app.add_url_rule("/","ListarProdutos",DataRoute_.ListarProdutos)

if(__name__ == '__main__'):
    app.run(debug=True)