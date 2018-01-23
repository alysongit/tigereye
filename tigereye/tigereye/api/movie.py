from flask import request
from tigereye.extensions.validator import Validator

from tigereye.api import ApiView

from tigereye.models.movie import Movie


class MovieView(ApiView):

    def all(self):
        return  Movie.query.all()

    @Validator(mid=int)
    def get(self):
        # mid = request.args['mid']
        mid = request.params['mid']
        movie = Movie.get(mid)
        return movie





