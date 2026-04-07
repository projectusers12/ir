links = {'A': ['B', 'C'], 'B': ['C'], 'C': ['A']}
PR = {'A': 1.0, 'B': 1.0, 'C': 1.0}


print("Iteration 0:", {k: round(v, 4) for k, v in PR.items()})

for i in range(1, 3):  
    for p in links:
       
        incoming = sum(PR[q] / len(links[q]) for q in links if p in links[q])
        
      
        PR[p] = 0.15 + 0.85 * incoming
        
   
    print(f"Iteration {i}:", {k: round(v, 4) for k, v in PR.items()})
