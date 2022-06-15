def func(w,h):
    a,b = max([w,h]),min([w,h])
    while(True):
        r= a%b
        print(r);
        if r == 0:
            print("b : ", b);
            return b
        a = b
        b = r
        

def solution(w,h):
    squares = w*h
    gcd = func(w,h)

    return squares-(w+h-gcd)

print(solution(w=9, h=12));

# 최소 공배수 / 최소 공약수 구하기
