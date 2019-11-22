"""
2 words can be chained if last character of first word == first character of 2nd word
Determine if all words in given array can be circle chained

Given: ['eggs', 'karat', 'apple', 'snack', 'tuna']
Output: True
"""

# O(2n) time complexity, O(n) space complexity
def determine_if_all_chained(arr: [str]) -> bool:
    # first pass, throw all first into dict
    firstWords = {}
    for word in arr:
        if word[0] not in firstWords:
            firstWords[word[0]] = 0
        firstWords[word[0]] += 1
    
    # second pass, take away from dict
    for word in arr:
        if word[-1] not in firstWords:
            return False
        firstWords[word[-1]] -= 1
    
    return all(value == 0 for value in firstWords.values())



def run_driver():
    arr = ['eggs', 'karat', 'apple', 'snack', 'tuna']
    res = determine_if_all_chained(arr)
    print(res)
    assert(res)
    
run_driver()
