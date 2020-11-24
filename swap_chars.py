def repl_two_strings(first, last):
    new_first = first[:2] + last[-1]
    new_last = last[:2] + first[-1]
    return new_last + ' ' + new_first


print(repl_two_strings("abc", "xyz"))


# here is a solution from w3source
# just put it here, looks much logical than mine

def chars_mix_up(a, b):  
  new_a = b[:2] + a[2:]  
  new_b = a[:2] + b[2:]  
  
  return new_a + ' ' + new_b  
print(chars_mix_up('abc', 'xyz'))  
