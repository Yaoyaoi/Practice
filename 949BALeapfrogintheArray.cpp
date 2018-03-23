#include <iostream>


using namespace std;


long long n;
int q;
int main() {
    cin >> n;
    cin >> q;
    for(int i = 0;i < q;i++){
        long long t;
        cin >> t;
        if (t%2){
            cout << (t + 1)/2 << endl;
        }else {
            do{t+=(n-t/2);}while(!(t%2));
            cout << (t + 1)/2 << endl;
        }

    }

return 0;
}