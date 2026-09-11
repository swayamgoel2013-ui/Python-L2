class Table:
    def __init__(self, data):

        # if data is a string, it is a file path
        if(isinstance(data, str)):
            # open the file for reading
            filePath = data
            file = open(filePath, "r")
            # read the first line to get the column names
            self.columns = file.readline().strip().split(",")
            self.col_count = len(self.columns)
            # create an empty table with the column names
            self.data = {}
            for col in self.columns:
                self.data[col] = []
            # read the rest of the file to get the data rows
            self.row_count = 0
            for line in file:
                values = line.strip().split(",")
                self.row_count += 1
                for (i,header) in enumerate(self.columns):
                    self.data[header].append(values[i])
            # close the file
            file.close()

        # if data is a dict, it is a table
        if(isinstance(data, dict)):
            # store the data in the table
            self.data = data
            # store metadata
            self.columns = list(data.keys())
            self.col_count = len(self.columns)
            self.row_count = len(data[self.columns[0]])
        
    def show(self, filePath = "output.txt"):
        # calculate the width of each column
        widths = {}
        for col in self.data:
            widths[col] = len(col)
            for i in range(self.row_count):
                widths[col] = max(widths[col], len(self.data[col][i]))
        # initialize horizontal line
        horizontal = "+"
        for col in self.data:
            horizontal += "-" * (widths[col] + 2) + "+"
        horizontal += "\n"
        # write the table in the file
        file = open(filePath, "w")
        file.write(horizontal)
        for col in self.data:
            file.write(f"| {col:{widths[col]}} ")
        file.write(f"|\n{horizontal}")
        for i in range(self.row_count):
            for col in self.data:
                if(self.data[col][i].isnumeric()):
                    file.write(f"| {self.data[col][i]:>{widths[col]}} ")
                else:
                    file.write(f"| {self.data[col][i]:<{widths[col]}} ")
            file.write("|\n")
        file.write(horizontal)
        file.close()

    def get_size(self):
        # return the size of the table
        return (self.row_count, self.col_count)

    def get_rows(self, row_numbers):
        # create a new table
        data = {}
        for col in self.columns:
            data[col] = []
        # filter the specified rows
        for col in self.columns:
            for i in range(self.row_count):
                if(i in row_numbers):
                    data[col].append(self.data[col][i])
        # return a new table with the specified rows
        return Table(data)
    
    def get_columns(self, column_names):
        # create a new table
        data = {}
        # filter the specified columns
        for col in self.columns :
            if(col in column_names):
                data[col] = self.data[col]
        # return a new table with the specified columns
        return Table(data)

    def get_value(self, row_number, col_name):
        pass

if __name__ == "__main__":
    # read the table data from the file
    pokedex = Table("dataset.csv")

    # print the table
    pokedex.show()

    # get selected rows from the table
    few_rows = pokedex.get_rows([0, 1, 2])
    few_rows.show("few_rows.txt")

    # get selected columns from the table
    few_cols = pokedex.get_columns(["name", "type_1", "type_2"])
    few_cols.show("few_cols.txt")