#include <cstdio>
#include <vector>
using namespace std;

bool chae[3200];
vector<int> prime;
int n;

int main() {
    for (int i = 2 ; i < 3200 ; i++) {
        if (chae[i]) 
            continue;
        for (int j = i + i ; j < 3200 ; j += i) {
            chae[j] = true;
        }
    }
    for (int i = 2 ; i < 3200 ; i++) {
        if (!chae[i]) {
            prime.push_back(i);
        }
    }
    scanf("%d", &n);
    if (n == 1) {
        return 0;
    }
    for (int i = 0 ; i < prime.size() ; i++) {
        while (n % prime[i] == 0) {
            printf("%d\n", prime[i]);
            n /= prime[i];
        }
        if(n == 1)
            break;
    }
    if (n > 1) {
        printf("%d\n", n);
    }
}