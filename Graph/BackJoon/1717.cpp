#include <cstdio>
#include <vector>
using namespace std;

vector<int> parent; 
int find(int num)
{
    if(parent[num] == num)
        return num;
    else
        return parent[num] = find(parent[num]);
}
void uni(int a, int b)
{
    int pa = find(a);
    int pb = find(b);

    if(pa == pb)
        return;
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