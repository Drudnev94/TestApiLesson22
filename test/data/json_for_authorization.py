
class JsonForAuthorization:

    def get_data_autorization(self,login = str, password = str):
        return  {"email": login, "password": password,}


