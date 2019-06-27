---
layout: post
title: Algoritmy pro život
description: Poznámky ke knize Algoritmy pro život od Briana Christiana a Toma Griffithse
author: Petr Lorenc
comments: true
---

Poznámky ke knize **Algoritmy pro život od Briana Christiana a Toma Griffithse**, která, už podle názvu, nemohla více vzbuzovat dojem asociálního čtenáře. Já ze z knihy dozvěděl mnoho praktických uplatnění algoritmů, které jsem znal díky studiu na FIT ČVUT ale **doporučil bych ji i netechnické části populace.** I když mírná znalost tématu by určitě nebyla na škodu.

# Algoritmy pro život

  * Napsal **Brian Christian a Tom Griffiths**
  * Anglický název **Algorithm to Live By**
  * <a href="https://www.databazeknih.cz/knihy/algoritmy-pro-zivot-354348">**Link**</a>

<figure class="image" align="middle">
  <a href="{{ site.baseurl }}/images/Books/algprozivot.png" data-title="Algoritmy pro život" data-lightbox="roadtrip">
    <img src="{{ site.baseurl }}/images/Books/algprozivot.png" alt="Algoritmy pro život" title="Algoritmy pro život"/>
    <figcaption>Algoritmy pro život</figcaption>
  </a>
</figure>

## Obsah

  * Problém s <a href="https://en.wikipedia.org/wiki/Secretary_problem">výběrem sekretářky</a>, který se dá, mimojiné, aplikovat i na hledání <a href="https://plus.maths.org/content/mathematical-dating">životního partnera</a>. Aneb pokud se nechcete vázat a hledáte pro to výmluvu (a za předpokladu, že vám neni více než 26 let)
    * Strategie **Nejřív hledej, potom jednej** (tj. 37 procent času/případů/pokusů zkoušet možnosti a pak vzít první, která je lepší než všechny předchozí) = **nejlepší možná strategie, která bohužel vede limitně k pouze 37 procentní úspěšnosti** výběru opravdu té nejlepší možnosti, tj. na 63 procent vám ve fázi hledání uteče ta celkově opravdu nejlepší možnost

<figure class="image" align="middle">
  <a href="{{ site.baseurl }}/images/Books/algprozivot2.png" data-title="Algoritmy pro život" data-lightbox="roadtrip">
    <img src="{{ site.baseurl }}/images/Books/algprozivot2.png" alt="Algoritmy pro život" title="Algoritmy pro život - Gittinsův index"/>
    <figcaption>Algoritmy pro život - Gittinsův index</figcaption>
  </a>
</figure>

  * <a href="https://en.wikipedia.org/wiki/Gittins_index">**Gittinsův index**</a> - lze použít v rozhodování jestli námy testovaný algoritmus stojí, za to abychom z něho vytěžili maximum (a obětovali třeba čas/peníze) na úkor prohledávání dalších možných algoritmů, které by mohli do důsledku být lepší

  * **Optimismus je z dlouhodobého hlediska nejlepší strategií proti výčitkám.** Měly bychom zkoušet nové věci a předpokládat v nich to nejlepší, pokud tedy nemáme důkazy o opaku (někdy ani 2-3 negativní zkušenosti nejsou dost pro zavrhnutí)

  * <a href="https://en.wikipedia.org/wiki/Zelen%27s_design">Zelenův algoritmus</a> - **pro volbu léčby pacienta, bez předchozích znalostí o úspěšnosti.** Máme 2 míčky (o dvou barvách pro dvě možné léčby) v kloubouku - jeden vytáhneme a jeho barva určí typ léčby. Míček vrátíme a pokud byla léčba úspěšná přidáme míček téže barvy. Pokud neúspěšná, vložíme míček druhé barvy.


  * <a href="https://en.wikipedia.org/wiki/Forgetting_curve">Ebbinghaussova křivka zapomínání</a> - získána pokusy s vybavováním určitých písmen
    * Staří lidé mají méně přátel cíleně - více pozornosti na méně lidí vede k menším výpadkům cache
    * **Mozek jako procesor s mezipamětí** - důvod proč trvá déle vybavit si věci které jsme dlouho nepoužívali a také proč starším lidem trvá toho vybavení ještě častěji (z důvodu většího celkového objemu dat, tj. spíše nějaká informace nebude v mezipaměti)

<figure class="image" align="middle">
  <a href="{{ site.baseurl }}/images/Books/algprozivot3.png" data-title="Algoritmy pro život" data-lightbox="roadtrip">
    <img src="{{ site.baseurl }}/images/Books/algprozivot3.png" alt="Algoritmy pro život" title="Algoritmy pro život - Ebbinghaussova křivka zapomínání"/>
    <figcaption>Algoritmy pro život - Ebbinghaussova křivka zapomínání</figcaption>
  </a>
</figure>


  * <a href="https://en.wikipedia.org/wiki/J._Richard_Gott#Copernicus_method_and_Doomsday_theory">Koperníkův princip</a> formulovaný Richardem Gottem
    * **Pokud o nějaké události/veličině nemáme žádnou informaci je nejlepší předpokládat, že jsem v polovině trvání (u události) nebo že jsem našli polovinu možných výskytů (u veličiny)**
    * Pokud přijdu k Berlínské zďi, která byla postavena před 8 lety a já nemám žádnou další informaci. Je raciolnální předpokládat, že bude ještě dalších 8 let stát
<figure class="image" align="middle">
  <a href="{{ site.baseurl }}/images/Books/algprozivot4_1.jpeg" data-title="Algoritmy pro život" data-lightbox="roadtrip">
    <img src="{{ site.baseurl }}/images/Books/algprozivot4_1.jpeg" alt="Algoritmy pro život" title="Algoritmy pro život - Koperníkův princip"/>
    <figcaption>Algoritmy pro život - Koperníkův princip</figcaption>
  </a>
</figure>

<figure class="image" align="middle">
  <a href="{{ site.baseurl }}/images/Books/algprozivot4_2.png" data-title="Algoritmy pro život" data-lightbox="roadtrip">
    <img src="{{ site.baseurl }}/images/Books/algprozivot4_2.png" alt="Algoritmy pro život" title="Algoritmy pro život - Koperníkův princip"/>
    <figcaption>Algoritmy pro život - Koperníkův princip</figcaption>
  </a>
</figure>



  * Pozor na overfitting (přeučení) <a href="https://www.quora.com/What-are-some-examples-in-everyday-life-analogous-to-overfitting-in-machine-learning">v reálném životě</a> - případy, kdy policisté byli ze střelnice tak "přeučeni", že začli sbírat patrony v době kdy protivník ještě nebyl zpasifikován se občas objevují

  * LRU cache (Least Recently Used cache) - lze ji **využívat v knihovnách, kde by mohla být sekce s nedávno navrácenými knihami.** Je větší pravděpodobnost, že pokud si někdo knihu v nedávné době půjčil, půjčí si ji někdo v nejbližší době znova (tj. je momentálně populární)
    * Bohužel, **moje domněnka je**, že při množství knížek v moderních knihovnách je úspora zanedbatelná

  * **V raných fázích** návrhu používat **tlustý štetec** (vyšší míru abstrakce)


  * <a href="https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test">Rabin-Millerův test prvočíselnosti</a> 
    * Millerův test určuji jestli je číslo prvočíslo na základě splění určitých podmínek - bohužel mnoho False Positive
    * Rabin-Millerův test nám dává svědky prvočíselnosti, kteří snížují pravděpodobnost False Positive (každý svědek sníží pravděpodobnost FP o čtvrtinu)

  * <a href="https://en.wikipedia.org/wiki/Additive_increase/multiplicative_decrease">AIMD</a> - Aditivní nárust, multiplikativní úbytek = prevence zahlcení fronty

  * Používání zpětné vazby v řeči (slova jako "hmm", "aha"), které zároveň nepřeruší mluvčího, se anglicky nazývá <a href="https://en.wikipedia.org/wiki/Backchannel_(linguistics)">**backchannel**</a> a lze to připodobnit k posilání paketů na internetu o tom, že spojení stále trvá. Tento způsob konfirmace pozornosti **je velice důležitý jak pro mluvčího, tak pro servery.**

## Citáty

  * **Užijte is odpoledne. S sebou si ho nevezmete.**
    * Annie Dillardová

  * **Když se ocitnente na straně většiny, je na čase zastavit a zamyslet se.**
    * Mark Twain