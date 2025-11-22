% ---------- Knowledge Base ----------
% Facts: known facts in the system
fact(has_fever, no).
fact(has_cough, no).
fact(has_sore_throat, no).
fact(has_bacterial_infection, no).
fact(should_take_antibiotic, no).

% Rules: forward chaining inference rules
rule(has_bacterial_infection, [has_fever, has_sore_throat]).
rule(should_take_antibiotic, [has_bacterial_infection]).

% ---------- Forward Chaining Engine ----------
forward_chain :-
    new_fact(Fact),
    \+ fact(Fact, yes),             % if fact not already known as yes
    assertz(fact(Fact, yes)),       % mark as true
    write('Derived: '), write(Fact), nl,
    forward_chain.
forward_chain :- !.                 % stop when no more facts can be derived

% Find a new fact from rules
new_fact(Fact) :-
    rule(Fact, Conditions),
    all_conditions_true(Conditions).

% Check if all conditions are true
all_conditions_true([]).
all_conditions_true([Cond | Rest]) :-
    fact(Cond, yes),
    all_conditions_true(Rest).

% ---------- Start with initial facts ----------
set_initial_facts :-
    retractall(fact(_, _)),
    write('Does the person have fever? (yes/no): '),
    read(Fever), assertz(fact(has_fever, Fever)),
    write('Does the person have cough? (yes/no): '),
    read(Cough), assertz(fact(has_cough, Cough)),
    write('Does the person have sore throat? (yes/no): '),
    read(Throat), assertz(fact(has_sore_throat, Throat)).

% ---------- Main Predicate ----------
start :-
    set_initial_facts,
    forward_chain,
    fact(should_take_antibiotic, yes) ->
        write('Conclusion: Patient should take antibiotics.');
        write('Conclusion: Antibiotics not required.').
