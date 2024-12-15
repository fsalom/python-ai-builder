from fastapi import FastAPI

from infrastructure.di.builder.container import BuilderContainer


def add_containers(app: FastAPI):
    builder_container = BuilderContainer()
    app.builder_container = builder_container
