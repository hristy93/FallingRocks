class Player:
    def __init__(self):
        # self.initial_position = (0, 0)
        # self.current_position = self.initial_position
        self.is_invincible = False
        self.invincibility_time = 300
        self.speed = 10

    def move_left(self, speed):
        pass

    def move_right(self, speed):
        pass

    def set_player_invinciblity(self):
        self.is_invincible = not self.is_invincible

    @property
    def player_speed(self):
        return self.speed

    @property
    def is_player_invincible(self):
        return self.is_invincible

    # @property
    # def player_invincibility_time(self):
    #     self.invincibility_time
