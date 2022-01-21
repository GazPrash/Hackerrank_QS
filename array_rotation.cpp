#include<bits/stdc++.h>
using namespace std;

vector<int> circularArrayRotation(vector<int> a, int k, vector<int> queries)
{
    // rotation of the array
    k %= a.size();
    int i = a.size()-k, counter = 0;
    vector<int> vec;
    
    if (a.size() == 1) return {0};

    if (k == 0){
        for (int i = 0; i < a.size(); i++)
        {
            vec.push_back(i);
        }
        return vec;
    }

    while (counter < a.size()){
        vec.push_back(a[i]);
        i = (i+1)%a.size();
        counter++;
    }

    vector<int> ans;

    for (int l = 0; l < queries.size(); l++)
    {
        ans.push_back(vec[queries[l]]);
    }
    
    return ans;

}

int main(){
    
    return 0;
}