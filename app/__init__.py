import os
from flask import Flask
from app import main
from app.main.database import db
from app.main.api import api
from app import model


# BASE APP & ADDING REST FUNCTIONALITY ON API
def create_app():
    app = Flask(__name__)
    app.config.from_object(main.settings[os.environ.get('APPLICATION_ENV', 'default')])

    db.init_app(app)

    # Flask API Initialization
    api.init_app(app)

    return app


# INITIALIZING APP
app = create_app()


# CREATING TABLES BASED ON THE MODELS
with app.app_context():
    db.create_all()


# ADDING SOAP FUNCTIONALITY
from app.soap import spyne
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from spyne.server.wsgi import WsgiApplication

# SOAP services are distinct wsgi applications, we should use dispatcher
# middleware to bring all aps together
app.wsgi_app = DispatcherMiddleware(app.wsgi_app, {
    '/soap': WsgiApplication(spyne.create_app())
})


# ADDING GRAPHQL FUNCTIONALITY
from app.graphql.schema import schema
from flask_graphql import GraphQLView


app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=schema,
        graphiql=True
    )
)

