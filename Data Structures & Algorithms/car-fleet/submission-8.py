class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = []
        for p , s in zip(position, speed):
            pairs.append([p, s])
        
        stack = []
        for p , s in sorted(pairs)[::-1]:
            stack.append((target - p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)


"""
key insight: time to reach the destination since cars are restricted to a 
single lane and cannot pass one another, their relative order remains constant 
throughout the journey.

Calculate arrival time: For every car, you calculate exactly 
how long it will take to reach the target position using the 
formula: (target - position) / speed

Process in reverse order: You should sort the cars by their starting position and iterate 
through them starting from the one closest to the destination

Detect collisions: As you move backward, you maintain a stack of 
the arrival times of the fleets ahead . If a car behind has a smaller 
or equal arrival time compared to the car in front of it, 
it means the rear car will catch up and form a fleet with the one in front 

Simplify the fleet: Because the rear car is forced to slow down to match the speed of the 
car it catches, you can simply ignore (or "pop") the rear car from your consideration, 
as it effectively becomes part of the fleet ahead of it 
"""