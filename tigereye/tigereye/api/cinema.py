from flask_classy import FlaskView
from tigereye.models.cinema import Cinema
from  flask import jsonify

class CinemaView(FlaskView):
    def all(self):
        cinemas=Cinema.query.all()
        cinema_list=[]
        for cinema in cinemas:
            cinema_list.append({
                "cid":cinema.cid,
                "name":cinema.name,
                'address':cinema.address,
                'halls':cinema.halls,
                "handle_free":cinema.handle_free,
                'buy_limit':cinema.buy_limit,
                'status':cinema.status,

            })
        return  jsonify(cinema_list)