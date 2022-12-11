package main

import (
	"fmt"
	"github.com/gorilla/websocket"
	"log"
	"net/http"
)

type subscription struct {
	con  *websocket.Conn
	room string
}

var upgrader = websocket.Upgrader{
	ReadBufferSize:  0,
	WriteBufferSize: 0,
}

var messages = make(chan map[string]map[*websocket.Conn]bool)

func readWs(s subscription) {
	defer func() {
		s.con.Close()
		h.unregister <- s
	}()
	for {
		_, _, err := s.con.ReadMessage()
		if websocket.IsUnexpectedCloseError(err, websocket.CloseGoingAway, websocket.CloseAbnormalClosure) {
			log.Printf("error: %v", err)
		}
		break
	}
}

func writeWs(con *websocket.Conn) {

	defer func() {
		con.Close()
	}()
	for {
		select {
		case message := <-messages:
			w, err := con.NextWriter(websocket.TextMessage)
			if err != nil {
				return
			}
			if len(message) == 0 {
				w.Write([]byte("All rooms are empty"))
			}
			for key, value := range message {
				msg := fmt.Sprintf("%v client in room %v ", len(value), key)
				w.Write([]byte(msg))
				for k := range value {
					w, err := k.NextWriter(websocket.TextMessage)
					if err != nil {
						return
					}
					msg2 := fmt.Sprintf("%v clients in room %v ", len(value), key)
					w.Write([]byte(msg2))
					k.WriteMessage(200, []byte(msg2))
				}
			}

			if err := w.Close(); err != nil {
				return
			}
		}
	}
}

func upgradeToWs(w http.ResponseWriter, r *http.Request, roomId string) {
	con, err := upgrader.Upgrade(w, r, nil)
	if err != nil {
		log.Println(err.Error())
	}
	s := subscription{con: con, room: roomId}
	h.register <- s
	go readWs(s)
}

func upgradeToWs2(w http.ResponseWriter, r *http.Request) {
	con, err := upgrader.Upgrade(w, r, nil)
	if err != nil {
		log.Println(err.Error())
	}
	go writeWs(con)
}
