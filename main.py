from flask import Flask
from flask_restful import Api, Resource, reqparse, abort

app = Flask(__name__)
api = Api(app)

pet_args = reqparse.RequestParser()
pet_args.add_argument("name", type=str, help="Name of the pet", required=True)
pet_args.add_argument("age", type=int, help="Age of the pet", required=True)
pet_args.add_argument("isCute", type=bool, help="Cuteness of the pet", required=True)

pets = {
        "1": {
            "name": "rafels",
            "age": 12,
            "isCute": True
        },
        "2": {
            "name": "toffy",
            "age": 5,
            "isCute": True
        },
}


def abort_if_pet_not_found(pet_id):
    if pet_id not in pets:
        abort(404, message="Pet with id {} not found".format(pet_id))


class Pets(Resource):
    def get(self):
        return pets

    def post(self):
        args = pet_args.parse_args()
        last_key = list(pets)[-1]
        next_key = str(int(last_key) + 1)
        pets[next_key] = args
        return pets[next_key]


class Pet(Resource):
    def get(self, pet_id):
        abort_if_pet_not_found(pet_id)
        return pets[pet_id]

    def put(self, pet_id):
        abort_if_pet_not_found(pet_id)
        args = pet_args.parse_args()
        pets[pet_id] = args
        return pets[pet_id], 201

    def delete(self, pet_id):
        abort_if_pet_not_found(pet_id)
        del pets[pet_id]
        return '', 204


api.add_resource(Pets, "/pets")
api.add_resource(Pet, "/pet/<string:pet_id>")


if __name__ == "__main__":
    app.run(debug=True)

