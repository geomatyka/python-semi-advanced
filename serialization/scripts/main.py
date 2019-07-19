from serialization.employee import Employee

import pickle
import json


def deserialize_pickle():
    with open('employees.pkl', 'rb') as f:
        employees = pickle.load(f)
    return employees

def load_json():
    with open('employees.json', 'r') as f:
        employees = json.load(f)
    return employees


if __name__ == '__main__':
    # kowalska = Employee('Magdalena', 'Kowalska')
    # kowalski = Employee('Jan', 'Kowalski')
    #
    # employees = [kowalska, kowalski]
    # print(employees)
    #
    # with open('employees.pkl', 'wb') as f:
    #     pickle.dump(employees,f)

    # kowalska = Employee('Magdalena', 'Kowalska')
    # kowalski = Employee('Jan', 'Kowalski')
    #
    # employees = [kowalska, kowalski]
    # print(employees)
    #
    # with open('employees.json', 'w') as f:
    #     json.dump(employees,f)

    employees = {
        'kowalska':{'first_name':'Magdalena','last_name':'Kowalska'},
        'kowalski': {'first_name': 'Jan', 'last_name': 'Kowalski'}
                }

    with open('employees.json', 'w') as f:
        json.dump(employees,f)

    print(load_json())
    print(json.dumps(employees))