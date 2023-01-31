def pascals_triangle(n):
    result = []
    for i in range(n):
        if i == 0:
            result.append([1])
        else:
            row = [1]
            for j in range(1, i):
                row.append(result[i-1][j-1] + result[i-1][j])
            row.append(1)
            result.append(row)
    for row in result:
        for j in range(len(row),len(result)):
            print(" ",end="")
        print(row)
    print("")
