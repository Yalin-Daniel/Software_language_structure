%yalin daniel 32491590

% introduction

% Assumption: in married(X,Y), X is always the man and Y is always the woman.
% parents
parent(orly, yalin).
parent(sara, orly).
parent(sara, shirley).
parent(shirley, ori).

% male
male(maoz).
male(ori).
male(keren).
male(doron).
male(joseph).

% female
female(yalin).
female(orly).
female(sara).
female(shirley).
% married
married(doron, orly).
married(joseph, sara).
married(keren, shirley).

% 1 - X is the father of Y
father(X,Y):-
    parent(X,Y),
    male(X).

% 2 - X is the mother of Y
mother(X,Y):-
    parent(X,Y),
    female(X).

% 3 - X is the son of Y
son(X,Y):-
    parent(Y,X),
    male(X).


% 4 - X is the daughter  of Y
daughter(X,Y):-
    parent(Y,X),
    female(X).
% 5 - X is the grandfather of Y
grandfather(X,Y):-
    parent(X,Z),
    parent(Z,Y),
    male(X).

% 6 - X is the grandmother of Y
grandmother(X,Y):-
    parent(X,Z),
    parent(Z,Y),
    female(X).

% 7 - X is the grandson of Y
grandson(X,Y):-
    parent(Y,Z),
    parent(Z,X),
    male(X).

% 8 - X is the granddaughter of Y
granddaughter(X,Y):-
    parent(Y,Z),
    parent(Z,X),
    female(X).

% 9 - X is the Sibling of Y
sibling(X,Y):-
    parent(Z,X),
    parent(Z,Y),
    X \= Y. %A person is not his own brother

% 10 - X is the uncle of Y without blood connection
uncle_not_connection_blood(X,Y):-
    parent(Z,Y),
    sibling(W,Z),
    married(X,W).

% 11 - X is the son of Y's aunt
cousin(X,Y):-
    male(X),
    parent(Z,X),
    female(Z),
    parent(W,Y),
    sibling(Z,W).

% 12 -  X is the brother_in_law of Y
brother_in_law(X,Y):-
    male(X),
    married(X,Z),
    sibling(Z,Y).


% 13 - X is the Niece of Y
niece(X,Y):-
    sibling(Y,Z),
    parent(Z,X),
    female(X).

% 14.a - X and Y are cousins
cousins(X,Y):-
    parent(A,X),
    parent(B,Y),
    sibling(A,B).

% 14.b - X and Y are second cousins
second_cousins(X,Y):-
    parent(Z,X),
    parent(W,Y),
    cousins(Z,W).
    
	
	

%Recursion and lists

% 1 
% Tail recursion (I know they didn't ask for it, but for self practice)
reverse_Tail(L,Z):-
    reverse_acc(L,[],Z).

reverse_acc([],Acc,Acc). % Stopping condition

reverse_acc([X|Xrest],Acc,Result):-
    reverse_acc(Xrest,[X|Acc],Result).

% regular recursion
reverse([],[]).
reverse([X|Xtail],Z):-
    reverse(Xtail,R),
    append(R,[X],Z).

% 2
%X is a member of L if one of two things is true:
%X is the head of the list.
%Or X is in the tail of the list.
member(X,[X|Tail]).
member(X,[Head|Tail]):-
    member(X,Tail).

% 3 
palindrome(L):-
    %reverse(L,X),
    %reverse(X,L).
	reverse(L,L).

% 4
%At each step, two adjacent elements are checked: Y >= X
%and then continue from the list that begins with Y.

sorted([]).
sorted([_]). %list with one number
sorted([X,Y|Rest]):-
    Y>=X,
    sorted([Y|Rest]).

% 5 
/*
If the list is empty — its permutation is also empty.
If the list is [X|L], then:
First we permute the tail of L
Then we insert X into any possible place within the permutation we received.
*/
permutation([],[]).
permutation([X|L],P):-
    permutation(L,L1),
    insert(X,L1,P).

% Delete X when X is the head of the list
del(X,[X|Xs],Xs).

% Keep Y and continue deleting X from the tail
del(X,[Y|Xs],[Y|Ys]):-
    del(X,Xs,Ys).


% Insert X anywhere into List and return the bigger list in Res
insert(X,List,Res):-
    del(X,Res,List).



% Arithmetic

% 1.a
scum(1,1).
scum(N,Res):-
    N>1,
    N1 is N-1,
    scum(N1,Temp),
    Res is Temp+N.

% 1.b
sumDigits(0,0).
sumDigits(Num,Sum):-
    Num > 0,
    Digit is Num mod 10,
    NumTemp is Num // 10,
    sumDigits(NumTemp,Temp),
    Sum is Temp + Digit.

% 2.a
split(0,[]).
split(N,Res):-
    N>0,
    Digit is N mod 10,
    NumTemp is N // 10,
    split(NumTemp,Temp),
    append(Temp,[Digit],Res).    

% 2.b
create([],0).
create([X|Rest],N):-
    create(Rest,Temp),
    N is X + 10*Temp.
    
% 2.c
split_create(Num,Reverse_number):-
    split(Num,List),
    create(List,Reverse_number).

% 3.a
%Recursively traverse L1, and check each element to see if it is a member of L2.
intersection([],L2,[]).

intersection([X1|Rest1],L2,[X1|Z]):-
    member(X1,L2),
    intersection(Rest1,L2,Z).

intersection([X1|Rest1],L2,Z):-
    \+ member(X1,L2),
    intersection(Rest1,L2,Z).
   

% 3.b
minus([],L2,[]).

minus([X|Rest],L2,Z):-
    member(X,L2),
    minus(Rest,L2,Z).

minus([X|Rest],L2,[X|Z]):-
    \+ member(X,L2),
    minus(Rest,L2,Z).




































    





















