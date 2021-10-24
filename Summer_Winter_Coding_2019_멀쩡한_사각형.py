# def solution(w,h):
#     diff = h / w
#     if diff != int(diff):
#         diff = int(diff) + 1

#     return w * (h - diff)

# print(solution(8,12))

#실패 케이스 등장


#부동 소수의 오차 발생
# def solution(w,h):
#     cut = []
#     diff = h / w
#     val = [diff * i for i in range(w+1)]
    
#     back = val.pop()
#     while val:
#         front = val.pop()
#         a = front
#         b = back
#         if a != int(a):
#             a = int(a)
#         if b != int(b):
#             b = int(b) + 1
#         cut.append(b-a)
#         back = front
    
#     return w*h - sum(cut)

#분수식을 포현해봐서 극복해볼까? -> scaling으로 분자만 다뤄보자
# def solution(w,h):
#     cut = []
#     diff_mul_w = h
#     val = [diff_mul_w * i for i in range(w+1)]

#     back = val.pop()
#     while val:
#         front = val.pop()
#         a = front
#         b = back
#         if a % w != 0:
#             a -= (a % w)
#         if b % w != 0:
#             b += w - (b % w)
#         cut.append((b-a) // w)
#         back = front
    
#     return w*h - sum(cut)
# 결과는 잘 나오나 11, 12, 14 케이스 시간초과

# 예외 처리로 극복
def solution(w,h):
    if w == 1 or h == 1:
        return 0

    elif w == h:
        return w*h - w
    else:
        cut = []
        diff_mul_w = h
        val = [diff_mul_w * i for i in range(w+1)]

        back = val.pop()
        while val:
            front = val.pop()
            a = front
            b = back
            if a % w != 0:
                a -= (a % w)
            if b % w != 0:
                b += w - (b % w)
            cut.append((b-a) // w)
            back = front
        
        return w*h - sum(cut)




