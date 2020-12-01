#include<iostream>
#include<vector>
#include<algorithm>
#include<cmath>
#include<string>
#include<numeric>
#include<unordered_set>
//other STL - priority_queue, deque, stack, list, set, map, unordered_map
#define all(a) a.begin(),a.end()
#define range(a,i,j) a.begin()+i,a.begin()+j
using namespace std;

int twoSum(vector<int>& nums, int start, int target) 
{
    int ans=-1;
    unordered_set<int>found;
    for(int i=start;i<nums.size();i++)
    {
        if(found.find(target-nums[i])!=found.end())
        {
            ans=nums[i]*(target-nums[i]);
            break;
        }
        else
            found.insert(nums[i]);
    }
    return ans;
}

int threeSum(vector<int>& nums, int target)
{
    int n=nums.size(),ans;
    for(int i=0;i<n;i++)
    {
        int rem=target-nums[i];
        int maybe=twoSum(nums,i+1,rem);
        if(maybe!=-1)
        {
            ans=nums[i]*maybe;
            break;
        }
    }
    return ans;
}

int main()
{
    #ifndef ONLINE_JUDGE
        freopen("../input.txt","r", stdin);
        freopen("../output.txt", "w", stdout);
    #endif
    std::ios::sync_with_stdio(false);
    cin.tie(NULL);
    vector<int>arr(200);
    for(int i=0;i<200;i++)
        cin>>arr[i];
    int prod=threeSum(arr,2020);
    cout<<prod<<endl;
    return 0;
}