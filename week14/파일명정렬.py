def solution(files):
    files_list = []
    answer = []
    
    # 각 file 이름 head/number/tail로 나누기
    for file in files:
        file_list = []
        head = ""
        number = ""
        for idx, char in enumerate(file):
            if char.isdigit():
                if head not in file_list:
                    file_list.append(head)
                number += char
                
                if idx == len(file) - 1:
                    tail = ""
                    file_list.append(number)
                    file_list.append(tail)
                    break

                elif not file[idx + 1].isdigit():
                    tail = file[idx + 1:]
                    
                    file_list.append(number)
                    file_list.append(tail)
                    break
            else:
                head += char
                    
        files_list.append(file_list)
    
    # 기준에 따라 정렬
    files_list.sort(key=lambda name: (name[0].lower(), int(name[1])))
    
    # 다시 문자열로 만들기
    for file in files_list:
        answer.append("".join(file))

    return answer