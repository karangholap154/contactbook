contacts = {}

while True:
    print("\nContact Book App")
    print("1. Create Contact")
    print("2. View Contact")
    print("3. Update Contact")
    print("4. Delet Contact")
    print("5. Search Contact")
    print("6. Count Contact")
    print("7. Exit")

    choice = input('Enter your choise = ')

    if choice == '1':
        name = input('Enter your name = ')
        if name in contacts:
            print(f'Contact name {name} already exists!')
        else:
            age = input('Enter age = ')
            email = input('Enter email = ')
            mobile = input('Enter mobile number = ')
            contacts[name] = {'age':int(age), 'email':email, 'mobile':mobile}
            print(f'Contact name {name} has been created successfully!')

    elif choice == '2':
        name = input('Enter your name to view = ')
        if name in contacts:
            contact = contacts[name]
            print(f'Name: {name}, Age:{age}, Mobile Number: {mobile}, Email:{email}')
        else:
            print('Contact Not Found!')
    
    elif choice == '3':
        name = input('Enter your name to update contact = ')
        if name in contacts:
            age = input('Enter updated age = ')
            email = input('Enter updated email = ')
            mobile = input('Enter updated mobile number = ')
            contacts[name] = {'age':int(age), 'email':email, 'mobile':mobile}
        else:
            print('Contact Not Found!')
    
    elif choice == '4':
        name = input('Enter your name to delet contact = ')
        if name in contacts:
            del contacts[name]
            print(f'Contact name {name} has been deleted successfully!')
        else:
            print('Contact Not Found!')
    
    elif choice == '5':
        search_name = input('Enter your name to search = ')
        found = False
        for name, contact in contacts.items():
            if search_name.lower() in name.lower():
                print(f'Found - Name: {name},  Age:{age}, Mobile Number: {mobile}, Email:{email}')
                found = True
        if not found:
            print('Contact Not Found With That Name!')
    
    elif choice == '6':
        print(f'Total contacts in your book : {len(contacts)}')
    
    elif choice == '7':
        print('Good bye...Closing the program!')
        break

    else:
        print('Invalid Input!')