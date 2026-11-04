#!/usr/bin/env python3

import typing
import random

def gen_event() -> typing.Generator[tuple[str, str], None, None]:
    actions = ["run", "eat", "sleep", "move", "swim", "climb", "grab", "release", "use"]
    names = ["Alice", "Charlie", "Bob", "Dylan"]
    while True:
        action = random.choice(actions)
        name = random.choice(names)
        yield name, action


def consume_event(events: list[tuple[str, str]]) -> typing.Generator[
            tuple[str, str], None, None]:
    while len(events) > 0:
        event = random.choice(events)
        events.remove(event)
        yield event


def data_stream() -> None:
    print("=== Game Data Stream Processor ===")
    eventt = gen_event()
    for i in range (1000):
        event = next(eventt)
        name = event[0]
        action = event[1]
        print(f"Event {i}: Player {name} did action {action}")
    event_list = []
    for i in range(10):
        event_list.append(next(eventt))
    print(f"Built list of 10 events: {event_list}")
    for event in consume_event(event_list):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {event_list}")
    return


if __name__ == "__main__":
    data_stream()