% Monkey and Banana Problem

% Representing the state as:
% state(MonkeyPosition, MonkeyOnBox?, BoxPosition, HasBanana?)
% MonkeyPosition and BoxPosition: floor, box, banana
% MonkeyOnBox? : onbox / onfloor
% HasBanana? : yes / no

% Initial State:
% Monkey is on the floor, at door, box at window, no banana
% Goal State: Monkey has banana

% Move actions
move(state(middle, onbox, middle, no),
     grab,
     state(middle, onbox, middle, yes)).

move(state(P, onfloor, P, HB),
     climb,
     state(P, onbox, P, HB)).

move(state(P, onbox, P, HB),
     climbdown,
     state(P, onfloor, P, HB)).

move(state(P1, onfloor, P1, HB),
     push(P1, P2),
     state(P2, onfloor, P2, HB)).

move(state(P1, onfloor, BP, HB),
     walk(P1, P2),
     state(P2, onfloor, BP, HB)).

% Plan to get banana
canget(state(_, _, _, yes)).
canget(State1) :-
    move(State1, Move, State2),
    write('Monkey does: '), write(Move), nl,
    canget(State2).

% Run example:
% ?- canget(state(door, onfloor, window, no)).
