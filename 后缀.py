expression = input("please input your test: ")
handle = []
for x in expression:
    handle.append(x)


# print(handle)


def isdigit(n):
    if n in "1234567890":
        return 1
    return 0


def fun(middle):
    dic = {'+': 1, '-': 1, '*': 2, '/': 2}
    num = []
    sign = []
    flag = -1
    for i in range(len(middle)):
        # print(sign, end = '  ')
        # print(num)
        if isdigit(middle[i]):
            num.append(middle[i])
        else:
            if middle[i] == '(':
                sign.append(middle[i])
                flag = -1

            elif middle[i] == ')':
                while sign != [] and sign[-1] != '(':
                    s = sign.pop()
                    num.append(s)
                del sign[-1]
                if sign:
                    flag = dic[sign[-1]]
                else:
                    flag = -1

            elif sign == [] or flag < dic[middle[i]]:
                flag = dic[middle[i]]
                sign.append(middle[i])

            else:
                # print("ss")

                while sign:

                    if sign != [] and sign[-1] != '(':
                        s = sign.pop()
                        num.append(s)
                    else:
                        if len(sign) > 1:
                            flag = dic[sign[-2]]
                        else:
                            flag = -1
                        break
                flag = dic[middle[i]]
                sign.append(middle[i])

    while sign != []:
        tmp = sign.pop()
        num.append(tmp)

    return num


ans = fun(handle)
for a in ans:
    print(a, end="")
print()
input("按回车退出")
