def solution(str1, str2):
    str2 = str2.upper();
    #유사도 비교 박스
    str1Box = [];
    str2Box = [];
    
    str1BoxUnder = '';
    str2BoxUnder = '';

    unionWord = [];

    tmp = 0;
    for i,v in zip(str1, str2):
        tmp += 1;
        str1BoxUnder += i;
        str2BoxUnder += v;
        
        if tmp % 2 == 0:
            str1Box.append(str1BoxUnder);
            str2Box.append(str2BoxUnder);
            
            unionWord.append(str1BoxUnder);
            unionWord.append(str2BoxUnder);
            
            str1BoxUnder = '';
            str2BoxUnder = '';
    
    for i in range(len(str1Box)):
        if str1Box[i] == str2Box[i]:
            tmp = len(str2Box[i]);
            
    answer =  tmp / len(unionWord) * 65536;
    print(answer);
    return answer;

solution(str1="handshake", str2="shake hands");
