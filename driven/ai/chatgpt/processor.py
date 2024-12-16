import re
from pathlib import Path


class CodeProcessor:
    BASE_OUTPUT_PATH = "output_clean_architecture"

    def __init__(self):
        Path(self.BASE_OUTPUT_PATH).mkdir(parents=True, exist_ok=True)

    def process_response(self, response):
        """
        Procesa la respuesta generada para extraer bloques de código y comentarios ###,
        y crea las carpetas y archivos correspondientes.
        """
        # Encuentra todos los comentarios ### y bloques de código que los siguen
        matches = re.findall(r"(### (.*?)\n```swift\n(.*?)\n```)", response, re.DOTALL)
        if not matches:
            print("No se encontraron bloques de código en la respuesta.")
            return

        for match in matches:
            full_match, header, code_block = match
            # Extrae el directorio y el nombre del archivo del comentario ###
            parts = header.strip().split("/")
            folder_path = Path(self.BASE_OUTPUT_PATH) / "/".join(parts[:-1])
            file_name = parts[-1]

            # Crea la carpeta correspondiente
            folder_path.mkdir(parents=True, exist_ok=True)

            # Crea el archivo y guarda el bloque de código
            file_path = folder_path / file_name
            with open(file_path, "w") as file:
                file.write(code_block.strip())
            print(f"Archivo creado: {file_path}")

    def process_and_create_files(self, response):
        """
        Procesa una respuesta completa y crea todos los archivos necesarios.
        """
        print("Procesando respuesta...")
        self.process_response(response)
        print("¡Archivos generados exitosamente!")