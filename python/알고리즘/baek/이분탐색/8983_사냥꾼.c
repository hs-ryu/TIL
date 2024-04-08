#include <stdio.h>
#include <stdlib.h>

int N;
int M;
int L;
int sadae[100001];
int X[100001];
int Y[100001];

void InputData() {
    scanf("%d %d %d", &M, &N, &L);
    for (int i = 0; i < M; i++) {
        scanf("%d", &sadae[i]);
        // printf("%d\n", sadae[i]);
    }
    for (int i = 0; i < N; i++) {
        scanf("%d %d", &X[i], &Y[i]);
        // printf("%d %d\n", X[i], Y[i]);
    }
}

int comp(const void *a, const void *b) {
    return *(int *)a - *(int *)b;
}

int main() {
    InputData();
    
    qsort(sadae, M, sizeof(int), comp);

    int result = 0;
    for (int i = 0; i < N; i++) {
        

        // 동물 하나씩 보면서 확인.
        int x = X[i];
        int y = Y[i];

        // 동물의 y 위치가 L보다 크다면 어차피 못잡음.
        if (y > L) {
            continue;
        }

        // 동물의 위치에서, 잡을 수 있는 사대의 위치 범위.
        int minX = x + y - L;
        int maxX = x - y + L;

        int l = 0;
        int r = M - 1;

        while (l <= r) {
            int middle = (l + r) / 2;

            if (minX <= sadae[middle] && sadae[middle] <= maxX ) {
                result++;
                break;
            } else if (sadae[middle] < minX) {
                l = middle + 1;
            } else if (maxX < sadae[middle]) {
                r = middle - 1;
            }
        }
    }

    printf("%d", result);

}