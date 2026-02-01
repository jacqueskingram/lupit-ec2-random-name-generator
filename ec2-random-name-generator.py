import random
import string

ALLOWED_DEPARTMENTS = {
    "marketing": "Marketing",
    "accounting": "Accounting",
    "finops": "FinOps",
}

def generate_ec2_names():
    """
    Generates unique EC2 instance names based on department + random suffix.

    Name format:
        <Department>-ec2-<random>
    Example:
        Accounting-ec2-k7p9x2
    """

    # --- Collect & validate department ---
    dept_input = input("Enter your department (Marketing, Accounting, FinOps): ").strip().lower()

    if dept_input not in ALLOWED_DEPARTMENTS:
        print(
            "This Name Generator is only for: Marketing, Accounting, FinOps.\n"
            "You should not use this Name Generator."
        )
        return  # Stop execution cleanly

    department = ALLOWED_DEPARTMENTS[dept_input]

    # --- Collect & validate count ---
    while True:
        count_input = input("How many EC2 instance names do you want? ").strip()
        if count_input.isdigit() and int(count_input) > 0:
            count = int(count_input)
            break
        print("Please enter a valid positive whole number (e.g., 1, 2, 10).")

    # --- Generate unique names ---
    # Adjust suffix length if you want even lower collision probability
    suffix_length = 6  # mix of lowercase letters + digits
    charset = string.ascii_lowercase + string.digits

    names = set()
    while len(names) < count:
        suffix = "".join(random.choices(charset, k=suffix_length))
        name = f"{department}-ec2-{suffix}"
        names.add(name)

    # --- Output ---
    print("\nGenerated EC2 Names:")
    for n in sorted(names):
        print(n)

if __name__ == "__main__":
    generate_ec2_names()
