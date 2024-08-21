#include<bits/stdc++.h>
using namespace std;

typedef long long ll;

int main() {
    /* 
        problem link:
        https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/favourite-singer-a18e086a/
    */
   ll n;
   cin >> n;

   int arr[n+2];
   
   for(int i = 0; i < n; i++){
       cin >> arr[i];
   }
   
   sort(arr, arr+n);

   int max_freq = 0; int current_freq = 1; int count = 0;

   for(int i = 1; i < n; i++) {
    
    if(arr[i] == arr[i-1]) {
        current_freq++; // count of current item in arr
    } else {
        if(current_freq > max_freq) {
            max_freq = current_freq;
            count = 1; // reset the count
        } else if(current_freq == max_freq) {
            count++;
        }
        current_freq = 1; // reset value for new item in arr
    }
   }

    if(current_freq > max_freq) {
        count = 1;
    } else if(current_freq == max_freq) {
        count++;
    }

    cout << count << "\n";
    
    return 0;
}

/*
// #1 Attempt: Partially Accepted.

#include<bits/stdc++.h>
using namespace std;

typedef long long ll;

int main(){
	ll n;
	cin >> n;

	vector<int> arr(n+1);

	for(ll i = 0; i < n; i++){
		cin >> arr[i];
	}

	unordered_map<ll, ll>mp;

	for(ll num : arr){
		mp[num]++;
	}

	ll max_freq_count = 0;

	for(const auto& i : mp) {
		max_freq_count = max(max_freq_count, i.second);
	}

	ll res = 0;

	for(cont auto& i : mp) {
		if(i.second == max_freq_count) {
			res++;
		}
	}

	cout << res << "\n";

	return 0;
}
*/