
def isPalindrome(x):
    if x < 0:
        return False
    elif x == 0:
        return True
    else:
        reverse = 0
        temp = x
        while temp > 0:
            reverse = (reverse * 10) + (temp % 10)
            temp = temp // 10
        return reverse == x
