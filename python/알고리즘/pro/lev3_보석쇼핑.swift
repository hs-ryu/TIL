import Foundation



// 핵심 개념 : 입력이 10만이라서 2중 반복문은 안된다. 
// 시작점, 끝점을 정해서 딕셔너리에 값을 집어넣어주고, 그 딕셔너리의 길이(현재 가지고 있는 보석 종류)를 체크해서, 다 포함되었는지 확인.
// 근데, 다 가지고 있다고 해서 끝나는게 아니라, 길이 체크가 필요하니까 시작점을 땡겨가면서 계속 확인.
func solution(_ gems:[String]) -> [Int] {
    var totalGems = [String:Int]()
    
    var startPoint = 0
    var endPoint = 0
    
    var totalGemsCnt = Set(gems).count
    var resultList = [[Int]]()
    
    while startPoint < gems.count {
        var setGemsCnt = totalGems.count
        if setGemsCnt == totalGemsCnt {
            resultList.append([startPoint+1, endPoint])
            totalGems[gems[startPoint]]! -= 1
            if totalGems[gems[startPoint]] == 0 {
                totalGems.removeValue(forKey: gems[startPoint])
            }
            startPoint += 1
        } 
        // 끝 점이 배열 끝에 도달했을때,
        // 근데 시작점을 더 땡겨서 확인해볼 수 있으니까 조건 설정 필요함.
        // 얘 처리 안해주니 케이스 2개에 대해 통과 못함. 굳!!!!
        if endPoint == gems.count {
            if setGemsCnt == totalGemsCnt {
                continue
            } else {
                break
            }
        }
        
        if setGemsCnt != totalGemsCnt {
            if let x = totalGems[gems[endPoint]] {
                totalGems[gems[endPoint]]! += 1
            } else {
                totalGems[gems[endPoint]] = 1
            }
            endPoint += 1
        }
    }
    resultList.sort(by: {$0[1]-$0[0] < $1[1]-$1[0]})
    
    return resultList[0]
}