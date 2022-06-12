def solution(a, b):
    answer = 0;
    for i in range(len(a)):
        res = a[i] * b[i]
        answer += res;
    print(answer); 
    return answer

solution(a=[-1,0,1],b=[1,0,-1]);