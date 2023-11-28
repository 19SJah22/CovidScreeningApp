introduction = "Welcome to the COVID 19 support service. Please select an option below:"
print(introduction)

print("1.Statistics\n2.Prevention\n3.Symptoms\n4.Treatment\n5.Report case\n6.Exit")

choice = int(input("Enter choice(1/2/3/4/5/6): "))
num_Choice = [1, 2, 3, 4, 5, 5, 6]
yes_no = ["y", "Y", "n", "N"]
bool1 = True
bool2 = True
for x in num_Choice:
    if choice!= x:
        bool1 = False
        continue
    else:
        bool1 = True
        break
if bool1 == False:
    print("Input is not valid")
if choice == 1:
    print("\nCurrently in SA there are 3,68M confirmed cases."
          "\nCurrently in China there are 111K confirmed cases."
          "\nCurrently in USA there are 79,2M confirmed cases.")

elif choice == 2:
    print("\nHere is how to prevent COVID-19:"
          "\n"
          "\nClean your hands often. Use soap and water, or alcohol-based hand rub."
          "\nMaintain a safe distance from anyone who is coughing or sneezing."
          "\nDon't touch your eyes, nose or mouth."
          "\nCover your nose and mouth with your bent elbow or a tissue when you cough or sneeze."
          "\nStay home if you feel unwell."
          "\nIf you have a fever, cough and difficulty breathing, seek medical attention. Call in advance."
          "\nFollow the directions of your local health authority.")
          
elif choice == 3:
    print("\nMost common symptoms:"
          "\nFever"
          "\nDry cough"
          "\nTiredness"
          "\n"
          "\nLess common symptoms:"
          "\nAches and pains"
          "\nSore throat"
          "\nDiarrhoea"
          "\nConjunctivitis"
          "\nHeadache"
          "\nLoss of taste or smell."
          "\nA rash on skin, or discoloration of fingers or toes."
          "\n"
          "\nSerious symptoms:"
          "\nDifficulty breathing or shortness of breath."
          "\nChest pain or pressure."
          "\nLoss of speech or movement.")
elif choice == 4:
    print("\nThe treatments are:"
          "\n"
          "\nIf you feel sick you should rest, drink plenty of fluid, and eat nutritious food. Stay in a separate room"
          "\nfrom other family members, and use a dedicated bathroom if possible. Clean and disinfect"
          "\nfrequently touched surfaces.")
elif choice == 5:
    Report_c = str(input("Do you have any of the symptoms? y/n: "))
    #Report_c == "y" or Report_c == "Y"
    #Report_c == "n" or Report_c == "N"
    Report_c = str(input("Is your temperature above 38.5°C? y/n: "))
    # Report_c == "y" or Report_c == "Y"
    # Report_c == "n" or Report_c == "N"
    print("In which country are you?, select an option below:")
    list = ["1.SA", "2.USA", "3.China"]
    print(list[0])
    print(list[1])
    print(list[2])
    Option = int(input("Enter option(1/2/3): "))
    if Report_c == "y" or Report_c == "Y":
        print("You have COVID-19. Please seek treatment.")
    elif Report_c == "n" or Report_c == "N":
        print("You don't have COVID-19.")
        
elif choice == 6:
    print("\nThank you, goodbye.")
    exit()

randomCountry = input("\nWould you like to see the Confirmed cases for a random country? y/n: ")
for x in yes_no:
    if randomCountry!= x:
        bool2 = False
        continue
    else:
        bool2 = True
        break
if bool2 == False:
    print("Input is not valid.")

if randomCountry == "y" or randomCountry == "Y":
    country = input("\nTo select a random country, type a number from 0 to 9: ")
    if country == "0":
        print("Austria has 314K confirmed cases.")
    if country == "1":
        print("Japan has 65K confirmed cases.")
    if country == "2":
        print("Ukraine has 114K confirmed cases.")
    if country == "3":
        print("Brazil has 136K confirmed cases.")
    if country == "4":
        print("Italy has 217K confirmed cases.")
    if country == "5":
        print("Argentina has 196K confirmed cases.")
    if country == "6":
        print("Papua New Guinea has 4 630 confirmed cases.")
    if country == "7":
        print("Greenland has 209K confirmed cases.")
    if country == "8":
        print("Russia has 114K confirmed cases.")
    if country == "9":
        print("Germany has 188K confirmed cases.")

   








