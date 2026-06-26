enum Direction{
    Up,
    Down,
    Left,
    Right
}


function move(direction: Direction) {
    console.log(`MOving ${Direction[direction].toLowerCase()}`)
}

move(Direction.Left)