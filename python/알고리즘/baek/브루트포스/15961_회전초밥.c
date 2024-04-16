#include <stdio.h>

int N, D, K, C;
int A[3000000+10];

void InputData(void){
    scanf("%d %d %d %d", &N, &D, &K, &C);
    for (int i=0; i<N ; i++){
        scanf("%d", &A[i]);
    }
}

int main(void){

    InputData();

    int selected_list[10000];
    int kinds = 0;
    int maximum_kinds = 0;
    for (int i = 0; i < K; i++) {
        if (selected_list[A[i]] == 0) {
            kinds++;
        }
        selected_list[A[i]]++;
    }

    if (selected_list[C] == 0) {
        maximum_kinds = kinds + 1;
    } else {
        maximum_kinds = kinds;
    }

    for (int i = 0; i < N; i++) {
        int front = i;
        int end = i + K;

        if (end >= N) {
            end -= N;
        }
        
        selected_list[A[front]]--;
        if (selected_list[A[front]] == 0) {
            kinds--;
        }

        if (selected_list[A[end]] == 0 ) {
            kinds++;
        }
        selected_list[A[end]]++;

        if (selected_list[C] == 0) {
            if (maximum_kinds < kinds + 1) {
                maximum_kinds = kinds + 1;
            }
        } else {
            if (maximum_kinds < kinds) {
                maximum_kinds = kinds;
            }
        }
    }

    printf("%d\n", maximum_kinds);
    return 0;
}