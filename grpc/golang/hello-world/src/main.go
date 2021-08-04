// This is the main class.
// Where you will extract the inputs asked on the config.json file and call the formula's method(s).

package main

import (
	"formula/pkg/formula"
	"os"
)

func main() {
	input1 := os.Getenv("RIT_INPUT_TEXT")

	formula.Formula{
		Text: input1,
	}.Run()
}
