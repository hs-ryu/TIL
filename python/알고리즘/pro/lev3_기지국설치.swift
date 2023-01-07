import Foundation

func solution(_ n:Int, _ stations:[Int], _ w:Int) -> Int{
    var answer = 0
    var points = [Int]()
    var flag = 0

    // 기지국을 기준으로, 왼쪽에 빈 곳이 몇개인지, 계속 체크해 나간다.
    for station in stations {
        var start = max(station-w,1)
        var end = min(station+w,n)
        
        if flag == 0 {
            points.append(start-1)
            flag = end
        } else {
            if flag + 1 < start {
                points.append(start-flag-1)
            }
            flag = end
        }
    }
    // 왼쪽만 계속 체크했기 때문에 하나 남는다. 맨 마지막꺼에서 오른쪽 기준에 몇개 있는지 넣어줘야한다.
    // 0이라도 상관없음!
    points.append(n-flag)

    // 범위로 나눠서 몇개 설치해야할지 구한다.
    let distance = w * 2 + 1
    for p in points {
        answer += p / distance
        if p % distance != 0 {
            answer += 1
        }
    }
    
    return answer
}