% Backward Chaining Example: Medical Advice System

% Facts: Symptoms
fever(john).
cough(john).
sore_throat(john).

% Rules: Diagnosing illness
illness(Person, flu) :-
    fever(Person),
    cough(Person),
    sore_throat(Person).

illness(Person, cold) :-
    cough(Person),
    sore_throat(Person).

% Rules: Advice based on illness
advice(Person, take_rest) :-
    illness(Person, flu).

advice(Person, drink_warm_fluids) :-
    illness(Person, cold).

advice(Person, see_doctor) :-
    illness(Person, flu),
    fever(Person).

% Example Queries:
% ?- illness(john, flu).
% ?- advice(john, Action).
