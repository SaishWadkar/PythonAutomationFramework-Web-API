import csv
from csv import DictWriter

class CSVUtils:

    no_of_rows=None

    def __init__(self,source_file_path,target_file_path):
        self.__source = source_file_path
        self.__target = target_file_path

    def read_data(self):
        file = open(file=self.__source, encoding="utf-8", newline="")
        reader = csv.reader(file)  # parse data from csv file
        header = next(reader)  # returns all header list
        data = [row for row in reader]
        self.no_of_rows = len(data)
        file.close()
        return header,data

    def write_data(self,process_name,process_id):
        file = open(file=self.__target, mode='a')
        dict = {"process_name": process_name, "process_id": process_id}

        dict_writer = DictWriter(file, fieldnames=['process_name', 'process_id'])
        dict_writer.writerow(dict)
        file.close()

    def get_number_of_rows(self):
        self.read_data()
        return self.no_of_rows






