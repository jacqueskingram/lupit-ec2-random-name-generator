# EC2 Random Name Generator

A simple Python script that generates unique EC2-style instance names based on user input.  
Built as part of the LevelUP in Tech – Python Fundamentals coursework.

## Features
- Generates one or more unique EC2 instance names
- Includes department name in each generated name
- Appends random letters and numbers to ensure uniqueness
- Restricts usage to approved departments:
  - Marketing
  - Accounting
  - FinOps
- Uses a Python function to encapsulate logic

## Name Format
<Department>-ec2-<random_string>

Example:
FinOps-ec2-a9x3kq  
Marketing-ec2-z7m4p2

## Requirements
- Python 3.x
- Linux, macOS, or Windows

## How to Run
1. Clone the repository:
git clone https://github.com/<your-username>/ec2-random-name-generator.git  
cd ec2-random-name-generator

2. Run the script:
python3 ec2_random_name_generator.py

3. Follow the prompts:
- Enter department name
- Enter the number of EC2 names to generate

## Example Usage
Enter your department (Marketing, Accounting, FinOps): FinOps  
How many EC2 instance names do you want? 3  

Generated EC2 Names:  
FinOps-ec2-4j9xq2  
FinOps-ec2-m7p2a8  
FinOps-ec2-z3k91r  

## Notes
This project focuses on Python fundamentals such as:
- Functions
- Conditionals
- Loops
- User input
- Random value generation

AWS services are not required to run this script.

## License
This project is for educational purposes.

