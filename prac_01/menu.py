name = input("Name: ")
while name == "":
    print("Error: No Name")
    name = input("Name: ")
print("(H)ello")
print("(G)oodbye")
print("(Q)uit")
choice = input(">>> ").lower()
while choice != "q":
   if choice == "h":
       print(f"Hello {name}")
   elif choice == "g":
       print(f"Goodbye {name}")
   else:
       print("Invalid choice")
   print("(H)ello")
   print("(G)oodbye")
   print("(Q)uit")
   choice = input(">>> ").lower()
print("Finished.")