la_dreapta(X,Y) :- X =:= Y + 1.
 
la_stanga(X,Y) :- X =:= Y - 1.
 
langa(X, Y) :- la_dreapta(X,Y).
langa(X, Y) :- la_stanga(X,Y).
 
%casa(Numar,Nationalitate,Culoare,AnimalCompanie,Bautura,Tigari)
 
solutie(Strada,PosesorPeste) :- Strada = [
casa(1,_,_,_,_,_),
casa(2,_,_,_,_,_),
casa(3,_,_,_,_,_),
casa(4,_,_,_,_,_),
casa(5,_,_,_,_,_)],
 
member(casa(_,englez,rosie,_,_,_), Strada),
 
member(casa(S,_,albastru,_,_,_), Strada),
member(casa(P,norvegian,_,_,_,_), Strada),
langa(S, P),
 
member(casa(A,_,verde,_,_,_), Strada),
member(casa(B,_,alb,_,_,_), Strada),
la_stanga(A, B),
 
 
member(casa(_,_,verde,_,cafea,_), Strada),
 
member(casa(3,_,_,_,lapte,_), Strada),
 
member(casa(_,_,galben,_,_,'Dunhill'), Strada),
 
member(casa(1,norvegian,_,_,_,_), Strada),
 
member(casa(_,suedez,_,caine,_,_), Strada),
 
member(casa(_,_,_,pasare,_,'Pall Mall'), Strada),
 
member(casa(Z,_,_,pisica,_,_), Strada),
member(casa(T,_,_,_,_,'Malboro'), Strada),
langa(Z, T),
 
member(casa(_,_,_,_,bere,'Winfield'), Strada),
 
member(casa(U,_,_,cal,_,_), Strada),
member(casa(V,_,_,_,_,'Dunhill'), Strada),
langa(U, V),
 
member(casa(_,german,_,_,_,'Rothmans'), Strada),
 
member(casa(X,_,_,_,_,'Malboro'), Strada),
member(casa(Y,_,_,_,apa,_), Strada),
langa(Y, X),
 
member(casa(_,PosesorPeste,_,peste,_,_), Strada).