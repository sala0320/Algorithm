#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

int l, c;
string pw;
bool checked[17] = { 0, };

void dfs(int cnt, int current) {

	if (cnt == l) {
        //자음 모음 개수 체크
		int m=0, j=0;
		for (int i = 0; i < pw.size(); i++) {
			if (checked[i]) {
				if (pw[i] == 'a' || pw[i] == 'e' || pw[i] == 'i' || pw[i] == 'o' || pw[i] == 'u')
					m++;
				else
					j++;
			}
		}
		if (m >= 1 && j >= 2) {
			for (int i = 0; i < pw.size(); i++)
				if (checked[i])
					cout << pw[i];
			cout << endl;
		}
		return;
	}

	for (int i = current; i < pw.size(); i++) {
		if (checked[i] == 0) {
			checked[i] = 1;
			dfs(cnt + 1, i);
			checked[i] = 0;
		}
	}
	return;
}

int main() {

	cin >> l >> c;
	for (int i = 0; i < c; i++) {
		char x;
		cin >> x;
		pw += x;
	}
	sort(pw.begin(), pw.end());
	dfs(0, 0);
	return 0;
}