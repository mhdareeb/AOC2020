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

long long int findWeakness(vector<long long int>& nums, int idx)
{
    long long int target=nums[idx],sum=0,ans;
    int i=0,j=0;
    while(sum!=target)
    {
        while(j<idx && sum<target)
            sum+=nums[j++];
        while(i<idx && sum>target)
            sum-=nums[i++];
    }
    long long int smallest=*min_element(range(nums,i,j));
    long long int largest=*max_element(range(nums,i,j));
    ans=smallest+largest;
    return ans;
}

bool twoSum(vector<long long int>& nums, int idx)
{    
    unordered_set<long long int>uset;
    for(int i=idx-25;i<idx;i++)
    {
        if((uset.find(nums[idx]-nums[i])!=uset.end()) && (nums[idx]!=2*nums[i]))
            return true;
        uset.insert(nums[i]);
    }    
    return false;
}

int main()
{
    #ifndef ONLINE_JUDGE
        freopen("../input.txt","r", stdin);
        freopen("../output.txt", "w", stdout);
    #endif
    std::ios::sync_with_stdio(false);
    cin.tie(NULL);
    vector<long long int>arr(1000);
    int firstWrong;
    long long int weakness;
    for(int i=0;i<1000;i++)
        cin>>arr[i];
    for(int i=25;i<1000;i++)
    {
        if(!twoSum(arr,i))
        {
            firstWrong=i;
            break;
        }
    }
    cout<<arr[firstWrong]<<endl;
    weakness=findWeakness(arr,firstWrong);
    cout<<weakness<<endl;
    return 0;
}