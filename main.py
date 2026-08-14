import cv2
name = input('Please enter the location of the image including name of the image with the extension or just the name with extension if the image is in the same directory: ')
image = cv2.imread(name)

restart_loop = True

while restart_loop:
    print('\nPlease choose the method for resizing the image by entering the corresponding number.\n1. Exact dimensions\n2. Downscale to a percentage of original size\n3. Scale down using INTER_AREA (Best quality for shrinking!)')
    
    # Choice validation
    choice = input('Enter your choice: ').strip()
    
    if not choice.isdigit():
        print('Please enter a valid number!')
        continue
    elif len(choice) > 1:
        print('Please enter only one integer!')
        continue
    
    choice = int(choice)
    restart_loop = False  # Exit main loop if choice is valid

    # Option 1 execution
    if choice == 1:
        restart_loop_2 = True
        while restart_loop_2:
            try:
                print('\nEnter 0 to go back')
                width = int(input('Enter Width: '))
                if width == 0:
                    restart_loop = True  # Send back to main menu
                    restart_loop_2 = False
                    break
                height = int(input('Enter Height: '))
                if height == 0:
                    restart_loop = True  # Send back to main menu
                    restart_loop_2 = False
                    break
                else:
                    res_image = cv2.resize(image, (width, height))
                    restart_loop_2 = False
                    break

            except ValueError:
                print('Please only enter numbers. Example: 400')
                width = None
                height = None
    elif choice == 2:
        restart_loop_3 = True
        while restart_loop_3:
            try:
                print('Enter 0 to go back')
                percentage = int(input('Enter percentage: '))
                if percentage==0:
                    restart_loop = True
                    restart_loop_3 = False
                else:
                    number = percentage/100
                    res_image = cv2.resize(image, (0, 0), fx=number, fy=number)
                    restart_loop_3 = False
                    break
            except ValueError:
                print('Please only enter numbers. Example: 50')
                restart_loop_3 = True
    elif choice == 3:
        restart_loop_4 = True
        while restart_loop_4:
                    try:
                        print('\nEnter 0 to go back')
                        width = int(input('Enter Width: '))
                        if width == 0:
                            restart_loop = True  # Send back to main menu
                            restart_loop_2 = False
                            break
                        height = int(input('Enter Height: '))                
                        if height == 0:
                            restart_loop = True  # Send back to main menu
                            restart_loop_4 = False
                            break
                        else:
                            res_image = cv2.resize(image, (400, 300), interpolation=cv2.INTER_AREA)
                            restart_loop_4 = False
                            break
        
                    except ValueError:
                        print('Please only enter numbers. Example: 400')
                        width = None
                        height = None
        




cv2.imshow('Original Image', image)
cv2.imshow('Resized Image', res_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1)

cv2.imwrite("resized_image.jpg", res_image)
print('Image successfully saved as resized_image.jpg')
