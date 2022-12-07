package main

import (
	"fmt"
	"github.com/gorilla/websocket"
	"github.com/labstack/echo/v4"
	"log"
)

var upgrader = websocket.Upgrader{
	ReadBufferSize:  1024,
	WriteBufferSize: 1024,
}

func main() {
	e := echo.New()

	e.Static("/static", "static")
	e.GET("/rooms", someFunc)

	if err := e.Start(":1323"); err != nil {
		log.Panic(err)
	}
}

func someFunc(c echo.Context) error {
	ws, err := upgrader.Upgrade(c.Response(), c.Request(), nil)
	if err != nil {
		return err
	}
	for {
		msgType, msg, err := ws.ReadMessage()
		if err != nil {
			c.Logger().Error(err)
		}

		fmt.Printf("%s sent: %s\n", ws.RemoteAddr(), string(msg))
		if err = ws.WriteMessage(msgType, msg); err != nil {
			c.Logger().Error(err)
		}
	}
}
