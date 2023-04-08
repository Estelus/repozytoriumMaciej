# <h1> Konfiguracja oprogramowania
# <h3>Dlaczego zdecydowałem się wziąć udział w wyzwaniu Dare IT Challenge?
Ponieważ chciałbym nabyć umiejętności w zakresie automatyzacji testów i zbudować swoje repozytorium. 

QUIZ ISTQB PURPUROWY- UDZIELONO ODPOWIEDZI DOBRZE NA 10 Z 14

# <h3>ZADANIE 2: Selektory
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