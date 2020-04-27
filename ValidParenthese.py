class Solution:
    def isValid(self, input):
        UpperToLower = {"{": "}", "[": "]", "(": ")",
                        "}": None, "]": None, ")": None}
        i = 0
        loops = len(input) / 2 + 1
        while (i < loops):
            index = 0
            while (index < len(input)-1):
                if(UpperToLower[input[index]] == input[index+1]):
                    input = input[0:index] + input[index+2:len(input)]
                index = index + 1
            i = i + 1
        if input:
            return False
        else:
            return True
        """
        algorithm : when we find an closing bracket right next the its opening bracket then we pop both of them,
                    eventually the string will be empty if it's valid 
        """