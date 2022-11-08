import sys


class check:
    def __init__(self,calc_type, input_json, json_data, output_file):
        self.json_data = json_data
        self.calc_type = calc_type
        self.input_json = input_json
        self.output_file = output_file
        self.id_array = []
        for i in range( len(json_data) ):
            self.id_array.append(self.json_data[i]["id"])


    def search_error(self):
        '''
        if not self.json_key():
            print("Invalid key in input json file", file = sys.stderr)
        '''
        if not self.json_input():
            print("input json file is invalid", file = sys.stderr)
            sys.exit(1)
        if not self.json_id():
            print("Invalid id in input json file", file = sys.stderr)
            sys.exit(1)
        if not self.json_output():
            print("Invalid outputfile", file = sys.stderr)
            sys.exit(1)




    '''
    def json_key(self):
        for i in range( len(self.json_data)):
            key_list = []
            for key in self.json_data[i]:
                key_list.append(key)
            if key_list != ["id", "name", "email", "phone_number", "birthday"]:
                return False
        return True
    '''

    def json_input(self):
        if self.input_json[-5:] != ".json":
            return False
        return True


    def json_id(self):
        for val in self.id_array:
            if not isinstance(val,int):
                return False
        if len(self.id_array) != len(set(self.id_array)):
            return False

        return True

    def json_output(self):
        if self.output_file[-5:] != ".json":
            return False
        return True
    
