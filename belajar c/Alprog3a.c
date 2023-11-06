#include <stdio.h>
 
int main()
{
    double num;
 
    printf("Masukkan skor antara 0 dan 100: ");
    scanf("%lf", &num);
    
    if (num >= 90)
        printf("Sepuluh nilai tertinggi.\n");
    else if (num >= 80 && num < 90)
        printf("Nilai Huruf A.\n");
    else if (num >= 70 && num < 80)
        printf("Nilai huruf B.\n");
    else if (num >= 60 && num < 70)
        printf("Nilai huruf C.\n"); 
    else if (num >= 50 && num < 60)
        printf("Nilai Huruf D.\n");
    else if (num >= 40 && num < 50)
        printf("Nilai huruf E.\n");
    else if (num < 40)
        printf("Dibawah nilai E.\n");
 
    return 0;
}