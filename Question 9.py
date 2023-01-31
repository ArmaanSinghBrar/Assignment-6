class ParenthesisChecker:
    def __init__(self, s):
        self.s = s
        
    def is_valid(self):
        stack = []
        mapping = {")": "(", "}": "{", "]": "["}
        for char in self.s:
            if char in mapping:
                if not stack or stack.pop() != mapping[char]:
                    return False
            else:
                stack.append(char)
        return not stack
