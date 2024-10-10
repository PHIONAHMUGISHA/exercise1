 # 3 witi has asked you to autmate a simple grading system 
           #as apython student, write aprogram using to display the grades 
           #the student will de recieving based on the mark scored in subjects 
           #The grades are :
           #90%-100% grade is 
           def calculate grades ():
           mark=int(input('Enter the marks scored:\t'))
           if mark >=90 and mark <=100:
            print("Grade A")
            elif mark >= 80 and mark <=89:
              print("Grad B ")
              elif mark >= 70and mark <=79:
                print("Grade C")
                elif mark >=60 and mark <=69:
                  print("Grade D")
                  elif mark >= 50 and mark <=59:
                    print("Grade E")
                    else:
                      print("fail")