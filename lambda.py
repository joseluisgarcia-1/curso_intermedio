#esta función sirve
"""string = str(input("palabra : "))
def palindrome(string):
    return string == string[::-1]
print(palindrome(string))

if __name__ == '__main__':
    palindrome(string)"""
#funcion lambda, también sirve
string = str(input("palabra : "))
palindrome = lambda string: string == string[::-1]
print(palindrome(string))
