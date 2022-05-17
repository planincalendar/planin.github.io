from asyncio import events
from models import *
from datetime import *

class Tools:
    def sort(slots):
        totalCount = len(slots) - 1

        for i in range(totalCount):
            i = totalCount - i

            for j in range(i):
                current = slots[j]
                next = slots[j + 1]

                if current.start_timedate > next.start_timedate:
                    slots[j] = next
                    slots[j + 1] = current

                
    def collapse(slot_a, slot_b, tolerant = False):
        if tolerant: return not(slot_b.end_timedate < slot_a.start_timedate or slot_b.start_timedate > slot_a.end_timedate)
        else: return not(slot_b.end_timedate <= slot_a.start_timedate or slot_b.start_timedate >= slot_a.end_timedate)


    def merge(events):

        if len(events) < 2: return
        current = events[0]
        idx = 1

        for _ in range(1, len(events)):
            target = events[idx]

            if current.collapse(target, True):
                current.end_timedate = target.end_timedate
                events.remove(target)
            else:
                current = target
                idx += 1


    def reverse(events_in, start, end):
        if len(events_in) == 0: return [Slot.create(start, end)]

        events = []
        results = []
        for e in events_in: events.append(e.copy())

        if start < events[0].start: results.append(Slot.create(start, events[0].start))
        for i in range(len(events) - 1): results.append(Slot.create(events[i].end, events[i + 1].start))
        if end > events[-1].end: results.append(Slot.create(events[-1].end, end))

        return results


    def intersect(events_a, events_b):
        results = []

        for current in events_a:
            for target in events_b:
                if current.collapse(target):
                    if current.start > target.start: start = current.start
                    else: start = target.start

                    if current.end > target.end: end = target.end
                    else: end = current.end

                    results.append(Slot.create(start, end))

        return results
