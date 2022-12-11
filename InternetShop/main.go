package main

import (
	"github.com/labstack/echo/v4"
	"strconv"
)

func main() {
	e := echo.New()
	go h.run()

	e.GET("/ws/rooms/:roomId", func(c echo.Context) error {
		roomId := c.Param("roomId")
		if _, err := strconv.Atoi(roomId); err != nil {
			return err
		}
		upgradeToWs(c.Response().Writer, c.Request(), roomId)
		return nil
	})

	e.GET("/ws/rooms", func(c echo.Context) error {
		upgradeToWs2(c.Response().Writer, c.Request())
		return nil
	})

	e.Start(":1323")
}
