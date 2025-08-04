maximum_pred(A, B, M) :- A > B, M = A.
maximum_pred(A, B, M) :- A =< B, M = B.

member_pred_aux(_, [], _, -1) :- !.
member_pred_aux(X, [X|_], P, P) :- !.
member_pred_aux(X, [H|T], P, N) :- X \=  H, 
    							   A is P + 1, 
                                   member_pred_aux(X, T, A, N).

member_pred(X, L, Sol) :- member_pred_aux(X, L, 1, Sol).

cancat_pred_aux(L, [], L) :- !.
cancat_pred_aux(L1, [H|T], S) :- cancat_pred_aux([L1|H], T, S).

cancat_pred([], L, L) :- !.
cancat_pred(L, [], L) :- !.
cancat_pred(L1, L2, Sol) :- cancat_pred_aux(L1, L2, Sol).