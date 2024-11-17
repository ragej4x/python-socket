import pygame
import threading
import time
import random
from queue import Queue

pygame.init()

WINDOW_WIDTH, WINDOW_HEIGHT = 800, 600
CUSTOMER_SIZE = 16
FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GRAY = (128, 128, 128)
WALL_COLOR = (105, 105, 105)
ENTRANCE_COLOR = (0, 0, 255)

WALLS = [
    pygame.Rect(350, 300, 10, 50),  
    pygame.Rect(650, 150, 10, 210), 
    pygame.Rect(350, 150, 300, 10),  
    pygame.Rect(350, 350, 300, 10),  
]
ENTRANCE_POS = (100, 140)  
EXIT_POS = (100, 300)  

class Customer:
    def __init__(self, start_pos, target_pos):
        self.pos = list(start_pos)
        self.target = target_pos
        self.waiting = True
        self.getting_haircut = False
        self.lost = False
        self.arrival_time = time.time()

    def update(self):
        #direction move
        speed = 2
        dx = self.target[0] - self.pos[0]
        dy = self.target[1] - self.pos[1]
        distance = max(abs(dx), abs(dy))
        
        if distance > 0:
            self.pos[0] += speed * (dx / distance)
            self.pos[1] += speed * (dy / distance)

class BarberShop:
    def __init__(self, waiting_room_size):
        self.waiting_room = Queue(maxsize=waiting_room_size)
        self.customers = []
        self.active_customer = None
        self.customers_served = 0
        self.customers_lost = 0
        self.barber_sleeping = threading.Event()
        self.customer_ready = threading.Event()
        self.entrance = ENTRANCE_POS
        self.exit = EXIT_POS
        self.barber_chair = (600, 250)
        self.waiting_positions = [(400, 180 + i * 40) for i in range(waiting_room_size)]
        self.barber_busy = False  

    def add_customer(self):
        customer = Customer(self.entrance, self.waiting_positions[0] if not self.waiting_room.full() else self.entrance)
        self.customers.append(customer)

        if self.waiting_room.full():
            threading.Thread(target=self.check_customer_timeout, args=(customer,), daemon=True).start()
        else:
            customer.target = self.waiting_positions[self.waiting_room.qsize()]
            self.waiting_room.put(customer)
            self.update_waiting_positions()
            self.customer_ready.set()
            if self.barber_sleeping.is_set():
                self.barber_sleeping.clear()  # wake up barber

    def check_customer_timeout(self, customer):
        time.sleep(2)
        if customer in self.customers and not customer.getting_haircut and self.waiting_room.full():
            customer.lost = True
            self.customers_lost += 1
            customer.target = self.exit 

    def update_waiting_positions(self):
        for idx, customer in enumerate(list(self.waiting_room.queue)):
            customer.target = self.waiting_positions[idx]

    def barber(self):
        while True:
            self.customer_ready.wait()
            self.customer_ready.clear()
            #barber room

            while not self.waiting_room.empty():
                self.active_customer = self.waiting_room.get()
                self.active_customer.getting_haircut = True
                self.active_customer.target = self.barber_chair

                while (int(self.active_customer.pos[0]), int(self.active_customer.pos[1])) != self.barber_chair:
                    time.sleep(0.1)  

                self.barber_busy = True
                time.sleep(random.randint(5, 8)) 
                self.customers_served += 1
                self.active_customer.getting_haircut = False
                self.active_customer.target = self.exit
                self.active_customer = None
                self.update_waiting_positions()  

            self.barber_busy = False
            self.barber_sleeping.set()

    def update_customers(self):
        for customer in self.customers[:]:
            customer.update()
            # remove customer if they reach the exit
            if customer.pos == list(self.exit):
                self.customers.remove(customer)

    def draw(self, screen):
        #pinto
        pygame.draw.rect(screen,(255,190,190,10), (350, 150, 10, 150))
        #barberroom
        pygame.draw.rect(screen, (190, 190, 190, 10), (560,160, 90,190))
        #chair
        pygame.draw.rect(screen, (90, 90, 190), (390,170, 20,20))
        pygame.draw.rect(screen, (90, 90, 190), (390,170 *1.24, 20,20))
        pygame.draw.rect(screen, (90, 90, 190), (390,170 *1.48, 20,20))

        for wall in WALLS:
            pygame.draw.rect(screen, WALL_COLOR, wall)

        #status text ubtu
        barber_color = RED if self.barber_busy else BLUE
        #BARDER
        pygame.draw.circle(screen, barber_color, self.barber_chair , 10)


        font = pygame.font.Font(None, 28)
        client_label = font.render('Customer', True, GREEN)

        status_text = "Working" if self.barber_busy else "Sleeping"
        status_text_surface = font.render(status_text, True, BLACK)

        screen.blit(status_text_surface, (self.barber_chair[0] - 30, self.barber_chair[1] + 30))

        for customer in self.customers:
            color = GREEN if customer.waiting else BLACK
            pygame.draw.circle(screen, color, (int(customer.pos[0]), int(customer.pos[1])), CUSTOMER_SIZE // 2)

            screen.blit(client_label, (int(customer.pos[0]) - 50, int(customer.pos[1]) + 10))

            if customer.lost:
                pygame.draw.circle(screen, RED, (int(customer.pos[0]), int(customer.pos[1]) - 10), 5)

        # Draw entrance and exit
        pygame.draw.circle(screen, ENTRANCE_COLOR, ENTRANCE_POS, 10)
        pygame.draw.circle(screen, GRAY, EXIT_POS, 10)

def spawn_customers(shop):
    while True:
        shop.add_customer()
        time.sleep(random.uniform(2, 6))  # randpm spawn intervl

def main():
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Simulation")
    clock = pygame.time.Clock()
    
    shop = BarberShop(waiting_room_size=3)
    
    threading.Thread(target=shop.barber, daemon=True).start()
    threading.Thread(target=spawn_customers, args=(shop,), daemon=True).start()
    
    running = True
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        shop.update_customers()  #custome
        
        screen.fill(WHITE)
        shop.draw(screen)
        
        font = pygame.font.Font(None, 36)
        served_text = font.render(f"Served: {shop.customers_served}", True, BLACK)
        lost_text = font.render(f"Lost: {shop.customers_lost}", True, BLACK)
        screen.blit(served_text, (10, 10))
        screen.blit(lost_text, (10, 50))
        
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()
