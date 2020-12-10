#include<iostream>
#include<vector>
#include<algorithm>
#include<cmath>
#include<string>
#include<numeric>
#include<unordered_map>
//other STL - priority_queue, deque, stack, list, set, map, unordered_map
#define all(a) a.begin(),a.end()
#define range(a,i,j) a.begin()+i,a.begin()+j
using namespace std;

int main()
{
    #ifndef ONLINE_JUDGE
        freopen("../input.txt","r", stdin);
        freopen("../output.txt", "w", stdout);
    #endif
    std::ios::sync_with_stdio(false);
    cin.tie(NULL);
    int n=93;
    vector<int>arr(n);
    for(int i=0;i<n;i++)
        cin>>arr[i];
    unordered_map<int,int>count;
    sort(all(arr));
    for(int i=1;i<n;i++)
        count[arr[i]-arr[i-1]]++;
    cout<<(count[1]+1)*(count[3]+1);
    return 0;
}