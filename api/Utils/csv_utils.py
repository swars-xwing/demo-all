import csv


class CSV:
    def __init__(self, file_name, column_headers):
        self.file_name = file_name
        self.column_headers = column_headers
        self.file_object = None
        self.file_writer = None

        self.initialize()

    def add_row(self, row):
        self.file_writer.writerow(row)

    def close(self):
        self.file_object.close()

    def create_writer(self):
        self.file_writer = csv.writer(self.file_object, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)

    def initialize(self):
        self.open_file()
        self.create_writer()
        self.add_row(self.column_headers)
        self.close()
        self.open_file()
        self.create_writer()

    def open_file(self):
        self.file_object = open(self.file_name, 'a')
