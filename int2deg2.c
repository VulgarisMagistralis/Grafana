#include<math.h>
#include<stdio.h>
#include<string.h>
#include<stdlib.h>
int main(int argc, char **args){
        int lat, i, j = 0,k = 0;
	int lng;
	char n1[2][10];
	for(i=0;i<=strlen(args[1]);i++){
		if(args[1][i] == '\t' || args[1][i] == '\0' || args[1][i] == ' '){
			n1[k][j] = '\0';
			j = 0; k++;
		}else{
			n1[k][j]=args[1][i]; j++;

		}
	}
	lat = atoi(n1[0]);
	lng = atoi(n1[1]);
        double deg_lat = lat/(pow(10,7));
	double deg_lng = lng/(pow(10,7));
        printf("%f %f",deg_lat, deg_lng);
        return 0;
}




