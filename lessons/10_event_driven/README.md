# 🔟 Event-Driven Programming

## The idea

React to events instead of direct calls. Components don't call each
other's functions and wait for a return value — they publish **events**
("this happened"), and anyone who cares subscribes to react. The
publisher never knows who's listening, how many listeners there are, or
what they do.

## The stop it adds

You stop writing `calculate_total(order); update_stock(order);
send_confirmation(order)` as three direct, sequential calls from one
place. Instead you publish one event — `OrderPlaced` — and let each
reaction subscribe independently. Placing an order doesn't "know about"
billing, stock, or notifications at all.

**Good for:** microservices, distributed systems — anywhere independent
parts need to react to the same thing without being coupled to each
other.
**Risk:** complex tracing and debugging — when three things need to
happen for one event and one of them silently didn't, there's no single
call stack to read; you have to know who's subscribed.

## Running it

No extra install — standard library `unittest`:

```bash
cd lessons/10_event_driven
python3 -m unittest test_events -v
```

## The example

- `event_bus.py` — a minimal in-process `EventBus`: `subscribe(event_name,
  handler)` and `publish(event_name, payload)`. (A real system would use
  something like Kafka, RabbitMQ, or SNS/SQS for this across services —
  same idea, this is the simplified in-memory version.)
- `handlers.py` — three independent reactions to `OrderPlaced`:
  calculating the total, logging what to decrement from stock, and
  recording a confirmation message. None of them call each other or know
  the others exist.
- `test_events.py` — publishes one `OrderPlaced` event and checks all
  three reactions happened, independently.

## What to notice

- `test_an_unrelated_event_triggers_nothing` — publishing `OrderCancelled`
  (a different event name) does nothing, even though the payload is
  identical. Reactions are tied to the event name, not the data shape.
- `test_a_new_handler_can_be_added_without_changing_how_orders_are_published`
  — a brand-new handler gets subscribed, and the code that publishes
  `OrderPlaced` never changes. That's the core promise of event-driven
  design: adding a new reaction never touches the thing that triggered it.
- The event payload here is a plain dict (like lesson 9), not a rich
  `Order` object — real events usually travel as serializable data
  (JSON), not live objects with methods.
