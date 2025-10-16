import pygame
from hanoi import Stack, solve_hanoi


class HanoiGame:
    def __init__(self, num_disks=4):
        pygame.init()
        self.NUM_DISKS = num_disks
        self.SCREEN_WIDTH, self.SCREEN_HEIGHT = 800, 400
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        pygame.display.set_caption("Torre de Hanói")
        self.clock = pygame.time.Clock()

        self.WHITE = (255, 255, 255)
        self.BLACK = (30, 30, 30)
        self.PEG_COLOR = (139, 69, 19)
        self.DISK_COLORS = [
            (255, 87, 34),
            (255, 193, 7),
            (139, 195, 74),
            (3, 169, 244),
            (103, 58, 183),
            (233, 30, 99),
            (0, 150, 136),
        ]

        self.stacks = {"A": Stack(), "B": Stack(), "C": Stack()}

        for i in range(self.NUM_DISKS, 0, -1):
            self.stacks["A"].push(i)

        self.moves = solve_hanoi(self.NUM_DISKS)
        self.move_index = 0

    def draw(self):
        self.screen.fill(self.BLACK)
        peg_positions = {"A": 150, "B": 400, "C": 650}
        peg_width, peg_height = 10, 200
        base_height = 20

        for name, x_pos in peg_positions.items():
            pygame.draw.rect(
                self.screen,
                self.PEG_COLOR,
                (x_pos - 75, self.SCREEN_HEIGHT - 50, 150, base_height),
            )
            pygame.draw.rect(
                self.screen,
                self.PEG_COLOR,
                (
                    x_pos - (peg_width / 2),
                    self.SCREEN_HEIGHT - 50 - peg_height,
                    peg_width,
                    peg_height,
                ),
            )

        disk_height = 20
        for name, stack in self.stacks.items():
            x_center = peg_positions[name]
            for i, disk_size in enumerate(stack._container):
                disk_width = 30 + (disk_size * 15)
                y_pos = (self.SCREEN_HEIGHT - 50 - base_height) - (i * disk_height)
                disk_rect = pygame.Rect(0, 0, disk_width, disk_height)
                disk_rect.center = (x_center, y_pos)
                color = self.DISK_COLORS[disk_size - 1 % len(self.DISK_COLORS)]
                pygame.draw.rect(self.screen, color, disk_rect, border_radius=5)

        pygame.display.flip()

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (
                    event.type == pygame.KEYDOWN and event.key == pygame.K_q
                ):
                    running = False

            if self.move_index < len(self.moves):
                source_name, dest_name = self.moves[self.move_index]
                source_stack = self.stacks[source_name]
                dest_stack = self.stacks[dest_name]

                if source_stack._container:
                    disk = source_stack.pop()
                    dest_stack.push(disk)

                self.move_index += 1

            self.draw()
            self.clock.tick(1)

        pygame.quit()


if __name__ == "__main__":
    game = HanoiGame(num_disks=5)
    game.run()
