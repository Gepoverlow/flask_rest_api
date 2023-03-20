from spyne import Iterable, Integer, Boolean, Unicode, rpc, Application, Service
from spyne.protocol.soap import Soap11
from app.service import pet_service


class UpdatePetService(Service):
    @rpc(Integer, Unicode, Integer, Boolean, _returns=Iterable(Unicode))
    def update_pet(ctx, pet_id, new_name, new_age, new_playfulness):
        pet_service.update_pet_with_soap(pet_id, new_name, new_age, new_playfulness)
        yield 'ok'


def create_app():
    application = Application(
        [UpdatePetService], 'spyne.examples.flask',
        in_protocol=Soap11(validator='lxml'),
        out_protocol=Soap11()
    )

    return application

