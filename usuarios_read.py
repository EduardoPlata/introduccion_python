import json

registro = open("personas.json","r")
personas = registro.read()
personas = json.loads(personas)

