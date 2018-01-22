from flask_classy import FlaskView
from tigereye.models.cinema import Cinema
from  flask import jsonify, request
from tigereye.api import ApiView
from tigereye.models.hall import Hall


class CinemaView(ApiView):

    def all(self):
        # cinemas = Cinema.query.all()
        return  Cinema.query.all()
    def halls(self):
        cid = request.args['cid']
        cinema=Cinema.query.get(cid)
        if not cinema:
            return {
                'rc':2,
                'data':{'cid':cid}
            }
        cinema.halls =Hall.query.filter_by(cid=cid).all()
        return cinema