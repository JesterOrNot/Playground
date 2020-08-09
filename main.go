package main

import (
	"fmt"
	"sync"
)

var (
	buffer []int
)

func init()  {
	buffer = []int{5, 10, 15, 30, 25}
}

func producer(channel chan int) {
	for _, i := range buffer {
		channel <- i
	}
	close(channel)
}

func consumer(wg *sync.WaitGroup, channel chan int) {
	for i := range channel {
		fmt.Println(i*2)
	}
	wg.Done()
}

func main() {
	wg := sync.WaitGroup{}
	wg.Add(1)
	channel := make(chan int)
	go producer(channel)
	go consumer(&wg, channel)
	wg.Wait()
}
