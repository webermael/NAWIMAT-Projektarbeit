import json

class FileManager:
    def __init__(self):
        pass

    def load_file(self, path):
        with open(path, "r") as file:
            file_content = json.load(file)
        file.close()
        return file_content
    
    def save_dict(self, path, dict):
        with open(path, "w") as file:
            file = open(path, "w")
        json.dump(dict, file)
        file.close()