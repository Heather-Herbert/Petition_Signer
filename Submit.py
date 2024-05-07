import requests
import random
import uuid
from bs4 import BeautifulSoup


def generate_random_name():
    # List of common forenames (first names)
    forenames = [
        "Alice", "Bob", "Charlie", "David", "Emily", "Fiona", "George", "Henry",
        "Isabella", "Jack", "Olivia", "William", "Sophia", "James", "Benjamin", "Charlotte",
        "Noah", "Ava", "Lucas", "Mia", "Liam", "Evelyn", "Mason", "Abigail", "Ethan",
        "Elizabeth", "Aiden", "Sofia", "Matthew", "Ella", "Daniel", "Avery", "Alexander",
        "Harper", "Anthony", "Camila", "Joseph", "Luna", "Jackson", "Scarlett", "Andrew",
        "Eleanor", "Michael", "Penelope", "Samuel", "Layla", "David", "Riley", "Richard",
        "Zoey", "Joshua", "Aurora", "Christopher", "Claire", "Daniel", "Violet", "Matthew",
        "Amelia", "Jacob", "Stella", "William", "Everly", "Brandon", "Natalia", "Benjamin",
        "Mila", "Nicholas", "Audrey", "Elijah", "Eleanor", "Logan", "Olive", "Alexander",
        "Elizabeth", "Gabriel", "Zoe", "Joseph", "Charlotte", "Daniel", "Leila", "Anthony",
        "Harper", "Andrew", "Luna", "James", "Evelyn", "Isaac", "Scarlett", "Lucas", "Amelia",
        "Owen", "Nora", "John", "Mila", "David", "Eliana", "Michael", "Avery", "Benjamin",
        "Zoe"
    ]

    # List of common surnames (last names)
    surnames = [
        'Smith', 'Johnson', 'Williams', 'Jones', 'Brown', 'Davis', 'Miller',
        'Wilson', 'Moore', 'Taylor', 'Anderson', 'Thomas', 'Jackson', 'White',
        'Harris', 'Martin', 'Thompson', 'Garcia', 'Martinez', 'Robinson'
    ]

    # Generate a random forename (first name) and surname (last name)
    forename = random.choice(forenames)
    surname = random.choice(surnames)

    # Return the generated full name
    return f"{forename} {surname}"


def add_random_to_email(email):
    # Split the email address at the "@" symbol
    username, domain = email.split("@")

    # Generate a random class 4 UUID without hyphens
    random_string = str(uuid.uuid4()).replace("-", "")

    # Combine the username, "+", random string, and domain
    modified_email = username + "+" + random_string + "@" + domain

    return modified_email


def generate_postcode():
    # List of outward codes for different UK regions
    outward_codes = {
        "England": [
            "AB", "AL", "B", "BA", "BB", "BC", "BD", "BE", "BF", "BH", "BL", "BN", "BR", "BS", "BT",
            "BX", "BY", "CA", "CB", "CF", "CH", "CI", "CK", "CL", "CM", "CN", "CO", "CR", "CT", "CV",
            "CW", "CX", "CY", "DA", "DD", "DE", "DG", "DH", "DL", "DN", "DT", "DY", "E", "EC", "EH",
            "EN", "EX", "FK", "FY", "G", "GL", "GU", "HA", "HD", "HE", "HF", "HG", "HP", "HR", "HS",
            "HU", "HX", "IG", "IM", "IP", "IV", "IW", "JE", "KA", "KF", "KG", "KH", "KT", "KY", "LA",
            "LD", "LE", "LF", "LG", "LH", "LI", "LL", "LN", "LS", "LU", "LV", "LW", "LY", "M", "ME",
            "MK", "ML", "MN", "MQ", "MU", "MW", "MX", "N", "NE", "NG", "NN", "NP", "NR", "NW", "OL",
            "OX", "PA", "PE", "PH", "PL", "PO", "PR", "PS", "PT", "PW", "QX", "RG", "RH", "RM", "RN",
            "RQ", "RS", "RU", "SA", "SE", "SG", "SH", "SK", "SL", "SM", "SN", "SO", "SP", "SR", "SS",
            "ST", "SW", "SY", "TA", "TD", "TE", "TF", "TG", "TH", "TN", "TO", "TR", "TS", "TT", "TW",
            "TY", "UB", "UX", "VA", "WD", "WF", "WG", "WN", "WR", "WS", "WV", "WX", "YO", "ZE"
        ],
        "Scotland": ["AB", "EH", "FK", "G", "KA", "KY", "ML", "PA", "PH", "TD", "ZE"],
        "Wales": ["CF", "SA", "SY", "LL", "LD", "SA", "TR"],
        "Northern Ireland": ["BT"]
    }
    # Generate random outward and inward codes
    region = random.choice(list(outward_codes.keys()))
    outward_code = random.choice(outward_codes[region]) + str(random.randint(0, 9)) + str(random.randint(0, 9))
    inward_code =  str(random.randint(0, 9)) + str(random.randint(0, 9)) + chr(random.randint(65, 90)) + str(random.randint(0, 9))
    return f"{outward_code} {inward_code}"


def submit_responce(url, original_email):

    # Send a GET request to the URL to obtain initial cookies and HTML content
    response = requests.get(url)
    cookies = response.cookies

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Identify the form fields by their IDs
    signature_name = generate_random_name()
    signature_email = modified_email = add_random_to_email(original_email)
    signature_location_code = 'GB'  # The UK
    signature_postcode = generate_postcode()

    # Prepare form data
    form_data = {
        'signature[name]': signature_name,
        'signature[email]': signature_email,
        'signature[location_code]': signature_location_code,
        'signature[postcode]': signature_postcode,
        'signature[notify_by_email]': '1',  # 1 if checkbox should be selected for email notification
        'signature[uk_citizenship]': '1'   # 1 if checkbox should be selected for UK citizenship
    }

    # Send a POST request to submit the form
    response = requests.post(url, data=form_data, cookies=cookies)

    print(f"{signature_name} - {signature_email} - {signature_postcode}")

    # Check if the form submission was successful
    if response.status_code == 200:
        print("Form submitted successfully!")
    else:
        print(f"Form submission failed with status code: {response.status_code}")


url = 'https://petition.parliament.uk/petitions/651223/signatures/new'
email_address = 'Fake.Address@gmail.com'

x = range(10)
for n in x:
    submit_responce(url,email_address)


