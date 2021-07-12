//30의 배수이기 위해서는 다음의 조건을 충족해야 한다.
//1. 끝의 자리수가 0이여야 합니다.
//2. 각 자리의 수의 합이 3의 배수여야 합니다.
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
string num;
bool flag = true;
long long sum = 0;
vector<int> marco;
int main()
{
    cin >> num;
    for(int i = 0; i < num.length(); i++)
    {
        sum += (num[i] - '0');
        if(!(num[i] - '0'))
            flag = false;
        marco.push_back(num[i] - '0');
    }
    //각 자리 수 합 3의 배수 아니거나, 끝자리수 0아니면
    if(sum % 3 || flag)
    {
        cout << "-1" << endl;
    }
    else
    {
        sort(marco.begin(), marco.end());
        for(int i = marco.size()-1; i >= 0; i--)
            cout << marco[i];
    }
    return 0;
}
