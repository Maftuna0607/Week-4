score1=int(input("Enter you first score: "))
score2=int(input("Enter you second score: "))
score3=int(input("Enter you third score: "))
midterm=int(input("Enter your midterm result: "))
final=int(input("Enter your final result: "))

def calculate_average(score1, score2, score3):
    return (score1+score2+score3)/3
def drop_lowest(score1, score2, score3):
    return (score1+score2+score3 - min(score1, score2, score3)/2)
def calculate_weighted(assignments, midterm, final):
     return(assignments*0.3+midterm*0.3+final*0.4)
def determine_grade(average):
    if average>89:
        return("A")
    elif average>79:
        return("B")
    elif average>69:
        return("C")
    elif average>59:
        return("D")
    else:
        return("F")
def needs_improvement(current_avg, target_grade):
    if target_grade-current_avg>=0:
        return ("Already meets requirement")
    else:
        return ("Needs improvement for")
    
def 
    reg_asn_avr=calculate_average(score1,score2,score3)
    lowest_dropped=drop_lowest(score1, score2, score3)
    assignments=score1+score2+score3
    weighted_avr=calculate_weighted(assignments, midterm, final)
    letter_grade=determine_grade(calculate_average(score1,score2,score3))
    

    print(f"STUDENT GRADE CALCULATOR")
    print(f"========================================")
    print(f"Assignment Scores: {score1}, {score2}, {score3}")
    print(f"Midterm Score: {midterm}")
    print(f"Final Score: {final}")
    print(f"----------------------------------------")
    print(f"Regular Asssignment Average: {reg_asn_avr}")
    print(f"Average with Lowest Dropped {lowest_dropped}")
    print(f"Using Better Average: {lowest_dropped}\n")
    print(f"Weighted Course Average: {weighted_avr:.2f}")
    print(f"Letter Grade: {letter_grade}")
    