from flask_restful import Resource,Api
from flask import request
from .. import auth

from flask_jwt_extended import create_access_token,jwt_required

from ..models import Usuario
from ..schemas import UsuarioSchema

from werkzeug.security import generate_password_hash,check_password_hash

api = Api(auth)

class UsuarioResource(Resource):
    
    @jwt_required
    def get(self):
        
        data = Usuario.get_all()
        
        data_schema = UsuarioSchema(many=True)
        
        context = {
            'status':True,
            'content': data_schema.dump(data)
        }
        
        return context
    
    def post(self):
        data = request.get_json()
        username = data['username']
        password = data['password']
        
        password_hash = generate_password_hash(password)
        
        objUsuario = Usuario(username,password_hash)
        objUsuario.save()
        
        data_schema = UsuarioSchema()
        
        context = {
            'status':True,
            'content':data_schema.dump(objUsuario)
        }
        
        return context
        
        
api.add_resource(UsuarioResource,'/usuario')
