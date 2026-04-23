import  re
import csv
import pandas as pd
import matplotlib.pyplot as plt

# df = pd.read_csv('alumni_anonymized.csv', index_col='Id No')
# print(df)





def missing(year:str) -> bool: #check if year is missing; exclude from data. Probabl Faculty
    if len(year) == 0: return True
    return False


def check_faculty(year:str) -> bool: #check if faculty in year; exclude from data
    if "Faculty" in year: return True
    return False


def two_digits(year:str) -> bool: #check if 2 digits; if true, send to make_four
    if len(year) == 2: return True
    return False

def one_digit(year:str) -> bool:
    if len(year) == 1: return True
    return False

def fix_one(year:str) -> str:
    return_str = "190" + year
    return return_str

def make_four(year:str) -> str: #take 2 digit number and return 4 digit; most likely 19 + 2 digit
    return_str = "19" + year
    return return_str


def remove_clutter(year:str) -> str:
    return_year = re.findall("[0-9]+", year)
    if len(return_year) > 0: return return_year[0]
    else: return year


def has_DOB(birth:str) -> bool: #Check if has DOB; If False, exclude from data
    if (len(re.findall('^DOB', birth)) > 0 or len(re.findall('^Born', birth)) > 0 or len(re.findall('^[0-9]', birth)) > 0) and (len(re.findall('DOB: UNK', birth)) == 0 and len(re.findall('Born: UNK', birth)) == 0 and len(re.findall('[?]+', birth)) == 0):
        return True
    return False

def extract_year(birth:str) -> str | None: #take DOB and extract year
    if len(re.findall("\\d+\/", birth)) > 0:
        return_birth = re.findall("\\d[/-]+[A-Za-z0-9]+[/-]+(\\d{2,4})", birth)
    else:
        return_birth = re.findall("[0-9]{4}", birth)
    
    if len(return_birth) > 0:
        return return_birth[0]
    return None


with open('alumni_birthdays.csv') as records:
    reader = csv.reader(records)
    entries = [] #this will store the rows in dictionary form
    next(reader)  #skip header
    for row in reader:
        if (check_faculty(row[1]) is False) and (missing(row[1]) is False) and ((has_DOB(row[4]) is True) or (row[5] is not None)):
            new_row = dict()
            year = remove_clutter(row[1])
            if missing(row[5]) is False:
                birth = extract_year(row[5])
            else: 
                birth = extract_year(row[4])
                
            if birth is not None:
                if two_digits(year) is True:
                    year = make_four(year)
                if two_digits(birth) is True:
                    birth = make_four(birth)
                elif one_digit(year) is True:
                    year = fix_one(year)
                if year.isdigit():
                    year_int = int(year)
                    birth_int = int(birth)
                    new_row['Id'] = row[3]
                    new_row['Exit_Year'] = year_int
                    new_row['Last_Name'] = row[0]
                    new_row['Birth_Year'] = birth_int
                    entries.append(new_row)

    
    exit = pd.DataFrame(entries)
    df = exit.set_index('Id')

    df = df[((df['Exit_Year'] >= 1880)) & (df['Exit_Year'] <= 1984) & ((df['Birth_Year'] >= 1857) & (df['Birth_Year'] <= 1980))]

    df['Age_at_Exit'] = df['Exit_Year']-df['Birth_Year']

    df = df[(df['Age_at_Exit'] >= 7) & (df['Age_at_Exit'] <= 23)]

    print(df)
    


with open('alumni_clean.csv', 'w', newline='') as new_file:
    # csv_writer = csv.DictWriter(new_file,fieldnames=['Last_Name','Exit_Year'])
    # csv_writer.writeheader()
    # csv_writer.writerows(entries)
    df.to_csv('alumni_clean.csv')
    

df.plot.scatter(x='Exit_Year', y='Birth_Year')
plt.xlabel('Exit Year')
plt.ylabel('Birth Year')
plt.title('Comparison of Birth Year and Exit Year of AMA graduates')
plt.savefig('Birth_vs_Exit_Comparison.png', dpi=200)
plt.show()


plt.hist(df['Exit_Year'],bins=40, color='red')
plt.xlabel('Exit Year')
plt.ylabel('Number of Records')
plt.title('Number of Graduates by year')
plt.savefig('Number_of_Grads.png', dpi=200)
plt.show()








