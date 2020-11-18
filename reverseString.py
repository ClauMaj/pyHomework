
def reverse(s): 
    str = "" 
    for i in s: 
        str = i + str
    return str
print(reverse('madlib'))

def revstr(a):
    if len(a) == 0:
        return a
    return revstr(a[1:]) + a[0]
result = revstr("python")
print(result)