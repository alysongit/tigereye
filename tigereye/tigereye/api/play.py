
from tigereye.extensions.validator import Validator
from flask import request
from tigereye.api import ApiView
from tigereye.models.play import Play
from tigereye.models.seat import PlaySeat


class PlayView(ApiView):
    def all(self):
        return Play.query.all()

    @Validator(pid=int)
    def seats(self):
        pid = request.params['pid']
        return  PlaySeat.query.filter(
            PlaySeat.pid == pid,
            PlaySeat.seat_type != 2

        ).all()
