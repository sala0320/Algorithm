// 손익분기점 Cx > A + Bx -> (C - B)x > A -> x > A / (C -B)

#include <iostream>
using namespace std;
int main()
{
	int A, B, C;
	int num = 0;

	cin >> A >> B >> C;

	if (C - B <= 0)
		cout << -1;
	else
		cout << (A / (C - B)) + 1 << endl;
}






