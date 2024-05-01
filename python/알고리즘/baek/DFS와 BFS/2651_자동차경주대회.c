#include <stdio.h>
#include <math.h>

int L; //정비를 받지 않고 갈수있는 최대거리
int N; //정비소 개수
int dist[100+10]; //정비소사이거리
int time[100+10]; //정비시간

int queue[100 * 100 * 100 + 10];
int wp;
int rp;


void push(int n) {
    queue[wp] = n;
    wp++;
}

void pop(void) {
    rp++;
}

int front(void) {
    return queue[rp];
}

int isEmpty(void) {
    return wp == rp;
}

// 시간으로 관리하고
long long int timeCheck[100+10];
// 효율이 좋을떄만 visited에 방문처리 (목적지에 출발지를 저장)
// 출력할 때 돌아가면서 하나씩 출력할거임.
int visited[100+10];


void BFS() {
    for (int i = 1; i <= N+1; i++) {
        timeCheck[i] = pow(2, 31);
        // printf("%lld ", timeCheck[i]);
    }
    
    push(0);
    
    while (!isEmpty()) {
        int now = front();
        pop();
        
        for (int target = now+1; target <= N+1; target++) {
            // 정비 안받으면 못가는 거리일 경우 버려
            if (dist[target]-dist[now] > L) {
                break;
            }
            // 정비를 받는게 이득인지 한번 보자
            if (timeCheck[target] > timeCheck[now] + time[target]) {
                // 정비 받는게 이득
                timeCheck[target] = timeCheck[now] + time[target];
                visited[target] = now;
                push(target);
            }
        }
    }
    // for (int i = 0; i <= N+1; i++) {
    //     printf("%d ", visited[i]);
    // }
}


void InputData(void){
    scanf("%d", &L);
    scanf("%d", &N);
    for (int i=1; i<=N+1; i++){
        scanf("%d", &dist[i]);
        dist[i] = dist[i-1] + dist[i];
        // printf("%d ", dist[i]);
    }
    for (int i=1; i<=N; i++){
        scanf("%d", &time[i]);
    }
    time[N+1] = 0;
}


void pri(int k, int cnt, int total) {
    if (visited[k] == 0) {
        printf("%d\n", total);
        printf("%d\n", cnt);
        return;
    }
    
    pri(visited[k], cnt + 1, total + time[visited[k]]);
    printf("%d ", visited[k]);
}


int main(void){
    InputData();

    // dist[1] -> 1번과 2번 정비소 사이의 거리
    
    // 만약 정비 시간이 0이라면 -> 출력 안해도 됨.
    
    // 현재 갈 수 있는 범위의 친구들을 찾는다.
    // 갈 수 있는 범위들의 친구들로 
    
    // 출발 : 0, 도착 : N+1
    
    // 정비 안받고도 목적지 도착할 수 있는 방법
    if (dist[N+1] <= L) {
        printf("0\n");
        printf("0");
    } else {
        BFS();
        pri(N+1, 0, 0);
    }
    

    return 0;
}