#include <stdio.h>

int main(void) {
    int n, total = 0;
    printf("Digite um número: ");
    scanf("%d", &n);
    
    for(int i = 1; i<=n; i++){
        total += 1;
        printf("%d\n", total);
    }
   
    return 0;
}