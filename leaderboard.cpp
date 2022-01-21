#include <iostream>
#include <vector>
using namespace std;

int binarySearchModified(vector<int> &ranked, int score){
    int low = 0, high = ranked.size()-1;

    while (low <= high){
        int mid = (low+high)/2;
        if (score == ranked[mid]){
            return mid;
        }
        else if (score > ranked[mid] && score < ranked[mid-1]){
            return mid;
        }
        else if (score < ranked[mid] && score > ranked[mid+1]){
            return mid+1;
        }
        else if (score > ranked[mid]){
            high = mid-1;
        }
        else if (score < ranked[mid]){
            low = mid+1;
        }
    }

    return -1;
}

vector<int> climbingLeaderboard(vector<int> ranked, vector<int> player)
{
    vector<int> alice_ranks;
    vector<int> global_ranks;
    int n = ranked.size();   // NO. OF PLAYERS IN THE LEADERBOARD  
    global_ranks.push_back(1);
    
    int rank_ = 1;
    for (int i = 1; i < n; i++)
    {
        if (ranked[i-1] == ranked[i])
        {
            global_ranks.push_back(rank_);
        }
        else
        {
            global_ranks.push_back(++rank_);
        }
        
    }

    for (int j = 0; j < player.size(); j++)
    {
        if (player[j] > ranked[0]){
            alice_ranks.push_back(1);
        }
        else if (player[j] < ranked[n-1]){
            alice_ranks.push_back(global_ranks[n-1]+1);
        }
        else{
            int returned_ind = binarySearchModified(ranked, player[j]);
            alice_ranks.push_back(global_ranks[returned_ind]);
        }
    }

    return alice_ranks;
    

}

int main()
{
    vector<int> a1 = {100, 100, 50, 40, 40, 20, 10};
    vector<int> a2 = {5, 25, 50, 120};
    vector<int> alice = climbingLeaderboard(a1, a2);

    for (int i = 0; i < alice.size(); i++)
    {   
        cout << alice[i] << endl;
    }

    return 0;
}