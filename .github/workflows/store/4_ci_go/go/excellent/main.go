package main

func EvenOrOdd(number int) string {
	if number%2 == 0 {
		return "Even"
	} else {
		return "Odd"
	}
}

// メイン関数
func main() {
	// 例: 4は偶数、5は奇数
	println(EvenOrOdd(4)) // 出力: Even
	println(EvenOrOdd(5)) // 出力: Odd
}
