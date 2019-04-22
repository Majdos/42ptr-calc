====================================
Inštalácia developérskeho prostredia
====================================

.. _našom githube: https://github.com/Majdos/42ptr-calc

Následujúce inštrukcie sa neodporúčaju, ak neplánujete modifikovať zdrojové kódy.
Ak chcete používať len kalkulačku, prosím, nainštalujte si kalkulačku pomocou
inštalátora, ktorý je dostupný na `našom githube`_.

.. warning::
    Tento návod požaduje minimálnu verziu pythonu 3.6

Začíname
========

Naším cieľom je nainštalovať závislosti, bez toho aby kolidovali s ostatnými
verziami už nainštalovaných závislostí.

Najprv než začneme, musíme vytvoriť pythonove virtuálne prostredie. To nám
zaistí, že nedôjde ku kolíziam verzií globálnych závislostí.

Vytvorenie virtualneho prostredia
---------------------------------

Virtuálne prostredie vytvoríme pomocou pythonom príkazom.

``python -m venv venv``

Po spustení príkazu sa nám vytvorí virtuálne prostredie s menom *venv*.

Aktivácia virtuálneho prostredia
-----------------------------------------------

Aktivácia prostredia *venv* záleži na platforme, na ktorej pracujeme.

Windows platforma
^^^^^^^^^^^^^^^^^

``.\venv\Scripts\activate``

Linux platforma
^^^^^^^^^^^^^^^

``source venv/bin/activate``

Instalacia zavislosti
---------------------

Po aktivácii môžeme nainštalovať závislosti.

``make install``

Deaktívacia prostredia
----------------------

Nakoniec, keď sme skončili s prácou na projekte, alebo chceme sa prepnúť do
iného prostredia, môžeme deaktivovať aktuálne prostredie pomocou príkazu.

``deactivate``
