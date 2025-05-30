s = input()
t = input()

def anagram(s, t):
    if len(s) == len(t):
        f = {}

        for l in s:
            if l in f:
                f[l] += 1
            else:
                f[l] = 1

        for l in t:
            if l not in f or f[l] == 0:
                print(False)
                return
            f[l] -= 1

        print(True)

anagram(s, t)

# scount = 

# if list(t) in list(s):
    
#     print(True)
# else:
#     print(False)

# if len(s) == len(t):
#     f = {}

#     for l in s:
#         if l in f:
#             f[l] += 1
#         else:
#             f[l] = 1

#     for l in t:
#         if l not in f or f[l] == 0:
#             print(False)
#             break
#         f[l] -= 1

#     print(True)