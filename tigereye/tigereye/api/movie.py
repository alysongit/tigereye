from flask import request

from tigereye.api import ApiView

from tigereye.models.movie import Movie


class MovieView(ApiView):

    def all(self):
        return  Movie.query.all()

    def get(self):
        mid = request.args['mid']
        movie = Movie.get(mid)
        return movie





