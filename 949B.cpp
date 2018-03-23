#include <iostream>


using namespace std;


long n;
int q;

int main() {
    cin >> n;
    cin >> q;
    for(int i = 0;i < q;i++){
        int temp;
        cin >> temp;
        if (temp < (n + 1) / 2){
            cout << temp * 2 -1 << endl;
        }else {
            cout << "没想好呢，为了保住绿点先commit一下" << endl;
        }
    }


    return 0;
}