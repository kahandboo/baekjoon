#include <stdio.h>

int main(){

    int x,n,a,b;
    int re = 0;
    scanf("%d\n%d",&x,&n);
    for(int i = 0; i < n; i++){
        scanf("%d %d",&a,&b);
        re = re + (a * b);
    }
    if (re == x){
        printf("%s","Yes");
    }
    else{
        printf("%s","No");
    }

    return 0;
}