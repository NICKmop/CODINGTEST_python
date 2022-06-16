from warnings import catch_warnings


def solution(progresses, speeds):
    standard = 100;
    funcDay = [];
    cnt = 0; 
    tnt = 0;
    extmp = 0;
    
    for i in range(len(progresses)):
        if progresses[i] == standard:
            break;
        else:
            while True:
                if progresses[tnt] <= 100:
                    progresses[tnt] += speeds[cnt];
                    if tnt <= len(progresses):
                        extmp += 1;
                else: 
                    funcDay.append(extmp - 1);
                    extmp = 0;
                    cnt += 1;
                    tnt += 1;
                    break;
    extmp = 1;
    answer = []
    for j in range(0,len(funcDay)):
        if j+1 >= len(funcDay):
            extmp = 1;
            answer.append(extmp);
            break;
        else:
            if funcDay[j] > funcDay[j+1]:
                extmp += 1;
                answer.append(extmp);
            else:
                extmp = 1;
                answer.append(extmp);
    print(answer);
    return answer;


solution(progresses=[95, 90, 99, 99, 80, 99], speeds=[1, 1, 1, 1, 1, 1]);