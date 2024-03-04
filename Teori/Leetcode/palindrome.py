def isPalindrome(x):
        y = len(str(x))
        if y == 1 :
            return True
        for i in range(y//2):
            if str(x)[i] != str(x)[-i-1] :
                return False
        return True