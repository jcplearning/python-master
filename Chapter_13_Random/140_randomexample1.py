import random

def random_example():
    # Generate a random integer between 1 and 100
    random_integer = random.randint(1, 100)
    print(f"Random Integer: {random_integer}")

    # Generate a random float between 0 and 1
    random_float = random.random()
    print(f"Random Float: {random_float}")

    # Choose a random element from a list
    sample_list = ['apple', 'banana', 'cherry', 'date', 'elderberry']
    random_choice = random.choice(sample_list)
    print(f"Random Choice from List: {random_choice}")

    # Shuffle a list randomly
    random.shuffle(sample_list)
    print(f"Shuffled List: {sample_list}")

    random_choices = random.choices(sample_list, k=3)
    print(f"Random Choices from List: {random_choices}")

    random_sample = random.sample(sample_list, k=3)
    print(f"Random Sample from List: {random_sample}")

    random_seed = 42
    random.seed(random_seed)
    print(f"Random Integer with Seed {random_seed}: {random.randint(1, 100)}")
    print(f"Random Float with Seed {random_seed}: {random.random()}")
    print(f"Random Choice from List with Seed {random_seed}: {random.choice(sample_list)}")
    print(f"Random Sample from List with Seed {random_seed}: {random.sample(sample_list, k=3)}")

if __name__ == "__main__":
    random_example()

