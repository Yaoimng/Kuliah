#include <stdio.h>

// int a(){   
// }

// int b(){ 
//     float r, luas, keliling;
//     float phi = 3.14;
//     printf("Masukkan jari-jari lingkaran = ");
//     scanf("%f",&r);
//     luas = phi * r * r;
//     keliling = 2 * r * phi;
//     printf("Luas = %.1f keliling = %.1f", luas, keliling);
// }

// int c(){ 
//     float r;
//     printf("\nMasukkan jari-jari lingkaran = ");
//     scanf("%f",&r);
// }


// int main()
// {
//     a();
//     b();
//     c();
// }

// int sumEven(int arr[], int n) {
//     int sum = 0;
//     for (int i = 0; i < n; i++) {
//         if (arr[i] % 2 == 0) {
//             sum += arr[i];
//         }
//     }
//     return sum;
// }

// int main() {
//     int n;
//     printf("Masukkan jumlah data: ");
//     scanf("%d", &n);
//     int arr[n];
//     printf("Masukkan data:\n");
//     for (int i = 0; i < n; i++) {
//         scanf("%d", &arr[i]);
//     }
//     int sum = sumEven(arr, n);
//     printf("Jumlah data genap adalah %d\n", sum);
//     return 0;
// }

// int Terbesar(){
//     int a, b, c, result;
//     printf("Masukkan 3 angka : ");
//     scanf("%d %d %d", &a, &b, &c);
//     if (a>b){
//         if (a>c)
//         {
//             result = a; 
//             printf("Angka yang terbesar adalah %d", result);
//         }
//         else
//         {
//             result = c;
//             printf("Angka yang terbesar adalah %d", result);
//         }
//     }
//     else if (b>c){
//         result = b;
//         printf("Angka yang terbesar adalah %d", result);}
//     else{
//         result = c;
//         printf("Angka yang terbesar adalah %d", result);}   
// }

// int main(){
//     Terbesar();
// }

// void tukar_nilai(int *a, int *b){
//     int temp = *a;
//     *a = *b;
//     *b = temp;
// }

// int main(){
//     int x, y;
//     printf("Masukkan bilangan ke-1 ");
//     scanf("%d", &x);
//     printf("Masukkan bilangan ke-2 ");
//     scanf("%d", &y);
//     tukar_nilai(&x, &y);
//     printf("Setelah ditukar: 1 = %d, 2 = %d\n", x, y);
//     return 0;
// }