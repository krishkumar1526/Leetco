n= str(input("Do you want to login? "))
while n=='Yes':
    a= input("Enter voter's deatils:")
    b= int(input("Enter unique access pin:"))
    input("Click 'Login':")
    vd= input("Enter voter's detail again to verify:")
    dv= int(input("Again write your unique access pin:"))
    if a==vd and b==dv:
        print("User exists and the pin is valid.")
        print("Granting access to Voting Interface.")
        c= input("Enter your first candidate for first Post using checkbox:")
        input("Enter 'Next':")
        c1= input("Enter your candidate for other Posts using checkbox:")
        ad= input("Click 'Next' to proceed or 'Back' to edit selected candidates:")
        while ad=='Next':
          v= str(input("Is voter ready to vote selected candidates:"))
          if v=='Yes':
              input("click'VOTE':")
              break
          elif v=='No':
              ad= input("Click 'Next' to proceed or 'Back' to edit selected candidates:")
        n= str(input("Do you want to login? "))
    else:
        print("User don't exist.You are not allowed to give vote.")
        n= str(input("Do you want to login? "))
while n=='No':
    input("Enter 'Menu':")
    print("Exit")
