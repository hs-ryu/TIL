#include <stdio.h>
#include <string.h>

#define MAXN ((int)1e4)
int M, T, N;
int AT[MAXN + 10];
char SIDE[MAXN + 10][10];
 
int arrived[MAXN + 10];

// 왼쪽, 오른쪽에 손님을 배치하기 위해 큐를 2차원으로 구현
int queue[2][MAXN + 10];
int wp[2], rp[2];

void push(int side, int d) {
    queue[side][wp[side]++] = d;
}

void pop(int side) {
    rp[side]++;
}

int front(int side) {
    return queue[side][rp[side]];
}

int isEmpty(int side) {
    return wp[side] == rp[side];
}
 
void InputData(void) {
    scanf("%d %d %d", &M, &T, &N);
    for (int i = 0; i < N; i++) {
        scanf("%d %s", &AT[i], SIDE[i]);
    }
}

int main(void) {
    InputData();
 
    wp[0] = rp[0] = 0;
    wp[1] = rp[1] = 0;
    // 왼쪽, 오른쪽 큐에 손님들을 배치하기.
    for (int i = 0; i < N; i++) {
        if (strcmp(SIDE[i], "left") == 0) push(0, i);
        else push(1, i);
    }

    // 현재 배의 위치
    int ship_location = 0;
    // 현재 시간
    int timer = 0;
    // 태워준 손님 수
    int total = 0;

    while (total < N) {
        // 만약 배가 있는 방향에 손님이 있고, 현재 시간에 태울 수 있는 손님이 있다면!
        if (!isEmpty(ship_location) && (timer >= AT[front(ship_location)])) {
            // 배에 태운 손님.
            int cnt = 0;
            // 배에 손님을 태울 수 있다면!
            while (!isEmpty(ship_location) && (cnt < M)) {
                int i = front(ship_location);
                if (AT[i] > timer) break;
                pop(ship_location);
                arrived[i] = timer + T;
                cnt++;
                total++;
            }
            timer += T;
            ship_location = ship_location == 0 ? 1 : 0;
        }
        // 현재 배가 있는 방향에 손님이 없거나 OR 현재 시간에 태울 수 있는 손님이 없다면
        else {
            // 만약 현재 배가 있는 방향에 손님이 없다면? 반대쪽에 손님이 반드시 있을것이기 때문에 배를 반대쪽으로 보낸다.
            if (isEmpty(ship_location)) {
                ship_location = ship_location == 0 ? 1 : 0;
                if (timer < AT[front(ship_location)]) {
                    timer = AT[front(ship_location)];
                }
                timer += T;
            }
            // 현재 배가 있는 방향에 손님이 있다면 
            else {
                int idx = front(ship_location);
                int other_side = ship_location == 0 ? 1 : 0;
                // 반대쪽이 비어있지 않고, 현재 배가 있는 방향에 있는 손님보다 반대쪽 손님을 먼저 태워야하는 경우
                if (!isEmpty(other_side) && (AT[idx] > AT[front(other_side)])) {
                    // 배를 반대쪽으로 보낸다
                    ship_location = ship_location == 0 ? 1 : 0;
                    idx = front(ship_location);
                    if (timer < AT[idx]) {
                        timer = AT[idx];
                    } 
                    timer += T;
                }
                // 타이머를 한번에 올려버리기!
                else {
                    timer = AT[idx];
                }
            }
        }
    }
 
    for (int i = 0; i < N; i++) {
        printf("%d\n", arrived[i]);
    }
    return 0;
}