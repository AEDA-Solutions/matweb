from json import JSONEncoder

class ModelParaJson(JSONEncoder):
    def default(self, o):
        return o.__dict__