#include <stdio.h>
#include <string.h>

int luas_segitiga(){
    int alas, tinggi, luas;
    printf("Masukkan alas : ");
    scanf("%d", &alas );
    printf("Masukkan tinggi : ");
    scanf("%d", &tinggi);

    luas = 0.5 * alas * tinggi;

    printf("Luas segitiga = %d", luas);
    return 0;
}

int luas_persegi(){
    int sisi, luas;
    printf("\nMasukkan sisi : ");
    scanf("%d", &sisi);

    luas = sisi * sisi;

    printf("Luas Persegi = %d", luas);
    return 0;
}


int main()
{
    int opsi;
    printf("Pilih : \n");
    printf("1. Luas Segitiga \n");
    printf("2. Luas Persegi \n");
    scanf("%d", &opsi);
    
    switch (opsi)
    {
    case 1:
        luas_segitiga();
        break;
    
    case 2:
        luas_persegi();
        break;
    
    
    default:
        printf("Pilihan Tidak valid \n");
        break;
    }
    return 0;
}