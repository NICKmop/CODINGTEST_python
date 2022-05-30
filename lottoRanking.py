def solution(lottos, win_nums):
    answer = [];
    # uncollect Item
    lottosList = [];
    win_numsList = [];

    for i in lottos:
        if i not in win_nums:
            lottosList.append(i);
        else:
            answer.append(i);

    for i in win_nums:
        if i not in lottos:
            win_numsList.append(i);

    # [44, 1, 0, 0, 31, 25]
    collect_lottosList = len(lottosList);
    for i in range(collect_lottosList):
        answer.append(lottosList[i]);
    return answer

solution(lottos = [44, 1, 0, 0, 31, 25], win_nums = [31, 10, 45, 1, 6, 19])