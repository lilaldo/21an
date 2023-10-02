# Import av random för används här för att slumpmässigt generera korten som dras av spelaren och datorn.
import random


# Här defineras klassen Cards som förklarar reglerna varje kort och vad de har för funktion och värde.
class Card:
    def __init__(self, färg, nummer):
        self.färg = färg
        self.nummer = nummer
        self.värde = self.get_värde()

    # Tilldelar värden för korten utan tal.
    def get_värde(self):
        if self.nummer == 'knäckt':  # knäckt = 11
            return 11
        elif self.nummer == 'dam':  # dam = 12
            return 12
        elif self.nummer == 'kung':  # kung = 13
            return 13
        elif self.nummer == 'ess':  # Valt att ess == 1.
            return 1
        else:
            return int(self.nummer)  # kompletterar färg och nummer som användaren får tillbaka.

    # Skriver ut tal + färg. Exempelvis '4 spader' eller annan symbol.
    def __str__(self):
        return f"{self.nummer} {self.färg}"


# Här defineras klassen för spelets motorik samt dragning av kort.
class Spel:
    def __init__(self):  # Skapar en kortlek genom att generera en slumpmässig kortlek men alla tal och färger.
        färger = ['♥', '♦', '♣', '♠']
        tal = ['ess', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'knäckt', 'dam', 'kung']
        self.cards = []
        for färg in färger:  # Slumpar fram färgerna...
            for nummer in tal:  # Slumpar fram talen...
                card = Card(färg, nummer)  # ... Till färdiga kort
                self.cards.append(card)  # ... Och lägger till dom i den tomma listan cards.
        random.shuffle(self.cards)

    # Funktion för dragning av det översta kortet i korthögen och ge det till spelarna.
    def dra_kort(self):
        return self.cards.pop()


# Funktion för att få fram totala poängen av de dragna kortet för att spelet ska börja.
def räkning(hand):
    return sum(kort.värde for kort in hand)


# Funktion för spelet
def spela_21():
    spelare = []  # Tom lista där spelarens kort kommer hamna.
    dator = []  # Tom lista där datorns kort kommer hamna.
    spel = Spel()  # Skapar en instans av klassen Spel och lagrar den i en variabel för att initiera en kortlek.

    # For loop för att ge spelaren och datorn kort.
    for x in range(1):
        spelare.append(spel.dra_kort())
        dator.append(spel.dra_kort())

    # While loop som gör det möjligt för att fortsätta dra kort så länge spelaren vill.
    while True:
        player_cards_str = ", ".join(map(str, spelare))  # omvandlar kortet och visar ett värde och en färg utan [].
        print("Dina kort:", player_cards_str)  # Skriver ut spelarens kort.
        spelare_total = räkning(spelare)
        print("Dina poäng:", spelare_total)  # Skriver ut spelarens poäng.

        # Huvudregel: Om spelarens poäng blir större än 21 så vinner datorn och loopen avslutas.
        if spelare_total > 21:
            print("Datorn är vinnare, lycka till nästa gång!")
            break

        # Låter användaren bestämma om hen vill dra ett kort till eller inte.
        choice = input("Vill du dra ett till kort? (ja/nej) ")
        if choice.lower() == 'ja':
            spelare.append(spel.dra_kort())  # Lägger till ett kort till spelaren.

        # Om användaren svarar nej så börjar dator dra kort och poängen börjar räknas.
        elif choice.lower() == 'nej':
            while räkning(dator) < 15:  # Datorn drar kort tills dessa att den totala poängen är mindre än 15.
                dator.append(spel.dra_kort())

            # datorns kort räknas och poängen visas.
            dator_cards_str = ", ".join(map(str, dator))  # omvandlar kortet och visar ett värde och en färg utan [].
            dator_total = räkning(dator)  # Räknar ihop datorns totala poäng...
            print("Datorns kort: ", dator_cards_str)  # ... Och skriver ut dessa tillsammans med kort.
            print("Datorns poäng", dator_total)

            # If loop för att färdigspela utfallet av spelet och utse vinnaren.
            # Om datorns totala poäng är större än 21 eller spelarens totala större än datorns: Vinst.
            if dator_total > 21 or spelare_total > dator_total:
                print(f"Datorn fick {dator_total} poäng och du fick {spelare_total}, Grattis, du vinner! \n")
            # Oavgjort:
            elif dator_total == spelare_total:
                print(f"Ni båda fick {dator_total} poäng, det blev oavgjort. Försök igen. \n")
            # Datorn vinner.
            else:
                print("Datorn vann. \n")
            # Spelet avslutas.
            break


# Om koden inte körs som importerad modul så anropas 'spela_21()' för att starta spelet.
if __name__ == "__main__":
    spela_21()
