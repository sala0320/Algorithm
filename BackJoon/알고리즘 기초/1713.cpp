#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;
int main()
{
    vector <int> vote;
    // vector <int> student;
    int pic, std_num;
    int std[1000];  

    scanf("%d", &pic);
    scanf("%d", &std_num);

    for (int i = 0; i < std_num; i++)
    {
        scanf("%d", &std[i]);
    }
    
    for (int j = 0; j < std_num; j++)
    {   
        int s = std[j];
        // printf("%d", s);
        if(vote.size() == 3)
        {   
            auto idx = find(vote.begin(), vote.end(), s);
            if(idx == vote.end())
            {
                vote.erase(vote.begin());
                vote.push_back(s);
            }
            else
            {
                vote.erase(idx);
                vote.push_back(s);
            }
        }
        else
        {
            vote.push_back(s);
        }
    }
    sort(vote.begin(), vote.end());
    for (int k=0; k < pic; k++)
        printf("%d ", vote[k]);
}