from flask_restful import Resource,Api
from flask import request
from .. import auth

from flask_jwt_extended import create_access_token,jwt_required

from ..models import Usuario
from ..schemas import UsuarioSchema

api = Api(auth)

class UsuarioResource(Resource):
    
    @jwt_required
    def get(self):
        
        context = {
            'status':True,
            'content':'usuarios'
        }
        
        return context
        
        
api.add_resource(UsuarioResource,'/usuario')
