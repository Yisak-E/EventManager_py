from .event import Event

class EventRepository:
    def __init__(self):
        self.events = {}
    def add_event(self, _event):
        self.events[_event.get_id()] = _event
    def remove_event(self, _event) -> None:
       if _event.get_id() in self.events:
           del self.events[_event.getId()]


    def get_event(self, _id="K-100") -> Event | None:
        return self.events.get(_id)
