#include <iostream>
#include <cstring>
#include <vector>
//#include <queue>

using namespace std;

vector<int>rows[51];
vector<int>columns[51];
//queue<int>row;
//queue<int>column;


int main() {
    int n,m;
    cin >> n;
    cin >> m;
    char cell;
    for (int i = 1; i <= n; i++){
        //rows[i].push_back(0);
        for(int j = 1; j <= m; j++){
            //if(i == 1)columns[j].push_back(0);
            cin >> cell;
            if(cell == '#'){
                rows[i].push_back(j);
                columns[j].push_back(i);
            }
        }
    }

    for (int i = 1; i <= n; i++){
        if(!rows[i].size())continue;
        //rows[i][0] = 1;
        int columnlist[50];
        int colcount = 0;
        while(rows[i].size()){
            //int tempcolumn = rows[i].back();
            //cout << tempcolumn << " ";
            columnlist[colcount] = rows[i].back();
            colcount++;
            //column.push(tempcolumn);
            rows[i].pop_back();
        }
        //cout << endl;
        for(int k = 0;k < colcount; k++){
            int j = columnlist[k];
            while(columns[j].size()){
                int temprow = columns[j].back();
                columns[j].pop_back();
                if(!rows[temprow].size())continue;
                if (rows[temprow].size() == colcount){
                    while(rows[temprow].size()){
                        if(rows[temprow].back() != columnlist[colcount-rows[temprow].size()]){
                            cout << "No" << endl;
                            return 0;
                        }
                        rows[temprow].pop_back();
                    }
                }else {
                    cout << "No" << endl;
                    return 0;
                }
            }
        }
    }
    cout << "Yes" << endl;

    return 0;
}