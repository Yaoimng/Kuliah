#include <stdio.h>
#include <string.h>
#include <ctype.h>

// int main() {
//     char str[100];
//     int panjang;

//     printf("Masukkan String: ");
//     gets(str);

//     panjang = strlen(str);

//     printf("Jadi panjang stringnya adalah %d\n", panjang);

//     return 0;
// }

// int main() {
//     char name[100];
//     char kebalikan[100];
//     int panjang, i;

//     printf("Masukkan Nama Anda (dalam huruf besar): ");
//     scanf("%s", name);

//     panjang = strlen(name);

//     for (i = 0; i < panjang; i++) {
//         name[i] = tolower(name[i]);
//     }

//     for (i = 0; i < panjang; i++) {
//         kebalikan[i] = name[panjang - i - 1];
//     }

//     printf("Hasil: %s\n", kebalikan);

//     return 0;
// }

// #include <stdio.h>
// #include <string.h>

// int main()
// {
//     char kalimat[100];
//     int panjang, i, j, palindrom = 1;
//     printf("Masukkan kalimat: ");
//     fgets(kalimat, 100, stdin);
//     kalimat[strcspn(kalimat, "\n")] = 0;
//     panjang = strlen(kalimat);
//     for (i = 0, j = panjang - 1; i < j; i++, j--)
//     {
//         if (kalimat[i] != kalimat[j])
//         {
//             palindrom = 0;
//             break;
//         }
//     }
//     if (palindrom == 1)
//     {
//         printf("Termasuk PALINDROM\n");
//     }
//     else
//     {
//         printf("Bukan PALINDROM\n");
//     }

//     return 0;
// }

// #include <stdio.h>
// #include <string.h>

// int main()
// {
//     char string[100];
//     int i;
//     printf("Masukkan string: ");
//     fgets(string, 100, stdin);
//     string[strcspn(string, "\n")] = 0;
//     for (i = 0; i < strlen(string); i++)
//     {
//         if (string[i] == 'a')
//         {
//             string[i] = 'i';
//         }
//     }
//     printf("Hasil: %s\n", string);

//     return 0;
// }

// #include <stdio.h>
// #include <string.h>

// int main()
// {
//     char string1[100], string2[100];

//     // Minta pengguna untuk memasukkan dua buah string
//     printf("Masukkan string pertama: ");
//     fgets(string1, 100, stdin);
//     string1[strcspn(string1, "\n")] = '\0';

//     printf("Masukkan string kedua: ");
//     fgets(string2, 100, stdin);
//     string2[strcspn(string2, "\n")] = '\0';

//     // Membandingkan kedua string
//     if (strcmp(string1, string2) == 0)
//     {
//         printf("Kedua string sama.\n");
//     }
//     else
//     {
//         printf("Kedua string tidak sama.\n");
//     }

//     return 0;
// }

// #include <stdio.h>
// #include <string.h>

// int main() {
//     char nama[4][100], temp[100];
//     int i, j;

//     // Minta pengguna untuk memasukkan 4 nama
//     for (i = 0; i < 4; i++) {
//         printf("Masukkan nama ke-%d: ", i + 1);
//         fgets(nama[i], 100, stdin);
//         nama[i][strcspn(nama[i], "\n")] = 0; // Hapus karakter newline
//     }

//     // Urutkan nama
//     for (i = 0; i < 3; i++) {
//         for (j = i + 1; j < 4; j++) {
//             if (strcmp(nama[i], nama[j]) > 0) {
//                 strcpy(temp, nama[i]);
//                 strcpy(nama[i], nama[j]);
//                 strcpy(nama[j], temp);
//             }
//         }
//     }

//     // Tampilkan nama yang sudah diurutkan
//     printf("\nSesudah diurutkan:\n");
//     for (i = 0; i < 4; i++) {
//         printf("Nama ke-%d: %s\n", i + 1, nama[i]);
//     }

//     return 0;
// }

#include <stdio.h>
#include <string.h>

int main() {
    char kata[] = "ELEKTRO";
    int panjang = strlen(kata);

    // Mengekstrak substring dan mencetaknya secara berurutan
    for (int i = panjang; i <= 1; i--) {
        printf("%.*s\n", i, kata);
    }

    return 0;
}

#include <stdio.h>
#include <string.h>

int main() {
    char kalimat[] = "ELEKTRO"; 
    int panjang = strlen(kalimat);

    for (int i = 1; i <= panjang; i++) { 
        for (int j = 0; j < i; j++) {
            printf("%c", kalimat[j]);
        }
        printf("\n");
    }

    return 0;
}
