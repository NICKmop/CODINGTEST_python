class dictObj(object):

    def __init__(self,name):
        self.name = name;
    def __str__(self):
        return self.name;
    def __repr__(self):
        return '숫자는 : {} '.format(self.name);

    def solution(priorities, location):
        cnt = 96;
        dict = {};
        
        for i in range(len(priorities)):
            cnt += 1;
            asciiNumber = chr(cnt);
            asciiNumberC = asciiNumber.upper();
            
            intTostr = str(priorities[i]);
            dict[dictObj(intTostr)] = asciiNumberC;

        tmp = [];
        for k,v in dict.items():
            k = str(k);
            ktoint = int(k);
            tmp.append(ktoint);
        
        comparetmp = 0;
        cnt = 0;
        for i in range(len(tmp)):
            comparetmp = tmp[0];
            if tmp[i] > comparetmp:
                print("tmp :  ", tmp[i]);
            else:
                cnt += 1;
                if i == location:
                    cnt -= 1;
                print("cnt  : ", cnt + 1 );
        answer = 0
        return answer



# dictObj.solution(priorities=[1, 1, 9, 1, 1, 1]	, location=0)
dictObj.solution(priorities=[2, 1, 3, 2], location=2)