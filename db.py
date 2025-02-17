import json

class DataBase:
    def add_data(self, email, name, pws):
        try:
            with open('database.json', 'r') as data:
                result = json.load(data)
        except (FileNotFoundError, json.JSONDecodeError):
            result = {}

        if email in result:
            print("Already Exists")
            return 0
        else:
            result[email] = {'name': name, 'password': pws}
            with open('database.json', 'w') as da:
                json.dump(result, da, indent=4)
            return 1

    def check_data(self, email, psw):
        try:
            with open('database.json', 'r') as data:
                result = json.load(data)
        except (FileNotFoundError, json.JSONDecodeError):
            return 0

        if email in result and result[email]['password'] == psw:
            return 1
        return 0
