import pygame

# 常量定义
TILE_SIZE = 64  # 单格尺寸
MAP_WIDTH = 9    # 地图宽度（列数）
MAP_HEIGHT = 12  # 地图高度（行数）
DEFAULT_SAMPLE_PATH = "sample/map/default.png"

class MapSystem:
    def __init__(self, screen):
        self.screen = screen
        self.tiles = [[None for _ in range(MAP_WIDTH)] for _ in range(MAP_HEIGHT)]
        self.default_sample = pygame.image.load(DEFAULT_SAMPLE_PATH)
        self.default_sample = pygame.transform.scale(self.default_sample, (TILE_SIZE, TILE_SIZE))
        self.fill_default()
    
    def fill_default(self):
        """用默认采样填充整个地图"""
        for row in range(MAP_HEIGHT):
            for col in range(MAP_WIDTH):
                self.tiles[row][col] = self.default_sample
    
    def add_sample(self, sample_path, positions):
        """加载新采样，并放置到指定的格子中"""
        sample = pygame.image.load(sample_path)
        sample = pygame.transform.scale(sample, (TILE_SIZE, TILE_SIZE))  # 无抗锯齿缩放
        
        for pos in positions:
            row, col = pos
            if 0 <= row < MAP_HEIGHT and 0 <= col < MAP_WIDTH:
                self.tiles[row][col] = sample
    
    def draw(self):
        """绘制地图"""
        for row in range(MAP_HEIGHT):
            for col in range(MAP_WIDTH):
                self.screen.blit(self.tiles[row][col], (col * TILE_SIZE, row * TILE_SIZE))

# Pygame 初始化
pygame.init()
screen = pygame.display.set_mode((MAP_WIDTH * TILE_SIZE, MAP_HEIGHT * TILE_SIZE))
pygame.display.set_caption("Pygame Map System")
clock = pygame.time.Clock()

# 创建地图系统
map_system = MapSystem(screen)

# 加载角色图像，角色初始位置设定为 (0,0)
character_img = pygame.image.load("sample/character/reimu.png")
character_img = pygame.transform.scale(character_img, (TILE_SIZE, TILE_SIZE))
# 使用列表来维护角色的位置：[行, 列]
character_pos = [0, 0]

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # 键盘按下事件，控制角色移动
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if character_pos[0] > 0:
                    character_pos[0] -= 1
            elif event.key == pygame.K_DOWN:
                if character_pos[0] < MAP_HEIGHT - 1:
                    character_pos[0] += 1
            elif event.key == pygame.K_LEFT:
                if character_pos[1] > 0:
                    character_pos[1] -= 1
            elif event.key == pygame.K_RIGHT:
                if character_pos[1] < MAP_WIDTH - 1:
                    character_pos[1] += 1

    screen.fill((0, 0, 0))
    # 绘制地图
    map_system.draw()
    # 将角色绘制在地图之上，注意坐标：col 对应 X 轴，row 对应 Y 轴
    screen.blit(character_img, (character_pos[1] * TILE_SIZE, character_pos[0] * TILE_SIZE))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
