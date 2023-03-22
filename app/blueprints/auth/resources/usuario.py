from flask_restful import Resource,Api
from flask import request
from .. import auth

from flask_jwt_extended import create_access_token,jwt_required

from ..models import Usuario
from ..schemas import UsuarioSchema

from werkzeug.security import generate_password_hash,check_password_hash

api = Api(auth)

class UsuarioResource(Resource):
    
    @jwt_required()
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
    
class LoginResource(Resource):
    def post(self):
        data = request.get_json()
        username = data['username']
        password = data['password']
        
        objUsuario = Usuario.query.filter_by(username=username)
        
        if check_password_hash(objUsuario[0].password,password):
            payload = {
                'id': objUsuario[0].id,
                'username':objUsuario[0].username
            }
            access_token = create_access_token(payload)
        else:
            access_token = "credenciales no validas"
            
        context = {
            'status':True,
            'content':access_token
        }
        
        return context
        
        
api.add_resource(UsuarioResource,'/usuario')
api.add_resource(LoginResource,'/login')
