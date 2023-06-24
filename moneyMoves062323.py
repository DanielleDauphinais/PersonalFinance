'''
Created: 06/23/23
last edited: 06/23/23
Author: Danielle Dauphinais

Working on financial planning can be confusing so this will help...
This is ideal for a early 20 something to get a handle of finances (saving money).
As a software engineer you can be making a lot of money early on and I've always been told to pay yourself first.
'''

class Plan:
    # Class Plan will Percent To Save for key areas.
    '''
    Each input will be a percent of income that should be saved 
    1. Retirement - never too early 
    2. Emergency savings - never know when you'll need it
    3. House - gotta start somewhere
    3. Education - for tax cuts and future kids
    4. Travel - gotta look forward to something
    5. Charity - giving back is key 2 Corinthians 9:6-8
    '''
    def __init__(self, retirement, emergency, house, education, travel, charity):
        self.retirement = retirement
        self.emergency = emergency
        self.house = house
        self.education = education
        self.travel = travel
        self.charity = charity
    
    '''
    use case: This function will calculate the amount of money you should be putting away in the accounts you
    have based on the income stated and the Plan object that has been created
    input: payment - number that should be split up to be saved
    returned: dictionary with the amount to save in each category along with the money that should be used to
    pay for life and not "paying your future self"
    '''
    def calculation(self, income):
        retirement = self.retirement*income
        emergency = self.emergency*income
        house = self.house*income
        education = self.education*income
        travel = self.travel*income
        charity = self.charity*income
        life = income-retirement-emergency-house-education-travel-charity
        return {"retirement": retirement, "emergency":emergency, "house":house, "education":education, "travel":travel, "charity":charity, "life":life}


'''
This funtion gets users income and ensures that the input is a positive number
'''
def getIncome():
    income = -1
    boolVal = True
    inputStatement = "Please input your income so we can calculate what to add to saving: \n"
    while boolVal:
        try:
            float(income)
            if float(income)<=0:
                income= input(inputStatement)
            else: 
                boolVal = False
        except:
            income= input(inputStatement)
    return float(income)


'''
This funtion gets users plan and ensures that each percent is inbetween 0<p<1 and in the end the percentages are not more than 1
'''
def getPlan():
    boolVal = True
    plan = {"retirement": -1, "emergency": -1, "house": -1, "education":-1, "travel":-1, "charity": -1}
    while boolVal:
        for percent in plan:
            inputStatement = "Please input your desired savings for "+percent+" in the following form, if you wish to save 10% of your income input 0.1\n"
            boolVal1 = True
            while boolVal1:
                try:
                    float(plan[percent])
                    if float(plan[percent])<=0 or float(plan[percent])>=1:
                        plan[percent]= input(inputStatement)
                    else: 
                        plan[percent] = float(plan[percent])
                        boolVal1 = False
                except:
                    plan[percent]= input(inputStatement)
        if sum(plan.values())>1:
            print("The total percent saved must be less than 1")
            plan = {"retirement": -1, "emergency": -1, "house": -1, "education":-1, "travel":-1, "charity": -1}
        else:
            boolVal = False
    print("You can now edit the code in line ??? to the following construtor so you do not have to make a new savings plan each time you use this script.")
    print("Plan("+str(plan["retirement"])+","+str(plan["emergency"])+","+str(plan["house"])+","+str(plan["education"])+","+str(plan["travel"])+","+str(plan["charity"])+")")
    return Plan(plan["retirement"],plan["emergency"],plan["house"],plan["education"],plan["travel"],plan["charity"])

'''
To avoid copying code this function can be called to print the amount a user should save based on the plan.
'''
def printSavingAmount(income, dict):
    print("With the income of $"+str(income)+" and the plan you have specified you should save accordingly:")
    for key in dict:
        print("For "+key+" $"+str(dict[key]))

''' 
If you have already created a plan using this script you were given a construtor to use so you don't need to input
saving goals every time that can be pasted below

'''
plan = None
#plan = Plan(0.1,0.05,0.15,0.05,0.05,0.05)
# Program enters here!
print("Welcome! Congratulations for getting paid and trying to pay yourself first!")

# if there is a plan already user will just input income and then get values to save
if plan != None:
    income = getIncome()
    dict = plan.calculation(income)
    printSavingAmount(income, dict)
    
else:
    plan = getPlan()
    print("Now let's start saving using this plan.")
    income = getIncome()
    dict = plan.calculation(income)
    printSavingAmount(income, dict)



