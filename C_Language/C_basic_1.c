#include <stdio.h>



int add_number(int *parr){
    int i;
    for (i=0; i<3 ; i++){
        parr[i]++;
    }
    return 0;
}

int main(){
    int arr[3];
    int i;

    for (i = 0; i < 3; i++){
        scanf("%d", &arr[i]);
    }
    add_number(arr);

    printf("Each Element : %d, %d, %d \n", arr[0], arr[1], arr[2]);

}

유저로부터 10개의 값을 받고 배열에 저장한 후 다른 함수에 보내어 Max value를 찾아 return 하라. 

maximum(arr)


// 포인터는 메모리 상에 위치한 특정한 데이터의 (시작)주소값을 보관하는 "변.수"
// (포인터에 주소값이 저장되는 데이터의 형태 type) *(포인터의 이름); -> int *a; 
// int* a; int *a; 
// & 연산자 
// &주소값을 계산할 데이터 
// &a 


// a= 소수점 두자리까지만 .2, .3-> 소수점 3자리 , .4f 소수점 4자리
// b= length of the string = 5 -> 
// c= length of the string = 6, 소수점 3자리까지

// gcc -o test C_basic_1.c

// int = 4byte -> 21억 어쩌고를 가질 수 있다.

/*
char 1 byte -> 한개의 문자를 저장 함 8비트 연산 안에 들어갈 수 있는건 문자 한개뿐
short int 2 bytes
int 4 bytes
long 4 bytes
bool 1 byte : true of false
float 4 bytes : 소수점 7자리까지 정확한 값계산 나옴  -> 이상 넘어가게 되면 ^x
double 8 bytes : 소수점 15자리까지 정확한 값계산 나옴
long double 8 bytes: 소수점 15자리까지 정확한 값계산 나옴
long long 16 bytes : 매우 김 
*/
