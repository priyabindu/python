# #
# while True:
#    print("1.square 2.cube.Anyother option will exit the code")
#    choice=(input("enter a choice:"))
#    if choice == "1" or choice == 'square':
#       num=int(input("enter a value:"))
#       print(num ** 2)
#    elif choice == "2" or choice == 'cube':
#       num=int(input("enter a value:"))
#       print(num ** 3)
#    else:
#       print("plz enter a possible choices")  
#       print("exiting")
#       break 
# #
# while True :
#     print('1.addition 2.subtraction 3.multiplication 4.divison')
#     choice = input('enter the number')

#     if choice == '1' or choice == 'addition':
#         input_num1 = float(input('enter the number'))
#         input_num2 = float(input('enter the number'))
#         print(input_num1+input_num2)

#     elif choice == '2' or choice == 'subtraction':
#         input_num1 = float(input('enter the number'))
#         input_num2 = float(input('enter the number'))
#         print(input_num1-input_num2)
#     elif choice == '2' or choice == 'multiplication':
#         input_num1 = float(input('enter the number'))
#         input_num2 = float(input('enter the number'))
#         print(input_num1*input_num2)

#     elif choice == '2' or choice == 'division':
#         input_num1 = float(input('enter the number'))
#         input_num2 = float(input('enter the number'))
#         print(input_num1/input_num2)


#     else:
#         print('no valid option picked')
#         print('existing')
#         break

# # for i in range(1,101):
# #    if i % 3 ==0 and i % 5 == 0:
# #       print(i)
    
   
   
# # def login_page():
# #     username=input("Enter your username: ")
# #     savedPassword="123456"
# #     count=1
# #     while count<4:
# #         count+=1
# #         password=input("Enter your password here: ")
# #         if password==savedPassword:
# #             print("Login Successfull")
# #             break
# #         elif password!=savedPassword:
# #             print(f"Wrong Password, You have {4-count} more attempts left")
# #             if count==4:
# #                 print("You have exhaused your login attempts. Revisit after 24hrs.")
# #         else:
# #             print("Something went wrong")
# #             break
# # login_page()


# n = int(input("enter a value:"))
# fact = 1
# for i in range(1, n + 1):
#     fact *= i
# print(fact)