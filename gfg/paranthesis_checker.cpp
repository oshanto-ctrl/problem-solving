/*
	Problem Link:
	https://www.geeksforgeeks.org/problems/parenthesis-checker2744/1

*/


class Solution
{
    public:
    
    bool validatePairs(char opening_bracket, char closing_bracket){
        if(opening_bracket == '(' && closing_bracket == ')') {
            return true;
        } else if(opening_bracket == '{' && closing_bracket == '}') {
            return true;
        } else if(opening_bracket == '[' && closing_bracket == ']') {
            return true;
        } else {
            return false;
        }
    }
    
    //Function to check if brackets are balanced or not.
    bool ispar(string x)
    {
        stack<char> charStack;
        int n = x.size();
        
        for(int i = 0; i < n; i++) {
            if(x[i] == '(' || x[i] == '{' || x[i] == '[') {
                charStack.push(x[i]);
            } else {
                if(charStack.empty()) {
                    return false;
                }
                
                if(validatePairs(charStack.top(), x[i])) {
                    charStack.pop();
                } else {
                    return false;
                }
            }
        }
        
        return charStack.empty();
    }

};