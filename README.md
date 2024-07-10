# DNS_entropy

DNS entropy refers to the randomness or unpredictability in the selection of domain names by users. It's a measure of how well domain names resist guessing or prediction. Higher entropy means domain names are harder to guess, which can be important for security and privacy. -ChatGPT

Basically it is saying using the same letter over and over in a domain is easy to come up with and a domain with many different characters is difficult to come up with. This can be important because it could be an indicator of Domain Generation Algorithms (DGAs) being used by malicious actors.

These scripts use the Shannon formula to generate an entropy score. The higher the score the greater the entropy (randomness of characters) and worth scrutinizing.
However, there are a lot of normal sites with relatively high entropy scores, for example: en.wikipedia.org has a score of 3.45, compared to this random example: qxe8g4xm.example.com has a score of 3.51.  

There are three scripts, hopefully their names will give you an idea of what they return.  
entropy.py will return the entropy score for the whole url  
entropySubdomain.py will return the entropy score for just the subdomain  
entropyDomain.py will return the entropy score for just the domain (minus the subdomain)

These are meant to be run through command line using python3 with an argument being the file of domain names. for example:
python3 entropy.py domains.txt  
the txt file can be anything as long as it's a list of URLs

There is a line at the top of the scripts to run them from bash, if you don't want that just delete it, or if you do make sure you chmod it to be executed
