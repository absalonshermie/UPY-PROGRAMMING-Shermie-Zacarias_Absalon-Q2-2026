#main.py
import pygame

config = {}
with open('config.txt', 'r') as file:
    for line in file:
        parameter, value = line.strip().split("=")
        if ',' in value:
            config[parameter] = tuple(int(c.strip()) for c in value.split(","))
        elif '.' in value:
            config[parameter] = float(value)
        else:
            config[parameter] = int(value)


#INITIALIZATION
pygame.init()
screen = pygame.display.set_mode((config['width'], config['height']))

#CONFIGURATION
def calculate_x_positions(surface, vertical_lines, space):
    x_positions = []
    width = surface.get_width()
    spacing = space * width
    central_line = width / 2
    offset = -int(vertical_lines / 2) 

    for i in range(vertical_lines):
        x_positions.append(central_line + (offset * spacing))
        offset += 1

    return x_positions

def draw_vertical_lines(surface, x_positions, color, width=2):
    height = surface.get_height()
    
    for x in x_positions:
        pygame.draw.line(surface, color, (x, 0), (x, height), width)

#MAIN LOOP
x_positions = calculate_x_positions(
    surface=screen,
    vertical_lines=config['vertical_lines'],
    space=config['space']
)
print(x_positions)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(config['bg_color'])
    draw_vertical_lines(screen, x_positions, config['line_color'])
    pygame.display.flip()

pygame.quit()