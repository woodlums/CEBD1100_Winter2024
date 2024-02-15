my_grades = [("Math", 4, "A"), ("English", 4, "B+"), ("Python", 4, "A+")]

gp = {"A+": 4.3, "A": 4, "A-": 3.7, "B+": 3.3, "B": 3, "B-": 2.7, "F": 0}

credits_taken = 0
gp_earned = 0

for course in my_grades:
    credits_taken += course[1]
    gp_earned += course[1] * gp[course[2]]

gpa = gp_earned / credits_taken

print(f"GPA = {gpa}")

# 4 credits x 4 gp = 16gp
# 4 credits x 3.3 gp = 13.2

# total gp = 29.2gp
# total credits = 8
# gpa = 29.2 / 8

# A+ = 4.3 grade points
# A = 4 grade points
# A- = 3.7 grade points
# B+ = 3.3 grade points
# B = 3 grade points
# B- = 2.7 grade points
# F  = 0 gp