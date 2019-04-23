====================================
Inštalácia developérskeho prostredia
====================================

.. _našom githube: https://github.com/Majdos/42ptr-calc

Následujúce inštrukcie sa neodporúčaju, ak neplánujete modifikovať zdrojové kódy.
Ak chcete používať len kalkulačku, prosím, nainštalujte si kalkulačku pomocou
inštalátora, ktorý je dostupný na `našom githube`_.

.. warning::
    Tento návod vyžaduje minimálnu verziu pythonu 3

Začíname
========

Naším cieľom je nainštalovať závislosti, bez toho aby kolidovali s ostatnými
verziami už nainštalovaných závislostí.

Tento projekt využíva na správu závislostí nástroje ako setuptools a pipenv, ktoré si
teraz nainštalujeme.

Inštalácia potrebných nástrojov
---------------------------------

Najprv si nainštalujeme **pipenv** a **setuptools**.

``pip install --user pipenv``

``pip install --user setuptools``


Inštalácia závislosti
---------------------

Na inštaláciu projektových závislosti už je predpripravený script v makefili.
Stačí jednoducho spustiť ``make install``.

Prvé spustenie programu
-----------------------

Predtým než začneme pracovať s programom, musíme skompilovať viacjazyčné preklady pomocou
príkazu:

``make i18_compile``

.. note::
    Túto procedúru je nutné vykonať pri každej zmene prekladu

Akonáhle sa dokončí kompilácia, môžeme spusiť program pomocou príkazu ``make run``.
