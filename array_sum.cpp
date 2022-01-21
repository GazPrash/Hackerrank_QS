#include<iostream>
#include<vector>
using namespace std;

int simpleArraySum(vector<int> ar) {
    int sum = 0;
    for (unsigned int i = 0; i < ar.size(); i++)
    {
        sum += ar[i];
    }
    
    return sum;
}


int main(){
    vector<int> vec = {1, 4, 2, 2, 2};

    cout<<simpleArraySum(vec);
    
    return 0;
}