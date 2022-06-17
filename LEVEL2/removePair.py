def solution(s):

    tmp = [];
    leng = len(s);
    for i in range(leng):
        tmp.append(s[i]);
    
    cnt = 0;
    answer = 0
    while True:
        if tmp[cnt] == tmp[cnt + 1]:
            answer += 1;
            print("if : ", tmp[cnt], tmp[cnt+1]);
            
            del(tmp[cnt]);
            print("tmp1 : ", tmp , cnt);
            del(tmp[cnt]);
            print("tmp2 : ", tmp , cnt);

            if len(tmp) == 0:
                print("값이 없음");
                break;
        else:
            print("else");
            cnt += 1;
            

    print(answer);            
    return answer

# 삭제 시 다시 0부터 돌리고 삭제


solution(s= "baabaa");