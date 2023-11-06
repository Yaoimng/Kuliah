#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
    int angkaAcak, tebakan;
    srand(time(0)); 
    angkaAcak = rand() % 100 + 1; 
    do {
        printf("Angka tebakan: ");
        scanf("%d", &tebakan);
        if (tebakan < angkaAcak) {
            printf("Tebakan terlalu kecil\n");
        } else if (tebakan > angkaAcak) {
            printf("Tebakan terlalu besar\n");
        }
    } while (tebakan != angkaAcak);
    printf("Angka tebakan: %d\n", angkaAcak);
    printf("Tebakan benar\n");
    return 0;
}
