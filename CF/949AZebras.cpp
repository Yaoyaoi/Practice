#include <iostream>
#include<cstring>
#include <vector>


using namespace std;
const int N = 200002;
char s[N];

vector <int> ans[N];



int main() {

    scanf("%s", s+1);
    int len = strlen(s+1);
    int zlp = 0;
    int olp = 0;

    for (int i = 1; i <= len; i++){
        if(s[i] == '0'){
            ans[++zlp].push_back(i);
        }else{
            if(!zlp){
                cout << -1 << endl;
                return 0;
            }
            ans[zlp--].push_back(i);
        }
        olp = max(zlp,olp);
    }
    if (zlp != olp){
        cout << -1 << endl;
        return 0;
    }
    cout << zlp << endl;
    for (int i = 1;i <= zlp; i++){
        cout << ans[i].size();
        for(int j = 0;j < ans[i].size(); j++){
            cout << ' ' << ans[i][j];
        }
        cout << endl;
    }

    return 0;
}

