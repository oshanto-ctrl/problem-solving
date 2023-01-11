
// https://codeforces.com/contest/1703/problem/B

#include<bits/stdc++.h>
using namespace std;

int get_ans(string str){

    unordered_map<char, int> mp;

    for(int i = 0; str[i]; i++){
        if(mp.find(str[i]) == mp.end()){
            mp.insert(make_pair(str[i], 1));
        }else{
            mp[str[i]]++;
        }
    }
    int result = 0;

    for(auto& it : mp){
        it.second += 1;
        result += it.second;
    }

    return result;
}




// driver

int main(){
    int t;
    cin >> t;

    while(t--){
        int n;
        string str;

        cin >> n;
        cin >> str;

        int result = 0;
        result = get_ans(str);
        cout << result << "\n";
    }


return 0;
}
