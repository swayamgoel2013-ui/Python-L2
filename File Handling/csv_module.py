def read_csv(filePath, method="col"):
    if(method == 'col'):
        # read csv in column major form : dict of lists
        table = dict()
        file = open(filePath, "r")
        headers = file.readline()
        headers = headers.strip().split(",")
        col_count = len(headers)
        for hdr in headers:
            table[hdr] = list()
        for line in file:
            line = line.strip().split(",")
            for i in range(col_count):
                table[headers[i]].append(line[i])
        file.close()
        return table
    if(method == 'row'):
        # read csv in row major form : list of dicts
        table = list()
        file = open(filePath, "r")
        headers = file.readline()
        headers = headers.strip().split(",")
        col_count = len(headers)
        for line in file:
            line = line.strip().split(",")
            row = dict()
            for i in range(col_count):
                row[headers[i]] = line[i]
            table.append(row)
        file.close()
        return table
    # Unsupported Method
    print("Unsupported Method")
    return None

def show_table(table):
    if(isinstance(table, list)):
        # row major form detected
        for row in table:
            print(f"{row}")
    if(isinstance(table, dict)):
        # column major form detected
        for col in table:
            print(f"{col} : {table[col]}") 

