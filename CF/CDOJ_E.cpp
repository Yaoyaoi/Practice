#include <iostream>

using namespace std;


int main() {
    int T;

    cin >> T;
    for (int j = 0;j < T;j++){
        int N;
        int zerocount = 0;
        int onecount = 0;

        cin >> N;

        for(int i = 0;i < N;i++){
            char temp;
            cin >> temp;
            if(temp == '1'){
                if(zerocount){
                    zerocount--;
                }else {
                    onecount++;
                }
            }else{
                zerocount++;
            }
        }
        printf("%.3f\n",(double)(onecount+zerocount));
    }
    
    
    return 0;
}