#include <iostream>


using namespace std;


int main() {
    
    int noa[26] = {0};
    int noac[26] = {0};
    int flag[26] = {0};
    string s;
    int sum = 0;//子数列长度
    int len;//母数列长度
    
    cin >> s;
    len = s.length();
    for(int i = 0;i < 26; i++){
        cin >> noa[i];
        sum += noa[i];
    }
    if(sum > len){
        cout << "No" <<endl;
        return 0;
    }
    
    for(int i = 0;i < sum;i++){
        noac[s[i] - 97]++;
    }
    for (int i = 0;i < 26;i++){
        if(noa[i] != noac[i]){
            flag[i] = 1;
        }
    }
    if(!(flag[0]|flag[1]|flag[2]|flag[3]|flag[4]|flag[5]|flag[6]|flag[7]|flag[8]|flag[9]|flag[10]|flag[11]|flag[12]|flag[13]|flag[14]|flag[15]|flag[16]|flag[17]|flag[18]|flag[19]|flag[20]|flag[21]|flag[22]|flag[23]|flag[24]|flag[25])){
        cout << "Yes" <<endl;
        return 0;
    }
    
    if(sum == len){
        cout << "No" <<endl;
        return 0;
    }
    
    for (int i = 1;i < (len - sum + 1);i++){
        int l = s[i-1] - 97;
        int r = s[sum + i - 1] - 97;
        noac[l]--;
        noac[r]++;
        if(noac[l]==noa[l]){
            flag[l] = 0;
        }else flag[l] = 1;
        if(noac[r]==noa[r]){
            flag[r] = 0;
        }else flag[r] = 1;
        if(!(flag[0]|flag[1]|flag[2]|flag[3]|flag[4]|flag[5]|flag[6]|flag[7]|flag[8]|flag[9]|flag[10]|flag[11]|flag[12]|flag[13]|flag[14]|flag[15]|flag[16]|flag[17]|flag[18]|flag[19]|flag[20]|flag[21]|flag[22]|flag[23]|flag[24]|flag[25])){
            cout << "Yes" <<endl;
            return 0;
        }
    }
            
    cout << "No" << endl;

return 0;
}