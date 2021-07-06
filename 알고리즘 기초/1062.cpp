
#include <cstring>
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;


// a n t  i c
bool check[26];
vector<string> v;
int ans;
void solve(int begin, int cnt)
{
    if (cnt == 0) {

        int sum = 0;
        //비교해서 최댓값 구한다
        for (int i = 0; i < v.size(); ++i) {

            bool ch = true;

            for (int j = 0; j < v[i].size(); ++j) {
                int temp = v[i][j] - 'a';
                if (check[temp] == 0) {
                    ch = false;
                    break;
                }
            }
            if (ch) sum++;
        }

        ans = max(ans, sum);
        return;
    }

    for (int i = begin + 1; i < 26; ++i) {

        if (check[i]) continue;

        check[i] = true;
        solve(i, cnt - 1);
        check[i] = false;

    }
}
int main()
{
    int n, k;

    cin >> n >> k;
    for (int i = 0; i < n; ++i) {
        string s;
        cin >> s;
        v.push_back(s);
    }
    if (k < 5) {
        cout << 0 << "\n";
        return 0;
    }

    k -= 5;
    check['a' - 'a'] = true;
    check['n' - 'a'] = true;
    check['t' - 'a'] = true;
    check['i' - 'a'] = true;
    check['c' - 'a'] = true;

    solve(-1, k);

    cout << ans << "\n";

    return 0;
}