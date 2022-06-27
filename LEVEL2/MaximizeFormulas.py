def solution(expression):
    answer = 0;
    if "+" not in expression:
        spex = expression.split('*');
        for i in spex:
            if '-' in i:
                answer *= eval(i);
            else:
                answer *= int(i);
    else:
        # *> +> -
        spex = expression.split('-');
        for i in spex:
            i = eval(i);
            answer -= i;
        print(abs(answer));
            

        #     answer = i;
        # print(type(answer));
    # spex = expression.split('-');
    # print(spex);

    return answer;

solution(expression="100-200*300-500+20")
# solution(expression="50*6-3*2")
# expression	result
# "100-200*300-500+20"	60420
# "50*6-3*2"	300