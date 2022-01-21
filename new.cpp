#include<vector>
#include<iostream>
using namespace std;

class NodeKen{
	private:
		bool restricted = true;
	public:
		int size = 22;
		NodeKen* next;
		NodeKen* prev;
		NodeKen* left;
		NodeKen* right;
};

int receding_zeroes(int n, vector<int> nums){
	vector<int> vec1; 
	for (int n = 0; n < nums.size()-1; n ++;){
		if (n == nums[n]){
			vec1.push_back((n*nums[n])//n);
			cout<<n<<" Went In";
		}
		else{
			cout<<'Nope';
		}
	}
}

int main(){
	
	return 0;
}

