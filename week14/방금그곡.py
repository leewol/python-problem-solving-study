def solution(m, musicinfos):
    answer = "(None)"
    playtime = 0
    music_dic = {}

    for music in musicinfos:
        music_list = music.split(",")
        title = music_list[2]
        codes = music_list[3].replace("C#", "c").replace("D#", "d").replace("F#", "f").replace("G#", "g").replace("A#", "a")

        # 재생 시간 계산
        start_h, start_m = map(int, music_list[0].split(":"))
        end_h, end_m = map(int, music_list[1].split(":"))
        music_time = (end_h - start_h) * 60 + (end_m - start_m)

        # 재생된 멜로디 계산
        quo, rem = divmod(music_time, len(codes))
        played_code = codes * quo + codes[:rem]

        # 음악 딕셔너리에 저장
        music_dic[played_code] = [title, music_time]

    m = m.replace("C#", "c").replace("D#", "d").replace("F#", "f").replace("G#", "g").replace("A#", "a")

    # 일치하는 노래 확인
    for key, value in music_dic.items():
        if m in key:
            if value[1] > playtime:
                answer = value[0]
                playtime = value[1]

    return answer