class EventBus:
    def __init__(self):
        self._subscribers = {}

    def subscribe(self, event_name, handler):
        self._subscribers.setdefault(event_name, []).append(handler)

    def publish(self, event_name, payload):
        for handler in self._subscribers.get(event_name, []):
            handler(payload)
