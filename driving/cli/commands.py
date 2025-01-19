from infrastructure.di.files.container import FilesContainer


def execute_command(command: str, **kwargs):
    container = FilesContainer()

    # Lógica de los comandos
    if command == "example":
        use_case = container.service()
        result = use_case.execute(kwargs.get("arg1"), kwargs.get("arg2"))
        print(f"Resultado: {result}")
    else:
        print(f"Comando desconocido: {command}")
