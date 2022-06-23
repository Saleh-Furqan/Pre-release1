# userDatabase = []
# jTeamMemb = 0
# aTeamMemb = 0
# sTeamMemb = 0
# gTeamMemb = 0

# # defining a function to be used for validating yes/no type inputs
# def validateYesNo(statement):
#     x = input(statement)
#     while x != "yes" and x != "no":
#         print('invalid input. Try again')
#         x = input(statement)
#     return x

# print("=========================================================")
# print(" ---------- Annual Audit of Membership Details ----------")
# print("=========================================================")
# print(
#     "Please Fill In All The User Details As Asked By The Program. Make Sure All Information Is Accurate."
# )

# # starts inputing user details into a list
# print("---------------------------------------------------------")
# newUser = validateYesNo("Add new user? (yes/no)  ")
# while newUser == "yes":

#     # ------- name input/validation (more than 5 chars and less than 20) --------- #
#     name = input('Enter Name: ')
#     while len(name) < 5 or len(name) > 20:
#         print('Please Make Sure Name is Between 5-20 Characters!  ')
#         name = input('Enter Name: ')

#     # ---------- age type input/validation ----------- #
#     age = input('Enter Age: ')
#     while age.isdigit() == False:
#         print('invalid age. Try again')
#         age = input('Enter Age: ')

#     # ---------- Converting age from string to integer ---------- #
#     age = int(age)
#     while age > 150:
#         print("please don't joke.")
#         age = input('Enter Age: ')

#     # ---------- membership and annualfee accoding to age ---------- #
#     if age < 18 and age >= 2:
#         typeMembership = "junior"
#         annualFee = 10
#     elif age < 50 and age >= 18:
#         typeMembership = "adult"
#         annualFee = 20
#     elif age < 80 and age >= 50:
#         typeMembership = "senior"
#         annualFee = 15
#     elif age >= 80:
#         typeMembership = "golden"
#         annualFee = 0

#     # ---------- gender input/validation ---------- #
#     gender = input('Enter Gender: ')
#     while gender != "male" and gender != "female":
#         print('Enter a valid gender (male/female)')
#         gender = input('Enter Gender: ')

#     # ---------- team-member input/validation (discount for annualFee) ---------- #
#     isteamMember = validateYesNo('Is user a Team Member? (yes/no)  ')
#     if isteamMember == "yes":
#         teamMember = "team member"
#         annualFee = annualFee * 0.9
#     else:
#         teamMember = "not team member"

#     # ---------- Checking if fee is paid ---------- #
#     isfeePaid = validateYesNo('Did user pay already? (yes/no)  ')
#     if isfeePaid == "yes":
#         feePaid = "paid"
#     else:
#         feePaid = "not yet paid"

#     # ---------- making a list of all the user details ---------- #
#     user = [name, age, gender, typeMembership, teamMember, annualFee, feePaid]

#     # ---------- Appending user into database ---------- #
#     userDatabase.append(user)

#     # ---------- assigning each user a unique id based on index ---------- #
#     annMemberNumber = userDatabase.index(user) + 1
#     print(annMemberNumber, ": ", name)

#     # ----- asking if all users are entered in database after 20 (written as 3 to ease testing), to quit ----- #
#     if annMemberNumber >= 3:
#         newUser = validateYesNo(
#             "20 user details have been entered entered. Continue? (yes/no)  ")
#     else:
#         newUser = validateYesNo('Add new user? (yes/no)  ')

# print("===========================")
# print("Here is a database with all the users and their details:  ")
# print("===========================")
# for i in range(len(userDatabase)):
#     print("[  Name:", userDatabase[i][0], ", Age:", userDatabase[i][1],
#           ", Gender:", userDatabase[i][2], ", Type Of Membership:",
#           userDatabase[i][3], ", Team Member?", userDatabase[i][4],
#           ", Annual Fee", userDatabase[i][5], "Paid?", userDatabase[i][6],
#           "  ]\n")
# print("---------------------------")

# # ======================================== TASK 2 ======================================== #

# print("---------------------------")
# continueTask2 = validateYesNo("Continue to task 2? (yes/no)  ")
# if continueTask2 == "yes":
#     print("Starting task 2...")
#     juniorMember = 0
#     juniorNotPaying = 0
#     adultMember = 0
#     adultNotPaying = 0
#     seniorMember = 0
#     seniorNotPaying = 0
#     goldenMember = 0
#     goldenNotPaying = 0

#     for i in userDatabase:
#         #counting all members by membership type
#         #counting all members who haven't paid annualfee
#         if i[3] == "junior":
#             juniorMember = juniorMember + 1
#             if i[6] == "not yet paid":
#                 juniorNotPaying = juniorNotPaying + 1
#         elif i[3] == "adult":
#             adultMember = adultMember + 1
#             if i[6] == "not yet paid":
#                 adultNotPaying = adultNotPaying + 1
#         elif i[3] == "senior":
#             seniorMember = seniorMember + 1
#             if i[6] == "not yet paid":
#                 seniorNotPaying = seniorNotPaying + 1
#         elif i[3] == "golden":
#             goldenMember = goldenMember + 1
#             if i[6] == "not yet paid":
#                 goldenNotPaying = goldenNotPaying + 1

#     #displaying % of each membership type if some haven't paid.
#     print("---------------------------")
#     if juniorMember != 0:
#         juniorNotPaidPercent = (juniorNotPaying / juniorMember) * 100
#         print("Percentage of junior members that haven't paid: ",
#               juniorNotPaidPercent, "%")
#     if adultMember != 0:
#         adultNotPaidPercent = (adultNotPaying / adultMember) * 100
#         print("Percentage of adult members that haven't paid: ",
#               adultNotPaidPercent, "%")
#     if seniorMember != 0:
#         seniorNotPaidPercent = (seniorNotPaying / seniorMember) * 100
#         print("Percentage of senior members that haven't paid: ",
#               seniorNotPaidPercent, "%")
#     if goldenMember != 0:
#         goldenNotPaidPercent = (goldenNotPaying / goldenMember) * 100
#         print("Percentage of golden members that haven't paid: ",
#               goldenNotPaidPercent, "%")
#     print("---------------------------")

#     # ---------- Calculating expected annualFees and the amount that is paid ---------- #
#     annualFeeExpected = (juniorMember * 10) + (adultMember *
#                                                20) + (seniorMember * 15)
#     annualFeePaid = ((juniorMember - juniorNotPaying) * 10) + (
#         (adultMember - adultNotPaying) * 20) + (
#             (seniorMember - seniorNotPaying) * 15)

#     #displaying expected and received payments
#     print("---------------------------")
#     print("annual fee expected: ", annualFeeExpected)
#     print("annual fee paid: ", annualFeePaid)
#     print("---------------------------")

# # ======================================== TASK 3 ======================================== #

# junior = []
# adult = []
# senior = []
# golden = []

# continueTask = validateYesNo("start task 3?  ")
# if continueTask == "yes":
#     print("---------------------------")
#     print("Starting task 3...")

#     # ---------- Checking members that haven't paid, outputting their list, and removing them from the database ---------- #
#     notPaidList = []
#     newUserDatabase = []
#     for i in userDatabase:
#         if i[6] == "not yet paid":
#             notPaidList.append(i[0])
#             # userDatabase.remove(userDatabase[i])
#         else:
#             newUserDatabase.append(i)
#     print("People that didn't pay: ", notPaidList)
#     print("updated user database: ")

#     for i in range(len(newUserDatabase)):
#         print("[  Name:", newUserDatabase[i][0], ", Age:",
#               newUserDatabase[i][1], ", Gender:", newUserDatabase[i][2],
#               ", Type Of Membership:", newUserDatabase[i][3], ", Team Member?",
#               newUserDatabase[i][4], ", Annual Fee", newUserDatabase[i][5],
#               "Paid?", newUserDatabase[i][6], "  ]\n")
#     print("---------------------------")

#     # ---------- Incrementing all user ages by 1 ---------- #
#     for i in newUserDatabase:
#         i[1] = int(i[1]) + 1

#         # ---------- Assigning membership types and annual fees based on age ---------- #
#         if int(i[1]) < 18 and int(i[1]) >= 2:
#             i[3] = "junior"
#             i[5] = 10
#         elif int(i[1]) < 50 and int(i[1]) >= 18:
#             i[3] = 'adult'
#             i[5] = 20
#         elif int(i[1]) < 80 and int(i[1]) >= 50:
#             i[3] = 'senior'
#             i[5] = 15
#         elif int(i[1]) >= 80:
#             i[3] = 'golden'
#             i[5] = 0

#         isteamMember2 = validateYesNo('Is ' + i[0] +
#                                       ' A Team Member? (yes/no)  ')
#         if isteamMember2 == "yes":
#             i[4] = "team member"
#             i[5] = int(i[5]) * 0.9
#         else:
#             i[4] = "not team member"

#         # ---------- setting fees as not paid for all members ---------- #
#         i[6] = "no"

#         # ---------- Making lists based on membership types ---------- #
#         if i[3] == "junior":
#             junior.append(i)
#         elif i[3] == "adult":
#             adult.append(i)
#         elif i[3] == "senior":
#             senior.append(i)
#         elif i[3] == "golden":
#             golden.append(i)

#     print("---------------------------")
#     print("juniors: ", junior)
#     print("adults: ", adult)
#     print("seniors: ", senior)
#     print("golden: ", golden)

# # starts inputing user details into a list
# print("---------------------------------------------------------")
# newUser = validateYesNo("Add new user? (yes/no)  ")
# while newUser == "yes":

#     # ------- name input/validation (more than 5 chars and less than 20) --------- #
#     name = input('Enter Name: ')
#     while len(name) < 5 or len(name) > 20:
#         print('Please Make Sure Name is Between 5-20 Characters!  ')
#         name = input('Enter Name: ')

#     # ---------- age type input/validation ----------- #
#     age = input('Enter Age: ')
#     while age.isdigit() == False:
#         print('invalid age. Try again')
#         age = input('Enter Age: ')

#     # ---------- Converting age from string to integer ---------- #
#     age = int(age)
#     while age > 150:
#         print("please don't joke.")
#         age = input('Enter Age: ')

#     # ---------- membership and annualfee accoding to age ---------- #
#     if age < 18 and age >= 2:
#         typeMembership = "junior"
#         annualFee = 10
#     elif age < 50 and age >= 18:
#         typeMembership = "adult"
#         annualFee = 20
#     elif age < 80 and age >= 50:
#         typeMembership = "senior"
#         annualFee = 15
#     elif age >= 80:
#         typeMembership = "golden"
#         annualFee = 0

#     # ---------- gender input/validation ---------- #
#     gender = input('Enter Gender: ')
#     while gender != "male" and gender != "female":
#         print('Enter a valid gender (male/female)')
#         gender = input('Enter Gender: ')

#     # ---------- team-member input/validation (discount for annualFee) ---------- #
#     isteamMember = validateYesNo('Is user a Team Member? (yes/no)  ')
#     if isteamMember == "yes":
#         teamMember = "team member"
#         annualFee = annualFee * 0.9
#     else:
#         teamMember = "not team member"

#     # ---------- Checking if fee is paid ---------- #
#     isfeePaid = validateYesNo('Did user pay already? (yes/no)  ')
#     if isfeePaid == "yes":
#         feePaid = "paid"
#     else:
#         feePaid = "not yet paid"

#     # ---------- making a list of all the user details ---------- #
#     user = [name, age, gender, typeMembership, teamMember, annualFee, feePaid]
#     # ---------- Appending user into database ---------- #
#     userDatabase.append(user)

#     # ---------- assigning each user a unique id based on index ---------- #
#     annMemberNumber = userDatabase.index(user) + 1
#     print(annMemberNumber, ": ", name)

#     # ----- asking if all users are entered in database after 20 (written as 3 to ease testing), to quit ----- #
#     if annMemberNumber >= 3:
#         newUser = validateYesNo(
#             "20 user details have been entered entered. Continue? (yes/no)  ")
#     else:
#         newUser = validateYesNo('Add new user? (yes/no)  ')

# print("===========================")
# print("Here is a database with all the users and their details:  ")
# print("===========================")
# for i in range(len(userDatabase)):
#     print("[  Name:", userDatabase[i][0], ", Age:", userDatabase[i][1],
#           ", Gender:", userDatabase[i][2], ", Type Of Membership:",
#           userDatabase[i][3], ", Team Member?", userDatabase[i][4],
#           ", Annual Fee", userDatabase[i][5], "Paid?", userDatabase[i][6],
#           "  ]\n")
# print("---------------------------")