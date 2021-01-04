#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include "Console.h"

int main(void){
    int x = 14, y= 28;
    int bx= 0, by = 0;
    bool bullet = false;

    int ex = 0, ey = 0;
    bool enemy = false;

    srand(time(NULL));
    SetConsoleSize(30, 30);

    while(1){
        Clear();
        //맨위에
        if (!enemy){
            ex = (rand() % 15) * 2
            ey = 0;
            enemy = true;
        }
        //맨 밑에
        if(enemy){
            GotoXY(ex, ey);
            printf("★");
            ey++;
            if(ey > y) enemy = false;
        }
    }   
}