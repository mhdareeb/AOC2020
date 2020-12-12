#include<iostream>
#include<vector>
#include<algorithm>
#include<cmath>
#include<string>
#include<numeric>
//other STL - priority_queue, deque, stack, list, set, map, unordered_map
#define all(a) a.begin(),a.end()
#define range(a,i,j) a.begin()+i,a.begin()+j
using namespace std;

bool isValid(int row, int col, int m, int n)
{
    if(row<0 || row>=m)
        return false;
    if(col<0 || col>=n)
        return false;
    return true;
}

int countOccupied(vector<vector<char>>& matrix)
{
    int count=0,m=matrix.size(),n=matrix[0].size();
    for(int i=0;i<m;i++)
    {
        for(int j=0;j<n;j++)
            count+=(matrix[i][j]=='#');
    }
    return count;
}

int main()
{
    #ifndef ONLINE_JUDGE
        freopen("../input.txt","r", stdin);
        freopen("../output.txt", "w", stdout);
    #endif
    std::ios::sync_with_stdio(false);
    cin.tie(NULL);
    int m=98,n=93;
    vector<vector<char>>old(m,vector<char>(n));
    vector<vector<char>>now(m,vector<char>(n,'.'));
    for(int i=0;i<m;i++)
    {
        for(int j=0;j<n;j++)
            cin>>old[i][j];
    }
    vector<pair<int,int>>directions{{0,-1},{-1,-1},{-1,0},{-1,1},{0,1},{1,1},{1,0},{1,-1}};
    while(true)
    {
        for(int i=0;i<m;i++)
        {
            for(int j=0;j<n;j++)
            {
                if(old[i][j]!='.')
                {
                    int occupied=0;
                    for(auto direction:directions)
                    {
                        int row=i+direction.first;
                        int col=j+direction.second;
                        if(isValid(row,col,m,n))
                        {
                            char neighbour=old[row][col];
                            if(neighbour=='#')
                                occupied+=1;
                        }
                    }
                    if(old[i][j]=='L')
                        now[i][j]=(occupied==0)?'#':old[i][j];
                    else if(old[i][j]=='#')
                        now[i][j]=(occupied>=4)?'L':old[i][j];
                }
            }
        }
        if(old==now)
            break;
        old=now;
    }
    int occupied=countOccupied(now);
    cout<<occupied<<endl;
    return 0;
}
