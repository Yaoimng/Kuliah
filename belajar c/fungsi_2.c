#include <stdio.h>
#include <stdbool.h>


int BilanganPrima(int batas){
    int i;
    for (i = 2; i <= batas/2; i++)
    {
        if (batas%i == 0)
        {
            return 0;
        }
        
    }
}

void deretprima(int batas){
    printf("Masukkan Batas deret bilangan prima antara 2 dan %d:\n", batas);

    for (int i = 2; i < batas; i++)
    {
        if (BilanganPrima(i))
        {
            printf("%d\n", i );
        }
        
    }
    
}


int BilanganTerbesar(int a, int b, int c)
{
    int max = a;
    if (b > max)
    {
        max = b;
    }
    if (c > max)
    {
    max =c;
}
    return max;
    
}

void pilih_rumus(int opsi){
    switch(opsi){
        case 1:
            {
                 int batas;
                 printf("Masukkan Batas : ");
                 scanf("%d", &batas);
                 deretprima(batas);
                 break;
            }
        case 2:
            {
                int a, b, c;
                printf("\nMasukkan 3 angka; ");
                scanf("%d %d %d", &a ,&b, &c);
                printf("Angka terbesar dari %d, %d, dan %d  adalah %d", a, b, c, BilanganTerbesar(a,b,c));
                break;
            }
        default:
            printf("Tidak ada opsi yang benar\n");
            break;
    }
}


int main() {
    int opsi;
    printf("Pilih salah satu opsi:\n");
    printf("1. Mencari Bilangan Prima\n");
    printf("2. Mencari Bilangan Terbesar\n");
    scanf("%d", &opsi);
    pilih_rumus(opsi);
    return 0;
}

