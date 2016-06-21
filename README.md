**Dieses Repository basiert auf einer alten Version von OParl und
wird nicht mehr weiter entwickelt. Es verbleibt jedoch aus Gründen
der Nachvollziehbarkeit auf GitHub.**

----

OParl Schema
============

Hier werden, passend zur [OParl-Spezifikation](https://github.com/OParl/specs),
die JSON-LD-Kontexte zu den OParl Objekttypen erarbeitet.

Die Ergebnisse sind persistent unter der URL

    http://oparl.org/schema/<Version>/<Name>

abrufbar. Beispiel:

    http://oparl.org/schema/1.0/Body
    http://oparl.org/schema/1.0/Paper
    http://oparl.org/schema/1.0/Person


## Testing

Die Kontexte können mit den Beispiel-Dokumenten im Ordner
test getestet werden. Dazu wird
[PyLD](https://github.com/digitalbazaar/pyld) benötigt.
Zur Installation:

    pip install PyLD

Zum Ausführen eines Tests:

    python test/test.py 1.0/Person test/person01.json

Werden hier Exceptions ausgegeben, ist entweder der Kontext
oder das jeweils eingelesene JSON-Dokument fehlerhaft.
