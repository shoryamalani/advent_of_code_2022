
from sys import argv
filename = "input-5.txt"
if len(argv) > 1:
    filename = "input-12.txt"

def string_to_list(string):

    return eval(string)
    a = string
    temp = []
    i = 0
    if a== '[]':
        return []
    if a[0][0] == '[' and a[-1][-1] == ']' and all(x[0] != '[' for x in a[1:]) and all(x[-1] != ']' for x in a[:len(a)-1]):
        a[0] = a[0][1:]
        a[-1] = a[-1][:-1]
        
    if a == ['']:
        return []
    while i < len(a):
        if a[i][0] == '[':
            if a[i][-1] == ']':
                if '[' in a[i][1:-1] or ']' in a[i][1:-1]:
                    temp.append([string_to_list(a[i][1:-1])])
                    i += 1
                    continue
                elif '' == a[i][1:-1]:
                    temp.append([])
                    i += 1
                    continue
                else:
                    temp.append([int(a[i][1:-1])])
                    i += 1
                    continue
            orig = i
            end = len(a) -1
            while end > orig:
                if a[end][-1] == ']':
                    break
                end -= 1
            temp.append(string_to_list(a[orig:end+1]))
            i = end
        else:
            temp.append(int(a[i]))
        i += 1
    return temp
            
                
            

# def compare(a,b):
#     if a == []:
#         return True if b == [] else False
#     if b == []:
#         return True
#     if isinstance(a, int) and isinstance(b, int):
#         return True if a <= b else False
#     if isinstance(a, int) and isinstance(b, list):
#         a = [a]
#         return compare(a, b)
#     if isinstance(b, int) and isinstance(a, list):
#         b = [b]
#         return compare(a, b)
#     if isinstance(a, list) and isinstance(b, list):
#         if compare(a[0], b[0]):
#             return compare(a[1:], b[1:])
#         else:
#             return False
#     return False if a < b else True if b < a else False

# def compare(a, b):
#     if type(a) == type(b) == int:
#         return a - b
#     if type(a) == int and type(b) == list:
#         a = [a]
#         return compare(a, b)
#     if type(b) == int and type(a) == list:
#         b = [b]
#         return compare(a, b)
    
#     for l,r in zip(a,b):
#         res = compare(l,r)
#         if res <= 0:
#             continue
#         return res
#     return res
def compare(left, right):
    if isinstance(left, int) and isinstance(right, int):
        if left < right: return -1
        if left > right: return +1
        return 0
    else:
        left = list([left]) if isinstance(left, int) else left
        right = list([right]) if isinstance(right, int) else right
        
        if len(left) == 0 and len(right) != 0: return -1 
        if len(right) == 0 and len(left) != 0: return +1
        if len(left) == 0 and len(right) == 0: return 0
        
        if (ret := compare(left[0], right[0])) != 0:
            return ret
        else:
            return compare(left[1:], right[1:])
        

# def compare(a, b):
#     #convert from string to list
#     # a[0] = a[0][1:]
#     # a[-1] = a[-1][:-1]
#     # b[0] = b[0][1:]
#     # b[-1] = b[-1][:-1]
#     if type(a) == str:

#         a = string_to_list(a)
#         b = string_to_list(b)
#     if type(a) == int and type(b) == list:
#         a = [a]
#     if type(b) == int and type(a) == list:
#         b = [b]
    
#     i = 0
#     while i < len(a):
#         if i >= len(b):
#             return False
        
#         if a == [] or b == []:
#             if a == [] and b != []:
#                 return True
#             if b == [] and a != []:
#                 return False
#         if type(a[i]) == int and type(b[i]) == int:
#             if a[i] > b[i]:
#                 return False
#         elif type(a[i]) == list and type(b[i]) == list or type(a[i]) == list and type(b[i]) == int or type(a[i]) == int and type(b[i]) == list:
#             if type(a[i]) == int:
#                 a[i] = [a[i]]
#             if type(b[i]) == int:
#                 b[i] = [b[i]]
#             if compare(a[i], b[i]):
#                 i+=1
#                 continue
#             else:
#                 return False
#             if type(a[i]) == int:
#                 a[i] = [a[i]]
#             if type(b[i]) == int:
#                 b[i] = [b[i]]
#             j = 0
#             while j < len(a[i]):
#                 if len(b[i]) == 0:
#                     return False
#                 if b[i][j] == []:
#                     return False
#                 return compare(a[i][j], b[i][j])
#                 if a[i][j] >= b[i][j]:
#                     j += 1
#                 else:
#                     return False
#             return True
#         i += 1
#     return True

with open(filename, "r") as f:
    data = f.read()
    data = data.replace("\n\n", "\n")
    # data = [x.split('\n') for x in data]
    data = data.split("\n")
    print(data)
    i =0
    val = 0
    finals = [[] for x in range(len(data))]
    in_order = 0
    while in_order < len(data) -1:
        in_order = 0
        i =0 
        while i < len(data) -1:

            # if compare(string_to_list(data[i][0]),string_to_list(data[i][1])) <= 0:
            #     val += i +1
            #     print(i +1 )
            if compare(string_to_list(data[i]),string_to_list(data[i+1])) == 0:
                in_order += 1
                finals[i] = data[i]
            elif compare(string_to_list(data[i]),string_to_list(data[i+1])) < 0:
                
                temp = data[i+1]
                data[i+1] = data[i]
                data[i] = temp
            elif compare(string_to_list(data[i]),string_to_list(data[i+1])) > 0:
                
                in_order += 1
                finals[i] = data[i]



            i += 1
    print(val)
    finals.reverse()
    print(finals.index('[[2]]'))
    print(finals.index('[[6]]'))
    