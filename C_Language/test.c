#include <stdio.h>
#include "human.h"

int main(){
    struct Human Kim = Create_Human("Kim", 16, MALE);
    Print_Human(&Kim);

    return 0;
}