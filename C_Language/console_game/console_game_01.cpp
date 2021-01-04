#include <stdio.h>
#include <stdlib.h>
#include "Console.h"


// 수업 순서 -> console.h의 함수들 만들기, 콘솔 사이즈, 고투 x,y, x좌표 이동 (키보드), y좌표 이동 및 clear()
int main(void) {
    int x = 14, y = 28;
    int bx = 0, by = 0;
    SetConsoleSize(30, 30);
    bool bullet = false;
    while (1) {
        // 0 키보드가 전혀 안눌려진 상황
        // 0x8000 호출 전 눌린적 없고 호출 시점에 눌린 상태
        // 0x8001 호줄 전 눌려 있고 호출 시점에도 눌린 상태
        // 1 호출전 눌린적 있고 호출 시점에는 안 눌린 상태
        Clear(); // y축을 위해서 지우면서 찍어줘야 함

        if (GetAsyncKeyState(VK_LEFT) & 0x8000) {
            x--;
            if (x < 0) x = 0;
        }
        if (GetAsyncKeyState(VK_RIGHT) & 0x8000) {
            x++;
            if (x > 28) x = 28;
        }
        if (GetAsyncKeyState(VK_SPACE) & 0x8000) {
            if (!bullet) {
                bx = x;
                by = y - 1;
                bullet = true;
            }
        }
        if (bullet) {
            GotoXY(bx, by);
            printf("↑");
            by--;
            if (by < 0) bullet = false;
        }

        GotoXY(x, y);
        printf("▲");
        Sleep(50); // 1000을 기준으로 1초
    }
    system("pause");

}