#include <stdio.h>
#define max(a,b)   (((a) > (b)) ? (a) : (b))

int N, D, K, C;
int Sushis[30000+10];

void InputData(void){
    scanf("%d %d %d %d", &N, &D, &K, &C);
    for (int i=0; i<N ; i++){
        scanf("%d", &Sushis[i]);
        // printf("%d ", Sushis[i]);
    }
}

int main(void) {

    InputData();
    
    int result = 0;

    for (int i = 0; i < N; i++) {
        int check[3010] = {0,};
        int cnt = 0;
        for (int j = i; j < i+K; j++) {
            int p = j;
            if (j >= N) {
                p -= N;
            }
            int sushi = Sushis[p];

            if (check[sushi]) {
                continue;
            }

            check[sushi] = 1;
            cnt++;
        }

        if (check[C] == 0) {
            cnt++;
        }
        result = max(result, cnt);
    }

    printf("%d", result);
    return 0;
}