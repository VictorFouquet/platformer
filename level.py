import os

import plateform as pf
from enemy import Enemy
from items import Item

class Level:
    def __init__(self, ref, plateforms, enemies, items):
        with open(ref, 'r') as f:
            rows = f.readlines()
        self.content = [[cell for cell in row] for row in rows]
        self.plateforms = plateforms
        self.enemies = enemies
        self.items = items


LEVELS = [
    Level(
        os.path.join(os.getcwd(), 'levels', 'scr1.txt'),
        [],
        [
            Enemy([
                40,
                20,
                1,
                [
                    "-'-,,-'-,,>",
                    ",,-'-,,-'->",
                    "-,,-'-,,-'>",
                    "'-,,-'-,,->",
                ],
                [
                    "<,,-'-,,-'-",
                    "<-'-,,-'-,,",
                    "<'-,,-'-,,-",
                    "<-,,-'-,,-'"
                ],
                
                0,
                19,
                60
            ]),
            Enemy([
                18,
                32,
                1,
                [
                    "-'-,,-'-,,>",
                    ",,-'-,,-'->",
                    "-,,-'-,,-'>",
                    "'-,,-'-,,->",
                ],
                [
                    "<,,-'-,,-'-",
                    "<-'-,,-'-,,",
                    "<'-,,-'-,,-",
                    "<-,,-'-,,-'"
                ],
                
                0,
                32,
                56
            ])
        ],
        [            
            Item([
                27,
                87,
                0,
                [*['|' for _ in range(10)], *['$' for _ in range(10)]]
            ])
        ]
    ),
    Level(
        os.path.join(os.getcwd(), 'levels', 'scr2.txt'),
        [],
        [
            Enemy([
                18,
                32,
                1,
                [
                    ",,-'-,,-'-,,>",
                    "'-,,-'-,,-'->",
                    "-'-,,-'-,,-'>",
                    ",-'-,,-'-,,->",
                ],
                [
                    "<,,-'-,,-'-,,",
                    "<-'-,,-'-,,-'",
                    "<'-,,-'-,,-'-",
                    "<-,,-'-,,-'-,"
                ],
                
                0,
                32,
                56
            ]),
            Enemy([
                40,
                38,
                1,
                [
                    ",,-'-,,-'-,,>",
                    "'-,,-'-,,-'->",
                    "-'-,,-'-,,-'>",
                    ",-'-,,-'-,,->",
                ],
                [
                    "<,,-'-,,-'-,,",
                    "<-'-,,-'-,,-'",
                    "<'-,,-'-,,-'-",
                    "<-,,-'-,,-'-,"
                ],
                
                0,
                38,
                61
            ])
        ],
        [
            Item([
                26,
                112,
                0,
                [*['|' for _ in range(10)], *['$' for _ in range(10)]]
            ])
        ]
    ),
    Level(
        os.path.join(os.getcwd(), 'levels', 'scr3.txt'),
        [
            pf.HorizontalMover([16,91,8,1,91,120])
        ],
        [
            Enemy([
                32,
                62,
                1,
                [
                    ",,-'-,,-'-,,>",
                    "'-,,-'-,,-'->",
                    "-'-,,-'-,,-'>",
                    ",-'-,,-'-,,->",
                ],
                [
                    "<,,-'-,,-'-,,",
                    "<-'-,,-'-,,-'",
                    "<'-,,-'-,,-'-",
                    "<-,,-'-,,-'-,"
                ],
                
                0,
                62,
                93
            ]),
            Enemy([
                18,
                32,
                1,
                [
                    ",,-'-,,-'-,,>",
                    "'-,,-'-,,-'->",
                    "-'-,,-'-,,-'>",
                    ",-'-,,-'-,,->",
                ],
                [
                    "<,,-'-,,-'-,,",
                    "<-'-,,-'-,,-'",
                    "<'-,,-'-,,-'-",
                    "<-,,-'-,,-'-,"
                ],
                
                0,
                32,
                56
            ])
        ],
        [
            Item([
                22,
                130,
                0,
                [*['|' for _ in range(10)], *['$' for _ in range(10)]]
            ])
        ]
    ),
    Level(
        os.path.join(os.getcwd(), 'levels', 'scr4.txt'),
        [
            pf.VerticalMover([27,114,8,1,8,27])
        ],
        [
            Enemy([
                18,
                26,
                1,
                [
                    ",,-'-,,-'-,,>",
                    "'-,,-'-,,-'->",
                    "-'-,,-'-,,-'>",
                    ",-'-,,-'-,,->",
                ],
                [
                    "<,,-'-,,-'-,,",
                    "<-'-,,-'-,,-'",
                    "<'-,,-'-,,-'-",
                    "<-,,-'-,,-'-,"
                ],
                
                0,
                26,
                51
            ]),
            Enemy([
                18,
                51,
                -1,
                [
                    "<,,-'-,,-'-,,",
                    "<-'-,,-'-,,-'",
                    "<'-,,-'-,,-'-",
                    "<-,,-'-,,-'-,"
                ],
                [
                    ",,-'-,,-'-,,>",
                    "'-,,-'-,,-'->",
                    "-'-,,-'-,,-'>",
                    ",-'-,,-'-,,->",
                ],
                
                0,
                26,
                51
            ]),
        ],
        [
            Item([
                7,
                118,
                0,
                [*['|' for _ in range(10)], *['$' for _ in range(10)]]
            ])
        ]
    ),
    Level(
        os.path.join(os.getcwd(), 'levels', 'scr5.txt'),
        [
            pf.CircularMover([30,40,8,1,0,0], 8, 1),
            pf.CircularMover([30,100,8,-1,0,0], 8, 1),
            pf.VerticalMover([22,66,8,-1,10,22]),
            pf.HorizontalMover([10,4,8,1,4,60]),
            pf.HorizontalMover([6,122,8,1,70,122])
        ],
        [],
        [
            Item([
                5,
                126,
                0,
                [*['|' for _ in range(10)], *['$' for _ in range(10)]]
            ])
        ]
    ),
    Level(
        os.path.join(os.getcwd(), 'levels', 'scr6.txt'),
        [
            
        ],
        [],
        []
    ),
    Level(
        os.path.join(os.getcwd(), 'levels', 'loose.txt'),
        [
            
        ],
        [],
        []
    ),
    Level(
        os.path.join(os.getcwd(), 'levels', 'win.txt'),
        [
            
        ],
        [],
        []
    )
]