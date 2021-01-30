#include <stdio.h>
#include <book_function.h>

int main() {
  int user_choice;        /* 유저가 선택한 메뉴 */
  int num_total_book = 0; /* 현재 책의 수 */

  /* 각각 책, 저자, 출판사를 저장할 배열 생성. 책의 최대 개수는 100 권*/
  char book_name[100][30], auth_name[100][30], publ_name[100][30];
  /* 빌렸는지 상태를 표시 */
  int borrowed[100];

  while (1) {
    printf("도서 관리 프로그램 \n");
    printf("메뉴를 선택하세요 \n");
    printf("1. 책을 새로 추가하기 \n");
    printf("2. 책을 검색하기 \n");
    printf("3. 책을 빌리기 \n");
    printf("4. 책을 반납하기 \n");
    printf("5. 프로그램 종료 \n");

    printf("당신의 선택은 : ");
    scanf("%d", &user_choice);

    if (user_choice == 1) {
      /* 책을 새로 추가하는 함수 호출 */
      add_book(book_name, auth_name, publ_name, borrowed, &num_total_book);
    } else if (user_choice == 2) {
      /* 책을 검색하는 함수 호출 */
      search_book(book_name, auth_name, publ_name, num_total_book);
    } else if (user_choice == 3) {
      /* 책을 빌리는 함수 호출 */
      borrow_book(borrowed);
    } else if (user_choice == 4) {
      /* 책을 반납하는 함수 호출 */
      return_book(borrowed);
    } else if (user_choice == 5) {
      /* 프로그램을 종료한다. */
      break;
    }
  }

  return 0;
}










// Compile 순위
// 1. () [] -> .
// 2. ! ~ ++ 
// 3. * \ %

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
