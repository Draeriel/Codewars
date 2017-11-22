import itertools
def choose_best_sum(t, k, ls):
  posibilidades = []
  lista = list(itertools.combinations(ls, k))
  for recorridos in lista:
    if sum(recorridos) <= t:
      posibilidades.append(sum(recorridos))
  if len(posibilidades) == 0:
      return None
  return max(posibilidades) 