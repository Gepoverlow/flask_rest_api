import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from app.model import PetModel
from app.service import pet_service


class Pet(SQLAlchemyObjectType):
    class Meta:
        model = PetModel
        interfaces = (graphene.relay.Node,)


class DeletePet(graphene.Mutation):
    class Arguments:
        pet_id = graphene.String(required=True)

    ok = graphene.Boolean()
    pet = graphene.Field(lambda: Pet)

    def mutate(self, info, pet_id):
        deleted_pet = pet_service.delete_pet(pet_id)
        ok = True
        return DeletePet(pet=deleted_pet, ok=ok)


class Query(graphene.ObjectType):
    pet = graphene.Field(Pet)


class Mutation(graphene.ObjectType):
    delete_pet = DeletePet.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)

