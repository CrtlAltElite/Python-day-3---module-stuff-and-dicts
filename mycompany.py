## Apply To my Company CLI application
def get_name():
    name = input("What is your first and last name? ")
    return name

def get_last_job():
    job=input("What is your prev job? ")
    return job
    
def get_location():
    location=input("What is your prefered Location? NY/SF/Raleigh")
    return location

def main():
    while True:
        response=input("Do you want to apply to my Company")
        if response[0].lower()!='y':
            print("Why did you come here?")
            break
        name =get_name()
        job = get_last_job()
        local = get_location()
        print(f"name: {name}\njob: {job}\nlocation: {local}")
        response = input("Is the Above Infomation correct?")
        if response[0].lower()=='y':
            print("Thanks for applying")
            break
        wrong=input("What field was wrong? name/job/local? ")
        if wrong=="name":
            name = get_name()
        elif wrong=="job":
            name = get_last_job()
        elif wrong == "local":
            local = get_location()
        print("Thanks for applying")
        break

        
        
if __name__ == '__main__':
    main()