# Subventions


Spécification du modèle de données relatif aux subventions attribuées par une collectivité

- name: subventions
- homepage: https://git.opendatafrance.net/scdl/subventions
- schema URL: https://git.opendatafrance.net/scdl/subventions/raw/v2.0.1/schema.json
- version: 2.0.1
- creation date: 4/26/2018
- last modification date: 6/27/2019
- relates to the country: FR
- missing values represented by: `[""]`
- contributors :
  - OpenDataFrance (author)
  - Pierre Dittgen, Jailbreak (author) [pierre.dittgen@jailbreak.paris](pierre.dittgen@jailbreak.paris)
- resources :
  - Exemple de fichier subventions invalide ([link](https://git.opendatafrance.net/scdl/subventions/raw/v2.0.1/exemples/exemple_invalide.csv))
- sources :
  - Décret n° 2017-779 du 5 mai 2017 relatif à l&#x27;accès sous forme électronique aux données essentielles des conventions de subvention​ ([link](https://www.legifrance.gouv.fr/jo_pdf.do?id=JORFTEXT000034600552))
  - Arrêté du 17 novembre 2017 relatif aux conditions de mises à disposition des données essentielles des conventions de subvention​ ([link](https://www.legifrance.gouv.fr/jo_pdf.do?id=JORFTEXT000036040528))
  - Format réglementaire pour la publication des données essentielles des conventions de subventions sur le dépôt Github de la mission Etalab​ ([link](https://github.com/etalab/format-subventions))

## Data model

This data model relies on the 14 following fields corresponding to the columns of the tabular file.

### `nomAttribuant`

- title: Nom de l'attribuant
- description: Nom officiel de la collectivité attribuant la subvention.
- type: string
- example: `Région Bretagne`
- required value

### `idAttribuant`

- title: Identification de l'attribuant
- description: Identifiant du [Système d'Identification du Répertoire des Etablissements](https://fr.wikipedia.org/wiki/Syst%C3%A8me_d%27identification_du_r%C3%A9pertoire_des_%C3%A9tablissements) (SIRET) de la collectivité attribuant la subvention, composé de 9 chiffres SIREN + 5 chiffres NIC d’un seul tenant.
- type: string
- example: `23350001600040`
- required value
- pattern: `^\d{14}$`

### `dateConvention`

- title: Date de la convention de subvention
- description: Date de la convention au format AAAA-MM-JJ suivant la norme internationale [ISO 8601](https://fr.wikipedia.org/wiki/ISO_8601).
- type: date
- example: `2017-06-27`
- required value

### `referenceDecision`

- title: Référence de la décision
- description: Identifiant interne de l’acte matérialisant la décision d’attribution de la subvention. Sa composition dépend des pratiques propres à la collectivité.
- type: string
- example: `2017-03-103`
- optional value

### `nomBeneficiaire`

- title: Nom du bénéficiaire
- description: Nom officiel ou raison sociale du bénéficiaire de la subvention.
- type: string
- example: `Association Les Petits Débrouillards Bretagne`
- required value

### `idBeneficiaire`

- title: Identification du bénéficiaire
- description: Identifiant du [Système d'Identification du Répertoire des Etablissements](https://fr.wikipedia.org/wiki/Syst%C3%A8me_d%27identification_du_r%C3%A9pertoire_des_%C3%A9tablissements) (SIRET) du bénéficiaire de la subvention, composé de 9 chiffres SIREN + 5 chiffres NIC d’un seul tenant.
- type: string
- example: `38047555800058`
- required value
- pattern: `^\d{14}$`

### `objet`

- title: Objet de la subvention
- description: Description de l'objet de la subvention attribuée limitée à 256 caractères maximum.
- type: string
- example: `Animations climat-énergie dans les lycées de la région`
- required value
- maximal length: 256

### `montant`

- title: Montant total de la subvention
- description: Montant total de la subvention attribuée, exprimé en euros et calculé avant répartition entre les bénéficiaires dans le cas de bénéficaires multiples. Le signe de séparation entre les parties entière et décimale du nombre est le point.
- type: real number
- example: `47800.20`
- required value

### `nature`

- title: Nature de la subvention
- description: Plusieurs choix possibles en combinant les valeurs 'aide en numéraire' et/ou 'aide en nature'. Les valeurs autorisées sont 'aide en numéraire', 'aide en nature', 'aide en numéraire;aide en nature', 'aide en nature;aide en numéraire'. Quand la nature de la subvention est à la fois en numéraire et en nature, le signe de séparation des valeurs est le point-virgule.
- type: string
- example: `aide en numéraire;aide en nature`
- required value
- allowed values: `["aide en numéraire","aide en nature","aide en numéraire;aide en nature","aide en nature;aide en numéraire"]`

### `conditionsVersement`

- title: Conditions de versement de la subvention
- description: Choix unique parmi plusieurs valeurs possibles : 'unique', 'échelonné' ou 'autre'. La valeur 'autre' correspond à une description libre des modalités de versement de la subvention dans la limite de 256 caractères maximum.
- type: string
- example: `échelonné`
- required value
- maximal length: 256

### `datesPeriodeVersement`

- title: Date ou période de versement
- description: Si le versement est unique et que la date précise est connue, alors il s'agit d'une date au format AAAA-MM-JJ suivant la norme internationale [ISO 8601](https://fr.wikipedia.org/wiki/ISO_8601). Si le versement est échelonné (ou que la date précise de versement unique est inconnue), alors il s'agit d'une période exprimée au format AAAA-MM-JJ/AAAA-MM-JJ où le séparateur entre la première et la seconde date de l'intervalle est la barre oblique suivant la norme internationale [ISO 8601](https://fr.wikipedia.org/wiki/ISO_8601).
- type: string
- example: `'2017-03-14' pour une date ou '2017-03-14/2018-03-14' pour une période`
- required value
- pattern: `^[0-9]{4}\-[0-9]{2}\-[0-9]{2}(\/[0-9]{4}\-[0-9]{2}\-[0-9]{2})?$`

### `idRAE`

- title: Identifiant RAE de l’aide au titre de laquelle la subvention est attribuée
- description: Numéro unique de référencement dans le [Répertoire des Aides aux Entreprises](https://aides-entreprises.fr/). Ce champ ne concerne que les subventions attribuées au titre d’une aide référencée dans la [base de données du RAE](https://data.aides-entreprises.fr/documentation) gérée par l'Institut Supérieur des Métiers.
- type: string
- example: `12345`
- optional value
- maximal length: 5

### `notificationUE`

- title: Aide d'Etat notifiée à la Commission Européenne
- description: Subvention attribuée au titre d’une aide de minimis notifiée à la Commission Européenne en vertu des dispositions du règlement n° 1407/2013 du 18 décembre 2013. Seules les valeurs 'oui' ou 'non' sont autorisées.
- type: boolean
- values considered true: oui
- values considered false: non
- example: `non`
- required value

### `pourcentageSubvention`

- title: Pourcentage du montant total de la subvention attribuée au bénéficiaire
- description: Pourcentage exprimé sous la forme d'un nombre décimal. Dans le cas d’un bénéficiaire unique, le pourcentage est 100%, soit '1.00' en nombre décimal. Dans le cas de bénéficiaires multiples, le pourcentage du montant attribué au bénéficiaire correspond à la part qui lui est versée : par exemple 45%, soit '0.45' en nombre décimal. Le signe de séparation entre les parties entière et décimale du nombre est le point.
- type: real number
- example: `0.45`
- required value
- minimal value: 0.01
- maximal value: 1


