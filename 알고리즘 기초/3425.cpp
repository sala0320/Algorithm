#include <iostream>
#include <stack>
#include <string>
#include <cstdlib>
using namespace std;
#define MAX 1000000000
string tmp;
bool error = false;
int idx;
long long N, num, temp, temp2;
long long NUM[1001];
int main() {
	while (1) {
		string order;
		idx = 0;
		while (1) {
			cin >> tmp;
			if (tmp == "END" || tmp =="QUIT") break;
			else if (tmp == "DIV" || tmp == "MUL") order += tmp[2];
			else if (tmp == "SWP") order += tmp[1];
			else {
				if (tmp == "NUM") cin >> NUM[idx++];
				order += tmp[0];
			}
		}
		if (tmp == "QUIT") break;
		cin >> N;
		for (int n = 0; n < N; n++) {
			cin >> num;
			stack <long long> st;
			st.push(num), error = false, idx = 0;
			for (int i = 0; i < (int)order.size(); i++) {
				switch (order[i])
				{
				case 'N': //NUM
					st.push(NUM[idx++]);
					break;
				case 'P': //POP
					if (st.empty()) error = true;
					else st.pop();
					break;
				case 'I': //INV
					if (st.empty()) error = true;
					else temp = st.top(), st.pop(), st.push(-1 * temp);
					break;
				case 'D': //DUP
					if (st.empty()) error = true;
					else st.push(st.top());
					break;
				case 'V': //DIV
					if (st.size() < 2) error = true;
					else {
						temp = st.top(), st.pop();
						temp2 = st.top(), st.pop();
						if (temp == 0) error = true;
						else st.push(temp2 / temp);
					}
					break;
				case 'S': //SUB
					if (st.size() < 2) error = true;
					else {
						temp = st.top(), st.pop();
						temp2 = st.top(), st.pop();
						if (abs(temp2 - temp) > MAX) error = true;
						else  st.push(temp2 - temp);
					}
					break;
				case 'W': //SWP
					if (st.size() < 2) error = true;
					else {
						temp = st.top(), st.pop();
						temp2 = st.top(), st.pop();
						st.push(temp), st.push(temp2);
					}
					break;
				case 'M': //MOD
					if (st.size() < 2) error = true;
					else {
						temp = st.top(), st.pop();
						temp2 = st.top(), st.pop();
						if (temp == 0) error = true;
						else st.push(temp2 % temp);
					}
					break;
				case 'L': //MUL
					if (st.size() < 2) error = true;
					else {
						temp = st.top(), st.pop();
						temp2 = st.top(), st.pop();
						if (abs(temp2 * temp) > MAX) error = true;
						else st.push(temp2 * temp);
					}
					break;
				case 'A': //ADD
					if (st.size() < 2) error = true;
					else {
						temp = st.top(), st.pop();
						temp2 = st.top(), st.pop();
						if (abs(temp2 + temp) > MAX) error = true;
						else st.push(temp2 + temp);
					}
					break;
				}
				if (error) break;
			}
			if (error == true || st.size() != 1) cout << "ERROR\n";
			else cout << (long long)st.top() << "\n";
		}
		cout << "\n";
	}
	return 0;
}