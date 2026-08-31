
try:
    n, x = map(int, input().split())
except ValueError:
    print("Input must have only two numbers with space!")
else:
    machines_by_year = {}
    for _ in range(n):
        try:
            year, cost, time = map(int, input().split())
        except ValueError:
            print("Input must have 3 numbers with space(year cost time), example: 2023 1000 34. Try again!")
            exit()
        else:
            if year not in machines_by_year:
                machines_by_year[year] = []
            machines_by_year[year].append((cost, time))

    min_cost = float('inf')

    for year, machines in machines_by_year.items():
        for i in range(len(machines)):
            for j in range(i + 1, len(machines)):
                if machines[i][1] + machines[j][1] == x and machines[i][0] + machines[j][0] < min_cost:
                    min_cost = machines[i][0] + machines[j][0]
        
    if min_cost == float('inf'):
        print("No solution")
    else:
        print(min_cost)
  
