# https://programmers.co.kr/learn/courses/30/lessons/60057

def tool(n,string):
    if n == 1:
        return string
    else:
        return str(n)+string

def solution(s):
    length = len(s)
    results = []
    for i in range(1,int(len(s)/2 + 1)):
        temp = [s[j*i:(j+1)*i] for j in range(length//i)]
        result = ''
        temp_num = 1
        temp_str = temp[0]

        for j in range(1,len(temp)):
            if temp[j] == temp_str:
                temp_num += 1
            else:
                result += tool(temp_num,temp_str)
                temp_num = 1
                temp_str = temp[j]
                
        result += tool(temp_num,temp_str)
        
        if length % i != 0:
            result += s[i*(length//i):]

        results.append(result)

    if not results:
        results.append(s)

    return (min([len(i) for i in results]))



lst = ["aabbaccc", "ababcdcdababcdcd", "abcabcdede", "abcabcabcabcdededededede", "xababcdcdababcdcd","aaaaaaaaaaaaaaaaaaa",'a']
for i in lst:
    print(solution(i))

