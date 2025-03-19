from collections import deque
class Solution:
    def BFS (self, graph):
        n = len(graph)
        final_state = (1 << n) - 1  # All nodes visited bitmask
        queue = deque([])
        for i in range(n):
            queue.append([(1<<i), i, 0])
        visited = set()
        [visited.add(((1<<i), i)) for i in range(n)]
        print(final_state)
        while queue:
            # print(queue)
            [cur_state, cur_node, num_steps] = queue.popleft()
            if cur_state == final_state:
                return num_steps
            for child in graph[cur_node]:
                existed = False
                if (cur_state & (1 << child)) != 0:
                    existed = True
                cur_state = cur_state | (1 << child)
                if (cur_state, child) not in visited:
                    queue.append([cur_state, child, num_steps + 1])
                    visited.add((cur_state, child))
                if not existed:
                    cur_state = cur_state & ~(1 << child)
        return -1

        #test
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        return self.BFS(graph)