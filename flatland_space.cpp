#include<iostream>
#include<vector>
#include <cstdlib>
#include<algorithm>
using namespace std;

int flatlandSpaceStations(int n, vector<int> c) {
    vector<int> cities;
    int n = c.size();
    for (int i = 0; i < n; i++)
    {
        cities.push_back(i);
    }

    vector<int> distance;

    for (int i = 0; i < cities.size(); i++)
    {
        for (int j = 0; j < n; j++)
        {
            distance.push_back(abs(cities[i]-j));
            

             
        }
        
    }

// sure i just felt like singing innit
    


    
}

int main(){
    
    return 0;
}