def palindrome(n):
    if len(n) == 0:
        return True
    elif len(n) == 1:
        return True
    else:
        if n[0] == n[-1]:
            return palindrome(n[1:len(n)-1])
        else:
            return False

print(palindrome("saippuakivikaupwpias"))