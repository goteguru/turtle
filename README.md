# Simple Turtle library

Basic turtle API for PyGame (or other drawing lib). This turtle lib stores (and returns) the turtle's path instead of drawing it.
Api functions are supporting method chaining. 

### Turtle properties

| property             | description                       |
|----------------------|-----------------------------------|
|Turtle.origin -> (x,y)|x,y screen coordinates of starting position|
|path -> [points]      |turtle path (list of (x,y) tuples) |
|angle -> a            | starting angle |         

### Turtle methods

|     method            |description                             |
|-----------------------|----------------------------------------|
|turn(angle) -> self    | turn right <angle> degrees. left if negative.|
|go(dist) -> self       | go forward <dist> units (backwards if negative)|
|close() -> self        | close to the start point|


## Example

Turtle((20,30)).go(10).turn(90).go(10).turn(90).go(10).turn(90).go(10).path

## Advanced examples

Sokszög, Kereszt, nyíl. rajzoló rutinok.
optimálisan objektumként.


## pygame displaying


