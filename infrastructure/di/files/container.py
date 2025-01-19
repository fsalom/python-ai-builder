from dependency_injector import containers, providers

from application.services.files_services_use_case import FilesServiceUseCase
from driven.files.adapter import FilesAdapter


class FilesContainer(containers.DeclarativeContainer):
    config = providers.Configuration()
    wiring_config = containers.WiringConfiguration(modules=["driving.cli.commands"])

    files_repository = providers.Factory(FilesAdapter)

    service = providers.Factory(
        FilesServiceUseCase,
        chatgpt_repository=files_repository
    )
