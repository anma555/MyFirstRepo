package main
import (
	"encoding/json"
	"fmt"
)

type Record struct {
	RequestID uint `json:"request_id"`
	UserID    uint `json:"user_id"`
	Priority  int  `json:"priority"`
	RequestTS int  `json:"request_ts"`
}

func main() {
	data := []byte(`{
		"request_id": 1,
		"user_id": 2,
		"priority": 3,
		"request_ts": 1709168580
	}`)

	var record Record
	err := json.Unmarshal(data, &record)
	if err != nil {
		fmt.Println("Error parsing JSON:", err)
		return
	}

	fmt.Printf("Parsed Record: %+v\n", record)
}
