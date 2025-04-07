// Problem Link: https://codeforces.com/problemset/problem/1992/A
#include<bits/stdc++.h>
using namespace std;

int main(){

    int t;
    cin >> t;

    while(t--){
        int a, b, c;
        cin >> a >> b >> c;

        for(int i = 0; i < 5; i++){

            int check = min(a, min(b, c));

            if(a <= check){
                a++;
            }else if(b <= check){
                b++;
            }else{
                c++;
            }

        }

        cout << (a*b*c) << "\n";
    }


return 0;
}
