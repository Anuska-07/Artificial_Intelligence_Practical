parent(niraj,anuska).
parent(nisha,anuska).
parent(niraj,aarya).
parent(nisha,aarya).
parent(niraj,nitisha).
parent(nisha,nitisha).
parent(lava,nisha).
parent(nirmala,nisha).
parent(lava,chhaya).
parent(nirmala,chhaya).
parent(lava,richa).
parent(nirmala,richa).
parent(lava,richan).
parent(nirmala,richan).

male(niraj).
male(lava).
male(richan).

female(nisha).
female(nitisha).
female(anuska).
female(aarya).
female(nirmala).
female(chhaya).
female(richa).

father(X,Y) :-
    male(X),
    parent(X,Y).

mother(X,Y) :-
    parent(X,Y),
    female(X).

grandparent(X, Y) :-
    parent(X, Z),
    parent(Z, Y).

sibling(X, Y) :-
    parent(Z, X),
    parent(Z, Y),
    X \= Y.

sister(X, Y) :-
    female(X),
    sibling(X, Y).

ancestor(X, Y) :-
    parent(X, Y).
ancestor(X, Y) :-
    parent(X, Z),
    ancestor(Z, Y).

descendant(X, Y) :-
    ancestor(Y, X).