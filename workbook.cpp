#include<iostream>
#include<vector>

int workbook(int n, int k, vector<int> arr) {
	int spp = 0, page_on = 1;
	
	for (int i=0; i < arr.size();i++){
		int ratio = 1;
		for (int j =0; j<=arr[i];j++){
			if (j <= ratio*k){
				if (j == page_on){
					spp++;
				}
				
			}
			else{
				page_on++;
				if (j==page_on){
					spp++;
				}
				ratio++;
			}
		}
		page_on++;
	}
	
	return spp;
}


int main(){


}