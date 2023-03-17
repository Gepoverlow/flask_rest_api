# -*- coding: utf-8 -*-
import os


class Config:

    # project root directory
    BASE_DIR = os.path.join(os.pardir, os.path.dirname(__file__))

    # Flask Configuration
    # --------------------------------------------------------------------
    DEBUG = False
    TESTING = False
    PORT = 8000

    # sqlalchemy database main
    # --------------------------------------------------------------------
    SQLALCHEMY_DATABASE_URI = 'sqlite:///pet-database.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):

    ENV = os.environ.get("FLASK_ENV", "development")
    DEBUG = True
    ASSETS_DEBUG = True


class ProductionConfig(Config):

    ENV = os.environ.get("FLASK_ENV", "production")
    DEBUG = False
    USE_RELOADER = False


settings = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig,
}

