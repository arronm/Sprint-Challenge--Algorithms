'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurrences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    # for each letter, check if it is t
    # if it is t, check n + 1 to see if it is h
    # if so increment th_counter and increment our counter to skip h

    # for i in range(len(word) -1):
    #   if word[i] == 't':
    #     if (i + 1) > len(word):
    #       break
    #     if word[i+1] == 'h':
    #       th_counter += 1
    #       i += 1

  if len(word) <= 2:
    if word == 'th':
      return 1
    return 0

  if word[0] == 't':
    if word[1] == 'h':
      return 1 + count_th(word[2:])  # possible out of range
    
  return count_th(word[1:])
