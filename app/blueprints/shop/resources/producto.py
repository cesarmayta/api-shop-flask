from flask_restful import Resource,Api
from flask import request
from .. import shop

from ..models import Producto
from ..schemas import ProductoSchema


api = Api(shop)



class ProductoResource(Resource):
    
    def get(self):

        data = Producto.get_all()

        data_schema = ProductoSchema(many=True)

        context = {
            'status':True,
            'content':data_schema.dump(data)
        }
        
        return context

    def post(self):
        data = request.get_json()
        nombre = data["nombre"]
        precio = data["precio"]

        objProducto = Producto(nombre)
        objProducto.precio = precio
        objProducto.save()

        data_schema = ProductoSchema()

        context = {
            'status':True,
            'content':data_schema.dump(objProducto)
        }

        return context

api.add_resource(ProductoResource,'/producto')