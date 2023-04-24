N = 8

def make_perm(s: str):
    m = dict({})

    for i in range(1, N + 1):
        c = str(i)
        j = s.find(c)
        if j != -1:     
            if j < len(s) - 1:
                m.update({ c : s[s.find(c) + 1]})
            else:
                m.update({ c : s[0] })
        else:
            m.update({ c : c })
    return m    


def parse(s: str):
    s = s.replace('(', '')
    l = s.split(')')
    l.remove('')
    p = []
    for i in l:
        p.append(make_perm(i))
    return p

def mult_perm(a: dict, b: dict):
    r = dict({})
    for i in range(1, N + 1):
        c = str(i)
        c_ = c
        try:
            c_ = b[c]
        except:
            c_ = c
        to = c_
        try:
            to = a[to]
        except:
            to = c_
        r.update({ c : to })
    return r
    
def print_perm(a, name=""):
    if name != "":
        print(name, ":", sep="")
    for i in range(N):
        print(i + 1, end=" ")
    print()
    for i in range(1, N + 1):
        print(a[str(i)], end=" ")
    print()

def mult_expr(s):
    p = parse(s)
    r = p[-1]
    for i in range(len(p) - 2, -1, -1):
        r = mult_perm(p[i], r)
    return r

def perm_one():
    e = dict({})
    for i in range(1, N + 1):
        e.update({ str(i) : str(i) })
    return e

def reverse_perm(a):
    r = dict({})
    for i in range(1, N + 1):
        c = str(i)
        r.update({ a[c] : c })
    return r

def pow_perm(a, k: int):
    if k == -1:
        return reverse_perm(a)
    if k == 0:
        return perm_one()
    if k == 1:
        return a
    k_2 = pow_perm(a, k//2)
    k_2 = mult_perm(k_2, k_2)
    if k % 2 == 1:
        k_2 = mult_perm(k_2, a)
    return k_2


while True:
    s = input()
    print_perm(mult_expr(s))