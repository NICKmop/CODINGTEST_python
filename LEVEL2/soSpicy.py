# 섞은음식의스코빌지수= 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)
# 스코빌 지수 k 이상 인 것들
# scoville 매운 정도.

from os import remove


def solution(scoville, k):
    answer = 0
    scoville = sorted(scoville);

    # for i in range(scovilleLen):
    while True:
        if scoville[0] >= 7:
            break;
        else:
            # while True:
            scoville[0] = scoville[0] + (scoville[1] * 2); # 5
            scoville.pop(1);
            scoville = sorted(scoville);

            answer += 1;
    
    return answer

solution(scoville=[1, 2, 3, 9, 10, 12], k=7);