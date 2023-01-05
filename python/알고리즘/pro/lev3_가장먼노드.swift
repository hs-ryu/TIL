import Foundation

func solution(_ n:Int, _ edge:[[Int]]) -> Int {
    // BFS 돌리면서 확인하기.
    // 다음 노드 뿐만 아니라 거리에 대한 정보도 함께 넣어 확인해준다.
    // visited에 값이 있더라도, 최소값이 아닐 경우도 있기 때문에 체크해 줘야한다.
    func BFS(_ start: Int) {
        var q = [[Int]]()
        for num in AL[start] {
            q.append([num, 1])
            visited[num] = 1
        }
        
        while !q.isEmpty {
            var temp = q.removeFirst()
            var node = temp[0]
            var length = temp[1] + 1
            
            for next in AL[node] {
                if visited[next] == 0 {
                    q.append([next, length])
                    visited[next] = length
                    if maxLength < length {
                        maxLength = length
                    }
                } else {
                    if visited[next] > length {
                        visited[next] = length
                        if maxLength < length {
                            maxLength = length
                        }
                    }
                }
            }
            
        }
    }
    
    var AL = [[Int]](repeating:[], count:n+1)
    for i in 0..<edge.count {
        var s = edge[i][0]
        var e = edge[i][1]
        AL[s].append(e)
        AL[e].append(s)
    }
    var maxLength = 1
    var visited = [Int](repeating: 0, count: n+1)
    visited[1] = 1
    BFS(1)
    let result = visited.filter { $0 == maxLength }.count
    
    return result
}