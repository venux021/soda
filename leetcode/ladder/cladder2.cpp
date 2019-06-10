#include <iostream>
#include <string>
#include <vector>
#include <queue>
#include <unordered_set>
#include <unordered_map>
using namespace std;

struct WordTransform {
    const string &originalWord;
    string wbuf;
    const int skipPos;
    int pos, end;
    int current_char;

    WordTransform(const string *word, int skipPos) :
        originalWord{*word}, wbuf{*word}, skipPos{skipPos},
        pos{0}, end{int(word->size())}, current_char{'a'}
    {
        if (pos == skipPos) {
            ++pos;
        }
    }

    bool nextWord(string *nxString, int *current_pos) {
        if (pos >= end) {
            return false;
        }

        if (current_char == originalWord[pos]) {
            ++current_char;
            if (current_char > 'z') {
                wbuf[pos] = originalWord[pos];
                ++pos;
                if (pos == skipPos) {
                    ++pos;
                }
                if (pos >= end) {
                    return false;
                }
                current_char = 'a';
            }
        }
        
        wbuf[pos] = current_char;
        *nxString = wbuf;
        *current_pos = pos;

        ++current_char;
        if (current_char > 'z') {
            wbuf[pos] = originalWord[pos];
            ++pos;
            if (pos == skipPos) {
                ++pos;
            }
            current_char = 'a';
        }

        return true;
    }
};

class Solution {
public:
    vector<vector<string>> findLadders(const string &beginWord, const string &endWord, vector<string>& wordList) 
    {
        int n = int(wordList.size());
        vector<vector<string>> results;
        
        // target is endWord's index in wordList, if any
        int target = 0;
        while (target < n && wordList[target] != endWord) {
            ++target;
        }
        if (target == n) {
            // endWord not in wordList
            return results;
        }
        
        std::unordered_map<string,int> wordIndexMap;
        for (int i = 0; i < n; ++i) {
            wordIndexMap[wordList[i]] = i;
        }

        vector<int> transformPosition(n, -1);
        
        std::queue<std::pair<int,int>> forwardQueue;
        vector<int> visited(n);
        vector<vector<int>> prev_record(n);
        
        // target_step will be greater than 0 when target found
        int target_step = 0;
int counter = 0;
unordered_map<string,int> testCount;
        WordTransform wordTrans(&beginWord, -1);
        string nextWord;
        int currentPos = -1;
        while (wordTrans.nextWord(&nextWord, &currentPos)) {
++testCount[beginWord];
            auto it = wordIndexMap.find(nextWord);
            if (it == wordIndexMap.end()) {
                continue;
            }
            int index = it->second;
            transformPosition[index] = currentPos;
            forwardQueue.push(make_pair(index, 2));
            visited[index] = 2;
            prev_record[index].push_back(-1);
            if (index == target) {
                target_step = 2;
                break;
            }
        }

        // target found
        if (target_step == 2) {
            vector<int> path(2);
            collectPath(beginWord, target, prev_record, wordList, path, target_step, results);
            return results;
        }

        std::queue<std::pair<int,int>> backwardQueue;
        backwardQueue.push(make_pair(target, -1));
        visited[target] = -1;

        bool meet = false;
        while (!meet && !forwardQueue.empty() && !backwardQueue.empty()) {
            int forwardSize = int(forwardQueue.size());
            int backwardSize = int(backwardQueue.size());
            if (forwardSize <= backwardSize) {
                while (forwardSize > 0) {
                    auto _f = forwardQueue.front();
                    forwardQueue.pop();
                    int front = _f.first, step = _f.second;
                    --forwardSize;

                    int skipPos = transformPosition[front];
                    WordTransform wTrans(&wordList[front], skipPos);
                    string nextWord;
                    int currentPos = -1;
                    while (wTrans.nextWord(&nextWord, &currentPos)) {
++testCount[wordList[front]];
                        auto it = wordIndexMap.find(nextWord);
                        if (it == wordIndexMap.end()) {
                            continue;
                        }
                        int index = it->second;
                        if (visited[index] == 0) {
                            transformPosition[index] = currentPos;
                            visited[index] = step + 1;
                            prev_record[index].push_back(front);
                            forwardQueue.push(make_pair(index, step+1));
                        } else if (visited[index] > step) {
                            // searched by other node in the level {step}
                            // converged from more than 1 path
                            prev_record[index].push_back(front);
                        } else if (visited[index] < 0) {
                            // meet with backward friends
                            meet = true;
                            target_step = step - visited[index];
                            prev_record[index].push_back(front);
                        }
                    }
                }
            } else {
                // forwardSize > backwardSize
                while (backwardSize > 0) {
                    // !! ATTENTION !!
                    // step is negative integer
                    auto _f = backwardQueue.front();
                    backwardQueue.pop();
                    int front = _f.first, step = _f.second;
                    --backwardSize;

                    int skipPos = transformPosition[front];
                    WordTransform wTrans(&wordList[front], skipPos);
                    string nextWord;
                    int currentPos = -1;
                    while (wTrans.nextWord(&nextWord, &currentPos)) {
++testCount[wordList[front]];
                        auto it = wordIndexMap.find(nextWord);
                        if (it == wordIndexMap.end()) {
                            continue;
                        }
                        int index = it->second;
                        if (visited[index] == 0) {
                            transformPosition[index] = currentPos;
                            visited[index] = step - 1;
                            prev_record[front].push_back(index);
                            backwardQueue.push(make_pair(index, step-1));
                        } else if (visited[index] < step) {
                            // searched by other node in the level {step}
                            // converged from more than 1 path
                            prev_record[front].push_back(index);
                        } else if (visited[index] > 0) {
                            // meet with forward friends
                            meet = true;
                            target_step = visited[index] - step;
                            prev_record[front].push_back(index);
                        }
                    }
                }
            }
        }

cout << "counter: " << counter << endl;
int __total_count = 0;
for (auto &p : testCount) {
//    cout << p.first << ": " << p.second << endl;
    __total_count += p.second;
}
cout << "total: " << __total_count <<endl;
        if (target_step == 0) {
            // no path found
            return results;
        }
        
        vector<int> path(target_step);
        collectPath(beginWord, target, prev_record, wordList, path, target_step, results);
        return results;
    }
    
    void collectPath(
        const string &beginWord, int target, 
        const vector<vector<int>> &prev_record,
        const vector<string> &wordList, vector<int> &path, 
        int step, vector<vector<string>> &results)
    {
        if (target == -1) {
            vector<string> rpath(path.size());
            rpath[0] = beginWord;
            for (int i = 1; i < int(path.size()); ++i) {
                rpath[i] = wordList[path[i]];
            }
            results.push_back(rpath);
            return;
        }
        
        path[step-1] = target;
        for (int i : prev_record[target]) {
            collectPath(beginWord, i, prev_record, wordList, path, step-1, results);
        }
    }
};

//#include "testcase.cpp"

int main()
{
    Solution su;
    string _beginWord = "hit", _endWord = "lod";
    vector<string> _wordList{"hit","hot","lit","lot","lid","lod"};
//    test('hot', 'dog', ['hot', 'dog'])
//    test('hit', 'cog', ["hot","dot","dog","lot","log","cog"])
//    test('hit', 'cog', ["hot","dot","dog","lot","log"])
//    test('hit', 'lod', ["hit","hot","lit","lot","lid","lod"])
    auto result = su.findLadders(_beginWord, _endWord, _wordList);
    for (const auto &words : result) {
        for (const string &w : words) {
            cout << w << ' ';
        }
        cout << endl;
    }
    return 0;
}

