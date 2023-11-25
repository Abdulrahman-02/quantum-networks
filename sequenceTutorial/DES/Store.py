from sequence.kernel.timeline import Timeline
from sequence.kernel.event import Event
from sequence.kernel.process import Process

class Store(object):
    # timeline is an instance of a DES kernel
    # we use timeline to bind entities to the DES Kernel
    def __init__ (self, tl: Timeline):
        self.open = False
        self.timeline = tl

    # open and close denotes if the store is in its business hours
    # These to functions change the state of the store
    def open_store (self) -> None:
        self.open = True

    def close_store (self) -> None:
        self.open = False

tl = Timeline() # create a timeline
tl.show_progress = False # turn off progress bar
store = Store(tl) # create a store

# open store at 7:00
open_proc = Process(store, 'open_store', [])
open_event = Event(7, open_proc)
tl.schedule(open_event)
tl.run()
print(tl.now(), store.open) # 7 True

close_proc = Process(store, 'close_store', [])
close_event = Event(19, close_proc)
tl.schedule(close_event)
tl.run()
print(tl.now(), store.open) # 19 False

# TODO: will the state of store change if we schedule close_event first, then open_event?

tl.time = 0
tl.schedule(open_event)
tl.schedule(close_event)
tl.run()
print(tl.time, store.open)

tl.time = 0
tl.schedule(close_event)
tl.schedule(open_event)
tl.run()
print(tl.time, store.open)

# Both generate the same result (19 False)
# as the order of executing events does not rely on the order of calling the scheduling method.
