# <h1> Konfiguracja oprogramowania
# <h3>Dlaczego zdecydowałem się wziąć udział w wyzwaniu Dare IT Challenge?
**Przepraszam, że wcześniej się nie rozpisałem, nie doczytałem tamtego zadania.**
  
*Nazywam się Maciej. Mam 29 lat i od 1,5 roku pracuje jako tester funkcjonalny gier. Chciałbym nabyć umiejętności w zakresie automatyzacji testów i zbudować swoje repozytorium. W swojej pracy do tej pory wykorzystywałem jedynie testy manualne. Nie samymi grami człowiek żyje, więc chciałbym poszerzyć również swoją wiedzę z testowania innych rodzajów aplikacji. 
Na co dzień lubie czytać powieści fantasy, historie kryminalne. Jestem miłośnikem zarówno kotków, jak i psów. W swoim domu mam kotkę Mimcie i psa Mikusie. 
Quiz ISTQB poszedł mi wyjątkowo dobrze, gdyż w 17 marca zdałem egzamin ISTQB.*


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
