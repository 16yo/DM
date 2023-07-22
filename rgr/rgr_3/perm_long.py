import os
N = 6

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

def ind_cycles(a):
    p = []
    for i in range(1, N + 1):
        skip = False
        c = str(i)
        for j in p:
            if a[c] in j:
                skip=True
                break
        if skip:
            continue
        f = c
        p.append([])
        while a[c] != f:
            p[-1].append(c)
            c = a[c]
        p[-1].append(c)
    return p
        
def to_str(a):
    s = ''
    if (a == perm_one()):
        s = '\\pi_0'
    else:
        p = ind_cycles(a)
        for i in p:
            if len(i) == 1:
                continue
            s += '('
            for j in i:
                s += j
            s += ')'
    return s
    
def print_perm(a, name="", short=True):
    if not short:
        if name != "":
            print(name, ":", sep="")
        for i in range(N):
            print(i + 1, end=" ")
        print()
        for i in range(1, N + 1):
            print(a[str(i)], end=" ")
        print()
    else:
        if a == perm_one():
            print('e')
        else:
            #p = ind_cycles(a)
            # for i in p:
            #     if len(i) == 1:
            #         continue
            #     print('(', end='')
            #     for j in i:
            #         print(j, end='')
            #     print(')', end='')
            print(to_str(a))
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

def interactive(on=False, type=1):
    if on:
        if type == 1:
            while True:
                s = input()
                if s.replace(' ', '') == "clear":
                    os.system('clear')
                else:
                    print_perm(mult_expr(s))
                    print()

def permutations_string(n = N, d = list(range(1, N + 1))):
    if n == 1:
        return [str(d[0])]
    P = []
    for i in d:
        c = str(i)
        d_ = d[:]
        d_.remove(i)
        for j in permutations_string(n - 1, d_):
            P.append(c + j)
    return P

def permutations(n = N):
    P = permutations_string(n)
    p = []
    for i in P:
        m = dict({})
        for j in range(1, n + 1):
            m.update({ str(j) : i[j - 1] })
        p.append(m)
    return p

def adjacent_group(g: dict, H, side: str):
    if side == "left":
        H_ = []
        for i in H:
            H_.append(mult_perm(g, i))
        return H_
    else:
        H_ = []
        for i in H:
            H_.append(mult_perm(i, g))
        return H_

def adjacent_group(g: dict, H, side: str):
    if side == "left":
        H_ = []
        for i in H:
            H_.append(mult_perm(g, i))
        return H_
    else:
        H_ = []
        for i in H:
            H_.append(mult_perm(i, g))
        return H_

def Adjasted_group(G, H, side: str):
    AG = []
    for i in G:
        AG.append([])
        p = adjacent_group(i, H, side)
        for k in p:
            AG[-1].append(k)
    return AG

def equivalent_groups(G, H, side):
    AG = []
    was = []
    for i in G:
        if (not i in was):
            AG.append([])
            p = adjacent_group(i, H, side)
            for k in p:
                AG[-1].append(k)
                was.append(k)
    return AG


def equal_groups(A, B):
    if len(A) != len(B):
        return False
    else:
        for i in B:
            if not i in A:
                return False
    return True

def latex_interpret(G, H, side):
    AG = equivalent_groups(G, H, side)
    for i in AG:
        if side == 'left':
            print('\\item $', to_str(i[0]), ' \\cdot  H = \\{', sep='', end='')
        else:
            print('\\item $H \\cdot ', to_str(i[0]), ' = \\{', sep='', end='')

        for j in range(len(i)):
            print(to_str(i[j]), end='')
            if (j < len(i) - 1):
                print(', ', end='')
        print('\\}$')


interactive(True)

# G = permutations()

# H = [                                                                     \
#      perm_one(),            mult_expr('(14)'),     mult_expr('(23)'),       \
#      mult_expr('(12)(34)'), mult_expr('(13)(24)'), mult_expr('(14)(23)'), \
#      mult_expr('(1243)'),   mult_expr('(1342)')                            
#     ]






