import sqlite3

conn = sqlite3.connect('questions.db')
cursor = conn.cursor()

cursor.execute('DROP TABLE IF EXISTS questions')
cursor.execute('''CREATE TABLE IF NOT EXISTS questions (
                    id INTEGER PRIMARY KEY,
                    question TEXT NOT NULL,
                    option_a TEXT NOT NULL,
                    option_b TEXT NOT NULL,
                    option_c TEXT NOT NULL,
                    option_d TEXT NOT NULL,
                    correct_answer TEXT NOT NULL,
                    difficulty TEXT NOT NULL
                )''')

conn.commit()

questions_f1_easy = [
    ("Who has won the most races in the past 2 years in Formula 1?", "Lewis Hamilton", "Lando Norris", "Max Verstappen", "Charles Leclerc", "c", "easy"),
    ("F1 testing before the start of the season takes how many days?", "1", "2", "3", "4", "c", "easy"),
    ("Who has won the 2024 Bahrain Grand Prix?", "Carlos Sainz", "Charles Leclerc", "Lando Norris", "Max Verstappen", "d", "easy"),
    ("For what team does Sergio Perez drive?", "Force India", "Red Bull", "Racing Bulls", "Aston Martin", "b", "easy"),
    ("What nationality is Oscar Piastry?", "Australian", "English", "Austrian", "French", "a", "easy"),
    ("Which Formula 1 team was known as 'The Scuderia'?", "Ferrari", "McLaren", "Mercedes", "Red Bull", "a", "easy"),
    ("In which country is Suzuka?", "Azerbaijan", "America", "Japan", "Italy", "c", "easy"),
    ("When was the first Grand Prix in Imola held?", "1949", "1870", "1980", "2010", "c", "easy"),
    ("When was the first Grand Prix in Monaco held?", "1950", "1971", "1982", "2017", "a", "easy"),
    ("Who won the 2024 Miami Grand Prix?", "Lando Norris", "Max Verstappen", "Carlos Sainz", "Lewis Hamilton", "a", "easy"),
    ("Who won the 2021 Abu Dhabi Grand Prix?", "Fernando Alonso", "Sebastian Vettel", "Lewis Hamilton", "Max Verstappen", "d", "easy"),
    ("How many points did Red Bull get in the 2023 season?", "368", "427", "563", "860", "d", "easy"),
    ("How many points did Max Verstappen get in 2023?", "389", "575", "622", "491", "b", "easy"),
    ("What was the fastest ever speed in a race?", "372.56 km/h", "396.18 km/h", "361.94 km/h", "383.62 km/h", "a", "easy"),
    ("What was the longest ever F1 race?", "2015 Suzuka GP", "2011 Canadian GP", "1997 Imola GP", "2002 Spain GP", "b", "easy"),
    ("How much does a F1 car cost?", "ca. $12 mil", "ca. $24 mil", "ca. $15 mil", "ca. $9 mil", "c", "easy"),
    ("How many races are on the 2024 Race calendar?", "18", "28", "22", "24", "d", "easy"),
    ("With what teams did Michael Schumacher win his 7 world titles?", "Ferrari, Mercedes", "McLaren, Mercedes", "Ferrari, Benetton", "Ferrari, McLaren", "c", "easy"),
    ("How many World Championships did Juan Manuel Fangio win?", "2", "5", "6", "4", "b", "easy"),
    ("How many World Championships did Alain Prost win?", "2", "4", "1", "3", "b", "easy"),
    ("How many World Championships did Sebastian Vettel win?", "4", "1", "3", "2", "a", "easy"),
        
    ("Which F1 driver is known as the 'Iceman'?", "Lewis Hamilton", "Sebastian Vettel", "Kimi Räikkönen", "Fernando Alonso", "c", "easy"),
    ("Which team has a prancing horse as its logo?", "Red Bull", "Ferrari", "McLaren", "Mercedes", "b", "easy"),
    ("Which country hosts the Silverstone Grand Prix?", "Italy", "Germany", "France", "United Kingdom", "d", "easy"),
    ("Which driver has the most pole positions in F1 history?", "Ayrton Senna", "Lewis Hamilton", "Michael Schumacher", "Sebastian Vettel", "b", "easy"),
    ("Which driver won the first ever F1 World Championship?", "Juan Manuel Fangio", "Jack Brabham", "Nino Farina", "Alberto Ascari", "c", "easy"),
    ("Which circuit is also known as 'The Temple of Speed'?", "Monza", "Silverstone", "Spa-Francorchamps", "Nürburgring", "a", "easy"),
    ("Who is the team principal of Red Bull Racing?", "Toto Wolff", "Christian Horner", "Zak Brown", "Mattia Binotto", "b", "easy"),
    ("What is the nickname of the Monaco Grand Prix?", "The Jewel in the Crown", "The Crown Jewel", "The Diamond Race", "The Jewel of Racing", "a", "easy"),
    ("Which country hosts the Marina Bay Street Circuit?", "Malaysia", "Thailand", "Singapore", "Vietnam", "c", "easy"),
    ("Who was the first female driver to score points in F1?", "Lella Lombardi", "Desiré Wilson", "Giovanna Amati", "Maria Teresa de Filippis", "a", "easy"),
    ("Which F1 team is based in Woking, UK?", "Ferrari", "McLaren", "Mercedes", "Williams", "b", "easy"),
    ("What color is traditionally associated with Ferrari?", "Blue", "Green", "Red", "Yellow", "c", "easy"),
    ("Who won the 2020 F1 World Championship?", "Max Verstappen", "Sebastian Vettel", "Lewis Hamilton", "Charles Leclerc", "c", "easy"),
    ("Which circuit is known for the 'Eau Rouge' corner?", "Silverstone", "Spa-Francorchamps", "Monza", "Suzuka", "b", "easy"),
    ("What nationality is Lewis Hamilton?", "French", "British", "German", "American", "b", "easy"),
    ("Who was Ayrton Senna's main rival in the late 1980s?", "Nigel Mansell", "Nelson Piquet", "Alain Prost", "Michael Schumacher", "c", "easy"),
    ("Which team did Ayrton Senna drive for in 1988?", "Ferrari", "McLaren", "Williams", "Lotus", "b", "easy"),
    ("Which driver holds the record for the most F1 wins?", "Ayrton Senna", "Michael Schumacher", "Lewis Hamilton", "Sebastian Vettel", "c", "easy"),
    ("What is the minimum weight of an F1 car including the driver?", "500 kg", "600 kg", "700 kg", "800 kg", "d", "easy"),
    ("Which Grand Prix is held at the Circuit de Barcelona-Catalunya?", "French Grand Prix", "Italian Grand Prix", "Spanish Grand Prix", "Portuguese Grand Prix", "c", "easy")


]

questions_f1_hard = [
    ("What was the pole lap time at the 2024 Bahrain Grand Prix?", "1:30.143", "1:17.833", "1:28:481", "1:30:031", "d", "hard"),
    ("What was the winning margin at the 2024 Bahrain Grand Prix?", "14 seconds", "22 seconds", "35 seconds", "3 seconds", "b", "hard"),
    ("How long is the Bahrain International Circuit?", "5.412 km", "5.287 km", "4.924 km", "5.618 km", "a", "hard"),
    ("When was the first Grand Prix in Bahrain held?", "2002", "1996", "2010", "2004", "d", "hard"),
    ("How many laps is the Bahrain International Circuit?", "72", "51", "63", "57", "d", "hard"),
    ("When was the first Grand Prix in Saudi Arabia held?", "2012", "2021", "2022", "2018", "b", "hard"),
    ("How long is the Melbourne Grand Prix Circuit?", "5.278 km", "5.287 km", "4.821 km", "5.618 km", "a", "hard"),
    ("When was the first Grand Prix in Australia held?", "2002", "1996", "2001", "1986", "b", "hard"),
    ("How many laps is Suzuka?", "71", "52", "53", "68", "c", "hard"),
    ("Who won the 2024 Australian Grand Prix?", "Max Verstappen", "Charles Leclerc", "Fernando Alonso", "Carlos Sainz", "d", "hard"),
    ("Who won the 2024 Monaco Grand Prix?", "Max Verstappen", "Charles Leclerc", "Lando Norris", "Lewis Hamilton", "b", "hard"),
    ("Who won the 2024 Canadian Grand Prix?", "Max Verstappen", "Charles Leclerc", "Lando Norris", "George Russell", "a", "hard"),
    ("What was the pole lap time at the 2024 Emilia-Romagna Grand Prix?", "1:10.141", "1:17.833", "1:14:746", "1:15:034", "c", "hard"),
    ("In which country did Formula1 NOT race in 1950?", "Switzerland", "Belgium", "Spain", "USA", "c", "hard"),
    ("How long is the Silverstone Circuit?", "5.891 km", "5.227 km", "4.975 km", "5.518 km", "a", "hard"),
    ("How many laps is Spa in Belgium?", "71", "44", "64", "57", "b", "hard"),
    ("When was the first Grand Prix in Austria held?", "2002", "1996", "1970", "1982", "c", "hard"),
    ("When was the first Grand Prix in Brazil held?", "1973", "1996", "2000", "1998", "a", "hard"),
    ("How many laps is Brazil?", "71", "68", "64", "57", "a", "hard"),
    ("How many World Championships did Alberto Ascari win?", "2", "1", "none", "3", "a", "hard"),
        
    ("Which driver has the most fastest laps in F1 history?", "Michael Schumacher", "Lewis Hamilton", "Kimi Räikkönen", "Ayrton Senna", "a", "hard"),
    ("In which year did Ayrton Senna win his first World Championship?", "1988", "1990", "1991", "1985", "a", "hard"),
    ("How many times has the Monaco Grand Prix been canceled?", "1", "2", "3", "4", "a", "hard"),
    ("Which circuit hosted the first ever night race in F1?", "Bahrain", "Singapore", "Monaco", "Abu Dhabi", "b", "hard"),
    ("What was the length of the original Nürburgring circuit?", "14 km", "20 km", "22 km", "28 km", "c", "hard"),
    ("Who holds the record for the most consecutive wins in a single season?", "Sebastian Vettel", "Michael Schumacher", "Nico Rosberg", "Lewis Hamilton", "a", "hard"),
    ("Which year did Lewis Hamilton join Mercedes?", "2012", "2013", "2014", "2015", "b", "hard"),
    ("Which F1 team was formerly known as Tyrrell Racing?", "Red Bull Racing", "Mercedes", "Aston Martin", "Honda", "c", "hard"),
    ("Which driver was disqualified from the 1984 Monaco Grand Prix?", "Alain Prost", "Ayrton Senna", "Nigel Mansell", "Niki Lauda", "d", "hard"),
    ("Who was the first driver to win the F1 World Championship posthumously?", "Jim Clark", "Gilles Villeneuve", "Jochen Rindt", "Bruce McLaren", "c", "hard"),
    ("In which year was the first turbocharged F1 car introduced?", "1977", "1978", "1979", "1980", "a", "hard"),
    ("Which driver won the 2009 Hungarian Grand Prix?", "Jenson Button", "Lewis Hamilton", "Sebastian Vettel", "Fernando Alonso", "b", "hard"),
    ("How many World Championships did Alain Prost win with McLaren?", "1", "2", "3", "4", "c", "hard"),
    ("Which F1 driver has competed in the most Grand Prix races?", "Lewis Hamilton", "Michael Schumacher", "Fernando Alonso", "Kimi Räikkönen", "c", "hard"),
    ("Which team won the first ever F1 Constructors' Championship?", "Ferrari", "Vanwall", "Lotus", "Mercedes", "b", "hard"),
    ("In which year did Michael Schumacher win his first World Championship?", "1991", "1992", "1993", "1994", "d", "hard"),
    ("Which driver won the most races in the 2007 season?", "Lewis Hamilton", "Kimi Räikkönen", "Felipe Massa", "Fernando Alonso", "b", "hard"),
    ("Which F1 driver had the nickname 'The Professor'?", "Nigel Mansell", "Niki Lauda", "Alain Prost", "Gerhard Berger", "c", "hard"),
    ("What is the longest track on the current F1 calendar?", "Circuit de Monaco", "Circuit de Spa-Francorchamps", "Silverstone Circuit", "Suzuka Circuit", "b", "hard"),
    ("Which driver suffered a life-threatening crash at the 1976 German Grand Prix?", "James Hunt", "Jackie Stewart", "Niki Lauda", "Clay Regazzoni", "c", "hard")
]

questions_cars_easy = [
    ("Which car brand is known for producing the Mustang?", "Chevrolet", "Ford", "Dodge", "Toyota", "b", "easy"),
    ("What does SUV stand for?", "Super Utility Vehicle", "Sports Utility Vehicle", "Special Utility Vehicle", "Small Utility Vehicle", "b", "easy"),
    ("Which company manufactures the Accord?", "Nissan", "Honda", "Toyota", "Mazda", "b", "easy"),
    ("Which car brand is known for the logo with four rings?", "BMW", "Mercedes-Benz", "Audi", "Volkswagen", "c", "easy"),
    ("What type of car is a Honda Civic?", "Sedan", "SUV", "Truck", "Coupe", "a", "easy"),
    ("Which car brand is known for producing the 911 model?", "Ferrari", "Porsche", "Lamborghini", "BMW", "b", "easy"),
    ("Which company produces the Camry?", "Honda", "Toyota", "Mazda", "Subaru", "b", "easy"),
    ("Which car brand uses a prancing horse as its logo?", "Lamborghini", "Ferrari", "Maserati", "Porsche", "b", "easy"),
    ("What does ABS stand for in cars?", "Automatic Braking System", "Anti-lock Braking System", "Advanced Braking System", "Anti-slip Braking System", "b", "easy"),
    ("Which car company produces the Model S?", "Nissan", "Tesla", "Chevrolet", "Ford", "b", "easy"),
    ("What fuel does a diesel engine use?", "Gasoline", "Diesel", "Electricity", "Hydrogen", "b", "easy"),
    ("Which company manufactures the Wrangler?", "Jeep", "Ford", "Chevrolet", "Toyota", "a", "easy"),
    ("What is the main characteristic of an electric car?", "Uses gasoline", "Uses electricity", "Uses diesel", "Uses hybrid power", "b", "easy"),
    ("Which country is home to the car manufacturer BMW?", "Italy", "Germany", "Japan", "France", "b", "easy"),
    ("Which car brand is known for its luxury vehicles?", "Kia", "Lexus", "Hyundai", "Fiat", "b", "easy"),
    ("What type of vehicle is a Chevrolet Silverado?", "Sedan", "SUV", "Truck", "Coupe", "c", "easy"),
    ("Which car brand produces the Mustang?", "Dodge", "Ford", "Chevrolet", "Tesla", "b", "easy"),
    ("What is the primary function of a turbocharger in a car?", "Increase fuel efficiency", "Increase engine power", "Decrease emissions", "Improve braking", "b", "easy"),
    ("Which car manufacturer produces the GT-R?", "Toyota", "Nissan", "Honda", "Subaru", "b", "easy"),
    ("What type of vehicle is a Honda CR-V?", "Sedan", "SUV", "Truck", "Coupe", "b", "easy"),
    ("Which company produces the Corolla?", "Nissan", "Toyota", "Honda", "Mazda", "b", "easy"),
    ("What does RPM stand for in car terminology?", "Revolutions Per Minute", "Rotations Per Mile", "Rounds Per Meter", "Revolts Per Motor", "a", "easy"),
    ("Which car brand uses a lion in its logo?", "Peugeot", "Ferrari", "Maserati", "Bugatti", "a", "easy"),
    ("What is the main benefit of a hybrid car?", "Only uses gasoline", "Combines gasoline and electric power", "Only uses electricity", "Uses diesel and gasoline", "b", "easy"),
    ("Which company produces the Civic?", "Toyota", "Honda", "Nissan", "Mazda", "b", "easy"),
    ("What type of car is a Toyota Camry?", "Sedan", "SUV", "Truck", "Coupe", "a", "easy"),
    ("Which car brand is known for its three-pointed star logo?", "BMW", "Audi", "Mercedes-Benz", "Volkswagen", "c", "easy"),
    ("Which car brand produces the F-150?", "Chevrolet", "Ford", "Dodge", "Toyota", "b", "easy"),
    ("What does EV stand for in the context of cars?", "Electric Vehicle", "Eco Vehicle", "Enhanced Vehicle", "Energy Vehicle", "a", "easy"),
    ("Which car manufacturer is based in Italy?", "BMW", "Audi", "Ferrari", "Nissan", "c", "easy")

]

questions_cars_hard = [
    ("What is the displacement of the engine in a Bugatti Veyron?", "6.0 L", "7.0 L", "8.0 L", "9.0 L", "c", "hard"),
    ("Which car manufacturer created the rotary engine?", "Mazda", "Nissan", "Toyota", "Honda", "a", "hard"),
    ("What does the 'GT' stand for in the Ford GT?", "Grand Touring", "Grand Technology", "Grand Turbo", "Grand Traction", "a", "hard"),
    ("Which car company introduced the first mass-produced hybrid car?", "Toyota", "Honda", "Ford", "Chevrolet", "a", "hard"),
    ("What is the top speed of a Bugatti Chiron?", "300 km/h", "350 km/h", "420 km/h", "450 km/h", "c", "hard"),
    ("Which company produces the Aventador?", "Ferrari", "Lamborghini", "Maserati", "Pagani", "b", "hard"),
    ("What is the 0-60 mph time of a Tesla Model S Plaid?", "1.9 seconds", "2.1 seconds", "2.5 seconds", "3.0 seconds", "a", "hard"),
    ("Which car manufacturer has the model 'Countach'?", "Ferrari", "Lamborghini", "Maserati", "Pagani", "b", "hard"),
    ("Which car is known as the 'Godzilla'?", "Toyota Supra", "Nissan GT-R", "Mazda RX-7", "Subaru WRX", "b", "hard"),
    ("What type of engine configuration is used in a Subaru WRX?", "Inline-4", "V6", "Boxer", "Rotary", "c", "hard"),
    ("Which car manufacturer produces the 'LaFerrari'?", "Ferrari", "Lamborghini", "Maserati", "Pagani", "a", "hard"),
    ("What is the engine layout of a Porsche 911?", "Front-engine", "Mid-engine", "Rear-engine", "Side-engine", "c", "hard"),
    ("Which car brand is known for the 'Quattro' all-wheel-drive system?", "BMW", "Audi", "Mercedes-Benz", "Volkswagen", "b", "hard"),
    ("Which car has a V10 engine?", "Ford Mustang", "Chevrolet Corvette", "Dodge Viper", "Nissan GT-R", "c", "hard"),
    ("What is the power output of a Tesla Model 3 Performance?", "300 hp", "450 hp", "500 hp", "600 hp", "b", "hard"),
    ("Which car company produces the 'Veneno'?", "Ferrari", "Lamborghini", "Maserati", "Pagani", "b", "hard"),
    ("What is the range of a fully charged Tesla Model S?", "300 miles", "350 miles", "400 miles", "450 miles", "c", "hard"),
    ("Which car manufacturer introduced the first V8 engine?", "Ford", "Chevrolet", "Cadillac", "Oldsmobile", "c", "hard"),
    ("What is the top speed of a McLaren P1?", "200 mph", "217 mph", "225 mph", "250 mph", "b", "hard"),
    ("Which car has the model 'Hellcat'?", "Chevrolet Camaro", "Ford Mustang", "Dodge Challenger", "Nissan 370Z", "c", "hard"),
    ("What is the engine displacement of a Lamborghini Huracan?", "4.0 L", "5.0 L", "5.2 L", "6.0 L", "c", "hard"),
    ("Which car brand produces the 'R8'?", "BMW", "Audi", "Mercedes-Benz", "Lexus", "b", "hard"),
    ("Which car has the nickname 'Godzilla'?", "Toyota Supra", "Nissan GT-R", "Mazda RX-7", "Subaru WRX", "b", "hard"),
    ("What type of car is a Pagani Huayra?", "Sedan", "SUV", "Hypercar", "Coupe", "c", "hard"),
    ("Which car company produced the first hybrid sports car?", "Toyota", "Porsche", "Ferrari", "BMW", "b", "hard"),
    ("What is the engine layout of a Lamborghini Aventador?", "V6", "V8", "V10", "V12", "d", "hard"),
    ("Which car manufacturer introduced the first all-electric supercar?", "Tesla", "Rimac", "NIO", "Lucid", "b", "hard"),
    ("Which car company produces the 'Veyron'?", "Ferrari", "Lamborghini", "Maserati", "Bugatti", "d", "hard"),
    ("What is the 0-60 mph time of a Bugatti Veyron?", "2.5 seconds", "2.7 seconds", "3.0 seconds", "3.5 seconds", "a", "hard"),
    ("Which car manufacturer produces the 'Regera'?", "Koenigsegg", "Pagani", "Ferrari", "Lamborghini", "a", "hard")
]
questions_cars_movie = [
    ("What is the name of the main character in the movie 'Cars'?", "Lightning McQueen", "Mater", "Sally", "Doc Hudson", "a", "easy"),
    ("What type of car is Lightning McQueen?", "Truck", "Race car", "Sedan", "SUV", "b", "easy"),
    ("Who is Lightning McQueen's best friend in Radiator Springs?", "Sally", "Doc Hudson", "Mater", "Fillmore", "c", "easy"),
    ("What is the name of the town where most of the movie 'Cars' takes place?", "Radiator Springs", "Engine City", "Gasoline Alley", "Motorville", "a", "easy"),
    ("Who is the old racing legend that mentors Lightning McQueen?", "Sheriff", "Mater", "Doc Hudson", "Sarge", "c", "easy"),
    ("What is the name of the Italian tire shop owner in Radiator Springs?", "Luigi", "Guido", "Ramone", "Fillmore", "a", "easy"),
    ("Which character is a 1951 Hudson Hornet?", "Mater", "Doc Hudson", "Sally", "Luigi", "b", "easy"),
    ("What type of vehicle is Mater in 'Cars'?", "Race car", "Tow truck", "Sports car", "Sedan", "b", "easy"),
    ("Who is Lightning McQueen's love interest in the movie?", "Flo", "Sally", "Lizzie", "Mia", "b", "easy"),
    ("What is the name of the racing series in which Lightning McQueen competes?", "Piston Cup", "Turbo Cup", "Speedway Series", "Racing League", "a", "easy")
]
driver_questions = [
    ("Who became the youngest driver to start a Formula 1 race in 2015?", "Sebastian Vettel", "Lewis Hamilton", "Max Verstappen", "Charles Leclerc", "c", "easy"),
    ("Which team did Max Verstappen drive for when he won his first Formula 1 race?", "Ferrari", "Red Bull Racing", "Mercedes", "McLaren", "b", "easy"),
    ("In which year did Max Verstappen win his first Formula 1 World Championship?", "2019", "2020", "2021", "2022", "c", "easy"),
    ("Max Verstappen is from which country?", "Germany", "Belgium", "Netherlands", "Denmark", "c", "easy"),
    ("Who was Max Verstappen's teammate at Red Bull Racing in the 2020 season?", "Sebastian Vettel", "Pierre Gasly", "Alexander Albon", "Sergio Perez", "c", "easy"),
    ("Which Grand Prix did Max Verstappen win to secure his first World Championship?", "Brazilian Grand Prix", "Mexican Grand Prix", "Abu Dhabi Grand Prix", "Hungarian Grand Prix", "c", "easy"),
    ("Max Verstappen's father, Jos Verstappen, was also a Formula 1 driver. For which team did Jos drive in 1994?", "Benetton", "Ferrari", "McLaren", "Williams", "a", "hard"),
    ("In which season did Max Verstappen join Red Bull Racing?", "2014", "2015", "2016", "2017", "c", "easy"),
    ("How many races did Max Verstappen win in the 2022 Formula 1 season?", "7", "9", "11", "13", "d", "hard"),
    ("Max Verstappen achieved his first Formula 1 pole position at which Grand Prix?", "Spanish Grand Prix", "Mexican Grand Prix", "Hungarian Grand Prix", "Brazilian Grand Prix", "b", "hard"), 
    
    ("Which team did Michael Schumacher win his first World Championship with?", "Ferrari", "Benetton", "McLaren", "Mercedes", "b", "easy"),
    ("How many World Championships did Michael Schumacher win?", "5", "6", "7", "8", "c", "easy"),
    ("In which year did Michael Schumacher win his first Formula 1 race?", "1991", "1992", "1993", "1994", "b", "easy"),
    ("Michael Schumacher retired from Formula 1 in which year?", "2010", "2011", "2012", "2013", "c", "easy"),
    ("Which Grand Prix did Michael Schumacher win to achieve his first victory?", "British Grand Prix", "Belgian Grand Prix", "Italian Grand Prix", "German Grand Prix", "b", "easy"),
    ("Michael Schumacher made his Formula 1 debut with which team?", "Ferrari", "Benetton", "Jordan", "Mercedes", "c", "easy"),
    ("How many races did Michael Schumacher win in the 2004 season?", "11", "12", "13", "14", "d", "hard"),
    ("Michael Schumacher holds the record for the most consecutive World Championships. How many did he win in a row?", "3", "4", "5", "6", "c", "easy"),
    ("Which country is Michael Schumacher from?", "Austria", "Germany", "Switzerland", "Italy", "b", "easy"),
    ("What was Michael Schumacher's car number during his most successful period at Ferrari?", "1", "3", "5", "7", "c", "easy"),

    ("Which team did Ayrton Senna win his first World Championship with?", "Lotus", "Williams", "McLaren", "Ferrari", "c", "easy"),
    ("How many World Championships did Ayrton Senna win?", "2", "3", "4", "5", "b", "easy"),
    ("In which year did Ayrton Senna win his first Formula 1 race?", "1984", "1985", "1986", "1987", "b", "easy"),
    ("Ayrton Senna tragically passed away during which Grand Prix?", "Brazilian Grand Prix", "San Marino Grand Prix", "Monaco Grand Prix", "Canadian Grand Prix", "b", "easy"),
    ("Which Grand Prix is Ayrton Senna famously known for dominating in wet conditions in 1984?", "Portuguese Grand Prix", "Spanish Grand Prix", "Monaco Grand Prix", "Brazilian Grand Prix", "c", "easy"),
    ("Ayrton Senna made his Formula 1 debut with which team?", "McLaren", "Lotus", "Toleman", "Williams", "c", "easy"),
    ("How many races did Ayrton Senna win in the 1991 season?", "5", "6", "7", "8", "b", "hard"),
    ("Which country is Ayrton Senna from?", "Argentina", "Brazil", "Colombia", "Venezuela", "b", "easy"),
    ("What was Ayrton Senna's car number during his most successful period at McLaren?", "1", "2", "3", "4", "a", "easy"),
    ("Ayrton Senna won his last World Championship in which year?", "1990", "1991", "1992", "1993", "b", "easy"),

    ("Which driver won the Formula 1 World Championship in 2016?", "Lewis Hamilton", "Sebastian Vettel", "Nico Rosberg", "Kimi Räikkönen", "c", "easy"),
    ("Which driver is known as 'The Iceman'?", "Lewis Hamilton", "Sebastian Vettel", "Nico Rosberg", "Kimi Räikkönen", "d", "easy"),
    ("Which team did Fernando Alonso win his World Championships with?", "Ferrari", "Renault", "McLaren", "Red Bull Racing", "b", "easy"),
    ("Which driver has won the most Formula 1 World Championships?", "Juan Manuel Fangio", "Alain Prost", "Sebastian Vettel", "Michael Schumacher", "d", "easy"),
    ("Who became the youngest Formula 1 World Champion in history?", "Lewis Hamilton", "Sebastian Vettel", "Fernando Alonso", "Kimi Räikkönen", "b", "easy"),
    ("Which driver holds the record for the most Grand Prix starts?", "Rubens Barrichello", "Fernando Alonso", "Kimi Räikkönen", "Michael Schumacher", "b", "easy"),
    ("Which driver won the Formula 1 World Championship in 2007?", "Lewis Hamilton", "Sebastian Vettel", "Nico Rosberg", "Kimi Räikkönen", "d", "easy"),
    ("Who is the only driver to have won championships in both Formula 1 and IndyCar?", "Juan Pablo Montoya", "Nigel Mansell", "Mario Andretti", "Jacques Villeneuve", "b", "hard"),
    ("Which driver won his first World Championship with Mercedes in 1954?", "Alberto Ascari", "Juan Manuel Fangio", "Jack Brabham", "Mike Hawthorn", "b", "hard"),
    ("Which driver switched from Williams to Mercedes in 2022?", "George Russell", "Valtteri Bottas", "Esteban Ocon", "Sergio Perez", "a", "easy")

]


for question_data in questions_f1_easy:
    cursor.execute('''INSERT INTO questions (question, option_a, option_b, option_c, option_d, correct_answer, difficulty)
                    VALUES (?, ?, ?, ?, ?, ?, ?)''', question_data)
for question_data in questions_f1_hard:
    cursor.execute('''INSERT INTO questions (question, option_a, option_b, option_c, option_d, correct_answer, difficulty)
                    VALUES (?, ?, ?, ?, ?, ?, ?)''', question_data)
for question_data in questions_cars_easy:
    cursor.execute('''INSERT INTO questions (question, option_a, option_b, option_c, option_d, correct_answer, difficulty)
                    VALUES (?, ?, ?, ?, ?, ?, ?)''', question_data)
for question_data in questions_cars_hard:
    cursor.execute('''INSERT INTO questions (question, option_a, option_b, option_c, option_d, correct_answer, difficulty)
                    VALUES (?, ?, ?, ?, ?, ?, ?)''', question_data)
for question_data in questions_cars_movie:
    cursor.execute('''INSERT INTO questions (question, option_a, option_b, option_c, option_d, correct_answer, difficulty)
                    VALUES (?, ?, ?, ?, ?, ?, ?)''', question_data) 
for question_data in driver_questions:
    cursor.execute('''INSERT INTO questions (question, option_a, option_b, option_c, option_d, correct_answer, difficulty)
                    VALUES (?, ?, ?, ?, ?, ?, ?)''', question_data) 


def show():
    cursor.execute('SELECT * FROM questions')
    rows = cursor.fetchall()
    for row in rows:
        print(row)
#show()

conn.commit()
conn.close()
print("Data inserted successfully.")

