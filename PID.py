import pygame

# Important Display Variables
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)


class Simulation(object):
   def __init__(self):
      self.pid = PID
      self.screen = pygame.display()
      self.screen.set_mode((1280, 720))

   def cycle(self):
      while running:
         for event in pygame.event.get():
            if event.type == pygame.QUIT:
               running = False
   
         screen.fill("black")

         pygame.draw.circle(screen, "red", player_pos, 40)

         pygame.display.flip()
         dt = clock.tick(60) / 1000



class PID(object):
	def __init__(self,KP,KI,KD,target):
		self.kp = KP
		self.ki = KI
		self.kd = KD 
		self.setpoint = target
		self.error = 0
		self.integral_error = 0
		self.error_last = 0
		self.derivative_error = 0
		self.output = 0
	def compute(self, pos):
		self.error = self.setpoint - pos
		self.integral_error += self.error * TIME_STEP
		self.derivative_error = (self.error - self.error_last) / TIME_STEP
		self.error_last = self.error
		self.output = self.kp*self.error + self.ki*self.integral_error + self.kd*self.derivative_error
		if(abs(self.output)>= MAX_THRUST and (((self.error>=0) and (self.integral_error>=0))or((self.error<0) and (self.integral_error<0)))):
			if(antiWindup):
				#no integration
				self.integral_error = self.integral_error
			else:
				#if no antiWindup rectangular integration
				self.integral_error += self.error * TIME_STEP
		else:
			#rectangular integration
			self.integral_error += self.error * TIME_STEP
		if self.output >= MAX_THRUST:
			self.output = MAX_THRUST
		elif self.output <= 0:
			self.output = 0
		return self.output
		
	def get_kpe(self):
		return self.kp*self.error
	def get_kde(self):
		return self.kd*self.derivative_error
	def get_kie(self):
		return self.ki*self.integral_error

pygame.quit()
