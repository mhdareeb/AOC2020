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

int sumProd(vector<int>arr, int start, int target)
{
    int n=arr.size(),left=start,right=n-1;
    while(left<right)
    {
        int sum=arr[left]+arr[right];
        if(sum==target)
            return arr[left]*arr[right];
        else if(sum<target)
            left++;
        else
            right--;
    }
    return -1;
}

int threeSum(vector<int>& nums, int target) 
{
    int first,second,third,ans;
    sort(nums.begin(),nums.end());
    for(int i=0;i<nums.size();i++)
    {
        int maybe=sumProd(nums,i+1,target-nums[i]);
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