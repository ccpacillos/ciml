from .lib import table

headers = ['easy', 'ai', 'sys', 'thy', 'morning', 'rating']

trainingData = table.Table(
    headers,
    [
        ['y', 'y', 'n', 'y', 'n', 2],
        ['n', 'y', 'n', 'n', 'n', 2],
        ['n', 'y', 'y', 'n', 'y', 2],
        ['y', 'y', 'n', 'y', 'n', 1],
        ['n', 'n', 'n', 'n', 'y', 0],
        ['n', 'y', 'n', 'y', 'n', 0],
        ['y', 'y', 'y', 'n', 'y', -1],
        ['n', 'n', 'y', 'n', 'y', -1],
        ['n', 'n', 'y', 'y', 'n', -2],
        ['y', 'n', 'y', 'n', 'n', -2],
        ['n', 'n', 'n', 'y', 'n', 2],
        ['y', 'y', 'n', 'n', 'n', 1],
        ['n', 'y', 'n', 'y', 'n', 1],
        ['y', 'n', 'n', 'y', 'y', 0],
        ['n', 'n', 'y', 'y', 'n', -1],
        ['y', 'n', 'y', 'n', 'y', -1]
    ])


testData = table.Table(
    headers,
    [
        ['y', 'y', 'n', 'y', 'n', 2],
        ['y', 'y', 'y', 'y', 'y', 0],
        ['n', 'y', 'y', 'n', 'y', -2],
        ['y', 'n', 'y', 'n', 'y', -2]
    ]
)
