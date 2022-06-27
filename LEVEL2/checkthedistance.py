def solution(places):
    array = [[0 for col in range(5)] for row in range(5)]
    for i in range(len(places)):
        # print("class number {} : {}".format(i, places[i]));
        for j in range(len(places[i])):
            # print("j number : {} - {}".format(j, places[i][j]));
            print("")
            for k in range(len(places[j])):
                word = places[j][k];
                if "P" not in word:
                    print("word Number : {} - {}".format(k,word));
                else:
                    print(word);
                for g in word.join(''):
                    print("gggggg : ", word);
                    
    answer = []
    return answer

places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
# [1, 0, 1, 1, 1] - result
# places 원소의 길이(대기실 가로 길이) = 5
# P는 응시자가 앉아있는 자리를 의미합니다.
# O는 빈 테이블을 의미합니다.
# X는 파티션을 의미합니다.
solution(places);