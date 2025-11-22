% Facts: gender
female(pam).
female(liz).
female(ann).
female(pat).

male(tom).
male(bob).
male(jim).

% Facts: parent relationships
parent(pam, liz).
parent(tom, liz).

parent(tom, bob).
parent(pam, bob).

parent(bob, ann).
parent(pat, ann).

parent(bob, jim).
parent(pat, jim).

% Mother relation
mother(M, C) :-
    female(M),
    parent(M, C).

% Father relation
father(F, C) :-
    male(F),
    parent(F, C).

% Grandfather relation
grandfather(GF, GC) :-
    male(GF),
    parent(GF, P),
    parent(P, GC).

% Grandmother relation
grandmother(GM, GC) :-
    female(GM),
    parent(GM, P),
    parent(P, GC).

% Sister relation
sister(S, X) :-
    female(S),
    parent(P, S),
    parent(P, X),
    S \= X.

% Brother relation
brother(B, X) :-
    male(B),
    parent(P, B),
    parent(P, X),
    B \= X.
