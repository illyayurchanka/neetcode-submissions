class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [[pos, v] for pos, v in zip(position, speed)]
        cars = sorted(cars, key=lambda car: car[0], reverse=True)

        times = [(target - pos) / v for pos, v in cars]
        stack = [times[0]]
        fleet = 1
        for time in times[1:]:
            if time > stack[-1]:
                fleet += 1
                stack.append(time) 

        return fleet