#!/usr/bin/env python

import pyagram


background = (0, 0, 0)
foreground = (255, 255, 255)

#background = (255, 255, 255)
#foreground = (0, 0, 0)

#background = (255, 128, 0)
#foreground = (0, 0, 255)


GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
PURPLE = (128, 0, 128)
BROWN = (128, 64, 0)
RED = (255, 0, 0)

points = [
    [GREEN],
    [False, YELLOW],
    [False, False, PURPLE, PURPLE],
    [False, False, PURPLE, False],
    [False, YELLOW, PURPLE],
    [False, YELLOW],
    [False, False, YELLOW, PURPLE],
    [False, BROWN, False, PURPLE],
    [GREEN, False],
    [False, RED, False],
    [GREEN, YELLOW]
]

connections = [
    [[0, 1]],
    [[0], [1, 2, 3]],
    [[0], [1], [2], [3]],
    [[0], [1], [1], [2]],
    [[0], [1], [1]],
    [[0], [1, 2, 3]],
    [[0], [1], [2], [3]],
    [[0], [0], [1], []],
    [[0, 1], [2]],
    [[0], [0, 1], [1]],
    [[0], [1]]
]

names = [
    [['Master Alpha 1.0.0', 'Project created']],
    [['', ''], ['Development', 'New features']],
    [['', ''], ['', ''], ['Feature', 'Special abilities'], ['Feature', 'New items']],
    [['', ''], ['', ''], ['Testing', 'Special abilities'], ['', '']],
    [['', ''], ['Development', 'Merged special abilities'], ['Testing', 'New items']],
    [['', ''], ['Development', 'Merged new items']],
    [['', ''], ['', ''], ['Development', ''], ['Feature', 'Combo abilities']],
    [['', ''], ['Pre-Release', 'Testing'], ['', ''], ['Scrapped', 'Combo abilities']],
    [['Master 1.0', 'Merged new features'], ['', '']],
    [['', ''], ['Quickfix', 'Glitchy item rendering fixed'], ['', '']],
    [['Master 1.1', 'Merged quickfix'], ['Development', '']]
]

o = pyagram.TreeDiagram(points, connections,
                             foreground=foreground,
                             background=background)
print(o.export('tree-diagram.png'))
o.interactive(names)
