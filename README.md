<table border="0">
 <tr>
    <td style="width:300px; vertical-align:middle; text-align:center;">
      <img src="https://upload.wikimedia.org/wikipedia/commons/e/e1/University_of_Prishtina_logo.svg" 
           alt="University Logo" 
           style="width:250px; height:auto;" />
    </td>
    <td style="vertical-align:middle; padding-left:20px;">
      <h2><strong>Universiteti i Prishtinës</strong></h2>
      <h3>Fakulteti i Inxhinierisë Elektrike dhe Kompjuterike</h3>
      <p>Inxhinieri Kompjuterike dhe Softuerike - Programi Master</p>
      <p><strong>Profesor:</strong> Dr.Sc. Mërgim H. HOTI</p>
    </td>
 </tr>
</table>



## Përshkrim i përgjithësuar i projektit
Ky projekt realizohet në kuadër të lëndës “Përgatitja dhe Vizualizimi i të Dhënave” në vitin akademik 2025/26. Qëllimi i tij është përgatitja, pastrimi, analiza dhe vizualizimi i të dhënave duke ndjekur faza të strukturuara pune. Projekti përfshin para-procesimin e të dhënave (mbledhjen, integrimin, pastrimin dhe transformimin e tyre), detektimin dhe trajtimin e të dhënave përjashtuese, si dhe vizualizimin statik dhe interaktiv përmes softuerëve të specializuar si PowerBI, Tableau apo Qlik Sense.

## Përzgjedhja e Dataset-it
Ne kemi zgjedhur dataset-in "Regional Datasets for Air Quality Monitoring in European Cities (2020–2023)" duke e fokusuar projektin në domenin e Cilësisë së Ajrit. Ky set i të dhënave shërben si bazë e përsosur për të adresuar të gjitha kërkesat e lëndës PVDH, pasi natyra e tij si Seri Kohore Multivariante kërkon aplikimin e gjerë të teknikave të para-procesimit, analizës dhe vizualizimit.

| Atributi | Detaji |
| :--- | :--- |
| **Emri i Dataset-it** | Regional Datasets for Air Quality Monitoring in European Cities (2020–2023) |
| **Burimi** | Zenodo |
| **Linku** | `https://zenodo.org/records/11220965` |
| **Përmbledhje** | Set i të dhënave të mbledhura nga stacionet monitoruese të cilësisë së ajrit në disa qytete evropiane, duke mbuluar periudhën nga viti 2020 deri në vitin 2023. |

## Faza e parë - Para-procesimi i të dhënave 

Në këtë fazë, qëllimi është përgatitja e të dhënave në mënyrë që të jenë të përshtatshme për analizë dhe vizualizim. Procesi përfshin mbledhjen, vlerësimin dhe pastrimin e të dhënave, si dhe organizimin e tyre në një formë të strukturuar. Aty ku është e nevojshme, bëhen transformime, përzgjedhje të karakteristikave kryesore dhe thjeshtime për të lehtësuar analizat e mëvonshme.

*Rezultati përfundimtar është një dataset i  pastër dhe i gatshëm për përdorim në fazën e dytë të projektit.*

Hapat e fazes se pare:

1. Identifikimi i Tipeve të të Dhënave

U analizua struktura e dataset-it për të përcaktuar llojin e të dhënave për secilën kolonë.
<img width="452" height="549" alt="image" src="https://github.com/user-attachments/assets/b34be36b-948f-46a7-b9f0-5c0c4f1877a1" />


2. Zbulimi i Vlerave Mungese (NULL)

Për çdo kolonë u llogarit përqindja e vlerave mungese për të vendosur metodën e duhur të pastrimit.
<img width="434" height="477" alt="image" src="https://github.com/user-attachments/assets/92868d13-ea86-46a8-a241-4a664af5f26e" />


3. Trajtimi i Vlerave Mungese

U përdorën disa teknika për eliminimin e vlerave NULL:
Forward filling
Interpolim i bazuar në korelacion
Mesatarja ndërmjet vlerës paraprake dhe asaj pasuese

Pas zbatimit të këtyre metodave, dataset-i nuk përmban më asnjë vlerë "NULL".

<img width="312" height="467" alt="image" src="https://github.com/user-attachments/assets/dcfa5955-08e9-4153-bb76-d3e933a0feb2" />


4. Diskretizimi i Kolonave PM2.5 dhe PM10

Janë krijuar dy kolona të reja që kategorizojnë nivelin e ndotjes së ajrit bazuar në vlerat e PM2.5 dhe PM10.
<img width="281" height="593" alt="image" src="https://github.com/user-attachments/assets/55917fc4-6632-497f-ba2c-a53ab1db519a" />


5. Binarizimi i Temperaturës

Është krijuar kolona Temp. binary:
0 → temperaturë nën 15°C
1 → temperaturë mbi 15°C

Kjo thjeshton analizat që kërkojnë vlera të kategorizuara.

<img width="186" height="640" alt="image" src="https://github.com/user-attachments/assets/3bbc1bf8-c0fc-4a72-8e27-380eee45f831" />

## Faza e dytë – Detektimi i përjashtuesve dhe mënjanimi

Qëllimi i kësaj faze është identifikimi i vlerave jonormale (outliers), vlerësimi i ndikimit të tyre në cilësinë e të dhënave, si dhe mënjanimi i vlerave të pasakta që mund të deformojnë analizat e mëvonshme. Janë përdorur teknika statistikore si z-residuals dhe identifikimi i pragjeve për të shënuar dhe trajtuar përjashtuesit në mënyrë të kontrolluar.

1. Eksplorimi fillestar i të dhënave

Para detektimit të përjashtuesve, u krye një inspektim fillestar i të dhënave:

- U vëzhguan vlerat ekstreme të ndotësve

- U kontrollua konsistenca e vlerave pas pastrimit të Fazës I

- U identifikuan ditët me sjellje të dyshimtë që kërkonin hetim të mëtejshëm

- U vlerësua rregullsia e serisë kohore për secilin ndotës


2. Llogaritja e Z-Residuals për identifikimin e përjashtuesve

Për secilin ndotës (PM10, PM2.5, NO2, O3) u llogaritën z-residuals, të cilat matin devijimin e vlerës nga sjellja e pritur statistikore.

- Vlerat shumë të mëdha → rritje jonormale

- Vlerat shumë të ulëta → rënie jonormale

Shërbejnë si bazë për detektimin e vlerave të dyshimta

Rezultati:
Ditët me devijime ekstreme identifikohen qartë dhe kategorizohen si përjashtues të mundshëm.

3. Vendosja e thresholds dhe shënimi i përjashtuesve

- U aplikua metoda two-sided thresholding, ku për çdo ndotës definohen kufij statistikorë:

- Vlerat jashtë intervalit të lejuar shënohen automatikisht si përjashtues

- Janë krijuar kolonat _outlier_two_sided për çdo ndotës

- Secila vlerë etiketohet True (përjashtues) ose False (normale)


4. Analiza e shpërndarjes së përjashtuesve

- Është analizuar sasia dhe shpërndarja e përjashtuesve në nivel ndotësi dhe stacioni:

- Numri i përjashtuesve për çdo ndotës

- Identifikimi i ditëve me devijime të shpeshta

Krahasimi i stacioneve për të parë cilat kanë më shumë vlera jonormale

<img width="1591" height="663" alt="image" src="https://github.com/user-attachments/assets/80f1a060-6c5d-4910-acca-94c51bde47bd" />


5. Mënjanimi i zbulimeve jo të sakta

Bazuar në përjashtuesit e identifikuar:

- U shqyrtuan ditët me vlera të dyshimta

- U larguan vlerat e pasakta që komprometonin analizën

Dataset-i u ristrukturua për të ruajtur integritetin e tij statistikor

<img width="591" height="484" alt="image" src="https://github.com/user-attachments/assets/9410f54a-08e7-4a2d-96c8-53afdcebc2e3" />

<img width="1036" height="727" alt="image" src="https://github.com/user-attachments/assets/ba4f64a3-08b5-480b-a435-5a1be3a3dedb" />



Rezultati:
Dataset-i është më i pastër, i qëndrueshëm dhe i gatshëm për fazën e III.



## Authors
- *Erza Merovci*
- *Fortesa Cena*
- *Melos Ymeri*
