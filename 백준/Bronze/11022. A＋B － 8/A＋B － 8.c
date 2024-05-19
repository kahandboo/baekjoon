#include <stdio.h>

int main(){

    int t;
    scanf("%d",&t);
    int a[t],b[t],re[t];
    for(int i = 0; i < t; i++){
        scanf("%d %d",&a[i],&b[i]);
        re[i] = a[i] + b[i];
    }
    for(int i = 0; i < t; i++){
        printf("Case #%d: %d + %d = %d\n",i+1,a[i],b[i],re[i]);
    }

    return 0;
}