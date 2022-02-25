#include <iostream>
using namespace std;
int main(){
    int n;
    cin >> n;
    for (int i=0; i<n; i++){
        int w;
        string s;
        cin >> w >> s;
        cout << s.erase(w-1, 1) << endl;
    }
}