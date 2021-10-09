# https://programmers.co.kr/learn/courses/30/lessons/67257

import itertools #순열을 손쉽게 활용하기 위한 모듈

def solution(expression):
    results = [] #계산된 값들을 담을 리스트
    numbers = [] #수식에서 숫자들을 선별하여 담을 리스트
    gihos = [] #수식에서 연산자들만 담을 리스트
    bag = '' #반복문을 통해 숫자를 추출할때 사용할 주머니용 문자열

    for i in expression: #매개변수로 받은 문자열을 한글자씩 순서대로 반복
        if i.isdecimal(): #문자가 숫자형일 경우
            bag += i #주머니에 넣음

        else: #그렇지 않을 경우(연산자)
            numbers.append(bag) #주머니에 있는 문자열을 numbers에 담음(자료형은 여전히 str)
            gihos.append(i) #현재 문자를(i) giho에 담음
            bag = '' #주머니 초기화
    numbers.append(bag) #반복문이 끝난 후 주머니에 남은 마지막 문자열도 numbers에 담음
    src_case = set(gihos) #giho 리스트의 요소들을 중복없이 집합형으로 변환

    for case in list(map(''.join, itertools.permutations(src_case, len(src_case)))): #permutations 메서드로 src_case의 요소들을 모두 선택하여 나열하는 순열 생성. 반복문 시작
        dummy_numbers = numbers.copy() #원본 변조 방지를 위해 dummy 생성
        dummy_gihos = gihos.copy() #원본 변조 방지를 위해 dummy 생성

        for target in case: #추출된 경우의 수를 기반으로 각 연산자 연산 시작 
            while True: #무한 반복
                try: #dummy_giho 에 target 연산자가 있을때 실행. 없을때 까지 무한 반복
                    idx = dummy_gihos.index(target) #dummy_giho에서 가장 앞에있는 target(연산자)의 인덱스
                    dummy_numbers[idx] = str(eval(dummy_numbers[idx]+dummy_gihos.pop(idx)+dummy_numbers.pop(idx+1))) #eval 함수로 '피연산수1'+'연산자'+'피연산수2'을 수행하여 피연산수1 인덱스에 대입. 대입과정에서 연산자와 피연산수2 는 소속된 리스트에서 자동 삭제
                except: #dummy_giho 에 target 연산자가 없으면 while문 종료
                    break

        results.append(abs(int(dummy_numbers[0]))) #dummy_giho는 모든 요소가 pop되어 사라지고 dummy_numbers에는 연산된 값이 문자형으로 들어있음. 정수로 변환 후 절대값을 취해서 results에 담음

    return max(results) #results에 담긴 정수 중 가장 큰 값 반환

print(solution("100-200*300-500+20")) #60420
print(solution("50*6-3*2")) #300