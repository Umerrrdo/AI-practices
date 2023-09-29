common_words = {"the", "of", "and", "a", "be", "this", "there", "an", "been", "some"}

def levenshmithDistance(a, b):
    len1, len2 = len(a), len(b)
    dp = [[0 for _ in range(len2 + 1)] for _ in range(len1 + 1)]

    for i in range(len1 + 1):
        dp[i][0] = i

    for j in range(len2 + 1):
        dp[0][j] = j

    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            cost = 0 if a[i - 1] == b[j - 1] else 1

            if a[i - 1] in common_words and b[j - 1] in common_words:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(
                    dp[i - 1][j] + 1,       # Deletion
                    dp[i][j - 1] + 1,       # Insertion
                    dp[i - 1][j - 1] + cost  # Substitution
                )

    return dp

def operationCalculator(matrix, a, b):
    m, n = len(matrix) - 1, len(matrix[0]) - 1
    operations = {"Insertions": 0, "Deletions": 0, "Substitutions": 0}

    while m > 0 or n > 0:
        if m > 0 and matrix[m][n] == matrix[m - 1][n] + 1:
            if a[m - 1] not in common_words:
                operations["Deletions"] += 1
            m -= 1
        elif n > 0 and matrix[m][n] == matrix[m][n - 1] + 1:
            if b[n - 1] not in common_words:
                operations["Insertions"] += 1
            n -= 1
        else:
            if matrix[m][n] != matrix[m - 1][n - 1]:
                if a[m - 1] not in common_words and b[n - 1] not in common_words:
                    operations["Substitutions"] += 1
            m -= 1
            n -= 1

    return operations

with open('reference.txt', 'r') as reference:
    ref = reference.read()
    refWords = ref.split()

with open('hypothesis.txt', 'r') as hypothesis:
    hyp = hypothesis.read()
    hypWords = hyp.split()

matrix = levenshmithDistance(refWords, hypWords)
operations = operationCalculator(matrix, refWords, hypWords)

with open('result2.txt','a') as result:
    result.write("Insertions: " + str(operations["Insertions"]) + "\n")
    result.write("Deletions: " + str(operations["Deletions"]) + "\n")
    result.write("Substitutions: " + str(operations["Substitutions"]) + "\n")
    result.write("\n")
    result.write("Levenshmith Distance: " + str(matrix[-1][-1]))
