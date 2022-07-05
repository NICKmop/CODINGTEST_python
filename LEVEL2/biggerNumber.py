def solution(numbers):
    extend = [];
    # 6102 6210 1062 1026 2610 2106
    tmp = len(numbers);

    for i in range(len(numbers)): # 6102
        strNum = str(numbers[i]);
        extend.extend(strNum);
        print("strNum : ", strNum);
        if i == tmp:
            tmp -= 1;
            print("tmp : " , tmp);
            print("if strNum : ", strNum);
        # for j in range(-1, len(numbers)-1): # 2610
        #     print(numbers[j])
        # for k in strNum:
        #     print("k : ", k);

    # for i in range(-1, len(numbers)-1): # 2610
    #     print(numbers[i])
    
    # for i in range(1, len(numbers)):
    #     print(i)

    answer = ''
    return answer

solution(numbers=[6,10,2]);

# [6, 10, 2]	"6210"
# [3, 30, 34, 5, 9]	"9534330"