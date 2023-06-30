# Readme

https://im-aadhirapr.github.io/resume-screener/

Screening the resume that has been uploaded and shortlisting the resumes that satisfy the condition given (example : The resumes scoring 10% above in data science would be shortlisted). The resumes that passes the condition will get an automatic mail of an technical aptitude.

We can split the project to 3 phases:
#### Phase 1
The candidates can only upload the resume which 
is in the format of PDF, into the website which we created with the help of the html. 
In to that created website the candidate need to upload the resume. Now the uploaded resume is taken as input process and it will performs it's further steps in next phase.

#### phase 2
Phase 2 can be divided into 7:
 1. PDF file opening, reading and text extraction
 2. Text cleaning
 3. Email extraction
 4. Dictionary with key terms by area setup
 5. Scores calculation per area
 6. Sorted data frame for final scores creation
 7. Pie chart creation

Now the uploaded resume is taken as input that as mentioned earlier in the phase 1, and the next phase of the project is to take the resume that has been uploaded and it reads and extract the text from the uploaded resume. Here they only take the pdf files. After extraction of the text, the resume is cleaned, which means clearing all kind of unnecessary texts such as commas, bracket and all sorts of special symbols. As the special symbols are removed we add @ symbol for extracting the E-mail id from resume. 

Then a dictionary is added where there would be keywords. The key terms included in each area of this dictionary were obtained through a research of the most common key terms included in industrial and system engineering job postings. This dictionary can be customized to add/remove key terms according to hiring managers criteria.

So when the extracted text words matches the words of keyword then the scores are appended. With the scores a calculated a sorted data frame would be created. With the help of sorted data frame a pie chart would be created.

#### phase 3
The sorted data frame that has been already calculated in phase 2 would be taken out to check the condition that the company required. The condition would be like: "if a candidates resume has a pass score in a particular slice of the pie chart then an automated mail would be send to the candidates". The pass score in particular slice is arranged by the company. 

- [references](references.md)
- [keywords](keywords.md)
- [installation](installation.md)
