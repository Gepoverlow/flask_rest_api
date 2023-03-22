from spyne import Iterable, Integer, Boolean, Unicode, rpc, Application, Service, Fault
from spyne.protocol.soap import Soap11
from app.service import pet_service
from app import app


class UpdatePetService(Service):
    @rpc(Integer, Unicode, Integer, Boolean, _returns=Iterable(Unicode))
    def update_pet(ctx, pet_id, new_name, new_age, new_playfulness):
        with app.app_context():
            result = pet_service.update_pet_with_soap(pet_id, new_name, new_age, new_playfulness)
            if not result:
                yield f"Pet with id {pet_id} not found"

            if result:
                yield f"pet name: {result.name}, pet age: {result.age}, pet playfulness: {result.isPlayful}"


def create_app():
    application = Application(
        [UpdatePetService], 'spyne.examples.flask',
        in_protocol=Soap11(validator='lxml'),
        out_protocol=Soap11()
    )

    return application

