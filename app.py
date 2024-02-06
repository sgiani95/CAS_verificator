import csv

def check_cas_number(cas_number):
    with open('default_cas_list.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['CAS Number'] == cas_number:
                return row['Attributes']  # Return the attributes of the CAS number if found
    return None  # Return None if the CAS number is not found

def main():
    cas_number = input("Enter a CAS number: ")
    attributes = check_cas_number(cas_number)
    if attributes:
        print(f"CAS number {cas_number} is present. Attributes: {attributes}")
    else:
        print(f"CAS number {cas_number} is not present.")

if __name__ == "__main__":
    main()
