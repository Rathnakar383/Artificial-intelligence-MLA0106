% sum_n(N, Sum) :- Sum is the sum of integers from 1 to N.

sum_n(0, 0) :- !.      % Base case: sum from 1 to 0 is 0
sum_n(N, Sum) :-
    N > 0,
    N1 is N - 1,        % Decrement N
    sum_n(N1, PrevSum), % Recursive call
    Sum is PrevSum + N. % Add N to the previous sum