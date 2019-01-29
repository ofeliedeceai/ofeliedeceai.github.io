import os
import cherrypy
from jinja2 import Environment, FileSystemLoader

CUR_DIR = os.path.dirname(os.path.abspath(__file__))
env = Environment(loader=FileSystemLoader(CUR_DIR), trim_blocks=True)


class HomePage(object):
    @cherrypy.expose
    def index(self):
        template = env.get_template('index.html')
        return template.render()

    @cherrypy.expose
    def treatments(self):
        template = env.get_template('treatments.html')
        return template.render()

    @cherrypy.expose
    def food(self):
        template = env.get_template('food.html')
        return template.render()

    @cherrypy.expose
    def documentation(self):
        template = env.get_template('documentation.html')
        return template.render()


if __name__ == '__main__':
    cherrypy.quickstart(HomePage())
