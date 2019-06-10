#include <iostream>
#include <string>
#include <vector>
using namespace std;

struct Record {
    vector<int> cuts;
    int maxCut{0};
};

class Solution {
public:
    vector<vector<string>> partition(string s) {
        vector<vector<string>> results;
        int n = int(s.size());
        if (n == 0) {
            return results;
        }
        
        vector<vector<char>> isp(n, vector<char>(n));
        vector<Record> part(n+1);
        
        for (int i = n-1; i >= 0; --i) {
            for (int j = i; j < n; ++j) {
                if (s[i] == s[j] && (j-i<2 || isp[i+1][j-1])) {
                    isp[i][j] = 1;
                    part[i].cuts.push_back(j+1);
                    part[i].maxCut = std::max(part[i].maxCut, part[j+1].maxCut + 1);
                }
            }
        }

        vector<int> path(part[0].maxCut);
        collect(s, part, 0, path, 0, results);
        return results;
    }

    void collect(
            const string &s, const vector<Record> &dp, int i,
            vector<int> &path, int k, vector<vector<string>> &results)
    {
        if (i == int(s.size())) {
            results.emplace_back();
            auto &strList = results.back();
            for (int x = 0, p = 0; x < k; p = path[x++]) {
                strList.emplace_back(s.begin()+p, s.begin()+path[x]);
            }
            return;
        }

        for (int p: dp[i].cuts) {
            path[k] = p;
            collect(s, dp, p, path, k+1, results);
        }
    }
};

int main()
{
    Solution su;
//    string s = "abbacab";
//    string s = "fddsdfasdfsddsadsdfadsdfasdfasdfaasdfafsdfsdadfasdfasdfasdfaddfdasdffdfasdfaasd";
    string s = "vdsfsacxvsadfazzdfsdvzsddzcvddas";
    auto result = su.partition(s);
    for (auto &r : result) {
        for (auto &s : r) {
            cout << s << ' ';
        }
        cout << endl;
    }
    return 0;
}
