from collections import defaultdict, deque

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0

        stop_to_routes = defaultdict(set)
        for i, route in enumerate(routes):
            for stop in route:
                stop_to_routes[stop].add(i)

        visited_routes = set()
        queue = deque([source])
        buses_taken = 0

        while queue:
            buses_taken += 1
            for _ in range(len(queue)):
                stop = queue.popleft()
                for route in stop_to_routes[stop]:
                    if route in visited_routes:
                        continue
                    visited_routes.add(route)
                    if target in routes[route]:
                        return buses_taken
                    for next_stop in routes[route]:
                        queue.append(next_stop)

        return -1