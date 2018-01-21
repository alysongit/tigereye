from flask_classy import FlaskView


class MiscView(FlaskView):


    def check(self):
        return "I'm ok"
