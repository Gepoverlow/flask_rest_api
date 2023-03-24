from flask_restful import reqparse
from graphql import GraphQLError

from app import db
from app.model import PetModel

pet_post_args = reqparse.RequestParser()
pet_post_args.add_argument("name", type=str, help="Name of the pet is required as string", required=True)
pet_post_args.add_argument("age", type=int, help="Age of the pet is required as integer", required=True)
pet_post_args.add_argument("isPlayful", type=bool, help="Playfulness of the pet is required as boolean", required=True)


def get_all_pets():
    result = PetModel.query.all()
    result_list = list()
    for pet in result:
        result_list.append(pet)

    return result_list


def add_pet():
    args = pet_post_args.parse_args()
    pet = PetModel(name=args['name'], age=args['age'], isPlayful=args['isPlayful'])

    db.session.add(pet)
    db.session.commit()

    return pet, 201


def update_pet(pet_id, new_name, new_age, new_playfulness):
    result = PetModel.query.filter_by(id=pet_id).first()
    if not result:
        return

    if new_name is not None:
        result.name = new_name
    if new_age is not None:
        result.age = new_age
    if new_playfulness is not None:
        result.isPlayful = new_playfulness

    db.session.commit()

    return result


def delete_pet(pet_id):
    result = PetModel.query.filter_by(id=pet_id).first()
    if not result:
        raise GraphQLError(f"Pet with id {pet_id} not found")

    db.session.delete(result)
    db.session.commit()

    return result

