// This is the main class.
// Where you will extract the inputs asked on the config.json file and call the formula's method(s).

package main

import (
	"formula/pkg/formula"
	"os"
)

func main() {
	input1 := os.Getenv("RIT_USERNAME")
	input2 := os.Getenv("RIT_PASSWORD")

	formula.Formula{
		Username: input1,
		Password: input2,
	}.Run()
}
