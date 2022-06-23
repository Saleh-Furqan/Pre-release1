index = []
names = []
ages = []
genders = []
typeMemberships = []
annualFees = []
teamMembers = []
feesPaid = []


# defining a function to be used for validating yes/no type inputs
def validateYesNo(statement):
    x = input(statement)
    while x != "yes" and x != "no":
        print('invalid input. Try again')
        x = input(statement)
    return x


print(
    "=========================================================\n----------- Annual Audit of Membership Details ----------\n========================================================="
)

print(
    "Please Fill In All The User Details As Asked By The Program. Make Sure All Information Is Accurate."
)

numberOfUsers = int(input("Enter number of users:  "))

for i in range(numberOfUsers):

    name = input('Enter Name: ')
    while len(name) < 5 or len(name) > 20:
        print('Please Make Sure Name is Between 5-20 Characters!  ')
        name = input('Enter Name: ')

    age = input('Enter Age: ')
    while age.isdigit() == False:
        print('invalid age. Try again')
        age = input('Enter Age: ')

    age = int(age)
    if age < 18 and age >= 2:
        typeMembership = "junior"
        annualFee = 10
    elif age < 50 and age >= 18:
        typeMembership = "adult"
        annualFee = 20
    elif age < 80 and age >= 50:
        typeMembership = "senior"
        annualFee = 15
    else:
        typeMembership = "golden"
        annualFee = 0

    gender = input('Enter Gender: ')
    while gender != "male" and gender != "female":
        print('Enter a valid gender (male/female)')
        gender = input('Enter Gender: ')

    isteamMember = validateYesNo('Is user a Team Member? (yes/no)  ')
    if isteamMember == "yes":
        teamMember = "team member"
        annualFee = annualFee * 0.9
    else:
        teamMember = "not team member"

    isfeePaid = validateYesNo('Did user pay already? (yes/no)  ')
    if isfeePaid == "yes":
        feePaid = "paid"
    else:
        feePaid = "not yet paid"

    index.append("user {}".format(i + 1))
    names.append(name)
    ages.append(age)
    genders.append(gender)
    typeMemberships.append(typeMembership)
    teamMembers.append(teamMember)
    annualFees.append(annualFee)
    feesPaid.append(feePaid)

    print("================NEW USER===============")

jMemb = 0
aMemb = 0
sMemb = 0
gMemb = 0
jMembNotPaid = 0
aMembNotPaid = 0
sMembNotPaid = 0
gMembNotPaid = 0

for i in range(numberOfUsers):
    user = [
        index[i], names[i], ages[i], genders[i], typeMemberships[i],
        teamMembers[i], annualFees[i], feesPaid[i]
    ]
    if user[4] == "junior":
        jMemb += 1
        if user[7] == "not yet paid":
            jMembNotPaid += 1
    elif user[4] == "adult":
        aMemb += 1
        if user[7] == "not yet paid":
            aMembNotPaid += 1
    elif user[4] == "senior":
        sMemb += 1
        if user[7] == "not yet paid":
            sMembNotPaid += 1
    else:
        gMemb += 1
        if user[7] == "not yet paid":
            gMembNotPaid += 1

    print(user)

print("---------------------------")
if jMemb != 0:
    jNotPaidPercent = (jMembNotPaid / jMemb) * 100
    print("Percentage of junior members that haven't paid: ", jNotPaidPercent,
          "%")
if aMemb != 0:
    aNotPaidPercent = (aMembNotPaid / aMemb) * 100
    print("Percentage of adult members that haven't paid: ", aNotPaidPercent,
          "%")
if sMemb != 0:
    sNotPaidPercent = (sMembNotPaid / sMemb) * 100
    print("Percentage of senior members that haven't paid: ", sNotPaidPercent,
          "%")
if gMemb != 0:
    gNotPaidPercent = (gMembNotPaid / gMemb) * 100
    print("Percentage of golden members that haven't paid: ", gNotPaidPercent,
          "%")
print("---------------------------")

annualFeeExpected = (jMemb * 10) + (aMemb * 20) + (sMemb * 15)
annualFeePaid = ((jMemb - jMembNotPaid) * 10) + (
    (aMemb - aMembNotPaid) * 20) + ((sMemb - sMembNotPaid) * 15)
#displaying expected and received payments
print("---------------------------")
print("annual fee expected: ", annualFeeExpected)
print("annual fee paid: ", annualFeePaid)
print("---------------------------")

membNotPaid = []
task3 = validateYesNo("Start task 3?  ")
if task3 == "yes":
    index2 = []
    names2 = []
    ages2 = []
    genders2 = []
    typeMemberships2 = []
    teamMembers2 = []
    annualFees2 = []
    feesPaid2 = []

    jMemb = []
    aMemb = []
    sMemb = []
    gMemb = []

    for i in range(numberOfUsers):

        if feesPaid[i] == "paid":
            ages[i] += 1
            if ages[i] < 18 and ages[i] >= 2:
                typeMemberships[i] = "junior"
                annualFees[i] = 10
            elif ages[i] < 50 and ages[i] >= 18:
                typeMemberships[i] = "adult"
                annualFees[i] = 20
            elif ages[i] < 80 and ages[i] >= 50:
                typeMemberships[i] = "senior"
                annualFees[i] = 15
            else:
                typeMemberships[i] = "golden"
                annualFees[i] = 0

            nowTeamMemb = validateYesNo("Is {} a team member? ".format(
                names[i]))
            print("---------------------------")
            if nowTeamMemb == "yes":
                teamMembers[i] = "team member"
                if typeMemberships[i] == "junior":
                    jMemb.append(names[i])
                elif typeMemberships[i] == "adult":
                    aMemb.append(names[i])
                elif typeMemberships[i] == "senior":
                    sMemb.append(names[i])
                else:
                    gMemb.append(names[i])

            else:
                teamMembers[i] = "not team member"

            feesPaid[i] == "not yet paid"
            index2.append("new user {}".format(i + 1))
            names2.append(names[i])
            ages2.append(ages[i])
            genders2.append(genders[i])
            typeMemberships2.append(typeMemberships[i])
            teamMembers2.append(teamMembers[i])
            annualFees2.append(annualFees[i])
            feesPaid2.append(feesPaid[i])
        else:
            membNotPaid.append(names[i])

    print("---------------------------")
    print("Members still not paid: ", membNotPaid)
    print("---------------------------")
    print("---------------------------")
    print("Juniors: ", jMemb)
    print("Adults: ", aMemb)
    print("Seniors: ", sMemb)
    print("Golden: ", gMemb)

    for i in range(len(names2)):
        feesPaid2[i] = "not yet paid"
        user = [
            index2[i], names2[i], ages2[i], genders2[i], typeMemberships2[i],
            teamMembers2[i], annualFees2[i], feesPaid2[i]
        ]
        print(user)
