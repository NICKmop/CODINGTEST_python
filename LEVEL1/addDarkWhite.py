def solution(absolutes, signs):
    result = [];
    for i in range(len(absolutes)):
        if signs[i] == True:
            result.append(abs(absolutes[i]));
        else:
            if absolutes[i] < 0 :
                result.append(absolutes[i]);
            else :
                result.append(absolutes[i] * -1)

solution(absolutes = [-4,-7,-12] , signs = [True, False, False]);