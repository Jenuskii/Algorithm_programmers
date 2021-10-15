# https://programmers.co.kr/learn/courses/30/lessons/42888

def solution(record):
    answer = []
    split = [i.split() for i in record]
    id_nick = dict()
    for i in split:
        if i[0] != "Leave":
            key,value = i[1:]
            id_nick[key]=value
    verbs = {"Enter": "들어왔습니다.", "Leave": "나갔습니다."}
    for msg in split:
        try:
            subject = id_nick[msg[1]]
            verb = verbs[msg[0]]
            answer.append("님이 ".join([subject,verb]))
        except:
            continue
    return answer


example = [
        "Enter uid1234 Muzi", 
        "Enter uid4567 Prodo",
        "Leave uid1234",
        "Enter uid1234 Prodo",
        "Change uid4567 Ryan"
        ]

print(solution(example))