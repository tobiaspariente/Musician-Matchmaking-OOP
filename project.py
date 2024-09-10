import random

database = {'1': {'name':'John Lennon', 'age':'40', 'musicaltool':'guitar'},
            '2':{'name':'Elvis Presley', 'age':'42', 'musicaltool':'guitar'},
            '3':{'name':'Jimi Hendrix', 'age':'27', 'musicaltool':'guitar'},
            '4':{'name':'Aretha Franklin', 'age':'76', 'musicaltool':'piano'},
            '5':{'name':'Paul McCartney', 'age':'78', 'musicaltool':'guitar'},
            '6':{'name':'Stevie Wonder', 'age':'70', 'musicaltool':'piano'},
            '7':{'name':'Bob Dylan', 'age':'79', 'musicaltool':'guitar'},
            '8':{'name':'Led Zeppelin', 'age':'70', 'musicaltool':'guitar'},
            '9':{'name':'Elton John', 'age':'73', 'musicaltool':'piano'},
            '10':{'name':'George Harrison', 'age':'58', 'musicaltool':'guitar'},
            '11':{'name':'Paul McCartney', 'age':'78', 'musicaltool':'guitar'},
            '12':{'name':'John Mayer', 'age':'42', 'musicaltool':'guitar'},
            '13':{'name':'Neil Young', 'age':'76', 'musicaltool':'guitar'},
            '14':{'name':'Bruce Springsteen', 'age':'70', 'musicaltool':'guitar'},
            '15':{'name':'Joni Mitchell', 'age':'78', 'musicaltool':'guitar'},
            '16':{'name':'Paul Simon', 'age':'78', 'musicaltool':'guitar'},
            '17':{'name':'Michael Jackson', 'age':'50', 'musicaltool':'piano'},
            '18':{'name':'Janis Joplin', 'age':'27', 'musicaltool':'piano'},
            '19':{'name':'David Bowie', 'age':'69', 'musicaltool':'piano'},
            '20':{'name':'Frank Sinatra', 'age':'82', 'musicaltool':'piano'},
            '21':{'name':'Madonna', 'age':'64', 'musicaltool':'piano'},
            '22':{'name':'Bee Gees', 'age':'74', 'musicaltool':'piano'},
            '23':{'name':'Paul Simon', 'age':'78', 'musicaltool':'piano'}}

def find_musicians(database, preferred_instrument, preferred_age):
    scores = {}
    for i in database.keys():
        score = 0
        if database[i]['musicaltool'] == preferred_instrument:
            score += 1
        if int(database[i]['age']) in range(int(preferred_age) - 5, int(preferred_age) + 5):
            score += 1
        scores[i] = score
    sorted_scores = dict(sorted(scores.items(), key=lambda item: item[1], reverse=True))
    musicians = [database[key]['name']for key in sorted_scores.keys()]
    return musicians

def get_input(prompt):
    return input(prompt)

def main():

    print("Welcome to your musical space!")
    preferred_instrument = get_input("What is your favourite musical instrument? (piano/guitar). ")
    preferred_age = get_input("What is your favourite age group? ")
    preferred_city = get_input("In which city do you live? ")
    result = find_musicians(database, preferred_instrument, preferred_age)
    if result:
        print("Here is a list of musicians who most closely match your search criteria:")
        for i, musician in enumerate(result):
            print(f"{i + 1}. {musician}")
    else:
        print("Sorry, there are no musicians matching your search criteria.")

    surprise_choice()

def surprise_choice():
    while True:
        answer = input("Do you want a surprise choice? (yes/no). ")
        if answer.lower() == "yes":
            print("Good. Let's go for a surprise choice!")
            random_value = random.choice(list(database.items()))
            print(f"Here is it: {random_value}")
            break
        elif answer.lower() == "no":
            print("You are going to missed something :) ")
            break
        else:
            print("Please enter a valid answer (yes/no). ")

if __name__ == '__main__':
    main()
