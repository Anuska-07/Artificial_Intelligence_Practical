parent(john,mary).
parent(john,peter).
parent(mary,david).
parent(mary,susan).
parent(peter,tom).
parent(peter,liz).
parent(susan, emma).
parent(susan, jack).

male(john).
male(peter).
male(david).
male(tom).
male(jack).

female(mary).
female(susan).
female(liz).
female(emma).

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

brother(X, Y) :-
    male(X),
    sibling(X, Y).  

sister(X, Y) :-
    female(X),
    sibling(X, Y).
    
child(X, Y) :-
    parent(Y, X).

son(X, Y) :-
    male(X),
    parent(Y, X).

daughter(X, Y) :-
    female(X),
    parent(Y, X).

ancestor(X, Y) :-
    parent(X, Y).
ancestor(X, Y) :-
    parent(X, Z),
    ancestor(Z, Y).

descendant(X, Y) :-
    ancestor(Y, X).