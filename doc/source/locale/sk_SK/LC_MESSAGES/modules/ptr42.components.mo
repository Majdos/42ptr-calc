��    ;      �              �  @   �  ,        ;  C   U  7   �  W   �  &   )  $   P     u     �     �  
   �  0   �     �       
   
       *   !  ,   L  .   y  -   �  (   �  +   �  S   +       *   �  ?   �  A     C   D  B   �  H   �  T   	     i	  %   �	     �	     �	  5   �	  7   �	  9   5
  8   o
  9   �
     �
  C   �
     >     P     j  "   {     �  "   �  *   �  ,        2  #   Q  #   u     �     �  &   �  A   �  �  !  @   �  ,        2  C   L  7   �  W   �  &      $   G     l     y     �  
   �  0   �     �     �  
          *     ,   C  .   p  -   �  (   �  +   �  S   "     v  *   �  ?   �  A   �  C   ;  B     H   �  T        `  %   }     �     �  5   �  7   �  9   ,  8   f  9   �     �  C   �     5     G     a  "   r     �  "   �  *   �  ,   �     )  #   H  #   l     �     �  &   �  A   �   Abstraktna metoda, ktora sa vola pri kliknuti a stlaceni klavesy Akciove tlacitka, ktore podporuje kalkulacka Bases: :class:`enum.Enum` Bases: :class:`ptr42.components.calculator_button.CalculatorButton` Bases: :class:`sphinx.ext.autodoc.importer._MockObject` Funkcia urcena na vytvaranie novej klavesnice, ktora bude pripojena ku tejto kalkulacke Nastavi klavesnicu ku tejto kalkulacke Nastavi ovladac klavesovych udalosti Odznaci text Oznaci chybny stav kalkulacky Oznaci text v zadanom rozmadzi Parameters Qt tlacitko reprezentujuce tlacitko v kalkulacke Raises Returns Submodules Subpackages Tlacitko reprezentujuce akciu v kalkulacke Tlacitko reprezentujuce funkcie v kalkulacke Tlacitko reprezentujuce konstantu v kalkulacke Tlacitko reprezentujuce operator v kalkulacke Trieda reprezentujuca displej kalkulacky Trieda reprezentujuca klavesnicu kalkulacky Vlozi text na poziciu aktualneho kurzoru, alebo ak je oznaceny text, tak ho nahradi Vrati layout klavesnice Vrati poziciu kurzoru v tvare (start, end) Zaregistruje akciu do kalkulacky a prida tlacitko do kalkulacky Zaregistruje funkciu do kalkulacky a prida tlacitko do kalkulacky Zaregistruje konstantu do kalkulacky a prida tlacitko do kalkulacky Zaregistruje operator do kalkulacky a prida tlacitko do kalkulacky Zaregistruje skrytu akciu do kalkulacky a neprida tlacitko do kalkulacky Zaregistruje skrytu akciu do kalkulacky s inverziou a neprida tlacitko do kalkulacky Zrusi chybny stav kalkulacky abstraktna metoda, musi byt prepisana akcia funkcia pre tlacitko funkcia, ktora sa zavola, ked dojde ku kliku na akciu funkcia, ktora sa zavola, ked dojde ku kliku na funkciu funkcia, ktora sa zavola, ked dojde ku kliku na konstantu funkcia, ktora sa zavola, ked dojde ku kliku na operator klavesnicu bez klaves s napojenymi signalmi na kalkulacku klavesova skratka akcie klavesova skratka akcie (inverzna akcia sa vykona po drzani shiftu) layout klavesnice pocet znakov na oznacenie pociatocny index poziciu zaciatku textu na displeji ptr42.components package ptr42.components.calculator module ptr42.components.calculator\_button module ptr42.components.calculator\_keyboard module ptr42.components.screen module riadok, kde bude umiestene tlacitko stlpec, kde bude umiestene tlacitko text na vlozenie text tlacitka true, ak je na obrazovke oznaceny text tuple so strukturou (start, end), co reprezentuje poziciu kurzoru Project-Id-Version: 42ptr calc 1.0
Report-Msgid-Bugs-To: 
POT-Creation-Date: 2019-04-20 16:03+0200
PO-Revision-Date: YEAR-MO-DA HO:MI+ZONE
Last-Translator: FULL NAME <EMAIL@ADDRESS>
Language: sk_SK
Language-Team: sk_SK <LL@li.org>
Plural-Forms: nplurals=3; plural=((n==1) ? 0 : (n>=2 && n<=4) ? 1 : 2)
MIME-Version: 1.0
Content-Type: text/plain; charset=utf-8
Content-Transfer-Encoding: 8bit
Generated-By: Babel 2.6.0
 Abstraktna metoda, ktora sa vola pri kliknuti a stlaceni klavesy Akciove tlacitka, ktore podporuje kalkulacka Bases: :class:`enum.Enum` Bases: :class:`ptr42.components.calculator_button.CalculatorButton` Bases: :class:`sphinx.ext.autodoc.importer._MockObject` Funkcia urcena na vytvaranie novej klavesnice, ktora bude pripojena ku tejto kalkulacke Nastavi klavesnicu ku tejto kalkulacke Nastavi ovladac klavesovych udalosti Odznaci text Oznaci chybny stav kalkulacky Oznaci text v zadanom rozmadzi Parameters Qt tlacitko reprezentujuce tlacitko v kalkulacke Raises Returns Submodules Subpackages Tlacitko reprezentujuce akciu v kalkulacke Tlacitko reprezentujuce funkcie v kalkulacke Tlacitko reprezentujuce konstantu v kalkulacke Tlacitko reprezentujuce operator v kalkulacke Trieda reprezentujuca displej kalkulacky Trieda reprezentujuca klavesnicu kalkulacky Vlozi text na poziciu aktualneho kurzoru, alebo ak je oznaceny text, tak ho nahradi Vrati layout klavesnice Vrati poziciu kurzoru v tvare (start, end) Zaregistruje akciu do kalkulacky a prida tlacitko do kalkulacky Zaregistruje funkciu do kalkulacky a prida tlacitko do kalkulacky Zaregistruje konstantu do kalkulacky a prida tlacitko do kalkulacky Zaregistruje operator do kalkulacky a prida tlacitko do kalkulacky Zaregistruje skrytu akciu do kalkulacky a neprida tlacitko do kalkulacky Zaregistruje skrytu akciu do kalkulacky s inverziou a neprida tlacitko do kalkulacky Zrusi chybny stav kalkulacky abstraktna metoda, musi byt prepisana akcia funkcia pre tlacitko funkcia, ktora sa zavola, ked dojde ku kliku na akciu funkcia, ktora sa zavola, ked dojde ku kliku na funkciu funkcia, ktora sa zavola, ked dojde ku kliku na konstantu funkcia, ktora sa zavola, ked dojde ku kliku na operator klavesnicu bez klaves s napojenymi signalmi na kalkulacku klavesova skratka akcie klavesova skratka akcie (inverzna akcia sa vykona po drzani shiftu) layout klavesnice pocet znakov na oznacenie pociatocny index poziciu zaciatku textu na displeji ptr42.components package ptr42.components.calculator module ptr42.components.calculator\_button module ptr42.components.calculator\_keyboard module ptr42.components.screen module riadok, kde bude umiestene tlacitko stlpec, kde bude umiestene tlacitko text na vlozenie text tlacitka true, ak je na obrazovke oznaceny text tuple so strukturou (start, end), co reprezentuje poziciu kurzoru 