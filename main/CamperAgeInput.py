"""
 Morgan Christensen
 Module 2 Camper Age input
 Updated: 09/07/20

 Program that takes in a users input for years and converts it to months
"""
import constants


def convert_to_months(years):
    months = years * constants.MONTHS
    return months


if __name__ == '__main__':
    age_in_years = input("Enter your child's age in: ")
    age_in_months = convert_to_months(int(age_in_years))
    print("{} years is {} months".format(age_in_years, age_in_months))
