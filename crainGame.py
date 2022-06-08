def solution(board, moves):
    answer = 0
    tmp = []
    for i, v in enumerate(moves):
        print("i: ", i, "v:", v)  # i=index, v=value
        for j in range(len(board)):
            if board[j][v-1] != 0:
                tmp.append(board[j][v-1])
                board[j][v-1] = 0
                break
            while True:
                if len(tmp) > 1:
                    if tmp[-1] == tmp[-2]:
                        answer += 2
                        del tmp[-1]
                        del tmp[-1]
                    else:
                        break
                else:
                    break
    return answer

solution(board=[[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], moves=[1,5,3,5,1,2,1,4]);