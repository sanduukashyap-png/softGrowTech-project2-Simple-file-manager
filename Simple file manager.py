while True:
    print("\n--- Simple File Manager ---")
    print("1. Create File")
    print("2. Write to File")
    print("3. Read File")
    print("4. Exit")

    choice = input("Enter your choice: ")

    # Create File
    if choice == "1":
        filename = input("Enter file name: ")

        file = open(filename, "w")
        file.close()

        print("File created successfully!")

    # Write to File
    elif choice == "2":
        filename = input("Enter file name: ")
        text = input("Enter text: ")

        file = open(filename, "a")
        file.write(text + "\n")
        file.close()

        print("Data written successfully!")

    # Read File
    elif choice == "3":
        filename = input("Enter file name: ")

        try:
            file = open(filename, "r")
            content = file.read()
            print("\nFile Content:")
            print(content)
            file.close()

        except FileNotFoundError:
            print("File not found!")

    # Exit
    elif choice == "4":
        print("Program exited.")
        break

    else:
        print("Invalid choice!")