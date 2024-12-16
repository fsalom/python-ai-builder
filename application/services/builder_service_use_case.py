from logging import Logger

from application.ports.driven.ai.ai_repository_port import AIRepositoryPort
from application.ports.driving.services.builder_service_port import BuilderServicePort


class BuilderServiceUseCase(BuilderServicePort):

    def __init__(self, chatgpt_repository: AIRepositoryPort):
        self.chatgpt_repository = chatgpt_repository

    def create(self, json_input):
        return self.chatgpt_repository.create(json_input=json_input)
