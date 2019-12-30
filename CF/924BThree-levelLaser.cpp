#include <iostream>

using namespace std;

bool compare(pair<int, int>p1, pair<int, int>p2);

int main(){
    long long E[100005];
    int n;
    long long U;
    pair<int, int>yita;
    cin >> n;
    cin >> U;
    
    for(int i = 0; i < n; i++)cin >> E[i];
    
    yita.first = 1;
    yita.second = 0;
    
    for (int i = 0; i < (n - 2); i++){
        int j = i + 1;
        int low = i + 2;
        int high = n;
        if(E[low] - E[i] > U)continue;
        int mid = (high + low) / 2;
        while (mid != low) {
            if(E[mid] - E[i] == U)break;
            if(E[mid] - E[i] > U){
                high = mid;
            }else low = mid;
            mid = (high + low) / 2;
        }
        int k = mid;
        if (compare(yita, make_pair(E[k] - E[i], E[k] - E[j])) == true){
            yita = make_pair(E[k] - E[i], E[k] - E[j]);
        }
    }
    if(yita.second == 0){
        cout << -1 << endl;
    }else printf("%.10lf\n",1.0 * yita.second / yita.first);
    return 0;
}

bool compare(pair<int, int>p1, pair<int, int>p2)
{
    return (long long)p1.second*p2.first <= (long long)p2.second*p1.first;
}

