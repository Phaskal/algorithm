def solution(testers, major, minor):
    answer = 0
    for tester in testers:
        temp = tester - major
        answer += 1
        
        if temp <=0:
            continue
        
        else:
            answer += temp // minor 
            if temp % minor != 0:
                answer += 1

    return answer

if __name__ == "__main__":
    n = input()
    testers = list(map(int, input().split()))    
    major, minor = map(int, input().split())
    print(solution(testers, major, minor))