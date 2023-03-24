from flask_restful import Api
from app.controller.pet_controller import PetController

# Flask API Configuration
api = Api(
    catch_all_404s=True,
    prefix='/rest'
)

api.add_resource(PetController, '/pets')

