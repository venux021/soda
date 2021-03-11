package main

import "encoding/json"
import "fmt"

import _ "soda/leetcode"
import "soda/unittest"
import "soda/util"

type TopVotedCandidate struct {
    N int
    times []int
    winner []int
}

func (this *TopVotedCandidate) initialize(persons []int) {
    counter := make([]int, this.N+1)
    win := 0
    for i := 0; i < this.N; i++ {
        counter[persons[i]]++
        if counter[persons[i]] >= counter[win] {
            win = persons[i]
        }
        this.winner[i] = win
    }
}

func Constructor(persons []int, times []int) TopVotedCandidate {
    var tvc TopVotedCandidate
    tvc.N = len(persons)
    tvc.times = times
    tvc.winner = make([]int, tvc.N)
    tvc.initialize(persons)
    return tvc
}


func (this *TopVotedCandidate) Q(t int) int {
    if t >= this.times[len(this.times)-1] {
        return this.winner[len(this.times)-1]
    }
    low, high := 0, this.N - 1
    for low < high {
        mid := (low + high) / 2
        if t <= this.times[mid] {
            high = mid
        } else {
            low = mid + 1
        }
    }
    if t == this.times[low] {
        return this.winner[low]
    } else {
        return this.winner[low-1]
    }
}

type Params struct {
    persons []int
    times []int
    qs []int
}

// func (this *Params) UnmarshalJSON(data []byte) error {
//     var temp []json.RawMessage
//     if err := json.Unmarshal(data, &temp); err != nil {
//         return err
//     }
//     var pt [][]int
//     if err := json.Unmarshal(temp[0], &pt); err != nil {
//         return err
//     }
//     this.persons = pt[0]
//     this.times = pt[1]
//     this.qs = append(this.qs, -1)
//     for i := 1; i < len(temp); i++ {
//         var values []int
//         if err := json.Unmarshal(temp[i], &values); err != nil {
//             return err
//         }
//         this.qs = append(this.qs, values[0])
//     }
//     return nil
// }

func doTest(commands []string, params Params) util.OptionalIntSlice {
    var tvc TopVotedCandidate
    res := make(util.OptionalIntSlice, len(commands))
    for i, cmd := range commands {
        var optInt util.OptionalInt
        if cmd == "TopVotedCandidate" {
            tvc = Constructor(params.persons, params.times)
        } else {
            r := tvc.Q(params.qs[i])
            optInt.Set(r)
        }
        res[i] = optInt
    }
    return res
}

func parse_params(temp []json.RawMessage) Params {
    var this Params
    var pt [][]int
    if err := json.Unmarshal(temp[0], &pt); err != nil {
        panic(fmt.Sprintf("json unmarshal error: %s\n", err))
    }
    this.persons = pt[0]
    this.times = pt[1]
    this.qs = append(this.qs, -1)
    for i := 1; i < len(temp); i++ {
        var values []int
        if err := json.Unmarshal(temp[i], &values); err != nil {
            panic(fmt.Sprintf("json unmarshal error: %s\n", err))
        }
        this.qs = append(this.qs, values[0])
    }
    return this
}

func main() {
    work := unittest.CreateWork(doTest)
    // work.SetValidator(func(e,r)bool)
    work.CompareSerial = true
    work.SetArgParser(1, parse_params)
    // work.SetResultParser(func(s)w)
    // work.SetResultSerializer(func(w)s)
    work.Run()
}
