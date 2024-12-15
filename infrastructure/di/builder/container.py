from dependency_injector import providers, containers

from application.services.builder_service_use_case import BuilderServiceUseCase
from driven.ai.chatgpt.adapter import ChatGPTAdapter


class BuilderContainer(containers.DeclarativeContainer):
    config = providers.Configuration()
    wiring_config = containers.WiringConfiguration(modules=["driving.api.v1.builder"])
    chatgpt_repository = providers.Factory(ChatGPTAdapter)

    service = providers.Factory(
        BuilderServiceUseCase,
        chatgpt_repository=chatgpt_repository
    )
