class Table:
    def __init__(self, filePath):
        file = open(filePath, "r")
        self.columns = file.readline().strip().split(",")
        self.col_count = len(self.columns)

        self.table = {}
        for col in self.columns:
            self.table[col] = []

        self.row_count = 0
        for line in file:
            values = line.strip().split(",")
            self.row_count += 1
            for (i,header) in enumerate(self.columns):
                self.table[header].append(values[i])
        file.close()
        
    def show(self, filePath = "output.txt"):
        widths = {}
        for col in self.table:
            widths[col] = len(col)
            for i in range(self.row_count):
                widths[col] = max(widths[col], len(self.table[col][i]))
        horizontal = "+"
        for col in self.table:
            horizontal += "-" * (widths[col] + 2) + "+"
        horizontal += "\n" 
        file = open(filePath, "w")
        file.write(horizontal)
        for col in self.table:
            file.write(f"| {col:{widths[col]}} ")
        file.write(f"|\n{horizontal}")
        for i in range(self.row_count):
            for col in self.table:
                if(self.table[col][i].isnumeric()):
                    file.write(f"| {self.table[col][i]:>{widths[col]}} ")
                else:
                    file.write(f"| {self.table[col][i]:<{widths[col]}} ")
            file.write("|\n")
        file.write(horizontal)
        file.close()

    def get_size(self):
        return (self.row_count, self.col_count)

    def get_rows(self, *row_numbers):
        pass

    def get_columns(self, *column_names):
        pass

    def get_value(self, row_number, col_name):
        pass

if __name__ == "__main__":
    pokedex = Table("dataset.csv")
    print("Table size = ", pokedex.get_size())
    pokedex.show()