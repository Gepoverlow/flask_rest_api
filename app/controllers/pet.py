from flask_restful import Resource, reqparse, fields, marshal_with, abort
from app import db
from app.models import Pet


pet_post_args = reqparse.RequestParser()
pet_post_args.add_argument("name", type=str, help="Name of the pet", required=True)
pet_post_args.add_argument("age", type=int, help="Age of the pet", required=True)
pet_post_args.add_argument("isPlayful", type=bool, help="Playfulness of the pet", required=True)

pet_put_args = reqparse.RequestParser()
pet_put_args.add_argument("name", type=str, help="Name of the pet")
pet_put_args.add_argument("age", type=int, help="Age of the pet")
pet_put_args.add_argument("isPlayful", type=bool, help="Playfulness of the pet")

resource_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'age': fields.Integer,
    'isPlayful': fields.Boolean
}


class PetsResource(Resource):
    @marshal_with(resource_fields)
    def get(self):
        result = Pet.query.all()
        result_list = list()
        for pet in result:
            result_list.append(pet)

        return result_list

    @marshal_with(resource_fields)
    def post(self):
        args = pet_post_args.parse_args()
        pet = Pet(name=args['name'], age=args['age'], isPlayful=args['isPlayful'])
        db.session.add(pet)
        db.session.commit()
        return pet, 201


class PetResource(Resource):
    @marshal_with(resource_fields)
    def get(self, pet_id):
        result = Pet.query.filter_by(id=pet_id).first()
        if not result:
            abort(404, message="Unable to find pet with id {}".format(pet_id))
        return result

    @marshal_with(resource_fields)
    def put(self, pet_id):
        args = pet_put_args.parse_args()
        result = Pet.query.filter_by(id=pet_id).first()
        if not result:
            abort(404, message="Unable to find pet with id {}".format(pet_id))

        if args['name'] is not None:
            result.name = args['name']
        if args['age'] is not None:
            result.age = args['age']
        if args['isPlayful'] is not None:
            result.isPlayful = args['isPlayful']

        db.session.commit()
        return result

    def delete(self, pet_id):
        result = Pet.query.filter_by(id=pet_id).first()
        if not result:
            abort(404, message="Unable to find pet with id {}".format(pet_id))
        db.session.delete(result)
        db.session.commit()
        return '', 204
