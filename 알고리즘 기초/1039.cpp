#include<iostream>
#include<string>
#include<algorithm>
#include<queue>
#include<set>

using namespace std;

string str;
int K, answer = 0;

queue<string> que;

int main() {

	ios_base::sync_with_stdio(false);
	cout.tie(NULL);
	cin.tie(NULL);

	cin >> str >> K;

	if (str.length() == 1 || (str.length() == 2 && stoi(str) % 10 == 0)) {
		cout << -1 << endl;
		return 0;
	}

	que.push(str);
	int cnt = 0;

	while (!que.empty() && cnt < K) {

		int size = que.size();
		set<string> visit;

		for (int s = 0; s < size; s++) {

			string temp = que.front();
			que.pop();

			for (int i = 0; i < temp.length() - 1; i++) {
				for (int j = i + 1; j < temp.length(); j++) {

					if (i == 0 && temp[j] == '0') continue;

					swap(temp[i], temp[j]);

					if (visit.find(temp) == visit.end()) {

						if (cnt == K - 1 && answer < stoi(temp)) {
							answer = stoi(temp);
						}
						que.push(temp);
						visit.insert(temp);
					}

					swap(temp[i], temp[j]);

				}
			}
		}
		cnt++;
	}

	cout << answer << endl;

	return 0;

}