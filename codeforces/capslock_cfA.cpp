
// https://codeforces.com/contest/131/problem/A

#include<bits/stdc++.h>
using namespace std;


bool all_upper_exp_one(string str){
    bool check = false;

    for(int i = 1; i < str.size(); i++){
        if(isupper(str[i])){
            check = true;
        }else{
            check = false; break;
        }
    }

    return check;

}


// driver
int main(){

string str;
    cin >> str;

    if( islower(str[0]) && all_upper_exp_one(str)){

        str[0] = toupper(str[0]);

        for(int i = 1; i < str.size(); i++){
            str[i] = tolower(str[i]);
        }

        cout << str << "\n";
    }else if(str.size() == 1 && islower(str[0])){
        str[0] = toupper(str[0]);
        cout << str << "\n";
    }else if(isupper(str[0]) && all_upper_exp_one(str)){
        for(int i = 0; i < str.size(); i++){
            str[i] = tolower(str[i]);
        }

        cout << str << "\n";
    }else if(str.size() == 1 && isupper(str[0])){
        str[0] = tolower(str[0]);
        cout << str << "\n";
    }else{
            cout << str << "\n";
    }


return 0;
}
