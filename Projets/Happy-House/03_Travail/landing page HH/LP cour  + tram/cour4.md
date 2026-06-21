

Python

from pptx import Presentation

filename \= "Cours Landing Partie 4.pptx"  
prs \= Presentation(filename)

text\_content \= \[\]

for i, slide in enumerate(prs.slides):  
    slide\_text \= \[\]  
    slide\_text.append(f"--- Slide {i+1} \---")  
      
    \# Sort shapes by their top position to get a rough reading order  
    shapes \= sorted(list(slide.shapes), key=lambda s: (s.top if hasattr(s, 'top') else 0, s.left if hasattr(s, 'left') else 0))  
      
    for shape in shapes:  
        if hasattr(shape, "text") and shape.text.strip():  
             slide\_text.append(shape.text.strip())  
        elif shape.has\_text\_frame:  
            for paragraph in shape.text\_frame.paragraphs:  
                text \= paragraph.text.strip()  
                if text:  
                    slide\_text.append(text)  
        elif shape.has\_table:  
             for row in shape.table.rows:  
                row\_text \= \[cell.text\_frame.text.strip() for cell in row.cells\]  
                slide\_text.append(" | ".join(row\_text))

    text\_content.append("\\n".join(slide\_text))

full\_text \= "\\n\\n".join(text\_content)  
print(full\_text)

Résultat du code

\--- Slide 1 \---  
UX/UI & Landing Page  
Chapitre 4 : UX writing  
Rocket School Toulouse

\--- Slide 2 \---  
partie intégrante de l’UI   
copywriting vs ux writing  
‹\#›  
source : gianni polito

\--- Slide 3 \---  
UX WRITING : C’est quoi ?  
l’UX writing s’intéresse à tous les mots et phrases d'une interface qui sont en lien direct avec les utilisateurs. Son but est de faciliter la navigation.

\--- Slide 4 \---  
À quoi ça sert ?  
contribue à améliorer l’ergonomie globale de l’interface  
son but ultime, c’est aussi la conversion.  
permet de se différencier  
réduit la friction  
renforce l’image de marque   
apporte de la cohérence

\--- Slide 5 \---  
l’écriture conversationnelle  
l’écriture conversationnelle consiste à considérer l’interaction utilisateur-interface   
comme une conversation.

elle apporte un côté agréable et naturel à l’interface

\--- Slide 6 \---  
TROUVER LE BON TON : se différencier  
‹\#›

\--- Slide 7 \---  
TROUVER LE BON TON : se différencier  
‹\#›

\--- Slide 8 \---  
TROUVER LE BON mot : faciliter l’utilisation  
Comment demanderiez-vous à un utilisateur d’inscrire le MRZ se trouvant sur son passeport ?  
Les deux lignes du bas  
Machine-Readable Zone  
‹\#›

\--- Slide 9 \---  
TROUVER LE BON mot : réduire la friction  
proposer une solution  
‹\#›

\--- Slide 10 \---  
TROUVER LE BON mot : réduire la friction  
donner une réponse claire  
‹\#›

\--- Slide 11 \---  
TROUVER LE BON mot : réduire la friction  
le cas de LegalStart  
‹\#›

\--- Slide 12 \---  
définir une charte éDITORIALe   
the tone of voice  
détermine l’identité de votre marque   
renforce la cohérence  
permet à n’importe quel rédacteur de créer du contenu pour la marque  
permet de gagner du temps  
a la même fonction que la charte graphique, mais pour le contenu textuel  
‹\#›

\--- Slide 13 \---  
the tone of voice  
message de la marque  
utilisation d’emojis  
taille des paragraphes   
formules récurrentes  
format des heures/dates, prix…  
usage de l’impératif/infinitif  
interlignes   
nom des catégories  
‹\#›

\--- Slide 14 \---  
bonnes pratiques ux writing  
ne pas écrire ce qu’on ne dirait pas à l’oral  
Téléchargez le pdf  
exporter PDF

\--- Slide 15 \---  
bonnes pratiques ux writing  
écrire à la voie active  
votre demande est en cours de traitement  
nous traitons votre demande

\--- Slide 16 \---  
bonnes pratiques ux writing  
privilégier toujours la valeur et le résultat  
gérer mes   
commandes  
ouvrir le tableau de bord

\--- Slide 17 \---  
bonnes pratiques ux writing  
éviter les acronymes  
besoin d’aide ?  
FAQ

\--- Slide 18 \---  
bonnes pratiques ux writing  
rester cohérent  
changer mon mot de passe  
changer votre mot de passe  
mon compte  
mon compte

\--- Slide 19 \---  
bonnes pratiques ux writing  
la démarche content first

\--- Slide 20 \---  
bonnes pratiques ux writing  
inclure l’UX writing dès le début de la phase de conception

\--- Slide 21 \---  
le cas de back market

\--- Slide 22 \---  
NEXT STEP  
processus de prototypage  
wireframe  
‹\#›

Voici le contenu du fichier PowerPoint "Partie 4" transformé en document Markdown.

Copiez le code ci-dessous et enregistrez-le sous le nom cours\_landing\_partie\_4.md.

Markdown

\# UX/UI & Landing Page \- Cours Partie 4

**\*\*Organisme :\*\*** Rocket School Toulouse  
**\*\*Sujet :\*\*** Chapitre 4 : UX Writing

\---

\#\# ✍️ UX Writing : Définition et Enjeux

\#\#\# C'est quoi ?  
L'UX writing s'intéresse à tous les mots et phrases d'une interface qui sont en lien direct avec les utilisateurs.  
\* **\*\*But principal :\*\*** Faciliter la navigation.  
\* Il est une partie intégrante de l'UI (User Interface).

\#\#\# À quoi ça sert ?  
L'UX writing a plusieurs fonctions stratégiques :  
\* Contribue à améliorer l'ergonomie globale de l'interface.  
\* Son but ultime est la **\*\*conversion\*\***.  
\* Permet de se différencier.  
\* Réduit la friction (les points de blocage pour l'utilisateur).  
\* Renforce l'image de marque.  
\* Apporte de la cohérence.

\#\#\# L'Écriture Conversationnelle  
Elle consiste à considérer l'interaction utilisateur-interface comme une **\*\*conversation\*\***.  
\* Elle apporte un côté agréable, humain et naturel à l'interface.

\---

\#\# 🔍 Trouver le Bon Ton et le Bon Mot

\#\#\# Se différencier par le ton (Tone of Voice)  
Le choix des mots permet de donner une personnalité à la marque.  
\* *\*Exemple visuel (Slide 6-7) :\** Comparaison entre des interfaces au ton formel vs décontracté/humoristique.

\#\#\# Faciliter l'utilisation  
Il faut utiliser le vocabulaire de l'utilisateur, pas celui du développeur.  
\* *\*Exemple Passeport :\** Au lieu de demander le "Machine-Readable Zone" (terme technique obscur), on demandera simplement "Les deux lignes du bas" (clair et visuel).

\#\#\# Réduire la friction  
L'UX writing doit rassurer et guider, surtout en cas d'erreur ou d'incertitude.  
\* **\*\*Proposer une solution :\*\*** Ne pas juste dire "Erreur", mais expliquer comment la résoudre.  
\* **\*\*Donner une réponse claire :\*\*** Éviter le jargon juridique ou technique.  
\* *\*Cas cité :\** LegalStart (simplification du langage juridique).

\---

\#\# 📖 La Charte Éditoriale (Tone of Voice Guidelines)

Tout comme la charte graphique définit l'identité visuelle, la charte éditoriale définit l'identité verbale.

\#\#\# Pourquoi en avoir une ?  
\* Détermine l'identité de votre marque.  
\* Renforce la cohérence sur tous les supports.  
\* Permet à n'importe quel rédacteur de créer du contenu aligné avec la marque.  
\* Permet de gagner du temps.

\#\#\# Que contient-elle ?  
\* Le message de la marque.  
\* L'utilisation (ou non) d'emojis.  
\* La taille des paragraphes.  
\* Les formules récurrentes.  
\* Le format des heures, dates, prix.  
\* L'usage de l'impératif ou de l'infinitif.  
\* Les interlignes.  
\* Le nom des catégories.

\---

\#\# ✅ Bonnes Pratiques UX Writing

Voici quelques règles d'or pour bien rédiger vos interfaces :

1\.  **\*\*Parler comme à l'oral :\*\*** Ne pas écrire ce qu'on ne dirait pas dans une vraie conversation.  
    \* *\*À éviter :\** "Exporter PDF"  
    \* *\*À privilégier :\** "Téléchargez le PDF"

2\.  **\*\*Utiliser la voix active :\*\*** C'est plus dynamique et engageant.  
    \* *\*À éviter :\** "Votre demande est en cours de traitement" (Passif)  
    \* *\*À privilégier :\** "Nous traitons votre demande" (Actif)

3\.  **\*\*Privilégier la valeur et le résultat :\*\*** Parler du bénéfice pour l'utilisateur.  
    \* *\*À éviter :\** "Gérer mes commandes" (Fonctionnel)  
    \* *\*À privilégier :\** "Ouvrir le tableau de bord" (Résultat concret)

4\.  **\*\*Éviter les acronymes :\*\*** Soyez clair pour tout le monde.  
    \* *\*À éviter :\** "FAQ" (si l'audience n'est pas tech)  
    \* *\*À privilégier :\** "Besoin d'aide ?"

5\.  **\*\*Rester cohérent :\*\*** Ne changez pas de pronom en cours de route.  
    \* *\*Exemple :\** Si vous utilisez "Mon compte", utilisez "Changer **\*\*mon\*\*** mot de passe" (pas "votre").

6\.  **\*\*La démarche "Content First" :\*\*** Ne pas traiter le texte comme du remplissage final.  
    \* Inclure l'UX writing dès le début de la phase de conception.

\#\#\# Étude de cas  
\* **\*\*Back Market :\*\*** Exemple cité pour son ton décalé et son UX writing distinctif.

\---

\#\# 🔜 Next Step

La prochaine étape du cours abordera la structure et la mise en forme concrète :  
\* Processus de prototypage.  
\* Wireframe.  
