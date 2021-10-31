from os import pipe


start = """
Ik was in mijn kantoor en opeens hoor ik een harde kanal. Ik wist niet wat er aan de hand was.
Ik zij dat we mischien weg moesten en daar was mijn baas helemaal mee eens.
Ik ging naar mijn huis om snel een tas intepakken. Het is vertrietig dat je huis moet verlaten.
"""

weg = """
Ik moest ergens heen maar waar overal is oorlog. Ik moet ergens heen.
Er is een stad verder op mischien 10 km hier vandaan.
Daar ga ik heen.
"""

nieuwestad1 = """
Ik ben net aangekomen er is overal paniek van mensen ik weet niet wat ik ga doen.
Er is een groep mensen aan het praten maar ik weet niet als ik met hun ga praten of niet.
"""

nieuwestad1AB = """
A: Praat met de groep mensen.
B: Praat niet met de groep mensen.
"""
#als je A van nieuwestad1AB kiest doe je dit

groep1 = """
De groep zegt dat ze ergens anders gaan naar waar mensen vechten voor vrijheid.
Ik vraag wat bedoel je met vrijheid.
De groep zegt dat mensen daar zijn vrij en zorgen voor elkaar.
Ik twijfl als ik met hun mee wil of niet.
"""

groep1AB = """
A: Ik ga mee.
B: ik blijf in de stad.
"""

#als je B kiest van nieuwestad1AB doe je dit

blijf1 = """
Je ziet iemand die heeft hulp nodig hij heeft last van zijn enkel en kan niet lopeen.
Je sleept hem naar een terras waar er overdakking is.
Hij heeft heel veel last van zijn enkel.
"""

blijf1AB = """
A: Je vraagt mensen in de buurt voor hulp.
B: Je probeert het zelf optelossen.
"""

#als je A kiest voor groep1AB doe je dit

onderweg1 = """
We beginnen ons voortebereiden voor het vertrek. We pakken extra eten en driken.
we willen zorgen dat we de weg niet kwijt raken anders gaan we het niet reden.
Ik ben aan het na denken wat er zou gebeuren als we de weg kwijt raken.
Na 30 minuten lopen heb ik het pas door dat ik mijn tas vergeten.
"""

onderweg1AB = """
A: Ik laat het.
B: Ik ga terug.
"""

#als je A kiest voor onderweg1AB doe je dit

wegkwijt1 = """
We zijn nu 3 uur aan het lopen de lijder van de groep vraagt voor het kaart.
Ik kwan toen pas achter dat ik de kaart had in mijn tas ik zeg dat we trug moeten.
de lijder zegt dan hebben we niet genoeg eten we moeten door lopen we kunnen niet terug.
Dus lopen we door en komen we bij een splitsing.
"""

wegkwijt1AB = """
A: Rechts
B: Links
"""

#als je B kiest voor onderweg1AB doe je dit

aangekomen1 = """
We gingen terug voor het kaart en daardoor konden we de weg vinden we deden ongeveer 2 dagen over.
Maar toch zijn we aangekomen we kregen gelijk wat eten en drinken.
Dat was heel aardig van hun. Graag wilde we hun helpen met dinken doen.
"""

aangekomen1AB = """
A: De leger in.
B: Andere werk vinden.
"""

#als je A kiest voor wegkwijt1AB doe je dit

dood1 = """
Jouw groep heeft uren itten lopen en de lijder zegt dat je 2 uur geleden bij het stad moest zijn.
Ik kwam pas achter dat al het eten op was en als we terug moesten ging we dat niet reden.
We gingen de bergen in maar zonder eten zijn we bevroren we konden niet meer.
"""

#als je B kiest voor wegkwijt1AB doe je dit

aangekomen2 = """
we kwamen aan na 2,5 dagen we hadden best honger en wilde at eten.
We waren heel dankbaar voor het eten en drinken die we kregen.
Ik wilde graag helpen. Maar wat weet ik niet.
"""

aangekomen2AB = """
A: Het leger in
B: Andere werk vinden
"""

#als je A kiest voor aangekomen1AB doe je dit

vechten1 = """
Je gaat vragen als je leger in mag want je wilt helpen om je land te bevreiden.
De general moet over na denken als jij de leger in mag.
Hij zegt dat het minstens een week kan duren.
Ik zit na te denken over als hij nee zegt wat kan ik dan doen.
Ik heb allei iedeen bedacht helpen met water uitdelen of eten regelen.
"""

#het gaat door print dit ook na vechten1

helpen1 = """
Je hoord dat de general ja heeft gezegt en daar ben je heel trots mee.
Ik moest wel leren hoe je een geweer vast moest houden.
Ik zat na te denken hoeveel mensen ik helpen om ons land te bevrijden.
"""

#einde van vechten1

#als je B kiest voor aangekomen1AB

werkvinden1 = """
Ik ging rond vragen als ik werk kon vinden om mensen te helpen.
Iemand zij wat over helpen met eten rond bregen en dat lijk me wat.
Ik kon heel veel mensen helpen om eten te brengen en ik wilde mensen helpen.
Het is nu 4 weken later en ik breng nog steeds eten rond maar ik hoorde een groep mensen
die wilde vluchten naar turkije.
"""

werkvinden1AB = """
A: Blijf ik mijn werk doen
B: Ik ga vluchten
"""

#als je A kiest voor wekvinden1AB doe je dit

blijf4 = """
Je blijft om dat je denk dat je meer hier kan doen dan als je ging vluchten.
Ik weet ook niet wat er gaat gebeuren maar toch denk ik dat hier veiliger is dan ergens anders.
Ik blijft liever in mijn land dan naar een vreemt land.
"""

#einde voor blijf4

#als je B kiest voor werkvinden1AB doe je dit

terkijeplan1 = """
Ik ging naar dat groep mensen en vroeg wanneer ze gaan vluchten.
Hun antwoord was morgen dus ging ik mijn spullen inpakken. Ik was er klaar voor.
Ze kwamen me wakker maken en zeiden dat me nu gingen. 
Onderweg vroeg ik hoe we gingen vluchten en hun zeiden met boot of vliegtuig.
Ik had wel genoeg geld voor allei opsies maar welk zal ik kiezen.
"""

terkijeplan1AB = """
A: Boot
B: Vliegtuig
"""

#als je A kiest voor terkijeplan1AB doe je dit

boot1 = """
Je kwam aan bij de boten ervaren er twee.
Ik wist niet voor welke boot ik moest kiezen kies ik voor de grote of de kleine.
"""

boot1AB = """
A: Grote boot
B: kleine boot
"""

#als je B kiest voor terkijeplan1AB doe je dit

vliegtuig1 = """
Je komt aan bij het vliegveld en je laat je pasport zien.
Ze vragen waar je vandaan komt en je verzint wat je mag doorlopen.
Ik was bang dat ik mischien de verkeerde ding zeg maar een van de mensen uit de groep zegt
waar die echt net vandaan komt en word opgepakt.
Kom je voor hem op of laat je hem achter.
"""

vliegtuig1AB = """
A: Je laat het zitten en durf niet om voor hem optekomen.
B: Je komt wel voor hem op.
"""

#als je B kiest vvor vliegtuig1AB doe je dit

mislukt1 = """
Je wordt opgepakt.

Ze denken dat je wilt vechten en wordt weg van de vliegveld gestuurd.
Ik vond het heel oneerlijk dat we weg werden gestuurd maar we konden er niks aan doen.
"""

#print dit gelijk ook na mislukt1

dood4 = """
Er komt een groep mensen aan.

Ik kwam er achter dat ze ons de hele tijd zaten te volgen.
Ik wilde me berschermen maar als was in mijn tas en dat zat binnen de vliegveld en kon ik niks aan doen.
Ik wilde gaan vechten maar had geen zin er waren 7 man op ons af we konden nergens heen rennen.
Wat gebeurd is ga ik niet vertellen maar het was wel snel.
Door dit hele verhaal wilde ik vluchten om er voor te zorgen dat ik geen zorgen hoef te maken
het was niet de einde die ik wilde maar toch hoef ik geen zorgen te maken.
"""

#als je A kiest voor boot1AB doe je dit

dood3 = """
Je heb voor de grote boot gekozen.
IK wist het niet maar er kwamen ongeveer 120 mensen in ons boot geen ruimte.
Ik wilde niet in de paniek komen dus had ik een spel bedacht vissen tellen.
Ik begon met tellen 1,2,3 en opeens raakte we iets ik weet niet wat.
We waren best ver van de kust niemand daar van daan kon ons zien.
De boot begon te sinken er waren geen redings vesten ik kon ook niet swemmen.
Voor dat ik het door had begon ik te sinken en verdrinken.
De boven kant van de zee werd steeds verder uit zich en opeens was het zwart ik kon niet meer zien.
"""

#einde van antoord A van boot1AB

#als je B kiest voor boot1AB doe je dit

aangekomen4 = """
In dat kleine boot zaten ongeveer 70 mensen geen ruimte.
Ik zach een vrouw. Ze zij dat ze het niet meer kon vol houden.
Ik zij tegen haar kom met mij een speletje doen vissen telen is wel leuk.
Daar was ze helemaal mee eens ik vond het ook leuk om met een vrouw vissen telen.
Na een tijdje vroeg iemand als hun mee kon doen ik zij natuurlijk en hij ging ook telen.
8 uur later kwamen we aan in Terkije en waren heel blij dat we eindelijk aangekomen.

Ik was eindelijk uit Afghanistan en daar was ik helemaal blij mee.
We waren in Terkije voor ongeveer 5 weken en zaten na te denken als ons leven beter kon zijn 
als we niet over oorlog hoeft na te denken.
Iemand zij europa maar ik wist niet veel van europa.
Hoe het daar is bijvoorbeeld.
"""

aangekomen4AB = """
A: Blijven.
B: Na europa gaan.
"""

#als je A kiest voor vliegtuig1AB doe je dit

aangekomen5 = """
Ik zat in de vliegveld en zat na te denken als ik mischien mijn vriend moest helpen of niet.
Dan zat hij mischien hier ook. Ik heb wel spijt over wat ik deed.
Maar ik moet zo de vliegtuig instappen naar Terkije en daar heb ik wel zin in.
Eindelijk weg van de oorlog en ik heb het ook overleeft.
Ik zat er over na te denken hoe heb ik dit overleeft.

2 uur later was het weer zo ver ik was in Terkijke ik was heel blij maar ik had geen plan.
Niemand had een plan dus moest ik een verzinnen voor mij.
4 weken later had ik van iemand gehoord over europa en dat leek me wel intresant.
"""
aangekomen5AB = """
A: Naar europa vluchten.
B: In Terkije blijven.
"""

#als je A kiest voor aangekomen4AB doe je dit

blijf5 = """
Ik heb toch gekozen om te blijven ik denk dat ik een goed leven kan beginnen.
Als ik toch terug moet om te helpen dan is dat best makkelijk.
Ik heb een nieuwe baan gevonden in tech en dat vind ik geweldig.
Daarom kan ik een huis huren en kan ik eindelijk wonen zonder dat er oorlog om me heen is.
En dat vind ik persoonlijk geweldig hier blijven.
"""

#einde van blijf5

#als je B kiest voor aangekomen5AB doe je dit

blijf6 = """
Ik heb gekozen om hier te blijven het is voor mij heel erg belangerijk
dat ik snel Afghanistan. Als ik binnen eroupa was kon dat niet zo snel.
Ik wil natuurlijk zo snel mogelijk een baan vinden hopelijk iets met Tech
maar dat weet ik nog niet. Ik kan niet wachten tot ik een huis heb.
Maar wel eerst een baan vinden dat is belangelijk.
"""

#einde van blijf6

#als je B kiest van aangekomen4AB of A kiest van aangekomen5AB doe je dit

europaplan1 = """
Ik wist niet hoe ik naar Europa ging met de boot of vliegtuig ik wil gewoon weg.
Ik denk dat ik met de boot ga want vliegtuig is veelste duur dus ga ik met de boot.
Ik hoop dat ik veilig aan kom in Europa  dat er niks ergs gebeurd.
Ik heb een smokelaar gevonden die mij wil helpen om naar Europa brengen.
Het kost wel veel om naar Europa te gaan maar hopelijk kan ik daar een beter leven krijgen.
Ik heb van de smokelaar gehoord dat we in Spanje aan zou komen.
"""

#print dit ook nog

spanje1 = """
Ik was wakker op de boot ik kon niet slapen het was donker je kon niks zien.
In de boot waren er ongeveer 100 mensen ik was bang dit keer ik wist niet wat zou gebeuren.
Ik ging met niemand praten. Het was dood stilte op de boot niemand kon wat zeggen.
Ik dacht dat iedereen bang was maar ik dufte het niet vragen.
Toen het iets lichter werd dan begon mensen met elkaar te praten.
Ik vond het wel gezellig en het is ook handig want dan denk je niet meer over het gevaar.
We kwamen aan in Spanje en gelijk wilde ze ons weg sturen maar dat wilde ik niet.
We kwamen aan op het stand en daar probeertse ons tegen te houden.
Toch liepen we door ze wilde ons niet in spanje hebben dus kregen we een dag om te blijven en daarna
een trein kaartje naar Nederland nooit van gehoord.
"""

#print dit ook nog

nederland1 = """
Ik stapte de trein uit en werden we door vluchteling werk Nederland geholpen.
Ik bleef in een asiel. Daar werd ik allei dingen gevraagd over wat deed ik in Afghnistan
waar ben ik natoe gegaan dat soort dingen. Daarna kreeg ik te horen dat ik mocht blijven.
En daar was ik helemaal blij mee.
"""

#print dit ook nog

blijf7 = """
In de asiel kreeg ik Nederlands les dus kon ik een burger worden.
Ik wist niet hoe moeilijk nederlands zou zijn maar dat is het ook.
Ik had gelukt want ik kon best goed Engels en dat spreekt ieder nederlander.
Dus stel dat ik een woord niet weet dan zeg ik dat in het Engels en dan weet iedereen het.

Na een tijdje kreeg ik mijn burgerschap en werd ik verplaats naar Castricum en daar heb ik een huis.
Ik heb ook een baan gevonden in Tech in Amsterdam dus voor mij is dat heel goed en hoef ik geen zorgen te maken over geld of
als ik kan worden neergeschoten zomaar op straat.
"""

#einde blijf7

#als je A kiest voor blijf1AB doe je dit.

vraaghulp1 = """
je vraagt hulp aan een groep mensen.

Ik vraag als ze mijn kunnen helpen. Gelukig is een van hun een doctor.
hij helpt mij om de man enkel recht te zetten. Ik vroeg als hij met ons mee wilde.
En ik hoop dat ze ja zeggen.
"""

vraaghulp1AB = """
A: Ze zeggen ja.
B: ze zeggen nee.
"""

#als je B kiest voor blijf1AB doe je dit.

zelf1 = """
Ik wilde geen hulp hebben.Ik kan dit allemaal zelf oplossen.
Ik moet alleen zijn enkel recht krijgen en dan gaat het goed.
Ik pak een kleine metalen paal en bind hem vast aan zijn enkel en hoop dat het goed gaat.
"""

zelf1AB = """
A: Let niet zo vaak op hem.
B: Let veel op hem.
"""

#als je A kiest voor zelf1AB doe je dit

erger1 = """
Je let niet zo vaak op hem.

Over nacht werd hij blijkbaar erger hij kon niet opstaan.
Hij kon niet eens zijn hooft optillen ik weet niet wat aan de hand is.
Ik wilde hulp vragen maar iedereen is weg en weet ik niet wat ik moet doen.
"""

erger1AB = """
A: Iets proberen.
B: Laten en hoop dat het vanzelf opgelost word.
"""

#als je B kiet voor zelf1AB doe je dit

beter1 = """
Het ging steeds beter hij had bijna geen pijn meer.
Hij wil dat hij gaat lopen maar dat wil ik nog niet anders krijgt hij mischien meer last.
Ik hoorde de leger aankomen maar ik wist niet wat ik moest doen ik kan wel verstoppen maar we kunnen ook vluchten.
"""
beter1AB = """
A: Verstoppen
B: Vluchten
"""

#als je A kiest voor beter1AB doe je dit

blijf3 = """
Ik ga verstoppen in een oud huis die een kelder heeft en ik hoop dat we niet worden gevonden.
Ik hoorde voeten stappen op het trap die de kelder in gaan ik was bang ik begon te trillen.
We konden nergens natoe HIj kwam de trap af en keek ons recht in de ogen en zij dat er mensen hier waren.
Ze dachten dat ik een spion was enwerd ik niet mee genomen ze hadden mij geschoten.
"""

#print dit ook

dood2 = """
Ik zag aleen zwart niks ik was dood en kon ik niks aandoen.
"""

#als je A kiest voor erger1AB doe je dit

koorts1 = """
Helaads heeft hij nu koorst.

Ik werd wakker een ik kwam er achter dat hij koorst had.
Ik ging hellemaal in de panniek ik wist niet wat ik moest doen.
Ik pakkte een doek met koud water en probeert het zo optelossen.
"""

#print dit ook

hijdood1 = """
Ik kwam er achter dat hij een infectie in zijn been had.
toen ik hem ging slepen heb ik perongeluk een kleine deel van zijn been open gemaakt.
Helaas heeft hij het niet overleeft ik had alls geprobeert wat ik kon verzinnen.
Maar helaas kwam ik er te laat achter.
"""

#print dit ook

opgepakt1 = """
Ik was aan het huilen toen het gebeurde ik hoorde niks.
Ik had niet eens door wat er aan de hand was. Ik werd opgepakt.
Door wie weet ik het niet. Ik weet niet hoe dit gaat aflopen maar het is niet goed.
"""

#einde van verhaal van erger

#als je B kiets voor erger1AB doe je dit 

#print je eerst hijdood1 en daarna opgepakt1

#als je B kiest voor groep1AB doe je dit

blijf2 = """
Ik was aan het rond lopen en zat ik over de oorlog natedenken.
Opeens kwam ik mijn oude vriend tegen en ging ik met praten.
Ik heb hem al jaren niet gezien ik zie een groep maar ga naar hun toe of niet.
"""

blijf2AB = """
A: Praat wel met een groep mensen.
B: Praat niet met de groep.
"""

#als je A kiest voor blijf2AB doe je dit

groep2 = """
De groep mensen hebben nog maar een plek over. 
Ik heb besloten om met de groep te gaan.
Ik zeg tegen mijn vriend dat ik met een greop ga en hoopt dat hij het begrijpt waarom ik hem verlaat.
"""

#print gelijk aangekomen3

aangekomen3 = """
We zijn onderweg niks vergeten het gaat hellemaal goed.
Ik zat me te bedenken wat er allemaal gebeurd is en hoe de toekomst uitziet.
Niemand weet als het oeit goed zou komen maar ik hoop van wel.
We kwammen aan na 2 dagen lopen maar ik ben blij ik kan eindelijk geen zorgen maken.
Ik ben heel te vreden over hoe het nu gaat en voor het eerst ben ik blij.
"""

#als je B kiest voor blijf2AB doe je dit

vriend1 = """
Ik heb besloten om met mijn vriend te blijven.
We hebben besloten om naar een andere stad te vluchten.
We pakken zo snel mogelijk dingen in om te vertrekken. We moeten heel snel zijn er kan niks fout gaan
"""

#als je B kiest voor beter1AB doe je dit

vlucht1 = """
Je kiest er voor om te vluchten.

Ik zie dat we op moesten schieten.
Ik zag in de verte een kar en dacht dat ik hem daar op zou leggen.
We moesten zo snel mogelijk vluchten omdat we wisten niet waar het leger was.
Ik heb bedacht om zo snel mogelijk te lopen dus dat deden we.
Hij zij dat we ook rechtstreeks naar Terkije kon vluchten waaar wat moet ik kiezen.
"""

vlucht1AB = """
A: Naar stad.
B: Terkijke
"""

aangekomen3AB = """
A: Ga het leger in
B: Vlucht naar Terkije
"""


#print gelijk aangekomen3 daar onder

#als je A kiest voor vraaghulp1AB print je groep2

#als je B kiest voor vraaghulp1AB print je erger1

def answer_check():
    answer = input()
    if str(answer).upper() in ['A','B']:
        return answer.upper()
    else:
        while str(answer).upper() not in ['A','B']:
            print('Kies A of B')
            answer = input()
        return answer.upper()
    


print(start)
print(weg)
print(nieuwestad1)
print(nieuwestad1AB)


answer = answer_check()
if answer == "A":
    print(groep1)
    print(groep1AB)
    answer = answer_check()
    if answer == "A":
        print(onderweg1)
        print(onderweg1AB)
        answer = answer_check()
        if answer == "A":
            print(wegkwijt1)
            print(wegkwijt1AB)
            answer = answer_check()
            if answer == "A":
                print(dood1)
                exit()
            else:
                print(aangekomen2)
                print(aangekomen2AB)
                if answer == "A":
                    print(vechten1)
                    print(helpen1)
                    exit()
                else:
                    print(werkvinden1)
                    print(werkvinden1AB)
                    answer = answer_check()
                    if answer == "A":
                        print(blijf4)
                        exit()
                    else:
                        print(terkijeplan1)
                        print(terkijeplan1AB)
                        answer = answer_check()
                        if answer == "A":
                            print(boot1)
                            print(boot1AB)
                            answer = answer_check()
                            if answer == "A":
                                print(dood3)
                                exit()
                            else:
                                print(aangekomen4)
                                print(aangekomen4AB)
                                answer = answer_check()
                                if answer == "A":
                                    print(blijf5)
                                    exit()
                                else:
                                    print(europaplan1)
                                    print(spanje1)
                                    print(nederland1)
                                    print(blijf7)
                                    exit()
                        else:
                            print(vliegtuig1)
                            print(vliegtuig1AB)
                            answer = answer_check()
                            if answer == "A":
                                print(aangekomen5)
                                print(aangekomen5AB)
                                answer = answer_check()
                                if answer == "A":
                                    print(europaplan1)
                                    print(spanje1)
                                    print(nederland1)
                                    print(blijf7)
                                    exit()
                                else:
                                    print(blijf6)
                                    exit()
                            else:
                                print(mislukt1)
                                print(dood4)
                                exit()
        else:
            print(aangekomen1)
            print(aangekomen1AB)
            answer = answer_check()
            if answer == "A":
                print(vechten1)
                print(helpen1)
                exit()
            else:
                print(werkvinden1)
                print(werkvinden1AB)
                answer = answer_check()
                if answer == "A":
                    print(blijf4)
                    exit()
                else:
                    print(terkijeplan1)
                    print(terkijeplan1AB)
                    answer = answer_check()
                    if answer == "A":
                        print(boot1)
                        print(boot1AB)
                        answer = answer_check()
                        if answer == "A":
                            print(dood3)
                            exit()
                        else:
                            print(aangekomen4)
                            print(aangekomen4AB)
                            answer = answer_check()
                            if answer == "A":
                                print(blijf5)
                                exit()
                            else:
                                print(europaplan1)
                                print(spanje1)
                                print(nederland1)
                                print(blijf7)
                                exit()
                    else:
                        print(vliegtuig1)
                        print(vliegtuig1AB)
                        answer = answer_check()
                        if answer == "A":
                            print(aangekomen5)
                            print(aangekomen5AB)
                            answer = answer_check()
                            if answer == "A":
                                print(europaplan1)
                                print(spanje1)
                                print(nederland1)
                                print(blijf7)
                                exit()
                            else:
                                print(blijf6)
                                exit()
                        else:
                            print(mislukt1)
                            print(dood4)
                            exit()
    else: 
        print(blijf2)
        print(blijf2AB)
        answer = answer_check()
        if answer == "A":
            print(groep2)
            print(aangekomen3)
            print(aangekomen3AB)
            answer = answer_check()
            if answer == "A":
                print(terkijeplan1)
                print(terkijeplan1AB)
                answer = answer_check()
                if answer == "A":
                    print(boot1)
                    print(boot1AB)
                    answer = answer_check()
                    if answer == "A":
                        print(dood3)
                        exit()
                    else:
                        print(aangekomen4)
                        print(aangekomen4AB)
                        answer = answer_check()
                        if answer == "A":
                            print(blijf5)
                            exit()
                        else:
                            print(europaplan1)
                            print(spanje1)
                            print(nederland1)
                            print(blijf7)
                            exit()
                else:
                    print(vliegtuig1)
                    print(vliegtuig1AB)
                    answer = answer_check()
                    if answer == "A":
                        print(aangekomen5)
                        print(aangekomen5AB)
                        answer = answer_check()
                        if answer == "A":
                            print(europaplan1)
                            print(spanje1)
                            print(nederland1)
                            print(blijf7)
                            exit()
                        else:
                            print(blijf6)
                            exit()
                    else:
                        print(mislukt1)
                        print(dood4)
                        exit()
            else:
                print(vechten1)
                print(helpen1)
                exit()
        else:
            print(vriend1)
            print(aangekomen3)
            print(aangekomen3AB)
            answer = answer_check()
            if answer == "A":
                print(terkijeplan1)
                print(terkijeplan1AB)
                answer = answer_check()
                if answer == "A":
                    print(boot1)
                    print(boot1AB)
                    answer = answer_check()
                    if answer == "A":
                        print(dood3)
                        exit()
                    else:
                        print(aangekomen4)
                        print(aangekomen4AB)
                        if answer == "A":
                            print(blijf5)
                            exit()
                        else:
                            print(europaplan1)
                            print(spanje1)
                            print(nederland1)
                            print(blijf7)
                            exit()
                else:
                    print(vliegtuig1)
                    print(vliegtuig1AB)
                    answer = answer_check()
                    if answer == "A":
                        print(aangekomen5)
                        print(aangekomen5AB)
                        answer = answer_check()
                        if answer == "A":
                            print(europaplan1)
                            print(spanje1)
                            print(nederland1)
                            print(blijf7)
                            exit()
                        else:
                            print(blijf6)
                            exit()
                    else:
                        print(mislukt1)
                        print(dood4)
                        exit()
            else:
                print(vechten1)
                print(helpen1)
                exit()
else: 
    print(blijf1)
    print(blijf1AB)
    answer = answer_check()
    if answer == "A":
        print(vraaghulp1)
        print(vraaghulp1AB)
        answer = answer_check()
        if answer == "A":
            print(erger1)
            print(erger1AB)
            answer = answer_check()
            if answer == "A":
                print(koorts1)
                print(hijdood1)
                print(opgepakt1)
                exit()
            else:
                print(hijdood1)
                print(opgepakt1)
                exit()
        else:
            print(groep2)
            print(aangekomen3)
            print(aangekomen3AB)
            answer = answer_check()
            if answer == "A":
                print(terkijeplan1)
                print(terkijeplan1AB)
                answer = answer_check()
                if answer == "A":
                    print(boot1)
                    print(boot1AB)
                    answer = answer_check()
                    if answer == "A":
                        print(dood3)
                        exit()
                    else:
                        print(aangekomen4)
                        print(aangekomen4AB)
                        answer = answer_check()
                        if answer == "A":
                            print(blijf5)
                            exit()
                        else:
                            print(europaplan1)
                            print(spanje1)
                            print(nederland1)
                            print(blijf7)
                            exit()
                else:
                    print(vliegtuig1)
                    print(vliegtuig1AB)
                    answer = answer_check()
                    if answer == "A":
                        print(aangekomen5)
                        print(aangekomen5AB)
                        answer = answer_check()
                        if answer == "A":
                            print(europaplan1)
                            print(spanje1)
                            print(nederland1)
                            print(blijf7)
                            exit()
                        else:
                            print(blijf6)
                    else:
                        print(mislukt1)
                        print(dood4)
                        exit()
            else:
                print(vechten1)
                print(helpen1)
                exit()
    else:
        print(zelf1)
        print(zelf1AB)
        answer = answer_check()
        if answer == "A":
            print(erger1)
            print(erger1AB)
            answer = answer_check()
            if answer == "A":
                print(koorts1)
                print(hijdood1)
                print(opgepakt1)
                exit()
            else:
                print(hijdood1)
                print(opgepakt1)
                exit()
        else:
            print(beter1)
            print(beter1AB)
            answer = answer_check()
            if answer == "A":
                print(blijf3)
                print(dood2)
                exit()
            else:
                print(vlucht1)
                print(vlucht1AB)
                answer = answer_check()
                if answer == "A":
                    print(aangekomen3)
                    print(aangekomen3AB)
                    answer = answer_check()
                    if answer == "A":
                        print(vechten1)
                        print(helpen1)
                        exit()
                    else:
                        print(terkijeplan1)
                        print(terkijeplan1AB)
                        answer = answer_check()
                        if answer == "A":
                            print(boot1)
                            print(boot1AB)
                            answer = answer_check()
                            if answer == "A":
                                print(dood3)
                                exit()
                            else:
                                print(aangekomen4)
                                print(aangekomen4AB)
                                answer = answer_check()
                                if answer == "A":
                                    print(blijf5)
                                    exit()
                                else:
                                    print(europaplan1)
                                    print(spanje1)
                                    print(nederland1)
                                    print(blijf7)
                                    exit()
                        else:
                            print(vliegtuig1)
                            print(vliegtuig1AB)
                            answer = answer_check()
                            if answer == "A":
                                print(aangekomen5)
                                print(aangekomen5AB)
                                answer = answer_check()
                                if answer == "A":
                                    print(europaplan1)
                                    print(spanje1)
                                    print(nederland1)
                                    print(blijf7)
                                    exit()
                                else:
                                    print(blijf6)
                                    exit()
                            else:
                                print(mislukt1)
                                print(dood4)
                                exit()
                else:
                    print(terkijeplan1)
                    print(terkijeplan1AB)
                    answer = answer_check()
                    if answer == "A":
                        print(boot1)
                        print(boot1AB)
                        answer = answer_check()
                        if answer == "A":
                            print(dood3)
                            exit()
                        else:
                            print(aangekomen4)
                            print(aangekomen4AB)
                            answer = answer_check()
                            if answer == "A":
                                print(blijf5)
                                exit()
                            else:
                                print(europaplan1)
                                print(spanje1)
                                print(nederland1)
                                print(blijf7)
                                exit()
                    else:
                        print(vliegtuig1)
                        print(vliegtuig1AB)
                        answer = answer_check()
                        if answer == "A":
                            print(aangekomen5)
                            print(aangekomen5AB)
                            answer = answer_check()
                            if answer == "A":
                                print(europaplan1)
                                print(spanje1)
                                print(nederland1)
                                print(blijf7)
                                exit()
                            else:
                                print(blijf6)
                                exit()
                        else:
                            print(mislukt1)
                            print(dood4)
                            exit()


      
        



    






