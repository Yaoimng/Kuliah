#include<stdio.h>
#include<string.h>

int main()
    {
        int a,b = 900;
        do
        {
            printf("Masukkan Tebakan anda : ");
        scanf("%d", &a);
        if (a > b )
        {
            printf("Lebih kecil \n");
        }
        if (a < b)
        {
            printf("Lebih besar \n");
        }
        } while (a != b);
        printf("Selamat!");
        return 0;
    }   