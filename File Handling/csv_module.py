def read_csv(filePath):
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

