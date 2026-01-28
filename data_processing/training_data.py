TRAIN_DATA = [

    ("cars drove his Toyota Camry to work.", {"entities": [(14, 26, "VEHICLE")]}),
    ("cars bought a Honda Civic last week.", {"entities": [(14, 25, "VEHICLE")]}),
    ("The Ford F-150 was parked outside.", {"entities": [(4, 13, "VEHICLE")]}),
    ("A Tesla Model S can accelerate very fast.", {"entities": [(2, 14, "VEHICLE")]}),
    ("He rented a Chevrolet Malibu for the weekend.", {"entities": [(12, 28, "VEHICLE")]}),
    ("Carss owns a Nissan Altima.", {"entities": [(13, 25, "VEHICLE")]}),
    ("The Dodge Charger is very popular.", {"entities": [(4, 16, "VEHICLE")]}),
    ("Calledd drove a BMW X5 through the city.", {"entities": [(12, 19, "VEHICLE")]}),
    ("We saw a Porsche 911 on the street.", {"entities": [(8, 18, "VEHICLE")]}),
    ("Her Audi A4 was recently serviced.", {"entities": [(4, 11, "VEHICLE")]}),
    ("Called Toyota Camry reg no. ABC1234 is parked outside.", {"entities": [(8, 20, "VEHICLE"), (24, 31, "PLATE")]}),
    ("Cars drove a Honda Civic plate XYZ5678 yesterday.", {"entities": [(12, 23, "VEHICLE"), (30, 37, "PLATE")]}),
    ("A Ford F-150 with reg no. F150XY was seen downtown.", {"entities": [(2, 11, "VEHICLE"), (17, 24, "PLATE")]}),
    ("Tesla Model S plate TS12345 is very fast.", {"entities": [(0, 12, "VEHICLE"), (18, 25, "PLATE")]}),
    ("Chevrolet Malibu reg no. CHEV567 was rented.", {"entities": [(0, 16, "VEHICLE"), (20, 27, "PLATE")]}),
    ("Nissan Altima with plate NA9988 is in the garage.", {"entities": [(0, 12, "VEHICLE"), (23, 29, "PLATE")]}),
    ("Dodge Charger reg no. DC2023 is new.", {"entities": [(0, 13, "VEHICLE"), (17, 24, "PLATE")]}),
    ("BMW X5 plate BX5555 belongs to.", {"entities": [(0, 7, "VEHICLE"), (13, 20, "PLATE")]}),
    ("Porsche 911 reg no. P911XX was spotted.", {"entities": [(0, 10, "VEHICLE"), (14, 21, "PLATE")]}),
    ("Audi A4 with plate AA1234 is her car.", {"entities": [(0, 7, "VEHICLE"), (17, 23, "PLATE")]}),
    ("Carss Jeep Wrangler is off-road ready.", {"entities": [(6, 19, "VEHICLE")]}),
    ("A Subaru Outback drove past the park.", {"entities": [(2, 17, "VEHICLE")]}),
    ("He traded his Kia Sorento for a newer model.", {"entities": [(13, 24, "VEHICLE")]}),
    ("The Volkswagen Golf is parked outside.", {"entities": [(4, 19, "VEHICLE")]}),
    ("Cars rented a Hyundai Tucson for her trip.", {"entities": [(12, 25, "VEHICLE")]}),
    ("The Ram 1500 is known for its durability.", {"entities": [(4, 11, "VEHICLE")]}),
    ("Called Acura MDX is brand new.", {"entities": [(7, 15, "VEHICLE")]}),
    ("He leased a Cadillac Escalade.", {"entities": [(10, 25, "VEHICLE")]}),
    ("Their GMC Sierra is very reliable.", {"entities": [(5, 14, "VEHICLE")]}),
    ("A Lincoln Navigator was on display.", {"entities": [(2, 21, "VEHICLE")]}),
    ("Mini Cooper reg no. MC2021 is parked.", {"entities": [(0, 11, "VEHICLE"), (15, 21, "PLATE")]}),
    ("Maserati Ghibli plate MG1234 is on the street.", {"entities": [(0, 14, "VEHICLE"), (20, 26, "PLATE")]}),
    ("Bentley Continental GT reg no. BCGT99 belongs to cars.", {"entities": [(0, 25, "VEHICLE"), (29, 36, "PLATE")]}),
    ("Fiat 500 plate F500ZZ is compact.", {"entities": [(0, 8, "VEHICLE"), (14, 20, "PLATE")]}),
    ("Alfa Romeo Giulia reg no. ARG456 was sold.", {"entities": [(0, 18, "VEHICLE"), (22, 29, "PLATE")]}),
    ("Volvo XC90 plate VX9090 is spacious.", {"entities": [(0, 11, "VEHICLE"), (17, 23, "PLATE")]}),
    ("Chrysler Pacifica reg no. CP2023 parked outside.", {"entities": [(0, 20, "VEHICLE"), (24, 31, "PLATE")]}),
    ("Peugeot 3008 plate P3008Y belongs to her.", {"entities": [(0, 13, "VEHICLE"), (19, 25, "PLATE")]}),
    ("Renault Megane reg no. RM2022 is efficient.", {"entities": [(0, 14, "VEHICLE"), (18, 25, "PLATE")]}),
    ("Dodge Durango plate DD1234 is his car.", {"entities": [(0, 13, "VEHICLE"), (19, 25, "PLATE")]}),
    ("Honda Accord is popular worldwide.", {"entities": [(0, 12, "VEHICLE")]}),
    ("Ford Mustang is very fast.", {"entities": [(0, 12, "VEHICLE")]}),
    ("Toyota Corolla has low maintenance costs.", {"entities": [(0, 14, "VEHICLE")]}),
    ("Chevrolet Tahoe is spacious.", {"entities": [(0, 16, "VEHICLE")]}),
    ("BMW 3 Series is a compact sedan.", {"entities": [(0, 12, "VEHICLE")]}),
    ("Mercedes-Benz C-Class is elegant.", {"entities": [(0, 17, "VEHICLE")]}),
    ("Audi Q7 has advanced features.", {"entities": [(0, 8, "VEHICLE")]}),
    ("Jeep Grand Cherokee is off-road ready.", {"entities": [(0, 20, "VEHICLE")]}),
    ("Subaru Forester is reliable.", {"entities": [(0, 16, "VEHICLE")]}),
    ("Kia Sportage is affordable.", {"entities": [(0, 13, "VEHICLE")]}),
    ("Toyota Hilux reg no. TH1234 was sold.", {"entities": [(0, 12, "VEHICLE"), (16, 23, "PLATE")]}),
    ("Honda CR-V plate HCR567 is new.", {"entities": [(0, 10, "VEHICLE"), (16, 22, "PLATE")]}),
    ("Ford Ranger reg no. FR2022 is durable.", {"entities": [(0, 11, "VEHICLE"), (15, 22, "PLATE")]}),
    ("BMW Z4 plate BZ4001 was parked outside.", {"entities": [(0, 7, "VEHICLE"), (13, 19, "PLATE")]}),
    ("Chevrolet Camaro reg no. CC2023 is fast.", {"entities": [(0, 17, "VEHICLE"), (21, 28, "PLATE")]}),
    ("Mercedes GLE plate MG5000 is luxury.", {"entities": [(0, 13, "VEHICLE"), (19, 25, "PLATE")]}),
    ("Audi A6 reg no. AA6000 belongs to cars.", {"entities": [(0, 7, "VEHICLE"), (11, 17, "PLATE")]}),
    ("Nissan Pathfinder plate NP7777 is rugged.", {"entities": [(0, 17, "VEHICLE"), (23, 29, "PLATE")]}),
    ("Toyota RAV4 reg no. TR8888 is family-friendly.", {"entities": [(0, 12, "VEHICLE"), (16, 22, "PLATE")]}),
    ("Ford Explorer plate FE9999 is spacious.", {"entities": [(0, 13, "VEHICLE"), (19, 25, "PLATE")]}),

    ("Call call at 07123 456789.", {"entities": [(13, 24, "TELECOMS")]}),
    ("called phone number is 07234 567890.", {"entities": [(23, 34, "TELECOMS")]}),
    ("Contact me at 07345 678901.", {"entities": [(14, 25, "TELECOMS")]}),
    ("Emergency line: 07456 789012.", {"entities": [(16, 27, "TELECOMS")]}),
    ("Office number: 07567 890123.", {"entities": [(15, 26, "TELECOMS")]}),
    ("Reach me on 07678 901234.", {"entities": [(12, 23, "TELECOMS")]}),
    ("My new number is 07789 012345.", {"entities": [(17, 28, "TELECOMS")]}),
    ("Call 07890 123456 for support.", {"entities": [(5, 16, "TELECOMS")]}),
    ("Contact via 07901 234567.", {"entities": [(12, 23, "TELECOMS")]}),
    ("Phone: 07012 345678", {"entities": [(7, 18, "TELECOMS")]}),
    ("Reach us at 07123 987654.", {"entities": [(13, 24, "TELECOMS")]}),
    ("Customer service: 07234 876543.", {"entities": [(18, 29, "TELECOMS")]}),
    ("Dial 07345 765432 for inquiries.", {"entities": [(5, 16, "TELECOMS")]}),
    ("Support line: 07456 654321.", {"entities": [(14, 25, "TELECOMS")]}),
    ("called number is 07567 543210.", {"entities": [(16, 27, "TELECOMS")]}),
    ("Emergency contact: 07678 432109.", {"entities": [(19, 30, "TELECOMS")]}),
    ("call can be reached at 07789 321098.", {"entities": [(23, 34, "TELECOMS")]}),
    ("Phone number: 07890 210987.", {"entities": [(14, 25, "TELECOMS")]}),
    ("Contact: 07901 109876.", {"entities": [(9, 20, "TELECOMS")]}),
    ("Customer care: 07012 998877.", {"entities": [(15, 26, "TELECOMS")]}),
    ("For help call 07123 887766.", {"entities": [(13, 24, "TELECOMS")]}),
    ("Reach us at 07234 776655.", {"entities": [(12, 23, "TELECOMS")]}),
    ("Service hotline: 07345 665544.", {"entities": [(17, 28, "TELECOMS")]}),
    ("Call 07456 554433 for assistance.", {"entities": [(5, 16, "TELECOMS")]}),
    ("Contact me on 07567 443322.", {"entities": [(14, 25, "TELECOMS")]}),
    ("Support: 07678 332211.", {"entities": [(9, 20, "TELECOMS")]}),
    ("Customer line: 07789 221100.", {"entities": [(15, 26, "TELECOMS")]}),
    ("called hotline is 07890 110099.", {"entities": [(17, 28, "TELECOMS")]}),
    ("Call us: 07901 009988.", {"entities": [(9, 20, "TELECOMS")]}),
    ("Emergency: 07012 998877.", {"entities": [(11, 22, "TELECOMS")]}),
    ("Reach call at 07123 887799.", {"entities": [(14, 25, "TELECOMS")]}),
    ("Dial 07234 776688 for info.", {"entities": [(5, 16, "TELECOMS")]}),
    ("Contact call at 07345 665577.", {"entities": [(16, 27, "TELECOMS")]}),
    ("Phone support: 07456 554466.", {"entities": [(15, 26, "TELECOMS")]}),
    ("Call our office at 07567 443388.", {"entities": [(19, 30, "TELECOMS")]}),
    ("For inquiries dial 07678 332299.", {"entities": [(18, 29, "TELECOMS")]}),
    ("Reach out to 07789 221133.", {"entities": [(13, 24, "TELECOMS")]}),
    ("Emergency contact: 07890 110022.", {"entities": [(19, 30, "TELECOMS")]}),
    ("Called hotline: 07901 009911.", {"entities": [(15, 26, "TELECOMS")]}),
    ("Call support at 07012 998833.", {"entities": [(16, 27, "TELECOMS")]}),
    ("Dial 07123 445566 for help.", {"entities": [(5, 16, "TELECOMS")]}),
    ("Reach us at 07234 556677.", {"entities": [(12, 23, "TELECOMS")]}),
    ("Service number: 07345 667788.", {"entities": [(16, 27, "TELECOMS")]}),
    ("Phone call at 07456 778899.", {"entities": [(11, 22, "TELECOMS")]}),
    ("Contact support: 07567 889900.", {"entities": [(17, 28, "TELECOMS")]}),
    ("Reach me on 07678 990011.", {"entities": [(12, 23, "TELECOMS")]}),
    ("Emergency: 07789 001122.", {"entities": [(11, 22, "TELECOMS")]}),
    ("Customer care line: 07890 112233.", {"entities": [(21, 32, "TELECOMS")]}),
    ("Call our hotline 07901 223344.", {"entities": [(18, 29, "TELECOMS")]}),
    ("Support desk: 07012 334455.", {"entities": [(14, 25, "TELECOMS")]}),
    ("Called number: 07123 445577.", {"entities": [(15, 26, "TELECOMS")]}),
    ("Dial 07234 556688 for assistance.", {"entities": [(5, 16, "TELECOMS")]}),
    ("Reach support at 07345 667799.", {"entities": [(17, 28, "TELECOMS")]}),
    ("Call 07456 778800 for info.", {"entities": [(5, 16, "TELECOMS")]}),
    ("Call can be reached on 07567 889911.", {"entities": [(27, 38, "TELECOMS")]}),
    
    ("Call John Smith for details.", {"entities": [(5, 15, "NAME")]}),
    ("Mary Johnson will attend the meeting.", {"entities": [(0, 12, "NAME")]}),
    ("Contact Michael Brown via email.", {"entities": [(8, 21, "NAME")]}),
    ("Sarah Lee is the project manager.", {"entities": [(0, 9, "NAME")]}),
    ("Reach out to David Wilson today.", {"entities": [(13, 25, "NAME")]}),
    ("Emily Davis sent the documents.", {"entities": [(0, 11, "NAME")]}),
    ("James Taylor called earlier.", {"entities": [(0, 11, "NAME")]}),
    ("Olivia Martin is in the office.", {"entities": [(0, 12, "NAME")]}),
    ("Contact Daniel Thomas immediately.", {"entities": [(8, 21, "NAME")]}),
    ("Sophia White replied to the email.", {"entities": [(0, 11, "NAME")]}),
    ("Matthew Harris will join soon.", {"entities": [(0, 14, "NAME")]}),
    ("Isabella Clark sent a message.", {"entities": [(0, 13, "NAME")]}),
    ("Joshua Lewis is on leave.", {"entities": [(0, 12, "NAME")]}),
    ("Mia Robinson called yesterday.", {"entities": [(0, 11, "NAME")]}),
    ("Alexander Walker submitted the report.", {"entities": [(0, 17, "NAME")]}),
    ("Charlotte Hall confirmed the appointment.", {"entities": [(0, 14, "NAME")]}),
    ("Benjamin Allen will attend the workshop.", {"entities": [(0, 14, "NAME")]}),
    ("Amelia Young is working remotely.", {"entities": [(0, 12, "NAME")]}),
    ("Ethan King is the team lead.", {"entities": [(0, 10, "NAME")]}),
    ("Harper Scott replied to the chat.", {"entities": [(0, 12, "NAME")]}),
    ("William Green submitted his form.", {"entities": [(0, 13, "NAME")]}),
    ("Ella Baker confirmed her attendance.", {"entities": [(0, 10, "NAME")]}),
    ("Logan Adams sent the package.", {"entities": [(0, 11, "NAME")]}),
    ("Avery Nelson is on vacation.", {"entities": [(0, 12, "NAME")]}),
    ("Daniel Carter requested a meeting.", {"entities": [(0, 13, "NAME")]}),
    ("Lily Mitchell approved the request.", {"entities": [(0, 11, "NAME")]}),
    ("Jackson Perez will call later.", {"entities": [(0, 13, "NAME")]}),
    ("Grace Roberts sent an email.", {"entities": [(0, 12, "NAME")]}),
    ("Sebastian Turner is unavailable today.", {"entities": [(0, 18, "NAME")]}),
    ("Victoria Phillips replied promptly.", {"entities": [(0, 17, "NAME")]}),    
    ("Owen Campbell is on leave.", {"entities": [(0, 12, "NAME")]}),
    ("Zoey Parker submitted her work.", {"entities": [(0, 11, "NAME")]}),
    ("Henry Evans is in a meeting.", {"entities": [(0, 11, "NAME")]}),
    ("Chloe Edwards replied quickly.", {"entities": [(0, 12, "NAME")]}),
    ("Nathan Collins will attend the call.", {"entities": [(0, 14, "NAME")]}),
    ("Aria Stewart confirmed her slot.", {"entities": [(0, 11, "NAME")]}),
    ("Samuel Sanchez is the speaker.", {"entities": [(0, 14, "NAME")]}),
    ("Hannah Morris will be late.", {"entities": [(0, 12, "NAME")]}),
    ("Ryan Rogers completed the task.", {"entities": [(0, 11, "NAME")]}),
    ("Lillian Reed submitted the file.", {"entities": [(0, 13, "NAME")]}),
    ("David Brooks is in the office.", {"entities": [(0, 12, "NAME")]}),
    ("Scarlett Gray will call soon.", {"entities": [(0, 14, "NAME")]}),
    ("Leo Price replied yesterday.", {"entities": [(0, 9, "NAME")]}),
    ("Layla Jenkins submitted her form.", {"entities": [(0, 13, "NAME")]}),
    ("Joseph Coleman will attend.", {"entities": [(0, 13, "NAME")]}),
    ("Riley Stewart sent the update.", {"entities": [(0, 13, "NAME")]}),
    ("Anthony Hughes is working today.", {"entities": [(0, 15, "NAME")]}),
    ("Aurora Simmons responded quickly.", {"entities": [(0, 14, "NAME")]}),
    ("Isaac Foster will join the call.", {"entities": [(0, 12, "NAME")]}),
    ("Sofia Bryant submitted her report.", {"entities": [(0, 13, "NAME")]}),
    ("Lucas Russell is available now.", {"entities": [(0, 12, "NAME")]}),
    ("Maya Griffin replied to the email.", {"entities": [(0, 12, "NAME")]}),
    ("Jack Hughes completed the task.", {"entities": [(0, 11, "NAME")]}),
    ("Emily Long is on holiday.", {"entities": [(0, 10, "NAME")]}),
    ("Connor Ward will attend the meeting.", {"entities": [(0, 12, "NAME")]}),
    ("Abigail Patterson sent the files.", {"entities": [(0, 16, "NAME")]}),
    ("Oliiver Bennett is in the office.", {"entities": [(0, 15, "NAME")]}),
    ("Ella Simmons responded yesterday.", {"entities": [(0, 10, "NAME")]}),
    ("Nathaniel Coleman submitted the request.", {"entities": [(0, 17, "NAME")]}),
    ("Grace Powell confirmed her attendance.", {"entities": [(0, 11, "NAME")]}),
    
    ("123 Baker Street, London is busy today.", {"entities": [(0, 16, "LOCATION"), (18, 24, "LOCATION")]}),
    ("He lives at 56 High Road, Manchester.", {"entities": [(14, 25, "LOCATION"), (27, 37, "LOCATION")]}),
    ("The office is located at 78 King Street, Bristol.", {"entities": [(29, 41, "LOCATION"), (43, 50, "LOCATION")]}),
    ("We visited 12 Elm Avenue yesterday.", {"entities": [(11, 24, "LOCATION")]}),
    ("The restaurant is at 45 Park Lane, Leeds.", {"entities": [(22, 33, "LOCATION"), (35, 40, "LOCATION")]}),
    ("Their shop is on 99 Queen Road, Birmingham.", {"entities": [(16, 27, "LOCATION"), (29, 39, "LOCATION")]}),
    ("The conference is happening in Oxford.", {"entities": [(34, 40, "LOCATION")]}),
    ("She moved to 21 Maple Drive, Liverpool.", {"entities": [(14, 27, "LOCATION"), (29, 38, "LOCATION")]}),
    ("The hotel is located at 5 King Street, York.", {"entities": [(27, 38, "LOCATION"), (40, 44, "LOCATION")]}),
    ("We stayed at 10 Pine Street, Brighton.", {"entities": [(12, 25, "LOCATION"), (27, 35, "LOCATION")]}),
    ("The museum is on 33 Church Lane, Nottingham.", {"entities": [(17, 30, "LOCATION"), (32, 42, "LOCATION")]}),
    ("Meet me at 7 Willow Road, Sheffield.", {"entities": [(11, 23, "LOCATION"), (25, 34, "LOCATION")]}),
    ("The park is located in Cambridge.", {"entities": [(22, 31, "LOCATION")]}),
    ("He lives near 88 Oak Avenue, Leicester.", {"entities": [(14, 26, "LOCATION"), (28, 36, "LOCATION")]}),
    ("The library is at 50 Station Road, Durham.", {"entities": [(16, 30, "LOCATION"), (32, 38, "LOCATION")]}),
    ("The cafe can be found at 3 Elm Street, York.", {"entities": [(28, 38, "LOCATION"), (40, 44, "LOCATION")]}),
    ("We took a trip to 77 Rose Street, Bath.", {"entities": [(20, 32, "LOCATION"), (34, 38, "LOCATION")]}),
    ("The shop is located at 12 Garden Road, Exeter.", {"entities": [(27, 39, "LOCATION"), (41, 47, "LOCATION")]}),
    ("He moved to 25 Willow Lane, Oxford.", {"entities": [(13, 26, "LOCATION"), (28, 34, "LOCATION")]}),
    ("The office is at 14 King Street, Coventry.", {"entities": [(14, 27, "LOCATION"), (29, 37, "LOCATION")]}),
    ("The supermarket is on 90 Victoria Street, Leeds.", {"entities": [(22, 40, "LOCATION"), (42, 47, "LOCATION")]}),
    ("We visited 34 Church Street, Cambridge.", {"entities": [(11, 28, "LOCATION"), (30, 39, "LOCATION")]}),
    ("The bank is at 5 Elm Road, Nottingham.", {"entities": [(13, 23, "LOCATION"), (25, 35, "LOCATION")]}),
    ("Meet me near 88 Park Avenue, Manchester.", {"entities": [(15, 27, "LOCATION"), (29, 39, "LOCATION")]}),
    ("The concert was held in Birmingham.", {"entities": [(25, 36, "LOCATION")]}),
    ("He rented a flat at 21 Willow Street, Leeds.", {"entities": [(24, 39, "LOCATION"), (41, 46, "LOCATION")]}),
    ("The market is at 12 Rose Avenue, Bristol.", {"entities": [(16, 29, "LOCATION"), (31, 37, "LOCATION")]}),
    ("She moved to 7 Oak Lane, Sheffield.", {"entities": [(13, 23, "LOCATION"), (25, 34, "LOCATION")]}),
    ("The hotel is on 33 Garden Street, Liverpool.", {"entities": [(16, 32, "LOCATION"), (34, 43, "LOCATION")]}),
    ("We walked along 45 Church Road, York.", {"entities": [(18, 33, "LOCATION"), (35, 39, "LOCATION")]}),
    ("The stadium is located at 90 Victoria Road, Leeds.", {"entities": [(28, 45, "LOCATION"), (47, 52, "LOCATION")]}),
    ("Meet me at 21 Elm Street, Cambridge.", {"entities": [(11, 24, "LOCATION"), (26, 35, "LOCATION")]}),
    ("The cafe is on 5 Maple Avenue, Nottingham.", {"entities": [(14, 28, "LOCATION"), (30, 40, "LOCATION")]}),
    ("He lives at 77 Oak Street, Leicester.", {"entities": [(13, 25, "LOCATION"), (27, 35, "LOCATION")]}),
    ("The park is located in York.", {"entities": [(22, 26, "LOCATION")]}),
    ("She stayed at 12 King Lane, Bath.", {"entities": [(15, 28, "LOCATION"), (30, 34, "LOCATION")]}),
    ("The library is at 34 Rose Road, Exeter.", {"entities": [(16, 28, "LOCATION"), (30, 36, "LOCATION")]}),
    ("We walked through 25 Garden Street, Oxford.", {"entities": [(19, 34, "LOCATION"), (36, 42, "LOCATION")]}),
    ("The cinema is at 7 Church Avenue, Coventry.", {"entities": [(17, 33, "LOCATION"), (35, 43, "LOCATION")]}),
    ("They went to 88 Victoria Lane, Manchester.", {"entities": [(12, 29, "LOCATION"), (31, 41, "LOCATION")]}),
    ("The gallery is located at 90 Oak Street, Bristol.", {"entities": [(28, 42, "LOCATION"), (44, 50, "LOCATION")]}),
    ("We visited 5 Willow Road, Sheffield.", {"entities": [(11, 24, "LOCATION"), (26, 35, "LOCATION")]}),
    ("The museum is on 33 Elm Avenue, Cambridge.", {"entities": [(17, 30, "LOCATION"), (32, 41, "LOCATION")]}),
    ("He lives at 12 King Street, Leeds.", {"entities": [(14, 27, "LOCATION"), (29, 34, "LOCATION")]}),
    ("The cafe is located at 21 Rose Lane, York.", {"entities": [(23, 35, "LOCATION"), (37, 41, "LOCATION")]}),
    ("Meet me at 7 Garden Street, Liverpool.", {"entities": [(11, 27, "LOCATION"), (29, 38, "LOCATION")]}),
    ("The shop is on 45 Church Lane, Nottingham.", {"entities": [(16, 31, "LOCATION"), (33, 43, "LOCATION")]}),
    ("We stayed at 34 Park Road, Leicester.", {"entities": [(12, 25, "LOCATION"), (27, 35, "LOCATION")]}),
    ("The office is at 88 Victoria Street, Bath.", {"entities": [(14, 33, "LOCATION"), (35, 39, "LOCATION")]}),
    ("They moved to 5 Elm Lane, Oxford.", {"entities": [(13, 24, "LOCATION"), (26, 32, "LOCATION")]}),

    ("The Ford Fiesta was seen near 21 Baker Street, London.",
     {"entities": [(4, 15, "VEHICLE"), (29, 44, "LOCATION"), (46, 52, "LOCATION")]}),

    ("Sarah owns a Volkswagen Golf.",
     {"entities": [(0, 5, "NAME"), (12, 27, "VEHICLE")]}),

    ("Call 07123 456789 about the Toyota Corolla.",
     {"entities": [(5, 18, "TELECOM"), (33, 48, "VEHICLE")]}),

    ("A BMW 3 Series was parked outside.",
     {"entities": [(2, 14, "VEHICLE")]}),

    ("James drives a Nissan Qashqai.",
     {"entities": [(0, 5, "NAME"), (14, 30, "VEHICLE")]}),

    ("The Audi A4 is registered to 07987 654321.",
     {"entities": [(4, 12, "VEHICLE"), (30, 43, "TELECOM")]}),

    ("A Honda Civic was spotted in Manchester.",
     {"entities": [(2, 14, "VEHICLE"), (30, 40, "LOCATION")]}),

    ("Emily recently bought a Kia Sportage.",
     {"entities": [(0, 5, "NAME"), (22, 34, "VEHICLE")]}),

    ("Text 07811 223344 regarding the Skoda Octavia.",
     {"entities": [(5, 18, "TELECOM"), (34, 48, "VEHICLE")]}),

    ("The Mercedes C Class was near Oxford.",
     {"entities": [(4, 21, "VEHICLE"), (31, 37, "LOCATION")]}),

    ("Daniel owns a Hyundai Tucson.",
     {"entities": [(0, 6, "NAME"), (15, 29, "VEHICLE")]}),

    ("A Peugeot 208 was linked to 07777 888999.",
     {"entities": [(2, 13, "VEHICLE"), (31, 44, "TELECOM")]}),

    ("The Vauxhall Astra was seen on King Street, Leeds.",
     {"entities": [(4, 20, "VEHICLE"), (32, 43, "LOCATION"), (45, 50, "LOCATION")]}),

    ("Olivia drives a Renault Clio.",
     {"entities": [(0, 6, "NAME"), (16, 28, "VEHICLE")]}),

    ("Call 07999 111222 if you find the Mazda CX5.",
     {"entities": [(5, 18, "TELECOM"), (36, 45, "VEHICLE")]}),

    ("The Seat Ibiza was parked in Bristol.",
     {"entities": [(4, 15, "VEHICLE"), (31, 38, "LOCATION")]}),

    ("Michael bought a Volvo XC60.",
     {"entities": [(0, 7, "NAME"), (17, 28, "VEHICLE")]}),

    ("A Toyota Yaris was associated with 07001 222333.",
     {"entities": [(2, 15, "VEHICLE"), (36, 49, "TELECOM")]}),

    ("The Citroen C3 was seen near Park Lane, York.",
     {"entities": [(4, 15, "VEHICLE"), (29, 38, "LOCATION"), (40, 44, "LOCATION")]}),

    ("Sophia owns a Mini Cooper.",
     {"entities": [(0, 6, "NAME"), (15, 26, "VEHICLE")]}),

    ("Please contact 07222 333444 about the Ford Focus.",
     {"entities": [(15, 28, "TELECOM"), (43, 53, "VEHICLE")]}),

    ("A Tesla Model 3 was parked in Cambridge.",
     {"entities": [(2, 16, "VEHICLE"), (32, 41, "LOCATION")]}),

    ("William drives a Jeep Compass.",
     {"entities": [(0, 7, "NAME"), (17, 29, "VEHICLE")]}),

    ("The car involved was a Fiat 500 near Elm Street, Bath.",
     {"entities": [(23, 32, "VEHICLE"), (38, 48, "LOCATION"), (50, 54, "LOCATION")]}),

    ("Ring 07333 444555 regarding the Subaru Forester.",
     {"entities": [(5, 18, "TELECOM"), (36, 53, "VEHICLE")]}),

    ("The Lexus RX was located in Nottingham.",
     {"entities": [(4, 13, "VEHICLE"), (28, 38, "LOCATION")]}),

    ("Charlotte owns a Dacia Duster.",
     {"entities": [(0, 9, "NAME"), (19, 32, "VEHICLE")]}),

    ("A Suzuki Swift was linked to 07444 555666.",
     {"entities": [(2, 15, "VEHICLE"), (33, 46, "TELECOM")]}),

    ("The Alfa Romeo Giulietta was parked near York.",
     {"entities": [(4, 26, "VEHICLE"), (44, 48, "LOCATION")]}),

    ("Henry drives a Mitsubishi Outlander.",
     {"entities": [(0, 5, "NAME"), (15, 36, "VEHICLE")]}),

    ("Contact 07555 666777 for the Hyundai i30.",
     {"entities": [(8, 21, "TELECOM"), (30, 41, "VEHICLE")]}),

    ("The Nissan Juke was spotted in Sheffield.",
     {"entities": [(4, 15, "VEHICLE"), (31, 40, "LOCATION")]}),

    ("Amelia owns a Smart ForFour.",
     {"entities": [(0, 6, "NAME"), (15, 29, "VEHICLE")]}),

    ("A Kia Ceed was connected to 07666 777888.",
     {"entities": [(2, 10, "VEHICLE"), (32, 45, "TELECOM")]}),

    ("The vehicle was a Porsche Macan near High Road, Leeds.",
     {"entities": [(18, 31, "VEHICLE"), (37, 46, "LOCATION"), (48, 53, "LOCATION")]}),

    ("Noah drives a Land Rover Discovery.",
     {"entities": [(0, 4, "NAME"), (14, 35, "VEHICLE")]}),

    ("Call 07888 999000 about the Peugeot 3008.",
     {"entities": [(5, 18, "TELECOM"), (33, 45, "VEHICLE")]}),

    ("The car was a Honda CRV seen in Derby.",
     {"entities": [(12, 21, "VEHICLE"), (30, 35, "LOCATION")]}),

    ("Ella owns a Toyota Aygo.",
     {"entities": [(0, 4, "NAME"), (14, 26, "VEHICLE")]}),

    ("The Renault Megane was tied to 07111 222333.",
     {"entities": [(4, 19, "VEHICLE"), (34, 47, "TELECOM")]}),

    ("A Mazda 6 was parked near Queen Street, Cardiff.",
     {"entities": [(2, 10, "VEHICLE"), (28, 41, "LOCATION"), (43, 50, "LOCATION")]}),

    ("Lucas drives a Ford Puma.",
     {"entities": [(0, 5, "NAME"), (15, 24, "VEHICLE")]}),

    ("Ring 07900 111222 if you see the Vauxhall Mokka.",
     {"entities": [(5, 18, "TELECOM"), (37, 52, "VEHICLE")]}),

    ("The Cupra Formentor was sighted in Milton Keynes.",
     {"entities": [(4, 19, "VEHICLE"), (34, 47, "LOCATION")]}),

    ("Grace owns a BMW X1.",
     {"entities": [(0, 5, "NAME"), (15, 21, "VEHICLE")]}),

    ("A Ford Mondeo was registered to 07012 345678.",
     {"entities": [(2, 13, "VEHICLE"), (34, 47, "TELECOM")]}),

    ("The Suzuki Vitara was seen near Church Lane, Durham.",
     {"entities": [(4, 18, "VEHICLE"), (32, 44, "LOCATION"), (46, 52, "LOCATION")]}),

    ("Leo drives a Toyota Hilux.",
     {"entities": [(0, 3, "NAME"), (13, 26, "VEHICLE")]}),

    ("Emma White phone is 07890 123456.", {
    "entities": [(0, 10, "NAME"), (19, 32, "TELECOM")]
}),

("James Carter drives a Ford Focus reg no. AB12 CDE.", {
    "entities": [(0, 12, "NAME"), (23, 33, "VEHICLE"), (43, 51, "PLATE")]
}),

("Emily Green moved to 45 Park Lane, London.", {
    "entities": [(0, 11, "NAME"), (20, 32, "LOCATION"), (34, 40, "LOCATION")]
}),

("Joshua King bought a Honda Accord.", {
    "entities": [(0, 11, "NAME"), (21, 34, "VEHICLE")]
}),

("Daniel Cooper can be reached on 07123 456789.", {
    "entities": [(0, 13, "NAME"), (31, 44, "TELECOM")]
}),

("Chloe Adams lives at 5 Rose Lane, Bath.", {
    "entities": [(0, 11, "NAME"), (20, 31, "LOCATION"), (33, 37, "LOCATION")]
}),

("Adam Wilson drives a Ford Fiesta.", {
    "entities": [(0, 11, "NAME"), (20, 31, "VEHICLE")]
}),

("Ryan Scott can be contacted at 07122 334455.", {
    "entities": [(0, 10, "NAME"), (33, 46, "TELECOM")]
}),

("Oliver Grant has a Mercedes C Class reg no. VW34 XYZ.", {
    "entities": [(0, 12, "NAME"), (20, 36, "VEHICLE"), (46, 54, "PLATE")]
}),

("Daniel Price works in Manchester.", {
    "entities": [(0, 12, "NAME"), (22, 32, "LOCATION")]
}),

("Lucy Turner uses a Hyundai Tucson plate AB90 CDE.", {
    "entities": [(0, 11, "NAME"), (20, 34, "VEHICLE"), (41, 49, "PLATE")]
}),

("Laura King uses 07999 000111.", {
    "entities": [(0, 10, "NAME"), (17, 30, "TELECOM")]
}),

("Thomas Hill moved to Oxford.", {
    "entities": [(0, 11, "NAME"), (21, 27, "LOCATION")]
}),

("Rebecca Moore owns a Toyota Yaris.", {
    "entities": [(0, 13, "NAME"), (22, 35, "VEHICLE")]
}),

("Luke Harris can be reached on 07901 234567.", {
    "entities": [(0, 11, "NAME"), (31, 44, "TELECOM")]
}),

("Michael Brown uses a Volkswagen Golf reg no. LM56 PQR.", {
    "entities": [(0, 13, "NAME"), (22, 38, "VEHICLE"), (48, 56, "PLATE")]
}),

("James Porter lives on 12 King Street, Leeds.", {
    "entities": [(0, 12, "NAME"), (22, 35, "LOCATION"), (37, 42, "LOCATION")]
}),

("Chloe Baker uses a Nissan Micra.", {
    "entities": [(0, 11, "NAME"), (20, 33, "VEHICLE")]
}),

("Paige Allen can be reached on 07777 888999.", {
    "entities": [(0, 11, "NAME"), (31, 44, "TELECOM")]
}),

("Hannah Bell moved to Sheffield.", {
    "entities": [(0, 11, "NAME"), (21, 30, "LOCATION")]
}),

("Sarah Collins bought a Honda Civic plate CD78 EFG.", {
    "entities": [(0, 13, "NAME"), (22, 34, "VEHICLE"), (41, 49, "PLATE")]
}),

("Chris Young uses 07666 777888.", {
    "entities": [(0, 11, "NAME"), (18, 31, "TELECOM")]
}),

("Oliver Scott relocated to Cambridge.", {
    "entities": [(0, 12, "NAME"), (26, 35, "LOCATION")]
}),

("Matthew Scott owns a Volkswagen Passat.", {
    "entities": [(0, 13, "NAME"), (22, 40, "VEHICLE")]
}),

("Holly Green number is 07333 444555.", {
    "entities": [(0, 11, "NAME"), (21, 34, "TELECOM")]
}),

("Matthew King works in Nottingham.", {
    "entities": [(0, 12, "NAME"), (22, 32, "LOCATION")]
}),

("Jack Foster bought a Renault Clio.", {
    "entities": [(0, 11, "NAME"), (21, 34, "VEHICLE")]
}),

("Amy Turner has phone 07233 445566.", {
    "entities": [(0, 10, "NAME"), (21, 34, "TELECOM")]
}),

("Hannah Price drives a Nissan Qashqai plate MN56 OPQ.", {
    "entities": [(0, 13, "NAME"), (23, 39, "VEHICLE"), (46, 54, "PLATE")]
}),

("Laura Wood stays near 77 Queen Street, Bristol.", {
    "entities": [(0, 10, "NAME"), (21, 36, "LOCATION"), (38, 45, "LOCATION")]
}),

("Ella Richardson owns a Peugeot 208.", {
    "entities": [(0, 14, "NAME"), (23, 34, "VEHICLE")]
}),

("Sam Walker phone number is 07888 999000.", {
    "entities": [(0, 10, "NAME"), (28, 41, "TELECOM")]
}),

("Thomas Reed owns a Kia Sportage reg no. EF78 GHI.", {
    "entities": [(0, 11, "NAME"), (20, 32, "VEHICLE"), (42, 50, "PLATE")]
}),

("Emily Watson owns a Toyota Corolla plate XY34 ZTR.", {
    "entities": [(0, 13, "NAME"), (22, 36, "VEHICLE"), (43, 51, "PLATE")]
}),

("Rachel Evans phone number is 07234 567890.", {
    "entities": [(0, 13, "NAME"), (30, 43, "TELECOM")]
}),

("Megan Howard drives a Skoda Octavia.", {
    "entities": [(0, 12, "NAME"), (21, 35, "VEHICLE")]
}),

("Daniel Hughes drives a BMW 3 Series reg no. JK90 HLM.", {
    "entities": [(0, 13, "NAME"), (23, 35, "VEHICLE"), (45, 53, "PLATE")]
}),

("Tom Wright can be contacted on 07444 555666.", {
    "entities": [(0, 9, "NAME"), (33, 46, "TELECOM")]
}),

("Laura Bennett owns a Audi A3 plate QR12 STU.", {
    "entities": [(0, 13, "NAME"), (22, 29, "VEHICLE"), (36, 44, "PLATE")]
}),

("Hannah Bell moved to Sheffield.", {
    "entities": [(0, 11, "NAME"), (21, 30, "LOCATION")]
}),

("Call 07123 456789 about the Ford Focus reg no. AB12 CDE.", {
    "entities": [(5, 18, "TELECOM"), (33, 43, "VEHICLE"), (53, 61, "PLATE")]
}),

("The number 07234 567890 is linked to Oxford.", {
    "entities": [(11, 24, "TELECOM"), (38, 44, "LOCATION")]
}),

("Reach James Carter on 07345 678901.", {
    "entities": [(6, 18, "NAME"), (22, 35, "TELECOM")]
}),

("Contact 07456 789012 regarding the Toyota Corolla.", {
    "entities": [(8, 21, "TELECOM"), (36, 50, "VEHICLE")]
}),

("Use 07567 890123 when visiting 12 King Street, Leeds.", {
    "entities": [(4, 17, "TELECOM"), (33, 46, "LOCATION"), (48, 53, "LOCATION")]
}),

("Emma White can be reached on 07678 901234.", {
    "entities": [(0, 10, "NAME"), (29, 42, "TELECOM")]
}),

("The Nissan Micra is associated with 07789 012345.", {
    "entities": [(4, 17, "VEHICLE"), (37, 50, "TELECOM")]
}),

("Phone 07890 123456 for information about Cambridge.", {
    "entities": [(6, 19, "TELECOM"), (41, 50, "LOCATION")]
}),

("Contact 07901 234567 about the BMW 3 Series reg no. JK90 HLM.", {
    "entities": [(8, 21, "TELECOM"), (36, 48, "VEHICLE"), (58, 66, "PLATE")]
}),

("Daniel Hughes is available on 07111 222333.", {
    "entities": [(0, 13, "NAME"), (29, 42, "TELECOM")]
}),

("The number 07222 333444 relates to Manchester.", {
    "entities": [(11, 24, "TELECOM"), (36, 46, "LOCATION")]
}),

("Call 07333 444555 about the Honda Civic.", {
    "entities": [(5, 18, "TELECOM"), (33, 45, "VEHICLE")]
}),

("Sarah Collins can be contacted via 07444 555666.", {
    "entities": [(0, 13, "NAME"), (35, 48, "TELECOM")]
}),

("Use 07555 666777 for directions to York.", {
    "entities": [(4, 17, "TELECOM"), (36, 40, "LOCATION")]
}),

("The Audi A3 plate QR12 STU is linked to 07666 777888.", {
    "entities": [(4, 11, "VEHICLE"), (18, 26, "PLATE"), (42, 55, "TELECOM")]
}),

("Call 07777 888999 when arriving at Bristol.", {
    "entities": [(5, 18, "TELECOM"), (37, 44, "LOCATION")]
}),

("Michael Brown uses the number 07888 999000.", {
    "entities": [(0, 13, "NAME"), (29, 42, "TELECOM")]
}),

("Reach 07999 000111 about the Volkswagen Passat.", {
    "entities": [(6, 19, "TELECOM"), (34, 52, "VEHICLE")]
}),

("The phone 07122 334455 connects to 45 Park Lane, London.", {
    "entities": [(10, 23, "TELECOM"), (37, 49, "LOCATION"), (51, 57, "LOCATION")]
}),

("Laura Bennett can be called on 07233 445566.", {
    "entities": [(0, 13, "NAME"), (32, 45, "TELECOM")]
}),

("Use 07344 556677 regarding the Kia Sportage.", {
    "entities": [(4, 17, "TELECOM"), (33, 45, "VEHICLE")]
}),

("The Hyundai Tucson reg no. MN56 OPQ uses 07455 667788.", {
    "entities": [(4, 18, "VEHICLE"), (28, 36, "PLATE"), (42, 55, "TELECOM")]
}),

("Contact 07566 778899 when near Nottingham.", {
    "entities": [(8, 21, "TELECOM"), (37, 47, "LOCATION")]
}),

("James Porter is reachable on 07677 889900.", {
    "entities": [(0, 12, "NAME"), (29, 42, "TELECOM")]
}),

("Call 07788 990011 about the Renault Clio.", {
    "entities": [(5, 18, "TELECOM"), (33, 46, "VEHICLE")]
}),

("The number 07899 001122 applies to Sheffield.", {
    "entities": [(11, 24, "TELECOM"), (38, 47, "LOCATION")]
}),

("Emma Green uses 07910 112233.", {
    "entities": [(0, 10, "NAME"), (16, 29, "TELECOM")]
}),

("Reach 07121 223344 for the Peugeot 208.", {
    "entities": [(6, 19, "TELECOM"), (33, 44, "VEHICLE")]
}),

("The Mercedes C Class reg no. VW34 XYZ is on 07232 334455.", {
    "entities": [(4, 20, "VEHICLE"), (30, 38, "PLATE"), (44, 57, "TELECOM")]
}),

("Contact 07343 445566 before arriving in Leeds.", {
    "entities": [(8, 21, "TELECOM"), (42, 47, "LOCATION")]
}),

("Rachel Evans can be reached on 07454 556677.", {
    "entities": [(0, 13, "NAME"), (31, 44, "TELECOM")]
}),

("Use 07565 667788 regarding the Skoda Octavia.", {
    "entities": [(4, 17, "TELECOM"), (33, 47, "VEHICLE")]
}),

("The Ford Fiesta reg no. CD78 EFG connects to 07676 778899.", {
    "entities": [(4, 15, "VEHICLE"), (25, 33, "PLATE"), (46, 59, "TELECOM")]
}),

("Call 07787 889900 for directions to Bath.", {
    "entities": [(5, 18, "TELECOM"), (37, 41, "LOCATION")]
}),

("Oliver Grant is available via 07898 990011.", {
    "entities": [(0, 12, "NAME"), (32, 45, "TELECOM")]
}),

("Reach 07909 001122 about the Nissan Qashqai.", {
    "entities": [(6, 19, "TELECOM"), (34, 50, "VEHICLE")]
}),

("The phone 07110 112233 relates to Liverpool.", {
    "entities": [(10, 23, "TELECOM"), (36, 45, "LOCATION")]
}),

("Sophie Adams can be contacted on 07221 223344.", {
    "entities": [(0, 12, "NAME"), (33, 46, "TELECOM")]
}),

("Use 07332 334455 for the Hyundai i30.", {
    "entities": [(4, 17, "TELECOM"), (26, 37, "VEHICLE")]
}),

("The Toyota Yaris reg no. EF78 GHI uses 07443 445566.", {
    "entities": [(4, 17, "VEHICLE"), (27, 35, "PLATE"), (42, 55, "TELECOM")]
}),

("Call 07554 556677 before visiting York.", {
    "entities": [(5, 18, "TELECOM"), (38, 42, "LOCATION")]
}),

("Matthew Scott can be reached via 07665 667788.", {
    "entities": [(0, 13, "NAME"), (32, 45, "TELECOM")]
}),

("Reach 07776 778899 regarding the Honda Accord.", {
    "entities": [(6, 19, "TELECOM"), (34, 47, "VEHICLE")]
}),

("The number 07887 889900 is tied to Coventry.", {
    "entities": [(11, 24, "TELECOM"), (38, 46, "LOCATION")]
}),

("Laura King uses 07998 990011.", {
    "entities": [(0, 10, "NAME"), (16, 29, "TELECOM")]
}),

("Use 07109 001122 about the Kia Ceed.", {
    "entities": [(4, 17, "TELECOM"), (32, 40, "VEHICLE")]
}),

("The Volkswagen Golf reg no. LM56 PQR connects to 07220 112233.", {
    "entities": [(4, 20, "VEHICLE"), (30, 38, "PLATE"), (50, 63, "TELECOM")]
}),

("Call 07331 223344 when near Exeter.", {
    "entities": [(5, 18, "TELECOM"), (33, 39, "LOCATION")]
}),

("Hannah Price is reachable on 07442 334455.", {
    "entities": [(0, 13, "NAME"), (31, 44, "TELECOM")]
}),

("James Carter visited Oxford.", {
    "entities": [(0, 12, "NAME"), (21, 27, "LOCATION")]
}),

("The Ford Focus reg no. AB12 CDE was seen on Baker Street, London.", {
    "entities": [(4, 14, "VEHICLE"), (24, 32, "PLATE"), (45, 57, "LOCATION"), (59, 65, "LOCATION")]
}),

("Call 07123 456789 when arriving in Leeds.", {
    "entities": [(5, 18, "TELECOM"), (36, 41, "LOCATION")]
}),

("Emily Green now lives in Manchester.", {
    "entities": [(0, 11, "NAME"), (25, 35, "LOCATION")]
}),

("A Toyota Corolla is parked on King Street, York.", {
    "entities": [(2, 16, "VEHICLE"), (31, 42, "LOCATION"), (44, 48, "LOCATION")]
}),

("Meet at 45 Park Lane, London.", {
    "entities": [(8, 20, "LOCATION"), (22, 28, "LOCATION")]
}),

("Daniel Hughes can be reached at Bristol.", {
    "entities": [(0, 13, "NAME"), (34, 41, "LOCATION")]
}),

("The BMW 3 Series reg no. JK90 HLM was spotted in Sheffield.", {
    "entities": [(4, 16, "VEHICLE"), (26, 34, "PLATE"), (52, 61, "LOCATION")]
}),

("Contact 07234 567890 near Cambridge.", {
    "entities": [(8, 21, "TELECOM"), (27, 36, "LOCATION")]
}),

("Sarah Collins moved to Bath.", {
    "entities": [(0, 13, "NAME"), (23, 27, "LOCATION")]
}),

("A Nissan Micra is located on Queen Road, Nottingham.", {
    "entities": [(2, 15, "VEHICLE"), (30, 40, "LOCATION"), (42, 52, "LOCATION")]
}),

("Use 07345 678901 when in York.", {
    "entities": [(4, 17, "TELECOM"), (26, 30, "LOCATION")]
}),

("Michael Brown relocated to Coventry.", {
    "entities": [(0, 13, "NAME"), (27, 35, "LOCATION")]
}),

("The Honda Civic plate CD78 EFG was seen in Leeds.", {
    "entities": [(4, 16, "VEHICLE"), (23, 31, "PLATE"), (44, 49, "LOCATION")]
}),

("Meet near 12 King Street, Leeds.", {
    "entities": [(10, 23, "LOCATION"), (25, 30, "LOCATION")]
}),

("Reach 07456 789012 while visiting Oxford.", {
    "entities": [(6, 19, "TELECOM"), (37, 43, "LOCATION")]
}),

("Laura Bennett is staying in Liverpool.", {
    "entities": [(0, 13, "NAME"), (28, 37, "LOCATION")]
}),

("The Audi A3 reg no. QR12 STU appeared on Park Lane, London.", {
    "entities": [(4, 11, "VEHICLE"), (21, 29, "PLATE"), (43, 52, "LOCATION"), (54, 60, "LOCATION")]
}),

("Call 07567 890123 in Nottingham.", {
    "entities": [(5, 18, "TELECOM"), (22, 32, "LOCATION")]
}),

("Oliver Grant moved to Exeter.", {
    "entities": [(0, 12, "NAME"), (22, 28, "LOCATION")]
}),

("A Volkswagen Passat is parked in Bristol.", {
    "entities": [(2, 20, "VEHICLE"), (34, 41, "LOCATION")]
}),

("The number 07678 901234 works in Leicester.", {
    "entities": [(11, 24, "TELECOM"), (35, 43, "LOCATION")]
}),

("Chloe Adams now lives on Rose Lane, Bath.", {
    "entities": [(0, 11, "NAME"), (28, 37, "LOCATION"), (39, 43, "LOCATION")]
}),

("The Kia Sportage reg no. EF78 GHI was seen in York.", {
    "entities": [(4, 16, "VEHICLE"), (26, 34, "PLATE"), (47, 51, "LOCATION")]
}),

("Arrive at 77 Queen Street, Bristol.", {
    "entities": [(10, 26, "LOCATION"), (28, 35, "LOCATION")]
}),

("Phone 07789 012345 while in Derby.", {
    "entities": [(6, 19, "TELECOM"), (31, 36, "LOCATION")]
}),

("Thomas Reed relocated to Cambridge.", {
    "entities": [(0, 11, "NAME"), (25, 34, "LOCATION")]
}),

("The Renault Clio is parked near Church Road, York.", {
    "entities": [(4, 17, "VEHICLE"), (35, 46, "LOCATION"), (48, 52, "LOCATION")]
}),

("Use 07890 123456 when visiting Hull.", {
    "entities": [(4, 17, "TELECOM"), (37, 41, "LOCATION")]
}),

("Emma White moved to Reading.", {
    "entities": [(0, 10, "NAME"), (20, 27, "LOCATION")]
}),

("The Mercedes C Class reg no. VW34 XYZ appeared in London.", {
    "entities": [(4, 20, "VEHICLE"), (30, 38, "PLATE"), (52, 58, "LOCATION")]
}),

("Call 07901 234567 in Swindon.", {
    "entities": [(5, 18, "TELECOM"), (22, 29, "LOCATION")]
}),

("Ryan Scott now lives in Durham.", {
    "entities": [(0, 10, "NAME"), (25, 31, "LOCATION")]
}),

("A Peugeot 208 was seen on Station Road, Cambridge.", {
    "entities": [(2, 13, "VEHICLE"), (29, 42, "LOCATION"), (44, 53, "LOCATION")]
}),

("Contact 07111 222333 while in Lincoln.", {
    "entities": [(8, 21, "TELECOM"), (35, 41, "LOCATION")]
}),

("Hannah Price moved to Chester.", {
    "entities": [(0, 13, "NAME"), (23, 30, "LOCATION")]
}),

("The Hyundai Tucson is located in Plymouth.", {
    "entities": [(4, 18, "VEHICLE"), (33, 41, "LOCATION")]
}),

("Use 07222 333444 when visiting Carlisle.", {
    "entities": [(4, 17, "TELECOM"), (37, 45, "LOCATION")]
}),

("Matthew King is staying in Preston.", {
    "entities": [(0, 12, "NAME"), (27, 34, "LOCATION")]
}),

("A Skoda Octavia reg no. MN56 OPQ appeared in Oxford.", {
    "entities": [(2, 16, "VEHICLE"), (26, 34, "PLATE"), (48, 54, "LOCATION")]
}),

("Reach 07333 444555 when in Doncaster.", {
    "entities": [(6, 19, "TELECOM"), (31, 41, "LOCATION")]
}),

("Lucy Turner relocated to Shrewsbury.", {
    "entities": [(0, 11, "NAME"), (25, 35, "LOCATION")]
}),

("The Toyota Yaris was seen on Elm Street, York.", {
    "entities": [(4, 17, "VEHICLE"), (30, 40, "LOCATION"), (42, 46, "LOCATION")]
}),

("Phone 07444 555666 while in Salisbury.", {
    "entities": [(6, 19, "TELECOM"), (31, 40, "LOCATION")]
}),

("Jack Foster moved to Worcester.", {
    "entities": [(0, 11, "NAME"), (21, 29, "LOCATION")]
}),

("A Kia Ceed is parked in Sunderland.", {
    "entities": [(2, 10, "VEHICLE"), (24, 33, "LOCATION")]
}),

("Call 07555 666777 when arriving in Taunton.", {
    "entities": [(5, 18, "TELECOM"), (37, 44, "LOCATION")]
}),

("Megan Howard relocated to Gloucester.", {
    "entities": [(0, 12, "NAME"), (26, 35, "LOCATION")]
}),

("The Volkswagen Golf reg no. LM56 PQR was seen in Reading.", {
    "entities": [(4, 20, "VEHICLE"), (30, 38, "PLATE"), (51, 58, "LOCATION")]
}),

("James Carter drives a Ford Focus and can be reached on 07123 456789.", {
    "entities": [(0,12,"NAME"), (23,33,"VEHICLE"), (54,67,"TELECOM")]
}),

("Emily Green owns a Toyota Corolla reg no. AB12 CDE and lives in Leeds.", {
    "entities": [(0,11,"NAME"), (20,34,"VEHICLE"), (44,52,"PLATE"), (66,71,"LOCATION")]
}),

("The BMW 3 Series reg no. JK90 HLM was spotted on Baker Street, London with 07234 567890.", {
    "entities": [(4,16,"VEHICLE"), (26,34,"PLATE"), (48,60,"LOCATION"), (62,68,"LOCATION"), (74,87,"TELECOM")]
}),

("Sarah Collins lives at 12 King Street, York and uses 07345 678901.", {
    "entities": [(0,13,"NAME"), (23,36,"LOCATION"), (38,42,"LOCATION"), (52,65,"TELECOM")]
}),

("Daniel Hughes owns a Honda Civic and can be contacted on 07456 789012.", {
    "entities": [(0,13,"NAME"), (22,34,"VEHICLE"), (57,70,"TELECOM")]
}),

("A Nissan Qashqai reg no. MN56 OPQ was seen in Oxford with 07567 890123.", {
    "entities": [(2,18,"VEHICLE"), (28,36,"PLATE"), (49,55,"LOCATION"), (61,74,"TELECOM")]
}),

("Michael Brown drives a Volkswagen Golf and lives in Manchester.", {
    "entities": [(0,13,"NAME"), (23,39,"VEHICLE"), (53,63,"LOCATION")]
}),

("Laura Bennett owns a Audi A3 reg no. QR12 STU and uses 07678 901234.", {
    "entities": [(0,13,"NAME"), (22,29,"VEHICLE"), (39,47,"PLATE"), (59,72,"TELECOM")]
}),

("The Ford Fiesta was parked on Queen Road, Nottingham near 07789 012345.", {
    "entities": [(4,15,"VEHICLE"), (31,41,"LOCATION"), (43,53,"LOCATION"), (60,73,"TELECOM")]
}),

("Oliver Grant lives in Bristol and can be reached on 07890 123456.", {
    "entities": [(0,12,"NAME"), (22,29,"LOCATION"), (53,66,"TELECOM")]
}),

("A Mercedes C Class reg no. VW34 XYZ was seen in London with 07901 234567.", {
    "entities": [(2,18,"VEHICLE"), (28,36,"PLATE"), (49,55,"LOCATION"), (61,74,"TELECOM")]
}),

("Emma White owns a Hyundai Tucson and lives in Sheffield.", {
    "entities": [(0,10,"NAME"), (20,34,"VEHICLE"), (48,57,"LOCATION")]
}),

("The Kia Sportage reg no. EF78 GHI appeared on Park Lane, London.", {
    "entities": [(4,16,"VEHICLE"), (26,34,"PLATE"), (48,57,"LOCATION"), (59,65,"LOCATION")]
}),

("Rachel Evans can be contacted on 07111 222333 while in Reading.", {
    "entities": [(0,13,"NAME"), (31,44,"TELECOM"), (55,62,"LOCATION")]
}),

("A Peugeot 208 was parked in York and linked to 07222 333444.", {
    "entities": [(2,13,"VEHICLE"), (27,31,"LOCATION"), (46,59,"TELECOM")]
}),

("Thomas Reed drives a Renault Clio and lives in Coventry.", {
    "entities": [(0,11,"NAME"), (21,34,"VEHICLE"), (48,56,"LOCATION")]
}),

("The Toyota Yaris reg no. CD78 EFG was seen near 07333 444555 in Bath.", {
    "entities": [(4,17,"VEHICLE"), (27,35,"PLATE"), (50,63,"TELECOM"), (67,71,"LOCATION")]
}),

("Lucy Turner lives at 45 Park Lane, Leeds and uses 07444 555666.", {
    "entities": [(0,11,"NAME"), (21,33,"LOCATION"), (35,40,"LOCATION"), (51,64,"TELECOM")]
}),

("A Skoda Octavia was seen in Derby and linked to 07555 666777.", {
    "entities": [(2,16,"VEHICLE"), (30,35,"LOCATION"), (50,63,"TELECOM")]
}),

("Matthew King owns a Kia Ceed and can be reached on 07666 777888.", {
    "entities": [(0,12,"NAME"), (22,30,"VEHICLE"), (54,67,"TELECOM")]
}),

("The Volkswagen Passat reg no. LM56 PQR was parked in Exeter.", {
    "entities": [(4,22,"VEHICLE"), (32,40,"PLATE"), (55,61,"LOCATION")]
}),

("Hannah Price lives in Chester and uses 07777 888999.", {
    "entities": [(0,13,"NAME"), (23,30,"LOCATION"), (41,54,"TELECOM")]
}),

("A Hyundai i30 was spotted on Church Road, York with 07888 999000.", {
    "entities": [(2,13,"VEHICLE"), (28,40,"LOCATION"), (42,46,"LOCATION"), (52,65,"TELECOM")]
}),

("Jack Foster drives a BMW X5 and lives in Durham.", {
    "entities": [(0,11,"NAME"), (21,27,"VEHICLE"), (41,47,"LOCATION")]
}),

("The Honda Accord reg no. GH12 JKL appeared in Leeds with 07999 000111.", {
    "entities": [(4,17,"VEHICLE"), (27,35,"PLATE"), (50,55,"LOCATION"), (61,74,"TELECOM")]
}),

("Amy Turner lives in Lincoln and can be reached on 07122 334455.", {
    "entities": [(0,10,"NAME"), (20,27,"LOCATION"), (50,63,"TELECOM")]
}),

("A Nissan Micra was parked in Hull near 07233 445566.", {
    "entities": [(2,15,"VEHICLE"), (29,33,"LOCATION"), (39,52,"TELECOM")]
}),

("Daniel Cooper drives a Ford Focus reg no. ZZ99 ABC.", {
    "entities": [(0,13,"NAME"), (23,33,"VEHICLE"), (43,51,"PLATE")]
}),

("Laura King lives at 88 Victoria Street, Bath and uses 07344 556677.", {
    "entities": [(0,10,"NAME"), (20,39,"LOCATION"), (41,45,"LOCATION"), (56,69,"TELECOM")]
}),

("A Renault Captur reg no. TT11 QWE was seen in Swindon.", {
    "entities": [(2,17,"VEHICLE"), (27,35,"PLATE"), (50,57,"LOCATION")]
}),

("Chris Young drives a Skoda Fabia and can be contacted on 07455 667788.", {
    "entities": [(0,11,"NAME"), (21,33,"VEHICLE"), (58,71,"TELECOM")]
}),

("The Audi A4 was parked in Preston near 07566 778899.", {
    "entities": [(4,11,"VEHICLE"), (25,32,"LOCATION"), (38,51,"TELECOM")]
}),

("Sophie Adams lives in Taunton and uses 07677 889900.", {
    "entities": [(0,12,"NAME"), (22,29,"LOCATION"), (40,53,"TELECOM")]
}),

("A Seat Leon reg no. UU22 ASD was seen on Elm Street, York.", {
    "entities": [(2,11,"VEHICLE"), (21,29,"PLATE"), (43,53,"LOCATION"), (55,59,"LOCATION")]
}),

("Ben Clark drives a Mazda CX-5 and lives in Carlisle.", {
    "entities": [(0,9,"NAME"), (19,30,"VEHICLE"), (44,52,"LOCATION")]
}),

("The Vauxhall Astra was spotted in Grimsby near 07788 990011.", {
    "entities": [(4,20,"VEHICLE"), (34,41,"LOCATION"), (47,60,"TELECOM")]
}),

("Olivia Turner lives in Shrewsbury and uses 07899 001122.", {
    "entities": [(0,13,"NAME"), (23,33,"LOCATION"), (44,57,"TELECOM")]
}),

("A Citroen C3 reg no. YY88 ZZZ was seen in Worcester.", {
    "entities": [(2,12,"VEHICLE"), (22,30,"PLATE"), (45,53,"LOCATION")]
}),

("Ryan Scott drives a Volvo XC60 and can be reached on 07910 112233.", {
    "entities": [(0,10,"NAME"), (20,31,"VEHICLE"), (56,69,"TELECOM")]
}),

("The Mini Cooper was parked in Kendal near 07121 223344.", {
    "entities": [(4,15,"VEHICLE"), (29,35,"LOCATION"), (41,54,"TELECOM")]
}),

("Grace Miller lives in Skipton and uses 07232 334455.", {
    "entities": [(0,12,"NAME"), (22,29,"LOCATION"), (40,53,"TELECOM")]
}),

("A Jeep Compass reg no. RR77 TTY was seen in Scarborough.", {
    "entities": [(2,14,"VEHICLE"), (24,32,"PLATE"), (47,58,"LOCATION")]
}),

("Luke Harris drives a Subaru Outback and lives in Hexham.", {
    "entities": [(0,11,"NAME"), (21,35,"VEHICLE"), (49,56,"LOCATION")]
}),

("The Toyota Avensis was parked in Worksop near 07343 445566.", {
    "entities": [(4,19,"VEHICLE"), (33,40,"LOCATION"), (46,59,"TELECOM")]
}),

("Paige Allen lives in Ripon and uses 07454 556677.", {
    "entities": [(0,11,"NAME"), (21,26,"LOCATION"), (37,50,"TELECOM")]
}),

("A Ford Mondeo reg no. PP66 LLL was seen in Kendal.", {
    "entities": [(2,13,"VEHICLE"), (23,31,"PLATE"), (46,52,"LOCATION")]
}),

("Tom Wright drives a Tesla Model 3 and can be contacted on 07565 667788.", {
    "entities": [(0,9,"NAME"), (19,33,"VEHICLE"), (61,74,"TELECOM")]
}),

("The Lexus RX was spotted in Malton near 07676 778899.", {
    "entities": [(4,12,"VEHICLE"), (26,32,"LOCATION"), (38,51,"TELECOM")]
}),

("Ella Richardson lives in Penrith and uses 07787 889900.", {
    "entities": [(0,14,"NAME"), (24,32,"LOCATION"), (43,56,"TELECOM")]
}),

("A Range Rover reg no. KK55 MMM was seen in Alnwick.", {
    "entities": [(2,13,"VEHICLE"), (23,31,"PLATE"), (46,53,"LOCATION")]
}),

("Sam Walker drives a Nissan Leaf and can be reached on 07898 990011.", {
    "entities": [(0,10,"NAME"), (20,31,"VEHICLE"), (56,69,"TELECOM")]
}),

("The Dacia Duster was parked in Morpeth near 07909 001122.", {
    "entities": [(4,16,"VEHICLE"), (30,37,"LOCATION"), (43,56,"TELECOM")]
}),

("Megan Howard lives in Whitby and uses 07109 001122.", {
    "entities": [(0,12,"NAME"), (22,28,"LOCATION"), (39,52,"TELECOM")]
}),

("A Peugeot 3008 reg no. NN44 QQQ was seen in Thirsk.", {
    "entities": [(2,15,"VEHICLE"), (25,33,"PLATE"), (48,54,"LOCATION")]
}),

("James Carter drives a Ford Focus reg no. AB12 CDE and lives on King Street, Leeds. Call 07123 456789.", {
    "entities": [(0,12,"NAME"), (23,33,"VEHICLE"), (43,51,"PLATE"), (66,77,"LOCATION"), (79,84,"LOCATION"), (91,104,"TELECOM")]
}),

("Emily Green owns a Toyota Corolla and lives at Park Lane, London. Contact 07234 567890.", {
    "entities": [(0,11,"NAME"), (20,34,"VEHICLE"), (49,58,"LOCATION"), (60,66,"LOCATION"), (76,89,"TELECOM")]
}),

("Daniel Hughes drives a BMW 3 Series reg no. JK90 HLM near Queen Road, York. Phone 07345 678901.", {
    "entities": [(0,13,"NAME"), (23,35,"VEHICLE"), (45,53,"PLATE"), (64,74,"LOCATION"), (76,80,"LOCATION"), (88,101,"TELECOM")]
}),

("Sarah Collins owns a Honda Civic and lives on Church Street, Bath. Call 07456 789012.", {
    "entities": [(0,13,"NAME"), (22,34,"VEHICLE"), (49,62,"LOCATION"), (64,68,"LOCATION"), (76,89,"TELECOM")]
}),

("Michael Brown drives a Volkswagen Golf reg no. CD78 EFG at Station Road, Cambridge. Reach 07567 890123.", {
    "entities": [(0,13,"NAME"), (23,39,"VEHICLE"), (49,57,"PLATE"), (61,74,"LOCATION"), (76,85,"LOCATION"), (93,106,"TELECOM")]
}),

("Laura Bennett owns a Audi A3 and lives on Rose Lane, York. Phone 07678 901234.", {
    "entities": [(0,13,"NAME"), (22,29,"VEHICLE"), (44,53,"LOCATION"), (55,59,"LOCATION"), (67,80,"TELECOM")]
}),

("Thomas Reed drives a Nissan Qashqai reg no. MN56 OPQ in Market Street, Chester. Call 07789 012345.", {
    "entities": [(0,11,"NAME"), (21,37,"VEHICLE"), (47,55,"PLATE"), (59,72,"LOCATION"), (74,81,"LOCATION"), (89,102,"TELECOM")]
}),

("Emma White owns a Hyundai Tucson and lives on Victoria Road, Derby. Contact 07890 123456.", {
    "entities": [(0,10,"NAME"), (20,34,"VEHICLE"), (49,63,"LOCATION"), (65,70,"LOCATION"), (80,93,"TELECOM")]
}),

("Oliver Grant drives a Kia Sportage reg no. EF78 GHI at High Street, Oxford. Phone 07901 234567.", {
    "entities": [(0,12,"NAME"), (22,34,"VEHICLE"), (44,52,"PLATE"), (56,67,"LOCATION"), (69,75,"LOCATION"), (83,96,"TELECOM")]
}),

("Chloe Adams owns a Peugeot 208 and lives on Mill Road, Cambridge. Call 07111 222333.", {
    "entities": [(0,11,"NAME"), (21,32,"VEHICLE"), (47,56,"LOCATION"), (58,67,"LOCATION"), (75,88,"TELECOM")]
}),

("Matthew King drives a Skoda Octavia reg no. QR12 STU at Elm Street, York. Phone 07222 333444.", {
    "entities": [(0,12,"NAME"), (22,36,"VEHICLE"), (46,54,"PLATE"), (58,68,"LOCATION"), (70,74,"LOCATION"), (82,95,"TELECOM")]
}),

("Lucy Turner owns a Renault Clio and lives on Queen Street, Leeds. Contact 07333 444555.", {
    "entities": [(0,11,"NAME"), (21,34,"VEHICLE"), (49,62,"LOCATION"), (64,69,"LOCATION"), (79,92,"TELECOM")]
}),

("Jack Foster drives a Ford Fiesta reg no. VW34 XYZ at Park Road, Nottingham. Call 07444 555666.", {
    "entities": [(0,11,"NAME"), (21,32,"VEHICLE"), (42,50,"PLATE"), (54,63,"LOCATION"), (65,75,"LOCATION"), (83,96,"TELECOM")]
}),

("Hannah Price owns a Seat Leon and lives on Bridge Street, Lincoln. Phone 07555 666777.", {
    "entities": [(0,13,"NAME"), (22,31,"VEHICLE"), (46,59,"LOCATION"), (61,68,"LOCATION"), (76,89,"TELECOM")]
}),

("Ryan Scott drives a Mazda CX-5 reg no. ZZ99 ABC at Station Lane, Hull. Contact 07666 777888.", {
    "entities": [(0,10,"NAME"), (20,31,"VEHICLE"), (41,49,"PLATE"), (53,66,"LOCATION"), (68,72,"LOCATION"), (82,95,"TELECOM")]
}),

("Megan Howard owns a Toyota Yaris and lives on North Road, Preston. Call 07777 888999.", {
    "entities": [(0,12,"NAME"), (22,35,"VEHICLE"), (50,60,"LOCATION"), (62,69,"LOCATION"), (77,90,"TELECOM")]
}),

("Luke Harris drives a Volvo XC60 reg no. TT11 QWE at South Street, Durham. Phone 07888 999000.", {
    "entities": [(0,11,"NAME"), (21,32,"VEHICLE"), (42,50,"PLATE"), (54,66,"LOCATION"), (68,74,"LOCATION"), (82,95,"TELECOM")]
}),

("Paige Allen owns a Mini Cooper and lives on West Lane, Ripon. Contact 07999 000111.", {
    "entities": [(0,11,"NAME"), (21,32,"VEHICLE"), (47,56,"LOCATION"), (58,63,"LOCATION"), (73,86,"TELECOM")]
}),

("Ben Clark drives a Range Rover reg no. KK55 MMM at Meadow Road, Kendal. Call 07121 223344.", {
    "entities": [(0,9,"NAME"), (19,30,"VEHICLE"), (40,48,"PLATE"), (52,64,"LOCATION"), (66,72,"LOCATION"), (80,93,"TELECOM")]
}),

("Sophie Adams owns a Citroen C3 and lives on Hill Street, Whitby. Phone 07232 334455.", {
    "entities": [(0,12,"NAME"), (22,32,"VEHICLE"), (47,58,"LOCATION"), (60,66,"LOCATION"), (74,87,"TELECOM")]
}),

("James Carter met Emily Green yesterday.", {
    "entities": [(0,12,"NAME"), (17,28,"NAME")]
}),

("Daniel Hughes spoke with Sarah Collins.", {
    "entities": [(0,13,"NAME"), (25,38,"NAME")]
}),

("Michael Brown emailed Laura Bennett.", {
    "entities": [(0,13,"NAME"), (22,35,"NAME")]
}),

("Thomas Reed and Emma White attended.", {
    "entities": [(0,11,"NAME"), (16,26,"NAME")]
}),

("Oliver Grant called Chloe Adams.", {
    "entities": [(0,12,"NAME"), (20,31,"NAME")]
}),

("Matthew King met Lucy Turner.", {
    "entities": [(0,12,"NAME"), (17,28,"NAME")]
}),

("Jack Foster helped Hannah Price.", {
    "entities": [(0,11,"NAME"), (19,32,"NAME")]
}),

("Ryan Scott thanked Megan Howard.", {
    "entities": [(0,10,"NAME"), (19,31,"NAME")]
}),

("Luke Harris greeted Paige Allen.", {
    "entities": [(0,11,"NAME"), (20,31,"NAME")]
}),

("Ben Clark spoke to Sophie Adams.", {
    "entities": [(0,9,"NAME"), (19,31,"NAME")]
}),

# ---- 2 VEHICLES (10) ----
("A Ford Focus and Toyota Corolla were parked.", {
    "entities": [(2,12,"VEHICLE"), (17,31,"VEHICLE")]
}),

("The BMW 3 Series followed a Audi A3.", {
    "entities": [(4,16,"VEHICLE"), (28,35,"VEHICLE")]
}),

("A Honda Civic passed a Nissan Micra.", {
    "entities": [(2,14,"VEHICLE"), (23,36,"VEHICLE")]
}),

("The Volkswagen Golf overtook a Ford Fiesta.", {
    "entities": [(4,20,"VEHICLE"), (32,43,"VEHICLE")]
}),

("A Hyundai Tucson met a Kia Sportage.", {
    "entities": [(2,16,"VEHICLE"), (25,37,"VEHICLE")]
}),

("The Peugeot 208 hit a Renault Clio.", {
    "entities": [(4,15,"VEHICLE"), (24,37,"VEHICLE")]
}),

("A Skoda Octavia passed a Seat Leon.", {
    "entities": [(2,16,"VEHICLE"), (25,34,"VEHICLE")]
}),

("The Mazda CX-5 followed a Volvo XC60.", {
    "entities": [(4,15,"VEHICLE"), (26,37,"VEHICLE")]
}),

("A Mini Cooper blocked a Range Rover.", {
    "entities": [(2,13,"VEHICLE"), (23,35,"VEHICLE")]
}),

("The Citroen C3 passed a Toyota Yaris.", {
    "entities": [(4,14,"VEHICLE"), (23,36,"VEHICLE")]
}),

# ---- 2 TELECOMS (10) ----
("Call 07123 456789 or 07234 567890 for help.", {
    "entities": [(5,18,"TELECOM"), (22,35,"TELECOM")]
}),

("Use 07345 678901 or 07456 789012.", {
    "entities": [(4,17,"TELECOM"), (21,34,"TELECOM")]
}),

("Numbers 07567 890123 and 07678 901234 are active.", {
    "entities": [(8,21,"TELECOM"), (26,39,"TELECOM")]
}),

("Contact 07789 012345 or 07890 123456 today.", {
    "entities": [(8,21,"TELECOM"), (25,38,"TELECOM")]
}),

("Reach 07901 234567 or 07111 222333.", {
    "entities": [(6,19,"TELECOM"), (23,36,"TELECOM")]
}),

("Either 07222 333444 or 07333 444555 will work.", {
    "entities": [(7,20,"TELECOM"), (24,37,"TELECOM")]
}),

("Call 07444 555666 or 07555 666777.", {
    "entities": [(5,18,"TELECOM"), (22,35,"TELECOM")]
}),

("Use 07666 777888 or 07777 888999.", {
    "entities": [(4,17,"TELECOM"), (21,34,"TELECOM")]
}),

("Try 07888 999000 or 07999 000111.", {
    "entities": [(4,17,"TELECOM"), (21,34,"TELECOM")]
}),

("Numbers 07121 223344 and 07232 334455 are listed.", {
    "entities": [(8,21,"TELECOM"), (26,39,"TELECOM")]
}),

# ---- 2 LOCATIONS (10) ----
("Meet at King Street, Leeds tomorrow.", {
    "entities": [(8,19,"LOCATION"), (21,26,"LOCATION")]
}),

("The office is on Park Lane, London.", {
    "entities": [(17,26,"LOCATION"), (28,34,"LOCATION")]
}),

("He lives near Queen Road, York.", {
    "entities": [(13,23,"LOCATION"), (25,29,"LOCATION")]
}),

("Deliver to Church Street, Bath.", {
    "entities": [(11,24,"LOCATION"), (26,30,"LOCATION")]
}),

("She moved to Station Road, Cambridge.", {
    "entities": [(13,26,"LOCATION"), (28,37,"LOCATION")]
}),

("They met on High Street, Oxford.", {
    "entities": [(11,22,"LOCATION"), (24,30,"LOCATION")]
}),

("The shop is at Mill Road, Derby.", {
    "entities": [(15,24,"LOCATION"), (26,31,"LOCATION")]
}),

("Wait outside Bridge Street, Lincoln.", {
    "entities": [(13,26,"LOCATION"), (28,35,"LOCATION")]
}),

("The event is on Victoria Road, Preston.", {
    "entities": [(15,29,"LOCATION"), (31,38,"LOCATION")]
}),

("Send it to North Road, Ripon.", {
    "entities": [(11,21,"LOCATION"), (23,28,"LOCATION")]
}),

(
"James Carter met Emily Green and Daniel Hughes while Michael Brown spoke to Laura Bennett as Thomas Reed greeted Emma White alongside Oliver Grant, Chloe Adams, and Jack Foster.",
{
    "entities": [
        (0,12,"NAME"),    # James Carter
        (17,28,"NAME"),   # Emily Green
        (33,46,"NAME"),   # Daniel Hughes
        (53,66,"NAME"),   # Michael Brown
        (76,89,"NAME"),   # Laura Bennett
        (93,104,"NAME"),  # Thomas Reed
        (114,124,"NAME"), # Emma White
        (134,146,"NAME"), # Oliver Grant
        (148,159,"NAME"), # Chloe Adams
        (165,175,"NAME"), # Jack Foster
    ]
}
),

# ---- 10 LOCATIONS ----
(
"King Street, Leeds Park Lane, London Queen Road, York Church Street, Bath Station Road, Cambridge High Street, Oxford Mill Road, Derby Bridge Street, Lincoln Victoria Road, Preston North Road, Ripon",
{
    "entities": [
        (0,11,"LOCATION"),    # King Street
        (13,18,"LOCATION"),   # Leeds
        (19,28,"LOCATION"),   # Park Lane
        (30,36,"LOCATION"),   # London
        (37,48,"LOCATION"),   # Queen Road
        (50,54,"LOCATION"),   # York
        (55,67,"LOCATION"),   # Church Street
        (69,73,"LOCATION"),   # Bath
        (74,87,"LOCATION"),   # Station Road
        (89,97,"LOCATION"),   # Cambridge
        (98,110,"LOCATION"),  # High Street
        (112,118,"LOCATION"), # Oxford
        (119,128,"LOCATION"), # Mill Road
        (130,134,"LOCATION"), # Derby
        (135,147,"LOCATION"), # Bridge Street
        (149,155,"LOCATION"), # Lincoln
        (156,169,"LOCATION"), # Victoria Road
        (171,178,"LOCATION"), # Preston
        (179,189,"LOCATION"), # North Road
        (191,196,"LOCATION"), # Ripon
    ]
}
),

# ---- 10 VEHICLES ----
(
"Ford Focus Toyota Corolla BMW 3 Series Audi A3 Honda Civic Nissan Micra Volkswagen Golf Hyundai Tucson Kia Sportage Peugeot 208",
{
    "entities": [
        (0,10,"VEHICLE"),     # Ford Focus
        (11,25,"VEHICLE"),    # Toyota Corolla
        (26,38,"VEHICLE"),    # BMW 3 Series
        (39,46,"VEHICLE"),    # Audi A3
        (47,59,"VEHICLE"),    # Honda Civic
        (60,73,"VEHICLE"),    # Nissan Micra
        (74,90,"VEHICLE"),    # Volkswagen Golf
        (91,105,"VEHICLE"),   # Hyundai Tucson
        (106,118,"VEHICLE"),  # Kia Sportage
        (119,130,"VEHICLE"),  # Peugeot 208
    ]
}
),

# ---- 10 TELECOMS ----
(
"07123 456789 07234 567890 07345 678901 07456 789012 07567 890123 07678 901234 07789 012345 07890 123456 07901 234567 07111 222333",
{
    "entities": [
        (0,13,"TELECOM"),     # 07123 456789
        (14,27,"TELECOM"),    # 07234 567890
        (28,41,"TELECOM"),    # 07345 678901
        (42,55,"TELECOM"),    # 07456 789012
        (56,69,"TELECOM"),    # 07567 890123
        (70,83,"TELECOM"),    # 07678 901234
        (84,97,"TELECOM"),    # 07789 012345
        (98,111,"TELECOM"),   # 07890 123456
        (112,125,"TELECOM"),  # 07901 234567
        (126,139,"TELECOM"),  # 07111 222333
    ]
}
),

("James Carter met Emily Green in King Street, Leeds and called 07123 456789 while driving a Ford Focus.",
{
    "entities": [
        (0,12,"NAME"),      # James Carter
        (17,28,"NAME"),     # Emily Green
        (32,43,"LOCATION"), # King Street
        (45,49,"LOCATION"), # Leeds
        (63,76,"TELECOM"),  # 07123 456789
    ]
}),

# 2
("Emily Green drives a Toyota Corolla on Park Lane, London while texting 07234 567890 and meeting Daniel Hughes.",
{
    "entities": [
        (0,11,"NAME"),      # Emily Green
        (21,35,"VEHICLE"),  # Toyota Corolla
        (39,48,"LOCATION"), # Park Lane
        (50,56,"LOCATION"), # London
        (83,96,"TELECOM"),  # 07234 567890
    ]
}),

# 3
("Michael Brown and Laura Bennett drove a BMW 3 Series through Queen Road, York calling 07345 678901.",
{
    "entities": [
        (0,13,"NAME"),      # Michael Brown
        (18,31,"NAME"),     # Laura Bennett
        (38,50,"VEHICLE"),  # BMW 3 Series
        (55,66,"LOCATION"), # Queen Road
        (68,72,"LOCATION"), # York
    ]
}),

# 4
("Thomas Reed owns a Honda Civic reg no. AB12 CDE and lives on Church Street, Bath calling 07456 789012.",
{
    "entities": [
        (0,11,"NAME"),      # Thomas Reed
        (20,32,"VEHICLE"),  # Honda Civic
        (42,50,"PLATE"),    # AB12 CDE
        (61,74,"LOCATION"), # Church Street
        (76,80,"LOCATION"), # Bath
    ]
}),

# 5
("Oliver Grant drives a Hyundai Tucson and met Chloe Adams on Station Road, Cambridge texting 07567 890123.",
{
    "entities": [
        (0,12,"NAME"),      # Oliver Grant
        (22,36,"VEHICLE"),  # Hyundai Tucson
        (47,58,"NAME"),     # Chloe Adams
        (62,75,"LOCATION"), # Station Road
        (77,86,"LOCATION"), # Cambridge
    ]
}),

# 6
("Jack Foster and Emma White called 07678 901234 while driving a Peugeot 208 near High Street, Oxford.",
{
    "entities": [
        (0,11,"NAME"),      # Jack Foster
        (16,26,"NAME"),     # Emma White
        (33,46,"TELECOM"),  # 07678 901234
        (60,71,"VEHICLE"),  # Peugeot 208
        (77,88,"LOCATION"), # High Street
    ]
}),

# 7
("Ryan Scott met Paige Allen on Mill Road, Derby while driving a Kia Sportage and calling 07789 012345.",
{
    "entities": [
        (0,10,"NAME"),      # Ryan Scott
        (15,26,"NAME"),     # Paige Allen
        (30,42,"LOCATION"), # Mill Road
        (44,48,"LOCATION"), # Derby
        (67,80,"TELECOM"),  # 07789 012345
    ]
}),

# 8
("Hannah Price owns a Mini Cooper reg no. CD78 EFG and lives on Bridge Street, Lincoln texting 07890 123456.",
{
    "entities": [
        (0,13,"NAME"),      # Hannah Price
        (22,33,"VEHICLE"),  # Mini Cooper
        (43,51,"PLATE"),    # CD78 EFG
        (61,74,"LOCATION"), # Bridge Street
        (76,83,"LOCATION"), # Lincoln
    ]
}),

# 9
("Matthew King drove a Ford Fiesta and met Lucy Turner at Victoria Road, Preston calling 07901 234567.",
{
    "entities": [
        (0,12,"NAME"),      # Matthew King
        (23,34,"VEHICLE"),  # Ford Fiesta
        (44,55,"NAME"),     # Lucy Turner
        (59,72,"LOCATION"), # Victoria Road
        (74,81,"LOCATION"), # Preston
    ]
}),

# 10
("Laura Bennett owns a Citroen C3 and drove on North Road, Ripon while texting 07111 222333.",
{
    "entities": [
        (0,13,"NAME"),      # Laura Bennett
        (23,33,"VEHICLE"),  # Citroen C3
        (37,48,"LOCATION"), # North Road
        (50,55,"LOCATION"), # Ripon
        (66,79,"TELECOM"),  # 07111 222333
    ]
}),

# 11
("Ben Clark and Sophie Adams called 07222 333444 while driving a Nissan Micra on Church Street, Bath.",
{
    "entities": [
        (0,9,"NAME"),       # Ben Clark
        (14,26,"NAME"),     # Sophie Adams
        (34,47,"TELECOM"),  # 07222 333444
        (60,72,"VEHICLE"),  # Nissan Micra
        (76,89,"LOCATION"), # Church Street
    ]
}),

# 12
("Luke Harris drove a Volkswagen Golf reg no. ZZ99 ABC and met Emily Green on Station Road, York.",
{
    "entities": [
        (0,11,"NAME"),      # Luke Harris
        (21,37,"VEHICLE"),  # Volkswagen Golf
        (47,55,"PLATE"),    # ZZ99 ABC
        (65,76,"NAME"),     # Emily Green
        (80,92,"LOCATION"), # Station Road
    ]
}),

# 13
("Paige Allen owns a Hyundai i30 and called 07333 444555 on Mill Lane, Sheffield.",
{
    "entities": [
        (0,11,"NAME"),      # Paige Allen
        (21,30,"VEHICLE"),  # Hyundai i30
        (40,53,"TELECOM"),  # 07333 444555
        (57,66,"LOCATION"), # Mill Lane
        (68,77,"LOCATION"), # Sheffield
    ]
}),

# 14
("Tom Wright drives a Toyota Avensis and met Hannah Bell on Bridge Road, York calling 07444 555666.",
{
    "entities": [
        (0,9,"NAME"),       # Tom Wright
        (19,35,"VEHICLE"),  # Toyota Avensis
        (45,56,"NAME"),     # Hannah Bell
        (60,71,"LOCATION"), # Bridge Road
        (73,77,"LOCATION"), # York
    ]
}),

# 15
("Ella Richardson owns a Renault Clio reg no. MN56 OPQ and drove on King Street, Derby calling 07555 666777.",
{
    "entities": [
        (0,14,"NAME"),      # Ella Richardson
        (24,37,"VEHICLE"),  # Renault Clio
        (47,55,"PLATE"),    # MN56 OPQ
        (65,76,"LOCATION"), # King Street
        (78,82,"LOCATION"), # Derby
    ]
}),

# 16
("Sam Walker drives a BMW 3 Series and met Laura Bennett on Queen Road, Leeds while texting 07666 777888.",
{
    "entities": [
        (0,10,"NAME"),      # Sam Walker
        (20,32,"VEHICLE"),  # BMW 3 Series
        (36,47,"NAME"),     # Laura Bennett
        (51,62,"LOCATION"), # Queen Road
        (64,68,"LOCATION"), # Leeds
    ]
}),

# 17
("Rachel Evans drove a Honda Civic reg no. EF78 GHI and called 07777 888999 on Park Lane, Cambridge.",
{
    "entities": [
        (0,13,"NAME"),      # Rachel Evans
        (23,35,"VEHICLE"),  # Honda Civic
        (45,53,"PLATE"),    # EF78 GHI
        (63,76,"TELECOM"),  # 07777 888999
        (80,92,"LOCATION"), # Park Lane
    ]
}),

# 18
("Megan Howard owns a Nissan Leaf and met Luke Harris on Station Street, Oxford calling 07888 999000.",
{
    "entities": [
        (0,12,"NAME"),      # Megan Howard
        (22,33,"VEHICLE"),  # Nissan Leaf
        (37,48,"NAME"),     # Luke Harris
        (52,67,"LOCATION"), # Station Street
        (69,74,"LOCATION"), # Oxford
    ]
}),

# 19
("Daniel Cooper drives a Volvo XC60 reg no. TT11 QWE and called 07999 000111 near Mill Lane, York.",
{
    "entities": [
        (0,13,"NAME"),      # Daniel Cooper
        (23,34,"VEHICLE"),  # Volvo XC60
        (44,52,"PLATE"),    # TT11 QWE
        (62,75,"TELECOM"),  # 07999 000111
        (81,89,"LOCATION"), # Mill Lane
    ]
}),

# 20
("Olivia Turner owns a Peugeot 208 and called 07121 223344 while driving on Church Road, Bath with Ryan Scott.",
{
    "entities": [
        (0,13,"NAME"),      # Olivia Turner
        (23,34,"VEHICLE"),  # Peugeot 208
        (44,57,"TELECOM"),  # 07121 223344
        (67,78,"LOCATION"), # Church Road
        (80,84,"LOCATION"), # Bath
    ]
})
]