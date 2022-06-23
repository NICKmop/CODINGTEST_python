from re import L


def solution(p):
    wordBox = [];

    for i in p:
        wordBox.append(i);
        if i == "(":
            print("1");
        elif i == ")":
            print("2")
    print(wordBox);
    answer = ''
    return answer


solution(p="()))((()");
# () () () ()