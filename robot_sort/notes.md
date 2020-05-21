        #turn light on to signify robot is working
        self.set_light_on()
        self.swap_item()

        #when the robot is on, if it can move right, then move right
        while self.light_is_on():

            while self.can_move_right():
                self.move_right()
                #after moving right, compare that item, and if it is greater then swap
                if self.compare_item() == 1:
                    self.swap_item()
           #when the robot can move left we will do the same thing but to compare if the item is smaller value
            # while self.can_move_left():
            while self.compare_item() != None:
                self.swap_item()
                self.move_left()
                if self.compare_item() == -1:
                   self.swap_item()
                else:
                    self.set_light_off()