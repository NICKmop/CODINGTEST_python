def solution(numbers):
    numbers = sorted(numbers);
    compareNumber = [0,1,2,3,4,5,6,7,8,9];
    result = set(compareNumber) - set(numbers); 
    answer = 0;
    for i in result:
        answer += i;
    return answer

numbers = 0;

if  0 <= numbers <=9:
    solution(numbers=[1,2,3,4,6,7,8,0]); 
