def cybertron0():
     print("you are standing on cybertron 0.\n\ you see to exits, labelled 1 and 2.")
     choice = input ("choose 1 or 2: ")
     if choice == "1" :
         autobots()
     elif choice == "2":
         desepticons()
     else:
         print("that's not one of the choices!")
         cyberron0()

def cybertron1():
     print("you are an autobot.\n\ you see two bots, labelled 3 and 5.")
     choice = input ("choose 3 or 5: ")
     if choice == "3": 
        optimus1()
     elif choice == "5":
        bumblebee2()
     else:
         print("that's not one of the choices!")
         cybertron3()
 
def cybertron2():
     print("you are decepticon.\n\ you see two cons, labelled 4 and 6.")
     choice = input ("choose 4 or 6: ")
     if choice == "4" :
         megatron5()
     elif choice == "6":
         shockwave6()
     else:
         print("that's not one of the choices!")
         cybertron2()

def cybertron3():
     print ("you can go and attack the autobots or the decepticons.")
     choice = input ("choose attack autobots or attack decepticons: ")
     if choice == "attack autobots" :
         attack()
     elif choice == "attack decepticons":
         attack ()
     else:
         print("that is not one of the choices!")
         cybertron3()
         
def cybertron4():
    print ("you chose decepticons, you have lost, a rail gun has blown your base.\n\ you game ends here.")

def cybertron5():
     print (" you chose autobots, you have won.\n\ you are now a prime.")
    
        
