# CodeChallenge

## Summary of challenge
- Node:ID, x, y
- Element: ID, 3 nodeIDs
- Values on elements: Element ID, value
- Neighbor of elements: share at least one node
- Values on elements: Element ID, value
- Quest:
Find local maxima
Find the first N view spots from highest to lowest Spot height
Same values report only one Element from neighbors; Nicht- Nachbarelemente aber berichten
Input: Json file, N integer
Output: list of N view spots ordered by value from highest to lowest, kein Json!
Messages nach stderr nicht stdout

## Outline Todo:
1. Speicherung der Json Daten in Datenstrukturen, zuerst einfache Listen, Dictionary
2. Mesh zeichnen mit obigen Datenstrukturen, erst mit 10 Dreiecken anfangen, reichen Datenstrukturen?
3. Koordinaten der Knoten der Dreiecke in Adjazenzlisten übersetzen
4. Algorithmus zum Durchlaufen der Adjazenzlisten und Finden der Maxima bestimmen

## Remarks
- Mesh can be bulky: evtl nicht zusammenhängend?
- Im zum Mesh dualen Graphen sind Zyklen vorhanden, Gefahr von endlosen Schleifen.
