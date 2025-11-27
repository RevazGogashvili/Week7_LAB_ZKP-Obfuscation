import random


def simulate_malicious_prover(trials=20):
    success_count = 0

    print(f"--- Simulating Malicious Prover (No Password) over {trials} trials ---")

    for i in range(1, trials + 1):
        path_entered = random.choice(['A', 'B'])

        challenge = random.choice(['A', 'B'])

        if path_entered == challenge:
            success = True
            result = "Success (Lucky Guess)"
        else:import random

def simulate_malicious_prover(trials=20):
    success_count = 0

    print(f"--- Simulating Malicious Prover (No Password) over {trials} trials ---")

    for i in range(1, trials + 1):
        path_entered = random.choice(['A', 'B'])
        challenge = random.choice(['A', 'B'])

        if path_entered == challenge:
            success = True
            result = "Success (Lucky Guess)"
        else:
            success = False
            result = "Fail (Caught!)"

        if success:
            success_count += 1

        print(f"Round {i}: Entered {path_entered}, Challenge {challenge} -> {result}")

    probability = (success_count / trials) * 100

    print(f"\nFinal Results:")
    print(f"Total Successful responses: {success_count}/{trials}")
    print(f"Success Probability: {probability}%")

simulate_malicious_prover(20)