package main


import (
	"fmt"
	"math/rand"
	"os"
	"time"

	"github.com/charmbracelet/bubbles/spinner"
	tea "github.com/charmbracelet/bubbletea"
)





func main() {

	rand.Seed(time.Now().UnixNano())
	p := tea.NewProgram(initialModel())
	if _, err := p.Run(); err != nil {
		fmt.Println("Alas, there's been an error:", err)
		os.Exit(1)
	}
}