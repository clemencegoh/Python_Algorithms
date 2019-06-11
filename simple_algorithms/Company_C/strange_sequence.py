def createSequence(n: int) -> [[int]]:
    answer = [[1,1]]
    sequence = [1,1]
    for i in range(n):
        temp_num = sequence[0]
        temp_count = 1
        temp_seq = []
        for j in range(1, len(sequence)):
            if sequence[j] == sequence[j-1]:
                temp_count += 1
                if j == len(sequence) - 1:
                    temp_seq.append(temp_count)
                    temp_seq.append(temp_num)
            else:
                temp_seq.append(temp_count)
                temp_seq.append(temp_num)
                temp_count = 1
                temp_num = sequence[j]
                if j == len(sequence) - 1:
                    temp_seq.append(temp_count)
                    temp_seq.append(temp_num)
        answer.append(temp_seq)
        sequence = temp_seq
    return answer

def sumOfTheDigits(q: [int]) -> [int]:
    # Write your code here
    max_num = max(q)
    memory = createSequence(max_num)

    answer = []
    for item in q:
        answer.append(sum(memory[item - 1]))
    return answer

print(createSequence(3))
print(sumOfTheDigits([1,2,3]))