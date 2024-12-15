from logging import Logger

from application.ports.driven.ai.ai_repository_port import AIRepositoryPort
from application.ports.driving.services.builder_service_port import BuilderServicePort


class BuilderServiceUseCase(BuilderServicePort):

    def __init__(self, chatgpt_repository: AIRepositoryPort, logger: Logger):
        self.chatgpt_repository = chatgpt_repository
        self.logger = logger

    def create(self):
        return self.chatgpt_repository.create()
