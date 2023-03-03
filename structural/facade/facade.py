class GraphicsEngine:
    def render(self, character_pos, enemy_pos):
        print(f"Rendering character at {character_pos} and enemy at {enemy_pos}.")

class PhysicsEngine:
    def update(self, character_pos, enemy_pos):
        print(f"Updating character position to {character_pos} and enemy position to {enemy_pos}.")

class EnemyGenerator:
    def generate(self):
        print("Generating enemy.")

class SoundSystem:
    def play_sound(self, sound):
        print(f"Playing {sound} sound.")

class GameFacade:
    def __init__(self):
        self.graphics_engine = GraphicsEngine()
        self.physics_engine = PhysicsEngine()
        self.enemy_generator = EnemyGenerator()
        self.sound_system = SoundSystem()

    def play(self):
        character_pos = (0, 0)
        enemy_pos = (100, 100)

        self.graphics_engine.render(character_pos, enemy_pos)
        self.physics_engine.update(character_pos, enemy_pos)
        self.enemy_generator.generate()
        self.sound_system.play_sound("background_music")

def main():
    game = GameFacade()
    game.play()

if __name__ == '__main__':
    main()
