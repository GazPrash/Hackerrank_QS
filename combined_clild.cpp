#include<iostream>
#include<vector>
using namespace std;


int dynamic(string s1, string s2, int i, int j){



}

int commonChild(string s1, string s2){
    // in my life i loved you moreee
    // anyways

    int n1 = s1.length();
    int n2 = s2.length();
    int arr[n1+1][n2+1] = {0};

    for (int i = 0; i < n1; ++i)
    {
        for (int j = 0; j < n2; ++j)
        {
            if (s1[i-1] == s2[j-1]){
                arr[i][j] = 1 + arr[i-1][j-1];    
            }
            else
            {
                arr[i][j] = max(arr[i-1][j], arr[i][j-1]);
            }
        }
        
    }

    return arr[n1][n2];
    


}

int main(){
    string s1 = " d", s2 = "s d";
    
    
    commonChild(s1, s2);
    return 0;
}