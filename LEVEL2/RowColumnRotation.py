# 1  2  3  4  5  6
# 7  8  9  10 11 12
# 13 14 15 16 17 18
# 19 20 21 22 23 24
# 25 26 27 28 29 30
# 31 32 33 34 35 36

def solution(rows, columns, queries):
    answer =[];
    arr = [
        [ j+1 for j in range(columns*i, columns*(i+1))] for i in range(rows)
    ]
    for x1,y1,x2,y2 in queries:

        tmp = arr[x1-1][y1-1];
        min_ = tmp;

        for i in range(x1-1, x2-1):
            min_ = min(min_, arr[i+1][y1-1])
            arr[i][y1-1] = arr[i+1][y1-1]
               
        for i in range(y1-1, y2-1):
            min_ = min(min_, arr[x2-1][i+1])
            arr[x2-1][i] = arr[x2-1][i+1]
            
        for i in range(x2-1, x1-1, -1):
            min_ = min(min_, arr[i-1][y2-1])
            arr[i][y2-1] = arr[i-1][y2-1] 
            
        for i in range(y2-1, y1-1, -1):
            min_ = min(min_, arr[x1-1][i-1])
            arr[x1-1][i] = arr[x1-1][i-1]
        arr[x1-1][y1] = tmp

        answer.append(min_)
    
    print(arr);
    return answer

solution(rows=6, columns=6, queries=
    [[2,2,5,4],[3,3,6,6],[5,1,6,3]]
)

# 1  2  3  4  5  6
# 7  14 8  9  11 12
# 13 20 21 15 10 17
# 19 26 28 16 23 18
# 31 25 27 22 29 24
# 32 34 33 35 36 30
