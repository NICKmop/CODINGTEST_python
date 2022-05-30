id_list = ["muzi", "frodo", "apeach", "neo"];
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"];
k = 2;

def logMsg(param1, param2):
    return print('"{}" 가 "{}" 를 신고 했습니다.'.format(param1, param2));
    
def solution(id_list, report, k):
    m,f,a,n = 0,0,0,0;
    answer = []
    for i in report:
        report_attacker = i.split(' ');
        if report_attacker[1] == 'muzi':
            m += 1;
            # if k == m:
            logMsg(report_attacker[0], report_attacker[1])
        elif report_attacker[1] == 'frodo':
            f += 1;
            # if k == f:
            logMsg(report_attacker[0], report_attacker[1])
        elif report_attacker[1] == 'apeach':
            a += 1;
            # if k == a:
            logMsg(report_attacker[0], report_attacker[1])
        else:
            n += 1;
            # if k == n:
            logMsg(report_attacker[0], report_attacker[1])
    answer.append(m);
    answer.append(f);
    answer.append(a);
    answer.append(n);
    return answer

solution(id_list, report, k);
