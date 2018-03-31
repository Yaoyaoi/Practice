#include <iostream>

using namespace std;

#define MAX 100005

long long Vs[MAX];
long long Ts[MAX];
long long melted[MAX];
long long SumT[MAX];
int P[MAX];

int main()
{
    
    int N;
    cin >> N;
    for (int i = 1;i <= N;i++){
        cin >> Vs[i];
    }
    for (int i = 0;i < N;i++){
        cin >> Ts[i];
        SumT[i+1] = SumT[i] + Ts[i];
    }
    
    for(int i = 1; i < N;i++){
        if(Vs[i]<=Ts[i-1]){
            melted[i]+=Vs[i];
            P[i]++;
            continue;
        }
        int l = i;
        int h = N+1;
        int m = (l+h)/2;
        while(l != m){
            if((SumT[m]-SumT[i-1])>=Vs[i]){
                h = m;
            }else l = m;
            m = (l+h)/2;
        }
        if(l+1<=N){
            melted[l+1] += Vs[i] + SumT[i-1] - SumT[l];
            P[l+1]++;
        }
//        for(int j = i;j <= l;j++){
//            melted[j]+=Ts[j-1];
//        }
    }
    int sumP = 0;
    for(int i = 1;i< N;i++){
        sumP += P[i];
        melted[i] += (i-sumP) * Ts[i-1];
    }
    sumP += P[N];
    melted[N] += (N - 1 - sumP) * Ts[N - 1];
    
    if(Vs[N]>Ts[N-1]){
        melted[N] += Ts[N-1];
    }else{
        melted[N]+=Vs[N];
    }
    for (int i = 1;i <= N;i++){
        cout << melted[i] << ' ';
    }
    return 0;
}