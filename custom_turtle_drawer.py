import turtle
import sys


#set up screen
ws = turtle.Screen()
ws.bgcolor("#a0e5f2")

#set up turtle
cherepaxa = turtle.Turtle()
cherepaxa.speed(0)
cherepaxa.pensize(5)
cherepaxa.shape('turtle')

#set length
length = 100

#initialize default color list
default_colors = ['red', 'blue', 'green', 'brown']

#exit programm if default_colors list is empty
def close_if_default_colors_empty():
     if not default_colors:
        print('No colors left to draw!')
        sys.exit()

#draw shape
def draw_shape(length):

    sides = len(default_colors) #number of sides equals the number of colors in default_colors list
    angles = 360 / sides
    color_index = 0
    
    for i in range(sides): #repeate drawing by the number of colors in default_colors list
        
        cherepaxa.color(default_colors[color_index]) #set the color to the current color from the default_colors list
        cherepaxa.left(angles)
        cherepaxa.forward(length)

        color_index += 1

        if color_index >= len(default_colors): #set the index to 0 if it exceeds the number of colors in the default_colors list 
            color_index = 0

#function to add colors to the default_colors list
def add_new_color():
    new_colors = input('Please, enter the colors you want to add, separeted by space.').split()    #split to make it a list becasue it needs to be added to the default_colors list
    
    default_colors.extend(new_colors) # add new color to the list using extend. Exten adds colors indivdually from the new list to default_colors list. 
    #Append would add a list to the default_colors list for exemple ['red', 'blue', ['yellow']]
    
        

def remove_color():
    
    removed_color = input('Which colors do you want to remove? Enter the colors separeted by space.').split()  #split to make it a list
    for color in removed_color: #iterate through the removed_color list
        if color in default_colors: #check each color if it is in the default_colors list
            default_colors.remove(color) #if yes, remove it
            close_if_default_colors_empty()             
        else:
            print(f'Colors not found.') #print if color entered is not found in default_colors list
            #try to remove color again
            another_color = input('Do you want to try to remove colors again? Yes or No?').lower()
            if another_color == 'yes':
                remove_another_color= input('Enter colors you want to remove.').split()
                for color in remove_another_color:
                    if color in default_colors:
                        default_colors.remove(color)
                         close_if_default_colors_empty()
                    else:
                        print(f'Colors not found.')
            else: draw_shape(length)
        
    

while True:
    choosing_colors = input('Default colors are red, blue, green and brown. Do you want to add/remove color or draw?').replace(' ', '').lower()
    
    #add colors
    if choosing_colors == 'add':
        add_new_color() 
        print(f'Default colors are: {', '.join(default_colors)}') #join creates a string from the list

        #further modify by removing colors
        modify = input('Do you want to remove colors? Yes or No?').replace(' ', '').lower()     
        if modify == 'yes':
            remove_color()
            draw_shape(length)
        else: draw_shape(length)
        break
    

    #remove colors
    elif choosing_colors == 'remove':
        remove_color()
        print(f'Default colors are: {', '.join(default_colors)}')

        #add colors
        modify = input('Do you want to add colors? Yes or No?').lower() 
        if modify == 'yes':
            add_new_color()
            draw_shape(length)
        else: draw_shape(length)
        break

    elif choosing_colors == 'draw':
        draw_shape(length)
        break

    else:
        print("Invalid input, please choose 'add', 'remove', or 'draw'.")

   
turtle.done()


 
