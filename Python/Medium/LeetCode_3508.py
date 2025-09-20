# Design a data structure that can efficiently manage data packets in a network router. Each data packet consists of the following attributes:

# source: A unique identifier for the machine that generated the packet.
# destination: A unique identifier for the target machine.
# timestamp: The time at which the packet arrived at the router.
# Implement the Router class:

# Router(int memoryLimit): Initializes the Router object with a fixed memory limit.

# memoryLimit is the maximum number of packets the router can store at any given time.
# If adding a new packet would exceed this limit, the oldest packet must be removed to free up space.
# bool addPacket(int source, int destination, int timestamp): Adds a packet with the given attributes to the router.

# A packet is considered a duplicate if another packet with the same source, destination, and timestamp already exists in the router.
# Return true if the packet is successfully added (i.e., it is not a duplicate); otherwise return false.
# int[] forwardPacket(): Forwards the next packet in FIFO (First In First Out) order.

# Remove the packet from storage.
# Return the packet as an array [source, destination, timestamp].
# If there are no packets to forward, return an empty array.
# int getCount(int destination, int startTime, int endTime):

# Returns the number of packets currently stored in the router (i.e., not yet forwarded) that have the specified destination and have timestamps in the inclusive range [startTime, endTime].
# Note that queries for addPacket will be made in increasing order of timestamp.



from collections import deque, defaultdict
import bisect

class Router:

    def __init__(self, memoryLimit: int):

        self.memoryLimit = memoryLimit
        self.queue = deque()   # FIFO order of packets
        self.packetSet = set()  # for duplicate check
        self.destMap = defaultdict(list)  # destination -> timestamps
        self.packetProcessed = defaultdict(int)  # destination -> index of first non-forwarded

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        packet = (source, destination, timestamp)
        if packet in self.packetSet:   # duplicate check
            return False
        
        # enforce memory limit
        if len(self.queue) == self.memoryLimit:
            self.forwardPacket()  # drop oldest before adding

        # insert packet
        self.queue.append(packet)
        self.packetSet.add(packet)
        self.destMap[destination].append(timestamp)
        return True

    def forwardPacket(self):
        if not self.queue:
            return []
        
        src, dest, ts = self.queue.popleft()
        self.packetSet.remove((src, dest, ts))
        # mark one more processed (i.e. forwarded) for that destination
        self.processed[dest] += 1
        return [src, dest, ts]

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        timestamps = self.destMap.get(destination, [])
        p_idx = self.packetProcessed[destination]  # skip already forwarded
        # binary search in the unprocessed portion
        lo = bisect.bisect_left(timestamps, startTime, p_idx)
        hi = bisect.bisect_right(timestamps, endTime, p_idx)
        return hi - lo