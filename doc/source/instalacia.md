# Instalacia

Nasledovne instrukcie sa mozu pocas vyvoja projektu zmenit.

## Najednoduchsia varianta (najmenej odporucana)

`cd ./src && make install`

## Varianta s virtulnym python prostredim

<small style="color: #777">Detailne informacie ohladom python venv najdete na [wiki Arch Linuxu](https://wiki.archlinux.org/index.php/Python/Virtual_environment)</small>.

Virtualne prostredie sluzi na lahsiu spravu nainstalovanych balikov pre projekty. Princip spociva v tom,
ze kazdy projekt ma svoje vlastne prostredie. Vyhoda je nasledovna ... keby sme baliky instalovali **globalne**,
postupom casu by sa nam **zacali krizit verzie balikov**. Napriklad, predstavme si, ze spravujeme 5 Django projektov, co
je web framework pre python. Ak by sme sa rozhodli aktualizovat nejaky projekt z verzie 1.0.0 na 2.0.0 a robili by
sme to na globalnom meritku, doslo by ku kolizii verzii, teda ku strate programovacieho casu.

### Vytvorenie virtualneho prostredia

Najprv musime vytvorit virtualne prostredie (nachadzame sa v rootovskom priecinku projektu).

`python -m venv venv`

### Aktivacia virtualneho prostredia (zalezi na OS)

#### Windows

`.\venv\Scripts\activate`

#### Linux

`source venv/bin/activate`

#### Pomocou utility virtualenv (najjednoduchsia moznost)

Ak sa vam da, pouzite tento postup

`virtualenv venv`

### Instalacia zavislosti

Nainstalujeme zavislosti(dependencies).

`cd src && make install`

### Deaktivacia prostredia

Nakoniec, po praci mozeme deaktivovat prostredie pomocou prikazu.

`deactivate`

## Vyvoj pomocou Docker kontajnera (nepodporovane)

TODO - Momentalne je problem, ze Docker na Windowse nedokaze vytvarat symlinky. Mozno sa pozriem na Vagrant.
