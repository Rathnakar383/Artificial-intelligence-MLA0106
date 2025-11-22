% Facts about birds and their flying ability
can_fly(sparrow).
can_fly(parrot).
can_fly(eagle).
can_fly(pigeon).

cannot_fly(penguin).
cannot_fly(ostrich).
cannot_fly(kiwi).

% Rule to check if a bird can fly
bird_can_fly(Bird) :-
    can_fly(Bird),
    write(Bird), write(' can fly.'), nl.

bird_can_fly(Bird) :-
    cannot_fly(Bird),
    write(Bird), write(' cannot fly.'), nl.

% Example queries:
% ?- bird_can_fly(sparrow).
% ?- bird_can_fly(penguin).
% ?- bird_can_fly(ostrich).
