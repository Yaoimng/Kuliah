#include <stdio.h>

int main() {
    int angka, hasil, i;

    printf("Input angka = ");
    scanf("%d", &angka);

    hasil = 1;
    i = 1;

    while(i <= angka) {
        hasil = hasil * i;
        i++;
    }

    printf("%d! = %d\n", angka, hasil);

    return 0;
}
