#include<iostream>
using namespace std;

permu(long long x){
    if (x == 1 || x == 0){
        return 1;
    }

    return x*permu(x-1);
}

int main(){
    long long x = 30;
    cout<<permu(25);
    return 0;
}