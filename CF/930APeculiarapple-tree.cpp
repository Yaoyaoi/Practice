#include <iostream>

using namespace std;

#define MAX 100005


int main()
{
    int noi;
    cin >> noi;
    int sum = 0;
    int structure[MAX] = {0};
    int apples[MAX] = {1};
    int turns[MAX] = {0};
    int lturn = 1;
    for (int i = 2;i <= noi; i++){
        cin >> structure[i];
        int turn = turns[structure[i]] + 1;
        turns[i] = turn;
        if(turn > lturn)lturn = turn;
        apples[turn] = ~apples[turn] + 2;
    }
    for(int i = 0; i <= lturn; i++){
        sum += apples[i];
    }
    cout << sum << endl;
    return 0;
}
