#!/usr/bin/env python3
from collections import deque
import json
import sys
import time
import string

from sodacomm.tools import testwrapper

def all_possible_transformed_words(word, skipPos):
    wbuf = list(word)
    for i in range(len(wbuf)):
        if i == skipPos:
            continue
        for ch in string.ascii_lowercase:
            if ch == word[i]:
                continue
            wbuf[i] = ch
            nextWord = ''.join(wbuf)
            yield (i, nextWord)
        wbuf[i] = word[i]

def findLadders3(beginWord, endWord, wordList):
    n = len(wordList)
    results = []

    # target is endWord's index in wordList, if any
    target = 0
    while target < n and wordList[target] != endWord:
        target += 1
    if target == n: # endWord not in wordList
        return results

    wordIndexMap = {}
    for i, word in enumerate(wordList):
        wordIndexMap[word] = i

    transformPosition = [-1] * n

    forwardQueue = deque()
    visited = [0] * n
    prev_record = [[] for i in range(n)]

    target_step = 0

    __counter = {}

    for pos, nextWord in all_possible_transformed_words(beginWord, -1):
        index = wordIndexMap.get(nextWord)
        __counter[beginWord] = __counter.get(beginWord, 0) + 1
        if index is None:
            continue
        transformPosition[index] = pos
        forwardQueue.append((index, 2))
        visited[index] = 2
        prev_record[index].append(-1)
        if index == target:
            target_step = 2
            break

    # target found
    if target_step == 2:
        path = [None, None]
        collectPath2(beginWord, target, prev_record, wordList, path, target_step, results)
        return results

    # initialize backward queue
    backwardQueue = deque()
    backwardQueue.append((target, -1))
    visited[target] = -1

    meet = False
    while not meet and forwardQueue and backwardQueue:
        forwardSize = len(forwardQueue)
        backwardSize = len(backwardQueue)
        if forwardSize <= backwardSize:
            while forwardSize > 0:
                front, step = forwardQueue.popleft()
                forwardSize -= 1
                skipPos = transformPosition[front]
                for pos, nextWord in all_possible_transformed_words(wordList[front], skipPos):
                    index = wordIndexMap.get(nextWord)
                    __counter[wordList[front]] = __counter.get(wordList[front], 0) + 1
                    if index is None:
                        continue
                    if visited[index] == 0:
                        transformPosition[index] = pos
                        visited[index] = step + 1
                        prev_record[index].append(front)
                        forwardQueue.append((index, step+1))
                    elif visited[index] > step:
                        # searched by other node in the level {step}
                        # converged from more than 1 path
                        prev_record[index].append(front)
                    elif visited[index] < 0:
                        # meet with backward friends
                        meet = True
                        target_step = step - visited[index]
                        prev_record[index].append(front)
        else:
            # forwardSize > backwardSize
            while backwardSize > 0:
                # !! ATTENTION !!
                # step is negative integer
                front, step = backwardQueue.popleft()
                backwardSize -= 1
                skipPos = transformPosition[front]
                for pos, nextWord in all_possible_transformed_words(wordList[front], skipPos):
                    index = wordIndexMap.get(nextWord)
                    __counter[wordList[front]] = __counter.get(wordList[front], 0) + 1
                    if index is None:
                        continue
                    if visited[index] == 0:
                        transformPosition[index] = pos
                        visited[index] = step - 1
                        prev_record[front].append(index)
                        backwardQueue.append((index, step-1))
                    elif visited[index] < step:
                        # searched by other node in the level {step}
                        # converged from more than 1 path
                        prev_record[front].append(index)
                    elif visited[index] > 0:
                        # meet with forward friends
                        meet = True
                        target_step = visited[index] - step
                        prev_record[front].append(index)

    print(sum(__counter.values()))

    if target_step == 0:
        # no available path found
        return results

    path = [None] * target_step
    collectPath2(beginWord, target, prev_record, wordList, path, target_step, results)
    return results

def collectPath2(beginWord, target, prev_record, wordList, path, step, results):
    if target == -1:
        rpath = [None] * len(path)
        rpath[0] = beginWord
        for i in range(1, len(path)):
            rpath[i] = wordList[path[i]]
        results.append(rpath)
        return

    path[step-1] = target
    for i in prev_record[target]:
        collectPath2(beginWord, i, prev_record, wordList, path, step-1, results)

@testwrapper
def test(b, e, List):
#    print(b, e, List)
#    tb = time.time()
#    print(findLadders2(b, e, List))
#    print(f'time of 2: {time.time() - tb}')
#    tb = time.time()
    print(findLadders3(b, e, List))
#    print(f'time of 3: {time.time() - tb}')

def main():
#    test('hot', 'dog', ['hot', 'dog'])
#    test('hit', 'cog', ["hot","dot","dog","lot","log","cog"])
#    test('hit', 'cog', ["hot","dot","dog","lot","log"])
#    test('hit', 'lod', ["hit","hot","lit","lot","lid","lod"])
    from mytestcase import _beginWord, _endWord, _wordList
    test(_beginWord, _endWord, _wordList)

if __name__ == '__main__':
    main()
