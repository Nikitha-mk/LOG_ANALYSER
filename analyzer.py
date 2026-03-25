#

def analyze_log(file_path):
    error_count = 0
    warning_count = 0
    info_count = 0

    try:
        with open(file_path, 'r') as file:
            for line in file:
                line = line.strip().lower()

                if "error" in line:
                    error_count += 1
                elif "warning" in line:
                    warning_count += 1
                elif "info" in line:
                    info_count += 1

        print("\n===== Log Analysis Result =====")
        print(f"Errors   : {error_count}")
        print(f"Warnings : {warning_count}")
        print(f"Info     : {info_count}")

    except FileNotFoundError:
        print("File not found. Please check the file path.")

# Run program
if __name__ == "__main__":
    file_path = input("Enter log file path: ")
    analyze_log(file_path)