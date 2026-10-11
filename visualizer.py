# visualizer.py
import settings
import pygame

def bubble_color(i, step):
    if step is None:
        return "normal"
    if step["indices"] and i in step["indices"]:
        return "swapping" if step["type"] == "swap" else "comparing"
    if i >= step["sorted_from"]:
        return "sorted"
    return "normal"


def selection_color(i, step):
    if step is None:
        return "normal"
    if step["type"] == "swap" and i in step["indices"]:
        return "swapping"
    if i == step["min_idx"]:
        return "min"
    if step["indices"] and i in step["indices"]:
        return "comparing"
    if i < step["sorted_upto"]:
        return "sorted"
    return "normal"   


def search_color(i, step):
    if step is None:
        return "normal"
    if step["type"] == "found" and i == step["mid"]:
        return "found"
    elif i == step["mid"]:
        return "mid"
    elif step["left"]<=i<=step["right"]:
        return "range"
    else:
        return "excluded"      


COLOR_RULES = {
    "Bubble Sort": bubble_color,
    "Selection Sort": selection_color,
    "Binary Search": search_color,
}



STAT_LABELS_BUBBLE = {
    "comparisons": "Comparisons",
    "swaps": "Swaps",
    "pass": "Pass",
    "steps": "Steps",
}

STAT_LABELS_SELECTION = {
    "comparisons": "Comparisons",
    "swaps": "Swaps",
    "pass": "Pass",
    "steps": "Steps",
    "min_index": "Minimum index",
}

STAT_LABELS_BINARY = {
    "target": "Target",
    "comparisons": "Comparisons",
    "steps": "Steps",
    "current_range": "Current range",
    "result": "Result",
}

STAT_LABELS = {
    "Bubble Sort":    STAT_LABELS_BUBBLE,
    "Selection Sort": STAT_LABELS_SELECTION,
    "Binary Search":  STAT_LABELS_BINARY,
}

def draw_stats(screen, fonts, zones, step, labels):
    area = zones["stats"]
    stats = step["stats"] if step else {key: 0 for key in labels}
    for line, (key, title) in enumerate(labels.items(), start=1):
        label = fonts["small"].render(f"{title}: {stats[key]}", True, settings.TEXT_COLOR)
        screen.blit(label, (area.left + 10, area.top + line * 24))

def create_zones():
    return {
        "header":   pygame.Rect(0,   0,   1100, 60),
        "stats":    pygame.Rect(0,   60,  220,  550),
        "body":     pygame.Rect(220, 60,  850,  550),
        "legend":   pygame.Rect(0,   610, 1100, 60),
        "controls": pygame.Rect(0,   670, 1100, 30),
    }

def center_label(text, rect, font, screen):
    label = font.render(text, True, settings.TEXT_COLOR)
    screen.blit(label, label.get_rect(center=rect.center))

def draw_menu(screen, fonts, zones):
    center_label("Choose option:", zones["header"], fonts["big"], screen)
    for key, value in settings.POSSIBLE_ALGORITHMS.items():
        item = pygame.Rect(0, 0, settings.WIDTH, 40)
        item.centerx = settings.WIDTH // 2
        item.top = zones["body"].top + 60 + key * 50
        center_label(f"{key} - {value}", item, fonts["small"], screen)

def draw_columns(screen, fonts, state, zones):
    array, step = state["array"], state["step"]
    color_of = COLOR_RULES[state["mode"]]
    area = zones["body"].inflate(-2 * settings.MARGIN, -2 * settings.MARGIN)
    width_slot = area.width / len(array)
    for i, value in enumerate(array):
        h = value / settings.VALUE_MAX * area.height
        label = fonts["small"].render(str(value), True, settings.TEXT_COLOR)
        screen.blit(label, (area.left + i * width_slot, area.bottom + 5))
        
        color = settings.COLORS[color_of(i, step)]
        pygame.draw.rect(screen, color,(area.left + i * width_slot, area.bottom - h, width_slot - 2, h))

def draw_legend(screen, fonts, zones):
    area = zones["legend"]
    columns, rows = 3, 3
    col_w = area.width / columns
    row_h = area.height / rows
    for i, (key, text) in enumerate(settings.LEGEND_LABELS.items()):
        col, row = divmod(i, rows)         
        x = area.left + col * col_w + 10
        cy = area.top + row * row_h + row_h / 2
        box = pygame.Rect(x, 0, 14, 14)
        box.centery = cy
        pygame.draw.rect(screen, settings.COLORS[key], box)
        label = fonts["tiny"].render(text, True, settings.TEXT_COLOR)
        screen.blit(label, label.get_rect(midleft=(box.right + 8, cy)))

def draw(screen, fonts, state):
    zones = create_zones()
    screen.fill(settings.BG_COLOR)
    if state["screen"] == "menu":
        draw_menu(screen, fonts, zones)
    else:
        center_label(state["mode"], zones["header"], fonts["big"], screen)
        center_label(settings.CONTROLS_TEXT, zones["controls"], fonts["small"], screen)
        draw_legend(screen, fonts, zones)
        draw_columns(screen, fonts, state, zones)
        draw_stats(screen, fonts, zones, state["step"], STAT_LABELS[state["mode"]])


