#include <cstdio>
#include <vector>
using namespace std;

vector<int> parent; 
int find(int num)
{
    //부모노드와 값이 같을  때
    if(parent[num] == num)
        return num;
    ///부모노드와 값이 다를 때 -> 부모노드에 값 연결(재귀)
    else
        return parent[num] = find(parent[num]);
}
void uni(int a, int b)
{
    int pa = find(a);
    int pb = find(b);

    if(pa == pb)
        return;
    //부모노드가 다르면 합치기
    parent[pb] = pa;
}
int main()
{
    int n,m;
    scanf("%d %d", &n, &m);
    for(int i = 0; i <= n; i++)
        parent.push_back(i);
    for (int i = 0; i < m; i++)
    {
        int c,a,b;
        scanf("%d %d %d", &c, &a, &b);
        if(c == 0){
            uni(a,b);
        }  
        else{
            if(find(a) == find(b))
                printf("YES\n");
            else    
                printf("NO\n");
        }

    }

}