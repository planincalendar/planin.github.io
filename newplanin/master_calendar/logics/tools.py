from datetime import *
from master_calendar.models import *

class Tools:
    def sort(slots):
        slots = list(slots)
        totalCount = len(slots) - 1

        for i in range(totalCount):
            i = totalCount - i

            for j in range(i):
                current = slots[j]
                next = slots[j + 1]

                if current.start_timedate > next.start_timedate:
                    slots[j] = next
                    slots[j + 1] = current

        return slots

                
    def collapse(slot_a, slot_b, tolerant = False):
        if tolerant: return not(slot_b.end_timedate < slot_a.start_timedate or slot_b.start_timedate > slot_a.end_timedate)
        else: return not(slot_b.end_timedate <= slot_a.start_timedate or slot_b.start_timedate >= slot_a.end_timedate)


    def merge(events):

        if len(events) < 2: return
        current = events[0]
        idx = 1

        for _ in range(1, len(events)):
            target = events[idx]

            if Tools.collapse(current,target, True):
                current.end_timedate = target.end_timedate
                events.remove(target)
            else:
                current = target
                idx += 1

        return events


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
                if Tools.collapse(current, target):
                    if current.start_timedate > target.start_timedate: start = current.start_timedate
                    else: start = target.start_timedate

                    if current.end_timedate > target.end_timedate: end = target.end_timedate
                    else: end = current.end_timedate

                    results.append(Slot.create(start, end))

        return results
        