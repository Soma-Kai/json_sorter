import json
class stdIO:
    def __init__(self):
        self.calc_type = None
        self.inputfile = None
        self.outputfile = None
        self.json_data = None

    def get_file(self):
        self.calc_type = input()
        self.inputfile = input()
        self.outputfile = input()

    def get_data(self):
        with open(self.inputfile,"r") as f:
            self.json_data = json.load(f)

    def output(self, index_array):
        output = []
        for index in index_array:
            output.append(self.json_data[index])

        with open(self.outputfile,"w") as fp:
            output_json = json.dump(output, fp, indent=3)


