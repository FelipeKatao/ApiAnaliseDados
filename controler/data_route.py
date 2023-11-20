from flask import render_template

class DataRoutes():
    def __init__(self) -> None:
        pass

    def ListarProdutos(self):
        return render_template('index.html')
    