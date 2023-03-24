import pytest

from app import create_app
from app.main.database import db
from graphene.test import Client
from app.graphql.schema import schema


@pytest.fixture()
def app():
    app = create_app('testing')

    with app.app_context():
        db.create_all()

    yield app


@pytest.fixture()
def app_ctx(app):
    with app.app_context():
        yield


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def graphql_client(app):
    return Client(schema)


