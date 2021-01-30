#pragma once
#include <windows.h>

//──────────────────────────────────────────────────────
// 화면을 지워주고 커서의 위치를 0,0 으로 이동시키는 함수
//──────────────────────────────────────────────────────
void Clear(void) {
	system("cls");
}
//──────────────────────────────────────────────────────
// 커서의 위치를 _x, _y 로 변경하는 함수
//──────────────────────────────────────────────────────
void GotoXY(int _x, int _y) {
	COORD pos = { _x, _y };
	SetConsoleCursorPosition(GetStdHandle(STD_OUTPUT_HANDLE), pos);
}
//──────────────────────────────────────────────────────
// console 창의 title을 변경해 주는 함수
//──────────────────────────────────────────────────────

//──────────────────────────────────────────────────────
// 배경색, 글자색을 변경해 주는 함수
//──────────────────────────────────────────────────────
void SetMyColor(unsigned char _BgColor, unsigned char _TextColor) {
	if (_BgColor > 15 || _TextColor > 15) return;
	unsigned short ColorNum = (_BgColor << 4) | _TextColor;
	SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE), ColorNum);
}
//──────────────────────────────────────────────────────
// cursor를 보이게, 안보이게 하는 함수 
//──────────────────────────────────────────────────────
void SetMyCursor(BOOL _bShow) {
	CONSOLE_CURSOR_INFO curInfor;
	GetConsoleCursorInfo(GetStdHandle(STD_OUTPUT_HANDLE), &curInfor);
	curInfor.bVisible = _bShow;
	GetConsoleCursorInfo(GetStdHandle(STD_OUTPUT_HANDLE), &curInfor);
}
//──────────────────────────────────────────────────────
// console 창의 크기를 정하는 함수 ( 디폴트 80, 25 )
//──────────────────────────────────────────────────────
void SetConsoleSize(int _col, int _lines) {
	system("mode con cols=80 lines=25");
}