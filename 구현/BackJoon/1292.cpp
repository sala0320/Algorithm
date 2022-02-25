#include <iostream>
#include <vector>
#include <numeric>
using namespace std;
int solve(int start, int last)
{
    vector<int> v;
    int num = 1, now = 1, flag = 0;
    while(num <= last){
        for(int i=0; i<now; i++){
            if(num >= last){
                v.push_back(now);
                return accumulate(v.begin(), v.end(), 0);
            }
            if(num >= start)
                v.push_back(now);
            
            num++;
        }
        now++;
    }
    return -1;
}
int main()
{
    int A, B, result;
    cin >> A >> B;
    result = solve(A, B);
    cout << result;
}