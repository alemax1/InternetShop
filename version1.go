package main

import (
	"fmt"
	"log"
	"math/rand"
	"os"
	"sync"
	"time"
)

type divider struct {
	divBy   int
	counter int
	ch      chan int
	mu      sync.Mutex
}

var (
	d2 = &divider{
		divBy:   2,
		counter: 0,
		ch:      make(chan int, 50),
		mu:      sync.Mutex{},
	}

	d3 = &divider{
		divBy:   2,
		counter: 0,
		ch:      make(chan int, 50),
		mu:      sync.Mutex{},
	}

	d4 = &divider{
		divBy:   2,
		counter: 0,
		ch:      make(chan int, 50),
		mu:      sync.Mutex{},
	}
)

var (
	ch = make(chan int)
	wg = sync.WaitGroup{}
)

func main() {
	for i := 0; i < 350; i++ {
		wg.Add(1)
		go generateRandomNum()
		go handleNum()
	}
	wg.Wait()
	printResult()
}

func generateRandomNum() {
	num := rand.Intn(100)
	ch <- num
}

func handleNum() {
	num := <-ch
	go divisibleByTwo(num)
	go divisibleByThree(num)
	go divisibleByFour(num)
}

func divisibleByTwo(num int) {
	d2.mu.Lock()
	defer d2.mu.Unlock()
	if num%d2.divBy == 0 && d2.counter < 50 {
		d2.ch <- num
		d2.counter++
	}
	time.Sleep(10 * time.Millisecond)
}

func divisibleByThree(num int) {
	d3.mu.Lock()
	defer d3.mu.Unlock()
	if num%d3.divBy == 0 && d3.counter < 50 {
		d3.ch <- num
		d3.counter++
	}
	time.Sleep(30 * time.Millisecond)
}

func divisibleByFour(num int) {
	d4.mu.Lock()
	defer func() {
		d4.mu.Unlock()
		wg.Done()
	}()
	if num%d4.divBy == 0 && d4.counter < 50 {
		d4.ch <- num
		d4.counter++
	}
	time.Sleep(100 * time.Millisecond)
}

func printResult() {
	f, err := os.Create("data.txt")
	if err != nil {
		log.Panic(err)
	}

	close(d4.ch)
	for i := range d4.ch {
		f.WriteString(fmt.Sprintf("printed by DIV4 %v\n", i))
	}

	close(d3.ch)
	for i := range d3.ch {
		f.WriteString(fmt.Sprintf("printed by DIV3 %v\n", i))
	}

	close(d2.ch)
	for i := range d2.ch {
		f.WriteString(fmt.Sprintf("printed by DIV2 %v\n", i))
	}
}
