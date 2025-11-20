# map_coloring.py
def mrv_select(unassigned, domains):
    return min(unassigned, key=lambda v: len(domains[v]))

def consistent(var, color, assignment, neighbors):
    for n in neighbors.get(var, []):
        if assignment.get(n)==color:
            return False
    return True

def backtrack(assignment, variables, domains, neighbors):
    if len(assignment)==len(variables):
        return assignment
    unassigned=[v for v in variables if v not in assignment]
    var=mrv_select(unassigned, domains)
    for value in domains[var]:
        if consistent(var, value, assignment, neighbors):
            assignment[var]=value
            # forward-checking: reduce neighbor domains temporarily
            saved={}
            for n in neighbors.get(var,[]):
                if n not in assignment and value in domains[n]:
                    saved[n]=domains[n].copy()
                    domains[n]=[c for c in domains[n] if c!=value]
            result=backtrack(assignment, variables, domains, neighbors)
            if result:
                return result
            del assignment[var]
            for n,v in saved.items():
                domains[n]=v
    return None

if __name__=="__main__":
    variables = ['A','B','C','D']
    neighbors = {'A':['B','C'], 'B':['A','C','D'], 'C':['A','B','D'], 'D':['B','C']}
    colors = ['Red','Green','Blue']
    domains = {v:colors.copy() for v in variables}
    sol = backtrack({}, variables, domains, neighbors)
    print("Solution:", sol)
