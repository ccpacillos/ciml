import table

trainingData = table.Table(
    ['easy', 'ai', 'sys', 'thy', 'morning', 'rating'],
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
        ['y', 'n', 'y', 'n', 'n', -2]
    ])
