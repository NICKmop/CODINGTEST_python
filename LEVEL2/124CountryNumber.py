# 10진법 124나라 10진법 124나라
#   1	    1	    6	 14
#   2	    2	    7	 21
#   3	    4	    8	 22
#   4	    11	    9	 24
#   5	    12	    10	 41
def solution(n):
    nara = [1,2,4];
    answer = '';
    
    while True:
        if n <= 0:
            return answer;
        n -= 1;
        print("n -= 1 : ", nara[n%3]);
        answer = str(nara[n%3]) + answer;
        n //= 3;
        print("n //= 3 : ", n);

print(4//3)
print(solution(n = 4));