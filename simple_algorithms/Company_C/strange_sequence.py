"""
Given sequence:
1 - 11 (2)
2nd - 21 (3)
3rd - 1211 (5)
4th - 111221 (8)

Given n, return sum of numbers in the sequence up till n
"""

import time

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


def alternateSequence(n: int) -> [[int]]:
    memory = []
    s = '1'
    for _ in range(n):
        let, temp, count = s[0], '', 0
        for l in s:
            if let == l:
                count += 1
            else:
                temp += str(count) + let
                let = l
                count = 1
        temp += str(count) + let
        s = temp
        memory.append(s)
    return memory

def sumOfTheDigits1(q: [int]) -> [int]:
    # Write your code here
    max_num = max(q)
    memory = createSequence(max_num)

    answer = []
    for item in q:
        answer.append(sum(memory[item - 1]))
    return answer

def sumOfDigits2(q: [int]) -> [int]:
    max_num = max(q)
    memory = alternateSequence(max_num)

    answer = []
    for item in q:
        sumArr = list(map(int, memory[item - 1]))
        answer.append(sum(sumArr))
    return answer

benchmark = time.time()
print(sumOfTheDigits1([50]))
endtime1 = time.time()
print(sumOfDigits2([50]))
endtime2 = time.time()

print("Completed first in {}s".format(endtime1 - benchmark))  # 2.735s
print("Completed second in {}s".format(endtime2 - endtime1))  # 1.873s