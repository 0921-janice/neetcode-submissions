class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # time =  (target - position) / speed
        n = len(position)
        cars = [[position[i], speed[i]] for i in range(n)] 

        sorted_cars = sorted(cars, key = lambda x: x[0], reverse = True)
        stack = [(target - sorted_cars[0][0]) / sorted_cars[0][1]]

        for i in range(1,n):
            time = (target - sorted_cars[i][0]) / sorted_cars[i][1]
            if time > stack[-1]:
                stack.append(time)


        return len(stack)
    
    
