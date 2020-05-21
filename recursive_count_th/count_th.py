'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    #base case if the length is less than 2 it can't contain th 
    if len(word) < 2:
        return 0
    #find if the first two letters are 'th
    elif word[:2] == 'th':
        # recursion to continue finding th, + 1 to return
        return count_th(word[2:]) + 1
    #if the first two letters are not 'th', move to the next letter and check
    else:
        return count_th(word[1:])
    
    
    
