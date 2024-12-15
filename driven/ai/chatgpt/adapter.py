import openai
import os
import json
from pathlib import Path

from application.ports.driven.ai.ai_repository_port import AIRepositoryPort


class ChatGPTAdapter(AIRepositoryPort):
    API_KEY = os.environ.get('APIGPT')
    openai.api_key = API_KEY

    BASE_OUTPUT_PATH = "output_ios_clean_architecture"

    def generate_code(prompt):
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=1000,
            n=1,
            stop=None,
            temperature=0.5
        )
        return response.choices[0].text.strip()

    def create_directories(self):
        for layer in ["Domain", "Data", "Presentation"]:
            path = Path(self.BASE_OUTPUT_PATH) / layer
            path.mkdir(parents=True, exist_ok=True)

    def save_file(self, layer, filename, content):
        file_path = Path(self.BASE_OUTPUT_PATH) / layer / filename
        with open(file_path, "w") as file:
            file.write(content)

    def create_prompts(json_input):
        return {
            "Domain": f"Dado el siguiente JSON: {json_input}, genera las clases de dominio necesarias para representar las entidades en una arquitectura clean para iOS.",
            "Data": f"Dado el siguiente JSON: {json_input}, genera los repositorios y modelos necesarios para la capa de datos en una arquitectura clean para iOS.",
            "Presentation": f"Dado el siguiente JSON: {json_input}, genera los ViewModels y cualquier otra clase necesaria para la capa de presentación en una arquitectura clean para iOS."
        }

    def create(self, json_input):
        self.create_directories()

        try:
            json_data = json.loads(json_input)
        except json.JSONDecodeError:
            print("El JSON proporcionado no es válido.")
            return

        prompts = self.create_prompts(json_input)

        for layer, prompt in prompts.items():
            print(f"Generando código para la capa {layer}...")
            code = self.generate_code(prompt)
            filename = f"{layer.lower()}_layer.swift"
            self.save_file(layer, filename, code)

        print(f"Archivos generados en la carpeta '{self.BASE_OUTPUT_PATH}'.")


