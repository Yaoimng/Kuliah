#include <stdio.h>

int main()
{
    int pilihan, uang, kembalian;
    printf("Pilih minuman: \n");
    printf("1. Cola \t Rp 5000 \n");
    printf("2. Susu \t Rp 3000 \n");
    printf("3. Teh  \t Rp 2500 \n");
    printf("4. Soda \t Rp 6000 \n");
    printf("Masukkan pilihan Anda (1-4): ");
    scanf("%d", &pilihan);
    printf("Masukkan uang Anda: ");
    scanf("%d", &uang);
    
    if (pilihan == 1) {
        if (uang >= 5000) {
            kembalian = uang - 5000;
            printf("Anda memilih Cola\n");
            printf("Kembalian Anda adalah Rp %d\n", kembalian);
        } else {
            printf("Uang Anda kurang\n");
        }
    } else if (pilihan == 2) {
        if (uang >= 3000) {
            kembalian = uang - 3000;
            printf("Anda memilih Susu\n");
            printf("Kembalian Anda adalah Rp %d\n", kembalian);
        } else {
            printf("Uang Anda kurang\n");
        }
    } else if (pilihan == 3) {
        if (uang >= 2500) {
            kembalian = uang - 2500;
            printf("Anda memilih Teh\n");
            printf("Kembalian Anda adalah Rp %d\n", kembalian);
        } else {
            printf("Uang Anda kurang\n");
        }
    } else if (pilihan == 4) {
        if (uang >= 6000) {
            kembalian = uang - 6000;
            printf("Anda memilih Soda\n");
            printf("Kembalian Anda adalah Rp %d\n", kembalian);
        } else {
            printf("Uang Anda kurang\n");
        }
    } else {
        printf("Pilihan tidak valid\n");
    }
    return 0;
}
