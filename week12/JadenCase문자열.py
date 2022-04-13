def solution(s):
    s_list = s.split(" ")

    for idx, el in enumerate(s_list):
        if el != "":
            s_list[idx] = el[0].upper() + el[1:].lower()
    
    return " ".join(s_list)