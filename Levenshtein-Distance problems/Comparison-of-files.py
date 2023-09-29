def levenshmithDistance(a,b):
    len1 = len(a)
    len2 = len(b)
    dpMatrix = [[0 for i in range(len2+1)] for j in range(len1+1)]
    for i in range(len1+1):
        dpMatrix[i][0] = i
    for j in range(len2+1):
        dpMatrix[0][j] = j
    for i in range(1,len1+1):
        for j in range (1,len2+1):
            if (a[i-1]==b[j-1]):
                dpMatrix[i][j] = dpMatrix[i-1][j-1]
            else:
                dpMatrix[i][j] = 1 + min(dpMatrix[i-1][j-1],    #insertion
                                         dpMatrix[i-1][j],      #deletion
                                         dpMatrix[i][j-1])      #substitution
    return dpMatrix

def printMatrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(matrix[i][j], end = " ")
        print()

def operationCalculator(matrix):
    m, n = len(matrix) - 1, len(matrix[0]) - 1
    operations = {"Insertions": 0, "Deletions": 0, "Substitutions": 0}

    while m > 0 or n > 0:
        if m > 0 and matrix[m][n] == matrix[m - 1][n] + 1:
            operations["Deletions"] += 1
            m -= 1
        elif n > 0 and matrix[m][n] == matrix[m][n - 1] + 1:
            operations["Insertions"] += 1
            n -= 1
        else:
            if matrix[m][n] != matrix[m - 1][n - 1]:
                operations["Substitutions"] += 1
            m -= 1
            n -= 1

    return operations


with open('reference.txt','r') as reference:
    ref = reference.read()
    refWords = ref.split()

with open('hypothesis.txt','r') as hypothesis:
    hyp = hypothesis.read()
    hypWords = hyp.split()

matrix = levenshmithDistance(hypWords, refWords)
operations = operationCalculator(matrix)

with open('result.txt','a') as result:
    result.write("Insertions: " + str(operations["Insertions"]) + "\n")
    result.write("Deletions: " + str(operations["Deletions"]) + "\n")
    result.write("Substitutions: " + str(operations["Substitutions"]) + "\n")
    result.write("\n")
    result.write("Levenshmith Distance: " + str(matrix[-1][-1]))
