# Incomplete app!

li=[
  {'title':'Titanic', 'director':'Teddy', 'year':'2000'}]
def add():
    title = input("Enter the movie title: ")
    director = input("Enter the movie director: ")
    year = input("Enter the movie release year: ")
    li.append({
    'title': title,
    'director': director,
    'year': year
    })
    print("added to the list:",li)
    return li


  
# You may want to create a function for this code
 

# Create other functions for:
#   - listing movies
def movies_h(d):
  if d=='l':
    print(li)
    get_input()
  elif d=='f':
     
     e = input("Enter the movie name to find:")
     di={'user':e}
     z=[]
     z.append(di)
     print(z)
     for i in range(0, len(li)):
       if z[0]['user']==li[i]['title']:
         print("already in the list")
       else:
         print("Not in the List")
         mohan=input("do you want to add the movie to list? Y/N: ")
         if mohan=='Y':
           add()
         get_input()


def get_input():
  MENU_PROMPT = input("\n Enter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie by title, or 'q' to quit: ")
  user_options(MENU_PROMPT)
  

def user_options(user):
  if user == 'a':
    sri=add()
    print(sri)
    get_input()
  elif user=='l' or user=='f':
    movies_h(user)
  elif user =='q':
    print("User typed exit")
  else:
    print("Please enter the correct input!!")
    get_input()

get_input()


# Remember to run the user menu function at the end!
