from datetime import datetime

def get_zodiac_sign(day, month):
    if (month == 3 and day >= 21) or (month == 4 and day <= 19):
        return "Aries"
    elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
        return "Taurus"
    elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
        return "Gemini"
    elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
        return "Cancer"
    elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
        return "Leo"
    elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
        return "Virgo"
    elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
        return "Libra"
    elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
        return "Scorpio"
    elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
        return "Sagittarius"
    elif (month == 12 and day >= 22) or (month == 1 and day <= 19):
        return "Capricorn"
    elif (month == 1 and day >= 20) or (month == 2 and day <= 18):
        return "Aquarius"
    else:
        return "Pisces"

def get_name_rashi(name):
    if name == 'Chu' or name== 'che'  or name== 'la' or name == 'li' or name == 'lu'or name == 'le' or name == 'lo' or name == 'A' :
        return "Aries / Mesha"
    elif  name == 'E'or name == 'V'or name == 'Al'or name == 'O'or name == 'Vaa'or name == 'Vi' or name == 'Vu' or name == 'Ve' or name == 'Vo' or name=='U' or name=='Ud':
        return "Taurus / Vrishabha"
    elif  name == 'Ka'or name == 'Ki'or name == 'Ku'or name == 'Gh'or name == 'Chh'or name == 'Ke'or name == 'Ko'or name == 'Ha' or name== 'Hy' :
        return "Gemini / Mithuna"
    elif  name == 'Hi'or name == 'Hu'or name == 'Ho'or name == 'Da'or name == 'Dy'or name == 'Du'or name == 'Da' or name == 'Do' :
        return "Cancer / Kataka"
    elif  name == 'M' or name == 'Mi' or name == 'Mu' or name == 'Ma' or name == 'Me' or name == 'Mo' or name == 'Ta' or name == 'Ti' or name == 'Tu' or name == 'Te':
        return "Leo / Simha"
    elif name == 'To'or name == 'Pa'or name == 'Pi' or name == 'Pe'or name == 'Sha'or name == 'Thha'or name == 'Pe'or name == 'Po'or name=='Poo':
        return "Virgo / Kanya"
    elif name == 'Ra'or name == 'Ri'or name == 'Ru'or name == 'Re'or name == 'Ro'or name == 'Ti'or name == 'Taa'or name == 'Tu' or name == 'Te':
        return "Libra / Tula"
    elif name == 'To'or name == 'N'or name == 'Ni'or name == 'Nu'or name == 'No'or name == 'Ne'or name == 'Ya'or name == 'Yi' or name == 'Yu':
        return "Scorpio / Vrischik"
    elif name == 'Ye'or name == 'Yo'or name == 'Bha'or name == 'Bhi'or name == 'Bhu'or name == 'Dha'or name == 'Pha'or name == 'F' or name == 'Dhha' or name=='Bhe':
        return "Sagittarius / Dhanu"
    elif name == 'Bho'or name == 'Ja'or name == 'Ji'or name == 'Jy'or name == 'Khu'or name == 'Khoo'or name == 'Ga'or name == 'Gi' or name == 'Jo'or name=='Je' or name=='Gya' or name=='Ge' or name=='G':
        return "Capricorn / Makar"
    elif name == 'Sa'or name == 'S'or name == 'Si'or name == 'Soo'or name == 'Su'or name == 'Se'or name == 'So'or name == 'The' or name == 'Te' or name=='Gu' or name=='Goo' or name=='Ge' or name=='Gae':
        return "Aquarius / Kumbh"
    elif name == 'Dee'or name == 'Di'or name == 'Dik'or name == 'Du'or name == 'Deo'or name == 'Thha'or name == 'Jha'or name == 'Jyaa' or name == 'Do' or name=='Ch' or name=='Chi':
        return "Pisces / Meen"
    else:
        return "Enter again properly"
    
def get_lucky_number(rashi):
    if rashi=="Aries": 
        return "\n Your lucky number is 9,1 "
    elif rashi=="Taurus":
        return "\n Your lucky number is 2,8"
    elif rashi=="Gemini":
        return "\n Your lucky number is 3,7"
    elif rashi=="Cancer":
        return "\n Your lucky number is 4,6"
    elif rashi=="Leo":
        return "\n Your lucky number is 1,4,6"
    elif rashi=="Virgo":
        return "\n Your lucky number is 2,5,7"
    elif rashi=="Libra":
        return "\nYour lucky number is 1,2,7"
    elif rashi=="Scorpio":
        return "Your lucky number is 2,7,9"
    elif rashi=="Sagittarius":
        return "Your lucky number is 3,5,8"
    elif rashi=="Capricon":
        return "Your lucky number is 6,3,5"
    elif rashi =="Aquarius":
        return "Your lucky number is 2,3,7"
    elif rashi=="Pisces":
        return "Your lucky number is 1,3,4,9"
    else:
        return "all number are lucky"
    
    
    

def get_zodiac_characteristics(rashi):
    characteristics = {
        "Aries": "Courageous, energetic, optimistic, and independent, main=Flexibility",
        "Taurus": "Patient, reliable, warm-hearted, and determined, main=Adventure",
        "Gemini": "Adaptable, outgoing, intelligent, and lively,Main=Bravery",
        "Cancer": "Loyal, emotional, sympathetic, and persuasive, Main=Charisma",
        "Leo": "Generous, creative, cheerful, and passionate,Independant,Dominant,",
        "Virgo": "Practical, loyal, gentle, and analytical,Determinant",
        "Libra": "Charming, diplomatic, cooperative, and gracious,Patience",
        "Scorpio": "Resourceful, brave, passionate, and stubborn.",
        "Sagittarius": "Generous, idealistic, great sense of humor, and optimistic.",
        "Capricorn": "Responsible, disciplined, self-control, and good managers,Attractive",
        "Aquarius": "Progressive, original, independent, and humanitarian,Intuitive",
        "Pisces": "Compassionate, artistic, intuitive, and gentle."
    }
    return characteristics.get(rashi, "Invalid Zodiac Sign")

def main():
    name = input("Enter your name of 2 Character (first Character must be Capital) :\n ")
    dob_str = input("Enter your date of birth (DD-MM-YYYY): \n")
    rashi=input("Enter your rashi ")   
    rashi=input()
    print("\n")
        
    
    try:
        dob = datetime.strptime(dob_str, "%d-%m-%Y")
        zodiac_sign = get_zodiac_sign(dob.day, dob.month)
        name_rashi = get_name_rashi(name)
        characteristics = get_zodiac_characteristics(rashi)
        
        lucky_number= get_lucky_number(rashi) 
       
        print(f"\nHello, Dear start name with:  {name}!\n")
        print(f"Your Zodiac Sign according to date of birth: {zodiac_sign}\n")
        print(f"Your Zodiac Sign according to your name: {name_rashi}\n")
        print(f"select your rashi:{input()}\n")
        
        print("\n")
        
        
        print(f"Characteristic according to the rashi: \n{characteristics}\n")
        
        print(f"Let's find your lucky number according to your name rashi:\n {lucky_number}\n")

    except ValueError:
        print("Invalid date format. Please enter date in the format DD-MM-YYYY.")

if __name__ == "__main__":
    main()

