links = {'A': ['B', 'C'], 'B': ['C'], 'C': ['A']}
PR = {'A': 1.0, 'B': 1.0, 'C': 1.0}

# 1. Print the initial starting state (all 1s) as requested
print("Iteration 0:", {k: round(v, 4) for k, v in PR.items()})

for i in range(1, 3):  
    for p in links:
        # Calculate incoming votes using the MOST RECENT values in the PR dictionary
        incoming = sum(PR[q] / len(links[q]) for q in links if p in links[q])
        
        # 2. Update PR directly! The next letter will instantly use this new value.
        PR[p] = 0.15 + 0.85 * incoming
        
    # Print the rounded results cleanly after all nodes are updated for this iteration
    print(f"Iteration {i}:", {k: round(v, 4) for k, v in PR.items()})
