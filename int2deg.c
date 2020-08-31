#include<math.h>
#include<stdio.h>
#include<stdlib.h>
int main(int argc, char **args){
	int num = atoi(args[1]);
	double deg = num/(pow(10,7));
	double temp = (fmod(num , pow(10,7)) / pow(10,7)) * 60;
	double min = (fmod(num, pow(10,7)) / pow(10,7) * 60);
	double sec = (fmod((temp * pow(10,5)) , pow(10,5)) * 60) /pow(10,5);

	printf("%.2f,%.2f,%.2f", deg, min ,sec);
	return 0;
}
