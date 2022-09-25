index = 0
interval = 0
class Animation:
    def __init__(self, surface_var, frames_between, frame_list, location):
       self.surface = surface_var
       self.frames_between = frames_between
       self.frame_list = frame_list
       self.location = location
       self.interval = 0
       self.index = 0
       self.last_index = len(self.frame_list) - 1

    def animate(self):
        self.surface.blit(self.frame_list[self.index], self.location)

        if self.interval >= self.frames_between:
            self.interval = 0
            
            if self.index == self.last_index:
                self.index = 0
                
            else:                
                self.index += 1
  
        self.interval += 1