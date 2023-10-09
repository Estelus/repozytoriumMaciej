
*My name is Maciej. I am 29 years old and have been working as a functional game tester for 1.5 years. I would like to acquire test automation skills and build my repository. So far, I have only used manual tests in my work. Man does not live by games alone, so I would also like to expand my knowledge by testing other types of applications.
Every day I like to read fantasy novels and crime stories. I am a lover of both cats and dogs. In my house I have a cat, Mimcie, and a dog, Mikusie.
The ISTQB quiz went exceptionally well for me as I passed the ISTQB exam on March 17.*


QUIZ ISTQB PURPUROWY- UDZIELONO ODPOWIEDZI DOBRZE NA 10 Z 14

# <h3> Selektory
#
Scouts Panel:

* $x//*"[@id="__next"]"
* $x//*"[text()="Scouts Panel""]
* $x//*"[@class=.MuiTypography-gutterBottom]"
* $x//*"("[@id="__next"]/form/h5")

Login: 

* $x//*([@id="__next"]/form/div[2]/a)
* $x//*([text()="Login"])
* $x//*([@class=".MuiFormControl-root"])

Password:

* $x//*([@id="password-label"])
* $x//*([contains(@class="MuiInputBase-input MuiInput-input ", @id="password")])
* $x//*(input[type="MuiInputBase-root MuiInput-root MuiInput-underline MuiInputBase-formControl MuiInput-formControl"])	

Remind Password:

* $x//*([@id="__next"]/form/div[3]/a)
* $x//*([contains(@class, "MuiTypography-root MuiLink")]) 
* $x//*([text()="Remind password"])
