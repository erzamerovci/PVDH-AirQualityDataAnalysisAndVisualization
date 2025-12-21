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

Qëllimi i kësaj faze ishte identifikimi i vlerave jonormale (outliers) në të dhënat e ndotjes ajrore, vlerësimi i ndikimit të tyre në cilësinë e të dhënave, si dhe mënjanimi i vlerave ekstreme që mund të ndikojnë në analizat e mëvonshme. Janë përdorur teknika të avancuara statistikore bazuar në zbërthimin STL dhe rezidualet robuste për të identifikuar dhe trajtuar outliers.

### 1. Përpunimi fillestar i të dhënave kohore
Para detektimit të përjashtuesve, është bërë përpunimi specifik për seritë kohore:

- Të dhënat u organizuan sipas stacioneve dhe orëve
- U verifikua vazhdimësia e të dhënave për secilin stacion
- U vlerësuan modelet sezonale ditore të çdo ndotësi


### 2. Zbërthimi STL dhe llogaritja e Z-Rezidualeve robuste
Për secilin ndotës (PM10, PM2.5, NO2, O3) dhe për secilin stacion veç e veç, u aplikua metoda STL (Seasonal-Trend decomposition using LOESS):

Zbërthimi i serive kohore: 
Çdo seri u nda në tre komponentë:

- Komponenti sezonal (ciklet ditore 24-orëshe)
- Komponenti trend (ndryshimet afatgjata)
- Rezidualet (devijimet)

Llogaritja e z-rezidualeve robuste: Në vend të z-score standardë (që përdorin mesataren dhe devijimin standard), u përdorën statistika robuste:

- Mesorja (median) në vend të mesatares
- MAD (Median Absolute Deviation) në vend të devijimit standard
- Faktori i shkallëzimit 1.4826 për krahasim me shpërndarjen normale

### 3. Vendosja e thresholds dhe gjetja e outliers
Për shkak të natyrës së të dhënave të ndotjes ajrore (shpërndarje të paqëndrueshme), u përcaktuan pragje të larta për çdo ndotës:

- PM10: |Z| > 15.0
- PM2.5: |Z| > 12.0
- NO2: |Z| > 10.0
- O3: |Z| > 8.0

Këto pragje të larta janë të nevojshme sepse:

Pas heqjes së modeleve sezonale dhe trendeve, rezidualet janë shumë më të vogla.
Metoda jonë është më e ndjeshme se metodat standarde.
Pragu |Z| > 15 në metodën tonë është i barabartë me |Z| > 3 në metodat tradicionale.

#### 3.1 Rezultatet e detektimit të outliers

- Numri i outliers për çdo ndotës

<img width="1724" height="638" alt="image" src="https://github.com/user-attachments/assets/8be18b80-5a82-4bed-9189-cb45017f884a" />

- Mesataret e outliers dhe non-outliers

<img width="1824" height="568" alt="image" src="https://github.com/user-attachments/assets/978a6d31-b368-4ac1-8267-7e1df0ae6879" />

<img width="1838" height="222" alt="image" src="https://github.com/user-attachments/assets/2a931177-e807-4d1c-8a50-4e9f7272c009" />

- Statistika të pastrimit të dataset-it (rows removed, columns kept)

<img width="1838" height="222" alt="image" src="https://github.com/user-attachments/assets/26269541-31c3-4044-82ee-9625ab9afd85" />


### 4. Analiza e karakteristikave unike të metodës
Metoda e implementuar ka këto avantazhe unike:

Stacion-për-stacion: Çdo stacion analizohet veçmas, duke respektuar niveli bazë unik të secilit
Varësia nga ora e ditës: Merret parasysh se në orët e pikut të trafikut, ndotja është normalisht më e lartë
Varësia nga stina: Merret parasysh ndikimi i stinëve në nivelet e ndotjes
Detektim orar, jo ditor: Identifikohen luhatje të shkurtra 1-6 orëshe që mesatarja ditore mund t'i humbasë

Shembull praktik: Një vlerë PM2.5 prej 30 μg/m³ mund të jetë:

Përjashtues ekstrem në një stacion rural (normalja: 5-15 μg/m³)
Vlerë normale në një stacion urban (normalja: 20-40 μg/m³)
Vlerë e ulët në një zonë industriale (normalja: 30-60 μg/m³)

<img width="1768" height="1294" alt="image" src="https://github.com/user-attachments/assets/8a2676b2-f40c-4339-a4ae-56e80f87dfb3" />

Konkluzioni: Dataset-i i pastruar është tani më i besueshëm për analiza të mëtejshme, duke eliminuar ngjarjet ekstreme që nuk përfaqësojnë sjelljen tipike të secilit stacion, duke ruajtur në të njëjtën kohë vlerat e larta që janë pjesë e profileve normale të ndotjes së secilit lokacion. Kjo qasje e sofistikuar siguron që "outlier"-ët e vërtetë (ngjarjet jashtëzakonisht të pazakonta) ndahen nga vlerat e larta por të zakonshme për zonat e ndryshme.

## Faza e tretë – Vizualizimi dhe analiza interaktive e të dhënave

Kjo fazë përfaqëson fazën finale të projektit dhe fokusohet në vizualizimin interaktiv dhe interpretimin analitik të të dhënave të pastruara, me qëllim nxjerrjen e njohurive domethënëse mbi cilësinë e ajrit dhe faktorët që ndikojnë në të. Të dhënat e përpunuara gjatë fazës së parë dhe të dytë u shfrytëzuan për ndërtimin e një dashboard-i interaktiv, i cili mundëson eksplorim dinamik të të dhënave në dimensione kohore, hapësinore dhe sezonale.

Vizualizimet janë ndërtuar duke përdorur mjete të avancuara për Business Intelligence (p.sh. Power BI), dhe janë të organizuara në tre blloqe kryesore analitike, siç përshkruhet më poshtë.

### 1.  Analiza mujore dhe ditore sipas stacioneve

<img width="1287" height="728" alt="Screenshot_2025-12-21_200034" src="https://github.com/user-attachments/assets/34c20876-b999-4266-ad4e-ef40e8a578cc" />


#### Qëllimi:
Ky vizualizim synon analizimin e cilësisë së ajrit në nivel mujor dhe ditor, duke ofruar mundësinë e krahasimit të një ose më shumë stacioneve monitoruese për ndotës të ndryshëm.

#### Përshkrimi:

- Grafiku kryesor paraqet mesataren ditore të PM2.5 (me mundësi kalimi në PM10) për një muaj të zgjedhur.

- Filtrat interaktivë lejojnë:

    - përzgjedhjen e muajit dhe intervalit kohor,

    - përzgjedhjen e një ose disa stacioneve për krahasim.

- Në anën e majtë shfaqen kartat përmbledhëse me vlerat mesatare mujore për:

    - PM2.5

    - PM10

    - NO2

    - O3

- Grafiku horizontal në të djathtë paraqet krahasimin e ndotësve sipas stacioneve të zgjedhura.

#### Vlera analitike:
Ky vizualizim mundëson identifikimin e:

- ndryshimeve ditore të ndotjes brenda një muaji,

- dallimeve mes stacioneve urbane dhe periferike,

- periudhave me rritje apo ulje të theksuar të ndotjes.

### 2. Analiza sezonale dhe krahasimi mes stacioneve

<img width="1254" height="688" alt="Screenshot_2025-12-21_200336" src="https://github.com/user-attachments/assets/555950a8-1d6a-4f16-9c57-151b133fa91e" />


#### Qëllimi:
Ky vizualizim fokusohet në analizimin e ndryshimeve sezonale të ndotësve të ajrit, duke krahasuar stacionet e përzgjedhura përgjatë katër stinëve të vitit.

#### Përshkrimi:

- Grafikët me shtylla janë të ndarë sipas stinëve:

    - Dimër

    - Pranverë

    - Verë

    - Vjeshtë

- Për secilën stinë paraqiten vlerat mesatare të:

    - PM2.5

    - PM10

    - NO2

    - O3

- Donut chart ofron një pamje përmbledhëse të përqindjes së ndotësve sipas stinëve, duke lehtësuar krahasimin vizual.

#### Vlera analitike:

- Evidentohet rritja e O3 gjatë stinës së verës, si pasojë e temperaturave më të larta dhe rrezatimit diellor.

- PM2.5 dhe PM10 shfaqin vlera më të larta gjatë dimrit dhe vjeshtës, të lidhura me ngrohjen dhe kushtet atmosferike.

- Vizualizimi ndihmon në kuptimin e modeleve sezonale të ndotjes.

### 3. Ndërlidhja mes O3 dhe temperaturës në kohë

<img width="1249" height="680" alt="Screenshot_2025-12-21_200434" src="https://github.com/user-attachments/assets/c0abd24e-b705-4e71-87ac-959fad830ea1" />


#### Qëllimi:
Ky vizualizim analizon marrëdhënien ndërmjet temperaturës mesatare dhe nivelit të ozonit (O3), si dhe evoluimin e tyre në kohë.

#### Përshkrimi:

- Scatter plot paraqet:

    - boshtin horizontal: temperaturën mesatare,

    - boshtin vertikal: vlerën mesatare të O3.

- Pikat janë të ngjyrosura sipas stinëve, duke mundësuar dallimin sezonal.

- Slider-i kohor lejon eksplorimin e të dhënave në bazë mujore dhe shumëvjeçare.

#### Vlera analitike:

- Vërehet një korrelacion pozitiv mes temperaturës dhe nivelit të O3.

- Me kalimin e viteve, vlerat e O3 shfaqin një trend rritës, veçanërisht gjatë muajve të verës.

- Ky trend sugjeron ndikimin e ndryshimeve klimatike dhe ngrohjes globale në rritjen e ozonit në shtresën e poshtme të atmosferës.

### 4. Harta gjeografike e stacioneve monitoruese

<img width="1232" height="670" alt="Screenshot_2025-12-21_200458" src="https://github.com/user-attachments/assets/b688492c-ca31-4732-a569-5b093a90db1e" />


#### Qëllimi:
Ky vizualizim ka për qëllim paraqitjen e shpërndarjes gjeografike të stacioneve monitoruese të cilësisë së ajrit, duke ofruar një kontekst hapësinor për analizat e realizuara në vizualizimet e tjera.

#### Përshkrimi:

- Vizualizimi paraqitet në formën e një harte interaktive, ku çdo pikë përfaqëson një stacion matës.

- Pozicioni i stacioneve bazohet në koordinatat gjeografike (latitude dhe longitude) të dataset-it.

- Harta mundëson:

    - identifikimin vizual të lokacionit të secilit stacion,

    - dallimin mes stacioneve urbane, periferike dhe rurale,

    - përzgjedhjen e stacioneve për analiza të mëtejshme në dashboard.

#### Vlera analitike:

- Ofron një pasqyrë hapësinore të rrjetit të monitorimit të cilësisë së ajrit.

- Ndihmon në interpretimin e dallimeve mes stacioneve duke i lidhur ato me:

    - dendësinë urbane,

    - afërsinë me trafikun apo zonat industriale,

    - karakteristikat gjeografike të zonës.

- Shërben si element orientues për përdoruesin dhe si pikënisje për analizat kohore dhe sezonale.

### Përfundim i Fazës së tretë

Faza e tretë konfirmon rëndësinë e vizualizimit interaktiv si mjet analitik për:

- kuptimin e sjelljes së ndotësve në kohë dhe hapësirë,

- identifikimin e modeleve sezonale,

- analizimin e lidhjes mes faktorëve klimatikë dhe cilësisë së ajrit.

Kombinimi i analizës statistikore nga fazat paraprake me vizualizime interaktive siguron një qasjë të plotë dhe të besueshme analitike, duke e bërë dataset-in të përshtatshëm për studime të avancuara dhe vendimmarrje të bazuar në të dhëna.


## Authors
- *Erza Merovci*
- *Fortesa Cena*
- *Melos Ymeri*
