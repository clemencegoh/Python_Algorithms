"""
Gary is an avid hiker. He tracks his hikes meticulously, paying close attention to small details like topography.
During his last hike he took exactly  steps. For every step he took, he noted if it was an uphill, U, or a downhill,
D step. Gary's hikes start and end at sea level and each step up or down represents a  unit change in altitude.
We define the following terms:

A mountain is a sequence of consecutive steps above sea level,
starting with a step up from sea level and ending with a step down to sea level.
A valley is a sequence of consecutive steps below sea level,
starting with a step down from sea level and ending with a step up to sea level.
Given Gary's sequence of up and down steps during his last hike,
find and print the number of valleys he walked through.

Input Format

The first line contains an integer n, the number of steps in Gary's hike.
The second line contains a single string s, of n characters that describe his path.

:input: 8, UDDDUDUU
_/\\       _
   \\     /
    \\/\\/
:output: 1
"""


# Completed
class CountingValleysSolution:
    def solve(self, n, s):
        """
        Concept:
            Starting will always be at sea level.
            Idea is thus to determine how many times the steps bring him back up to sea level from a valley
            Ignore mountains
        """
        state = 0
        valleyCounter = 0
        for i in range(n):
            nextStep = s[i].upper()
            if nextStep == "U":
                state -= 1
                if state == 0:
                    valleyCounter += 1
            if nextStep == "D":
                state += 1

        return valleyCounter
        
 
sol = CountingValleysSolution()
print(sol.solve(8, "UDDDUDUU"))
