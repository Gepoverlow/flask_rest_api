from flask import Flask
from flask_restful import Api, Resource, reqparse, fields, marshal_with, abort
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)
db.create_all()


class PetModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    isPlayful = db.Column(db.Boolean, nullable=False)

    def __repr__(self):
        return f"Pet(name = {self.name}, age = {self.age}, isPlayful = {self.isPlayful})"


db.drop_all()
db.create_all()

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


class Pets(Resource):
    @marshal_with(resource_fields)
    def get(self):
        result = PetModel.query.all()
        result_list = list()
        for pet in result:
            result_list.append(pet)

        return result_list

    @marshal_with(resource_fields)
    def post(self):
        args = pet_post_args.parse_args()
        pet = PetModel(name=args['name'], age=args['age'], isPlayful=args['isPlayful'])
        db.session.add(pet)
        db.session.commit()
        return pet, 201


class Pet(Resource):
    @marshal_with(resource_fields)
    def get(self, pet_id):
        result = PetModel.query.filter_by(id=pet_id).first()
        if not result:
            abort(404, message="Unable to find pet with id {}".format(pet_id))
        return result

    @marshal_with(resource_fields)
    def put(self, pet_id):
        args = pet_put_args.parse_args()
        result = PetModel.query.filter_by(id=pet_id).first()
        if not result:
            abort(404, message="Unable to find pet with id {}".format(pet_id))

        if args['name']:
            result.name = args['name']
        if args['age']:
            result.age = args['age']
        if args['isPlayful']:
            result.isPlayful = False

        db.session.commit()
        return result

    def delete(self, pet_id):
        result = PetModel.query.filter_by(id=pet_id).first()
        if not result:
            abort(404, message="Unable to find pet with id {}".format(pet_id))
        db.session.delete(result)
        db.session.commit()
        return '', 204


api.add_resource(Pets, "/pets")
api.add_resource(Pet, "/pet/<string:pet_id>")


if __name__ == "__main__":
    app.run(debug=True)

