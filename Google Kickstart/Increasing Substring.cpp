// # https://codingcompetitions.withgoogle.com/kickstart/round/0000000000435a5b/000000000077a882

#include<bits/stdc++.h>
using namespace std;

void solve(){
	int n;
	string s;
	cin >> n;
	cin >> s;
	vector<int> answer(n, 0);
	for(int i = 0; i < n; i++){
		int ans = 1;
		for(int j = i - 1; j >=0; j--){
			if(s[j] < s[j+1]){
				ans++;
			}
			else{
				break;
			}
		}
		answer[i] = ans;
	}
	for(auto a: answer){
		cout << a << " ";
	}
	cout << endl;
}

int main(){
	int t, yolo = 1;
	cin >> t;
	while(t--){
		cout << "Case #" << yolo << ": ";
		solve();
		yolo++;
	}
	
	return 0;
}