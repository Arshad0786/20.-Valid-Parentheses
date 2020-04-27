class Solution:
    def isValid(self, input):
        stack = []
        opening = ["{", "[", "("]
        closing = ["}", "]", ")"]
        match = {"}": "{", "]": "[", ")": "("}
        for index in range(len(input)):
            if (input[index] in opening):
                stack.append(input[index])

            if (input[index] in closing):
                if not stack:
                    return False
                if(match[input[index]] == stack[len(stack)-1]):
                    stack = stack[:-1]
                else:
                    return False
        if stack:
            return False
        else:
            return True
