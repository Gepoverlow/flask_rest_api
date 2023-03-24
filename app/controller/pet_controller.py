from flask_restful import Resource, fields, marshal_with
from app.service import pet_service


resource_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'age': fields.Integer,
    'isPlayful': fields.Boolean
}


class PetController(Resource):
    @marshal_with(resource_fields)
    def get(self):
        return pet_service.get_all_pets()

    @marshal_with(resource_fields)
    def post(self):
        return pet_service.add_pet()

