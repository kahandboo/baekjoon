#include <stdio.h>

int main(){

    int n;
    scanf("%d",&n);
    int try = n / 4;
    for (int i = 0; i < try; i++){
        printf("%s ","long");
    }
    printf("%s","int");

    return 0;
}