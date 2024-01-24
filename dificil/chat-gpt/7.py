from collections import defaultdict, deque
from typing import List

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0

        stop_to_routes = defaultdict(list)
        for i, route in enumerate(routes):
            for stop in route:
                stop_to_routes[stop].append(i)

        visited_routes = set()
        visited_stops = set()
        queue = deque([(source, 0)])

        while queue:
            current_stop, buses_taken = queue.popleft()

            for route_index in stop_to_routes[current_stop]:
                if route_index not in visited_routes:
                    visited_routes.add(route_index)
                    for next_stop in routes[route_index]:
                        if next_stop == target:
                            return buses_taken + 1
                        if next_stop not in visited_stops:
                            visited_stops.add(next_stop)
                            queue.append((next_stop, buses_taken + 1))

        return -1

# Example usage:
routes1 = [[1, 2, 7], [3, 6, 7]]
source1, target1 = 1, 6
sol = Solution()
output1 = sol.numBusesToDestination(routes1, source1, target1)
print(output1)  # Output: 2

routes2 = [[7, 12], [4, 5, 15], [6], [15, 19], [9, 12, 13]]
source2, target2 = 15, 12
output2 = sol.numBusesToDestination(routes2, source2, target2)
print(output2)  # Output: -1
