#include <iostream>
#include <math.h>
//#include <cstring>
//#include <vector>
//#include <queue>
using namespace std;

int main(){
    int hh,mm;
    int H,D,C,N;
    int minto20;
    cin >> hh;
    cin >> mm;
    cin >> H;
    cin >> D;
    cin >> C;
    cin >> N;
    
    if(hh >= 20){
        cout << C * 0.8 * ceil(1.0 * H / N) << endl;
        return 0;
    }
    if(mm){
        hh++;
        mm = 60 - mm;
    }
    minto20 = (20 - hh) * 60 + mm;
    int Cbefore = C * ceil(1.0 * H / N);
    double Cafter = C * 0.8 * ceil(1.0 * (H + D * minto20)/ N);
    if(Cafter - Cbefore <= 0.000000){
        cout << Cafter << endl;
        return 0;
    }
    cout << Cbefore << endl;
    return 0;
}

