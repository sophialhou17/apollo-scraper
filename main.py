import files
import request

import os
from dotenv import load_dotenv

load_dotenv()

APOLLO_API_KEY = os.getenv("APOLLO_API_KEY")
INPUT_PATH = os.getenv("INPUT_PATH")
parsed_path = INPUT_PATH.split("\\")[:-1]
parsed_path.append("emails.csv")

OUTPUT_PATH = "\\".join(parsed_path)

if __name__ == "__main__":
    companies = files.read_companies_csv(INPUT_PATH) # read in companies

    company_info = request.get_emails(companies) # find name and email through apollo

    files.write_email_csv(INPUT_PATH, OUTPUT_PATH, company_info) # write to csv file

    print("Done.")