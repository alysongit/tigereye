from flask_classy import FlaskView
from tigereye.app import ApiView

class MiscView(ApiView):


    def check(self):
        return "I'm ok"
    def error(self):
        1/0
