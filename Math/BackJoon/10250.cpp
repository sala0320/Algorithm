#include <iostream>
using namespace std;
int main()
{
	int T;
	int H, W, N;
	int height, width;
	cin >> T;
	for (int i = 0; i < T; i++)
	{
		cin >> H >> W >> N;
		if (N % H == 0)
		{
			height = H;
			width = N / H;
		}
		els¤¤e
		{
			height = N % H;
			width = N / H + 1;
		}
		cout << height * 100 + width << "\n";
	}
}