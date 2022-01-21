#include <bits/stdc++.h>

using namespace std;

string ltrim(const string &);
string rtrim(const string &);

/*
 * Complete the 'stones' function below.
 *
 * The function is expected to return an INTEGER_ARRAY.
 * The function accepts following parameters:
 *  1. INTEGER n
 *  2. INTEGER a
 *  3. INTEGER b
 */

vector<int> stones(int n, int a, int b) {
	vector<int> vec_ans
	for (int x = 0; x < n; x++){
		vec_ans.push_back(((n-1)-x)*(a) + (x)*b);
	}
	
	return sort(vec_ans.begin(), vec_ans.end());

}


int main(){

}