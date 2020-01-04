from PIL import Image, ImageDraw
import pygame


class TreeDiagram:
    # Set up data
    def __init__(self,
                 points, connections,
                 foreground=(255, 255, 255),
                 background=(0, 0, 0)):
        # Get image width
        m = []
        for i in points:
            m.append(len(i))
        m = max(m)
        # Create new image object
        self.img = Image.new('RGB',
                             (20 * (m * 2), 20 * (len(points) * 2)),
                             color=background)
        # Create new drawing object
        self.draw = ImageDraw.Draw(self.img)
        # Draw connection lines
        for i in range(len(connections)):
            for j in range(len(connections[i])):
                for k in range(len(connections[i][j])):
                    self.draw.line((
                        20 * (j * 2 + 1),
                        20 * (i * 2 + 1),
                        20 * (connections[i][j][k] * 2 + 1),
                        20 * (i * 2 + 3)
                    ), fill=foreground, width=2)
        # Draw circles
        for i in range(len(points)):
            for j in range(len(points[i])):
                if points[i][j] is False:
                    pass
                else:
                    self.draw.ellipse((
                        20 * (j * 2 + 1) - 7.5,
                        20 * (i * 2 + 1) - 7.5,
                        20 * (j * 2 + 1) + 7.5,
                        20 * (i * 2 + 1) + 7.5
                    ), fill=points[i][j], outline=foreground, width=2)
        # Make variables global
        self.points = points
        self.connections = connections
        self.colours = (foreground, background)
        self.size = (20 * (m * 2) + 400, 20 * (len(points) * 2))

    # Get image object
    def get(self):
        # Return image object
        return(self.img)

    # Save image object to file
    def export(self, name):
        return(self.img.save(name))

    # Create interactive diagram
    def interactive(self, subtext):
        # Setup interactive diagram
        pygame.init()
        screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption("Interactive Hierarchy Diagram")
        clock = pygame.time.Clock()
        pygame.font.init()
        comic_sans_ms = pygame.font.SysFont('Comic Sans MS', 30)
        lastTouched = False
        while True:
            # Set background colour
            screen.fill((self.colours[1]))
            # Check if quitting
            quit = False
            for event in pygame.event.get():  # User did something
                if event.type == pygame.QUIT:
                    quit = True
            if quit:
                break
            # Draw border line
            pygame.draw.line(
                screen,
                self.colours[0],
                (self.size[0] - 400, 0),
                (self.size[0] - 400, self.size[1]),
                2
            )
            pygame.draw.line(
                screen,
                self.colours[0],
                (self.size[0] - 400, 40),
                (self.size[0], 40),
                2
            )
            # Draw connection lines
            for i in range(len(self.connections)):
                for j in range(len(self.connections[i])):
                    for k in range(len(self.connections[i][j])):
                        pygame.draw.line(
                            screen,
                            self.colours[0],
                            (
                                20 * (j * 2 + 1),
                                20 * (i * 2 + 1)
                            ),(
                                20 * (self.connections[i][j][k] * 2 + 1),
                                20 * (i * 2 + 3)
                            ),
                            2
                        )
            # Draw circles
            for i in range(len(self.points)):
                for j in range(len(self.points[i])):
                    if self.points[i][j] is False:
                        pass
                    else:
                        pos = pygame.mouse.get_pos()
                        if (pos[0] > (
                            20 * (j * 2 + 1) - 10
                        ) and pos[0] < (
                            20 * (j * 2 + 1) + 10
                        ) and pos[1] > (
                            20 * (i * 2 + 1) - 10
                        ) and pos[1] < (
                            20 * (i * 2 + 1) + 10
                        )) or (
                            lastTouched is not False
                            and lastTouched[0] == i
                            and lastTouched[1] == j
                        ):
                            pygame.draw.ellipse(
                                screen,
                                self.points[i][j],
                                (
                                    20 * (j * 2 + 1) - 10,
                                    20 * (i * 2 + 1) - 10,
                                    20,
                                    20
                                )
                            )
                            pygame.draw.ellipse(
                                screen,
                                self.colours[0],
                                (
                                    20 * (j * 2 + 1) - 10,
                                    20 * (i * 2 + 1) - 10,
                                    20,
                                    20
                                ),
                                2
                            )
                            lastTouched = (i, j)
                        else:
                            pygame.draw.ellipse(
                                screen,
                                self.points[i][j],
                                (
                                    20 * (j * 2 + 1) - 7.5,
                                    20 * (i * 2 + 1) - 7.5,
                                    15,
                                    15
                                )
                            )
                            pygame.draw.ellipse(
                                screen,
                                self.colours[0],
                                (
                                    20 * (j * 2 + 1) - 7.5,
                                    20 * (i * 2 + 1) - 7.5,
                                    15,
                                    15
                                ),
                                2
                            )
                        if lastTouched is not False:
                            if subtext[lastTouched[0]][lastTouched[1]][0] == '':
                                text_canvas = comic_sans_ms.render(
                                    'Untitled',
                                    False,
                                    self.colours[0]
                                )
                                screen.blit(
                                    text_canvas,
                                    (self.size[0] - 390, 10)
                                )
                            else:
                                text_canvas = comic_sans_ms.render(
                                    subtext[lastTouched[0]][lastTouched[1]][0],
                                    False,
                                    self.colours[0]
                                )
                                screen.blit(
                                    text_canvas,
                                    (self.size[0] - 390, 10)
                                )
                            if subtext[lastTouched[0]][lastTouched[1]][1] == '':
                                text_canvas = comic_sans_ms.render(
                                    'No Description',
                                    False,
                                    self.colours[0]
                                )
                                screen.blit(
                                    text_canvas,
                                    (self.size[0] - 390, 50 + (30 * k))
                                )
                            else:
                                for k in range(len(subtext[lastTouched[0]][lastTouched[1]][1].split('\n'))):
                                    text_canvas = comic_sans_ms.render(
                                        subtext[lastTouched[0]][lastTouched[1]][1].split('\n')[k],
                                        False,
                                        self.colours[0]
                                    )
                                    screen.blit(
                                        text_canvas,
                                        (self.size[0] - 390, 50 + (30 * k))
                                    )
            # Update screen
            pygame.display.flip()
            # Limit frametime to 60 fps
            clock.tick(60)
        pygame.quit()
