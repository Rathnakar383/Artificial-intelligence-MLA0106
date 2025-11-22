% Facts: fruit and its color
fruit_color(apple, red).
fruit_color(apple, green).
fruit_color(banana, yellow).
fruit_color(grape, green).
fruit_color(grape, purple).
fruit_color(orange, orange).
fruit_color(mango, yellow).
fruit_color(blueberry, blue).

% Rule to find fruit by color
find_fruit_by_color(Color, Fruit) :-
    fruit_color(Fruit, Color).

% Rule to find color by fruit
find_color_by_fruit(Fruit, Color) :-
    fruit_color(Fruit, Color).
