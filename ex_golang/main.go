package main

import (
	"encoding/json"
	"fmt"
	"net/http"
	"time"
)

type BinanceTickerResponse struct {
	Symbol string `json:"symbol"`
	Price  string `json:"price"`
}

func get_coin_price(symbol string) (string, error) {
	// Create an HTTP client
	client := &http.Client{
		Timeout: 5 * time.Second,
	}

	// Make the request to Binance API
	url := fmt.Sprintf("https://api.binance.com/api/v3/ticker/price?symbol=%s", symbol)
	response, err := client.Get(url)
	if err != nil {
		return "", err
	}
	defer response.Body.Close()

	// Parse the response JSON
	var tickerResponse BinanceTickerResponse
	err = json.NewDecoder(response.Body).Decode(&tickerResponse)
	if err != nil {
		return "", err
	}

	// Extract and print the Bitcoin price
	return tickerResponse.Price, nil
}

func main() {

	// get top 10 coin symbols
	symbols := []string{"BTCUSDT", "ETHUSDT", "BNBUSDT", "ADAUSDT", "XRPUSDT", "DOGEUSDT", "DOTUSDT", "UNIUSDT", "BCHUSDT", "LTCUSDT"}

	// get coin price
	for _, symbol := range symbols {
		price, err := get_coin_price(symbol)
		if err != nil {
			fmt.Println("Error:", err)
			return
		}
		fmt.Printf("%s Price (USDT): %s\n", symbol, price)
	}

}
