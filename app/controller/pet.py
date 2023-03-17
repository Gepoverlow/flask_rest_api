from flask_restful import Resource, fields, marshal_with
from app.service import pet_service


resource_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'age': fields.Integer,
    'isPlayful': fields.Boolean
}


class PetsResource(Resource):
    @marshal_with(resource_fields)
    def get(self):
        return pet_service.get_all_pets()

    @marshal_with(resource_fields)
    def post(self):
        return pet_service.add_new_pet()


class PetResource(Resource):
    @marshal_with(resource_fields)
    def get(self, pet_id):
        return pet_service.get_pet_by_id(pet_id)

    @marshal_with(resource_fields)
    def put(self, pet_id):
        return pet_service.update_pet(pet_id)

    def delete(self, pet_id):
        return pet_service.delete_pet(pet_id)
