'''
news.py: Modulo para definir las rutas relacionadas con la API News
'''
from flask import request
from endpoints.get_news.get_news import GetNews

def create_routes_news(app):
    '''
    Metodo que crea las rutas relacionadas con la API News
    '''

    # pylint: disable=unused-variable
    @app.route('/news')
    def get_news():
        get_news = GetNews()
        return get_news(request)
