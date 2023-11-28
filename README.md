# Projet Inteprète

Le projet permet d'interpréter du code écrit dans un langage de programmation que nous avons inventé. Dans l'ensemble, les fonctionnalités du langage sont plûtot limitées, mais elles suffisent à écrire des algorithmes classiques sur les entiers. Des programmes d'exemples sont disponibles.

# Structure

Le projet se décompose en trois fichiers (en réalité deux), `main.py` est le fichier principal. `lexique.py` permet de convertir un programme écrit dans un fichier texte en un langage symbolique, plus simple à intepréter. Enfin, `intepreteur.py` permet de correctement exécuter le code écrit dans le langage symbolique.

# Utilisation

`python main.py <programme>`

# Le langage de programmation

## Généralités

- Toutes les variables sont des **entiers relatifs**.
- Les **opérations disponibles** sont l'addition, la multiplication, la division, la soustraction. On peut également comparer deux entiers afin de déterminer s'ils sont égaux, ou si l'un est supérieur à l'autre et inversement.
- Les **structures de contrôle** disponibles sont les structures alternatives ("les `if`"), ainsi que les "boucles `while`".
- Il n'y a **pas** de **priorités opératoires**, les opérations sont lues de gauche à droite. Par exemple, la chaîne de caractères `125+532*32-241*3` sera évaluée comme `(((125+532)*32)-241)*3`.
- Voici la liste de noms de variables invalides (même en tant que préfixes) (car utilisés comme mots-clés): `func`, `output`, `input`, `\d*while`, `\d*if`, `\d*endi`, `\d*endw`, `\d*endf`, `rval`, `arg\d+`, `endf`
- Une **fonction** peut retourner ou non une valeur. Si aucune valeur n'est retournée par une fonction, par défaut on considère que la valeur retournée est la dernière valeur retournée par une fonction.
- Une fonction **ne peut être définie** dans une fonction.
- Une fonction **peut** en **appeler d'autres** (et cela inclus le cas où elle s'appelle elle-même).
- Une fonction ne peut avoir accès qu'à ses variables locales (et ses arguments).
- Il est possible d'**écrire** des nombres en **sortie**, et de prendre des nombres en **entrée**.
- L'indentation n'est pas prise en compte, et une instruction se termine à la fin d'une ligne.

## Syntaxe

- Une **variable** est définie à l'aide du symbole `:`. Par exemple `var:500` créé une nouvelle variable `var` et lui assigne la valeur 500. On peut assigner à une variable une valeur issue d'un calcul. Par exemple, `var2:var+2` donne la valeur de la somme de `var` et 2 à `var2` (donc 502).
- Une **opération arithmétique** doit être écrite **sans** parenthèses.
- Les **opérateurs mathématiques** sont +, *, /, - avec leur sens usuel.
- Les **opérateurs de comparaison** sont >, < et = avec leur sens usuel.
- Lorsqu'un mot clé est utilisé, il doit être suivi d'**un** seul espace. De même s'il a plusieurs arguments, ils doivent être espacés d'**un** seul espace.
- L'instruction `output` permet d'**écrire en sortie** le résultat de l'évaluation de l'opération arithmétique qui le suit. Par exemple `output 52+13` permet d'afficher `65` en sortie.
- L'instruction `input` permet à l'utilisateur **d'entrer un nombre**. Ce nombre sera retourné par input. Par exemple `a:65+input` va assigner à `a` la somme de 65 et le nombre entré par l'utilisateur.
- Une **condition** (resp. une boucle) commence par le mot clé `if` (resp. `while`). Ce qui suit le mot clé sera considéré comme une opération à évaluer. Si elle est évaluée, alors tout ce qui suit jusqu'au mot clé `endi` (resp. `endw`) sera exécuté. Lorsque plusieurs `if` (ou `while`) sont **imbriqués**, il est nécessaire de les **préfixer** par un nombre. Par exemple:
    ```
    if var1>5
        while var2<10
            1if var2 > 6
                var1:var1-1
                2if var1<10
                    var2:var2-1
                2endi
            1endi
        endw
    endif

    ```
    est une définition valide (d'une boucle très potentiellement infine).
- Une **fonction** est définie par le mot-clé `func`. Le mot clé est suivi du nom de la fonction, puis du nombre d'arguments qu'elle prend. Les arguments ne sont pas nommés, mais prennent les noms par défaut `arg0`, suivi de `arg1` et ainsi de suite. Elle peut retourner une valeur avec le mot clé `return`. Elle se termine par le mot clé `endf`. Par exemple, voici une définition de fonction valide: 
    ```
    func add 2
        return arg0+arg1
    endf
    ```
- Pour **appeler** une fonction, on utilise le mot-clé `call` suivi du nom de la fonction puis de ses arguments (séparés par des espaces).
- Après l'**exécution** d'une fonction, son résultat est stocké dans la **variable globale** reservée `rval`.

Pour tester votre compréhension du langage, voici un programme d'exemple:
```
func mystere 1
    x:1
    y:0
    while x < arg0
        x:x*2
        y:y+1
    return y

call mystere 20
output rval
```

Celui-ci calcule la partie entière du logarithme binaire de 20.

