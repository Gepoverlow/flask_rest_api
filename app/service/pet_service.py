from flask_restful import reqparse, abort
from app import db
from app.model import Pet

pet_post_args = reqparse.RequestParser()
pet_post_args.add_argument("name", type=str, help="Name of the pet is required", required=True)
pet_post_args.add_argument("age", type=int, help="Age of the pet is required as integer", required=True)
pet_post_args.add_argument("isPlayful", type=bool, help="Playfulness of the pet is required as boolean", required=True)

pet_put_args = reqparse.RequestParser()
pet_put_args.add_argument("name", type=str, help="Name of the pet")
pet_put_args.add_argument("age", type=int, help="Age of the pet")
pet_put_args.add_argument("isPlayful", type=bool, help="Playfulness of the pet")


def get_all_pets():
    result = Pet.query.all()
    result_list = list()
    for pet in result:
        result_list.append(pet)

    return result_list


def get_pet_by_id(pet_id):
    result = Pet.query.filter_by(id=pet_id).first()
    if not result:
        abort(404, message="Unable to find pet with id {}".format(pet_id))
    return result


def add_new_pet():
    args = pet_post_args.parse_args()
    pet = Pet(name=args['name'], age=args['age'], isPlayful=args['isPlayful'])
    db.session.add(pet)
    db.session.commit()
    return pet, 201


def update_pet(pet_id):
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


def update_pet_with_soap(pet_id, new_name, new_age, new_playfulness):
    result = Pet.query.filter_by(id=pet_id).first()

    result.name = new_name
    result.age = new_age
    result.isPlayful = new_playfulness

    db.session.commit()
    return result


def delete_pet(pet_id):
    result = Pet.query.filter_by(id=pet_id).first()
    if not result:
        abort(404, message="Unable to find pet with id {}".format(pet_id))
    db.session.delete(result)
    db.session.commit()
    return '', 204

