from ortools.sat.python import cp_model

def solveNQueens(N):
    model = cp_model.CpModel()
    queens = [model.NewIntVar(0, N - 1, f'x{i}') for i in range(N)]

    # Ensure no two queens threaten each other
    for i in range(N):
        for j in range(i + 1, N):
            model.Add(queens[i] != queens[j])
            model.Add(queens[i] - queens[j] != i - j)
            model.Add(queens[i] - queens[j] != j - i)

    solver = cp_model.CpSolver()
    status = solver.Solve(model)

    solutions = []
    if status == cp_model.FEASIBLE:
        solution = [solver.Value(queen) for queen in queens]
        solutions.append(solution)

    return solutions