import re

import openai
import os
from pathlib import Path

from openai import OpenAI

from application.ports.driven.ai.ai_repository_port import AIRepositoryPort
from driven.ai.chatgpt.processor import CodeProcessor


class ChatGPTAdapter(AIRepositoryPort):
    BASE_OUTPUT_PATH = "output_clean_architecture"

    def __init__(self):
        self.client = OpenAI(
            api_key=os.environ.get(os.environ.get('OPENAI_API_KEY')),
        )
        self.conversation_history = []

    def generate_code(self, prompt, tech):
        """
        Genera código usando el modelo GPT.
        """
        try:
            self.conversation_history.append({"role": "user", "content": prompt})
            response = self.client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "system",
                     "content": f"Eres un asistente que genera código para arquitecturas clean en {tech}."}
                ] + self.conversation_history,
                max_tokens=3000,
                temperature=0.5
            )

            response_content = response.choices[0].message.content.strip()
            self.conversation_history.append({"role": "assistant", "content": response_content})

            print(response_content)
            return response_content
        except Exception as e:
            print(f"Error al generar código: {e}")
            return None

    def create_directories(self):
        """
        Crea las carpetas necesarias para las capas de la arquitectura clean.
        """
        for layer in ["Domain", "Data", "Presentation"]:
            path = Path(self.BASE_OUTPUT_PATH) / layer
            path.mkdir(parents=True, exist_ok=True)

    def save_file(self, layer, filename, content):
        """
        Guarda el contenido generado en un archivo dentro de la carpeta correspondiente.
        """
        file_path = Path(self.BASE_OUTPUT_PATH) / layer / filename
        with open(file_path, "w") as file:
            file.write(content)

    def create_prompts(self, json_input, tech):
        """
        Crea los prompts necesarios para las capas de la arquitectura clean.
        """
        domain_prompt = self.read_file(f"driven/ai/chatgpt/prompts/{tech}/domain.prompt")
        data_prompt = self.read_file(f"driven/ai/chatgpt/prompts/{tech}/data.prompt")
        return {
            "Domain": f"Dado el siguiente JSON: {json_input} {domain_prompt}",
            "Data": f"Dado el siguiente JSON: {json_input}, {data_prompt}",
            #"Presentation": f"Dado el siguiente JSON: {json_input}, genera los ViewModels y cualquier otra clase necesaria para la capa de presentación en una arquitectura clean para iOS."
        }

    def read_file(self, file_path):
        with open(file_path, 'r') as file:
            return file.read()

    def create(self, json_input, tech):
        """
        Genera las clases y las guarda en las carpetas correspondientes.
        """
        self.create_directories()
        processor = CodeProcessor(tech)
        prompts = self.create_prompts(json_input, tech)
        for layer, prompt in prompts.items():
            print(f"Generando código para la capa {layer}...")
            result = self.generate_code(prompt, tech)
            processor.process_and_create_files(result)
        print(f"Archivos generados en la carpeta '{self.BASE_OUTPUT_PATH}'.")
