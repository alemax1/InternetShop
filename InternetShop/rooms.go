package main

import "github.com/gorilla/websocket"

type hub struct {
	rooms      map[string]map[*websocket.Conn]bool
	register   chan subscription
	unregister chan subscription
}

var h = &hub{
	rooms:      make(map[string]map[*websocket.Conn]bool),
	register:   make(chan subscription),
	unregister: make(chan subscription),
}

func (h *hub) run() {
	for {
		select {
		case s := <-h.register:
			connections := h.rooms[s.room]
			if connections == nil {
				connections = make(map[*websocket.Conn]bool)
				h.rooms[s.room] = connections
			}
			h.rooms[s.room][s.con] = true
			messages <- h.rooms
		case s := <-h.unregister:
			connections := h.rooms[s.room]
			if connections != nil {
				if _, ok := connections[s.con]; ok {
					delete(connections, s.con)
					if len(connections) == 0 {
						delete(h.rooms, s.room)
					}
				}
			}
			messages <- h.rooms
		}
	}
}
