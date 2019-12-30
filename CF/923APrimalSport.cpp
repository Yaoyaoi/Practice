#include <iostream>

using namespace std;

#define MAX 1000005

int GPF[MAX];

int main()
{
    int X2;
    cin >> X2;
    for(int i = 2; i < X2; i++){
        if(GPF[i])continue;
        for(int j = i + i; j <= X2; j += i){
            GPF[j] = i;
        }
    }
    
    int X1min = X2 - GPF[X2] + 1;
    int X0 = X1min;
    for(int X1 = X1min;X1 <= X2 - 1; X1++){
        if(!GPF[X1])continue;
        int tX = X1 - GPF[X1] + 1;
        if(tX < X0)X0 = tX;
    }
    cout << X0 << endl;
    return 0;
}
