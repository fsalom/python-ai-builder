from fastapi import FastAPI

from driving.api.v1.builder.adapter import builder_router


def add_routers(app: FastAPI):
    # v1
    app.include_router(builder_router, prefix='/api/v1')
