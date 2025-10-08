import pygame, sys, random

pygame.init()

window = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Random Color Game")
font = pygame.font.Font(None, 74)
small_font = pygame.font.Font(None, 48)

def GenRandomColor():
    return (
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255)
    )

# Initial color
color = GenRandomColor()

while True:
    rgb_text = f"RGB: {color}"

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # 🖱 Change color when mouse button is pressed
        if event.type == pygame.MOUSEBUTTONDOWN:
            color = GenRandomColor()
            print(rgb_text)

        # 🎹 Change color when SPACE key is pressed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                color = GenRandomColor()
                print(rgb_text)


    # Fill window with the new color
    window.fill(color)

    # Render static text
    text_surface = font.render("Hello", True, (255, 255, 255))
    window.blit(text_surface, (330, 250))

    # Render RGB value text
    rgb_surface = small_font.render(rgb_text, True, (255, 255, 255))
    window.blit(rgb_surface, (10, 10))
    # Update display
    pygame.display.update()
