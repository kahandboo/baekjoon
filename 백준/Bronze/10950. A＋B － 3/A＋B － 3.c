#include <stdio.h>

int main(){

    int a,b,t;
    scanf("%d", &t);
    int re[t];
    for(int i = 0; i < t; i++){
        scanf("%d %d",&a,&b);
        re[i] = a+b;
    }
    for (int i = 0; i < t; i++){
        printf("%d\n",re[i]);
    }

    return 0;
}