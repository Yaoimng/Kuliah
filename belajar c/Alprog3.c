#include <stdio.h>

int main()
{
     int Nilai;
    
    printf("Masukkan Nilai antara 0 hingga 100: ");
    scanf("%d", &Nilai);

    if (Nilai > 80)
    {
        printf("A\n");
    }
    else if (Nilai > 70 && Nilai <= 80)
    {
        printf("Nilai : B.\n");
    }
    else if (Nilai > 60 && Nilai <= 70)
    {
        printf("Nilai : C.\n");
    }
    else if (Nilai > 50 && Nilai <= 60)
    {
        printf("Nilai : D.\n"); 
    }
    else if (Nilai <= 50)
    {
        printf("Nilai : E.\n");  
    } 
    
    return 0;
}       
