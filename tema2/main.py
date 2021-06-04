# Ciobanu Alin-Matei 335CB
import sys
from typing import List, Tuple, Set, Dict

def epsilonClosure(delta, state):
	eps = set()
	eps.add(state)
	for (state, e) in delta.keys():
		if state in eps:
			if e == "eps":
				for nextState in delta[(state, e)]:
					eps.add(nextState)
	return sorted(eps)

def onestep(delta, state, c):
	s = set()
	if (state, c) in delta.keys():
		for nextState in delta[(state, c)]:
			s.update(epsilonClosure(delta, nextState))

	return s

def isInList(l, L):
	if L == []:
		return False
	for (state, l2) in L:
		if l2 == l:
			return True
	return False 

def findStateInL(l, L):
	for (state, l2) in L:
		if l2 == l:
			return state
	return None

def findListInL(state, L):
	for (st, l) in L:
		if st == state:
			return l
	return []

if __name__ == "__main__":
	f = open(sys.argv[1])
	g = open(sys.argv[2], "w")
	numberOfStates = int(f.readline())
	l = f.readline().split()
	final_states = []
	for c in l:
		final_states.append(int(c))

	lines = f.readlines()
	d = {}
	alphabet = set()
	for line in lines:
		l = line.split()
		s1 = int(l[0])
		var = l[1]
		if var != "eps":
			alphabet.add(var) # adaug caracterele in alphabet
		d[(s1, var)] = []
		for i in range(2, len(l)):
			d[(s1, var)].append(int(l[i]))

	alphabet = sorted(alphabet)

	state = 0
	current_state = 0
	L = [] # contine perechi (state, list_of_states), asociez o stare pt fiecare stare compusa
	dfa = {} # delta pentru dfa

	eps = epsilonClosure(d, 0)
	L.append((0, list(eps))) # starea initiala din dfa va fi eps(0) pe care o mapez prin starea 0

	state = 1
	while(current_state < len(L)):
		l = findListInL(current_state, L)
		for c in alphabet:
			l2 = [] # starea compusa in care ma duc intr-un pas pe caracterul curent
			for j in l: # parcurg starea compusa
				l2 = l2 + list(onestep(d, j, c)) # si vad ce tranzitii am pe caracterul curent
			l2 = list(dict.fromkeys(l2)) # elimin duplicatele
			if not isInList(l2, L): # daca nu o am deja in L
				L.append((state, l2)) # o adaug si ii asociez o stare formata doar dintr-un nr
				state += 1
			dfa[(current_state, c)] = findStateInL(l2, L) # adaug tranzitia in delta
		current_state += 1

	finalDFA = set() # starile finale
	for (state, l) in L:
		for i in final_states:
			if i in l:
				finalDFA.add(state)

	g.write(str(len(L)) + "\n")
	for qf in finalDFA:
		g.write(str(qf) + " ")
	g.write("\n")
	for (state, c) in dfa:
		g.write(str(state) + " ")
		g.write(c + " ")
		g.write(str(dfa[(state, c)]))
		g.write("\n")

