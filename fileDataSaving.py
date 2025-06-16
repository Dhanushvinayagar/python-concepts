
class File:
    __file_data = ''

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name
    
    def __convert_file_to_json(self,file_data):
        data = file_data
        data = data.split('\n')
        keys = data[0].split(' ')
        response = []
        for x in data[1:]:
            response.append(dict(zip(keys,x.split(' '))))
        return response
        
    def read(self):
        with open(self.name,"r") as f:
            file = f.read()
            self.__file_data = self.__convert_file_to_json(file)
    
    def get_file_data(self):
        return self.__file_data
        
class Database:
    def __init__(self):
        self.db = 'Database'

    def save(self,data):
        print(str(data))
        return str(data)
    
file = 'data.txt'
f = File(file)
f.read()
file_data = f.get_file_data()
db = Database()
db.save(file_data)