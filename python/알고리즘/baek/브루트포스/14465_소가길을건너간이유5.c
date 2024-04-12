#include <stdio.h>
#define min(a,b)   (((a) < (b)) ? (a) : (b))

int N, K, B;
int TrafficLight[100000+10] = {1,};

void InputData(void){
    scanf("%d %d %d %d", &N, &K, &B);
    int Empty;
    for (int i=0; i<B ; i++){
        scanf("%d", &Empty);
        TrafficLight[Empty] = 0;
    }
}


int main(void) {
    InputData();

    int need = 0;
    for (int i = 1; i < K+1; i++) {
        if (TrafficLight[i] == 0) {
            need++;
        }
    }
    int result = need;
    for (int i = 2; i < N - K + 2; i++) {
        if (TrafficLight[i-1] == 0) {
            need--;
        }
        if (TrafficLight[i+K-1] == 0) {
            need++;
        }
        
        result = min(result, need);
    }

    printf("%d", result);
    return 0;
}