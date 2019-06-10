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
    int ladderLength(const string &beginWord, const string &endWord, vector<string>& wordList) 
    {
        int n = int(wordList.size());
        
        // target is endWord's index in wordList, if any
        int target = 0;
        while (target < n && wordList[target] != endWord) {
            ++target;
        }
        if (target == n) {
            // endWord not in wordList
            return 0;
        }
        
        std::unordered_map<string,int> wordIndexMap;
        for (int i = 0; i < n; ++i) {
            wordIndexMap[wordList[i]] = i;
        }

        vector<int> transformPosition(n, -1);
        
        std::queue<std::pair<int,int>> forwardQueue;
        vector<int> visited(n);
        
        // target_step will be greater than 0 when target found
        int target_step = 0;
        WordTransform wordTrans(&beginWord, -1);
        string nextWord;
        int currentPos = -1;
        while (wordTrans.nextWord(&nextWord, &currentPos)) {
            auto it = wordIndexMap.find(nextWord);
            if (it == wordIndexMap.end()) {
                continue;
            }
            int index = it->second;
            transformPosition[index] = currentPos;
            forwardQueue.push(make_pair(index, 2));
            visited[index] = 2;
            if (index == target) {
                target_step = 2;
                break;
            }
        }

        // target found
        if (target_step == 2) {
            return 2;
        }

        std::queue<std::pair<int,int>> backwardQueue;
        backwardQueue.push(make_pair(target, -1));
        visited[target] = -1;

        while (!forwardQueue.empty() && !backwardQueue.empty()) {
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
                        auto it = wordIndexMap.find(nextWord);
                        if (it == wordIndexMap.end()) {
                            continue;
                        }
                        int index = it->second;
                        if (visited[index] == 0) {
                            transformPosition[index] = currentPos;
                            visited[index] = step + 1;
                            forwardQueue.push(make_pair(index, step+1));
                        } else if (visited[index] < 0) {
                            // meet with backward friends
                            return step - visited[index];
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
                        auto it = wordIndexMap.find(nextWord);
                        if (it == wordIndexMap.end()) {
                            continue;
                        }
                        int index = it->second;
                        if (visited[index] == 0) {
                            transformPosition[index] = currentPos;
                            visited[index] = step - 1;
                            backwardQueue.push(make_pair(index, step-1));
                        } else if (visited[index] > 0) {
                            // meet with forward friends
                            return visited[index] - step;
                        }
                    }
                }
            }
        }

        return target_step;
    }
};

//#include "testcase.cpp"

int main()
{
    Solution su;
    string _beginWord = "hot", _endWord = "dot";
    vector<string> _wordList{"hot","dot"};
//    test('hot', 'dog', ['hot', 'dog'])
//    test('hit', 'cog', ["hot","dot","dog","lot","log","cog"])
//    test('hit', 'cog', ["hot","dot","dog","lot","log"])
//    test('hit', 'lod', ["hit","hot","lit","lot","lid","lod"])
    auto result = su.ladderLength(_beginWord, _endWord, _wordList);
    cout << result << endl;
    return 0;
}

