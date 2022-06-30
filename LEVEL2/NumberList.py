def solution(phone_book):
    checkDt = 0;
    for i in range(len(phone_book)):
        if phone_book[i] not in phone_book[i-1]:
            print('not in ');
        else:
            checkDt += 1;
    if checkDt == 1:
        answer = True;
    else:
        answer = False;
    
    return answer;

solution(phone_book=["119", "97674223", "1195524421"]);
# solution(phone_book=["123","456","789"]);
# ["119", "97674223", "1195524421"]	false
# ["123","456","789"]	true
# ["12","123","1235","567","88"]	false