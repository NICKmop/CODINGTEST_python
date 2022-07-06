def solution(numbers):
    answer = ''
    strnum = list(map(str, numbers));

    # '//' 이 연산자는 몫을 반환하는 연산자
    same_length = [[i, i * (12//len(i)) ] for i in strnum]

    ch = same_length.sort(key=lambda x:x[1], reverse=True)

    for i in same_length:
        answer += i[0]

    test ='';
    for k in ['1','5','2','3','4']:
        print("k : " , k)
        test += k[0];

    answer = str(int(answer))
    print(answer);


    return answer
# solution(numbers=[6,10,2]);
solution(numbers=[3,30,34,5,9]);
