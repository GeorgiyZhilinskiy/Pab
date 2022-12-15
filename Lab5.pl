domains
	subject = symbol
	department = symbol	 
	person = symbol
	groupnum = symbol
	exammark = integer
predicates
	% Группа относится к кафедре 
	kaf(department, group)

	% Студент учится в указанной группе
	group(person, groupnum) 

	% Указанная персона является студентом
	student(person)

	% Студент по указанному предмету получил такую-то оценку 	
	exam(subject, person, exammark).
	
	kafst(person, department)
	student(person, department)
clauses
	kaf(math, m1). % кафедра математики, группа m1
	kaf(math, m2). % кафедра математики, группа m2
	kaf(gum, g1). % кафедра гуманитарных наук, группа g1
	kaf(lang, l1). % кафедра языков, группа l1
	kaf(phis, p1). %кафедра физики, группа p1
	kaf(leg, a1). %кафедра физики, группа p1


	student(lisa). % студент Лиза
	student(andrey). 
	student(maria). 
	student(egor). 
	student(dima). 
	student(olga). 

	group(lisa, l1). % Лиза - студент группы l1
	group(andrey, m1). % Андрей - студент группы m1
	group(maria, m2). % Мария - студент группы m2
	group(egor, l1). % Егор - студент группы l1
	group(dima, g1). % Дима - студент группы g1
	group(olga, p1). % Ольга - студент группы p1

	study(andrey, math).
	study(andrey, phis).
	study(lisa, russ).
	study(lisa, eng).
	study(dima, hist).
	study(dima, econom).
	study(olga, phis).
	study(olga, math).
	study(egor, lit).
	study(egor, eng).
	study(maria, econom).

	exam(math, andrey, 5).
	exam(russ, lisa, 5).
	exam(eng, lisa, 4).
	exam(econom, maria,5).
	exam(phis, andrey, 5).
	exam(hist, dima, 3).
	exam(eng, egor, 3).
	exam(lit, egor, 3).
	exam(phis, olga, 4).
	exam(math, olga, 4).
	exam(phis, maria, 5).
goal 
	% Студент обучается на кафедре, если он обучается в группе относящейся к кафедре 	
	student(ST, KF) :- kaf(KF, GR), group(ST, GR).
	kafst(X, Y) :- kaf(Y, G), group(X,G).


