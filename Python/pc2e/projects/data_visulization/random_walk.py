from random import choice

class RandomWalk:
    """ A class to generate random walks """

    def __init__(self,num_points = 5000):
        """ Initialize the attributes of the walk """
        self.num_points = num_points

        #all walk starts at (0,0)
        self.x_value = [0]
        self.y_value = [0]

    def fill_walk(self):
        """ calculate all the points for the walk"""
        
        # keep taking steps until you reach desired steps 
        while len(self.x_value) < self.num_points:
            
            # calculate direction, distance and step for the walk 
            x_step = self.get_step()
            y_step = self.get_step()

            #reject moves that go no where
            if x_step == 0 and y_step == 0:
                continue
            
            #calcualte the new positions 
            x = self.x_value[-1] + x_step
            y = self.y_value[-1] + y_step 

            self.x_value.append(x)
            self.y_value.append(y)

    def get_step(self):
        """ Determine the direction and distance of each step """ 
        x_direction = choice([1,-1])
        x_distance = choice([0,1,2,3,4])
        return x_direction * x_distance 
