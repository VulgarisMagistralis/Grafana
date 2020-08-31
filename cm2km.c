#include<math.h>
#include<stdio.h>
#include<stdlib.h>
int main(int argc, char **args){
        int speed_c = atoi(args[1]);
	int speed_k = speed_c/36*1000;
        printf("%d",speed_k);
        return 0;
}





