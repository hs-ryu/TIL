#include <stdio.h>

int N;
unsigned long long ATK;
int T[123457];
int A[123457];
int H[123457];


void InputData() {
    scanf("%d %llu", &N, &ATK);
    for (int i = 0; i < N; i++) {
        scanf("%d %d %d", &T[i], &A[i], &H[i]);
    }
}

int main() {
    InputData();

    unsigned long long l = 0;
    unsigned long long r = (1000001 * 1000001);
    // printf("%llu\n", r);
    unsigned long long result = 0;
    
    while (l <= r) {
        unsigned long long ATK_copy = ATK;
        unsigned long long MaxHP = (l + r) / 2;

        int isDie = 0;
        unsigned long long CurHP = MaxHP;

        for (int i = 0; i < N; i++) {
            int t,a,h = T[i], A[i], H[i];

            if (t == 2) {
                ATK_copy += a;
                if (CurHP + h < MaxHP) {
                    CurHP = CurHP + h;
                } else {
                    CurHP = MaxHP;
                }
            }
            else if (t == 1) {
                if (h % ATK_copy != 0) {
                    CurHP -= a * (h / ATK_copy);
                } else {
                    CurHP -= a * ((h / ATK_copy)-1);
                }
            }
            if (CurHP <= 0) {
                isDie = 1;
                break;
            }
            printf("%llu %llu %llu %llu %llu %d", ATK_copy, MaxHP, CurHP,  l, r, isDie);
        }
        if (isDie) {
            l = MaxHP + 1;
        } else {
            r = MaxHP - 1;
            result = MaxHP;
        }
    }
    printf("%llu", result);

    return 0;
}