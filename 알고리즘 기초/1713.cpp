#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int N,K,temp;
vector <pair<int,int>> candi;

void chking(int a){
    int chking=true;
    for(int i=0;i<candi.size();i++){
        if(candi[i].first==a){
            candi[i].second++;
            chking=false;
            break;
        }
    }
    if(chking){
        if(candi.size()<N){
            candi.push_back({a,1});
        }else{
            int min=1000;
            int index=-1;
            for(int i=0;i<candi.size();i++){
                int chk = candi[i].second;
                if(min>chk){
                    min=chk;
                    index=i;
                }
            }
            candi.erase(candi.begin()+index);
            candi.push_back({a,1});
        }
    }
}

int main(){
    
    cin>>N>>K;
    for(int i=0;i<K;i++){
        cin>>temp;
        chking(temp);
    }
    sort(candi.begin(),candi.end());
    for(int i=0;i<N;i++){
        cout<<candi[i].first<<" ";
    }
    return 0;
}