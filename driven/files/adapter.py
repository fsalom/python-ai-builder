from typing import List

from application.ports.driven.files.files_repository_port import FilesRepositoryPort
from domain.directory import Directory


class FilesAdapter(FilesRepositoryPort):
    def read_dir(self, path) -> List[Directory]:
        pass

    def read_file(self, path, extensions: [str]) -> str:
        pass
