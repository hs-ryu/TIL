import Foundation

// BFS로 풀이. 굳.
func solution(_ n:Int, _ computers:[[Int]]) -> Int {
    var visited = [Int](repeating:0, count:n)
    func search(_ s: Int, _ check: Int) {
        var q = [Int]()
        for i in 0..<n {
            if computers[s][i] == 1 {
                q.append(i)
            }
        }
        
        while !q.isEmpty {
            var temp = q.removeFirst()
            if visited[temp] == 0 {
                visited[temp] = check
                for i in 0..<n {
                    if computers[temp][i] == 1 && visited[i] == 0{ 
                        q.append(i)
                    }
                }
            }
            
        }
        
    }
    
    var check = 1
    for i in 0..<n {
        if visited[i] == 0 {
            search(i,check)
            check += 1
        }
    }
    var result = Set(visited).count
    
    return result
}



// 다른사람의 풀이
// 재귀 활용

import Foundation

func solution(_ n:Int, _ computers:[[Int]]) -> Int {
    var visited = Array<Bool>(repeating: false, count: n)
    var group = 0

    func dfs(_ vertex: Int) {
        visited[vertex] = true
        for i in 0..<n {
            if computers[vertex][i] == 1 && !visited[i] {
                dfs(i)
            }
        }
    }

    for i in 0..<n {
        if !visited[i] {
            group += 1
            dfs(i)
        }
    }

    return group
}