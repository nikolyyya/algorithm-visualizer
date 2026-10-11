# main.py
import pygame
import settings
import visualizer
import random
import algorithms

ALGORITHMS = {
    "Bubble Sort": algorithms.bubble_sort_steps,
    "Selection Sort": algorithms.selection_sort_steps,
    "Binary Search": algorithms.binary_search_steps,
}

def create_state():
    return {
        "running": False,     
        "mode": "-",
        "array": [],
        "generator": None,
        "timer": 0, 
        "screen": "menu",
        "step": None,
        "target": None,          
    }

def advance(state):
    if state["generator"] is None:
        if state["mode"] == "Binary Search":
            state["generator"] = ALGORITHMS[state["mode"]](state["array"], state["target"])
        else:
            state["generator"] = ALGORITHMS[state["mode"]](state["array"])
    try:
        state["step"] = next(state["generator"])
    except StopIteration:
        state["running"] = False     

def reset_state(state):
    state["generator"] = None
    state["timer"] = 0
    state["array"] = []
    state["step"] = None
    state["running"] = False
    state["target"] = None

def generate_array(state):
    count = random.randint(settings.ARRAY_SIZE_MIN, settings.ARRAY_SIZE_MAX)
    state["array"] = [random.randint(settings.VALUE_MIN, settings.VALUE_MAX) for _ in range(count)]

def generate_target(state):
    state["target"] = random.choice(state["array"])

def main():
    pygame.init()

    screen = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))
    pygame.display.set_caption("MySort")
    clock = pygame.time.Clock()

    fonts = {
        "big": pygame.font.Font(None, settings.FONT_BIG_SIZE),
        "small": pygame.font.Font(None, settings.FONT_SMALL_SIZE),
        "tiny": pygame.font.Font(None, settings.FONT_TINY_SIZE)
    }

    state = create_state()

    active = True
    while active:
        dt = clock.tick(settings.FPS) 

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                active = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    active = False
                elif event.unicode.isdigit() and "1"<=event.unicode<="3":
                    reset_state(state)
                    state["mode"] = settings.POSSIBLE_ALGORITHMS[int(event.unicode)]
                    state["screen"] = "main_field"
                    generate_array(state)
                    if state["mode"] == "Binary Search":
                        generate_target(state)
                        state["array"].sort()
                elif event.key == pygame.K_m:
                    reset_state(state)
                    state["screen"] = "menu"
                elif state["screen"] == "main_field":
                    if event.key == pygame.K_r:
                        reset_state(state)
                        generate_array(state)
                        if state["mode"] == "Binary Search":
                            state["array"].sort()
                            generate_target(state)
                    elif event.key == pygame.K_n:
                        advance(state)
                    elif event.key == pygame.K_SPACE:
                        state["running"] = not state["running"]


        if state["running"]:
            state["timer"] += dt
            if state["timer"] >= settings.STEP_DELAY_MS:
                state["timer"] -= settings.STEP_DELAY_MS
                advance(state)
        visualizer.draw(screen, fonts, state)
        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()

