import datetime
import math
from pprint import pprint

email = {
    "subject": "  Quarterly Report  ",
    "from": "  Alice.Cooper@Company.ru ",
    "to": "   bob_smith@Gmail.com   ",
    "body": "Hello Bob,\n\tHere is the quarterly report.\n\tPlease review and let me know your feedback.\n\nBest,\nAlice",
}

send_date = datetime.date.today().strftime("%Y-%m-%d")
email["date"] = send_date

email["from"] = email["from"].strip().lower()
email["to"] = email["to"].strip().lower()

login, domain = email["from"].split("@")

email["short_body"] = email["body"][:10] + "..."

personal_domains = [
    "gmail.com",
    "list.ru",
    "yahoo.com",
    "outlook.com",
    "hotmail.com",
    "icloud.com",
    "yandex.ru",
    "mail.ru",
    "list.ru",
    "bk.ru",
    "inbox.ru",
]
unique_personal_domains = list(set(personal_domains))

corporate_domains = [
    "company.ru",
    "corporation.com",
    "university.edu",
    "organization.org",
    "company.ru",
    "business.net",
]
unique_corporate_domains = list(set(corporate_domains))

has_intersection = bool(set(personal_domains) & set(corporate_domains))

is_corporate = domain in unique_corporate_domains

email["clean_body"] = email["body"].replace("\n", " ").replace("\t", " ").strip()

email[
    "sent_text"
] = f"""Кому: {email["to"]}, от {email["from"]}
Тема: {email["subject"]}, дата {email["date"]}
{email["clean_body"]}"""

pages = math.ceil(len(email["sent_text"]) / 500)

is_subject_empty = not bool(email["subject"].strip())
is_body_empty = not bool(email["body"].strip())

email["masked_from"] = (
    f"{email['from'].split('@')[0][:2]}***@{email['from'].split('@')[1]}"
)

personal_domains.remove("list.ru")
personal_domains.remove("bk.ru")

pprint(email)
