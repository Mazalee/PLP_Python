def process_file(filename):
    try: 
        with open(filename, "r") as file:
            content = file.read()

        # Count the number of words
        words = content.split()
        word_count = len(words)

        # Convert to uppercase
        uppercase_content = content.upper()

        # Write the processed text and the word count to a new file called output.txt
        with open("output.txt", "w") as file:
            file.write("Processed Text:\n")
            file.write(uppercase_content + "\n")
            file.write(f"\nWord Count: {word_count}")
        
        print("✅ output.txt created successfully with processed text and word count.")
    
    except FileNotFoundError:
        print(f"❌ Error: The file '{filename}' does not exist.")
    except PermissionError:
        print(f"⚠️ Error: You don't have permission to read '{filename}'.")
    except Exception as e:
        print(f"💥 An unexpected error occurred: {e}")

# --- Program ---
filename = input("Enter the filename to process: ")
process_file(filename)
