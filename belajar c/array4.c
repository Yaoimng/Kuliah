#include <stdio.h>
// Soal Latihan 4

int main(){
    int i;
    int letters[20] = {'a','b','c','z','e','f','g','h','i','j','k','l','m','n','o'};
    for (i = 0; i < 20; i += 2)
    {
        printf("%c\n",letters[i]);
    } 
}