import application.db.people as ape, application.salary as asa
from datetime import date
import wikipedia

if __name__ == '__main__':
    ape.get_employee()
    asa.calculate_salary()
    current_date = date.today()
    print(current_date)
    print("*"*10)
    result = wikipedia.page("Python Programming Language")
    print(result.summary)