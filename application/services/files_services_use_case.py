from application.ports.driven.files.files_repository_port import FilesRepositoryPort
from application.ports.driving.services.files_service_port import FilesServicePort


class FilesServiceUseCase(FilesServicePort):

    def __init__(self,
                 files_repository: FilesRepositoryPort,):
        self.files_repository = files_repository

    def read_dir(self, path):
        directories = self.files_repository.read_dir(path="")
