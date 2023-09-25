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

def operationCalculator(matrix, str1, str2):
    i = len(matrix) - 1
    j = len(matrix[0]) - 1
    operations = {"Insertions": 0, "Deletions": 0, "Substitutions": 0}

    while i > 0 or j > 0:
        if i > 0 and j > 0 and matrix[i][j] == matrix[i - 1][j - 1] + (str1[i - 1] != str2[j - 1]):
            # No operation (characters match) or substitution
            if str1[i - 1] != str2[j - 1]:
                operations["Substitutions"] += 1
            i -= 1
            j -= 1
        elif i > 0 and matrix[i][j] == matrix[i - 1][j] + 1:
            # Deletion
            operations["Deletions"] += 1
            i -= 1
        elif j > 0 and matrix[i][j] == matrix[i][j - 1] + 1:
            # Insertion
            operations["Insertions"] += 1
            j -= 1

    return operations



a = input("Enter the first string: ")
b = input("Enter the second string: ")

dp = levenshmithDistance(a,b)
operations = operationCalculator(dp,a,b)
printMatrix(dp)
print("The Levenshmith Distance is: ",dp[-1][-1])
print("The number of Insertions are: ",operations["Insertions"])
print("The number of Deletions are: ",operations["Deletions"])
print("The number of Substitutions are: ",operations["Substitutions"])

