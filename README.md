# bank-match-ambiguity

## Français

Trouver toutes les correspondances bancaires bornées possibles.

Données fictives ; aucun accès réseau ni secret requis.

```sh
python -m bank_match_ambiguity examples/demo.json --lang fr
python -m unittest discover -s tests -v
```

### Méthode et différence

Recherche exacte bornée de sous-ensembles puis affectations disjointes entre paiements ; montre plusieurs explications compatibles au lieu de prendre la première somme trouvée.

### Limites

Même devise, paiements de factures entières sans frais ni versement partiel ; preuve d’unicité limitée à l’ensemble candidat. Arrêt200000 nœuds déclaré incomplet.

### Validation

Tests de domaine, cas limites et interface FR/EN/ES. La CI teste Python 3.11/3.13 et exécute la wheel installée hors du checkout. JSON conserve les identifiants techniques et les données fournis. Erreur d’entrée : code de sortie 2.

## English

Find every bounded possible bank matching.

Synthetic data; no network access or secret required.

```sh
python -m bank_match_ambiguity examples/demo.json --lang en
python -m unittest discover -s tests -v
```

### Method and difference

Bounded exact subset search then disjoint assignments across payments; shows multiple compatible explanations instead of accepting the first matching sum.

### Limits

Same currency, whole-invoice payments without fees or partial settlement; uniqueness limited to candidate set.200000-node cutoff explicitly incomplete.

### Validation

Domain tests, boundary cases and FR/EN/ES interface. CI tests Python 3.11/3.13 and runs the installed wheel outside the checkout. JSON preserves technical identifiers and supplied data. Invalid input exits with code 2.

## Español

Encontrar todas las conciliaciones bancarias posibles acotadas.

Datos sintéticos; no requiere red ni secretos.

```sh
python -m bank_match_ambiguity examples/demo.json --lang es
python -m unittest discover -s tests -v
```

### Método y diferencia

Búsqueda exacta acotada de subconjuntos y asignaciones disjuntas entre pagos; muestra varias explicaciones compatibles sin aceptar la primera suma.

### Límites

Misma moneda, facturas completas sin comisiones ni pagos parciales; unicidad limitada a candidatos. Corte200000 nodos explícitamente incompleto.

### Validación

Pruebas de dominio, casos límite e interfaz FR/EN/ES. CI prueba Python 3.11/3.13 y ejecuta la wheel instalada fuera del repositorio. JSON conserva identificadores técnicos y datos proporcionados. Entrada inválida termina con código 2.

## Sources / Fuentes

- https://docs.peppol.eu/poacc/billing/3.0/bis/#_payment
