# problem 929 Unique email address
import re
def uniqueEmail(emails: list[str]) -> int :
  uniqueEmails=[] #store exact email destination
  for email in emails : #iterate through emails
    splitEmail=email.split("@") #split local name and domain name
    # remove "." and chars after "+" from local name
    splitEmail[0] = re.sub(r'\.|(\+.*)','',splitEmail[0])
    email="@".join(splitEmail) # merge the local name and domain name
    if email not in uniqueEmails: # assert emails uniquness
      uniqueEmails.append(email) # store unique email
  return len(uniqueEmails) # return number of unique emails

emails= ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
print(uniqueEmail(emails))

emails = ["a@leetcode.com","b@leetcode.com","c@leetcode.com"]
print(uniqueEmail(emails))