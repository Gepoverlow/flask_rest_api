from flask_restful import Api
from app.controllers.pet import PetResource, PetsResource

# Flask API Configuration
api = Api(
    catch_all_404s=True,
    prefix='/api'
)

api.add_resource(PetsResource, '/pets')
api.add_resource(PetResource, '/pet/<string:pet_id>')

