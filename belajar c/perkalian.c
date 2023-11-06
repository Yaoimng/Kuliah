#include <stdio.h>

int main(){
    int a, b, i = 0;

    printf("Masukkan Bilangan Pertama: ");
    scanf("%d", &a);
    printf("Masukkan Bilangan Kedua: ");
    scanf("%d", &b);

    while (a >= b)
    {
        a = a -b;
        i++;
    }
    
    printf("Hasil pembagian adalah %f\n" , i );
    return 0;
}