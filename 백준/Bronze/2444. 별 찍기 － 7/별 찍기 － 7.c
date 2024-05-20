#include <stdio.h>

int main(){

    int n;
    scanf("%d",&n);
    int row = 2*n-1;
    for(int i = 0; i < row; i++){
        if(i < n-1){
            for(int j = 1; j < n - i; j++){
                printf(" ");
            }
            for(int k = 1; k < (i+1)*2; k++){
                printf("%s","*");
            }
            printf("\n");
        }
        else{
            for(int k = 0; k < i-n+1 ; k++){
                printf(" ");
            }
            for(int j = 1; j < (row-i)*2; j++){
                printf("%s","*");
            }
            printf("\n");
        }
    }

    return 0;
}