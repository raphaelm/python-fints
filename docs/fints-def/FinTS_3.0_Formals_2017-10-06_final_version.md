<!-- PageHeader: Bundesverband der Deutschen Volksbanken und Raiffeisenbanken e. V. Bundesverband deutscher Banken e. V. Bundesverband Öffentlicher Banken Deutschlands e. V. Deutscher Sparkassen- und Giroverband e. V. Verband deutscher Pfandbriefbanken e. V. -->
<!-- PageHeader: Die Deutsche Kreditwirtschaft -->


# FinTS Financial Transaction Services

Schnittstellenspezifikation

Formals

Herausgeber:

Bundesverband deutscher Banken e.V., Berlin

Deutscher Sparkassen- und Giroverband e.V., Bonn/Berlin

Bundesverband der Deutschen Volksbanken und Raiffeisenbanken e.V., Berlin
Bundesverband Öffentlicher Banken Deutschlands e.V., Berlin

<!-- PageFooter: Version: 3.0-FV -->
<!-- PageFooter: Stand: 06.10.2017 -->
<!-- PageFooter: Final Version -->
<!-- PageBreak -->

<!-- PageBreak -->

Die vorliegende Schnittstellenspezifikation für eine automatisiert nutzbare multibankfähige
Banking-Schnittstelle (im Folgenden: Schnittstellenspezifikation) wurde im Auftrag der Deut-
schen Kreditwirtschaft entwickelt. Sie wird hiermit zur Implementation in Kunden- und Kredit-
institutssysteme freigegeben.

Die Schnittstellenspezifikation ist urheberrechtlich geschützt. Zur Implementation in Kunden-
und Kreditinstitutssysteme wird interessierten Herstellern unentgeltlich ein einfaches Nut-
zungsrecht eingeräumt. Im Rahmen des genannten Zwecks darf die Schnittstellenspezifika-
tion auch - in unveränderter Form - vervielfältigt und zu den nachstehenden Bedingungen
verbreitet werden.

Umgestaltungen, Bearbeitungen, Übersetzungen und jegliche Änderung der Schnittstellen-
spezifikation sind untersagt. Kennzeichnungen, Copyright-Vermerke und Eigentumsangaben
dürfen in keinem Fall geändert werden.

Im Hinblick auf die Unentgeltlichkeit des eingeräumten Nutzungsrechts wird keinerlei Ge-
währleistung oder Haftung für Fehler der Schnittstellenspezifikation oder die ordnungsge-
mäße Funktion der auf ihr beruhenden Produkte übernommen. Die Hersteller sind aufgefor-
dert, Fehler oder Auslegungsspielräume der Spezifikation, die die ordnungsgemäße Funkti-
on oder Multibankfähigkeit von Kundenprodukten behindern, der Deutschen Kreditwirtschaft
zu melden. Es wird weiterhin ausdrücklich darauf hingewiesen, dass Änderungen der
Schnittstellenspezifikation durch Die Deutsche Kreditwirtschaft jederzeit und ohne vorherige
Ankündigung möglich sind.

Eine Weitergabe der Schnittstellenspezifikation durch den Hersteller an Dritte darf nur un-
entgeltlich, in unveränderter Form und zu den vorstehenden Bedingungen erfolgen.

Dieses Dokument kann im Internet abgerufen werden unter http://www.fints.org.

<!-- PageBreak -->


## Versionsführung

Das vorliegende Dokument wurde von folgenden Personen erstellt bzw. geändert:


<table>
<tr>
<th>Name</th>
<th>Organi- sation</th>
<th>Datum</th>
<th>Versi- on</th>
<th>Dokumente</th>
<th>Anmerkungen</th>
</tr>
<tr>
<td>Stein</td>
<td>SIZ</td>
<td>22.11.1996</td>
<td>1.0</td>
<td>hbci10.doc</td>
<td>Erste vom ZKA verab- schiedete Version</td>
</tr>
<tr>
<td rowspan="4">Stein</td>
<td rowspan="4">SIZ</td>
<td rowspan="4">24.07.1997</td>
<td rowspan="4">2.0</td>
<td>hbci20a.doc</td>
<td>Änderungen und Fehler-</td>
</tr>
<tr>
<td>hbci20b.doc</td>
<td>korrekturen sowie neue</td>
</tr>
<tr>
<td>hbci20c.doc</td>
<td>Geschäftsvorfälle</td>
</tr>
<tr>
<td>hbci20d.doc</td>
<td></td>
</tr>
<tr>
<td rowspan="4">Stein</td>
<td rowspan="4">SIZ</td>
<td rowspan="4">02.02.1998</td>
<td rowspan="4">2.0.1</td>
<td>hbci201a.doc</td>
<td>Änderungen und Fehler-</td>
</tr>
<tr>
<td>hbci201b.doc</td>
<td>korrekturen zur Version</td>
</tr>
<tr>
<td>hbci201c.doc</td>
<td>2.0</td>
</tr>
<tr>
<td>hbci201d.doc</td>
<td></td>
</tr>
<tr>
<td rowspan="4">Stein</td>
<td rowspan="4">SIZ</td>
<td rowspan="4">02.03.1999</td>
<td rowspan="4">2.1</td>
<td>hbci21a.doc</td>
<td>Änderungen und neue</td>
</tr>
<tr>
<td>hbci21b.doc</td>
<td>Geschäftsvorfälle (Wert-</td>
</tr>
<tr>
<td>hbci21c.doc</td>
<td>papiergeschäft)</td>
</tr>
<tr>
<td>hbci21d.doc</td>
<td></td>
</tr>
<tr>
<td rowspan="4">Stein</td>
<td rowspan="4">SIZ</td>
<td rowspan="4">10.05.2000</td>
<td rowspan="4">2.2</td>
<td>hbci22a.doc</td>
<td>Neue Geschäftsvorfälle</td>
</tr>
<tr>
<td>hbci22b.doc</td>
<td>und inhaltliche Korrektu-</td>
</tr>
<tr>
<td>hbci22c.doc</td>
<td>ren (keine Änderungen</td>
</tr>
<tr>
<td>hbci22d.doc</td>
<td>an der Basiskomponen- te)</td>
</tr>
<tr>
<td>Stein</td>
<td>SIZ</td>
<td>15.11.2002</td>
<td>3.0</td>
<td>FinTS 3.0 Formals.doc</td>
<td>Dieses Dokument ent- spricht dem Teil A der bisherigen HBCI- Spezifikation</td>
</tr>
<tr>
<td>Haubner</td>
<td>für SIZ</td>
<td>12.11.2010</td>
<td>3.0</td>
<td>FinTS 3.0 Formals Rel. 2010-11-12 final ver- sion.doc</td>
<td>Extrahieren des Kapitels zur Bedeutung der Rückmeldungscodes</td>
</tr>
<tr>
<td>Haubner</td>
<td>für SIZ</td>
<td>14.06.2011</td>
<td>3.0</td>
<td>FinTS 3.0 Formals Rel. 2011-06-14 final ver- sion.doc</td>
<td>Fehler und Klarstellun- gen P1 bis P5, Integrati- on RAH-Verfahren</td>
</tr>
<tr>
<td>Haubner</td>
<td>für SIZ</td>
<td>11.05.2017</td>
<td>3.0-FV</td>
<td>FinTS 3.0 Formals Rel. 2017-05-11 final ver- sion.doc</td>
<td>UPD-Erweiterung und - Prozesse; Anpassungen für starke Kun- denauthentifizierung nach PSD2 / RTS</td>
</tr>
<tr>
<td>Haubner</td>
<td>für SIZ</td>
<td>06.10.2017</td>
<td>3.0</td>
<td>FinTS 3.0 Formals Rel. 2017-10-06 final ver- sion.doc</td>
<td>Klarstellungen zur star- ken Kundenauthentifizie- rung</td>
</tr>
</table>


<!-- PageBreak -->


## Änderungen gegenüber der Vorversion:

Hinzufügungen und Änderungen sind im Dokument in dieser Farbe und zusätzlich
durch Unterstreichung und einen Randbalken markiert. Löschungen sind aufgrund
der besseren Übersichtlichkeit nur durch einen Randbalken markiert. Hypertextlinks
sind je nach Überarbeitungsversion in unterschiedlichen Farben markiert. Falls sich
die Kapitelnummerierung geändert hat, bezieht sich die Kapitelangabe auf die neue
Nummerierung. Aufgrund der umfangreichen Textumstellungen wurden nicht alle
Änderungen markiert.


<table>
<tr>
<th>lfd. Nr.</th>
<th>Kapitel</th>
<th>Kapitel- nummer</th>
<th>Ken- nung<br>1</th>
<th>Art2</th>
<th>Beschreibung</th>
</tr>
<tr>
<td>1</td>
<td rowspan="2">Allgemeines</td>
<td></td>
<td>-</td>
<td>K</td>
<td>Ersetzung von DM durch Euro in Text und Beispielen</td>
</tr>
<tr>
<td>2</td>
<td></td>
<td>131</td>
<td>Ä</td>
<td>Umwandlung von GD und GDG in DE bzw. DEG.</td>
</tr>
<tr>
<td>3</td>
<td rowspan="2">Nachrichtenaufbau</td>
<td>B.3.1</td>
<td>131</td>
<td>Ä</td>
<td>Einführung des Status „C“ (konditional); Umwandlung des Status ,,K" in ,O“ (opti- onal)</td>
</tr>
<tr>
<td>4</td>
<td>B.4.2</td>
<td>166</td>
<td>Ä</td>
<td>Einführung des Formats ,code' für Da- tenelemente, deren Inhalt durch eine Schlüsseltabelle definiert wird (diese Änderung ist lediglich deskriptiv und hat keine Auswirkungen auf den physischen Nachrichtenaufbau und die Segment- versionen)</td>
</tr>
<tr>
<td>5</td>
<td rowspan="3">Dialogspezifikation</td>
<td>C.3 C.8</td>
<td>162</td>
<td>Ä</td>
<td>Das Segment HKISA kann bis zu 3-mal in die Dialoginitialisierung eingestellt werden</td>
</tr>
<tr>
<td>6</td>
<td>C.9</td>
<td>149</td>
<td>E</td>
<td>Life-Indikator-Nachricht hinzugefügt</td>
</tr>
<tr>
<td>7</td>
<td>C. 10</td>
<td>171</td>
<td>E</td>
<td>Kapitel bzgl. Unterstützung beliebiger Geschäftsvorfallversionen hinzugefügt</td>
</tr>
<tr>
<td>8</td>
<td rowspan="2">Bankparameter- daten</td>
<td>D.2</td>
<td>149</td>
<td>Ä</td>
<td>Aufnahme von Feldern zur Angabe des Timeout-Wertes in die Bankparameter- daten</td>
</tr>
<tr>
<td>9</td>
<td>D.5</td>
<td>190</td>
<td>Ä</td>
<td>Ermöglichung von Komprimierung (de- flate/GZIP als zwingend vorgeschriebe- ner Algorithmus</td>
</tr>
<tr>
<td>10</td>
<td rowspan="3">Userparameter- daten</td>
<td>E.1</td>
<td>134</td>
<td>K</td>
<td>Klarstellung, welche Konten für Berech- tigungsprüfung herangezogen werden</td>
</tr>
<tr>
<td>11</td>
<td>E.2 E.3</td>
<td>172</td>
<td>Ä</td>
<td>Aufnahme des Feldes ,,Benutzername“ in das Segment HIUPA und des Feldes ,Kontoart" in das Segment HIUPD</td>
</tr>
<tr>
<td>12</td>
<td>E.3</td>
<td>134</td>
<td>Ä</td>
<td>DE Kontoverbindung erhält Status „opti- onal" um auch nicht kontogebundene Geschäftsvorfälle angeben zu können</td>
</tr>
<tr>
<td>13</td>
<td>Data-Dictionary</td>
<td>F.</td>
<td>131</td>
<td>Ä</td>
<td>Trennung der semantischen Daten- beschreibung vom Geschäftsvorfalls- modell (Einführung eines Data Dictio- naries)</td>
</tr>
</table>

1
nur zur internen Zuordnung

2
F = Fehler; Ä = Änderung; K = Klarstellung; E = Erweiterung


<!-- PageBreak -->


<table>
<tr>
<th>lfd. Nr.</th>
<th>Kapitel</th>
<th>Kapitel- nummer</th>
<th>Ken- nung<br>1</th>
<th>Art2</th>
<th>Beschreibung</th>
</tr>
<tr>
<td>14</td>
<td rowspan="2">Code-Bedeutungen</td>
<td>F.</td>
<td></td>
<td>Ä</td>
<td>DE ,,Kommunikationsadresse": ,https' als möglicher Wert hinzugefügt</td>
</tr>
<tr>
<td>15</td>
<td>Β.7.5.3</td>
<td>P6</td>
<td>K</td>
<td>Verlagern des Kapitels ,,Bedeutung der Rückmeldungscodes“ in ein separates Dokument [RM-Codes].</td>
</tr>
<tr>
<td>16</td>
<td>Einleitung</td>
<td>A</td>
<td></td>
<td>K</td>
<td>Entfernen der Kontaktinformationen und stattdessen Verweis auf fints.org.</td>
</tr>
<tr>
<td>17</td>
<td>Einleitung</td>
<td>A</td>
<td></td>
<td>E</td>
<td>Ergänzen der Begriffsdefinitionen für ,HBCI" und ,FinTS"</td>
</tr>
<tr>
<td>18</td>
<td>Transportmedien- spezifische Festle- gungen</td>
<td>H.4</td>
<td></td>
<td>E</td>
<td>Entfernen des Kommunikationsdienstes BtxFIF aus der Spezifikation</td>
</tr>
<tr>
<td>19</td>
<td>Statusprotokoll</td>
<td>C.7</td>
<td>P5</td>
<td>Ä</td>
<td>Entfall der kreditinstitutsseitigen Ver- pflichtung zur Unterstützung des Sta- tusprotokolls</td>
</tr>
<tr>
<td>20</td>
<td>UPD</td>
<td>C.2</td>
<td>P4</td>
<td>K</td>
<td>Verhalten bei UPD=0</td>
</tr>
<tr>
<td>21</td>
<td>Verarbeitungsvor- bereitung</td>
<td>C.3.1.3</td>
<td>P3</td>
<td>E</td>
<td>Rückmeldecodes für den Schlüssel- wechsel von RDH-1 auf RDH-2</td>
</tr>
<tr>
<td>22</td>
<td>UPD</td>
<td>E</td>
<td>P2</td>
<td>E</td>
<td>Ergänzen der Datenelemente „Erweite- rung. Allgemein" und ,Erweiterung, kon- tobezogen“</td>
</tr>
<tr>
<td>23</td>
<td>UPD</td>
<td>E.3</td>
<td>P1</td>
<td>K</td>
<td>Längenanpassung bei den Datenele- menten ,,Name des Kontoinhabers 1 und 2"</td>
</tr>
<tr>
<td>24</td>
<td>UPD</td>
<td>E.3</td>
<td></td>
<td>K</td>
<td>Längenanpassung beim Datenelement ,IBAN" von ..35 auf ..34.</td>
</tr>
<tr>
<td>25</td>
<td>Diverse</td>
<td></td>
<td></td>
<td>E</td>
<td>Ergänzen des RAH-Verfahrens</td>
</tr>
<tr>
<td>26</td>
<td>UPD, FinTS- Prozesse</td>
<td>D.3.1 und E</td>
<td>0461</td>
<td>E</td>
<td>Beschreibung von Inhalten und Prozes- sen der UPD-Erweiterung, kontobezo- gen (ohne Revisionsmarkierungen)</td>
</tr>
<tr>
<td>27</td>
<td>Dialoginitialisierung</td>
<td>B.3</td>
<td>0480</td>
<td>E</td>
<td>Berücksichtigung der starken Authentifi- zierung</td>
</tr>
</table>


## Releasedatum 06.10.2017


<table>
<tr>
<th>lfd. Nr.</th>
<th>Kapitel</th>
<th>Kapitel- nummer</th>
<th>Ken- nung<br>3</th>
<th>Art4</th>
<th>Beschreibung</th>
</tr>
<tr>
<td>1</td>
<td>Verarbeitungsvor- bereitung</td>
<td>C.3.1.3</td>
<td>0496</td>
<td>Ä</td>
<td>Ändern der Segmentversion auf 3.</td>
</tr>
<tr>
<td>2</td>
<td>Segmente</td>
<td>I.1.3</td>
<td>0496</td>
<td>E</td>
<td>Ergänzen fehlender Segmente</td>
</tr>
<tr>
<td>3</td>
<td>Anlagen</td>
<td>I.2.1</td>
<td>0496</td>
<td>E</td>
<td>Hinzufügen von HKTAN/HITAN bei Auf- tragsnachrichten</td>
</tr>
<tr>
<td>4</td>
<td>Diverse</td>
<td></td>
<td>0496</td>
<td>E</td>
<td>Einfügen der Spalte „Version“ in allen Syntaxtabellen.<br>Nachpflegen von fehlenden Änderungen aus den ,,Changes" unter fints.org.</td>
</tr>
</table>


<!-- PageFooter: 3 nur zur internen Zuordnung -->
<!-- PageFooter: 4 F = Fehler; Ä = Änderung; K = Klarstellung; E = Erweiterung -->
<!-- PageBreak -->


## Dokumentenstruktur

Das vorliegende Dokument steht in folgendem Bezug zu den anderen Bänden der
FinTS V3.0 Spezifikation:


![Hauptdokument Formals Rückmeldungen SCPA Messages Geschäftsvorfälle Messages Finanzdatenformate IZV Messages Geschäftsvorfälle Security HBCI Security PIN/TAN Security Secoder ☐ 1 5 2 3 4 1 5 2 3 4 6 0 8 9 7 6 7 0 DK- Signaturkarte 8 9 C R C R Secoder chipTAN mobile TAN Secoder](figures/7.1)


<!-- PageBreak -->

<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th rowspan="2">Version: 3.0-FV</th>
<th rowspan="2">Kapitel: A</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Formals</td>
</tr>
<tr>
<td>Kapitel:</td>
<td>Einleitung</td>
<td>Stand: 06.10.2017</td>
<td>Seite: 1</td>
</tr>
</table>


## Inhaltsverzeichnis


<table>
<tr>
<td>A. Einleitung</td>
<td>7</td>
</tr>
<tr>
<td>B. Nachrichtenaufbau</td>
<td>9</td>
</tr>
<tr>
<td>B.1 Zeichensatz</td>
<td>9</td>
</tr>
<tr>
<td>B.2 Nachrichtenelemente</td>
<td>9</td>
</tr>
<tr>
<td>B.3 Festlegungen</td>
<td>10</td>
</tr>
<tr>
<td>B.3.1 Status und Anzahl</td>
<td>10</td>
</tr>
<tr>
<td>B.3.2 Restriktionen</td>
<td>11</td>
</tr>
<tr>
<td>B.3.3 Längenangaben</td>
<td>12</td>
</tr>
<tr>
<td>B.3.4 Transparente Daten</td>
<td>12</td>
</tr>
<tr>
<td>B.3.5 Datum und Uhrzeit</td>
<td>12</td>
</tr>
<tr>
<td>B.4 Datenformate</td>
<td>13</td>
</tr>
<tr>
<td>B.4.1 Basisformate</td>
<td>13</td>
</tr>
<tr>
<td>B.4.2 Abgeleitete Formate</td>
<td>14</td>
</tr>
<tr>
<td>B.5 Steuerstrukturen</td>
<td>15</td>
</tr>
<tr>
<td>B.5.1 Segmentkopf</td>
<td>15</td>
</tr>
<tr>
<td>B.5.2 Nachrichtenkopf</td>
<td>15</td>
</tr>
<tr>
<td>B.5.3 Nachrichtenabschluss</td>
<td>15</td>
</tr>
<tr>
<td>B.6 Kundennachrichten allgemein</td>
<td>17</td>
</tr>
<tr>
<td>B.6.1 Allgemeiner Nachrichtenaufbau</td>
<td>17</td>
</tr>
<tr>
<td colspan="2">B.6.2 Aufträge 19</td>
</tr>
<tr>
<td>B.6.3 Abholauftrag</td>
<td>19</td>
</tr>
<tr>
<td>B.7 Kreditinstitutsnachrichten allgemein</td>
<td>23</td>
</tr>
<tr>
<td>B.7.1 Allgemeiner Nachrichtenaufbau</td>
<td>23</td>
</tr>
<tr>
<td>B.7.2 Rückmeldungen zur Gesamtnachricht</td>
<td>24</td>
</tr>
<tr>
<td>B.7.3 Rückmeldungen zu Segmenten</td>
<td>25</td>
</tr>
<tr>
<td>B.7.4 Datensegmente</td>
<td>26</td>
</tr>
<tr>
<td>B.7.5 Rückmeldungscodes</td>
<td>27</td>
</tr>
<tr>
<td>B.7.5.1 Grundkonzept</td>
<td>27</td>
</tr>
<tr>
<td>B.7.5.2 Reaktionsvorschriften</td>
<td>27</td>
</tr>
<tr>
<td>B.7.5.3 Code-Bedeutungen</td>
<td>30</td>
</tr>
<tr>
<td>B.7.6 Dialogabbruchnachricht</td>
<td>31</td>
</tr>
</table>


<!-- PageBreak -->


<table>
<tr>
<td>Kapitel:<br>A</td>
<td>Version: 3.0-FV</td>
<td>Financial Transaction Services (FinTS) Dokument: Formals</td>
</tr>
<tr>
<td>Seite: 2</td>
<td>Stand: 06.10.2017</td>
<td>Kapitel: Einleitung</td>
</tr>
</table>


<table>
<tr>
<td>B.8 8 Allgemeiner Nachrichtenaufbau bei Verschlüsselung</td>
<td>33</td>
</tr>
<tr>
<td>C. Dialogspezifikation</td>
<td>35</td>
</tr>
<tr>
<td>C.1 Allgemeines</td>
<td>35</td>
</tr>
<tr>
<td>C.1.1 Begriffsbestimmung</td>
<td>35</td>
</tr>
<tr>
<td>C.1.2 Dialogabfolge</td>
<td>37</td>
</tr>
<tr>
<td>C.1.3 Verschlüsselung des Dialoges beim Sicherheitsverfahren HBCI</td>
<td>39</td>
</tr>
<tr>
<td>C.2 Abfolge von Operationen</td>
<td>40</td>
</tr>
<tr>
<td>C.3 Dialoginitialisierung</td>
<td>41</td>
</tr>
<tr>
<td>C.3.1 Kundennachricht</td>
<td>41</td>
</tr>
<tr>
<td>C.3.1.1 Nachrichtenformat</td>
<td>41</td>
</tr>
<tr>
<td>C.3.1.2 Segment: Identifikation</td>
<td>43</td>
</tr>
<tr>
<td>C.3.1.3 Segment: Verarbeitungsvorbereitung</td>
<td>45</td>
</tr>
<tr>
<td>C.3.1.4 Segment: Anforderung eines öffentlichen Schlüssels</td>
<td>47</td>
</tr>
<tr>
<td>C.3.2 Kreditinstitutsnachricht</td>
<td>48</td>
</tr>
<tr>
<td>C.3.2.1 Nachrichtenformat</td>
<td>48</td>
</tr>
<tr>
<td>C.3.2.2 Segmentfolge: Bankparameterdaten</td>
<td>49</td>
</tr>
<tr>
<td>C.3.2.3 Segmentfolge: Userparameterdaten</td>
<td>50</td>
</tr>
<tr>
<td>C.3.2.4 Segment: Übermittlung eines öffentlichen Schlüssels</td>
<td>51</td>
</tr>
<tr>
<td>C.3.2.5 Segment: Kreditinstitutsmeldung</td>
<td>52</td>
</tr>
<tr>
<td>C.4 Dialogbeendigung</td>
<td>53</td>
</tr>
<tr>
<td>C.4.1 Ausnahmen zur Dialogbeendigung</td>
<td>53</td>
</tr>
<tr>
<td>C.4.2 Kundennachricht</td>
<td>53</td>
</tr>
<tr>
<td>C.4.2.1 Nachrichtenformat</td>
<td>53</td>
</tr>
<tr>
<td>C.4.2.2 Segment: Dialogende</td>
<td>54</td>
</tr>
<tr>
<td>C.4.3 Kreditinstitutsnachricht</td>
<td>54</td>
</tr>
<tr>
<td>C.5 Anonymer Zugang</td>
<td>55</td>
</tr>
<tr>
<td>C.5.1 Dialoginitialisierung</td>
<td>55</td>
</tr>
<tr>
<td>C.5.2 Auftragsnachricht</td>
<td>57</td>
</tr>
<tr>
<td>C.5.3 Dialogbeendigung</td>
<td>57</td>
</tr>
<tr>
<td>C.6 Verbindungsabbruch</td>
<td>59</td>
</tr>
<tr>
<td>C.7 Statusprotokoll</td>
<td>63</td>
</tr>
<tr>
<td>C.8 Synchronisierung</td>
<td>66</td>
</tr>
<tr>
<td>C.8.1 Kundennachricht</td>
<td>67</td>
</tr>
<tr>
<td>C.8.1.1 Nachrichtenformat</td>
<td>67</td>
</tr>
<tr>
<td>C.8.1.2 Segment: Synchronisierung</td>
<td>68</td>
</tr>
<tr>
<td>C.8.2 Kreditinstitutsnachricht</td>
<td>69</td>
</tr>
<tr>
<td>C.8.2.1 Nachrichtenformat</td>
<td>69</td>
</tr>
<tr>
<td>C.8.2.2 Segment: Synchronisierungsantwort</td>
<td>69</td>
</tr>
</table>


<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th rowspan="2">Version: 3.0-FV</th>
<th rowspan="2">Kapitel: A</th>
</tr>
<tr>
<th>Dokument:</th>
<th>Formals</th>
</tr>
<tr>
<td>Kapitel:</td>
<td>Einleitung</td>
<td>Stand: 06.10.2017</td>
<td>Seite: 3</td>
</tr>
</table>


<table>
<tr>
<td>C.9 Life-Indikator-Nachricht</td>
<td>71</td>
</tr>
<tr>
<td>C.10 Unterstützung von Geschäftsvorfallversionen</td>
<td>74</td>
</tr>
<tr>
<td>D. Bankparameterdaten (BPD)</td>
<td>77</td>
</tr>
<tr>
<td>D.1 Allgemeines</td>
<td>77</td>
</tr>
<tr>
<td>D.2 Bankparameter allgemein</td>
<td>79</td>
</tr>
<tr>
<td>D.3 Kommunikationszugang</td>
<td>80</td>
</tr>
<tr>
<td>D.4 Sicherheitsverfahren</td>
<td>81</td>
</tr>
<tr>
<td>D.5 Komprimierungsverfahren</td>
<td>82</td>
</tr>
<tr>
<td>D.6 Geschäftsvorfallparameter</td>
<td>83</td>
</tr>
<tr>
<td>D.7 Parameterdaten</td>
<td>84</td>
</tr>
<tr>
<td>E. Userparameterdaten (UPD)</td>
<td>85</td>
</tr>
<tr>
<td>E.1 Allgemeines</td>
<td>85</td>
</tr>
<tr>
<td>E.2 Userparameter allgemein</td>
<td>87</td>
</tr>
<tr>
<td>E.3 Kontoinformation</td>
<td>88</td>
</tr>
<tr>
<td>E.3.1 Aufbau der UPD-Erweiterung, kontobezogen</td>
<td>89</td>
</tr>
<tr>
<td>E.3.1.1 Belegungsvorschriften für die einzelnen JSON-Elemente</td>
<td>93</td>
</tr>
<tr>
<td>E.3.1.2 Beispiel für die Verwendung der UPD-Erweiterung zur Bestandsoptimierung</td>
<td>97</td>
</tr>
<tr>
<td>F. FinTS Prozesse</td>
<td>99</td>
</tr>
<tr>
<td>F.1 Versionsverwaltung</td>
<td>99</td>
</tr>
<tr>
<td>F.2 Generelle Festlegungen</td>
<td>100</td>
</tr>
<tr>
<td>F.3 Spezielle Prozesse</td>
<td>101</td>
</tr>
<tr>
<td>F.3.1 Abruf von Umsätzen</td>
<td>102</td>
</tr>
<tr>
<td>F.3.2 Abruf von Salden</td>
<td>102</td>
</tr>
<tr>
<td>F.3.3 Abruf von Beständen</td>
<td>103</td>
</tr>
<tr>
<td>F.3.4 Abruf von SEPA-Kontoverbindungsdaten</td>
<td>103</td>
</tr>
<tr>
<td>F.3.5 Anzeige der verfügbaren TAN-Medien</td>
<td>104</td>
</tr>
<tr>
<td>G. Data Dictionary</td>
<td>105</td>
</tr>
<tr>
<td>A</td>
<td>105</td>
</tr>
<tr>
<td>B</td>
<td>106</td>
</tr>
<tr>
<td>D</td>
<td>109</td>
</tr>
<tr>
<td>E</td>
<td>110</td>
</tr>
<tr>
<td>F</td>
<td>111</td>
</tr>
<tr>
<td>G</td>
<td>112</td>
</tr>
<tr>
<td>Η</td>
<td>112</td>
</tr>
</table>


<!-- PageBreak -->


<table>
<tr>
<td>Kapitel:<br>A</td>
<td>Version: 3.0-FV</td>
<td>Financial Transaction Services (FinTS) Dokument: Formals</td>
</tr>
<tr>
<td>Seite: 4</td>
<td>Stand: 06.10.2017</td>
<td>Kapitel: Einleitung</td>
</tr>
</table>


<table>
<tr>
<td>I</td>
<td>113</td>
</tr>
<tr>
<td>K</td>
<td>113</td>
</tr>
<tr>
<td>L</td>
<td>117</td>
</tr>
<tr>
<td>M</td>
<td>118</td>
</tr>
<tr>
<td>N</td>
<td>120</td>
</tr>
<tr>
<td>P</td>
<td>121</td>
</tr>
<tr>
<td>R</td>
<td>121</td>
</tr>
<tr>
<td>S</td>
<td>123</td>
</tr>
<tr>
<td>U</td>
<td>126</td>
</tr>
<tr>
<td>V</td>
<td>129</td>
</tr>
<tr>
<td>W</td>
<td>129</td>
</tr>
<tr>
<td>H. Syntax</td>
<td>131</td>
</tr>
<tr>
<td>H.1 Nachrichtensyntax</td>
<td>131</td>
</tr>
<tr>
<td>H.1.1 Syntaxzeichen</td>
<td>131</td>
</tr>
<tr>
<td>H.1.2 Nachrichtenaufbau</td>
<td>131</td>
</tr>
<tr>
<td>H.1.3 Entwertung</td>
<td>132</td>
</tr>
<tr>
<td>H.1.4 Binäre Daten</td>
<td>133</td>
</tr>
<tr>
<td>H.1.5 Auslassen von Datenstrukturen</td>
<td>133</td>
</tr>
<tr>
<td>H.2 Beispiele</td>
<td>135</td>
</tr>
<tr>
<td>H.2.1 Datenelementgruppen</td>
<td>135</td>
</tr>
<tr>
<td>H.2.2 Segmente</td>
<td>135</td>
</tr>
<tr>
<td>H.2.3 Segmentfolgen</td>
<td>154</td>
</tr>
<tr>
<td>H.2.4 Dialog 156</td>
<td></td>
</tr>
<tr>
<td>H.2.4.1 Nachricht ,,Dialoginitialisierung"</td>
<td>156</td>
</tr>
<tr>
<td>H.2.4.2 Nachricht „SEPA-Einzelüberweisung“</td>
<td>159</td>
</tr>
<tr>
<td>H.2.4.3 Nachricht ,,Saldenabfrage“</td>
<td>160</td>
</tr>
<tr>
<td>H.2.4.4 Nachricht ,,Dialogbeendigung“</td>
<td>162</td>
</tr>
<tr>
<td>I. Anlagen</td>
<td>165</td>
</tr>
<tr>
<td>I.1 Übersicht der FinTS-Elemente</td>
<td>165</td>
</tr>
<tr>
<td>I.1.1 Nachrichten</td>
<td>165</td>
</tr>
<tr>
<td>I.1.2 Segmentfolgen</td>
<td>166</td>
</tr>
<tr>
<td>I.1.3 Segmente</td>
<td>167</td>
</tr>
<tr>
<td>I.2 Übersicht Nachrichtenaufbau</td>
<td>169</td>
</tr>
<tr>
<td>I.2.1 Standarddialog</td>
<td>170</td>
</tr>
<tr>
<td>I.2.2 Anonymer Dialog</td>
<td>172</td>
</tr>
<tr>
<td>I.2.3 Synchronisierung</td>
<td>173</td>
</tr>
</table>


<!-- PageBreak -->


<table>
<tr>
<th>Financial Transaction Services (FinTS)</th>
<th>Version:</th>
<th>Kapitel:</th>
</tr>
<tr>
<td>Dokument: Formals</td>
<td>3.0-FV</td>
<td>A</td>
</tr>
<tr>
<td>Kapitel:<br>Einleitung</td>
<td>Stand: 06.10.2017</td>
<td>Seite: 5</td>
</tr>
</table>


<table>
<tr>
<td></td>
<td>I.2.4 Kommunikationszugang</td>
<td>174</td>
</tr>
<tr>
<td rowspan="5"></td>
<td>I.2.5 Änderung eines öffentlichen Schlüssels des Kunden (HBCI RAH und RDH)</td>
<td>175</td>
</tr>
<tr>
<td>I.2.6 Erstmalige Anforderung der öffentlichen Schlüssel des Kreditinstituts (HBCI RAH und RDH)</td>
<td>176</td>
</tr>
<tr>
<td>I.2.7 Erstmalige Übermittlung der öffentlichen Schlüssel des Kunden (HBCI RAH und RDH)</td>
<td>177</td>
</tr>
<tr>
<td>I.2.8 Schlüsselsperrung durch den Kunden (HBCI RAH und RDH)</td>
<td>178</td>
</tr>
<tr>
<td>I.2.9 Schlüsselsperrung durch den Kunden (HBCI DDV)</td>
<td>179</td>
</tr>
<tr>
<td>I.3</td>
<td>FinTS-Basiszeichensätze</td>
<td>180</td>
</tr>
<tr>
<td rowspan="3"></td>
<td>I.3.1 ISO 8859-1 Subset Deutsch</td>
<td>180</td>
</tr>
<tr>
<td>I.3.2 ISO 8859-1 Subset Englisch</td>
<td>180</td>
</tr>
<tr>
<td>I.3.3 ISO 8859-1 Subset Französisch</td>
<td>181</td>
</tr>
<tr>
<td>I.4</td>
<td>Transportmedienspezifische Festlegungen</td>
<td>183</td>
</tr>
<tr>
<td></td>
<td>I.4.1 TCP/IP</td>
<td>184</td>
</tr>
<tr>
<td></td>
<td>I.4.1.1 Internet (WWW)</td>
<td>184</td>
</tr>
<tr>
<td>I.5</td>
<td>Abruf von Kommunikationszugangsdaten</td>
<td>185</td>
</tr>
<tr>
<td>Kapitel:<br>A</td>
<td>Version: 3.0-FV</td>
<td>Financial Transaction Services (FinTS) Dokument: Formals</td>
</tr>
<tr>
<td>Seite:<br>6</td>
<td>Stand: 06.10.2017</td>
<td>Kapitel: Einleitung</td>
</tr>
</table>


## Abbildungsverzeichnis


<table>
<tr>
<td>Abbildung 1: Übersicht der Schnittstellenbeziehungen</td>
<td>7</td>
</tr>
<tr>
<td>Abbildung 2: Nachrichtenaufbau</td>
<td>10</td>
</tr>
<tr>
<td>Abbildung 3: Logischer Nachrichtenaufbau</td>
<td>18</td>
</tr>
<tr>
<td>Abbildung 6: Dialogabfolge</td>
<td>37</td>
</tr>
<tr>
<td>Abbildung 7: Einzelbenutzer</td>
<td>38</td>
</tr>
<tr>
<td>Abbildung 8: Mehrere Benutzer</td>
<td>38</td>
</tr>
<tr>
<td>Abbildung 9: Verbindungsabbruch Fall 1</td>
<td>60</td>
</tr>
<tr>
<td>Abbildung 10: Verbindungsabbruch Fall 2</td>
<td>60</td>
</tr>
<tr>
<td>Abbildung 11: Verbindungsabbruch Fall 3</td>
<td>61</td>
</tr>
<tr>
<td>Abbildung 12: Verbindungsabbruch Fall 4</td>
<td>61</td>
</tr>
<tr>
<td>Abbildung 13: Funktionsweise des Life-Indikators</td>
<td>71</td>
</tr>
<tr>
<td>Abbildung 14: Beispielhafter Aufbau der UPD-Erweiterung, kontobezogen (Tabelle)</td>
<td>90</td>
</tr>
<tr>
<td>Abbildung 15: Beispielhafter Aufbau der UPD-Erweiterung, kontobezogen (JSON)</td>
<td>91</td>
</tr>
</table>


<!-- PageBreak -->


<table>
<tr>
<th>Financial Transaction Services (FinTS)</th>
<th>Version:</th>
<th>Kapitel:</th>
</tr>
<tr>
<td>Dokument:<br>Formals</td>
<td>3.0-FV</td>
<td>A</td>
</tr>
<tr>
<td>Kapitel:<br>Einleitung</td>
<td>Stand: 06.10.2017</td>
<td>Seite: 7</td>
</tr>
</table>


### A. EINLEITUNG

Die vorliegende Spezifikation bildet die Grundlage für eine automatisiert nutzbare
multibankfähige Onlinebanking-Schnittstelle. Eine parallele Nutzung anderer Kredit-
institutszugänge (z. B. „Browserbanking“) bleibt hiervon unberührt.

Mit der Version 3.0 fand eine Namensänderung von „HBCI" nach ,,FinTS" statt.
HBCI bezeichnet in diesem Kontext ausschließlich das Sicherheitsverfahren wäh-
rend FinTS als Bezeichnung für das gesamte Protokoll steht. Im Dokument wurden
die Begriffe wo immer möglich in diesem Sinn verwendet. Wird jedoch auf konkrete
Protokollstrukturen (z. B. ,,HBCI-Version") oder ältere Spezifikationsversionen wie
,HBCI V2.2" verwiesen, so bezeichnet der Begriff ,,HBCI" in diesen Fällen auch das
Protokoll und ist gleichbedeutend mit ,,FinTS".

Beschrieben wird die Schnittstelle zwischen Kundenprodukt und Kreditinstituts-
system. Um die Multibankfähigkeit zu gewährleisten, ist zusätzlich eine Beschrei-
bung der Schnittstelle zwischen Kundenprodukt und Sicherheitsmedium erforderlich.
Daher findet sich in [HBCI] eine Spezifikation der Schnittstelle zwischen einem
FinTS-Kundenprodukt und einer Chipkarte bzw. einer Diskette. Zur Abwicklung des
PIN/TAN-Verfahrens findet sich die Schnittstellenspezifikation in [PINTAN].


Abbildung 1: Übersicht der Schnittstellenbeziehungen

![Sicherheitsverfahren HBCI USB-Stick Chipkarte FinTS Benutzer FinTS Kreditinstitut Sicherheitsverfahren PIN/TAN chipTAN mobile TAN](figures/15.1)


Im Rahmen dieser Schnittstellenbeschreibung findet grundsätzlich keine Spezi-
fikation von Kunden- oder Kreditinstitutssystemen statt. Lediglich werden an einigen
gekennzeichneten Stellen Empfehlungen für die Präsentation im Kundenprodukt

<!-- PageBreak -->


<table>
<tr>
<td>Kapitel:<br>A</td>
<td>Version: 3.0-FV</td>
<td>Financial Transaction Services (FinTS) Dokument: Formals</td>
</tr>
<tr>
<td>Seite:<br>8</td>
<td>Stand: 06.10.2017</td>
<td>Kapitel: Einleitung</td>
</tr>
</table>


bzw. für die Verarbeitung im Kreditinstitutssystem gegeben.1 Diese Ausführungen
sind jedoch nicht als Teil der eigentlichen Schnittstellenspezifikation zu verstehen.

Grundsätzlich ist die Schnittstellenbeschreibung Plattform- und Endgeräte unabhän-
gig. Ein Teil dieser Empfehlungen erfordert jedoch intelligente Endgeräte mit lokaler
Speicherintelligenz.

Die Spezifikation ist als Schichtenstruktur aufgebaut und somit grundsätzlich unab-
hängig vom zugrunde liegenden Transportmedium. Um eine einheitliche und mult-
ibankfähige Schnittstelle zu gewährleisten, werden jedoch hierzu in den Anlagen
(Kap. I.4) einige grundsätzliche Festlegungen getroffen.

Für einzelne Teile der Schnittstelle (z. B. Signatur, Verschlüsselung und Standard-
Finanzdatenformate) wird in den Anlagen in [Master] auf weitere allgemein zugäng-
liche Spezifikationen verwiesen.

In [Messages] ist eine Vielfalt von Geschäftsvorfällen zwischen Kunde und Kreditin-
stitut beschrieben. Da hiermit jedoch nicht sämtliche Anforderungen aller beteiligten
Kreditinstitute abgebildet werden können, steht es den Verbänden der Deutschen
Kreditwirtschaft frei, eigene Geschäftsvorfälle, die in diesem Dokument nicht enthal-
ten sind, zu definieren und anzubieten. Die Klassifizierung in DK-weit definierte und
verbands- bzw. institutsspezifische Geschäftsvorfälle erfolgt dabei über die erste
Stelle der jeweiligen Segmentkennung (s. Kap. B.5.1).

Es werden folgende Segmentkennungen reserviert:

'Hxxxx':
DK-weit verabschiedete Geschäftsvorfälle

'Bxxxx':

Geschäftsvorfälle für den Bundesverband deutscher Banken e.V.

'Dxxxx':

Geschäftsvorfälle für den Deutschen Sparkassen- und Giroverband e.V.

'Gxxxx':
Geschäftsvorfälle für den Bundesverband der Deutschen Volksbanken
und Raiffeisenbanken e.V.

'Vxxxx':
Geschäftsvorfälle für den Bundesverband Öffentlicher Banken e.V.

'Xxxxx':

Bilateral vereinbarte Geschäftsvorfälle anderer Verbände/Institutionen

'Ixxxx':
Intern verwendete Segmente (Diese Segmente dürfen nur für die Pro-
grammierung von Kunden- und Bankprodukten verwendet werden. Sie
dürfen keinesfalls im Rahmen von FinTS-Nachrichten gesendet wer-
den).

Die Vergabe und Koordination der mit 'H' und 'X' beginnenden Kennungen über-
nimmt die DK. Die Vergabe und Koordination der übrigen Kennungen übernehmen
die jeweiligen Verbände. I-Segmente können von Herstellern bei Bedarf beliebig
verwendet werden. Kennungen, die diesen Definitionen nicht entsprechen, sind
nicht zulässig.

Für weitere Fragen und Informationen zu FinTS wenden Sie sich bitte an die unter
[www.fints.org](http://www.fints.org/) in der Rubrik ,Impressum" angegebenen Adressen.

<!-- PageFooter: 1 Das Symbol -->
<!-- PageFooter: steht für Hinweise an Kundenprodukthersteller. Das Symbol &bezeichnet Imple- mentierungshinweise für Banksysteme. -->
<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th rowspan="2">Version: 3.0-FV</th>
<th rowspan="2">Kapitel: B</th>
</tr>
<tr>
<th>Dokument:</th>
<th>Formals</th>
</tr>
<tr>
<td>Kapitel:<br>Abschnitt:</td>
<td>Nachrichtenaufbau Zeichensatz</td>
<td>Stand: 06.10.2017</td>
<td>Seite: 9</td>
</tr>
</table>


### B. NACHRICHTENAUFBAU


#### B.1 Zeichensatz

Der HBCI-Basiszeichensatz baut auf dem international normierten Zeichensatz
ISO 8859 auf. Im DE ,Unterstützte Sprachen“ in die Bankparameterdaten (s. Kap.
D.2) stellt das Kreditinstitut das jeweiligen Codeset des ISO 8859 ein.1 Ferner wird
in die BPD das sprachen-spezifische Subset des ISO 8859 eingestellt. Codeset und
Subset definieren gemeinsam den FinTS-Basiszeichensatz. Dieser gilt grundsätzlich
für sämtliche nicht-binären Datenelemente. Sofern hiervon aufgrund von Verarbei-
tungsrestriktionen abgewichen wird, ist dies bei der jeweiligen Formatbeschreibung
vermerkt. Für transparente Daten gilt der jeweilige Zeichensatz des Fremdformats.

Kreditinstitutsseitig ist jeweils der vollständige erlaubte Zeichensatz zu unterstützen.
FinTS-Syntaxzeichen (s. Kap. H.1.1) bleiben von den Zeichensatzvorgaben unbe-
rührt (d. h. sind stets erforderlich und mit fester Codierung vorgegeben).

Wird ein Auftrag an ein Kreditinstitut übermittelt, der hinsichtlich Zeichensatz und
Codierung nicht den Richtlinien entspricht, so ist dieser abzuweisen. Eine kreditinsti-
tutsseitige Korrektur der Auftragsdaten erfolgt nicht.


#### B.2 Nachrichtenelemente


##### ◆ Datenelemente

Datenelemente (DE) sind die kleinsten syntaktischen Informationseinheiten.


##### . Datenelementgruppen

Zusammengehörende Daten können zu einer syntaktischen Einheit zusammenge-
fasst werden. Diese Datenelementgruppen (DEG) bestehen wiederum aus Daten-
elementen. Jede DEG kann beliebig viele DE enthalten. Datenelementgruppen kön-
nen nur unter bestimmten Bedingungen Bestandteil einer Datenelementgruppe sein
(s. Kap. H.1)).


##### . Segmente

Datenelemente und Datenelementgruppen setzen sich zu Segmenten (SEG) zu-
sammen. Jedes Segment enthält bestimmte zusammengehörige Informationen (z.
B. Steuerinformationen, Nutzdaten oder Signatur). Die Segmente werden aus-
schlieBlich in der angegebenen Reihenfolge eingestellt, sofern eine Reihenfolge
vorgegeben ist.


##### . Segmentfolgen

Eine Segmentfolge (SF) beschreibt eine Gruppe von Segmenten, die nur gemein-
sam auftreten dürfen. Dabei handelt es sich nicht um eine syntaktische, sondern nur
um eine logische Einheit.


##### . Nachrichten

Die Kommunikation zwischen Kunde und Kreditinstitut erfolgt bei FinTS über Nach-
richten. Nachrichten setzen sich aus einer vorgegebenen Segmentabfolge zusam-
men (s. Abbildung). Ausnahmslos alle Nachrichten (Kunde an Kreditinstitut und um-
gekehrt) enthalten je ein Kopf- und ein Abschlusssegment. Alle weiteren Nachrich-

<!-- PageFooter: 1 Z.Zt. ist lediglich Codeset 1 (Latin 1) zugelassen. -->
<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: B</td>
<td>Version: 3.0-FV</td>
<td>Financial Transaction Services (FinTS) Dokument: Formals</td>
</tr>
<tr>
<td>Seite:<br>10</td>
<td>Stand: 06.10.2017</td>
<td>Kapitel: Nachrichtenaufbau<br>Abschnitt: Festlegungen</td>
</tr>
</table>


teninhalte werden ebenfalls in Segmente, die vom Aufbau her dem allgemeinen fes-
ten Segmentformat entsprechen, eingestellt. Der allgemeine Nachrichtenaufbau
(Segmentabfolge) ist in den jeweiligen Kapiteln zu Kunden- und Kreditinstitutsnach-
richten (B.6, B.7) beschrieben.


Abbildung 2: Nachrichtenaufbau

![Nachrichtenkopf Segmentkopf DE 1 Segment 1 DE 1 (DEG 1) . . Nachricht . . DEG 2 (DE 2) . . . . Segment n . . Nachrichten- abschluss DE n (DEG n) DE n](figures/18.1)


#### Β.3 Festlegungen


##### B.3.1 Status und Anzahl

Alle Datenstrukturen sind durch einen Existenzstatus beschrieben. Folgende Stati
sind möglich:


<table>
<tr>
<th>Code</th>
<th>Bedeutung</th>
<th>Erläuterung</th>
</tr>
<tr>
<td>M</td>
<td>Muss</td>
<td>Datenstruktur muss vorhanden sein und ist in- haltlich korrekt zu füllen</td>
</tr>
<tr>
<td>C</td>
<td>Konditional</td>
<td>Datenstruktur ist konditional, d. h. der Status (M = Muss, O = optional, N = Nicht erlaubt) ist von einer Bedingung (condition) abhängig</td>
</tr>
<tr>
<td>O</td>
<td>Optional</td>
<td>Datenstruktur ist optional</td>
</tr>
<tr>
<td>N</td>
<td>nicht erlaubt (not allowed)</td>
<td>Datenstruktur darf nicht vorhanden sein. Dieser Status ist nur im Zusammenhang mit dem Status ,Konditional' erlaubt.</td>
</tr>
</table>


In Zusammenhang mit der Angabe zur Anzahl des Auftretens ergeben sich folgende
Bedeutungen:

<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th rowspan="2">Version: 3.0-FV</th>
<th rowspan="2">Kapitel: B</th>
</tr>
<tr>
<th>Dokument:</th>
<th>Formals</th>
</tr>
<tr>
<td>Kapitel:<br>Abschnitt:</td>
<td>Nachrichtenaufbau Festlegungen</td>
<td>Stand: 06.10.2017</td>
<td>Seite: 11</td>
</tr>
</table>


<table>
<tr>
<th>Sta- tus</th>
<th>An- zahl</th>
<th>Bedeutung</th>
</tr>
<tr>
<td>O</td>
<td>1</td>
<td>Das Element kann einmal auftreten oder entfallen</td>
</tr>
<tr>
<td>O</td>
<td>m</td>
<td>Das Element kann bis zu m-mal auftreten oder entfallen</td>
</tr>
<tr>
<td>O</td>
<td>n</td>
<td>Das Element kann unbegrenzt oft auftreten oder entfallen</td>
</tr>
<tr>
<td>C</td>
<td>n</td>
<td>abhängig von der jeweiligen Regel</td>
</tr>
<tr>
<td>M</td>
<td>1</td>
<td>Das Element muss genau einmal auftreten</td>
</tr>
<tr>
<td>M</td>
<td>m</td>
<td>Das Element muss genau m-mal auftreten (m&gt;1)</td>
</tr>
<tr>
<td>M</td>
<td>n</td>
<td>Das Element kann unbegrenzt oft auftreten, muss aber mindestens 1-mal auftreten</td>
</tr>
<tr>
<td>M</td>
<td>l..m</td>
<td>Das Element kann bis zu m-mal, muss aber mindestens l-mal auftreten</td>
</tr>
</table>


Die Stati beziehen sich jeweils auf die beschriebene Syntaxebene. Stati übergeord-
neter Syntaxebenen sind hiervon unbenommen.

Beispiel:
Eine DEG hat den Status 'Optional', ihre DE haben den Status 'Muss'.

Bedeutung: Die DEG kann optional eingestellt werden. Wenn sie jedoch eingestellt
wird, müssen alle DE, die den Status 'Muss' haben, gefüllt werden.

Bei numerischen optionalen Elementen ist zwischen der Nichtbelegung und der Be-
legung mit dem Wert 0 zu unterscheiden.

Beispiel:
Stellt das Kreditinstitut in das Kann-DE ,,Dispokredit" den Wert '0' ein,
bedeutet dies, dass dem Kunde kein Kredit zur Verfügung steht. Stellt
es dagegen das DE nicht ein, so ist keine Interpretation des Kreditrah-
mens möglich.


##### B.3.2 Restriktionen

Durch Restriktionen können die Werte, die eine Datenstruktur annehmen kann, oder
die Bedingung, unter denen eine Datenstruktur auftreten kann, näher spezifiziert
werden. Restriktionen werden in der Datenstrukturtabelle beim jeweiligen Element
aufgeführt. Diese können sein:

· Zulässige Werte (insb. beim Datentyp ,code')

• Wertebereiche (z. B. > 100)

. konditionale Belegungsregeln

Konditionale Belegungsregeln treten in Verbindung mit dem Status „C“ (konditional)
auf. In diesem Fall beschreibt die Restriktion, unter welcher Bedingung das Element
welchen Status annimmt.

Beispiel:


<table>
<tr>
<th>Nr.</th>
<th>Name</th>
<th>Ver- sion</th>
<th>Typ</th>
<th>For- mat</th>
<th>Län- ge</th>
<th>Sta- tus</th>
<th>An- zahl</th>
<th>Restriktionen</th>
</tr>
<tr>
<td>1</td>
<td>Element</td>
<td>1</td>
<td>DE</td>
<td></td>
<td></td>
<td>C</td>
<td>1</td>
<td>M: &lt;Bedingung&gt; N: sonst</td>
</tr>
</table>


Bedeutung: Falls die Bedingung <Bedingung> vorliegt, muss das Element zwingend
auftreten. Andernfalls darf es nicht belegt werden.

<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: B</td>
<td>Version: 3.0-FV</td>
<td>Financial Transaction Services (FinTS) Dokument: Formals</td>
</tr>
<tr>
<td>Seite:<br>12</td>
<td>Stand: 06.10.2017</td>
<td>Kapitel: Nachrichtenaufbau<br>Abschnitt: Festlegungen</td>
</tr>
</table>


##### B.3.3 Längenangaben

Die Zahlen in der Tabellenspalte "Länge" geben jeweils die Länge des Datenele-
mentes in Byte an. Die Angabe bezieht sich auf die Darstellung vor Entwertung (vgl.
Kap. H.1.3), d. h. in entwerteter Darstellung kann die Zeichenkette evtl. eine größere
Länge aufweisen.

Es ist zwischen Maximal- und Festlängen zu unterscheiden. Sind der Längenanga-
be zwei Punkte '..' vorangestellt, so handelt es sich um eine Maximallänge. In die-
sem Fall darf das eingestellte Datenelement auch eine geringere Länge aufweisen.
Bei Festlängen dagegen führt jede Abweichung von der angegebenen Längenan-
gabe zu einem Syntaxfehler.

Die Angabe '..' ohne Ziffern kennzeichnet ein Datenelement beliebiger Länge (z. B.
externe Datenformate). Bei abgeleiteten Datenformaten (z. B. Datum, Uhrzeit) ist
die maximale Länge durch die Formatdefinition vorgegeben. Dieser Fall ist durch ein
'#' im Längenfeld gekennzeichnet. DEG besitzen weder ein Längen- noch ein For-
matfeld, da sich die Länge einer DEG aus der Summe der Längen der zugehörigen
DE ergibt. Die Länge von Binärdaten wird im Segment durch ein vorangestelltes
Längenfeld angegeben.


#### B.3.4 Transparente Daten

Im Rahmen dieser Schnittstelle werden gegebenenfalls Daten gemäß anderer
Standards und Formate (z. B. SEPA, camt) transparent eingestellt. Diese trans-
parent eingestellten Daten werden wie binäre Daten behandelt. Somit haben die Be-
legungs- und Formatregeln (auch Zeichensatzkonventionen) des FinTS-Standards
an dieser Stelle keinen Einfluss. An dessen Stelle treten die Belegungs- und For-
matregeln des jeweiligen Formatstandards. Institutsindividuelle Belegungen sind bei
transparenten Formaten nicht zugelassen.


#### B.3.5 Datum und Uhrzeit

Generell besitzen Datums- und Uhrzeitangaben, die von Kundensystemen automa-
tisch generiert werden (z. B. Zeitpunkt der Signatur), keinen rechtsverbindlichen
Charakter, da nicht davon ausgegangen werden kann, dass Kundensysteme diese
Daten korrekt erzeugen.

Datum und Uhrzeit, die vom Kundensystem gesendet werden, besitzen somit keine
verarbeitungstechnische Bedeutung, sondern lediglich dokumentarischen Charak-
ter. Dies bezieht sich nicht auf Datums- und Uhrzeitangaben, die vom Kunden selbst
eingegeben werden (z. B. Ausführungsdatum von terminierten Überweisungen).

<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th rowspan="2">Version: 3.0-FV</th>
<th rowspan="2">Kapitel: B</th>
</tr>
<tr>
<th>Dokument:</th>
<th>Formals</th>
</tr>
<tr>
<td>Kapitel: Abschnitt:</td>
<td>Nachrichtenaufbau Datenformate</td>
<td>Stand: 06.10.2017</td>
<td>Seite: 13</td>
</tr>
</table>


#### B.4 Datenformate


##### B.4.1 Basisformate

Grundsätzlich sind Daten nicht durch Leerzeichen auf feste Längen aufzufüllen. Alle
Daten mit Ausnahme von Binärdaten müssen um führende und nachfolgende Leer-
zeichen gekürzt werden, bevor sie in die Nachricht eingestellt werden.


<table>
<tr>
<th>Name</th>
<th>Ken- nung</th>
<th>Beschreibung</th>
</tr>
<tr>
<td>Alphanumerisch</td>
<td>an</td>
<td>Es gilt der FinTS-Basiszeichensatz ohne die Zeichen CR und LF.</td>
</tr>
<tr>
<td>Text</td>
<td>txt</td>
<td>Es gilt der vollständige FinTS-Basiszeichensatz.</td>
</tr>
<tr>
<td>DTAUS-Zeichensatz</td>
<td>dta</td>
<td>Es gilt der DTAUS-Zeichensatz mit der entsprechenden Co- dierung.<br>2</td>
</tr>
<tr>
<td>Numerisch</td>
<td>num</td>
<td>Zulässig sind lediglich die Ziffern '0' bis '9'. Führende Nullen sind nicht zugelassen.</td>
</tr>
<tr>
<td>Ziffern</td>
<td>dig</td>
<td>Zulässig sind die Ziffern '0' bis '9'. Führende Nullen sind zu- gelassen.</td>
</tr>
<tr>
<td>Fließkommadar- stellung</td>
<td>float</td>
<td>Es gelten die Ausführungen zu numerischen Daten. Zusätz- lich ist als Dezimaltrennzeichen das Komma erlaubt. Es gelten folgende Regeln bzgl. der Bildung von Fließkom- mazahlen:<br>. Der Integer-Teil einer Fließkommazahl hat aus mindes- tens einem Zeichen zu bestehen.<br>. Nachkommastellen mit dem Wert 0 sind von rechts zu kürzen.<br>• Führende Nullen sind nicht zugelassen (Ausnahme: Werte mit dem Betrag kleiner 1 müssen eine führende Null ha- ben).<br>· Das Komma als Dezimaltrennzeichen ist obligatorisch.<br>Beispiele: 100,00 → 100, 100,20 → 100,2<br>4.567,89 → 4567,89<br>0 → 0,<br>0,50 → 0,5</td>
</tr>
<tr>
<td>Binär</td>
<td>bin</td>
<td>Binäre Daten werden unverändert in den FinTS-Datensatz eingestellt. Eine Umwandlung in eine Zeichendarstellung er- folgt nicht. Es ist zu beachten, dass der FinTS-Basiszeichen- satz für binäre Daten keine Gültigkeit besitzt. Ferner gelten die speziellen Syntaxregeln für binäre Daten (s. Kap. H.1.3).</td>
</tr>
<tr>
<td>Kapitel:</td>
<td>Version:</td>
<td>Financial Transaction Services (FinTS)</td>
</tr>
<tr>
<td>B</td>
<td>3.0-FV</td>
<td>Dokument: Formals</td>
</tr>
<tr>
<td>Seite:</td>
<td>Stand:</td>
<td>Kapitel: Nachrichtenaufbau</td>
</tr>
<tr>
<td>14</td>
<td>06.10.2017</td>
<td>Abschnitt: Datenformate</td>
</tr>
</table>


##### B.4.2 Abgeleitete Formate

Nachstehende aus den oben genannten Basisformaten abgeleitete Formate haben
stets den folgenden Aufbau:


<table>
<tr>
<th>Name</th>
<th>Ken- nung</th>
<th>Basis- format</th>
<th>Län- ge</th>
<th>Beschreibung</th>
</tr>
<tr>
<td>Ja/Nein</td>
<td>jn</td>
<td>an</td>
<td>1</td>
<td>Format: J bzw. N (in Großbuchstaben) Hat das DE den Status ,Kann", so gilt bei Auslassung der Standardwert ,,N“.</td>
</tr>
<tr>
<td>Code</td>
<td>code</td>
<td>an</td>
<td>#</td>
<td>Es sind nur die jeweils aufgeführten Werte zulässig.</td>
</tr>
<tr>
<td>Datum</td>
<td>dat</td>
<td>num</td>
<td>8</td>
<td>Format: JJJJMMTT gemäß ISO 8601 Erlaubt sind alle existenten Datumsangaben.</td>
</tr>
<tr>
<td>Virtuelles Datum</td>
<td>vdat</td>
<td>num</td>
<td>8</td>
<td>Format: JJJJMMTT gemäß ISO 8601 Unabhängig vom Monat sind jeweils 31 Tage möglich (z. B. 31.04. als Valutadatum für Zinsabschlüsse oder Ausführungsdatum von Daueraufträgen).</td>
</tr>
<tr>
<td>Uhrzeit</td>
<td>tim</td>
<td>dig</td>
<td>6</td>
<td>Format: hhmmss gemäß ISO 8601 Gültige Uhrzeit. Es ist immer Ortszeit des sendenden Systems einzustellen. Unter- schiedliche Zeitzonen werden nicht unter- stützt</td>
</tr>
<tr>
<td>Identifikation</td>
<td>id</td>
<td>an</td>
<td>..30</td>
<td>dient der eindeutigen Kennzeichnung von Objekten (z. B. Benutzerkennung, Kontonum- mer)</td>
</tr>
<tr>
<td>Länderkennzeichen</td>
<td>ctr</td>
<td>dig</td>
<td>3</td>
<td>Kennzeichen gemäß ISO 3166-1 (numeri- scher Code)</td>
</tr>
<tr>
<td>Währung</td>
<td>cur</td>
<td>an</td>
<td>3</td>
<td>Kennzeichen gemäß ISO 4217 (alphabeti- scher Code) in Großbuchstaben4</td>
</tr>
<tr>
<td>Wert</td>
<td>wrt</td>
<td>float</td>
<td>..15</td>
<td>Fließkommabetrag (z. B. für Wertbeträge o- der Zinssätze)</td>
</tr>
</table>


<!-- PageFooter: 3 s. [Messages], Anlagen -->
<!-- PageFooter: 4 s. [Messages], Anlagen -->
<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th rowspan="2">Version: 3.0-FV</th>
<th rowspan="2">Kapitel: B</th>
</tr>
<tr>
<th>Dokument:</th>
<th>Formals</th>
</tr>
<tr>
<td>Kapitel:<br>Abschnitt:</td>
<td>Steuerstrukturen<br>Nachrichtenaufbau</td>
<td>Stand: 06.10.2017</td>
<td>Seite: 15</td>
</tr>
</table>


#### B.5 Steuerstrukturen


##### B.5.1 Segmentkopf


##### . Beschreibung

Informationen, die jedem Segment als Kopfteil vorangestellt sind. Im Unterschied zu
Nachrichten enthalten Segmente jedoch keinen Abschlussteil, da das Segmentende
durch das Segmentende-Zeichen markiert ist.

Im Segmentkopf stehen die Segmentkennung und Segmentversion unabhängig von
der FinTS-Version (s. DE ,,HBCI-Version") immer an derselben Stelle, damit ein
Segment auch in späteren FinTS-Versionen immer eindeutig als solches identifiziert
werden kann.


##### . Format

siehe Data-Dictionary


#### B.5.2 Nachrichtenkopf


##### . Beschreibung

Nachstehender Kopfteil führt alle Kunden- und Kreditinstitutsnachrichten an.


##### . Format


<table>
<tr>
<td>Name:</td>
<td>Nachrichtenkopf</td>
<td></td>
</tr>
<tr>
<td>Typ:</td>
<td>Segment</td>
<td></td>
</tr>
<tr>
<td>Segmentart:</td>
<td>Administration</td>
<td></td>
</tr>
<tr>
<td>Kennung:</td>
<td>HNHBK</td>
<td></td>
</tr>
<tr>
<td>Bezugssegment:</td>
<td>-</td>
<td></td>
</tr>
<tr>
<td>Version:</td>
<td>3</td>
<td></td>
</tr>
<tr>
<td>Sender:</td>
<td>Kunde/Kreditinstitut</td>
<td></td>
</tr>
</table>


<table>
<tr>
<th>Nr.</th>
<th>Name</th>
<th>Ver- sion</th>
<th>Typ</th>
<th>For- mat</th>
<th>Län- ge</th>
<th>Sta- tus</th>
<th>An- zahl</th>
<th>Restriktionen</th>
</tr>
<tr>
<td>1</td>
<td>Segmentkopf</td>
<td>1</td>
<td>DEG</td>
<td></td>
<td></td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>2</td>
<td>Nachrichtengröße</td>
<td>1</td>
<td>DE</td>
<td>dig</td>
<td>12</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>3</td>
<td>HBCI-Version</td>
<td>1</td>
<td>DE</td>
<td>num</td>
<td>..3</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>4</td>
<td>Dialog-ID</td>
<td>1</td>
<td>DE</td>
<td>id</td>
<td>#</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>5</td>
<td>Nachrichtennum- mer</td>
<td>1</td>
<td>DE</td>
<td>num</td>
<td>.4</td>
<td>M</td>
<td>1</td>
<td>&gt;0</td>
</tr>
<tr>
<td>6</td>
<td>Bezugsnachricht</td>
<td>1</td>
<td>DEG</td>
<td></td>
<td></td>
<td>C</td>
<td>1</td>
<td>M: bei Kreditinstitutsnach- richten N: bei Kundennachrichten</td>
</tr>
</table>


### . Belegungsrichtlinien


### HBCI-Version

Für die in diesem Dokument beschriebene HBCI-Version muss der Wert
,300' (für Version 3.0) eingestellt werden.


### B.5.3 Nachrichtenabschluss


### . Beschreibung

Dieses Segment beendet alle Kunden- und Kreditinstitutsnachrichten.

<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: B</td>
<td>Version: 3.0-FV</td>
<td>Financial Transaction Services (FinTS) Dokument: Formals</td>
</tr>
<tr>
<td>Seite:<br>16</td>
<td>Stand: 06.10.2017</td>
<td>Kapitel: Nachrichtenaufbau<br>Abschnitt: Steuerstrukturen</td>
</tr>
</table>


### . Format


<table>
<tr>
<td>Name:</td>
<td>Nachrichtenabschluss</td>
</tr>
<tr>
<td>Typ:</td>
<td>Segment</td>
</tr>
<tr>
<td>Segmentart:</td>
<td>Administration</td>
</tr>
<tr>
<td>Kennung:</td>
<td>HNHBS</td>
</tr>
<tr>
<td>Bezugssegment:</td>
<td>-</td>
</tr>
<tr>
<td>Version:</td>
<td>1</td>
</tr>
<tr>
<td>Sender:</td>
<td>Kunde/Kreditinstitut</td>
</tr>
</table>


<table>
<tr>
<th>Nr.</th>
<th>Name</th>
<th>Ver- sion</th>
<th>Typ</th>
<th>For- mat</th>
<th>Län- ge</th>
<th>Sta- tus</th>
<th>An- zahl</th>
<th>Restriktionen</th>
</tr>
<tr>
<td>1</td>
<td>Segmentkopf</td>
<td>1</td>
<td>DEG</td>
<td></td>
<td></td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>2</td>
<td>Nachrichten- nummer</td>
<td>1</td>
<td>DE</td>
<td>num</td>
<td>..4</td>
<td>M</td>
<td>1</td>
<td>&gt;0</td>
</tr>
</table>


### . Belegungsrichtlinien


### Nachrichtennummer

Es ist die Nummer der Nachricht einzustellen, die auch im Nachrichtenkopf
eingestellt ist.

<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th rowspan="2">Version: 3.0-FV</th>
<th rowspan="2">Kapitel: B</th>
</tr>
<tr>
<th>Dokument:</th>
<th>Formals</th>
</tr>
<tr>
<td>Kapitel:<br>Abschnitt:</td>
<td>Nachrichtenaufbau Kundennachrichten allgemein</td>
<td>Stand: 06.10.2017</td>
<td>Seite: 17</td>
</tr>
</table>


## B.6 Kundennachrichten allgemein


### B.6.1 Allgemeiner Nachrichtenaufbau


### . Beschreibung

In einer Nachricht sind Aufträge beliebiger unterschiedlicher Geschäftsvorfallsarten
zugelassen (z. B. drei Segmente HKCCS und ein Segment HKSAL). Eine Ein-
schränkung ist mit Hilfe des Feldes „Anzahl Geschäftsvorfallsarten" im Segment
„Bankparameter allgemein“ möglich.

Bezüglich der Reihenfolge der in die Nachricht einzustellenden Aufträge wird keine
Vorgabe getroffen. Da die Reihenfolge der Weiterleitung von Aufträgen an die Ver-
arbeitungssysteme institutsspezifisch ist, beeinflusst die Anordnung der Aufträge
nicht zwingend die Reihenfolge der Verarbeitung bzw. Ausführung. Insbesondere ist
daher auch keine kundenseitige Priorisierung der Aufträge durch deren Anordnung
in der Nachricht möglich.


![](figures/25.1)


Eine Priorisierung von Aufträgen könnte für den Kunden u. U. wün-
schenswert sein, wenn bei geringer Deckung des Kontos mehrere
Zahlungsaufträge mit unterschiedlicher Priorität ausgeführt werden
sollen. In diesem Fall sollten zuerst die wichtigen Aufträge ausge-
führt werden. Da die eingereichten Zahlungsaufträge nicht notwen-
digerweise in dieser Reihenfolge ausgeführt werden, könnte das
Kundenprodukt vor dem Versenden automatisch den Kontensaldo
(und ggf. Kontokorrentkredit) abfragen und mit der Summe der Zah-
lungsaufträge vergleichen. Sind alle Aufträge gedeckt, können sie
automatisch versendet werden. Bei mangelnder Deckung kann dies
dem Kunden mitgeteilt werden, damit er zunächst lediglich die Auf-
träge mit hoher Priorität einreicht.

Werden in einer Nachricht Aufträge mit verschiedenen Signaturvorschriften ge-
mischt, so werden diejenigen Aufträge der Nachricht ausgeführt, für welche die Si-
gnatur ausreichend ist.


![](figures/25.2)


Falls der Kunde Aufträge verschiedener Geschäftsvorfallsarten oder
Signaturvorschriften formuliert und diese zusammen abschicken
möchte, so obliegt es dem Kundenprodukt, die Aufträge jeweils in
Nachrichten mit gleichem Geschäftsvorfall und Signatur aufzuteilen
und diese nacheinander zu verschicken.

Das Kundenprodukt sollte grundsätzlich vor dem Senden des Auf-
trags anhand der in den UPD übermittelten Daten prüfen, ob der
vom Kunden gewählte Geschäftsvorfall für das angegebene Konto
zulässig ist.


#### . Format


<table>
<tr>
<td>Name:</td>
<td>Kundennachricht allgemein</td>
</tr>
<tr>
<td>Typ:</td>
<td>Nachricht</td>
</tr>
<tr>
<td>Version:</td>
<td>4</td>
</tr>
<tr>
<td>Sender:</td>
<td>Kunde</td>
</tr>
</table>


<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: B</td>
<td>Version: 3.0-FV</td>
<td>Financial Transaction Services (FinTS) Dokument: Formals</td>
</tr>
<tr>
<td>Seite:<br>18</td>
<td>Stand: 06.10.2017</td>
<td>Kapitel: Nachrichtenaufbau<br>Abschnitt:<br>Kundennachrichten allgemein</td>
</tr>
</table>


<table>
<tr>
<th>Nr.</th>
<th>Name</th>
<th>Ver- sion</th>
<th>Typ</th>
<th>Ken- nung</th>
<th>Sta- tus</th>
<th>An- zahl</th>
<th>Anmerkungen</th>
</tr>
<tr>
<td>1</td>
<td>Nachrichtenkopf</td>
<td>3</td>
<td>SEG</td>
<td>HNHBK</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>2</td>
<td>Signaturkopf</td>
<td>4</td>
<td>SEG</td>
<td>HNSHK</td>
<td>M</td>
<td>1..3</td>
<td>s. [HBCI], Kap. B.5.1</td>
</tr>
<tr>
<td>3</td>
<td>Aufträge</td>
<td>2</td>
<td>SF</td>
<td>#</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>4</td>
<td>Zwei-Schritt-TAN- Einreichung</td>
<td>≥6</td>
<td>SEG</td>
<td>HKTAN</td>
<td>O</td>
<td>1</td>
<td>s. [PINTAN], Kap. B.3.3 und B.4</td>
</tr>
<tr>
<td>5</td>
<td>Signaturabschluss</td>
<td>2</td>
<td>SEG</td>
<td>HNSHA</td>
<td>M</td>
<td>1..3</td>
<td>s. [HBCI], Kap. B.5.2</td>
</tr>
<tr>
<td>6</td>
<td>Nachrichtenab- schluss</td>
<td>1</td>
<td>SEG</td>
<td>HNHBS</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
</table>


### . Belegungsrichtlinien


#### Signaturkopf

Je nach Nachrichtentyp ist hier die Signatur des Übermittlers bzw. Die Signa-
tur des Unterzeichners einzustellen.

Der Signaturkopf darf nur bei Mehrfachsignaturen mehrfach eingestellt wer-
den.


#### Zwei-Schritt-TAN-Einreichung

Zur Einleitung des Prozesses der Gewährleistung einer starken Kun-
denauthentifizierung gemäß [PSD2] muss bei TAN-Verfahren ein HKTAN-
Segment ab Segmentversion #6 eingestellt werden, wenn ein Kreditinstitut
die Verwendung von HKTAN#6 unterstützt (BPD). Ansonsten kann der Dialog
vom Institut mit dem Rückmeldungscode 9075 - Dialog abgebrochen
\- Starke Authentifizierung erforderlich abgewiesen werden.


#### Signaturabschluss

Der Signaturabschluss darf nur bei Mehrfachsignaturen mehrfach eingestellt
werden. Die Anzahl der Signaturabschlusssegmente muss mit der Anzahl
der Signaturkopfsegmente übereinstimmen.


Abbildung 3: Logischer Nachrichtenaufbau

![Nachricht Auftragsart Auftrag 1 Auftrag 2 Auftrag n](figures/26.1)


<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th rowspan="2">Version: 3.0-FV</th>
<th rowspan="2">Kapitel: B</th>
</tr>
<tr>
<th>Dokument:</th>
<th>Formals</th>
</tr>
<tr>
<td>Kapitel:<br>Abschnitt:</td>
<td>Nachrichtenaufbau Kundennachrichten allgemein</td>
<td>Stand: 06.10.2017</td>
<td>Seite: 19</td>
</tr>
</table>


## B.6.2 Aufträge


### . Beschreibung

Die Segmentfolge enthält die in [Messages] definierten Auftragssegmente des Kun-
den. Jedes Segment kann dabei beliebig oft und in beliebiger Reihenfolge auftreten.
Das Kreditinstitut hat jedoch mit Hilfe der Bankparameterdaten die Möglichkeit, die
Art und Anzahl der erlaubten Segmente einzuschränken:

. Die erlaubten Kundensegmente gibt das Kreditinstitut in den Geschäftsvorfallpa-
rametern an (s. Kap. D.6)

· Die maximale Anzahl von Geschäftsvorfallssegmenten pro Nachricht kann mit
Hilfe des DE ,,Maximale Anzahl Aufträge“ eingestellt werden (s. Kap. D.6).

• Die maximale Anzahl von Geschäftsvorfallsarten pro Nachricht kann mit Hilfe des
DE „Anzahl Geschäftsvorfallsarten" eingestellt werden (s. Kap. D.2).


<table>
<tr>
<td colspan="2">. Format</td>
</tr>
<tr>
<td>Name:</td>
<td>Aufträge</td>
</tr>
<tr>
<td>Typ:</td>
<td>Segmentfolge</td>
</tr>
<tr>
<td>Sender:</td>
<td>Kunde</td>
</tr>
<tr>
<td>Version:</td>
<td>2</td>
</tr>
</table>


## B.6.3 Abholauftrag


### . Beschreibung

Abholaufträge werden an das Kreditinstitut gesendet, um die institutsseitige Gene-
rierung und Übermittlung von spezifischen Informationen einzuleiten (z. B. Konto-
umsätze, Börsenkurse). In Abgrenzung dazu haben Transaktionsaufträge nicht nur
einen Informationsfluss, sondern reale Transaktionen zur Folge (z. B. Überwei-
sungsauftrag).

Falls im Abholauftrag keine Währung angegeben wird, entspricht die Währung, in
der die Kreditinstitutsantwort auf den Abholauftrag erfolgt, stets der Währung des
Kundenkontos.


### . Format

Das Segmentformat ist beim jeweiligen Geschäftsvorfall spezifiziert. Die Erläute-
rungen beziehen sich auf die dort angegebenen Felder.


### ◆ Erläuterungen


### Kontoverbindung Auftraggeber

Es ist diejenige Kontoverbindung des Kunden einzustellen, für die im Abhol-
auftrag Daten zurückgemeldet werden sollen. Falls der noch zur Ausführung
anstehende Auftrag nicht in Beziehung zu einem bestimmten Konto steht (z.
B. Abruf von Devisenkursen, Abruf des Statusprotokolls), so ist eine beliebi-
ge Kontoverbindung des Kunden einzustellen. Es darf nur ein Konto eines
Kreditinstituts angegeben werden, für das sich der Kunde im Rahmen der
Dialoginitialisierung legitimiert hat.


### Alle Konten

Mit dieser Option kann gewählt werden, ob die angeforderten Informationen
(z. B. Salden, Umsätze) nur zu dem angegebenen oder zu allen Anlagekon-
ten des Kunden, für die er eine Zugriffsberechtigung besitzt, zurückgemeldet
werden sollen.

<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: B</td>
<td>Version: 3.0-FV</td>
<td>Financial Transaction Services (FinTS) Dokument: Formals</td>
</tr>
<tr>
<td>Seite:<br>20</td>
<td>Stand: 06.10.2017</td>
<td>Kapitel: Nachrichtenaufbau<br>Abschnitt: Kundennachrichten allgemein</td>
</tr>
</table>


![](figures/28.1)


Zur Zeit können Aufsetzpunkte evtl. nicht korrekt zugewiesen
werden, wenn mehrere Antwortsegmente gesendet werden.
Daher sollte die Option ,,Alle Konten" nur erlaubt werden,
wenn ein Aufsetzpunkt aufgrund der bankseitigen Verarbei-
tung nicht vorkommen kann.


## Von Datum, Bis Datum

Mit Hilfe dieser Angaben kann die Menge der zurückzumeldenden Daten
(z. B. Buchungspositionen) anhand eines Zeitraums eingegrenzt werden.
Wird kein Zeitraum angegeben, so werden stets alle verfügbaren Einträge
zurückgemeldet. Wird ein Zeitraum angegeben, so werden nur diejenigen
Einträge zurückgemeldet, die im Zeitraum (einschließlich des Grenzdatums)
liegen. Die Eingabemöglichkeiten sind der nachfolgenden Tabelle zu ent-
nehmen.

Falls der Zeitraum inkonsistent ist (Anfangsdatum größer als Enddatum),
wird der Auftrag abgelehnt. Ein Zeitraum darf nicht gleichzeitig mit einem
Kennungsbereich (s. u.) angegeben werden.


### Beispiele:


<table>
<tr>
<th>Von Datum</th>
<th>Bis Datum</th>
<th>Bedeutung</th>
</tr>
<tr>
<td>01.07.2016</td>
<td>31.07.2016</td>
<td>liefert alle Einträge, die im angegebenen Zeitraum liegen</td>
</tr>
<tr>
<td>01.07.2016</td>
<td>leer</td>
<td>liefert alle Einträge, die am 1.7.2016 oder danach angefallen sind</td>
</tr>
<tr>
<td>leer</td>
<td>31.07.2016</td>
<td>liefert alle Einträge, die am 31.7.2016 oder davor angefallen sind</td>
</tr>
<tr>
<td>leer</td>
<td>leer</td>
<td>liefert alle verfügbaren Einträge</td>
</tr>
</table>


## Von <Kennung>, Bis <Kennung>

Hier kann der Abholbereich durch bankfachliche Informationen (z. B. Dauer-
auftrags-ID, Wertpapiernamen) eingegrenzt bzw. genauer spezifiziert wer-
den, sofern dies durch den betreffenden Geschäftsvorfall unterstützt wird.

Falls die Informationen zu einer bestimmten Kennung (z. B. Kontonummer
xy) abgeholt werden sollen, so ist in beide Felder dieselbe Kennung einzu-
tragen.

Im Übrigen gelten die Festlegungen zu den Feldern ,,Von Datum“ und ,Bis
Datum".


## Aufsetzpunkt

Falls das Kreditinstitut den Kundenauftrag nicht in einem einzigen Auftrags-
segment beantworten kann, besteht die Möglichkeit, dass es die Beantwor-
tung an einem bestimmten Punkt kontrolliert beendet und dem Kunden in der
Antwortnachricht mit dem Rückmeldungscode einen Aufsetzpunkt mitteilt.
Hierzu ist der spezielle Rückmeldungscode 3040 (,Es liegen weitere Infor-
mationen vor") vorgesehen. Der Aufsetzpunkt kann ein beliebiger institutsin-
terner Ordnungsbegriff sein, der vom Kundenprodukt nicht interpretiert zu
werden braucht. Bei transparenten Daten kann die Fragmentierung beliebig

<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th rowspan="2">Version: 3.0-FV</th>
<th rowspan="2">Kapitel: B</th>
</tr>
<tr>
<th>Dokument:</th>
<th>Formals</th>
</tr>
<tr>
<td>Kapitel: Abschnitt:</td>
<td>Nachrichtenaufbau Kundennachrichten allgemein</td>
<td>Stand: 06.10.2017</td>
<td>Seite: 21</td>
</tr>
</table>


(z. B. logisch oder binär) erfolgen. Es ist lediglich zu fordern, dass die Zu-
sammensetzung der Fragmente im Kundensystem problemlos möglich ist.


![](figures/29.1)


Grundsätzlich hat das Kreditinstitutssystem dafür Sorge zu
tragen, dass auch bei umfangreichen Abholaufträgen (z. B.
Abruf der Kontoumsätze der vergangenen drei Jahre oder
Abruf sämtlicher verfügbarer Börsenkurse) die komplette In-
formation in einem Antwortsegment übertragen wird. D .h. es
muss ausgeschlossen sein, dass als Antwort auf einen Ab-
holauftrag dem Kunden wegen zu großer Antwortnachricht
nur ein Teil der geforderten Informationen zurückgemeldet
wird. Seitens des Kreditinstituts besteht jedoch bei Über-
schreitung von Zeit- oder Volumengrenzen die Möglichkeit,
den Auftrag abzulehnen.


![](figures/29.2)


Falls das Kreditinstitut jedoch einen Aufsetzpunkt rückmel-
det, wird vom Kundenprodukt erwartet, dass es denselben
Abholauftrag unter Hinzufügung des Aufsetzpunktes erneut
schickt. In der Antwortnachricht erhält der Kunde den fol-
genden Teil der Informationen (evtl. inkl. eines erneuten Auf-
setzpunktes) rückgemeldet. Dieses Verfahren kann sich so-
lange wiederholen, bis die komplette Informationsmenge
übertragen wurde. Die Generierung der Folgenachrichten
sollte automatisch, d. h. ohne Einwirkung des Kunden, erfol-
gen.

Ein Aufsetzpunkt darf vom Kundenprodukt nur dann einge-
stellt werden, wenn im selben Dialog ein Aufsetzpunkt vom
Kreditinstitut rückgemeldet wurde. Nach Beendigung des Di-
aloges verliert der Aufsetzpunkt seine Gültigkeit.


## Maximale Anzahl Einträge

Dieser Parameter dient dazu, die maximale Anzahl zurück zu meldender Ein-
träge zu begrenzen. Diese Begrenzung kann auf Wunsch des Kunden erfol-
gen oder aus technischen Restriktionen des Kundensystems resultieren. So
wird Endgeräten, die aufgrund technischer Restriktionen nur eine begrenzte
Anzahl rückgemeldeter Einträge (z. B. Umsatzinformationen im Kontoaus-
zug) verarbeiten können, die Möglichkeit gegeben, den Umfang der Instituts-
nachrichten zu begrenzen. Falls der Kunde keine Begrenzung wünscht, wird
das DE ausgelassen. Der Wert 0 ist nicht zulässig.

Falls im angegebenen Bereich weniger Einträge vorliegen als in „Maximale
Anzahl Einträge“ angegeben, werden nur die vorliegenden Einträge zurück
gemeldet. Falls mehr Einträge vorliegen, werden laut untenstehender Tabel-
le nur <Anzahl> Einträge zurück gemeldet. In diesem Fall erhält das Kun-
densystem im Rückmeldungscode mitgeteilt, dass noch weitere Informa-
tionen vorliegen. Im Rückmeldungsparameter wird dem Kundensystem ein
Aufsetzpunkt (s. o.) zurückgemeldet, mit Hilfe dessen die über <Anzahl>
hinausgehenden Einträge abgerufen werden können.

<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: B</td>
<td>Version: 3.0-FV</td>
<td>Financial Transaction Services (FinTS) Dokument: Formals</td>
</tr>
<tr>
<td>Seite: 22</td>
<td>Stand: 06.10.2017</td>
<td>Kapitel: Nachrichtenaufbau<br>Abschnitt: Kundennachrichten allgemein</td>
</tr>
</table>


## Beispiel:


<table>
<tr>
<th>Von Datum</th>
<th>Bis Datum</th>
<th>Anzahl</th>
<th>Bedeutung</th>
</tr>
<tr>
<td>01.07.2016</td>
<td>31.07.2016</td>
<td>10</td>
<td>liefert die ersten 10 Einträge ab 1.7.2016 (sofern mindestens 10 Einträge vorhanden, sonst weniger)</td>
</tr>
<tr>
<td>01.07.2016</td>
<td>leer</td>
<td>10</td>
<td>liefert die ersten 10 Einträge ab 1.7.2016</td>
</tr>
<tr>
<td>leer</td>
<td>31.07.2016</td>
<td>10</td>
<td>liefert die letzten 10 Einträge vor dem 31.07.2016</td>
</tr>
<tr>
<td>leer</td>
<td>leer</td>
<td>10</td>
<td>liefert von allen verfügbaren Einträgen die letzten 10</td>
</tr>
</table>


![](figures/30.1)


Die Einträge werden dem Kunden stets in aufsteigender
Reihenfolge rückgemeldet. Eine hiervon abweichende Sor-
tierung (z. B. absteigend oder nach anderen Kriterien) kann
das Kundenprodukt bei Bedarf dem Kunden anbieten.


### ◆ Ausgewählte Beispiele für Rückmeldungscodes


<table>
<tr>
<td>Code</td>
<td>Beispiel für Rückmeldungstext</td>
</tr>
<tr>
<td>0020</td>
<td>Auftrag ausgeführt</td>
</tr>
<tr>
<td>3010</td>
<td>Es liegen keine Einträge vor</td>
</tr>
<tr>
<td>3040</td>
<td>Auftrag nur teilweise ausgeführt</td>
</tr>
<tr>
<td>3040</td>
<td>Es liegen weitere Informationen vor</td>
</tr>
<tr>
<td>9210</td>
<td>Keine gültige Kontoverbindung des Kunden</td>
</tr>
<tr>
<td>9210</td>
<td>Zeitraum hier nicht erlaubt</td>
</tr>
<tr>
<td>9210</td>
<td>Kennungen hier nicht erlaubt</td>
</tr>
<tr>
<td>9210</td>
<td>Bereichende darf nicht vor Bereichanfang liegen</td>
</tr>
<tr>
<td>9210</td>
<td>Aufsetzpunkt unbekannt</td>
</tr>
</table>


<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th rowspan="2">Version: 3.0-FV</th>
<th rowspan="2">Kapitel: B</th>
</tr>
<tr>
<th>Dokument:</th>
<th>Formals</th>
</tr>
<tr>
<td>Kapitel:<br>Abschnitt:</td>
<td>Nachrichtenaufbau Kreditinstitutsnachrichten allgemein</td>
<td>Stand: 06.10.2017</td>
<td>Seite: 23</td>
</tr>
</table>


## B.7 Kreditinstitutsnachrichten allgemein


### B.7.1 Allgemeiner Nachrichtenaufbau


### . Beschreibung

Der nachfolgend beschriebene Nachrichtenaufbau bezieht sich auf unverschlüsselte
Nachrichten (Aufbau verschlüsselter Nachrichten vgl. Kap. B.8).


### . Format


<table>
<tr>
<td>Name:</td>
<td>Kreditinstitutsnachricht allgemein</td>
</tr>
<tr>
<td>Typ:</td>
<td>Nachricht</td>
</tr>
<tr>
<td>Version:</td>
<td>4</td>
</tr>
<tr>
<td>Sender:</td>
<td>Kreditinstitut</td>
</tr>
</table>


<table>
<tr>
<th>Nr.</th>
<th>Name</th>
<th>Ver- sion</th>
<th>Typ</th>
<th>Ken- nung</th>
<th>Sta- tus</th>
<th>An- zahl</th>
<th>Anmerkungen</th>
</tr>
<tr>
<td>1</td>
<td>Nachrichtenkopf</td>
<td>3</td>
<td>SEG</td>
<td>HNHBK</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>2</td>
<td>Signaturkopf</td>
<td>4</td>
<td>SEG</td>
<td>HNSHK</td>
<td>O</td>
<td>1</td>
<td>s. [HBCI], Kap. B.5.1</td>
</tr>
<tr>
<td>3</td>
<td>Rückmeldungen zur Gesamtnachricht</td>
<td>2</td>
<td>SEG</td>
<td>HIRMG</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>4</td>
<td>Rückmeldungen zu Segmenten</td>
<td>2</td>
<td>SEG</td>
<td>HIRMS</td>
<td>O</td>
<td>n</td>
<td></td>
</tr>
<tr>
<td>5</td>
<td>Datensegmente</td>
<td>2</td>
<td>SF</td>
<td>#</td>
<td>O</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>6</td>
<td>Zwei-Schritt-TAN- Einreichung</td>
<td>≥6</td>
<td>SEG</td>
<td>HITAN</td>
<td>O</td>
<td>1</td>
<td>s. [PINTAN], Kap. B.3.3 und B.4</td>
</tr>
<tr>
<td>7</td>
<td>Signaturabschluss</td>
<td>2</td>
<td>SEG</td>
<td>HNSHA</td>
<td>O</td>
<td>1</td>
<td>s. [HBCI], Kap. B.5.2</td>
</tr>
<tr>
<td>8</td>
<td>Nachrichtenab- schluss</td>
<td>1</td>
<td>SEG</td>
<td>HNHBS</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
</table>


### . Belegungsrichtlinien


### Signaturkopf

Falls es das Kreditinstitut wünscht, kann es seine Nachrichten ebenfalls sig-
nieren. In diesem Fall hat es dasselbe Signaturverfahren anzuwenden wie
der Kunde.

Es ist dem Kreditinstitut freigestellt, ob es als Signatur-ID (vgl. [HBCI]) die
vom Kunden gesendete ID verwendet oder einen eigenen Zähler verwaltet.


![](figures/31.1)


Falls Kreditinstitutsnachrichten signiert werden, hat das
Kundenprodukt deren Signatur verpflichtend zu prüfen. Falls
die Prüfung negativ ausfällt, hat es dem Kunden eine ent-
sprechende Rückmeldung zu geben und den Dialog zu be-
enden. Falls die Prüfung auch bei einem erneuten Dialog
negativ ausfällt, muss von einem Sicherheitsproblem ausge-
gangen werden.

<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: B</td>
<td>Version: 3.0-FV</td>
<td>Financial Transaction Services (FinTS) Dokument: Formals</td>
</tr>
<tr>
<td>Seite:<br>24</td>
<td>Stand: 06.10.2017</td>
<td>Kapitel: Nachrichtenaufbau<br>Abschnitt: Kreditinstitutsnachrichten allgemein</td>
</tr>
</table>


### B.7.2 Rückmeldungen zur Gesamtnachricht


#### . Beschreibung

In diesem Segment werden Rückmeldungen übermittelt, die sich auf die gesamte
Nachricht und nicht auf ein spezifisches Segment beziehen (z. B. ,,Nachricht entge-
gengenommen", "Elektronische Signatur gesperrt").


#### . Format


<table>
<tr>
<td>Name:</td>
<td>Rückmeldungen zur Gesamtnachricht</td>
</tr>
<tr>
<td>Typ:</td>
<td>Segment</td>
</tr>
<tr>
<td>Segmentart:</td>
<td>Administration</td>
</tr>
<tr>
<td>Kennung:</td>
<td>HIRMG</td>
</tr>
<tr>
<td>Bezugssegment:</td>
<td>-</td>
</tr>
<tr>
<td>Version:</td>
<td>2</td>
</tr>
<tr>
<td>Sender:</td>
<td>Kreditinstitut</td>
</tr>
<tr>
<td></td>
<td></td>
</tr>
</table>


<table>
<tr>
<th>Nr.</th>
<th>Name</th>
<th>For- mat</th>
<th>Typ</th>
<th>For- mat</th>
<th>Län- ge</th>
<th>Sta- tus</th>
<th>An- zahl</th>
<th>Restriktionen</th>
</tr>
<tr>
<td>1</td>
<td>Segmentkopf</td>
<td>1</td>
<td>DEG</td>
<td></td>
<td></td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>2</td>
<td>Rückmeldung</td>
<td>1</td>
<td>DEG</td>
<td></td>
<td></td>
<td>M</td>
<td>1..99</td>
<td></td>
</tr>
</table>


## . Belegungsrichtlinien


## Rückmeldung

Das DE ,,Bezugsdatenelement“ dieser DEG ist nicht zu belegen.

Ein Erfolgscode (Rückmeldungscode der Klasse 0) darf nur eingestellt wer-
den, wenn alle Aufträge fehlerfrei sind, d. h. in den Segmenten „Rückmel-
dungen zu Segmenten“ dürfen in diesem Fall keine Fehlermeldungen ge-
sendet werden.

<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th rowspan="2">Version: 3.0-FV</th>
<th rowspan="2">Kapitel: B</th>
</tr>
<tr>
<th>Dokument:</th>
<th>Formals</th>
</tr>
<tr>
<td>Kapitel:<br>Abschnitt:</td>
<td>Nachrichtenaufbau Kreditinstitutsnachrichten allgemein</td>
<td>Stand: 06.10.2017</td>
<td>Seite: 25</td>
</tr>
</table>


## B.7.3 Rückmeldungen zu Segmenten


### . Beschreibung

Dieses Segment ist genau einmal für jedes Segment der Kundennachricht einzu-
stellen. Hier sind sämtliche Rückmeldungscodes aufzuführen, die sich auf das Kun-
densegment bzw. die zugehörigen Datenelemente und Datenelementgruppen be-
ziehen. Falls für das jeweilige Kundensegment keine Rückmeldungscodes erzeugt
wurden, kann das zugehörige Rückmeldesegment entfallen. Ist das jeweilige Kun-
densegment fehlerhaft, dann dürfen keine Datensegmente (s.u.) rückgemeldet wer-
den.


### . Format


<table>
<tr>
<td>Name:</td>
<td>Rückmeldungen zu Segmenten</td>
</tr>
<tr>
<td>Typ:</td>
<td>Segment</td>
</tr>
<tr>
<td>Segmentart:</td>
<td>Administration</td>
</tr>
<tr>
<td>Kennung:</td>
<td>HIRMS</td>
</tr>
<tr>
<td>Bezugssegment:</td>
<td>abhängig von Kundensegment</td>
</tr>
<tr>
<td>Version:</td>
<td>2</td>
</tr>
<tr>
<td>Sender:</td>
<td>Kreditinstitut</td>
</tr>
</table>


<table>
<tr>
<th>Nr.</th>
<th>Name</th>
<th>Ver- sion</th>
<th>Typ</th>
<th>For- mat</th>
<th>Län- ge</th>
<th>Sta- tus</th>
<th>An- zahl</th>
<th>Restriktionen</th>
</tr>
<tr>
<td>1</td>
<td>Segmentkopf</td>
<td>1</td>
<td>DEG</td>
<td></td>
<td></td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>2</td>
<td>Rückmeldung</td>
<td>1</td>
<td>DEG</td>
<td></td>
<td></td>
<td>M</td>
<td>1..99</td>
<td></td>
</tr>
</table>


### ◆ Erläuterungen


#### Segmentkopf

Als Bezugssegment ist die Segmentnummer des Kundensegments, auf das
sich die Rückmeldungen beziehen, einzustellen.


#### Rückmeldung

Hier sind diejenigen Rückmeldungscodes einzustellen, die sich auf das Se-
gment (Auftrag) bzw. die zugehörigen Datenelemente und Datenelement-
gruppen beziehen.

<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: B</td>
<td>Version: 3.0-FV</td>
<td>Financial Transaction Services (FinTS) Dokument: Formals</td>
</tr>
<tr>
<td>Seite:</td>
<td>Stand:</td>
<td>Kapitel: Nachrichtenaufbau</td>
</tr>
<tr>
<td>26</td>
<td>06.10.2017</td>
<td>Abschnitt: Kreditinstitutsnachrichten allgemein</td>
</tr>
</table>


## B.7.4 Datensegmente


### . Beschreibung

Hier werden die Daten für die Kreditinstitutsrückmeldung (z. B. Kontoumsätze) ein-
gestellt. Auf ein Kundensegment hin (z. B. ,Dauerauftragsbestand abrufen“) können
hier eine Vielzahl von Segmenten mit identischer Kennung (und somit identischem
Format jedoch unterschiedlichem Inhalt) zurückgeliefert werden (z. B. jedes Seg-
ment liefert die Daten eines Dauerauftrags).


![](figures/34.1)


Falls das Kreditinstitut mehrere Versionen eines Geschäftsvorfalls
unterstützt, hat es stets mit einem Segment derjenigen Version zu
antworten, die dem Auftragssegment der Kundennachricht ent-
spricht.

Beispiel: Wenn das Kreditinstitut die Versionen 2, 3 und 4 unter-
stützt und das Kundenprodukt sendet einen Abholauftrag mit der
Segmentversion 3, so hat das Kreditinstitut ebenfalls ein Antwort-
segment der Segmentversion 3 zurückzumelden.


<table>
<tr>
<td colspan="2">. Format</td>
</tr>
<tr>
<td>Name:</td>
<td>Datensegmente</td>
</tr>
<tr>
<td>Typ:</td>
<td>Segmentfolge</td>
</tr>
<tr>
<td>Sender:</td>
<td>Kreditinstitut</td>
</tr>
<tr>
<td>Version:</td>
<td>2</td>
</tr>
</table>


### ◆ Erläuterungen

Die Segmentfolge enthält die in [Messages] definierten Rückmeldungssegmente
des Kreditinstituts. Jedes Segment kann dabei beliebig oft auftreten.

<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th rowspan="2">Version: 3.0-FV</th>
<th rowspan="2">Kapitel: B</th>
</tr>
<tr>
<th>Dokument:</th>
<th>Formals</th>
</tr>
<tr>
<td>Kapitel: Abschnitt:</td>
<td>Nachrichtenaufbau Kreditinstitutsnachrichten allgemein</td>
<td>Stand: 06.10.2017</td>
<td>Seite: 27</td>
</tr>
</table>


## B.7.5 Rückmeldungscodes


### B.7.5.1 Grundkonzept

Die Änderung und Ergänzung von Rückmeldungscodes erfolgt in Abstimmung mit
allen beteiligten Verbänden (Gewährleistung der Multibankfähigkeit). Änderungen
bestehender Codes implizieren darüber hinaus neue Versionsnummern der betref-
fenden Segmentformate.

Institutsindividuelle Rückmeldungen (z. B. Konditionen, Werbung, Hinweise) sind
über den Codebereich "Kreditinstitutsindividuelle Rückmeldung" zu generieren.


![](figures/35.1)


Die Rückmeldungscodes sollen Kundensystemen automatisierte
Reaktionen auf Institutsnachrichten ermöglichen; z. B. kann bei der
Rückmeldung "BLZ falsch" das Kundensystem automatisiert zur
Korrektur der BLZ aus einer hinterlegten BLZ-Tabelle auffordern.

Der „Rückmeldungstext“ dient dazu, den Kunden klartextliche In-
formationen zu übermitteln. Kundenprodukte sollten die kreditinsti-
tutsseitigen Rückmeldungen im vollständigen Klartext anzeigen.
Ebenso sollte der numerische Rückmeldungscode stets angezeigt
werden, um den Kreditinstituten eine einfachere Bearbeitung von
Kundenrückfragen zu spezifischen Rückmeldungstexten zu ermög-
lichen.

Rückmeldungen beziehen sich auf unterschiedliche Datenstrukturen (Nachricht,
Segment, DEG, DE etc.). In Bezug auf eine Datenstruktur können mehrere Rück-
meldungen zurück geliefert werden.


![](figures/35.2)


Der Umfang der Online-Prüfung (z. B. nur physikalische Entgegen-
nahme der Nachricht oder auch Syntax- und bankfachliche Prüfung)
ist institutsindividuell.


![](figures/35.3)


### B.7.5.2 Reaktionsvorschriften

Bei Erfolgsmeldungen (Klasse 0) wird die Nachricht bzw. der Auftrag stets ange-
nommen. Warnungen (Klasse 3) sind Hinweise auf mögliche Fehler, die jedoch
nicht zur Ablehnung führen. Bei Fehlermeldungen (Klasse 9) wird die zugehörige
syntaktische Einheit (Auftrag bzw. Nachricht) abgelehnt.

Pro Auftrag (Segment) muss im Erfolgsfall genau eine Erfolgsmeldung und im Feh-
lerfall mindestens eine Fehlermeldung eingestellt werden. Warnungen und Hinweise
können darüber hinaus beliebig hinzugefügt werden.

Nachfolgend sind die gültigen Kombinationen von FinTS-Rückmeldungen unter-
schiedlicher Meldungsklassen aufgeführt:

<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: B</td>
<td>Version: 3.0-FV</td>
<td>Financial Transaction Services (FinTS) Dokument: Formals</td>
</tr>
<tr>
<td>Seite:<br>28</td>
<td>Stand: 06.10.2017</td>
<td>Kapitel: Nachrichtenaufbau<br>Abschnitt: Kreditinstitutsnachrichten allgemein</td>
</tr>
</table>


<table>
<tr>
<th>Nr.</th>
<th>Klasse 0 (Erfolg)</th>
<th>Klasse 3 (Warnung/ Hinweis)</th>
<th>Klasse 9 (Fehler)</th>
<th>Ergebnis</th>
</tr>
<tr>
<td>1</td>
<td>1</td>
<td>-</td>
<td>-</td>
<td>Auftrag angenommen</td>
</tr>
<tr>
<td>2</td>
<td>1</td>
<td>1-98</td>
<td>-</td>
<td>Auftrag angenommen</td>
</tr>
<tr>
<td>3</td>
<td>-</td>
<td>1</td>
<td>-</td>
<td>Auftrag angenommen</td>
</tr>
<tr>
<td>4</td>
<td>-</td>
<td>2-99</td>
<td>-</td>
<td>Auftrag angenommen</td>
</tr>
<tr>
<td>5</td>
<td>-</td>
<td>-</td>
<td>1</td>
<td>Auftrag abgelehnt</td>
</tr>
<tr>
<td>6</td>
<td>-</td>
<td>1-98</td>
<td>1</td>
<td>Auftrag abgelehnt</td>
</tr>
<tr>
<td>7</td>
<td>-</td>
<td>-</td>
<td>2-99</td>
<td>Auftrag abgelehnt</td>
</tr>
<tr>
<td>8</td>
<td>-</td>
<td>1-(99)</td>
<td>1-(99)</td>
<td>Auftrag abgelehnt</td>
</tr>
</table>


Weitere Hinweise zur Verwendung der Rückmeldungen:

. Andere als die genannten Kombinationen dürfen für einen Geschäftsvorfall nicht
auftreten.

· Das Senden einer Warnung ohne kombinierte Erfolgs- bzw. Fehlermeldung ist
nur für den Fall der Teilausführung sinnvoll, da andererseits der Status des Auf-
trags (angenommen bzw. abgelehnt) nicht eindeutig bestimmbar ist.

· Es ist sinnvoll, die Rückmeldungen an Kunden auf ein überschaubares Maß zu
reduzieren (Kein Ausschöpfen der insgesamt 99 möglichen Meldungen)

. Um Kundenprodukten die Auswertung zu erleichtern, soll die jeweils wichtigste
Meldung als erste in das Rückmeldungssegment eingestellt werden (Klasse 0
oder 9, falls vorhanden)

Auch wenn einzelne Aufträge einer Nachricht inkorrekt sind, müssen andere kor-
rekte Aufträge in derselben Nachricht vom Kreditinstitut ausgeführt werden. Dies gilt
auch für Syntaxfehler, sofern dieser nur Auswirkungen auf einen einzigen Auftrag
hat. D. h., bei Syntaxfehlern in administrativen Segmenten (Nachrichtenkopf, Signa-
turkopf etc.) ist stets die gesamte Nachricht abzulehnen.


#### Beispiel:


<table>
<tr>
<td>Code-Bedeutung</td>
<td>Reaktion</td>
</tr>
<tr>
<td>DE im Auftrag syntaktisch ungültig</td>
<td>Nachricht ok, Auftrag nicht ok</td>
</tr>
<tr>
<td>DE im Nachrichtenkopf syntaktisch ungültig</td>
<td>Nachricht nicht ok, Auftrag nicht ok</td>
</tr>
<tr>
<td>Unbekannter Nachrichtenaufbau</td>
<td>Nachricht nicht ok, Auftrag nicht ok</td>
</tr>
</table>


Verstöße gegen die syntaktischen Festlegungen in Kapitel H sind nicht zu tolerieren,
sondern führen zur Ablehnung des Auftrags bzw. der Nachricht.

Folgende Voraussetzungen müssen erfüllt sein, damit die Nachricht als gültig er-
kannt wird:

• Die Nachricht muss mit der Zeichenkette ,,HNHBK:1:" beginnen.

· Die Nachricht muss in einzelne Segmente aufgeteilt werden können.

· Ein Segment muss in einzelne Datenelemente zerlegt werden können.

. Der Sender darf erst eine neue Nachricht schicken, nachdem er die Kreditinsti-
tutsantwortnachricht erhalten hat.

• Die Länge der Nachricht darf nicht größer als die in den BPD angegebene maxi-
male Nachrichtengröße sein.

<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th rowspan="2">Version: 3.0-FV</th>
<th rowspan="2">Kapitel: B</th>
</tr>
<tr>
<th>Dokument:</th>
<th>Formals</th>
</tr>
<tr>
<td>Kapitel:<br>Abschnitt:</td>
<td>Nachrichtenaufbau Kreditinstitutsnachrichten allgemein</td>
<td>Stand: 06.10.2017</td>
<td>Seite: 29</td>
</tr>
</table>


Eine Nachricht, bei der diese Voraussetzungen nicht zutreffen, muss nicht mit einer
Kreditinstitutsnachricht beantwortet werden. In diesem Fall darf das Kreditinstitut
von sich aus die Transportverbindung ohne Rückmeldung beenden. Ansonsten sind
Nachrichten, die gegen grundlegende FinTS-Aufbauvorschriften verstoßen, mit dem
Rückmeldungscode 9110 „Unbekannter Aufbau“ zu beantworten.

Grundsätzlich werden dem Kunden alle auftretenden Meldungen mitgeteilt.

Ausnahmen:

. Tritt in einer Nachricht ein Fehler auf, der dazu führt, dass eine syntaktische Ein-
heit (z. B. Nachricht, Segment, DEG) komplett ungültig ist oder nachfolgende Tei-
le der syntaktischen Einheit ebenfalls fehlerhaft sind (Folgefehler), so kann die
Bearbeitung der syntaktischen Einheit nach diesem Fehler abgebrochen werden.

· Zu nachgeordneten syntaktischen Einheiten brauchen keine Meldungen rückge-
meldet werden, falls deren Code derselbe ist wie der der übergeordneten syntak-
tischen Einheit (Bsp.: Falls die Nachricht insgesamt fehlerfrei ist, brauchen für die
einzelnen Segmente keine Erfolgsmeldungen rückgemeldet werden).


![](figures/37.1)


Wurde ein Auftrag abgelehnt, so ist darauf zu achten, dass nach der
Fehlerbehebung bei einem eventuellen neuen Senden durch das
Kundensystem die Nachricht neu aufgebaut wird, d. h. insbesonde-
re eine neue Signatur eingestellt wird.

Bei Transaktionsaufträgen kann bei der institutsinternen Verarbei-
tung unter Umständen ein Fehler auftreten, bei dem für das rück-
meldende System nicht ersichtlich ist, ob der Fehler vor oder nach
der Verarbeitung des Auftrags aufgetreten ist. In diesem Fall wird
dem Kundenprodukt der Rückmeldungscode 9000 „Status indiffe-
rent" mitgeteilt. Das Kundenprodukt darf den Auftrag anschließend
nicht erneut einreichen, da er eventuell doppelt verarbeitet wird.
Stattdessen hat der Kunde den Status des Auftrags auf anderem
Wege in Erfahrung zu bringen. Das Kundenprodukt sollte dem Kun-
den einen entsprechenden Hinweis geben.

<!-- PageBreak -->


<table>
<tr>
<th>Kapitel: B</th>
<th>Version: 3.0-FV</th>
<th>Financial Transaction Services (FinTS) Dokument: Formals</th>
</tr>
<tr>
<td>Seite:<br>30</td>
<td>Stand: 06.10.2017</td>
<td>Kapitel: Nachrichtenaufbau<br>Abschnitt: Kreditinstitutsnachrichten allgemein</td>
</tr>
</table>


### B.7.5.3 Code-Bedeutungen

Die Bedeutung der einzelnen Rückmeldungscodes wurde in ein separates Doku-
ment ,,Financial Transaction Services (FinTS) - Rückmeldungscodes" [RM-Codes]
ausgelagert.

<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th rowspan="2">Version: 3.0-FV</th>
<th rowspan="2">Kapitel: B</th>
</tr>
<tr>
<th>Dokument:</th>
<th>Formals</th>
</tr>
<tr>
<td>Kapitel:<br>Abschnitt:</td>
<td>Nachrichtenaufbau Kreditinstitutsnachrichten allgemein</td>
<td>Stand: 06.10.2017</td>
<td>Seite: 31</td>
</tr>
</table>


## B.7.6 Dialogabbruchnachricht

In bestimmten Fällen kann es erforderlich sein, dass das Kreditinstitut aufgrund ei-
ner fehlerhaften Kundennachricht oder eines institutsinternen Problems den Dialog
abbrechen muss.

Bei einem solchen Dialogabbruch muss unterschieden werden, ob es sich um eine
Dialoginitialisierungsnachricht oder um eine Auftragsnachricht handelt. Dabei muss
die Tatsache berücksichtigt werden, dass dem Kreditinstitutssystem evtl. bei Folge-
nachrichten nicht immer alle Daten wie Nachrichtennummer oder Dialog-ID zur Ver-
fügung stehen. In bestimmten Situationen kann dann das Kreditinstitut eine unver-
schlüsselte und nicht signierte Nachricht mit festem Aufbau an das Kundensystem
senden.

Folgende Situationen sind u.a. denkbar:

· Bank vorübergehend gesperrt (Release-Einsatz)

. BLZ unbekannt (nach einer Fusion)

. Fehlerhafter Nachrichtenkopf

. Unbekannte HBCI-Version (wird nicht mehr unterstützt)

• Nachrichtenlänge ungleich

Die in Kap. B.7.5.2 beschriebene Möglichkeit eines unbeantworteten Dialogab-
bruchs bleibt hiervon unberührt.


### . Beschreibung

Die Abbruchnachricht hat den folgenden festen Aufbau. Sie wird weder verschlüs-
selt noch signiert.


![](figures/39.1)


Das Kundenprodukt sollte in jedem Fall die Abbruchnachricht mit
dem Hinweistext entgegennehmen und dem Kunden anzeigen.


### . Format


<table>
<tr>
<td>Name:</td>
<td>Abbruchnachricht</td>
</tr>
<tr>
<td>Typ:</td>
<td>Nachricht</td>
</tr>
<tr>
<td>Version:</td>
<td>1</td>
</tr>
<tr>
<td>Sender:</td>
<td>Kreditinstitut</td>
</tr>
</table>


<table>
<tr>
<th>Nr.</th>
<th>Name</th>
<th>Ver- sion</th>
<th>Typ</th>
<th>Ken- nung</th>
<th>Sta- tus</th>
<th>An- zahl</th>
<th>Anmerkungen</th>
</tr>
<tr>
<td>1</td>
<td>Nachrichtenkopf</td>
<td>3</td>
<td>SEG</td>
<td>HNHBK</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>2</td>
<td>Rückmeldungen zur Gesamtnachricht</td>
<td>2</td>
<td>SEG</td>
<td>HIRMG</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>3</td>
<td>Nachrichtenab- schluss</td>
<td>1</td>
<td>SEG</td>
<td>HNHBS</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
</table>


### . Belegungsrichtlinien


#### Nachrichtenkopf

Der Nachrichtenkopf ist dabei wie folgt zu belegen:

<!-- PageBreak -->


<table>
<tr>
<th>Kapitel: B</th>
<th>Version: 3.0-FV</th>
<th>Financial Transaction Services (FinTS) Dokument: Formals</th>
</tr>
<tr>
<td>Seite:<br>32</td>
<td>Stand: 06.10.2017</td>
<td>Kapitel: Nachrichtenaufbau<br>Abschnitt: Kreditinstitutsnachrichten allgemein</td>
</tr>
</table>


<table>
<tr>
<th>Feldname</th>
<th>Fehler tritt auf bei Dialo- ginitialisierung</th>
<th>Fehler tritt auf bei Auftrags- nachricht</th>
</tr>
<tr>
<td>Nachrichtengröße</td>
<td>Größe der Nachricht</td>
<td>Größe der Nachricht</td>
</tr>
<tr>
<td>HBCI-Version</td>
<td>Wenn bekannt, einstellen, ansonsten die vom Institut unterstützte Version</td>
<td>Wenn bekannt, einstellen, an- sonsten die vom Institut unter- stützte Version</td>
</tr>
<tr>
<td>Dialog-ID</td>
<td>Konstante: ,,unbekannt"</td>
<td>Wenn bekannt, die Dialog-ID Sonst Konstante: unbekannt</td>
</tr>
<tr>
<td>Nachrichtennummer</td>
<td>„1“</td>
<td>Wenn bekannt, Nachrichten- nummer Sonst Konstante: ,9999"</td>
</tr>
<tr>
<td>Bezugsnachricht</td>
<td>Zu belegen wie Siehe Dialog-ID bzw. Nachrichtennummer</td>
<td>Zu belegen wie Siehe Dialog-ID bzw. Nachrich- tennummer</td>
</tr>
</table>


##### Rückmeldungen zur Gesamtnachricht

Das Segment „Rückmeldungen zur Gesamtnachricht" ist mit einem Rück-
meldungscode und Text zu belegen, der den aufgetretenen Fehler möglichst
genau angibt.

<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th rowspan="2">Version: 3.0-FV</th>
<th rowspan="2">Kapitel: B</th>
</tr>
<tr>
<th>Dokument:</th>
<th>Formals</th>
</tr>
<tr>
<td>Kapitel: Abschnitt:</td>
<td>Nachrichtenaufbau Allgemeiner Nachrichtenaufbau bei Verschlüsselung</td>
<td>Stand: 06.10.2017</td>
<td>Seite: 33</td>
</tr>
</table>


## B.8 Allgemeiner Nachrichtenaufbau bei Verschlüsselung


### . Beschreibung

Beim Sicherheitsverfahren HBCI (s. [HBCI]) werden generell alle Kunden- und alle
Kreditinstitutsnachrichten verschlüsselt. Ausnahmen sind in Kap. C.1.3 aufgeführt.
Bei TAN-Verfahren (s. [PINTAN]) findet eine Transportverschlüsselung z. B. durch
TLS statt (vgl. Kap. I.4).

Für den Aufbau von verschlüsselten Nachrichten ist folgendes Vorgehen einzuhal-
ten5:

1\. Die Nachricht ist zunächst unverschlüsselt aufzubauen.

2\. Das Segment „Verschlüsselungskopf" ist direkt hinter dem Nachrichtenkopf ein-
zustellen.

3\. Die verschlüsselten Signatur- und Auftragssegmente sind in das Segment ,,Ver-
schlüsselte Daten“ einzustellen.

Vor der Verschlüsselung weisen die Segmente eine kontinuierliche Nummerierung
auf (s. Abb. links). Um die Eindeutigkeit der Segmentnummern zu gewährleisten,
erhält das Segment „Verschlüsselungskopf“ die Segmentnummer 998 und das
Segment „Verschlüsselte Daten" die Segmentnummer 999 (s. Abb. rechts). Diese
beiden Segmentnummern dürfen daher vor der Verschlüsselung noch nicht verge-
ben worden sein. Bei der Entschlüsselung wird das Segment „Verschlüsselungs-
kopf" entfernt und das Segment „Verschlüsselte Daten“ in die Einzelsegmente auf-
gelöst, so dass die Nachricht wieder eine kontinuierliche Segmentnumerierung auf-
weist.

Vor Verschlüsselung:


<table>
<tr>
<td>Nr.</td>
<td>Segmentname</td>
</tr>
<tr>
<td>1</td>
<td>Nachrichtenkopf</td>
</tr>
<tr>
<td>2</td>
<td>Signaturkopf</td>
</tr>
<tr>
<td>3</td>
<td>Auftrag 1</td>
</tr>
<tr>
<td>4</td>
<td>Auftrag 2</td>
</tr>
<tr>
<td>5</td>
<td>Signaturabschluss</td>
</tr>
<tr>
<td>6</td>
<td>Nachrichtenabschluss</td>
</tr>
</table>


Nach Verschlüsselung:


<table>
<tr>
<td>Nr.</td>
<td>Segmentname</td>
</tr>
<tr>
<td>1</td>
<td>Nachrichtenkopf</td>
</tr>
<tr>
<td>998</td>
<td>Verschlüsselungskopf</td>
</tr>
<tr>
<td>999</td>
<td>Verschlüsselte Daten (enthält: 2 Signaturkopf<br>3 Auftrag 1<br>4 Auftrag 2<br>5 Signaturabschluss)</td>
</tr>
<tr>
<td>6</td>
<td>Nachrichtenabschluss</td>
</tr>
</table>


. Format


<table>
<tr>
<td>Name:</td>
<td>Verschlüsselte Nachricht</td>
</tr>
<tr>
<td>Typ:</td>
<td>Nachricht</td>
</tr>
<tr>
<td>Version:</td>
<td>3</td>
</tr>
<tr>
<td>Sender:</td>
<td>Kunde/Kreditinstitut</td>
</tr>
</table>


<!-- PageFooter: 5 Falls im Fortlauf dieses Dokuments Nachrichtenaufbautabellen dargestellt sind, wurde stets die un- verschlüsselte Form (s.o.) gewählt. -->
<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: B</td>
<td>Version: 3.0-FV</td>
<td>Financial Transaction Services (FinTS) Dokument: Formals</td>
</tr>
<tr>
<td>Seite:<br>34</td>
<td>Stand: 06.10.2017</td>
<td>Kapitel: Nachrichtenaufbau<br>Abschnitt: Allgemeiner Nachrichtenaufbau bei Verschlüsselung</td>
</tr>
</table>


<table>
<tr>
<th>Nr.</th>
<th>Name</th>
<th>Ver- sion</th>
<th>Typ</th>
<th>Ken- nung</th>
<th>Sta- tus</th>
<th>An- zahl</th>
<th>Anmerkungen</th>
</tr>
<tr>
<td>1</td>
<td>Nachrichtenkopf</td>
<td>3</td>
<td>SEG</td>
<td>HNHBK</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>2</td>
<td>Verschlüsselungs- kopf</td>
<td>3</td>
<td>SEG</td>
<td>HNVSK</td>
<td>M</td>
<td>1</td>
<td>s. [HBCI], Kap. B.5.4</td>
</tr>
<tr>
<td>3</td>
<td>Verschlüsselte Da- ten</td>
<td>1</td>
<td>SEG</td>
<td>HNVSD</td>
<td>M</td>
<td>1</td>
<td>s. [HBCI], Kap. B.5.5</td>
</tr>
<tr>
<td>4</td>
<td>Nachrichtenab- schluss</td>
<td>1</td>
<td>SEG</td>
<td>HNHBS</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
</table>


### . Belegungsrichtlinien


#### Verschlüsselte Daten

In dieses Segment sind die verschlüsselten Signatur- und Auftragssegmente
einzustellen.

<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th>Version:</th>
<th rowspan="2">Kapitel: C</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Formals</td>
<td>3.0-FV</td>
</tr>
<tr>
<td>Kapitel:<br>Abschnitt:</td>
<td>Dialogspezifikation Allgemeines</td>
<td>Stand: 06.10.2017</td>
<td>Seite: 35</td>
</tr>
</table>


# C. DIALOGSPEZIFIKATION


## C.1 Allgemeines


### C.1.1 Begriffsbestimmung

Die Identifizierung des Kunden sowie die Festlegung der Rechte, die einem Kunden
im Rahmen eines FinTS-Dialoges offen stehen, erfolgt in FinTS anhand der Begriffe
'Benutzer' und 'Kunde' bzw. anhand der zugeordneten Identifikationsmerkmale 'Be-
nutzerkennung' und 'Kunden-ID'. Hierzu sind folgende Unterscheidungen zu treffen:


### Benutzer

Ein Benutzer ist eine natürliche Person, die als Inhaber oder Berechtigter
(z. B. Bevollmächtigter) eines Kontos über ein Kundenprodukt/-endgerät am
FinTS-Verfahren teilnimmt. Jeder Benutzer kann von seinem Kreditinstitut
Userparameterdaten erhalten, in denen er über seine Rechte im Rahmen
des FinTS-Verfahrens informiert wird. Dem Kreditinstitut gegenüber tritt der
Benutzer als Inhaber eines Sicherheitsmediums auf.

Die Identifizierung des Benutzers erfolgt anhand des DE Benutzerkennung.


### Kunde

Neben dem allgemeinen Gebrauch des Kundenbegriffs in Abgrenzung zum
Kreditinstitut kann der Begriff 'Kunde' optional dazu verwendet werden, eine
institutsindividuelle Differenzierung eines Benutzers zu ermöglichen, um die
Rolle, in der er auftritt, zu spezifizieren. So lässt sich zum Beispiel unter-
scheiden, ob ein Benutzer den Dialog in der Eigenschaft als Privatperson
oder als Bevollmächtigter einer Firma führen möchte (s. Abbildung 4). Durch
die Rolle werden die Rechte festgelegt, die dem Benutzer im FinTS-Dialog
zur Verfügung stehen.

Die Identifizierung des 'Kunden', bzw. der Rolle, in der der Kunde auftritt,
kann anhand des DE Kunden-ID erfolgen.

Es steht dem Kreditinstitut jedoch frei, dem Benutzer für jede Rolle eine ei-
gene Benutzerkennung (Sicherheitsmedium) zur Verfügung zu stellen. Diese
Rolle muss nicht zwingend über eine eigene Kunden-ID im FinTS-System
festgelegt werden. Bei Gleichheit von Benutzerkennung und Kunden-ID im
FinTS-System wird die Rolle des Kunden im nachgelagerten operativen Sys-
tem festgelegt. Sie entscheidet sich durch die Verknüpfungen zwischen Be-
nutzerkennung und 'interner' Kundennummer und den dazugehörigen Kon-
ten mit ihren jeweiligen Vollmachten.

Der Kundenbezug gilt immer für den gesamten Dialogkontext, d. h. für sämt-
liche Benutzer, die im Rahmen des Dialoges als Signierende auftreten (d. h.
auch für eventuelle Zweit- und Drittsignierende).


![](figures/43.1)


Da Kunden-ID und Benutzerkennung voneinander abweichen
können, ist im Kundenprodukt eine Eingabemöglichkeit für die
Kunden-ID vorzusehen.

<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: C</td>
<td>Version: 3.0-FV</td>
<td>Financial Transaction Services (FinTS) Dokument: Formals</td>
</tr>
<tr>
<td>Seite:<br>36</td>
<td>Stand: 06.10.2017</td>
<td>Kapitel: Dialogspezifikation<br>Abschnitt: Allgemeines</td>
</tr>
</table>


Im Einzelnen sind folgende Belegungsvarianten für Benutzerkennung und Kunden-
ID möglich:

· Benutzerkennung und Kunden-ID sind identisch:

In diesem Fall wird institutsseitig keine logische Differenzierung zwischen Kunde
und Benutzer vorgenommen. Die Benutzerkennung wird in das Feld 'Kunden-ID'
eingestellt. Die Rolle des Benutzers ergibt sich, wie oben dargestellt, erst im nach
gelagerten System.

· Benutzerkennung und Kunden-ID sind nicht identisch:

Es wird institutsseitig eine logische Differenzierung zwischen Kunde und Benut-
zer vorgenommen, um die Rolle festzulegen, in der der Benutzer auftritt.

Die folgenden Abbildungen gelten für den Fall, dass die Kunden-ID genutzt wird, um
die Rolle des Benutzers festzulegen:


Abbildung 4: Benutzer, mehreren Kunden zugeordnet

![Benutzerkennung: 26314255 Ernst Müller Rolle: Prokurist Rolle: Privatperson Zugriff auf Konten: 345678 345679 Zugriff auf Konten: 1234 345680 Kunden-ID: 28515199 Kunden-ID: 26314255 Firma Meyer & Co. Ernst Müller Hat Konten: Hat Konten: 1234 345678 345679 345680](figures/44.1)


Abbildung 5: Kunde, mehreren Benutzern zugeordnet

![Benutzerkennung: 83637129 Benutzerkennung: 26314255 Eva Schulze Ernst Müller Rolle: Sekretärin Rolle: Prokurist Zugriff auf Konten: Zugriff auf Konten: 345678 Kunden-ID: 28515199 345678 345679 345679 Firma Meyer & Co. 345680 Hat Konten: 345678 345679 345680](figures/44.2)


<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th>Version:</th>
<th rowspan="2">Kapitel: C</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Formals</td>
<td>3.0-FV</td>
</tr>
<tr>
<td>Kapitel:<br>Abschnitt:</td>
<td>Dialogspezifikation Allgemeines</td>
<td>Stand: 06.10.2017</td>
<td>Seite: 37</td>
</tr>
</table>


## C.1.2 Dialogabfolge

Die Initiierung eines Dialogs geht stets vom Kunden aus. Auf eine Kundennachricht
wird stets mit einer genau definierten Kreditinstitutsnachricht unmittelbar geantwor-
tet. Erst wenn der Kunde diese Kreditinstitutsnachricht vollständig erhalten hat, darf
er die nächste Nachricht an das Kreditinstitut übermitteln (Ausnahme: Nach einem
Verbindungsabbruch sendet der Kunde im nächsten Dialog eine Nachricht an das
Kreditinstitut, ohne vorher eine vollständige Antwortnachricht erhalten zu haben).
Sowohl Kunde als auch Kreditinstitut dürfen jeweils nur eine Nachricht auf einmal
übermitteln. Das Kundensystem hat die Pflicht, solange zu warten, bis das Kredit-
institut die entsprechende Antwortnachricht übermittelt hat.


Abbildung 6: Dialogabfolge

![Aufbau der physikalischen Verbindung Dialoginitialisierung Kreditinstitut K Antwort auf Dialoginitialisierung Auftragnachricht 1 K Antwortnachricht u . n . d n . e Auftragnachricht n Antwortnachricht t Dialogendenachricht Antwortnachricht Abbau der physikalischen Verbindung](figures/45.1)


Jeder Dialog beginnt mit einer Dialoginitialisierungsnachricht. Erst wenn das Kun-
densystem die Bestätigungsnachricht erhalten hat, darf die erste Auftragsnachricht
gesendet werden. Sollen keine weiteren Auftragsnachrichten mehr gesendet wer-
den, so hat das Kundensystem eine Dialogendenachricht zu senden. Mit der Rück-
meldung auf diese Nachricht erhält das Kundensystem die Dialogendebestätigung
des Kreditinstituts.

Im Ausnahmefall kann das Kreditinstitut den Dialog auch von sich aus beendigen
(z. B. bei wiederholter ungültiger Authentisierung des Kunden). Hierzu sendet es in
der Antwort auf eine Kundennachricht den Rückmeldungscode 9800 („Dialog abge-
brochen"). Danach kann es die Transportverbindung abbauen. Das Kundenprodukt
hat den Dialog in diesem Fall als beendet anzusehen und darf keine Dialogende-
nachricht mehr schicken.

<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: C</td>
<td>Version: 3.0-FV</td>
<td>Financial Transaction Services (FinTS) Dokument: Formals</td>
</tr>
<tr>
<td>Seite:<br>38</td>
<td>Stand: 06.10.2017</td>
<td>Kapitel: Dialogspezifikation<br>Abschnitt: Allgemeines</td>
</tr>
</table>


Abbildung 7: Einzelbenutzer

![Aufbau der physikalischen Verbindung Dialoginitialisierung für Benutzerkennung 12345 Kreditinstitut K Antwort auf Dialoginitialisierung Einzelüberweisung für Konto 1111 K Antwortnachricht u n d e Kontostandabfrage für Konto 2222 n Antwortnachricht S t i Dialogendenachricht t Antwortnachricht u t Abbau der physikalischen Verbindung](figures/46.1)


Sollen Aufträge für mehrere Benutzer gesendet werden, ohne dass die physikali-
sche Verbindung unterbrochen wird, so ist für jede neue Benutzerkennung eine
neue Dialoginitialisierung durchzuführen (s. Abbildung 8).


Abbildung 8: Mehrere Benutzer

![Aufbau der physikalischen Verbindung Dialoginitialisierung für Benutzerkennung 12345 Antwort auf Dialoginitialisierung K Sammelüberweisung für Konto 1111 r e Antwortnachricht d K u Dialogendenachricht i t Antwortnachricht n d e i Dialoginitialisierung für Benutzerkennung 54321 n Antwort auf Dialoginitialisierung s t i Kontostandabfrage für Konto 3333 Antwortnachricht t u Dialogendenachricht t Antwortnachricht Abbau der physikalischen Verbindung](figures/46.2)


<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th rowspan="2">Version: 3.0-FV</th>
<th rowspan="2">Kapitel: C</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Formals</td>
</tr>
<tr>
<td>Kapitel: Abschnitt:</td>
<td>Dialogspezifikation Allgemeines</td>
<td>Stand: 06.10.2017</td>
<td>Seite: 39</td>
</tr>
</table>


## C.1.3 Verschlüsselung des Dialoges beim Sicherheitsverfahren HBCI

Grundsätzlich sind beim Sicherheitsverfahren HBCI alle Kunden- und alle Kreditin-
stitutsnachrichten eines Dialoges zu verschlüsseln. Von dieser Regel ausgenom-
men sind die folgenden Dialogarten:

. Anonymer Zugang (vgl. Kap. C.5)

· Erstmalige Anforderung der öffentlichen Schlüssel des Kreditinstituts (vgl. [HBCI],
Kap. B.6.2.2)

· Schlüsselsperrung durch den Kunden (vgl. [HBCI], Kap. B.6.2.4)1

· Kommunikationszugang anfordern (vgl. Kap. 1.5)

. Life-Indikator-Nachricht (vgl. Kap. C.9)


![](figures/47.1)


Unverschlüsselte Nachrichten, die keiner der oben genannten
Ausnahmen zuzuordnen sind, sind vom empfangenden Sys-
tem abzulehnen.


![](figures/47.2)


Alle Kundennachrichten eines Dialoges sind vom Übermittler der Nachricht zu ver-
schlüsseln. Alle Kreditinstitutsnachrichten sind mit dem Chiffrierschlüssel des Kredit-
instituts zu verschlüsseln.

Kunde und Kreditinstitut haben stets dasselbe Verschlüsselungsverfahren anzuwen-
den. Der Kunde gibt im Verschlüsselungskopf ([HBCI], Kap. B.5.4) den von ihm ver-
wendeten Verschlüsselungsalgorithmus an und bestimmt damit ebenfalls den Algo-
rithmus, den das Kreditinstitut anzuwenden hat. Weder Kunde noch Kreditinstitut
dürfen das Verfahren während des Dialoges wechseln. Der Kunde darf nur ein Ver-
fahren wählen, das vom Kreditinstitut unterstützt wird. Die vom Kreditinstitut unter-
stützten Verfahren werden dem Kundensystem in den Bankparameterdaten im
Segment ,,Sicherheitsverfahren“ (Kap. D.4) bzw. ,,Komprimierungsverfahren“ (Kap.
D.5) mitgeteilt.


![](figures/47.3)


Falls das Kreditinstitut das vom Kunden gewählte Verschlüsse-
lungsverfahren nicht unterstützt, ist dem Kunden eine entsprechen-
de Rückmeldung zu geben und der Dialog zu beenden. Das Kun-
denprodukt wird diese Nachricht nicht entschlüsseln können, da es
das Verschlüsselungsverfahren des Kreditinstituts nicht unterstützt.
Das Kundenprodukt hat in diesem Fall dem Verschlüsselungskopf
der Kreditinstitutsnachricht zu entnehmen, dass es ein dem Kredit-
institut nicht bekanntes Verschlüsselungsverfahren verwendet. In
diesem Fall hat der Kunde über den (unverschlüsselten) anonymen
Zugang die aktuellen Bankparameterdaten anzufordern, in denen
die Verschlüsselungsverfahren des Kreditinstituts angegeben sind.

<!-- PageFooter: 1 Es liegt im Ermessen des Kreditinstituts, ob es auch unverschlüsselte Sperren (z. B. aufgrund Schlüsselverlust des Kunden) entgegennimmt. -->
<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: C</td>
<td>Version: 3.0-FV</td>
<td>Financial Transaction Services (FinTS) Dokument: Formals</td>
</tr>
<tr>
<td>Seite:<br>40</td>
<td>Stand: 06.10.2017</td>
<td>Kapitel: Dialogspezifikation<br>Abschnitt: Abfolge von Operationen</td>
</tr>
</table>


## C.2 Abfolge von Operationen

Bei der Erstellung einer Nachricht sind die Arbeitsschritte in folgender Reihenfolge
auszuführen (Arbeitsschritte teils optional):

1\. Zusammenstellung der Informationen im System des Senders

2\. Aufbau der Nachricht. Aus den Informationen werden die zu übertragenden Se-
gmente bis auf ggf. erforderliche Signatur-Segmente aufgebaut, wobei beim Ein-
stellen der Informationen in die Nachricht Syntaxzeichen entwertet werden.

3\. Bildung der elektronischen Signatur (optional)

. Erstellung des Signaturkopfes

. Berechnung der elektronischen Signatur über Signaturkopf und Auftrags-
segmente

. Erstellung des Signaturabschlusses und Einstellung der Daten in das ent-
sprechende Feld

4\. Wiederholung von Schritt 3 für weitere Signaturen (optional)

5\. Komprimierung

6\. Verschlüsselung (Ausnahme: nicht verschlüsselungspflichtige Nachrichten)

Beim Empfänger einer Nachricht erfolgen die Verarbeitungsschritte entsprechend in
umgekehrter Reihenfolge:

1\. Entschlüsselung (Ausnahme: unverschlüsselte Nachrichten)

2\. Dekomprimierung

3\. Syntaxprüfung

4\. Prüfung der elektronischen Signatur (optional)

. Berechnung der elektronischen Signatur über Signaturkopf und Auftrags-
segmente gemäß Parametern im Signaturkopf

. Extrahieren des Signaturwertes aus dem Signaturabschluss

· Vergleich des berechneten und des extrahierten Signaturwertes

5\. Wiederholung von Schritt 4 für weitere Signaturen (optional)

6\. Zerlegung der übrigen Datensegmente, dabei Entfernung von Entwertungs-
zeichen

7\. Bereitstellung der Informationen zur Verarbeitung im System des Empfängers

<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th>Version:</th>
<th rowspan="2">Kapitel: C</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Formals</td>
<td>3.0-FV</td>
</tr>
<tr>
<td>Kapitel:</td>
<td>Dialogspezifikation</td>
<td>Stand:</td>
<td>Seite:</td>
</tr>
<tr>
<td>Abschnitt:</td>
<td>Dialoginitialisierung</td>
<td>06.10.2017</td>
<td>41</td>
</tr>
</table>


## C.3 Dialoginitialisierung

Die Dialoginitialisierung dient folgenden Zwecken:

1\. Prüfung, ob der Kommunikationspartner ein sendeberechtigter Benutzer ist

2\. Festlegung der Dialog-ID

3\. Prüfung auf Aktualität der im Kundensystem vorhandenen BPD und UPD sowie
ggf. deren Aktualisierung

4\. Prüfung auf Aktualität der öffentlichen Schlüssel des Kreditinstituts sowie ggf. de-
ren Aktualisierung (nur bei asymmetrischen Verfahren)

5\. Übermittlung vorbereitender Informationen für die kunden- und kreditinstituts-
seitige Verarbeitung

6\. Übertragung von Kreditinstitutsmeldungen

Bei Verwendung der starken Authentifizierung gelten zusätzlich die entsprechenden
Abläufe, wie sie in [PINTAN] beschrieben sind. Während Auftragsnachrichten von
dem bzw. den jeweiligen Signaturpflichtigen zu signieren sind, wird die Dialoginitiali-
sierung von demjenigen Benutzer signiert, der sich im Rahmen der Dialoginitialisie-
rung anmeldet. Im Regelfall ist dieser Benutzer auch Auftraggeber der nachfolgen-
den Aufträge, d. h. identisch mit dem Kunden. Während eines Dialoges dürfen nur
Aufträge für Auftraggeberkonten gesendet werden, die der bei der Dialoginitialisie-
rung angegebenen Kunden-ID zugeordnet sind.

Darüber hinaus darf die Dialoginitialisierung auch von einem Benutzer signiert wer-
den, der für die nachfolgenden Auftraggeberkonten bevollmächtigt ist. Dies gilt auch
bei Aufträgen für Konten mit Mehrfachunterschrift. Die Auftragsnachrichten müssen
jedoch weiterhin von den Signaturpflichtigen signiert werden. Der Umfang der Be-
vollmächtigung ist Inhalt einer Vereinbarung zwischen Kunde und Kreditinstitut.


## C.3.1 Kundennachricht


### C.3.1.1 Nachrichtenformat

Realisierung Bank: verpflichtend

Realisierung Kunde: verpflichtend


## . Beschreibung

Da der Kunde die Dialogsprache erst in dieser Nachricht mitteilt, muss zur Bildung
der Dialoginitialisierungsnachricht der mit der Standardsprache des Kreditinstituts
festgelegte Zeichensatz herangezogen werden. Dieser ist dem Feld ,Standardspra-
che" des Kommunikationszugangs zu entnehmen. Die Antwort des Kreditinstituts er-
folgt dann in der vom Kunden gewünschten Sprache (Zeichensatz).

. Format


<table>
<tr>
<td>Name:</td>
<td>Dialoginitialisierung</td>
</tr>
<tr>
<td>Typ:</td>
<td>Nachricht</td>
</tr>
<tr>
<td>Version:</td>
<td>4</td>
</tr>
<tr>
<td>Sender:</td>
<td>Kunde</td>
</tr>
</table>


<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: C</td>
<td>Version: 3.0-FV</td>
<td>Financial Transaction Services (FinTS) Dokument: Formals</td>
</tr>
<tr>
<td>Seite: 42</td>
<td>Stand: 06.10.2017</td>
<td>Kapitel: Dialogspezifikation<br>Abschnitt: Dialoginitialisierung</td>
</tr>
</table>


<table>
<tr>
<th>Nr.</th>
<th>Name</th>
<th>Ver- sion</th>
<th>Typ</th>
<th>Ken- nung</th>
<th>Sta- tus</th>
<th>An- zahl</th>
<th>Anmerkungen</th>
</tr>
<tr>
<td>1</td>
<td>Nachrichtenkopf</td>
<td>3</td>
<td>SEG</td>
<td>HNHBK</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>2</td>
<td>Signaturkopf</td>
<td>4</td>
<td>SEG</td>
<td>HNSHK</td>
<td>M</td>
<td>1</td>
<td>s. [HBCI], Kap. B.5.1</td>
</tr>
<tr>
<td>3</td>
<td>Identifikation</td>
<td>2</td>
<td>SEG</td>
<td>HKIDN</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>4</td>
<td>Verarbeitungsvor- bereitung</td>
<td>3</td>
<td>SEG</td>
<td>HKVVB</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>5</td>
<td>Zwei-Schritt-TAN- Einreichung</td>
<td>≥6</td>
<td>SEG</td>
<td>HKTAN</td>
<td>O</td>
<td>1</td>
<td>s. [PINTAN], Kap. B.3.3</td>
</tr>
<tr>
<td>6</td>
<td>Anforderung eines öffentlichen Schlüs- sels</td>
<td>3</td>
<td>SEG</td>
<td>HKISA</td>
<td>C</td>
<td>3</td>
<td>M: bei RAH und RDH N: bei DDV und PIN/TAN</td>
</tr>
<tr>
<td>7</td>
<td>Signaturabschluss</td>
<td>2</td>
<td>SEG</td>
<td>HNSHA</td>
<td>M</td>
<td>1</td>
<td>s. [HBCI], Kap. B.5.2</td>
</tr>
<tr>
<td>8</td>
<td>Nachrichtenab- schluss</td>
<td>1</td>
<td>SEG</td>
<td>HNHBS</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
</table>


## . Belegungsrichtlinien


### Zwei-Schritt-TAN-Einreichung

Zur Einleitung des Prozesses der Gewährleistung einer starken Kun-
denauthentifizierung gemäß [PSD2] muss bei TAN-Verfahren ein HKTAN-
Segment ab Segmentversion #6 eingestellt werden, wenn ein Kreditinstitut
die Verwendung von HKTAN ≥ #6 unterstützt (BPD). Wenn HKTAN ≥ #6
nicht gesendet wird, kann der Dialog vom Institut mit dem Rückmeldungs-
code 9075 - Dialog abgebrochen - Starke Authentifizierung
erforderlich abgewiesen werden.

<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th rowspan="2">Version: 3.0-FV</th>
<th rowspan="2">Kapitel: C</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Formals</td>
</tr>
<tr>
<td>Kapitel: Abschnitt:</td>
<td>Dialogspezifikation Dialoginitialisierung</td>
<td>Stand: 06.10.2017</td>
<td>Seite: 43</td>
</tr>
</table>


### C.3.1.2 Segment: Identifikation


#### . Beschreibung

Das Identifikations-Segment enthält Kontextinformationen, die für den gesamten Di-
alog Gültigkeit haben. Anhand dieser Daten wird die Sendeberechtigung des Benut-
zers geprüft. Eine Prüfung der transportmedienspezifischen Kennung des Benutzers
erfolgt nicht.

Falls dem Benutzer die Berechtigung zum Senden weiterer Nachrichten nicht erteilt
werden kann, ist ein entsprechender Rückmeldungscode in die Kreditinstituts-
antwort einzustellen. Es steht Kreditinstituten frei, in bestimmten Fällen auf eine
Identifizierung des Kunden zu verzichten. Dies ist zum Beispiel für den anonymen
Zugang (s.u.) erforderlich, wo mit einem Nichtkunden kommuniziert wird.


<table>
<tr>
<td colspan="2">. Format</td>
</tr>
<tr>
<td>Name:</td>
<td>Identifikation</td>
</tr>
<tr>
<td>Typ:</td>
<td>Segment</td>
</tr>
<tr>
<td>Segmentart:</td>
<td>Administration</td>
</tr>
<tr>
<td>Kennung:</td>
<td>HKIDN</td>
</tr>
<tr>
<td>Bezugssegment:</td>
<td>-</td>
</tr>
<tr>
<td>Version:</td>
<td>2</td>
</tr>
<tr>
<td>Sender:</td>
<td>Kunde</td>
</tr>
</table>


<table>
<tr>
<th>Nr.</th>
<th>Name</th>
<th>Ver- sion</th>
<th>Typ</th>
<th>For- mat</th>
<th>Län- ge</th>
<th>Sta- tus</th>
<th>An- zahl</th>
<th>Restriktionen</th>
</tr>
<tr>
<td>1</td>
<td>Segmentkopf</td>
<td>1</td>
<td>DEG</td>
<td></td>
<td></td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>2</td>
<td>Kreditinstitutsken- nung</td>
<td>1</td>
<td>DEG</td>
<td>kik</td>
<td>#</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>3</td>
<td>Kunden-ID</td>
<td>1</td>
<td>DE</td>
<td>id</td>
<td>#</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>4</td>
<td>Kundensystem-ID</td>
<td>1</td>
<td>DE</td>
<td>id</td>
<td>#</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>5</td>
<td>Kundensystem- Status</td>
<td>1</td>
<td>DE</td>
<td>code</td>
<td>1</td>
<td>M</td>
<td>1</td>
<td>0, 1</td>
</tr>
</table>


#### . Belegungsrichtlinien


##### Kreditinstitutskennung

Es ist die Kennung des Kreditinstituts anzugeben, zu dem der Zugang ge-
wünscht wird. In nachfolgenden Auftragsnachrichten dürfen nur Auftragge-
berkonten dieses Institutbereichs angegeben werden.


##### Kunden-ID

Es ist diejenige Kunden-ID des Benutzers einzustellen, die die Rolle festlegt,
in der er im Rahmen des Dialoges auftritt (s. Kap. C.1.1). Diese Kunden-ID
gilt ebenso für eventuelle Zweit- und Drittsignierende.


## Kundensystem-ID

Die Kundensystem-ID ist beim RAH- / RDH- sowie beim PIN/TAN-Verfahren
erforderlich. Beim DDV-Verfahren ist dieses DE mit dem Wert 0 zu belegen.

<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: C</td>
<td>Version: 3.0-FV</td>
<td>Financial Transaction Services (FinTS) Dokument: Formals</td>
</tr>
<tr>
<td>Seite: 44</td>
<td>Stand: 06.10.2017</td>
<td>Kapitel: Dialogspezifikation<br>Abschnitt: Dialoginitialisierung</td>
</tr>
</table>


![](figures/52.1)


Bevor ein Benutzer bei Verwendung des RAH- / RDH- bzw.
PIN/TAN-Verfahrens von einem neuen Kundensystem Auf-
träge erteilen kann, hat er im Wege einer Synchronisierung
eine Kundensystem-ID für dieses System anzufordern (s.
Kap. C.8).

Bei der Verwendung von RAH-/RDH-Chipkarten ab Sicher-
heitsprofil-Version 3 wird anstatt der Kundensystem-ID die
CID der gesteckten Karte verwendet.


## ◆ Ausgewählte Beispiele für Rückmeldungscodes


<table>
<tr>
<td>Code</td>
<td>Beispiel für Rückmeldungstext</td>
</tr>
<tr>
<td>0020</td>
<td>Informationen fehlerfrei entgegengenommen</td>
</tr>
<tr>
<td>9210</td>
<td>Unbekannter Kunde</td>
</tr>
<tr>
<td>9210</td>
<td>Ungültige Kundensystem-ID</td>
</tr>
</table>


<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th rowspan="2">Version: 3.0-FV</th>
<th rowspan="2">Kapitel: C</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Formals</td>
</tr>
<tr>
<td>Kapitel:<br>Abschnitt:</td>
<td>Dialogspezifikation<br>Dialoginitialisierung</td>
<td>Stand: 06.10.2017</td>
<td>Seite: 45</td>
</tr>
</table>


### C.3.1.3 Segment: Verarbeitungsvorbereitung


#### . Beschreibung

Dieses Segment dient der Übermittlung von Informationen über das Kundensystem,
mit Hilfe derer das Kreditinstitut individuell auf Anforderungen des Kunden reagieren
kann.


#### . Format


<table>
<tr>
<td>Name:</td>
<td>Verarbeitungsvorbereitung</td>
</tr>
<tr>
<td>Typ:</td>
<td>Segment</td>
</tr>
<tr>
<td>Segmentart:</td>
<td>Administration</td>
</tr>
<tr>
<td>Kennung:</td>
<td>HKVVB</td>
</tr>
<tr>
<td>Bezugssegment:</td>
<td>-</td>
</tr>
<tr>
<td>Version:</td>
<td>3</td>
</tr>
<tr>
<td>Sender:</td>
<td>Kunde</td>
</tr>
</table>


<table>
<tr>
<th>Nr.</th>
<th>Name</th>
<th>Ver- sion</th>
<th>Typ</th>
<th>For- mat</th>
<th>Län- ge</th>
<th>Sta- tus</th>
<th>An- zahl</th>
<th>Restriktionen</th>
</tr>
<tr>
<td>1</td>
<td>Segmentkopf</td>
<td>1</td>
<td>DEG</td>
<td></td>
<td></td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>2</td>
<td>BPD-Version</td>
<td>1</td>
<td>DE</td>
<td>num</td>
<td>..3</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>3</td>
<td>UPD-Version</td>
<td>1</td>
<td>DE</td>
<td>num</td>
<td>..3</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>4</td>
<td>Dialogsprache</td>
<td>2</td>
<td>DE</td>
<td>code</td>
<td>..3</td>
<td>M</td>
<td>1</td>
<td>0, 1, 2, 3</td>
</tr>
<tr>
<td>5</td>
<td>Produktbezeich- nung</td>
<td>1</td>
<td>DE</td>
<td>an</td>
<td>.25</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>6</td>
<td>Produktversion</td>
<td>1</td>
<td>DE</td>
<td>an</td>
<td>..5</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
</table>


## . Belegungsrichtlinien


### BPD-Version

Es ist die aktuelle Version der im Kundenprodukt vorliegenden BPD einzu-
stellen. Falls noch keine BPD vorliegen, ist der Wert ,,0" einzustellen. Anhand
dieser Information prüft das Kreditinstitut, ob der Kunde über die aktuelle
BPD-Version verfügt.


## Dialogsprache

Der Kunde darf lediglich ein Sprachkennzeichen einstellen, das im Rahmen
der BPD vom Kreditinstitut an das Kundensystem übermittelt wurde.

Wenn noch keine BPD vorliegen, sollte das Kundenprodukt mit Hilfe eines
anonymen Dialogs die aktuelle BPD des Instituts ermitteln und die Standard-
sprache des Instituts einstellen, die in den Bankparameterdaten mitgeteilt
wird. Falls die BPD nicht abgerufen werden kann, ist der Wert ,0" ein-
zustellen. Das Kreditinstitut antwortet in diesem Fall in seiner Standardspra-
che.


## Produktbezeichnung, Produktversion

Beide Datenelemente sind verpflichtend mit aussagekräftigen Informationen
über das verwendete Kundenprodukt, nicht eine ggf. verwendete interne
FinTS-/HBCI-Bibliothek, zu füllen, um Support-Anfragen leichter beantworten
zu können.

<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: C</td>
<td>Version: 3.0-FV</td>
<td>Financial Transaction Services (FinTS) Dokument: Formals</td>
</tr>
<tr>
<td>Seite:<br>46</td>
<td>Stand: 06.10.2017</td>
<td>Kapitel: Dialogspezifikation<br>Abschnitt: Dialoginitialisierung</td>
</tr>
</table>


Kundenprodukte, die nach dem durch die Deutsche Kreditwirtschaft festge-
legten Verfahren registriert sind, müssen in dieses DE die vergebene Pro-
duktregistrierungsnummer einstellen.


## ◆ Ausgewählte Beispiele für Rückmeldungscodes


<table>
<tr>
<td>Code</td>
<td>Beispiel für Rückmeldungstext</td>
</tr>
<tr>
<td>0020</td>
<td>Informationen fehlerfrei entgegengenommen</td>
</tr>
<tr>
<td>3050</td>
<td>BPD nicht mehr aktuell. Aktuelle Version folgt</td>
</tr>
<tr>
<td>3050</td>
<td>UPD nicht mehr aktuell. Aktuelle Version folgt</td>
</tr>
<tr>
<td>3075</td>
<td>Starke Authentifizierung ab dem ... erforderlich</td>
</tr>
<tr>
<td>3340</td>
<td>RDH-2-Kundenschlüssel neu generieren und einreichen. Wird noch ... Tage akzeptiert</td>
</tr>
<tr>
<td>3345</td>
<td>Sicherheitsprofilwechsel auf RDH-2 durchführen. RDH-2-Kundenschlüssel neu generieren und einreichen. RDH-1 wird noch ... Tage akzeptiert.</td>
</tr>
<tr>
<td>9075</td>
<td>Dialog abgebrochen - starke Authentifizierung erforderlich</td>
</tr>
<tr>
<td>9185</td>
<td>HBCI-/FinTS-Version wird nicht unterstützt</td>
</tr>
<tr>
<td>9210</td>
<td>Sprache wird nicht unterstützt</td>
</tr>
</table>


<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th>Version:</th>
<th rowspan="2">Kapitel: C</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Formals</td>
<td>3.0-FV</td>
</tr>
<tr>
<td>Kapitel:</td>
<td>Dialogspezifikation</td>
<td>Stand:</td>
<td>Seite:</td>
</tr>
<tr>
<td>Abschnitt:</td>
<td>Dialoginitialisierung</td>
<td>06.10.2017</td>
<td>47</td>
</tr>
</table>


### C.3.1.4 Segment: Anforderung eines öffentlichen Schlüssels


#### . Beschreibung

Bei asymmetrischen HBCI Signatur- bzw. Verschlüsselungsverfahren muss dieses
Segment eingestellt werden, da hiermit bei jeder Dialoginitialisierung der eventuell
zwischenzeitlich geänderte öffentliche Chiffrierschlüssel des Kreditinstituts angefor-
dert wird. Falls eine kreditinstitutsseitige Signierung der Nachrichten vorgesehen ist,
muss dieses Segment zusätzlich auch zur Anforderung des öffentlichen Signier-
schlüssels eingestellt werden.

Bei symmetrischen HBCI-Verfahren und TAN-Verfahren unter Verwendung von
HKTAN > Segmentversion #4 darf dieses Segment nicht eingestellt werden.


#### . Format


<table>
<tr>
<td>Name:</td>
<td>Anforderung eines öffentlichen Schlüssels</td>
</tr>
<tr>
<td>Typ:</td>
<td>Segment</td>
</tr>
<tr>
<td>Segmentart:</td>
<td>Administration</td>
</tr>
<tr>
<td>Kennung:</td>
<td>HKISA</td>
</tr>
<tr>
<td>Bezugssegment:</td>
<td>-</td>
</tr>
<tr>
<td>Version:</td>
<td>s. [HBCI], Kap. B.6.1.2</td>
</tr>
<tr>
<td>Sender:</td>
<td>Kunde</td>
</tr>
<tr>
<td>Format:</td>
<td>s. [HBCI], Kap. B.6.1.2</td>
</tr>
</table>


◆ Ausgewählte Beispiele für Rückmeldungscodes


<table>
<tr>
<td>Code</td>
<td>Beispiel</td>
</tr>
<tr>
<td>0020</td>
<td>Angegebener Schlüssel ist noch aktuell</td>
</tr>
<tr>
<td>0020</td>
<td>Angegebener Schlüssel ist nicht mehr aktuell. Der neue Schlüssel wird mitgeteilt</td>
</tr>
<tr>
<td>9010</td>
<td>Sicherheitsverfahren unterstützt keine öffentlichen Schlüssel</td>
</tr>
<tr>
<td>9030</td>
<td>Schlüsselversion nicht mehr aktuell</td>
</tr>
<tr>
<td>9210</td>
<td>Angegebener Schlüssel ist im Kreditinstitut unbekannt</td>
</tr>
</table>


<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: C</td>
<td>Version: 3.0-FV</td>
<td>Financial Transaction Services (FinTS) Dokument: Formals</td>
</tr>
<tr>
<td>Seite: 48</td>
<td>Stand: 06.10.2017</td>
<td>Kapitel: Dialogspezifikation<br>Abschnitt: Dialoginitialisierung</td>
</tr>
</table>


##### C.3.2 Kreditinstitutsnachricht


###### C.3.2.1 Nachrichtenformat

Realisierung Bank: verpflichtend

Realisierung Kunde: verpflichtend


####### . Beschreibung

Sofern die Dialoginitialisierungsnachricht des Kunden fehlerhaft ist, darf die Kredit-
institutsnachricht nur dazu genutzt werden, dem Kunden die betreffenden Rückmel-
decodes mitzuteilen. Es dürfen in diesem Fall keine Datensegmente (z. B. BPD,
UPD) rückgemeldet werden.


#### . Format


<table>
<tr>
<td>Name:</td>
<td>Antwort auf Dialoginitialisierung</td>
</tr>
<tr>
<td>Typ:</td>
<td>Nachricht</td>
</tr>
<tr>
<td>Version:</td>
<td>4</td>
</tr>
<tr>
<td>Sender:</td>
<td>Kreditinstitut</td>
</tr>
</table>


<table>
<tr>
<th>Nr.</th>
<th>Name</th>
<th>Ver- sion</th>
<th>Typ</th>
<th>Ken- nung</th>
<th>Sta- tus</th>
<th>An- zahl</th>
<th>Anmerkungen</th>
</tr>
<tr>
<td>1</td>
<td>Nachrichtenkopf</td>
<td>3</td>
<td>SEG</td>
<td>HNHBK</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>2</td>
<td>Signaturkopf</td>
<td>4</td>
<td>SEG</td>
<td>HNSHK</td>
<td>O</td>
<td>1</td>
<td>s. [HBCI], Kap. B.5.1</td>
</tr>
<tr>
<td>3</td>
<td>Rückmeldungen zur Gesamtnachricht</td>
<td>2</td>
<td>SEG</td>
<td>HIRMG</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>4</td>
<td>Rückmeldungen zu Segmenten</td>
<td>2</td>
<td>SEG</td>
<td>HIRMS</td>
<td>O</td>
<td>n</td>
<td></td>
</tr>
<tr>
<td>5</td>
<td>Bankparameterda- ten</td>
<td>3</td>
<td>SF</td>
<td>#</td>
<td>O</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>6</td>
<td>Userparameterda- ten</td>
<td>3</td>
<td>SF</td>
<td>#</td>
<td>O</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>7</td>
<td>Übermittlung eines öffentlichen Schlüs- sels</td>
<td>3</td>
<td>SEG</td>
<td>HIISA</td>
<td>C</td>
<td>3</td>
<td>O: bei RAH und RDH N: bei DDV und PIN/TAN2</td>
</tr>
<tr>
<td>8</td>
<td>Kreditinstitutsmel- dung</td>
<td>2</td>
<td>SEG</td>
<td>HIKIM</td>
<td>O</td>
<td>n</td>
<td></td>
</tr>
<tr>
<td>9</td>
<td>Zwei-Schritt-TAN- Einreichung</td>
<td>≥6</td>
<td>SEG</td>
<td>HITAN</td>
<td>O</td>
<td>1</td>
<td>s. [PINTAN], Kap. B.3.3</td>
</tr>
<tr>
<td>10</td>
<td>Signaturabschluss</td>
<td>2</td>
<td>SEG</td>
<td>HNSHA</td>
<td>O</td>
<td>1</td>
<td>s. [HBCI], Kap. B.5.2</td>
</tr>
<tr>
<td>11</td>
<td>Nachrichtenab- schluss</td>
<td>1</td>
<td>SEG</td>
<td>HNHBS</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
</table>


## ◆ Ausgewählte Beispiele für Rückmeldungscodes


<table>
<tr>
<td>Code</td>
<td>Beispiel</td>
</tr>
<tr>
<td>0020</td>
<td>Dialoginitialisierung erfolgreich</td>
</tr>
<tr>
<td>9800</td>
<td>Dialogabbruch</td>
</tr>
</table>


<!-- PageFooter: 2 Bei Verwendung von HKTAN > Segmentversion #4 -->
<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th>Version:</th>
<th rowspan="2">Kapitel: C</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Formals</td>
<td>3.0-FV</td>
</tr>
<tr>
<td>Kapitel:</td>
<td>Dialogspezifikation</td>
<td>Stand:</td>
<td>Seite:</td>
</tr>
<tr>
<td>Abschnitt:</td>
<td>Dialoginitialisierung</td>
<td>06.10.2017</td>
<td>49</td>
</tr>
</table>


### C.3.2.2 Segmentfolge: Bankparameterdaten


#### . Beschreibung

Entspricht die vom Kunden übermittelte BPD-Version nicht der aktuellen im Kredit-
institut gespeicherten Version, so erhält der Kunde automatisch die aktuellen Bank-
parameterdaten. Dies gilt auch, wenn ihm zu einem früheren Zeitpunkt bereits die-
selben BPD gesendet wurden. Die BPD werden sofort aktiv, d. h. sie sollten dann
vom Kundenprodukt unmittelbar verwendet werden.

Die Bankparameterdaten müssen stets komplett übertragen werden, d. h. das Aus-
lassen einzelner Segmente ist nicht zulässig. Zu einem späteren Zeitpunkt ist denk-
bar, dass nur die geänderten BPD-Segmente übertragen werden.


#### . Format


<table>
<tr>
<td>Name:</td>
<td>Bankparameterdaten</td>
</tr>
<tr>
<td>Typ:</td>
<td>Segmentfolge</td>
</tr>
<tr>
<td>Sender:</td>
<td>Kreditinstitut</td>
</tr>
<tr>
<td>Format:</td>
<td>s. Kap. D</td>
</tr>
<tr>
<td>Version:</td>
<td>3</td>
</tr>
</table>


<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: C</td>
<td>Version: 3.0-FV</td>
<td>Financial Transaction Services (FinTS) Dokument: Formals</td>
</tr>
<tr>
<td>Seite:<br>50</td>
<td>Stand: 06.10.2017</td>
<td>Kapitel: Dialogspezifikation<br>Abschnitt: Dialoginitialisierung</td>
</tr>
</table>


##### C.3.2.3 Segmentfolge: Userparameterdaten


###### . Beschreibung

Entspricht die vom Kunden übermittelte UPD-Version nicht der aktuellen im Kredit-
institut gespeicherten Version, so erhält der Kunde automatisch die aktuellen User-
parameterdaten. Dies gilt auch, wenn ihm zu einem früheren Zeitpunkt bereits die-
selben UPD gesendet wurden. Die UPD werden sofort aktiv, d. h. sie sollten dann
vom Kundenprodukt unmittelbar verwendet werden.

Die Userparameterdaten müssen stets komplett übertragen werden, d. h. das Aus-
lassen einzelner Segmente ist nicht zulässig. Zu einem späteren Zeitpunkt ist denk-
bar, dass nur die geänderten UPD-Segmente übertragen werden.


![](figures/58.1)


Es ist zu beachten, dass lediglich die Userparameterdaten des sich
anmeldenden Benutzers aktualisiert werden. Falls mehrere Benut-
zer an der Erstellung der Aufträge beteiligt sind (z. B. bei Mehrfach-
signaturen), so ist sicherzustellen, dass auch für die passiven Be-
nutzer, die die Aufträge nicht versenden, sondern lediglich signie-
ren, stets die aktuellen UPD vorliegen.

Hierzu haben sich die passiven Benutzer in regelmäßigen Abstän-
den beim Kreditinstitut mit einer Dialoginitialisierung anzumelden,
damit ggf. ihre Userparameterdaten aktualisiert werden können.
Dieses Verfahren kann vom Kundenprodukt durch eine automati-
sche Aufforderung unterstützt werden.


#### . Format


<table>
<tr>
<td>Name:</td>
<td>Userparameterdaten</td>
</tr>
<tr>
<td>Typ:</td>
<td>Segmentfolge</td>
</tr>
<tr>
<td>Sender:</td>
<td>Kreditinstitut</td>
</tr>
<tr>
<td>Format:</td>
<td>s. Kap. E</td>
</tr>
<tr>
<td>Version:</td>
<td>3</td>
</tr>
</table>


<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th rowspan="2">Version: 3.0-FV</th>
<th rowspan="2">Kapitel: C</th>
</tr>
<tr>
<th>Dokument:</th>
<th>Formals</th>
</tr>
<tr>
<td>Kapitel:<br>Abschnitt:</td>
<td>Dialogspezifikation Dialoginitialisierung</td>
<td>Stand: 06.10.2017</td>
<td>Seite: 51</td>
</tr>
</table>


### C.3.2.4 Segment: Übermittlung eines öffentlichen Schlüssels


#### . Beschreibung

Falls bei asymmetrischen HBCI Signatur- bzw. Verschlüsselungsverfahren einer der
öffentlichen Schlüssel des Kreditinstituts aktualisiert wurde, wird dem Kunden dieser
in diesem Segment zurückgemeldet. Das Segment kann sowohl für den Signier-
schlüssel als auch für den Chiffrierschlüssel eingestellt werden. Hat sich der jewei-
lige Schlüssel nicht geändert, so wird das Segment nicht gesendet.

Zur Verifizierung der Richtigkeit des öffentlichen Schlüssels muss entweder die Dia-
loginitialisierungs-Antwortnachricht signiert sein oder es muss auf alternativem Weg
(z. B. Brief) ein neuer Hashwert übermittelt werden.

Bei symmetrischen HBCI-Verfahren und TAN-Verfahren unter Verwendung von
HKTAN > Segmentversion #4 darf dieses Segment nicht eingestellt werden.

Zwangsweiser Wechsel der Schlüssel des Kunden

Mit dem Rückmeldungscode 3340 kann das Kreditinstitut dem Kundensystem signa-
lisieren, dass es die RDH-2-Kundenschlüssel neu generieren soll. Dies kann z. B.
bei einer Aufhebung der Einschränkungen bezüglich der maximalen Schlüssellän-
gen des Bankenprofils (s. [HBCI], Kap. B.1.1) erforderlich sein. Die neu generierten
öffentlichen RDH-2-Schlüssel des Kunden müssen anschließend mit dem Ge-
schäftsvorfall "Änderung eines öffentlichen Schlüssels des Kunden einreichen" (s.
[HBCI], Kap. B.6.2.1) an das Kreditinstitut übermittelt werden.

Wechsel des Sicherheitsprofils von RDH-1 auf RDH-2

Mit dem Rückmeldungscode 3345 kann das Kreditinstitut dem Kundensystem signa-
lisieren, dass es einen Sicherheitsprofilwechsel von RDH-1 auf RDH-2 durchführen
soll. Dazu muss das Kundensystem ein neues RDH-2- Sicherheitsmedium erzeugen
und die RDH-2-Kundenschlüssel neu generieren. Die neu generierten öffentlichen
RDH-2-Schlüssel des Kunden müssen anschließend mit dem Geschäftsvorfall "Än-
derung eines öffentlichen Schlüssels des Kunden einreichen" (s. [HBCI], Kap.
B.6.2.1) an das Kreditinstitut übermittelt werden.


#### . Format


<table>
<tr>
<td>Name:</td>
<td>Übermittlung eines öffentlichen Schlüssels</td>
</tr>
<tr>
<td>Typ:</td>
<td>Segment</td>
</tr>
<tr>
<td>Segmentart:</td>
<td>Administration</td>
</tr>
<tr>
<td>Kennung:</td>
<td>HIISA</td>
</tr>
<tr>
<td>Bezugssegment:</td>
<td>HKISA</td>
</tr>
<tr>
<td>Version:</td>
<td>s. [HBCI], Kap. B.6.1.3</td>
</tr>
<tr>
<td>Sender:</td>
<td>Kreditinstitut</td>
</tr>
<tr>
<td>Format:</td>
<td>s. [HBCI], Kap. B.6.1.3</td>
</tr>
</table>


<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: C</td>
<td>Version: 3.0-FV</td>
<td>Financial Transaction Services (FinTS) Dokument: Formals</td>
</tr>
<tr>
<td>Seite:<br>52</td>
<td>Stand: 06.10.2017</td>
<td>Kapitel: Dialogspezifikation<br>Abschnitt: Dialoginitialisierung</td>
</tr>
</table>


##### C.3.2.5 Segment: Kreditinstitutsmeldung


###### . Beschreibung

Kreditinstitutsmeldungen können z. B. Werbenachrichten oder auch kundenrele-
vante Informationen zu Geschäftsvorfällen, die nicht in Rückmeldungscodes abge-
bildet werden können, beinhalten. Diese werden dem Kunden automatisch im Rah-
men der Dialoginitialisierungsantwortnachricht übermittelt. Dadurch wird gewähr-
leistet, dass die Zustellung dieser Meldungen nicht auf Initiative des Kunden erfol-
gen muss.

Es ist lediglich die Übermittlung von unformatierten Textnachrichten möglich.


![](figures/60.1)


Kreditinstitutsmeldungen können dem Kunden unmittelbar nach Er-
halt, d. h. z. B. während im Hintergrund der Dialog abläuft, ange-
zeigt werden.

Hersteller von Kundenprodukten sollten darüber hinaus eine Mög-
lichkeit zur Verwaltung von Kreditinstitutsmeldungen vorsehen. Falls
mehrere Meldungen gleichzeitig vorliegen, sollte der Kunde die
Möglichkeit haben, die Meldungen nacheinander zu bearbeiten
(Funktionen „Nächste lesen“, „Vorherige lesen“). Ferner sollten Kre-
ditinstitutsmeldungen gespeichert, gelöscht und ausgedruckt wer-
den können.


###### . Format


<table>
<tr>
<td>Name:</td>
<td>Kreditinstitutsmeldung</td>
</tr>
<tr>
<td>Typ:</td>
<td>Segment</td>
</tr>
<tr>
<td>Segmentart:</td>
<td>Administration</td>
</tr>
<tr>
<td>Kennung:</td>
<td>HIKIM</td>
</tr>
<tr>
<td>Bezugssegment:</td>
<td>-</td>
</tr>
<tr>
<td>Version:</td>
<td>2</td>
</tr>
<tr>
<td>Sender:</td>
<td>Kreditinstitut</td>
</tr>
</table>


<table>
<tr>
<th>Nr.</th>
<th>Name</th>
<th>Ver- sion</th>
<th>Typ</th>
<th>For- mat</th>
<th>Län- ge</th>
<th>Sta- tus</th>
<th>An- zahl</th>
<th>Restriktionen</th>
</tr>
<tr>
<td>1</td>
<td>Segmentkopf</td>
<td>1</td>
<td>DEG</td>
<td></td>
<td></td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>2</td>
<td>Betreff</td>
<td>1</td>
<td>DE</td>
<td>an</td>
<td>..35</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>3</td>
<td>Freitextmeldung</td>
<td>1</td>
<td>DE</td>
<td>txt</td>
<td>..<br>2048</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
</table>


###### . Belegungsrichtlinien


###### Freitextmeldung

Die Daten dürfen nicht um führende oder nachfolgende Leerzeichen gekürzt
werden.

<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th>Version:</th>
<th rowspan="2">Kapitel: C</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Formals</td>
<td>3.0-FV</td>
</tr>
<tr>
<td>Kapitel:</td>
<td>Dialogspezifikation</td>
<td>Stand:</td>
<td>Seite:</td>
</tr>
<tr>
<td>Abschnitt:</td>
<td>Dialogbeendigung</td>
<td>06.10.2017</td>
<td>53</td>
</tr>
</table>


## C.4 Dialogbeendigung

Jeder Dialog ist durch eine Dialogendenachricht zu beenden (Ausnahmen s. Kap.
C.4.1). Das Senden der Dialogbeendigung hat zwei Funktionen: Zum einen teilt der
Kunde mit, dass keine weiteren Nachrichten folgen und die Verbindung zum Kredit-
institut beendet werden soll. Zum anderen bestätigt der Kunde hiermit implizit den
Erhalt aller vorangegangenen Kreditinstitutsnachrichten des Dialoges.

Nach Erhalt der Kreditinstitutsantwortnachricht ist der Dialog logisch beendet. An-
schließend muss das Kundenprodukt entweder die Kommunikation physisch been-
den oder einen neuen Dialog für diesen Benutzer beginnen. Falls der Kunde keine
Dialogbeendigung sendet, wird der Dialog kreditinstitutsseitig nach einem trans-
portmedienabhängigen Timeout beendet.

Der Dialog kann auch bereits direkt nach der Dialoginitialisierung beendet werden,
sofern der Kunde bspw. lediglich seine BPD und UPD aktualisieren möchte.

Realisierung Bank: verpflichtend

Realisierung Kunde: verpflichtend


## C.4.1 Ausnahmen zur Dialogbeendigung

Im Fall eines impliziten Dialogendes bei Verwendung von starker Authentifizierung
(s. [PINTAN], Kap. B.3.3) wird ein Dialog nicht durch eine explizite Dialogendenach-
richt des Benutzers / Kreditinstituts beendet.


## C.4.2 Kundennachricht


### C.4.2.1 Nachrichtenformat


#### . Beschreibung

Die Nachricht muss signiert und verschlüsselt werden (Ausnahmen s. Kap. C.4.1)
und wird mit einer Standard-Kreditinstitutsnachricht beantwortet. Die Nachricht ist
von demjenigen Benutzer zu signieren, der auch die Dialoginitialisierung signiert
hat.


##### . Format


<table>
<tr>
<td>Name:</td>
<td>Dialogbeendigung</td>
</tr>
<tr>
<td>Typ:</td>
<td>Nachricht</td>
</tr>
<tr>
<td>Version:</td>
<td>3</td>
</tr>
<tr>
<td>Sender:</td>
<td>Kunde</td>
</tr>
</table>


<table>
<tr>
<th>Nr.</th>
<th>Name</th>
<th>Ver- sion</th>
<th>Typ</th>
<th>Ken- nung</th>
<th>Sta- tus</th>
<th>An- zahl</th>
<th>Anmerkungen</th>
</tr>
<tr>
<td>1</td>
<td>Nachrichtenkopf</td>
<td>3</td>
<td>SEG</td>
<td>HNHBK</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>2</td>
<td>Signaturkopf</td>
<td>4</td>
<td>SEG</td>
<td>HNSHK</td>
<td>M</td>
<td>1</td>
<td>s. [HBCI], Kap. B.5.1</td>
</tr>
<tr>
<td>3</td>
<td>Dialogende</td>
<td>1</td>
<td>SEG</td>
<td>HKEND</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>4</td>
<td>Signaturabschluss</td>
<td>2</td>
<td>SEG</td>
<td>HNSHA</td>
<td>M</td>
<td>1</td>
<td>s. [HBCI], Kap. B.5.2</td>
</tr>
<tr>
<td>5</td>
<td>Nachrichtenab- schluss</td>
<td>1</td>
<td>SEG</td>
<td>HNHBS</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
</table>


<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: C</td>
<td>Version: 3.0-FV</td>
<td>Financial Transaction Services (FinTS) Dokument: Formals</td>
</tr>
<tr>
<td>Seite:<br>54</td>
<td>Stand: 06.10.2017</td>
<td>Kapitel: Dialogspezifikation<br>Abschnitt: Dialogbeendigung</td>
</tr>
</table>


### C.4.2.2 Segment: Dialogende


<table>
<tr>
<td colspan="2">. Format</td>
</tr>
<tr>
<td>Name:</td>
<td>Dialogende</td>
</tr>
<tr>
<td>Typ:</td>
<td>Segment</td>
</tr>
<tr>
<td>Segmentart:</td>
<td>Administration</td>
</tr>
<tr>
<td>Kennung:</td>
<td>HKEND</td>
</tr>
<tr>
<td>Bezugssegment:</td>
<td>-</td>
</tr>
<tr>
<td>Version:</td>
<td>1</td>
</tr>
<tr>
<td>Sender:</td>
<td>Kunde</td>
</tr>
</table>


<table>
<tr>
<th>Nr.</th>
<th>Name</th>
<th>Ver- sion</th>
<th>Typ</th>
<th>For- mat</th>
<th>Län- ge</th>
<th>Sta- tus</th>
<th>An- zahl</th>
<th>Restriktionen</th>
</tr>
<tr>
<td>1</td>
<td>Segmentkopf</td>
<td>1</td>
<td>DEG</td>
<td></td>
<td></td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>2</td>
<td>Dialog-ID</td>
<td>1</td>
<td>DE</td>
<td>id</td>
<td>#</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
</table>


#### . Belegungsrichtlinien


#### Dialog-ID

Es ist die Dialog-ID des zu beendigenden Dialoges einzustellen.


## C.4.3 Kreditinstitutsnachricht


### . Beschreibung

Das Kreditinstitut bestätigt die Dialogbeendigung mit dem Rückmeldungscode 0100
(,,Dialog beendet“).


### . Format


<table>
<tr>
<td>Name:</td>
<td>Kreditinstitutsnachricht allgemein</td>
</tr>
<tr>
<td>Typ:</td>
<td>Nachricht</td>
</tr>
<tr>
<td>Format:</td>
<td>s. Kap. B.7.1</td>
</tr>
</table>


### ◆ Erläuterungen

Es werden keine Datensegmente zurückgemeldet.


### ◆ Ausgewählte Beispiele für Rückmeldungscodes


<table>
<tr>
<td>Code</td>
<td>Beispiel für Rückmeldungstext</td>
</tr>
<tr>
<td>0100</td>
<td>Dialog beendet</td>
</tr>
</table>


<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th rowspan="2">Version: 3.0-FV</th>
<th rowspan="2">Kapitel: C</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Formals</td>
</tr>
<tr>
<td>Kapitel: Abschnitt:</td>
<td>Dialogspezifikation Anonymer Zugang</td>
<td>Stand: 06.10.2017</td>
<td>Seite: 55</td>
</tr>
</table>


## C.5 Anonymer Zugang

Um Kunden die Möglichkeit zu geben, sich anonym anzumelden, um sich bspw.
über die angebotenen Geschäftsvorfälle fremder Kreditinstitute (von denen sie keine
BPD besitzen) zu informieren bzw. nicht-signierungspflichtige Aufträge bei fremden
Kreditinstituten einreichen zu können, kann sich der Kunde anonym (als Gast) an-
melden.

Die Zugangsdaten zu den Fremdinstituten erhält der Kunde über den Abruf der
Kommunikationszugänge (s. Anlagen).

Bei anonymen Dialogen werden Nachrichten weder signiert, noch können sie ver-
schlüsselt und komprimiert werden.

Realisierung Bank: optional

Realisierung Kunde: optional


## C.5.1 Dialoginitialisierung


### a) Kundennachricht

. Format


<table>
<tr>
<td>Name:</td>
<td>Dialoginitialisierung bei anonymem Zugang</td>
</tr>
<tr>
<td>Typ:</td>
<td>Nachricht</td>
</tr>
<tr>
<td>Version:</td>
<td>3</td>
</tr>
<tr>
<td>Sender:</td>
<td>Kunde</td>
</tr>
</table>


<table>
<tr>
<th>Nr.</th>
<th>Name</th>
<th>Ver- sion</th>
<th>Typ</th>
<th>Ken- nung</th>
<th>Sta- tus</th>
<th>An- zahl</th>
<th>Anmerkungen</th>
</tr>
<tr>
<td>1</td>
<td>Nachrichtenkopf</td>
<td>3</td>
<td>SEG</td>
<td>HNHBK</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>2</td>
<td>Identifikation</td>
<td>2</td>
<td>SEG</td>
<td>HKIDN</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>3</td>
<td>Verarbeitungsvor- bereitung</td>
<td>3</td>
<td>SEG</td>
<td>HKVVB</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>4</td>
<td>Nachrichtenab- schluss</td>
<td>1</td>
<td>SEG</td>
<td>HNHBS</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
</table>


### . Belegungsrichtlinien


#### Identifikation

Die Datenelemente des Identifikationssegments sind wie folgt zu belegen:

· Kreditinstitutskennung: Ländercode und BLZ des gewünschten Instituts

. Kunden-ID:
99999999993

. Kundensystem-ID:
0

. Kundensystem-Status:
0

<!-- PageFooter: 3 Diese Kunden-ID darf daher nicht an Kunden vergeben werden. -->
<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: C</td>
<td>Version: 3.0-FV</td>
<td>Financial Transaction Services (FinTS) Dokument: Formals</td>
</tr>
<tr>
<td>Seite:<br>56</td>
<td>Stand: 06.10.2017</td>
<td>Kapitel: Dialogspezifikation<br>Abschnitt: Anonymer Zugang</td>
</tr>
</table>


## Verarbeitungsvorbereitung

Mit diesem Segment fordert der Kunde die Bankparameterdaten des Kredit-
instituts an.

Sofern schon von einem früheren anonymen Zugang Bank- oder Userpara-
meterdaten dieses Kreditinstituts vorliegen, ist die jeweilige Versionsnummer
anzugeben.


## b) Kreditinstitutsnachricht

. Format


<table>
<tr>
<td>Name:</td>
<td>Antwort auf anonyme Dialoginitialisierung</td>
</tr>
<tr>
<td>Typ:</td>
<td>Nachricht</td>
</tr>
<tr>
<td>Version:</td>
<td>3</td>
</tr>
<tr>
<td>Sender:</td>
<td>Kreditinstitut</td>
</tr>
</table>


<table>
<tr>
<th>Nr.</th>
<th>Name</th>
<th>Ver- sion</th>
<th>Typ</th>
<th>Ken- nung</th>
<th>Sta- tus</th>
<th>An- zahl</th>
<th>Anmerkungen</th>
</tr>
<tr>
<td>1</td>
<td>Nachrichtenkopf</td>
<td>3</td>
<td>SEG</td>
<td>HNHBK</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>2</td>
<td>Rückmeldungen zur Gesamtnachricht</td>
<td>2</td>
<td>SEG</td>
<td>HIRMG</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>3</td>
<td>Rückmeldungen zu Segmenten</td>
<td>2</td>
<td>SEG</td>
<td>HIRMS</td>
<td>O</td>
<td>n</td>
<td></td>
</tr>
<tr>
<td>4</td>
<td>Bankparameterda- ten</td>
<td>3</td>
<td>SF</td>
<td>#</td>
<td>O</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>5</td>
<td>Userparameterda- ten</td>
<td>3</td>
<td>SF</td>
<td>#</td>
<td>O</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>6</td>
<td>Kreditinstitutsmel- dung</td>
<td>2</td>
<td>SEG</td>
<td>HIKIM</td>
<td>O</td>
<td>n</td>
<td></td>
</tr>
<tr>
<td>7</td>
<td>Nachrichtenab- schluss</td>
<td>1</td>
<td>SEG</td>
<td>HNHBS</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
</table>


## . Belegungsrichtlinien


## Bankparameterdaten

Die BPD bei einem anonymen Zugang sind identisch mit denen bei einem
Zugang als Kunde.


## Userparameterdaten

In den Gast-UPD sind im DE „Erlaubte Geschäftsvorfälle“ diejenigen Ge-
schäftsvorfälle aufgeführt, die der Gast ausführen darf. Dies können jedoch
nur Geschäftsvorfälle sein, für die keine Signatur erforderlich ist, wie z. B.
der Abruf von Börsenkursen oder die Sendung einer Gastmeldung (Die Fest-
legung, für welche Geschäftsvorfälle eine Signatur erforderlich ist, ist insti-
tutsspezifisch).

Als Benutzerkennung wird in den Gast-UPD eine Standardkennung einge-
tragen, indem das Feld mit der Ziffer '9' aufgefüllt wird. Diese Kennung darf
daher nicht an tatsächliche Benutzer vergeben werden. In der Kontoverbin-
dung sind Kreditinstitutskennung und Länderkennzeichen mit den Werten
des Kreditinstituts zu belegen. Als Kontonummer wird ebenfalls eine Stan-
dardkennung eingegeben, die in derselben Weise wie die Benutzerkennung
zu bilden ist. Kunden-ID ist der Wert ,,9999999999", wie in der Kundennach-
richt.

<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th rowspan="2">Version: 3.0-FV</th>
<th rowspan="2">Kapitel: C</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Formals</td>
</tr>
<tr>
<td>Kapitel:<br>Abschnitt:</td>
<td>Dialogspezifikation Anonymer Zugang</td>
<td>Stand: 06.10.2017</td>
<td>Seite: 57</td>
</tr>
</table>


## Kreditinstitutsmeldung

Bei den Meldungen kann es sich lediglich um allgemeine, d. h. nicht benut-
zerspezifische Informationen handeln.


## C.5.2 Auftragsnachricht


### a) Kundennachricht


#### . Format


<table>
<tr>
<td>Name:</td>
<td>Kundennachricht allgemein bei anonymem Zugang</td>
</tr>
<tr>
<td>Typ:</td>
<td>Nachricht</td>
</tr>
<tr>
<td>Version:</td>
<td>4</td>
</tr>
<tr>
<td>Sender:</td>
<td>Kunde</td>
</tr>
</table>


<table>
<tr>
<th>Nr.</th>
<th>Name</th>
<th>Ver- sion</th>
<th>Typ</th>
<th>Ken- nung</th>
<th>Sta- tus</th>
<th>An- zahl</th>
<th>Anmerkungen</th>
</tr>
<tr>
<td>1</td>
<td>Nachrichtenkopf</td>
<td>3</td>
<td>SEG</td>
<td>HNHBK</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>2</td>
<td>Aufträge</td>
<td>2</td>
<td>SF</td>
<td>#</td>
<td>O</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>3</td>
<td>Nachrichtenab- schluss</td>
<td>1</td>
<td>SEG</td>
<td>HNHBS</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
</table>


### . Belegungsrichtlinien


#### Aufträge

Es dürfen lediglich nicht-signierungspflichtige Geschäftsvorfälle (z. B. Abruf
von Börsenkursen, Gastmeldung) eingestellt werden. Welche Geschäftsvor-
fälle signierungspflichtig sind, bestimmt das Kreditinstitut in der UPD des
Kunden.

Die Auftraggeberkontonummer ist jeweils mit dem Wert „9999999999" zu be-
legen.


## b) Kreditinstitutsnachricht

Format


<table>
<tr>
<td>Name:</td>
<td>Kreditinstitutsnachricht allgemein</td>
</tr>
<tr>
<td>Typ:</td>
<td>Nachricht</td>
</tr>
<tr>
<td>Format:</td>
<td>s. Kap. B.7.1</td>
</tr>
</table>


## C.5.3 Dialogbeendigung


## a) Kundennachricht

. Format


<table>
<tr>
<td>Name:</td>
<td>Dialogbeendigung bei anonymem Zugang</td>
</tr>
<tr>
<td>Typ:</td>
<td>Nachricht</td>
</tr>
<tr>
<td>Version:</td>
<td>3</td>
</tr>
<tr>
<td>Sender:</td>
<td>Kunde</td>
</tr>
</table>


<table>
<tr>
<th>Nr.</th>
<th>Name</th>
<th>Ver- sion</th>
<th>Typ</th>
<th>Ken- nung</th>
<th>Sta- tus</th>
<th>An- zahl</th>
<th>Anmerkungen</th>
</tr>
<tr>
<td>1</td>
<td>Nachrichtenkopf</td>
<td>3</td>
<td>SEG</td>
<td>HNHBK</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>2</td>
<td>Dialogende</td>
<td>1</td>
<td>SEG</td>
<td>HKEND</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>3</td>
<td>Nachrichtenab-</td>
<td>1</td>
<td>SEG</td>
<td>HNHBS</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
</table>


<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: C</td>
<td>Version: 3.0-FV</td>
<td>Financial Transaction Services (FinTS) Dokument: Formals</td>
</tr>
<tr>
<td>Seite:<br>58</td>
<td>Stand: 06.10.2017</td>
<td>Kapitel: Dialogspezifikation<br>Abschnitt: Anonymer Zugang</td>
</tr>
</table>


<table>
<tr>
<td></td>
<td>schluss</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</table>


## b) Kreditinstitutsnachricht


### . Format


<table>
<tr>
<td>Name:</td>
<td>Kreditinstitutsnachricht allgemein</td>
</tr>
<tr>
<td>Typ:</td>
<td>Nachricht</td>
</tr>
<tr>
<td>Format:</td>
<td>s. Kap. B.7.1</td>
</tr>
</table>


### ◆ Erläuterungen

Es werden keine Datensegmente zurückgemeldet.


### ◆ Ausgewählte Beispiele für Rückmeldungscodes


<table>
<tr>
<td>Code</td>
<td>Beispiel für Rückmeldungstext</td>
</tr>
<tr>
<td>0100</td>
<td>Dialog beendet</td>
</tr>
</table>


<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th rowspan="2">Version: 3.0-FV</th>
<th rowspan="2">Kapitel: C</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Formals</td>
</tr>
<tr>
<td>Kapitel:<br>Abschnitt:</td>
<td>Dialogspezifikation Verbindungsabbruch</td>
<td>Stand: 06.10.2017</td>
<td>Seite: 59</td>
</tr>
</table>


## C.6 Verbindungsabbruch

Im Unterschied zu einigen derzeit aktuellen Transportmedien erfolgt in keinem Fall
kreditinstitutsseitig ein Abbruch der Übertragung von Kundennachrichten; auch dann
nicht, wenn kreditinstitutsseitig bereits ein Fehler in der Nachricht während der
Übertragung festgestellt wird. Der Abbruch wird aus Gründen der Einheitlichkeit
nicht durchgeführt, weil entsprechende Funktionalitäten nicht bei allen Kommunikati-
onsdiensten zur Verfügung stehen.

Bzgl. Verbindungsstörungen bzw. Abbrüchen sind aus Sicht des Kreditinstituts fol-
gende Fälle zu unterscheiden:


## Fall 1: Abbruch während der Kunde eine Dialoginitialisierung an das Kredit- institut sendet

Der Kunde konnte in diesem Fall nicht identifiziert werden. Die Legitimation
konnte dem gemäß nicht erteilt werden.

Fall 2: Abbruch nachdem der Kunde eine Dialoginitialisierung an das Kredit-
institut gesendet hat

Die Nachricht wurde erhalten. Anschließend wurde der Kunde identifiziert
und die Legitimation erteilt. Das Kreditinstitut erwartet eine Auftragsnach-
richt. Diese kann jedoch nicht eintreffen, da der Kunde die Antwortnachricht
nicht erhalten hat.

Fall 3: Abbruch während der Kunde eine Auftragsnachricht an das Kredit-
institut sendet

In diesem Fall ignoriert das Kreditinstitut das erhaltene Nachrichtenfragment.

Fall 4: Abbruch nachdem der Kunde eine Auftragsnachricht an das Kredit-
institut gesendet hat

Der Abbruch erfolgt hierbei bevor oder während das Kreditinstitut die Ant-
wortnachricht an den Kunden sendet. In diesem Fall wird die erhaltene
Nachricht vom Kreditinstitut bearbeitet.

Bei einem Abbruch konnte der Dialog nicht ordnungsgemäß beendet werden. So
fehlt z. B. die ordnungsgemäße Dialogbeendigung oder es fehlen bei einem Ab-
bruch während der Dialoginitialisierung die Auftragsnachrichten. Das Kreditinstitut
hat dennoch den Dialog als abgeschlossen zu betrachten, da der Kunde einen neu-
en Dialog beginnen muss, um sich über den Status der abgebrochenen Nachricht
zu informieren.


![](figures/67.1)


Verhalten auf Kundenseite:

Erfolgt der Abbruch während oder nach der Dialoginitialisierung (Fall
1 und 2), ist der Dialog auf jeden Fall mit einer erneuten Dialoginitia-
lisierung zu beginnen.

<!-- PageBreak -->


<table>
<tr>
<td>Kapitel:<br>C</td>
<td>Version: 3.0-FV</td>
<td>Financial Transaction Services (FinTS) Dokument: Formals</td>
</tr>
<tr>
<td>Seite: 60</td>
<td>Stand: 06.10.2017</td>
<td>Kapitel: Dialogspezifikation<br>Abschnitt: Verbindungsabbruch</td>
</tr>
</table>


Abbildung 9: Verbindungsabbruch Fall 1

![Nach- richten- nr. Sig- natur- ID Dialog- referenzen K Sig- natur- ID 1 5 Initialisierung 1 ohne Auftragsteil Be-Ref1 r 4 e B d e i t n u Be-Ref2 2 6 Initialisierung 2 i 4 → 6 t Antwortnachricht 1 n z Be-Ref2 / Kr-Ref1 s e t 2 7 r Benutzernachricht 3 Be-Ref2 / Kr-Ref1 i 6 → 7 t Antwortnachricht 2 u t Be-Ref2 / Kr-Ref1](figures/68.1)


Abbildung 10: Verbindungsabbruch Fall 2

![Nach- richten- nr. Sig- natur- ID Dialog- referenzen K Sig- natur- ID 1 5 Initialisierung 1 ohne Auftragsteil Be-Ref1 r 4 → 5 Antwortnachricht 1 e B d e Be-Ref1 / Kr-Ref1 i t n 2 6 u Initialisierung 2 Be-Ref2 i t 5 → 6 Antwortnachricht 2 n z Be-Ref2 / Kr-Ref2 s e t 2 7 r Benutzernachricht 3 Be-Ref2 / Kr-Ref2 i 6 → 7 Antwortnachricht 3 t Be-Ref2 / Kr-Ref2 u t](figures/68.2)


Im Falle eines Abbruch während oder nach dem Senden einer Auf-
tragsnachricht (Fall 3 und 4) ist für das Kundenprodukt im Regelfall
nicht nachvollziehbar, zu welchem dieser beiden Zeitpunkte der Ab-
bruch erfolgt ist. Diese Kenntnis ist jedoch erforderlich, um zu ent-
scheiden, ob die Auftragsnachricht erneut gesendet werden muss.

Das Kundenprodukt sendet hierzu eine Synchronisierungsnachricht.

<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th>Version:</th>
<th rowspan="2">Kapitel: C</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Formals</td>
<td>3.0-FV</td>
</tr>
<tr>
<td>Kapitel:<br>Abschnitt:</td>
<td>Dialogspezifikation Verbindungsabbruch</td>
<td>Stand: 06.10.2017</td>
<td>Seite: 61</td>
</tr>
</table>


In der Antwortnachricht erhält es die letzte Nachrichtennummer der
Kundennachricht, die im abgebrochenen Dialog noch verarbeitet
wurde. Anhand dieser Information ist für das Kundenprodukt ersicht-
lich, welche Auftragsnachrichten noch gesendet werden müssen.


Abbildung 11: Verbindungsabbruch Fall 3

![Nach- richten- nr. Sig- natur- ID Dialog- referenzen Sig- natur- ID Benutzernachricht mit Initialisierung Be-Ref1 1 5 K Antwortnachricht 1 4 → 5 r Be-Ref1 / Kr-Ref1 e B 2 6 Benutzernachricht mit Auftragsteil 1 Be-Ref1 / Kr-Ref1 d e i n Be-Ref2 t 1 7 u Synchronisierung i 5 → 7 t Antwortnachricht 2 (# = 1) Be-Ref2 / Kr-Ref2 n z s e Benutzernachricht mit Initialisierung Be-Ref3 t 1 8 r Antwortnachricht 3 i 7 → 8 Be-Ref3 / Kr-Ref3 t Be-Ref3 / Kr-Ref3 u 2 9 Benutzernachricht mit Auftragsteil 1 t 8 → 9 Antwortnachricht 4 Be-Ref3 / Kr-Ref3](figures/69.1)


![Nach- richten- nr. Sig- natur- ID Dialog- referenzen Sig- natur- ID K Benutzernachricht mit Initialisierung Be-Ref1 r 1 5 Antwortnachricht 1 4 → 5 e B Be-Ref1 / Kr-Ref1 d e i n Benutzernachricht mit Auftragsteil 1 Be-Ref1 / Kr-Ref1 t 2 6 u Antwortnachricht 2 i 5 → 6 t Be-Ref1 / Kr-Ref1 n z s e t 1 7 r Synchronisierung Be-Ref2 i t 6 → 7 Antwortnachricht 3 (# = 2) Be-Ref2 / Kr-Ref2 u t Abbildung 12: Verbindungsabbruch Fall 4](figures/69.2)


<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: C</td>
<td>Version: 3.0-FV</td>
<td>Financial Transaction Services (FinTS) Dokument: Formals</td>
</tr>
<tr>
<td>Seite:<br>62</td>
<td>Stand: 06.10.2017</td>
<td>Kapitel: Dialogspezifikation<br>Abschnitt: Verbindungsabbruch</td>
</tr>
</table>


Eine erneut zu sendende Nachricht darf nicht unverändert (bit-
identisch) gesendet werden, da sie aufgrund der nicht mehr aktuel-
len Signatur-ID (s. [HBCI] Kap. B.4) als Doppeleinreichung abgelehnt
würde. Daher muss diese Nachricht im Signaturkopf und -abschluss
eine neue Signatur-ID und folglich auch eine neue elektronische
Signatur erhalten.

<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th rowspan="2">Version: 3.0-FV</th>
<th rowspan="2">Kapitel: C</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Formals</td>
</tr>
<tr>
<td>Kapitel: Abschnitt:</td>
<td>Dialogspezifikation Statusprotokoll</td>
<td>Stand: 06.10.2017</td>
<td>Seite: 63</td>
</tr>
</table>


# C.7 Statusprotokoll

Um dem Kunden bzw. dem Kundensystem die Möglichkeit zu geben, den Verarbei-
tungsstatus von Nachrichten abzufragen, kann kreditinstitutsseitig ein Statusproto-
koll geführt werden, in dem die Status aller Aufträge aufgeführt sind. Die kreditinsti-
tutsseitige Unterstützung des Statusprotokolls ist optional. Es ist also zulässig, dass
ein Kreditinstitut den Geschäftsvorfall „Statusprotokoll anfordern" in der BPD nicht
anbietet. Ein FinTS-Kundenprodukt muss das Statusprotokoll zwingend unterstüt-
zen.

Dies ist beispielsweise sinnvoll, um Kunden die Ausführung ihrer Aufträge mitzutei-
len, da online im Regelfall lediglich der Empfang der Aufträge bestätigt werden kann
und die weitere Verarbeitung offline erfolgt. Ferner dient das Statusprotokoll dazu,
nach einem Verbindungsabbruch den Status der übermittelten Aufträge zu erfahren,
insbesondere wenn durch das Kundensystem eine Nachricht vollständig an das
Kreditinstitut übermittelt wurde, beim Senden der Antwort seitens des Kreditinstituts
jedoch ein Fehler auftrat.

Grundsätzlich erzeugen sämtliche als Geschäftsvorfall gekennzeichneten Segmente
von Kundennachrichten (s. Kap. I.1.3) einen Eintrag in das Statusprotokoll. Beim
anonymen Zugang (s. o.) wird kein Statusprotokoll erzeugt.

Meldungen im Statusprotokoll sind identisch mit den Rückmeldungen zu Aufträgen
in Kreditinstitutsnachrichten (s. Segment HIRMS). Daher kann ein Auftrag im Sta-
tusprotokoll durch 1 bis n Segmente beschrieben sein. Das Statusprotokoll enthält
jeweils die letzte für den Kunden bestimmte(n) Rückmeldung(en) in Bezug auf einen
Auftrag bzw. eine Rückmeldung, die den Abschluss der Bearbeitung beschreibt.
Somit ist zu jedem Zeitpunkt der Verarbeitungsstatus eines Auftrages durch genau
einen Status definiert. Ferner enthält das Statusprotokoll sämtliche Meldungen, die
in das Segment „Rückmeldungen zur Gesamtnachricht" (HIRMG) eingestellt wer-
den.

Die Festlegung, welcher Teil der Rückmeldungen im Rahmen der Online-Prüfung (z.
B. ,Auftrag entgegengenommen") und welcher Teil durch die Offline-Prüfung (z. B.
„Auftrag ausgeführt“) generiert wird, ist kreditinstitutsspezifisch.

Da Meldungen, die erst bei der Weiterverarbeitung generiert werden, identisch mit
den Online-Meldungen sind, kann das Kundenprodukt auch bei asynchroner Ver-
arbeitung wie beim Onlinebetrieb auf Meldungen des Kreditinstituts reagieren.

Statusmeldungen werden stets dem Absender des Auftrags zugeordnet, d. h. Stati
sind benutzerbezogen und nicht kontenbezogen.

Die Frage, wie detailliert der Kunde über das Fortschreiten der kreditinstitutsinternen
Verarbeitung informiert werden soll, wird institutsindividuell gehandhabt.

Stati müssen im Protokoll als Abgleichhilfe mindestens bis zum Ablauf von 2 Bu-
chungstagen nach dem nächsten Dialog, jedoch höchstens 6 Monate, vorgehalten
werden. Auf diese Weise ist sichergestellt, dass dem Kunden keine Statusmel-
dungen verloren gehen (z. B. bei längerem Urlaub etc.). Gleichzeitig wird das kredit-
institutsseitig vorzuhaltende Datenvolumen minimiert, indem die Stati bereits 2 Tage
nach dem nächsten Dialog gelöscht werden können.


![](figures/71.1)


Das Kundenprodukt sollte über ein Journal verfügen, in das sämtli-
che Statusmeldungen chronologisch eingetragen werden, um auch
zu einem späteren Zeitpunkt die Rückverfolgung von Aufträgen zu
gewährleisten.

<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: C</td>
<td>Version: 3.0-FV</td>
<td>Financial Transaction Services (FinTS) Dokument: Formals</td>
</tr>
<tr>
<td>Seite:<br>64</td>
<td>Stand: 06.10.2017</td>
<td>Kapitel: Dialogspezifikation<br>Abschnitt: Statusprotokoll</td>
</tr>
</table>


<table>
<tr>
<td>Realisierung Bank:</td>
<td>verpflichtend</td>
</tr>
<tr>
<td>Realisierung Kunde:</td>
<td>optional</td>
</tr>
</table>


## a) Kundenauftrag


### . Format


<table>
<tr>
<td>Name:</td>
<td>Statusprotokoll anfordern</td>
</tr>
<tr>
<td>Typ:</td>
<td>Segment</td>
</tr>
<tr>
<td>Segmentart:</td>
<td>Geschäftsvorfall</td>
</tr>
<tr>
<td>Kennung:</td>
<td>HKPRO</td>
</tr>
<tr>
<td>Bezugssegment:</td>
<td>-</td>
</tr>
<tr>
<td>Version:</td>
<td>4</td>
</tr>
<tr>
<td>Sender:</td>
<td>Kunde</td>
</tr>
</table>


<table>
<tr>
<th>Nr.</th>
<th>Name</th>
<th>Ver- sion</th>
<th>Typ</th>
<th>For- mat</th>
<th>Län- ge</th>
<th>Sta- tus</th>
<th>An- zahl</th>
<th>Restriktionen</th>
</tr>
<tr>
<td>1</td>
<td>Segmentkopf</td>
<td>1</td>
<td>DEG</td>
<td></td>
<td></td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>2</td>
<td>Von Datum</td>
<td>1</td>
<td>DE</td>
<td>dat</td>
<td>#</td>
<td>O</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>3</td>
<td>Bis Datum</td>
<td>1</td>
<td>DE</td>
<td>dat</td>
<td>#</td>
<td>O</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>4</td>
<td>Maximale Anzahl Einträge</td>
<td>1</td>
<td>DE</td>
<td>num</td>
<td>..4</td>
<td>O</td>
<td>1</td>
<td>&gt;0</td>
</tr>
<tr>
<td>5</td>
<td>Aufsetzpunkt</td>
<td>1</td>
<td>DE</td>
<td>an</td>
<td>..35</td>
<td>C</td>
<td>1</td>
<td>M: vom Kreditinstitut wurde ein Aufsetzpunkt rückge- meldet (s. Kap. B.6.3). N: sonst</td>
</tr>
</table>


## . Belegungsrichtlinien


### Von Datum, Bis Datum

Werden beide Felder nicht belegt, werden automatisch alle aktuellen Stati (d.
h. die neuen Stati und zusätzlich die Stati, die aufgrund der 2-Tage-Regel
noch nicht gelöscht wurden) zurückgemeldet.


![](figures/72.1)


Das Kundenprodukt muss damit rechnen, dass aufgrund der
2-Tage-Regel derselbe Status u.U. mehrfach vom Kreditinsti-
tut gesendet wird.


# b) Kreditinstitutsrückmeldung


## . Beschreibung

Für jeden Auftrag, für den ein Statusprotokoll verfügbar ist, ist ein Segment bzw.
mehrere Segmente mit nachfolgendem Format in die Antwortnachricht einzustellen.


## . Format


<table>
<tr>
<td>Name:</td>
<td>Statusprotokoll rückmelden</td>
</tr>
<tr>
<td>Typ:</td>
<td>Segment</td>
</tr>
<tr>
<td>Segmentart:</td>
<td>Geschäftsvorfall</td>
</tr>
<tr>
<td>Kennung:</td>
<td>HIPRO</td>
</tr>
<tr>
<td>Bezugssegment:</td>
<td>HKPRO</td>
</tr>
<tr>
<td>Version:</td>
<td>4</td>
</tr>
<tr>
<td>Sender:</td>
<td>Kreditinstitut</td>
</tr>
</table>


<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th rowspan="2">Version: 3.0-FV</th>
<th rowspan="2">Kapitel: C</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Formals</td>
</tr>
<tr>
<td>Kapitel: Abschnitt:</td>
<td>Dialogspezifikation Statusprotokoll</td>
<td>Stand: 06.10.2017</td>
<td>Seite: 65</td>
</tr>
</table>


<table>
<tr>
<th>Nr.</th>
<th>Name</th>
<th>Ver- sion</th>
<th>Typ</th>
<th>For- mat</th>
<th>Län- ge</th>
<th>Sta- tus</th>
<th>An- zahl</th>
<th>Restriktionen</th>
</tr>
<tr>
<td>1</td>
<td>Segmentkopf</td>
<td>1</td>
<td>DEG</td>
<td></td>
<td></td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>2</td>
<td>Bezugsnachricht</td>
<td>1</td>
<td>DEG</td>
<td></td>
<td></td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>3</td>
<td>Bezugssegment</td>
<td>1</td>
<td>DE</td>
<td>num</td>
<td>..3</td>
<td>C</td>
<td>1</td>
<td>&gt;=1<br>M: Statusmeldung bezieht sich auf einen Auftrag N: Statusmeldung bezieht sich auf die Gesamtnach- richt</td>
</tr>
<tr>
<td>4</td>
<td>Datum</td>
<td>1</td>
<td>DE</td>
<td>dat</td>
<td>#</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>5</td>
<td>Uhrzeit</td>
<td>1</td>
<td>DE</td>
<td>tim</td>
<td>#</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>6</td>
<td>Rückmeldung</td>
<td>1</td>
<td>DEG</td>
<td></td>
<td></td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
</table>


## . Belegungsrichtlinien


### Bezugsnachricht

Einzustellen ist die Referenz auf die Kundennachricht, auf die sich die Sta-
tusmeldung bezieht.


## c) Bankparameterdaten


### . Beschreibung

Geschäftsvorfallspezifische Parameter existieren nicht.


### . Format


<table>
<tr>
<td>Name:</td>
<td>Statusprotokoll Parameter</td>
</tr>
<tr>
<td>Typ:</td>
<td>Segment</td>
</tr>
<tr>
<td>Segmentart:</td>
<td>Geschäftsvorfall</td>
</tr>
<tr>
<td>Kennung:</td>
<td>HIPROS</td>
</tr>
<tr>
<td>Bezugssegment:</td>
<td>HKVVB</td>
</tr>
<tr>
<td>Version:</td>
<td>4</td>
</tr>
<tr>
<td>Sender:</td>
<td>Kreditinstitut</td>
</tr>
</table>


<table>
<tr>
<th>Nr.</th>
<th>Name</th>
<th>Ver- sion</th>
<th>Typ</th>
<th>For- mat</th>
<th>Län- ge</th>
<th>Sta- tus</th>
<th>An- zahl</th>
<th>Restriktionen</th>
</tr>
<tr>
<td>1</td>
<td>Segmentkopf</td>
<td>1</td>
<td>DEG</td>
<td></td>
<td></td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>2</td>
<td>Maximale Anzahl Aufträge</td>
<td>1</td>
<td>DE</td>
<td>num</td>
<td>..3</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>3</td>
<td>Anzahl Signaturen mindestens</td>
<td>1</td>
<td>DE</td>
<td>num</td>
<td>1</td>
<td>M</td>
<td>1</td>
<td>0, 1, 2, 3</td>
</tr>
<tr>
<td>4</td>
<td>Sicherheitsklasse</td>
<td>1</td>
<td>DE</td>
<td>code</td>
<td>1</td>
<td>M</td>
<td>1</td>
<td>0, 1, 2, 3, 4</td>
</tr>
</table>


<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: C</td>
<td>Version: 3.0-FV</td>
<td>Financial Transaction Services (FinTS) Dokument: Formals</td>
</tr>
<tr>
<td>Seite:<br>66</td>
<td>Stand: 06.10.2017</td>
<td>Kapitel: Dialogspezifikation<br>Abschnitt: Synchronisierung</td>
</tr>
</table>


# C.8 Synchronisierung

Eine Synchronisierung ist erforderlich, wenn

· für das vom Kunden verwendete Endgerät noch keine Kundensystem-ID verge-
ben wurde. Dies ist nur bei Verwendung des HBCI RAH- / RDH- und PIN/TAN-
Verfahrens erforderlich, da bei symmetrischen Signatur- und Verschlüs-
selungsverfahren kreditinstitutsseitig keine Verwaltung respektive Generierung
einer Kundensystem-ID erfolgt. Bei der Verwendung von RAH-/RDH-Chipkarten
ab Sicherheitsprofil-Version 3 wird anstatt der Kundensystem-ID die CID der ge-
steckten Karte verwendet. Im Rahmen der Dialoginitialisierungs-Antwortnachricht
erhält das entsprechende Kundensystem eine neue Kundensystem-ID mitgeteilt.


![](figures/74.1)


Bevor ein Benutzer bei Verwendung des HBCI RAH- / RDH- bzw.
des PIN/TAN-Verfahrens von einem neuen Kundensystem Auf-
träge erteilen kann, hat er im Wege einer Synchronisierung eine
Kundensystem-ID für dieses System anzufordern (Ausnahme:
bei Verwendung einer RAH-/RDH-Chipkarte ab Sicherheitsprofil-
Version 3). Diese ID ist im Folgenden stets anzugeben, wenn der
Benutzer von diesem Kundensystem aus Nachrichten sendet.
Wenn eine Synchronisierung der Kundensystem-ID durchgeführt
wird, ist das DE ,Kundensystem-ID" mit dem Wert '0' zu belegen.
Das DE "Identifizierung der Partei" im Signaturkopf in der DEG
"Sicherheitsidentifikation, Details" ist mit dem Wert ,0' zu bele-
gen.

Kundensystem-IDs, die länger als 6 Monate nicht beim Kredit-
institut eingereicht wurden, können im Kreditinstitut gelöscht
werden. Meldet sich der Kunde mit dieser Kundensystem-ID er-
neut an, wird keine Legitimierung zum Senden von Auftragsnach-
richten erteilt. Der Kunde hat in diesem Fall eine erneute Syn-
chronisierung durchzuführen.

Da jedes Kreditinstitut die Kundensystem-ID unabhängig von an-
deren Kreditinstituten vergibt, muss das Kundenprodukt in der
Lage sein, für jeden Kreditinstitutszugang eine eigene Kunden-
system-ID zu verwalten.

. aufgrund eines Verbindungsabbruchs nicht ersichtlich ist, welche Nachrichten
vom Kreditinstitut bereits entgegengenommen wurden. In diesem Fall wird dem
Kunden in der Antwort die Nummer der im vorangegangenen Dialog vom Kredit-
institut zuletzt verarbeiteten Nachricht zurückgemeldet (s. auch Kap. C.6 ,,Verbin-
dungsabbruch"). Eine Synchronisierung der Nachrichtennummer ist daher nur für
den letzten Auftragsdialog des sendenden Benutzers möglich. Eine abge-
brochene Synchronisierungsnachricht überschreibt die letzte Nachrichtennummer
nicht.


![](figures/74.2)


Das Kundensystem sollte die Synchronisierung von Nachrichten
nicht automatisieren, da bei längeren Ausfallzeiten betroffene
Aufträge evtl. bereits auf anderem Wege beim Kreditinstitut ein-
gereicht wurden.

<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th rowspan="2">Version: 3.0-FV</th>
<th rowspan="2">Kapitel: C</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Formals</td>
</tr>
<tr>
<td>Kapitel: Abschnitt:</td>
<td>Dialogspezifikation Synchronisierung</td>
<td>Stand: 06.10.2017</td>
<td>Seite: 67</td>
</tr>
</table>


. bei Verwendung des HBCI RAH- oder RDH-Verfahrens die Signatur-ID abhand-
engekommen ist (z. B. durch Festplattendefekt). Da bei fehlender Signatur-ID
keine ordnungsgemäße Signatur erzeugt werden kann, ist in diesem Fall als Sig-
natur-ID der reservierte Wert '9999999999999999' zu verwenden.4 In der Ant-
wortnachricht wird die bisher höchste vom Benutzer bei diesem Kreditinstitut ein-
gereichte Signatur-ID zurückgemeldet.5 Bei symmetrischen HBCI Signatur-
Verfahren und TAN-Verfahren unter Verwendung von HKTAN > Segmentversion
#4 ist diese Option nicht zulässig.


![](figures/75.1)


Da die Signatur-ID multibankfähig ist, muss im Fall des Verlusts
der Signatur-ID bei jedem Kreditinstitut, bei dem der Benutzer
Signaturen eingereicht hat, eine Synchronisierung vorgenommen
werden. Für zukünftige Signaturen ist dann der höchste aller zu-
rückgemeldeten Werte inkrementiert um 1 zu verwenden.

Bestehende Aufträge, die noch nicht abgeschickt wurden, sind
nach der Synchronisierung der Signatur-ID neu zu signieren, da
ansonsten neu erfasste Aufträge aufgrund einer Doppeleinrei-
chung abgelehnt würden.


![](figures/75.2)


Bei einer Synchronisierung der Kundensystem-ID oder der Signa-
tur-ID sollte für die Synchronisierungsnachricht keine Doppelein-
reichungskontrolle durchgeführt werden soll.

Falls eine Synchronisierungsnachricht gesendet wird, dürfen anschließend keine
Auftragsnachrichten gesendet werden. Hierzu hat das Kundensystem nach dem Er-
halt der Antwortnachricht den Dialog durch Senden einer Dialogendenachricht zu
beenden. Um Auftragsnachrichten zu schicken, muss das Kundenprodukt anschlie-
Bend eine neue Dialoginitialisierung für diesen Benutzer senden.


## C.8.1 Kundennachricht


### C.8.1.1 Nachrichtenformat

. Format


<table>
<tr>
<td>Name:</td>
<td>Synchronisierungsnachricht</td>
</tr>
<tr>
<td>Typ:</td>
<td>Nachricht</td>
</tr>
<tr>
<td>Version:</td>
<td>4</td>
</tr>
<tr>
<td>Sender:</td>
<td>Kunde</td>
</tr>
</table>


<!-- PageFooter: 4 Der angegebene Wert darf nur für diese spezielle Nachricht verwendet werden. Der aktuelle Wert der Signatur-ID bleibt von dieser Belegung unberührt. -->
<!-- PageFooter: 5 Es ist zu beachten, dass das Kreditinstitut nicht unbedingt die letzte, sondern immer die höchste eingereichte Signatur-ID zurückmeldet. Dies ist notwendig, weil die Aufträge nicht zwingend mit aufsteigender Signatur-ID beim Kreditinstitut eingereicht werden müssen und daher die Verwen- dung der aktuellen Signatur-ID u.U. zu einer Doppeleinreichung führen könnte. -->
<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: C</td>
<td>Version: 3.0-FV</td>
<td>Financial Transaction Services (FinTS) Dokument: Formals</td>
</tr>
<tr>
<td>Seite: 68</td>
<td>Stand: 06.10.2017</td>
<td>Kapitel: Dialogspezifikation<br>Abschnitt: Synchronisierung</td>
</tr>
</table>


<table>
<tr>
<th>Nr.</th>
<th>Name</th>
<th>Ver- sion</th>
<th>Typ</th>
<th>Ken- nung</th>
<th>Sta- tus</th>
<th>An- zahl</th>
<th>Anmerkungen</th>
</tr>
<tr>
<td>1</td>
<td>Nachrichtenkopf</td>
<td>3</td>
<td>SEG</td>
<td>HNHBK</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>2</td>
<td>Signaturkopf</td>
<td>4</td>
<td>SEG</td>
<td>HNSHK</td>
<td>M</td>
<td>1</td>
<td>s. [HBCI], Kap. B.5.1</td>
</tr>
<tr>
<td>3</td>
<td>Identifikation</td>
<td>2</td>
<td>SEG</td>
<td>HKIDN</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>4</td>
<td>Verarbeitungsvor- bereitung</td>
<td>3</td>
<td>SEG</td>
<td>HKVVB</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>5</td>
<td>Zwei-Schritt-TAN- Einreichung</td>
<td>≥6</td>
<td>SEG</td>
<td>HKTAN</td>
<td>O</td>
<td>1</td>
<td>s. [PINTAN], Kap. B.3.3</td>
</tr>
<tr>
<td>6</td>
<td>Anforderung eines öffentlichen Schlüs- sels</td>
<td>3</td>
<td>SEG</td>
<td>HKISA</td>
<td>C</td>
<td>3</td>
<td>O: bei HBCI RAH und RDH N: bei HBCI DDV oder TAN-Verfahren</td>
</tr>
<tr>
<td>7</td>
<td>Synchronisierung</td>
<td>3</td>
<td>SEG</td>
<td>HKSYN</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>8</td>
<td>Signaturabschluss</td>
<td>2</td>
<td>SEG</td>
<td>HNSHA</td>
<td>M</td>
<td>1</td>
<td>s. [HBCI], Kap. B.5.2</td>
</tr>
<tr>
<td>9</td>
<td>Nachrichtenab- schluss</td>
<td>1</td>
<td>SEG</td>
<td>HNHBS</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
</table>


### C.8.1.2 Segment: Synchronisierung


<table>
<tr>
<td colspan="2">. Format</td>
</tr>
<tr>
<td>Name:</td>
<td>Synchronisierung</td>
</tr>
<tr>
<td>Typ:</td>
<td>Segment</td>
</tr>
<tr>
<td>Segmentart:</td>
<td>Administration</td>
</tr>
<tr>
<td>Kennung:</td>
<td>HKSYN</td>
</tr>
<tr>
<td>Bezugssegment:</td>
<td>-</td>
</tr>
<tr>
<td>Version:</td>
<td>3</td>
</tr>
<tr>
<td>Sender:</td>
<td>Kunde</td>
</tr>
</table>


<table>
<tr>
<th>Nr.</th>
<th>Name</th>
<th>Ver- sion</th>
<th>Typ</th>
<th>For- mat</th>
<th>Län- ge</th>
<th>Sta- tus</th>
<th>An- zahl</th>
<th>Restriktionen</th>
</tr>
<tr>
<td>1</td>
<td>Segmentkopf</td>
<td>1</td>
<td>DEG</td>
<td></td>
<td></td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>2</td>
<td>Synchronisierungs- modus</td>
<td>2</td>
<td>DE</td>
<td>code</td>
<td>1</td>
<td>M</td>
<td>1</td>
<td>0, 1, 2</td>
</tr>
</table>


#### ◆ Ausgewählte Beispiele für Rückmeldungscodes


<table>
<tr>
<td>Code</td>
<td>Beispiel für Rückmeldungstext</td>
</tr>
<tr>
<td>0020</td>
<td>Auftrag ausgeführt</td>
</tr>
<tr>
<td>9210</td>
<td>Kundensystem-ID wird vom Kreditinstitut nicht unterstützt</td>
</tr>
<tr>
<td>9210</td>
<td>Synchronisierung der Signatur-ID ist nicht zulässig</td>
</tr>
</table>


<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th rowspan="2">Version: 3.0-FV</th>
<th rowspan="2">Kapitel: C</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Formals</td>
</tr>
<tr>
<td>Kapitel:<br>Abschnitt:</td>
<td>Dialogspezifikation Synchronisierung</td>
<td>Stand: 06.10.2017</td>
<td>Seite: 69</td>
</tr>
</table>


## C.8.2 Kreditinstitutsnachricht


### C.8.2.1 Nachrichtenformat


#### . Beschreibung

Das Kreditinstitut meldet dem Kundensystem je nach Kundenanforderung entweder
die neu zugeteilte Kundensystem-ID, die zuletzt erhaltene Nachrichtennummer des
vorangegangenen Dialoges oder die aktuelle Signatur-ID (Sicherheitsreferenznum-
mer) zurück.


#### . Format


<table>
<tr>
<td>Name:</td>
<td>Synchronisierungsantwortnachricht</td>
</tr>
<tr>
<td>Typ:</td>
<td>Nachricht</td>
</tr>
<tr>
<td>Version:</td>
<td>4</td>
</tr>
<tr>
<td>Sender:</td>
<td>Kreditinstitut</td>
</tr>
</table>


<table>
<tr>
<th>Nr.</th>
<th>Name</th>
<th>Ver- sion</th>
<th>Typ</th>
<th>Ken- nung</th>
<th>Sta- tus</th>
<th>An- zahl</th>
<th>Anmerkungen</th>
</tr>
<tr>
<td>1</td>
<td>Nachrichtenkopf</td>
<td>3</td>
<td>SEG</td>
<td>HNHBK</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>2</td>
<td>Signaturkopf</td>
<td>4</td>
<td>SEG</td>
<td>HNSHK</td>
<td>O</td>
<td>1</td>
<td>s. [HBCI], Kap. B.5.2</td>
</tr>
<tr>
<td>3</td>
<td>Rückmeldungen zur Gesamtnachricht</td>
<td>2</td>
<td>SEG</td>
<td>HIRMG</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>4</td>
<td>Rückmeldungen zu Segmenten</td>
<td>2</td>
<td>SEG</td>
<td>HIRMS</td>
<td>O</td>
<td>n</td>
<td></td>
</tr>
<tr>
<td>5</td>
<td>Bankparameterda- ten</td>
<td>3</td>
<td>SF</td>
<td>#</td>
<td>O</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>6</td>
<td>Userparameterda- ten</td>
<td>3</td>
<td>SF</td>
<td>#</td>
<td>O</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>7</td>
<td>Übermittlung eines öffentlichen Schlüs- sels</td>
<td>3</td>
<td>SEG</td>
<td>HIISA</td>
<td>C</td>
<td>3</td>
<td>O: bei HBCI RAH und RDH N: bei HBCI DDV- oder TAN-Verfahren</td>
</tr>
<tr>
<td>8</td>
<td>Synchronisierungs- antwort</td>
<td>4</td>
<td>SEG</td>
<td>HISYN</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>9</td>
<td>Kreditinstitutsmel- dung</td>
<td>2</td>
<td>SEG</td>
<td>HIKIM</td>
<td>O</td>
<td>n</td>
<td></td>
</tr>
<tr>
<td>10</td>
<td>Signaturabschluss</td>
<td>2</td>
<td>SEG</td>
<td>HNSHA</td>
<td>O</td>
<td>1</td>
<td>s. [HBCI], Kap. B.5.3</td>
</tr>
<tr>
<td>11</td>
<td>Nachrichtenab- schluss</td>
<td>1</td>
<td>SEG</td>
<td>HNHBS</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
</table>


### C.8.2.2 Segment: Synchronisierungsantwort


#### . Format


<table>
<tr>
<td>Name:</td>
<td>Synchronisierungsantwort</td>
</tr>
<tr>
<td>Typ:</td>
<td>Segment</td>
</tr>
<tr>
<td>Segmentart:</td>
<td>Administration</td>
</tr>
<tr>
<td>Kennung:</td>
<td>HISYN</td>
</tr>
<tr>
<td>Bezugssegment:</td>
<td>HKSYN</td>
</tr>
<tr>
<td>Version:</td>
<td>4</td>
</tr>
<tr>
<td>Sender:</td>
<td>Kreditinstitut</td>
</tr>
</table>


<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: C</td>
<td>Version: 3.0-FV</td>
<td>Financial Transaction Services (FinTS) Dokument: Formals</td>
</tr>
<tr>
<td>Seite: 70</td>
<td>Stand: 06.10.2017</td>
<td>Kapitel: Dialogspezifikation<br>Abschnitt: Synchronisierung</td>
</tr>
</table>


<table>
<tr>
<th>Nr.</th>
<th>Name</th>
<th>Ver- sion</th>
<th>Typ</th>
<th>For- mat</th>
<th>Län- ge</th>
<th>Sta- tus</th>
<th>An- zahl</th>
<th>Restriktionen</th>
</tr>
<tr>
<td>1</td>
<td>Segmentkopf</td>
<td>1</td>
<td>DEG</td>
<td></td>
<td></td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>2</td>
<td>Kundensystem-ID</td>
<td>1</td>
<td>DE</td>
<td>id</td>
<td>#</td>
<td>C</td>
<td>1</td>
<td>M: Synchronisierungsmo- dus = 0 N: sonst</td>
</tr>
<tr>
<td>3</td>
<td>Nachrichtennum- mer</td>
<td>1</td>
<td>DE</td>
<td>num</td>
<td>..4</td>
<td>C</td>
<td>1</td>
<td>&gt;0<br>M: Synchronisierungsmo- dus = 1 N: sonst</td>
</tr>
<tr>
<td>4</td>
<td>Sicherheitsrefe- renznummer für Signierschlüssel</td>
<td>1</td>
<td>DE</td>
<td>num</td>
<td>.. 16</td>
<td>C</td>
<td>1</td>
<td>M: Synchronisierungsmo- dus = 2 N: sonst</td>
</tr>
<tr>
<td>5</td>
<td>Sicherheitsrefe- renznummer für Di- gitale Signatur</td>
<td>1</td>
<td>DE</td>
<td>num</td>
<td>.. 16</td>
<td>C</td>
<td>1</td>
<td>M: Synchronisierungsmo- dus = 2 und Sicherheits- profil = RAH-7,RDH-3, RDH-6 oder RDH-7 N: sonst</td>
</tr>
</table>


# . Belegungsrichtlinien


## Sicherheitsreferenznummer für Digitale Signatur

Es ist die Signatur-ID des Schlüssels für Digitale Signaturen (Schlüsselart
,,D") anzugeben.

<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th rowspan="2">Version: 3.0-FV</th>
<th rowspan="2">Kapitel: C</th>
</tr>
<tr>
<th>Dokument:</th>
<th>Formals</th>
</tr>
<tr>
<td>Kapitel:<br>Abschnitt:</td>
<td>Dialogspezifikation Life-Indikator-Nachricht</td>
<td>Stand: 06.10.2017</td>
<td>Seite: 71</td>
</tr>
</table>


## C.9 Life-Indikator-Nachricht

Falls in einem laufenden Dialog über einen längeren Zeitraum keine weiteren Kun-
dennachrichten mehr geschickt werden, ist es für ein Kreditinstitutssystem nicht er-
sichtlich, ob der Kunde noch weitere Nachrichten senden wird oder den Dialog be-
reits abgebrochen hat.

Insbesondere für Kundenprodukte, die im Online-Modus arbeiten (d. h. der Dialog
wird nach dem Senden der Aufträge nicht automatisch beendet), steht daher mit der
Life-Indikator-Nachricht eine Möglichkeit zur Verfügung, dem Kreditinstitutssystem
anzuzeigen, dass der Kundendialog aufrecht erhalten werden soll und somit eine
Dialogbeendigung aufgrund eines Timeouts durch das Kreditinstitutssystem vermie-
den wird.

Das Kreditinstitut in den Bankparameterdaten einen minimalen und einen maxima-
len Timeout-Wert mitteilen, der dem Kundensystem eine Information darüber gibt,
nach welchem Zeitraum eine Life-Indikator-Nachricht frühestens gesendet werden
darf bzw. nach welchem Zeitraum das Kreditinstitut den Dialog voraussichtlich be-
enden wird


Abbildung 13: Funktionsweise des Life-Indikators

![Letzte Nachricht KeepAlive- Nachricht t t0 tmin tmax Dialogendenachricht, Auftragsnachricht oder weiter KeepAlive- Nachricht t t0 tmin tmax](figures/79.1)


Das Senden einer Life-Indikator-Nachricht führt jedoch nicht zwingend zur Aufrecht-
erhaltung eines Dialoges. Unabhängig von gesendeten Life-Indikator-Nachrichten
und dem Timeout-Wert in den Bankparameterdaten hat das Kreditinstitut jederzeit
die Möglichkeit den Dialog abzubrechen.

Die Life-Indikator-Nachricht ist sowohl für Kunde als auch für Kreditinstitut optional.
Das Kreditinstitut teilt durch Angabe des Timeout-Wertes in den BPD dem Kunden-
system mit, dass es die Life-Indikator-Nachricht unterstützt. Sind beide Werte dage-
gen nicht angegeben, so muss das Kundenprodukt davon ausgehen, dass das Kre-
ditinstitut die Life-Indikator-Nachricht nicht unterstützt.

<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: C</td>
<td>Version: 3.0-FV</td>
<td>Financial Transaction Services (FinTS) Dokument: Formals</td>
</tr>
<tr>
<td>Seite:<br>72</td>
<td>Stand: 06.10.2017</td>
<td>Kapitel: Dialogspezifikation<br>Abschnitt: Life-Indikator-Nachricht</td>
</tr>
</table>


Das Life-Indikator-Segment darf nur in der speziell hierfür vorgesehenen Nachricht
gesendet werden. Diese Nachricht darf nicht auBerhalb der Dialogschrittfolge ge-
sendet werden, d. h. nicht, wenn noch die Beantwortung eines Auftrags durch das
Kreditinstitut aussteht. Obwohl die Nachricht bei personalisierten Dialogen innerhalb
eines signierten und verschlüsselten Dialoges gesendet wird, ist sie unsigniert und
unverschlüsselt.

Das Senden einer Life-Indikator-Nachricht hat keine Auswirkungen auf die aktuelle
Nachrichtennummer. Der Inhalt des Feldes ,,Nachrichtennummer“ ist beliebig befüll-
bar und wird vom Kreditinstitut ignoriert. Auch wird die Nummer einer Life-Indikator-
Nachricht nie bei einer Synchronisierung der Nachrichtennummer zurückgeliefert.

Das Segment enthält mit Ausnahme des Segmentkopfes keine Datenelemente.


<table>
<tr>
<td>Realisierung Bank:</td>
<td>optional</td>
</tr>
<tr>
<td>Realisierung Kunde:</td>
<td>optional</td>
</tr>
</table>


### . Format


<table>
<tr>
<td>Name:</td>
<td>Life-Indikator</td>
</tr>
<tr>
<td>Typ:</td>
<td>Segment</td>
</tr>
<tr>
<td>Segmentart:</td>
<td>Administration</td>
</tr>
<tr>
<td>Kennung:</td>
<td>HKLIF</td>
</tr>
<tr>
<td>Bezugssegment:</td>
<td>-</td>
</tr>
<tr>
<td>Version:</td>
<td>1</td>
</tr>
<tr>
<td>Sender:</td>
<td>Kunde</td>
</tr>
</table>


<table>
<tr>
<th>Nr.</th>
<th>Name</th>
<th>Ver- sion</th>
<th>Typ</th>
<th>For- mat</th>
<th>Län- ge</th>
<th>Sta- tus</th>
<th>An- zahl</th>
<th>Restriktionen</th>
</tr>
<tr>
<td>1</td>
<td>Segmentkopf</td>
<td>1</td>
<td>DEG</td>
<td></td>
<td></td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
</table>


### a) Kundennachricht


#### . Format


<table>
<tr>
<td>Name:</td>
<td>Life-Indikator-Nachricht</td>
</tr>
<tr>
<td>Kennung:</td>
<td>N21</td>
</tr>
<tr>
<td>Typ:</td>
<td>Nachricht</td>
</tr>
<tr>
<td>Version:</td>
<td>1</td>
</tr>
<tr>
<td>Sender:</td>
<td>Kunde</td>
</tr>
</table>


<table>
<tr>
<th>Nr.</th>
<th>Name</th>
<th>Ver- sion</th>
<th>Typ</th>
<th>Ken- nung</th>
<th>Sta- tus</th>
<th>An- zahl</th>
<th>Anmerkungen</th>
</tr>
<tr>
<td>1</td>
<td>Nachrichtenkopf</td>
<td>3</td>
<td>SEG</td>
<td>HNHBK</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>2</td>
<td>Life-Indikator</td>
<td>1</td>
<td>SEG</td>
<td>HKLIF</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>3</td>
<td>Nachrichtenab- schluss</td>
<td>1</td>
<td>SEG</td>
<td>HNHBS</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
</table>


#### . Belegungsrichtlinien


#### Nachrichtenkopf

Es muss die Dialog-ID des zugrunde liegenden Dialoges angegeben werden.


#### b) Kreditinstitutsnachricht


#### . Beschreibung

Das Kreditinstitut antwortet auf die Life-Indikator-Nachricht mit einer allgemeinen
Kreditinstitutsnachricht und informiert mit dem Rückmeldungscode das Kundensys-

<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th rowspan="2">Version: 3.0-FV</th>
<th rowspan="2">Kapitel: C</th>
</tr>
<tr>
<th>Dokument:</th>
<th>Formals</th>
</tr>
<tr>
<td>Kapitel:<br>Abschnitt:</td>
<td>Dialogspezifikation<br>Life-Indikator-Nachricht</td>
<td>Stand: 06.10.2017</td>
<td>Seite: 73</td>
</tr>
</table>


tem, ob es dem Wunsch nach Aufrechterhaltung des Dialoges entspricht oder die-
sen ablehnt. Wie auch die Kundennachricht ist die Antwortnachricht nicht signiert
und nicht verschlüsselt.


### . Format


<table>
<tr>
<td>Typ:</td>
<td>Nachricht</td>
</tr>
<tr>
<td>Name:</td>
<td>Kreditinstitutsnachricht allgemein</td>
</tr>
<tr>
<td>Typ:</td>
<td>Nachricht</td>
</tr>
<tr>
<td>Format:</td>
<td>s. Kap. B.7.1</td>
</tr>
</table>


### ◆ Ausgewählte Beispiele für Rückmeldungscodes


<table>
<tr>
<td>Code</td>
<td>Beispiel für Rückmeldungstext</td>
</tr>
<tr>
<td>0020</td>
<td>Dialog wird fortgeführt</td>
</tr>
<tr>
<td>9800</td>
<td>Dialog wird nicht fortgeführt</td>
</tr>
</table>


<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: C</td>
<td>Version: 3.0-FV</td>
<td>Financial Transaction Services (FinTS) Dokument: Formals</td>
</tr>
<tr>
<td>Seite:<br>74</td>
<td>Stand: 06.10.2017</td>
<td>Kapitel: Dialogspezifikation<br>Abschnitt: Unterstützung von Geschäftsvorfallversionen</td>
</tr>
</table>


# C.10 Unterstützung von Geschäftsvorfallversionen

Die Geschäftsvorfallversion (Segmentversion) ist unabhängig von der FinTS-
Version, d. h. grundsätzlich können alternativ oder zusätzlich zu den in [Messages]
beschriebenen Geschäftsvorfallversionen in allen FinTS-Versionen beliebige andere
existierende Versionen eines Geschäftsvorfalls unterstützt werden. Einzige Bedin-
gung ist, dass der Geschäftsvorfall einer älteren Version auch aus Anwendungsge-
sichtspunkten noch zulässig ist. So sind folgende Segmentversionen von dieser Re-
gelung ausgenommen:

. Segmentversionen aus FinTS-Versionen vor Version 2.0.1

· Segmentversionen von Geschäftsvorfällen, die aufgrund geänderter rechtli-
cher Rahmenbedingungen nicht mehr gültig sind, z. B. Geschäftsvorfälle des
ehemaligen Inlands-Zahlungsverkehrs.

. Segmentversionen von Geschäftsvorfällen, die Fremdformate enthalten, die
nicht mehr unterstützt werden (z. B. aufgrund fehlender Euro-Fähigkeit)

Die konkret zulässigen Segmentversionen sind der Tabelle in Anhang von [Messa-
ges] zu entnehmen. In den Spalten sind zum einen je Geschäftsvorfall die in den
bisher veröffentlichten FinTS-Versionen definierten Segmentversionen angegeben.
In der Spalte ,gültig“ sind diejenigen Segmentversionen des Geschäftsvorfalls an-
gegeben, die in allen der angegeben FinTS-Versionen grundsätzlich zulässig sind.
Sofern neue FinTS-Versionen veröffentlicht werden, wird diese Tabelle entspre-
chend erweitert.


## Beispiele:

Eine FinTS-Implementierung auf Basis FinTS 3.0 kann den Geschäftsvorfall AOM in
den Versionen 1 oder 2 anbieten, obwohl dieser Geschäftsvorfall in der Spezifikati-
on dieser FinTS-Version unbekannt ist.

In den Bankparameterdaten sind immer alle bankseitig unterstützten Segmentversi-
onen eines Geschäftsvorfalls anzugeben (d. h. das Parametersegment ist für jede
unterstützte Segmentversion einzeln einzustellen, s. Kap. D.6), also auch derjenigen
Segmentversionen, die nicht mehr zum Umfang der aktuellen FinTS-Version gehö-
ren. Die Angabe einer Segmentversion in den BPD setzt die Unterstützung der
Segmentversion sowohl durch die FinTS-Implementierung als auch durch die jewei-
lige fachliche Anwendung voraus. Die bankseitig unterstützten Segmentversionen
sind unabhängig von der FinTS-Version stets eine Teilmenge (oder die Gesamtheit)
der in der Spalte ,,gültig“ angegebenen Segmentversionen.

Aufgrund der genannten Änderungen kann ein Kundensystem nicht davon ausge-
hen, dass die zur jeweils ausgehandelten FinTS-Version gehörigen Segmentversio-
nen bankseitig auch unterstützt werden. Kundenprodukte sollten daher nach Mög-
lichkeit mehrere Versionen eines Geschäftsvorfalls unterstützen, um die Gefahr zu
minimieren, dass eine Kommunikation aufgrund unterschiedlicher Versionsunter-
stützung nicht zustande kommt. Sofern von beiden Seiten mehrere gemeinsame
Versionen unterstützt werden, so sollte die Kommunikation auf Basis der höchsten
gemeinsamen Version erfolgen.


## Beispiel:

Ein Kundensystem unterstützt die Versionen 4, 5 und 6 eines Geschäftsvorfalls. An-
hand der Bankparameterdaten erfährt das Kundensystem, dass bankseitig die Ver-

<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th>Version:</th>
<th rowspan="2">Kapitel: C</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Formals</td>
<td>3.0-FV</td>
</tr>
<tr>
<td>Kapitel:</td>
<td>Dialogspezifikation</td>
<td>Stand:</td>
<td>Seite:</td>
</tr>
<tr>
<td>Abschnitt:</td>
<td>Unterstützung von Geschäftsvorfallversionen</td>
<td>06.10.2017</td>
<td>75</td>
</tr>
</table>


sionen 3, 4 und 5 des Geschäftsvorfalls verarbeitet werden können. Daher sollte
das Kundensystem den Auftrag gemäß Segmentversion 5 senden.

Diese Vereinbarungen gelten ausdrücklich nur für Geschäftsvorfallsegmente und
nicht für administrative Segmente. Es handelt sich lediglich um verbale Klarstellun-
gen, die keine Änderungen an bestehenden FinTS-Formaten und Abläufen bedin-
gen. Die Unterstützung dieser Funktionalität durch FinTS-Implementierungen ist
nicht verpflichtend.

<!-- PageBreak -->

<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th rowspan="2">Version: 3.0-FV</th>
<th rowspan="2">Kapitel: D</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Formals</td>
</tr>
<tr>
<td>Kapitel:<br>Abschnitt:</td>
<td>Bankparameterdaten (BPD) Allgemeines</td>
<td>Stand: 06.10.2017</td>
<td>Seite: 77</td>
</tr>
</table>


# D. BANKPARAMETERDATEN (BPD)


## D.1 Allgemeines


### . Beschreibung

Die Bankparameterdaten dienen zum einen der automatisierten kreditinstitutsspezi-
fischen Konfiguration von Kundensystemen und zum anderen der dynamischen An-
passung an institutsseitige Vorgaben hinsichtlich der Auftragsgenerierung.

Des Weiteren ist es mit Hilfe der BPD möglich, bestimmte Fehler bereits auf der
Kundenseite zu erkennen, was sich wiederum positiv auf die institutsseitige Verar-
beitung der Auftragsdaten auswirkt.


#### Beispiel:

Zur Einreichung einer terminierten SEPA-Überweisung bei einem Kreditinstitut ent-
halten die BPD-Parameter die minimale und maximale Vorlaufzeit für das ge-
wünschte Datum der Ausführung.

Bei korrekter Nutzung durch das Kundensystem verhindert dieser Mechanismus
somit, dass Informationen an die Kreditinstitute gesendet werden, die diese nicht
darstellen bzw. verarbeiten können.


![](figures/85.1)


Da auf Schnittstellenebene nicht gewährleistet werden kann, dass
das Kundenprodukt die Bankparameterdaten korrekt auswertet, hat
auf jeden Fall eine entsprechende kreditinstitutsseitige Prüfung
stattzufinden.

Bei kreditinstitutsseitigen Änderungen werden die aktualisierten Bankparameterda-
ten dem Kunden beim nächsten Dialog automatisch im Rahmen der Dialoginitiali-
sierung übermittelt. Die neuen BPD werden sofort, d. h. schon für den laufenden Di-
alog, aktiv.


![](figures/85.2)


Intelligente Kundenprodukte können in diesem Fall im laufenden Di-
alog die Einhaltung der BPD prüfen und die Auftragsnachrichten wie
geplant senden, falls die BPD-Änderungen keine Auswirkung auf
die zur Versendung anstehenden Aufträge haben. Steht diese Intel-
ligenz nicht zur Verfügung, so muss nach Erhalt der neuen BPD der
laufende Dialog vom Kunden (Kundenprodukt) beendet, die Aufträ-
ge geprüft bzw. neu erfasst und dann ein neuer Dialog begonnen
werden.

In Abgrenzung zu den UPD enthalten die BPD ausschließlich Daten, die für das je-
weilige Kreditinstitut spezifisch sind, und damit eher seltener geändert werden müs-
sen.

Ist zur Belegung von DEs keine Angabe gemacht (z. B. Signaturverfahren etc.), er-
folgt die Belegung wie in der entsprechenden Nachricht/Segment.

Realisierung Bank: verpflichtend

Realisierung Kunde: verpflichtend

<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: D</td>
<td>Version: 3.0-FV</td>
<td>Financial Transaction Services (FinTS) Dokument: Formals</td>
</tr>
<tr>
<td>Seite:<br>78</td>
<td>Stand: 06.10.2017</td>
<td>Kapitel: Bankparameterdaten (BPD)<br>Abschnitt: Allgemeines</td>
</tr>
</table>


![](figures/86.1)


Werden Bankparameterdaten in einer Form übergeben, die
eine Dateibenennung erfordert (z. B. auf Diskette), ist als Na-
me für Bankparameterdaten "\*.bpd" zu wählen, wobei
"\*"
durch die jeweilige Kreditinstitutskennung (Bankleitzahl) zu er-
setzen ist.1

Über die Angebote fremder Kreditinstitute kann sich der Kun-
de mit Hilfe derer BPD informieren. Es wird empfohlen, Kun-
denprodukte standardmäßig mit einer Auswahl von Bankpa-
rameterdaten gängiger Kreditinstitute auszustatten. Falls die-
se nicht auf dem Kundensystem verfügbar sind, muss ein Dia-
log mit dem Fremdinstitut geführt werden, während dessen die
aktuellen BPD automatisch übertragen werden. Zur erstmali-
gen Verbindungsaufnahme mit dem Fremdinstitut sind dessen
Zugangsdaten erforderlich. Diese erhält das Kundenprodukt
entweder durch den Abruf der Kommunikationszugangsdaten
(s. Kap. 1.5) oder auf anderem Wege (z. B. direkt von seinem
Institut). Im letzteren Fall müssen die Zugangsdaten manuell
eingegeben werden.


### . Format

Name:
Bankparameterdaten
Typ:
Segmentfolge
Sender:
Kreditinstitut
Version:
3


<table>
<tr>
<th>Nr.</th>
<th>Name</th>
<th>Ver- sion</th>
<th>Typ</th>
<th>Ken- nung</th>
<th>Sta- tus</th>
<th>An- zahl</th>
<th>Anmerkungen</th>
</tr>
<tr>
<td>1</td>
<td>Bankparameter all- gemein</td>
<td>3</td>
<td>SEG</td>
<td>HIBPA</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>2</td>
<td>Kommunikations- zugang rückmelden</td>
<td>1</td>
<td>SEG</td>
<td>HIKOM</td>
<td>O</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>3</td>
<td>Sicherheitsverfah- ren</td>
<td>3</td>
<td>SEG</td>
<td>HISHV</td>
<td>O</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>4</td>
<td>Komprimierungs- verfahren</td>
<td>1</td>
<td>SEG</td>
<td>HIKPV</td>
<td>O</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>5</td>
<td>Parameterdaten</td>
<td>2</td>
<td>SF</td>
<td>#</td>
<td>O</td>
<td>1</td>
<td></td>
</tr>
</table>


<!-- PageFooter: 1 Systeme, die GroB- und Kleinschreibung unterscheiden, sollten den Dateinamen wie abgebildet (d. h. in Kleinschreibung) verwenden. -->
<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th rowspan="2">Version: 3.0-FV</th>
<th rowspan="2">Kapitel: D</th>
</tr>
<tr>
<th>Dokument:</th>
<th>Formals</th>
</tr>
<tr>
<td>Kapitel:<br>Abschnitt:</td>
<td>Bankparameterdaten (BPD) Bankparameter allgemein</td>
<td>Stand: 06.10.2017</td>
<td>Seite: 79</td>
</tr>
</table>


## D.2 Bankparameter allgemein


### . Format


<table>
<tr>
<td>Name:</td>
<td>Bankparameter allgemein</td>
</tr>
<tr>
<td>Typ:</td>
<td>Segment</td>
</tr>
<tr>
<td>Segmentart:</td>
<td>Administration</td>
</tr>
<tr>
<td>Kennung:</td>
<td>HIBPA</td>
</tr>
<tr>
<td>Bezugssegment:</td>
<td>HKVVB</td>
</tr>
<tr>
<td>Version:</td>
<td>3</td>
</tr>
<tr>
<td>Sender:</td>
<td>Kreditinstitut</td>
</tr>
</table>


<table>
<tr>
<th>Nr.</th>
<th>Name</th>
<th>Ver- sion</th>
<th>Typ</th>
<th>For- mat</th>
<th>Län- ge</th>
<th>Sta- tus</th>
<th>An- zahl</th>
<th>Restriktionen</th>
</tr>
<tr>
<td>1</td>
<td>Segmentkopf</td>
<td>1</td>
<td>DEG</td>
<td></td>
<td></td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>2</td>
<td>BPD-Version</td>
<td>1</td>
<td>DE</td>
<td>num</td>
<td>..3</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>3</td>
<td>Kreditinstitutsken- nung</td>
<td>1</td>
<td>DEG</td>
<td>kik</td>
<td>#</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>4</td>
<td>Kreditinstitutsbe- zeichnung</td>
<td>1</td>
<td>DE</td>
<td>an</td>
<td>..60</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>5</td>
<td>Anzahl Geschäfts- vorfallsarten</td>
<td>1</td>
<td>DE</td>
<td>num</td>
<td>..3</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>6</td>
<td>Unterstützte Spra- chen</td>
<td>2</td>
<td>DEG</td>
<td></td>
<td></td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>7</td>
<td>Unterstützte HBCI- Versionen</td>
<td>2</td>
<td>DEG</td>
<td></td>
<td></td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>8</td>
<td>Maximale Nachrich- tengröße</td>
<td>1</td>
<td>DE</td>
<td>num</td>
<td>..4</td>
<td>O</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>9</td>
<td>Minimaler Timeout- Wert</td>
<td>1</td>
<td>DE</td>
<td>num</td>
<td>..4</td>
<td>O</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>10</td>
<td>Maximaler Timeout- Wert</td>
<td>1</td>
<td>DE</td>
<td>num</td>
<td>..4</td>
<td>O</td>
<td>1</td>
<td></td>
</tr>
</table>


## . Belegungsrichtlinien


## Kreditinstitutskennung

Es ist die Institutskennung des Kreditinstituts einzustellen, auf das sich die
nachfolgenden Bankparameterdaten beziehen.


## Maximale Nachrichtengröße


![](figures/87.1)


Sollte dieses DE belegt sein, hat das Kundenprodukt bei der
Zusammenstellung der Nachricht diese Restriktion zu beach-
ten. Zu große Nachrichten dürfen nicht zur Versendung frei-
gegeben werden. Eventuell hat das Kundenprodukt Nach-
richten, die aus mehreren Aufträgen bestehen, in mehrere
kleinere Nachrichten mit je einem Auftrag aufzuteilen. Kann
die Nachrichtengröße bei umfangreichen Einzelaufträgen (z.
B. Sammelüberweisungen) nicht verringert werden, so ist der
Auftrag anwendungsseitig zu verkleinern.

<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: D</td>
<td>Version: 3.0-FV</td>
<td>Financial Transaction Services (FinTS) Dokument: Formals</td>
</tr>
<tr>
<td>Seite:<br>80</td>
<td>Stand: 06.10.2017</td>
<td>Kapitel: Bankparameterdaten (BPD)<br>Abschnitt: Kommunikationszugang</td>
</tr>
</table>


## D.3 Kommunikationszugang


### . Beschreibung

Dieses Segment enthält transportmedienspezifische Informationen, die für den Zu-
gang zum Kreditinstitut erforderlich sind.


![](figures/88.1)


Für den Erstzugang oder den anonymen Zugang ist die Einstellung
dieser Informationen in den BPD nicht hilfreich, da in diesem Fall
zum Zeitpunkt des Zugangs die entsprechenden BPD noch nicht
vorliegen. Die vom Kundenprodukt benötigten Zugangsinformati-
onen sollten daher durch den Abruf der Kommunikationszugangs-
daten (s. Kap. I.5) angefordert werden.

Die Einstellung dieser Daten erfolgt dennoch redundant in den BPD,
um einerseits dem Kundenprodukt Änderungen der Zugangspara-
meter direkt online mitzuteilen und andererseits den Zugang auch
zu ermöglichen, sofern das Kundenprodukt die BPD bereits vorlie-
gen hat (bspw. auf CD).


![](figures/88.2)


Grundsätzlich gelten für alle Kommunikationszugänge eines Insti-
tuts dieselben Bankparameterdaten (BPD). Möchte das Kreditinsti-
tut seine Angebote (z. B. die erlaubten Geschäftsvorfälle) abhängig
vom Kommunikationsmedium gestalten, so besteht die Möglichkeit,
für bestimmte Kommunikationszugänge eine eigene, noch nicht be-
legte BLZ zu vergeben.

. Format


<table>
<tr>
<td>Name:</td>
<td>Kommunikationszugang rückmelden</td>
</tr>
<tr>
<td>Typ:</td>
<td>Segment</td>
</tr>
<tr>
<td>Segmentart:</td>
<td>Administration</td>
</tr>
<tr>
<td>Kennung:</td>
<td>HIKOM</td>
</tr>
<tr>
<td>Bezugssegment:</td>
<td>HKVVB</td>
</tr>
<tr>
<td>Version:</td>
<td>s. Kap. I.5</td>
</tr>
<tr>
<td>Sender:</td>
<td>Kreditinstitut</td>
</tr>
<tr>
<td>Format:</td>
<td>s. Kap. I.5</td>
</tr>
</table>


<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th rowspan="2">Version: 3.0-FV</th>
<th rowspan="2">Kapitel: D</th>
</tr>
<tr>
<th>Dokument:</th>
<th>Formals</th>
</tr>
<tr>
<td>Kapitel:<br>Abschnitt:</td>
<td>Bankparameterdaten (BPD) Sicherheitsverfahren</td>
<td>Stand: 06.10.2017</td>
<td>Seite: 81</td>
</tr>
</table>


## D.4 Sicherheitsverfahren


### . Beschreibung

Es sind die Sicherheitsverfahren, d. h. Signatur- und Verschlüsselungsalgorithmen,
anzugeben, die das Kreditinstitut unterstützt.

. Format


<table>
<tr>
<td>Name:</td>
<td>Sicherheitsverfahren</td>
</tr>
<tr>
<td>Typ:</td>
<td>Segment</td>
</tr>
<tr>
<td>Segmentart:</td>
<td>Administration</td>
</tr>
<tr>
<td>Kennung:</td>
<td>HISHV</td>
</tr>
<tr>
<td>Bezugssegment:</td>
<td>HKVVB</td>
</tr>
<tr>
<td>Version:</td>
<td>3</td>
</tr>
<tr>
<td>Sender:</td>
<td>Kreditinstitut</td>
</tr>
<tr>
<td></td>
<td></td>
</tr>
</table>


<table>
<tr>
<th>Nr.</th>
<th>Name</th>
<th>Ver- sion</th>
<th>Typ</th>
<th>For- mat</th>
<th>Län- ge</th>
<th>Sta- tus</th>
<th>An- zahl</th>
<th>Restriktionen</th>
</tr>
<tr>
<td>1</td>
<td>Segmentkopf</td>
<td>1</td>
<td>DEG</td>
<td></td>
<td></td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>2</td>
<td>Mischung zulässig</td>
<td>1</td>
<td>DE</td>
<td>jn</td>
<td>#</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>3</td>
<td>Unterstützte Si- cherheitsverfahren</td>
<td>3</td>
<td>DEG</td>
<td></td>
<td></td>
<td>M</td>
<td>1..9</td>
<td></td>
</tr>
</table>


<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: D</td>
<td>Version: 3.0-FV</td>
<td>Financial Transaction Services (FinTS) Dokument: Formals</td>
</tr>
<tr>
<td>Seite:<br>82</td>
<td>Stand: 06.10.2017</td>
<td>Kapitel: Bankparameterdaten (BPD)<br>Abschnitt: Komprimierungsverfahren</td>
</tr>
</table>


## D.5 Komprimierungsverfahren


### . Beschreibung

Es sind die Komprimierungsverfahren anzugeben, die das Kreditinstitut unterstützt.

Falls das Kreditinstitut Komprimierung unterstützt, ist der deflate- oder auch GZIP-
Algorithmus gemäß RFC 1951 [RFC 1951] zwingend anzubieten. Die anderen Algo-
rithmen können zusätzlich optional angeboten werden. Zum deflate-Algorithmus gibt
es eine freie, auch in kommerziellen Produkten einsetzbare Referenzimplementie-
rung sowohl in Source-Form als auch als binäre Bibliothek für alle gängigen Platt-
formen [(http://www.gzip.org/zlib).](http://www.gzip.org/zlib)

Das Kreditinstitut darf nur komprimiert antworten, wenn das Kundensystem (z. B.
ein Smartphone) auch komprimiert gesendet hat. Damit wird vermieden, dass ein
Kundensystem eine komprimierte Nachricht erhält und diese ggf. nicht verarbeiten
kann.

. Format


<table>
<tr>
<td>Name:</td>
<td>Komprimierungsverfahren</td>
</tr>
<tr>
<td>Typ:</td>
<td>Segment</td>
</tr>
<tr>
<td>Segmentart:</td>
<td>Administration</td>
</tr>
<tr>
<td>Kennung:</td>
<td>HIKPV</td>
</tr>
<tr>
<td>Bezugssegment:</td>
<td>HKVVB</td>
</tr>
<tr>
<td>Version:</td>
<td>1</td>
</tr>
<tr>
<td>Sender:</td>
<td>Kreditinstitut</td>
</tr>
</table>


<table>
<tr>
<th>Nr.</th>
<th>Name</th>
<th>Ver- sion</th>
<th>Typ</th>
<th>For- mat</th>
<th>Län- ge</th>
<th>Sta- tus</th>
<th>An- zahl</th>
<th>Restriktionen</th>
</tr>
<tr>
<td>1</td>
<td>Segmentkopf</td>
<td>1</td>
<td>DEG</td>
<td></td>
<td></td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>2</td>
<td>Unterstützte Kom- primierungs- verfahren</td>
<td>2</td>
<td>DEG</td>
<td></td>
<td></td>
<td>M</td>
<td>1..9</td>
<td></td>
</tr>
</table>


<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th rowspan="2">Version: 3.0-FV</th>
<th rowspan="2">Kapitel: D</th>
</tr>
<tr>
<th>Dokument:</th>
<th>Formals</th>
</tr>
<tr>
<td>Kapitel:<br>Abschnitt:</td>
<td>Bankparameterdaten (BPD) Geschäftsvorfallparameter</td>
<td>Stand: 06.10.2017</td>
<td>Seite: 83</td>
</tr>
</table>


## D.6 Geschäftsvorfallparameter


### . Beschreibung

Dieses Segment beschreibt anhand von Parametern die konkrete kreditinstitutsindi-
viduelle Ausgestaltung eines Geschäftsvorfalls.

Das Segment ist für jeden Geschäftsvorfall einzustellen, den das Kreditinstitut unter-
stützt. Geschäftsvorfälle sind hierbei alle Auftragssegmente mit der Segmentart ,,Ge-
schäftsvorfall“. Bei Nichtunterstützung eines Geschäftsvorfalls entfällt das Segment.
Falls mehrere Versionen des Geschäftsvorfalls unterstützt werden, ist das Segment
für jede Segmentversion einzustellen. Die Zuordnung der Geschäftsvorfallparameter
zur jeweiligen Version des Geschäftsvorfalls erfolgt hierbei durch die im Segment-
kopf angegebene Segmentversion (s. Kap. B.5.1).


![](figures/91.1)


Da ein Kreditinstitut neben den in der DK standardisierten Ge-
schäftsvorfällen auch verbandseigene Transaktionen unterstützen
kann2, die dem Kundenprodukt u. U. nicht bekannt sind, darf ein
Kundenprodukt Segmente mit einer ihm unbekannten Segmentken-
nung nicht als Syntaxfehler ablehnen, sondern darf diese nicht in-
terpretieren.


![](figures/91.2)


Es ist dem Kreditinstitut freigestellt, ob es in den Bankparameterda-
ten grundsätzlich alle Segmentversionen eines Geschäftsvorfalls
einstellt, die es unterstützt oder nur diejenigen, die in Abhängigkeit
von der FinTS-Version, die der Kunde in der Dialoginitialisierung
mitteilt, im aktuellen Dialog als gültig entgegengenommen würden.


### . Format

Typ:

Format


<table>
<tr>
<th>Nr.</th>
<th>Name</th>
<th>Ver- sion</th>
<th>Typ</th>
<th>For- mat</th>
<th>Län- ge</th>
<th>Sta- tus</th>
<th>An- zahl</th>
<th>Restriktionen</th>
</tr>
<tr>
<td>1</td>
<td>Segmentkopf</td>
<td>1</td>
<td>DEG</td>
<td></td>
<td></td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>2</td>
<td>Maximale Anzahl Aufträge</td>
<td>1</td>
<td>DE</td>
<td>num</td>
<td>..3</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>3</td>
<td>Anzahl Signaturen mindestens</td>
<td>1</td>
<td>DE</td>
<td>num</td>
<td>1</td>
<td>M</td>
<td>1</td>
<td>0, 1, 2, 3</td>
</tr>
<tr>
<td>4</td>
<td>Sicherheitsklasse</td>
<td>1</td>
<td>DE</td>
<td>code</td>
<td>1</td>
<td>M</td>
<td>1</td>
<td>0, 1, 2, 3, 4</td>
</tr>
<tr>
<td>5</td>
<td>Parameter</td>
<td>1</td>
<td>DEG</td>
<td></td>
<td></td>
<td>#</td>
<td>1</td>
<td></td>
</tr>
</table>


<!-- PageFooter: 2 s. Kap. „Einleitung“ -->
<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: D</td>
<td>Version: 3.0-FV</td>
<td>Financial Transaction Services (FinTS) Dokument: Formals</td>
</tr>
<tr>
<td>Seite:<br>84</td>
<td>Stand: 06.10.2017</td>
<td>Kapitel: Bankparameterdaten (BPD)<br>Abschnitt: Parameterdaten</td>
</tr>
</table>


## D.7 Parameterdaten


### . Beschreibung

Die Segmentfolge ,,Parameterdaten“ enthält die in [Messages] beschriebenen Pa-
rametersegmente.


<table>
<tr>
<td colspan="2">. Format</td>
</tr>
<tr>
<td>Name:</td>
<td>Parameterdaten</td>
</tr>
<tr>
<td>Typ:</td>
<td>Segmentfolge</td>
</tr>
<tr>
<td>Sender:</td>
<td>Kreditinstitut</td>
</tr>
<tr>
<td>Version:</td>
<td>2</td>
</tr>
</table>


### ◆ Erläuterungen

Die Reihenfolge der Segmente ist nicht erheblich.

<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th rowspan="2">Version: 3.0-FV</th>
<th rowspan="2">Kapitel: E</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Formals</td>
</tr>
<tr>
<td>Kapitel:<br>Abschnitt:</td>
<td>Userparameterdaten (UPD) Allgemeines</td>
<td>Stand: 06.10.2017</td>
<td>Seite: 85</td>
</tr>
</table>


# E. USERPARAMETERDATEN (UPD)


## E.1 Allgemeines


### . Beschreibung

Die Userparameterdaten, die kreditinstitutsseitig benutzerbezogen generiert und
vorgehalten werden, erlauben eine automatisierte und dynamische Konfiguration
von Kundensystemen. In Abgrenzung zu den BPD enthalten die UPD ausschließlich
kunden- und kontenspezifische Informationen und sind somit häufigeren Modifikati-
onen unterworfen.

Während die Bankparameterdaten die grundsätzlich vom Kreditinstitut angebotenen
Geschäftsvorfälle angeben, gestatten die Userparameterdaten kontenbezogene Be-
rechtigungsprüfungen im Kundenprodukt. So kann das Kundenprodukt mit Hilfe der
Userparameterdaten prüfen, ob der Kunde für die Ausführung eines der in den
Bankparameterdaten angegebenen Geschäftsvorfälle in Verbindung mit einem be-
stimmten Konto berechtigt ist.

Das Konto, das im jeweiligen Geschäftsvorfall für die Berechtigungsprüfung heran-
zuziehen ist, ist im Regelfall entweder das Auftraggeberkonto oder das Depotkonto
bei Wertpapieraufträgen oder das Anlagekonto bei Festgeldanlagen. In den Fällen,
in denen es sich um ein hiervon abweichendes Konto handelt, ist dies in der Ge-
schäftsvorfallbeschreibung vermerkt. Bei Geschäftsvorfällen ohne Kontenbezug (z.
B. Informationsbestellung) findet keine Berechtigungsprüfung statt.

Bei Änderungen werden die Userparameterdaten im Rahmen der Dialoginitialisie-
rung für den sich anmeldenden Benutzer automatisch aktualisiert. Die aktualisierten
UPD werden sofort aktiv (s. hierzu die Ausführungen zu den BPD).

Realisierung Bank: verpflichtend

Realisierung Kunde: verpflichtend


![](figures/93.1)


Da auf Schnittstellenebene nicht gewährleistet werden kann, dass
das Kundenprodukt die Userparameterdaten korrekt auswertet, hat
auf jeden Fall eine entsprechende kreditinstitutsseitige Prüfung
stattzufinden.

Obwohl die Einstellung der Kontoinformationen für das Kreditinstitut
nicht verpflichtend ist, sollte es im Interesse einer einfachen und
komfortablen Kontenverwaltung für den Kunden, diese Informatio-
nen für alle Konten des Kunden bereitstellen.

<!-- PageBreak -->


<table>
<tr>
<th>Kapitel: E</th>
<th>Version: 3.0-FV</th>
<th>Financial Transaction Services (FinTS) Dokument: Formals</th>
</tr>
<tr>
<td>Seite:<br>86</td>
<td>Stand: 06.10.2017</td>
<td>Kapitel: Userparameterdaten (UPD)<br>Abschnitt: Allgemeines</td>
</tr>
</table>


![](figures/94.1)


(s. auch Hinweise bei „Bankparameterdaten“) Die Nutzung der UPD
erfordert eine entsprechende Unterstützung durch das Kunden-
produkt. Dateiname (sofern erforderlich) ist "\*.upd", wobei "\*" durch
eine eindeutige Kennung, die den Benutzer angibt, zu ersetzen ist.1

Da die Einstellung der Kontoinformationen für das Kreditinstitut nicht
verpflichtend ist, sollte das Kundenprodukt die Möglichkeit der ma-
nuellen Kontenerfassung vorsehen.


<table>
<tr>
<td colspan="2">. Format</td>
</tr>
<tr>
<td>Name:</td>
<td>Userparameterdaten</td>
</tr>
<tr>
<td>Typ:</td>
<td>Segmentfolge</td>
</tr>
<tr>
<td>Sender:</td>
<td>Kreditinstitut</td>
</tr>
<tr>
<td>Version:</td>
<td>3</td>
</tr>
</table>


<table>
<tr>
<th>Nr.</th>
<th>Name</th>
<th>Ver- sion</th>
<th>Typ</th>
<th>Kennung</th>
<th>Sta- tus</th>
<th>An- zahl</th>
<th>Anmerkungen</th>
</tr>
<tr>
<td>1</td>
<td>Userparameter all- gemein</td>
<td>4</td>
<td>SEG</td>
<td>HIUPA</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>2</td>
<td>Kontoinformation</td>
<td>6</td>
<td>SEG</td>
<td>HIUPD</td>
<td>O</td>
<td>n</td>
<td></td>
</tr>
</table>


<!-- PageFooter: 1 Systeme, die GroB- und Kleinschreibung unterscheiden, sollten den Dateinamen wie abgebildet (d. h. in Kleinschreibung) verwenden. -->
<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th rowspan="2">Version: 3.0-FV</th>
<th rowspan="2">Kapitel: E</th>
</tr>
<tr>
<th>Dokument:</th>
<th>Formals</th>
</tr>
<tr>
<td>Kapitel:<br>Abschnitt:</td>
<td>Userparameterdaten (UPD)<br>Userparameter allgemein</td>
<td>Stand: 06.10.2017</td>
<td>Seite: 87</td>
</tr>
</table>


## E.2 Userparameter allgemein


### . Format


<table>
<tr>
<td>Name:</td>
<td>Userparameter allgemein</td>
</tr>
<tr>
<td>Typ:</td>
<td>Segment</td>
</tr>
<tr>
<td>Segmentart:</td>
<td>Administration</td>
</tr>
<tr>
<td>Kennung:</td>
<td>HIUPA</td>
</tr>
<tr>
<td>Bezugssegment:</td>
<td>HKVVB</td>
</tr>
<tr>
<td>Version:</td>
<td>4</td>
</tr>
<tr>
<td>Sender:</td>
<td>Kreditinstitut</td>
</tr>
</table>


<table>
<tr>
<th>Nr.</th>
<th>Name</th>
<th>Ver- sion</th>
<th>Typ</th>
<th>For- mat</th>
<th>Län- ge</th>
<th>Sta- tus</th>
<th>An- zahl</th>
<th>Restriktionen</th>
</tr>
<tr>
<td>1</td>
<td>Segmentkopf</td>
<td>1</td>
<td>DEG</td>
<td></td>
<td></td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>2</td>
<td>Benutzerkennung</td>
<td>1</td>
<td>DE</td>
<td>id</td>
<td>#</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>3</td>
<td>UPD-Version</td>
<td>1</td>
<td>DE</td>
<td>num</td>
<td>..3</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>4</td>
<td>UPD-Verwendung</td>
<td>2</td>
<td>DE</td>
<td>code</td>
<td>1</td>
<td>M</td>
<td>1</td>
<td>0, 1</td>
</tr>
<tr>
<td>5</td>
<td>Benutzername</td>
<td>1</td>
<td>DE</td>
<td>an</td>
<td>..35</td>
<td>O</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>6</td>
<td>Erweiterung, allge- mein</td>
<td>1</td>
<td>DE</td>
<td>an</td>
<td>.204 8</td>
<td>O</td>
<td>1</td>
<td></td>
</tr>
</table>


## . Belegungsrichtlinien


### Benutzerkennung

Es ist die Benutzerkennung des Benutzers anzugeben, auf den sich die
Userparameterdaten beziehen (s. Kap. C.1.1).


### UPD-Version

Antwortet ein Kreditinstitut auf das Kundensegment HKVVB und der UPD-
Version=0 im Segment HIUPA ebenfalls mit einer UPD-Version=0, so müs-
sen im aktuellen Dialog diese übermittelten UPD verwendet werden; die
UPD sind dann nur für diesen Dialog gültig.


### Erweiterung, allgemein

Die innere Struktur dieses Parameterfeldes ist nicht weiter spezifiziert und
kann von den Partnern bilateral verwendet werden. Zur Selektion dieses
neuen Datenelementes muss HKVVB (Verarbeitungsvorbereitung) mindes-
tens in der Segmentversion 3 gesendet werden.

<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: E</td>
<td>Version: 3.0-FV</td>
<td>Financial Transaction Services (FinTS) Dokument: Formals</td>
</tr>
<tr>
<td>Seite:<br>88</td>
<td>Stand: 06.10.2017</td>
<td>Kapitel: Userparameterdaten (UPD)<br>Abschnitt: Kontoinformation</td>
</tr>
</table>


## E.3 Kontoinformation


### . Beschreibung

Das Segment ,,Kontoinformation“ sollte für jedes Konto, für das der Benutzer beim
betreffenden Kreditinstitut eine Verfügungsberechtigung besitzt, eingestellt werden.

Darüber hinaus kann auch ein Eintrag für nicht kontogebundene Geschäftsvorfälle
(z. B. Informationsbestellung) eingestellt werden. Hierbei handelt es sich im Regel-
fall um Geschäftsvorfälle, die auch über den anonymen Zugang genutzt werden
können. In diesem Fall sind die Felder für die Kontoverbindung und die übrigen kon-
tobezogenen Angaben nicht zu belegen.


<table>
<tr>
<td colspan="2">. Format</td>
</tr>
<tr>
<td>Name:</td>
<td>Kontoinformation</td>
</tr>
<tr>
<td>Typ:</td>
<td>Segment</td>
</tr>
<tr>
<td>Segmentart:</td>
<td>Administration</td>
</tr>
<tr>
<td>Kennung:</td>
<td>HIUPD</td>
</tr>
<tr>
<td>Bezugssegment:</td>
<td>HKVVB</td>
</tr>
<tr>
<td>Version:</td>
<td>6</td>
</tr>
<tr>
<td>Sender:</td>
<td>Kreditinstitut</td>
</tr>
</table>


<table>
<tr>
<th>Nr.</th>
<th>Name</th>
<th>Ver- sion</th>
<th>Typ</th>
<th>For- mat</th>
<th>Län- ge</th>
<th>Sta- tus</th>
<th>An- zahl</th>
<th>Restriktionen</th>
</tr>
<tr>
<td>1</td>
<td>Segmentkopf</td>
<td>1</td>
<td>DEG</td>
<td></td>
<td></td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>2</td>
<td>Kontoverbindung</td>
<td>2</td>
<td>DEG</td>
<td>ktv</td>
<td>#</td>
<td>C</td>
<td>1</td>
<td>N: bei Geschäftsvorfällen ohne Kontenbezug M: sonst</td>
</tr>
<tr>
<td>3</td>
<td>IBAN</td>
<td>1</td>
<td>DE</td>
<td>an</td>
<td>..34</td>
<td>O</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>4</td>
<td>Kunden-ID</td>
<td>1</td>
<td>DE</td>
<td>id</td>
<td>#</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>5</td>
<td>Kontoart</td>
<td>1</td>
<td>DE</td>
<td>num</td>
<td>..2</td>
<td>O</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>6</td>
<td>Kontowährung</td>
<td>1</td>
<td>DE</td>
<td>cur</td>
<td>#</td>
<td>O</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>7</td>
<td>Name des Kontoin- habers 1</td>
<td>1</td>
<td>DE</td>
<td>an</td>
<td>..27</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>8</td>
<td>Name des Kontoin- habers 2</td>
<td>1</td>
<td>DE</td>
<td>an</td>
<td>..27</td>
<td>O</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>9</td>
<td>Kontoproduktbe- zeichnung</td>
<td>1</td>
<td>DE</td>
<td>an</td>
<td>..30</td>
<td>O</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>10</td>
<td>Kontolimit</td>
<td>2</td>
<td>DEG</td>
<td></td>
<td></td>
<td>O</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>11</td>
<td>Erlaubte Ge- schäftsvorfälle</td>
<td>2</td>
<td>DEG</td>
<td></td>
<td></td>
<td>O</td>
<td>999</td>
<td></td>
</tr>
<tr>
<td>12</td>
<td>Erweiterung, konto- bezogen</td>
<td>1</td>
<td>DE</td>
<td>an</td>
<td>.204 8</td>
<td>O</td>
<td>1</td>
<td></td>
</tr>
</table>


## . Belegungsrichtlinien


## IBAN

Das Feld "IBAN" ist in FinTS V3.0 im Band „Multibankfähige Geschäftsvorfäl-
le" mit ..34 Stellen definiert. Die ursprüngliche Definition des HIUPD#6 sah
irrtümlicherweise eine maximale Länge von 35 Stellen vor. Falls ein Kreditin-
stitut in HIUPD IBANs mit 35 Stellen senden sollte, kann die Stelle 35 abge-
schnitten werden.

<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th rowspan="2">Version: 3.0-FV</th>
<th rowspan="2">Kapitel: E</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Formals</td>
</tr>
<tr>
<td>Kapitel:<br>Abschnitt:</td>
<td>Userparameterdaten (UPD) Kontoinformation</td>
<td>Stand: 06.10.2017</td>
<td>Seite: 89</td>
</tr>
</table>


## Name Kontoinhaber 1 und 2

Die Felder "Name des Kontoinhabers 1" und "Name des Kontoinhabers 2"
sind in FinTS V3.0 mit ..27 Stellen definiert. Da diese Felder in anderem
Kontext maximal 35 Stellen lang sein können, wird auch für diese beiden
UPD-Felder eine Maximallänge von 35 Stellen zugelassen. Bestehende Im-
plementierungen sollten damit keine Probleme bekommen und evtl. überzäh-
lige Stellen (>27) ggf. abschneiden.


## Erweiterung, kontobezogen

Die innere Struktur dieses Parameterfeldes ist in Abschnitt E.3.1 spezifiziert.
Zur Selektion dieses neuen Datenelementes muss HKVVB (Verarbeitungs-
vorbereitung) in der Segmentversion 3 gesendet werden.

Mit Einführung dieser neuen Struktur innerhalb des DE Erweiterung,
kontobezogen ist keine individuelle Nutzung dieses Datenelements mehr
zugelassen.


## E.3.1 Aufbau der UPD-Erweiterung, kontobezogen

Das Datenelement Erweiterung, kontobezogen wird in JSON-Notation (Ja-
vascript Object Notation) verwendet und enthält Informationen zur Steuerung von
FinTS-Kundenprodukten, deren Reaktionen im Kapitel F ,,FinTS Prozesse" be-
schrieben sind.

Einige Institute nutzen dieses Datenelement bereits bilateral zur Übermittlung eines
Timestamp des letzten bereitgestellten Umsatzes (Version ,00.00"). Eine multibank-
fähige Definition wird jedoch erst ab Version 01.00 spezifiziert.

In der vorliegenden Beschreibung wird auch bei JSON-Notation von ,Datenelemen-
ten" bzw. ,Elementen" gesprochen.

Beispielhafter Aufbau der JSON-Struktur der „Version 00.00“

{
"umsltzt": "2014-11-24-15.06.38.253985"
}

<!-- PageBreak -->


<table>
<caption>Beispielhafter Aufbau der JSON-Struktur ab Version 01.00</caption>
<tr>
<td>Kapitel: E</td>
<td>Version: 3.0-FV</td>
<td>Financial Transaction Services (FinTS) Dokument: Formals</td>
</tr>
<tr>
<td>Seite:<br>90</td>
<td>Stand: 06.10.2017</td>
<td>Kapitel: Userparameterdaten (UPD)<br>Abschnitt: Kontoinformation</td>
</tr>
</table>


<table>
<caption>Abbildung 14: Beispielhafter Aufbau der UPD-Erweiterung, kontobezogen (Tabelle)</caption>
<tr>
<td colspan="2">Ver</td>
<td colspan="3">"01.00"</td>
</tr>
<tr>
<td rowspan="20"></td>
<td colspan="4">AcctBal</td>
</tr>
<tr>
<td rowspan="19"></td>
<td>Cur</td>
<td colspan="2">EUR</td>
</tr>
<tr>
<td colspan="3">CurValBal</td>
</tr>
<tr>
<td rowspan="4"></td>
<td>&lt;&gt; DebCrd</td>
<td>D</td>
</tr>
<tr>
<td>《) Val</td>
<td>1476,98</td>
</tr>
<tr>
<td>&lt;&gt; Date</td>
<td>20151124</td>
</tr>
<tr>
<td>&lt;&gt; Time</td>
<td>"021533"</td>
</tr>
<tr>
<td colspan="3">InclPendTransBal</td>
</tr>
<tr>
<td rowspan="4"></td>
<td>&lt;&gt; DebCrd</td>
<td>D</td>
</tr>
<tr>
<td>() Val</td>
<td>1476,98</td>
</tr>
<tr>
<td>&lt;&gt; Date</td>
<td>20151124</td>
</tr>
<tr>
<td>&lt;&gt; Time</td>
<td>"063825"</td>
</tr>
<tr>
<td>&lt;&gt; OverDraftLim</td>
<td colspan="2">5000,00</td>
</tr>
<tr>
<td>&lt;&gt; AvailFunds</td>
<td colspan="2">1000,00</td>
</tr>
<tr>
<td>(&gt; AlrdyDrwnOnBal</td>
<td colspan="2">385,00</td>
</tr>
<tr>
<td>&lt; &gt; OverDraft</td>
<td colspan="2">500,00</td>
</tr>
<tr>
<td colspan="3">BookTime</td>
</tr>
<tr>
<td rowspan="2"></td>
<td>&lt;&gt; Date</td>
<td>20151124</td>
</tr>
<tr>
<td>&lt;&gt; Time</td>
<td>"021533"</td>
</tr>
<tr>
<td>&lt;&gt; MatDate</td>
<td colspan="2">20151124</td>
</tr>
<tr>
<td colspan="2">BalComplete</td>
<td colspan="3">true</td>
</tr>
<tr>
<td colspan="2">BalStatAcct</td>
<td colspan="3">true</td>
</tr>
<tr>
<td rowspan="3"></td>
<td>AcctStatNext</td>
<td colspan="3"></td>
</tr>
<tr>
<td rowspan="2"></td>
<td>&lt;&gt; Date</td>
<td colspan="2">20151125</td>
</tr>
<tr>
<td>Time</td>
<td colspan="2">110000</td>
</tr>
<tr>
<td rowspan="7"></td>
<td colspan="4">Inventory</td>
</tr>
<tr>
<td rowspan="6"></td>
<td>HKKAZ</td>
<td colspan="2">2015-11-24-15.06.38.2539850000</td>
</tr>
<tr>
<td>() HKCAZ</td>
<td colspan="2">2015-11-24-15.06.38.2539850000</td>
</tr>
<tr>
<td>(&gt; HKEKA</td>
<td colspan="2">2015-11-23-23.17.22.1234560000</td>
</tr>
<tr>
<td>(&gt; HKECA</td>
<td colspan="2">2015-11-23-23.17.22.1234560000</td>
</tr>
<tr>
<td>() HKCSB</td>
<td colspan="2"></td>
</tr>
<tr>
<td>() HKCDB</td>
<td colspan="2">MBLTJ4bAa5kCLCglcFGuWdVZoPKuBE</td>
</tr>
<tr>
<td colspan="2">&lt;&gt; BIC</td>
<td colspan="3">SSKMDEMM</td>
</tr>
<tr>
<td colspan="2">&lt;&gt; SEPAFmt</td>
<td colspan="3">true</td>
</tr>
<tr>
<td colspan="2">SEPAName</td>
<td colspan="3">R2FicmllbGUgTXVzdGVybWFubg==</td>
</tr>
</table>


<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th rowspan="2">Version: 3.0-FV</th>
<th rowspan="2">Kapitel: E</th>
</tr>
<tr>
<th>Dokument:</th>
<th>Formals</th>
</tr>
<tr>
<td>Kapitel:<br>Abschnitt:</td>
<td>Userparameterdaten (UPD)<br>Kontoinformation</td>
<td>Stand: 06.10.2017</td>
<td>Seite: 91</td>
</tr>
</table>


Abbildung 15: Beispielhafter Aufbau der UPD-Erweiterung, kontobezogen (JSON)

![{ "Ver": "01.00", "AcctBal": { "Cur": "EUR", "CurValBal": { "DebCrd": "D", "Val": "1476,98", "Date": 20151124, "Time": "021533" }, "InclPendTransBal": { "DebCrd": "D", "Val": "1476,98", "Date": 20151124, "Time": "063825" }, "OverDraftLim": "5000,00", "AvailFunds": "1000,00", "AlrdyDrwnOnBal": "385,00", "OverDraft": "500,00", "BookTime": { "Date": 20151124, "Time": "021533" }, "MatDate": 20151124 }, "BalComplete": true, "BalStatAcct": true, "AcctStatNext":{ "Date": 20151125, "Time": 110000 }, "Inventory": { "HKKAZ": "2015-11-24-15.06.38.2539850000", "HKCAZ": "2015-11-24-15.06.38.2539850000", "HKEKA": "2015-11-23-23.17.22.1234560000", "HKECA": "2015-11-23-23.17.22.1234560000", "HKCSB": "", "HKCDB": "MBLTJ4bAa5kCLCglcFGuWdVZoPKuBE" }, "BIC": "SSKMDEMM", "SEPAFmt":true, "SEPAName": "R2FicmllbGUgTXVzdGVybWFubg==" }](figures/99.1)


<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: E</td>
<td>Version: 3.0-FV</td>
<td>Financial Transaction Services (FinTS) Dokument: Formals</td>
</tr>
<tr>
<td>Seite: 92</td>
<td>Stand: 06.10.2017</td>
<td>Kapitel: Userparameterdaten (UPD)<br>Abschnitt: Kontoinformation</td>
</tr>
</table>


<table>
<tr>
<th>Name</th>
<th>Bedeutung</th>
<th>Typ</th>
<th>Län- ge</th>
<th>Sta tus</th>
<th>An- zahl</th>
<th>Restriktion / Bemerkung</th>
</tr>
<tr>
<td>Ver</td>
<td>Version</td>
<td>String</td>
<td>5</td>
<td>M</td>
<td>1</td>
<td>Aufbau: 00.00</td>
</tr>
<tr>
<td>AcctBal</td>
<td>Saldo</td>
<td>Object</td>
<td>#</td>
<td>O</td>
<td>0-1</td>
<td>analog MVE Saldo</td>
</tr>
<tr>
<td>Cur</td>
<td>Währung</td>
<td>String</td>
<td>3</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>CurValBal</td>
<td>Geb. Saldo</td>
<td>Object</td>
<td>#</td>
<td>O</td>
<td>0-1</td>
<td></td>
</tr>
<tr>
<td>DebCrd</td>
<td>Soll/Haben</td>
<td>String</td>
<td>1</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>Val</td>
<td>Wert</td>
<td>String</td>
<td>.15</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>Date</td>
<td>Datum</td>
<td>dat</td>
<td>#</td>
<td>M</td>
<td>1</td>
<td>jjjjmmtt</td>
</tr>
<tr>
<td>Time</td>
<td>Uhrzeit</td>
<td>tim</td>
<td>#</td>
<td>O</td>
<td>0-1</td>
<td>hhmmss</td>
</tr>
<tr>
<td>InclPend TransBal</td>
<td>Vorgem. Um- sätze</td>
<td>Object</td>
<td>#</td>
<td>O</td>
<td>0-1</td>
<td></td>
</tr>
<tr>
<td>DebCrd</td>
<td>Soll/Haben</td>
<td>String</td>
<td>1</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>Val</td>
<td>Wert</td>
<td>String</td>
<td>.15</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>Date</td>
<td>Datum</td>
<td>dat</td>
<td>#</td>
<td>M</td>
<td>1</td>
<td>jjjjmmtt</td>
</tr>
<tr>
<td>Time</td>
<td>Uhrzeit</td>
<td>tim</td>
<td>#</td>
<td>O</td>
<td>0-1</td>
<td>hhmmss</td>
</tr>
<tr>
<td>OverdraftLim</td>
<td>Kreditlinie</td>
<td>String</td>
<td>..15</td>
<td>O</td>
<td>0-1</td>
<td></td>
</tr>
<tr>
<td>AvailFunds</td>
<td>Verfügbarer Betrag</td>
<td>String</td>
<td>.. 15</td>
<td>O</td>
<td>0-1</td>
<td></td>
</tr>
<tr>
<td>AlrdyDrwn OnBal</td>
<td>Bereits verfüg- ter Betrag</td>
<td>String</td>
<td>.. 15</td>
<td>O</td>
<td>0-1</td>
<td></td>
</tr>
<tr>
<td>Overdraft</td>
<td>Überziehung</td>
<td>String</td>
<td>..15</td>
<td>O</td>
<td>0-1</td>
<td></td>
</tr>
<tr>
<td>BookTime</td>
<td>Buchungszeit- punkt</td>
<td>Object</td>
<td>#</td>
<td>O</td>
<td>0-1</td>
<td></td>
</tr>
<tr>
<td>Date</td>
<td>Datum</td>
<td>dat</td>
<td>#</td>
<td>M</td>
<td>1</td>
<td>jjjjmmtt</td>
</tr>
<tr>
<td>Time</td>
<td>Uhrzeit</td>
<td>tim</td>
<td>#</td>
<td>O</td>
<td>0-1</td>
<td>hhmmss</td>
</tr>
<tr>
<td>MatDate</td>
<td>Fälligkeit</td>
<td>dat</td>
<td>#</td>
<td>O</td>
<td>0-1</td>
<td>jjjjmmtt</td>
</tr>
<tr>
<td>BalComplete</td>
<td>Kompletter HISAL?</td>
<td>Bool</td>
<td>#</td>
<td>O</td>
<td>0-1</td>
<td>Wenn AcctBal enthalten</td>
</tr>
<tr>
<td>BalStatAcct</td>
<td>Umsatzsaldo aktuell?</td>
<td>Bool</td>
<td>1</td>
<td>O</td>
<td>0-1</td>
<td>Wenn Inventory Umsatzda- ten enthält</td>
</tr>
<tr>
<td>AcctStatNext</td>
<td>Zeitpunkt nächste Um- sätze</td>
<td>Object</td>
<td>#</td>
<td>O</td>
<td>0-1</td>
<td>Wenn Inventory Umsatzda- ten enthält</td>
</tr>
<tr>
<td>Date</td>
<td>Datum</td>
<td>dat</td>
<td>#</td>
<td>M</td>
<td>1</td>
<td>jjjjmmtt</td>
</tr>
<tr>
<td>Time</td>
<td>Uhrzeit</td>
<td>tim</td>
<td>#</td>
<td>O</td>
<td>0-1</td>
<td>hhmmss</td>
</tr>
<tr>
<td>Inventory</td>
<td>Bestände</td>
<td>Object</td>
<td>#</td>
<td>O</td>
<td>0-n</td>
<td></td>
</tr>
<tr>
<td>SegID</td>
<td>Segmentken- nung</td>
<td>String</td>
<td>5</td>
<td>M</td>
<td>1-n</td>
<td></td>
</tr>
<tr>
<td>ID</td>
<td>ID</td>
<td>String</td>
<td>30</td>
<td>O</td>
<td>0-n</td>
<td></td>
</tr>
<tr>
<td>BIC</td>
<td></td>
<td>String</td>
<td>.11</td>
<td>O</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>SEPAFmt</td>
<td>Format des SEPA-Namens</td>
<td>bool</td>
<td>1</td>
<td>O</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>SEPAName</td>
<td></td>
<td>String bzw. base64</td>
<td>..70 bzw. .100</td>
<td>O</td>
<td>1</td>
<td></td>
</tr>
</table>


<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th rowspan="2">Version: 3.0-FV</th>
<th rowspan="2">Kapitel: E</th>
</tr>
<tr>
<th>Dokument:</th>
<th>Formals</th>
</tr>
<tr>
<td>Kapitel:<br>Abschnitt:</td>
<td>Userparameterdaten (UPD) Kontoinformation</td>
<td>Stand: 06.10.2017</td>
<td>Seite: 93</td>
</tr>
</table>


![](figures/101.1)


Ein Kundenprodukt kann bei Belegung des Datenelements „Erweite-
rung, kontobezogen" anhand des ersten JSON-Elements erkennen,
ob es sich um die ,,Version 00.00" (mit erstem Datenelement
umsltzt) oder eine Version ab V01.00 (mit erstem Datenelement
Ver) handelt.

In beiden Fällen sollten die enthaltenen Inhalte entsprechend inter-
pretiert und berücksichtigt werden.

Für das JSON-Format String gilt der FinTS-Zeichensatz und -Zeichenvorrat.

Als Zeitzone für die Elemente umsltzt, Date und Time wird UTC+01:00 ange-
nommen.

Für die einzelnen JSON-Elemente gelten die im Folgenden beschriebenen
Festlegungen. Als Rahmenbedingung gilt, dass die in der JSON-Struktur
verwendeten Geschäftsvorfälle sowohl in den BPD als auch in den UPD unter Er-
laubte Geschäftsvorfälle enthalten sind.


### E.3.1.1 Belegungsvorschriften für die einzelnen JSON-Elemente

Im Folgenden werden die Belegungsvorschriften für die einzelnen JSON-Elemente
der Erweiterung, kontobezogen beschrieben. Bzgl. der konkreten Hand-
lungsoptionen gelten die detaillierteren Aussagen in Kapitel F ,,FinTS Prozesse“).


<table>
<tr>
<td>Element</td>
<td>Belegungsvorschriften und Festlegungen</td>
</tr>
<tr>
<td>Ver</td>
<td>Version der JSON-Struktur<br>Mit Ausnahme der ,,Version 00.00“ beginnt jede JSON-Struktur mit der Versionskennzeichnung Ver. Es sind nur die in den FinTS Formals veröffentlichten Versionen und deren Inhalte gül- tig.</td>
</tr>
<tr>
<td>AcctBal</td>
<td>Saldo (Aufbau analog HISAL in der Segmentversion #7)<br>Das Kreditinstitut liefert in diesem Objekt Saldeninformationen. Das Format leitet sich aus dem in FinTS spezifizierten MVE ab; daher gelten auch die entsprechenden Belegungen.<br>Erforderliche Reaktion des Kundenprodukts:<br>Liefert das Kreditinstitut mit diesem Element den aktuellen Sal- do, so sollte das Kundenprodukt keine separate Abfrage des ak- tuellen Saldo einreichen.</td>
</tr>
<tr>
<td>BalComplete</td>
<td>Saldeninformationen analog HISAL komplett enthalten<br>AcctBal enthält alle Informationen, die auch in HISAL bereitge- stellt werden. Ein separater Abruf von HKSAL liefert also keine zusätzlichen Informationen.<br>Erforderliche Reaktion des Kundenprodukts:<br>Das Kundenprodukt sollte keine separate Saldenabfrage einrei- chen.</td>
</tr>
</table>


<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: E</td>
<td>Version: 3.0-FV</td>
<td>Financial Transaction Services (FinTS) Dokument: Formals</td>
</tr>
<tr>
<td>Seite: 94</td>
<td>Stand: 06.10.2017</td>
<td>Kapitel: Userparameterdaten (UPD)<br>Abschnitt: Kontoinformation</td>
</tr>
</table>


<table>
<tr>
<th>Element</th>
<th colspan="5">Belegungsvorschriften und Festlegungen</th>
</tr>
<tr>
<td>BalStatAcct</td>
<td colspan="5">Saldo in der Umsatzliste aktuell<br>Dieses Element darf nur belegt werden, wenn sich in Invento- ry entsprechende Geschäftsvorfälle für Umsatzabfragen befin- den (vgl. Kapitel F.3.1).<br>Mit diesem Element wird darüber informiert, ob der gebuchte Saldo bzw. der Saldo der vorgemerkten Umsätze dem aktuellen Saldo entspricht. Dies wird durch die Existenz dieses JSON- Elements in der UPD-Erweiterung, kontobezogen ausge- drückt.<br>Erforderliche Reaktion des Kundenprodukts:<br>Wird der gelieferte Saldo der bereitgestellten Umsätze als aktu- ell gekennzeichnet, sollte das Kundenprodukt keine separate Abfrage zum Erhalt des aktuellen Saldo bzw. des Saldo der vor- gemerkten Umsätze einreichen.</td>
</tr>
<tr>
<td>AcctStatNext</td>
<td colspan="5">Datum und Uhrzeit der nächsten Umsatzbereitstellung<br>Dieses Objekt darf nur belegt werden, wenn sich in Inventory entsprechende Geschäftsvorfälle für Umsatzabfragen befinden (vgl. Kapitel F.3.1).<br>Das Kreditinstitut stellt den Zeitpunkt der nächsten Umsatzbe- reitstellung zur Verfügung.<br>Erforderliche Reaktion des Kundenprodukts:<br>Stellt das Kreditinstitut den Zeitpunkt der nächsten Umsatzbe- reitstellung zur Verfügung, sollte das Kundenprodukt vor diesem Zeitpunkt keine weiteren Umsatzabfragen durchführen.</td>
</tr>
<tr>
<td rowspan="5">Inventory</td>
<td colspan="5">Für den Benutzer angelegte Bestände<br>Für jeden für den Benutzer unterstützten Bestand wird vom Kre- ditinstitut die entsprechende Segmentkennung des Abholauf- trags und ggf. die zugehörige ID geliefert.<br>Diese Segmentkennungen müssen in der BPD und in den UPD unter Erlaubte Geschäftsvorfälle enthalten sein.<br>Es lassen sich folgende Zustände unterscheiden;<br>in UPD<br>Seg- ID<br>ID<br>Bedeutung</td>
</tr>
<tr>
<td>[Z1]</td>
<td>N</td>
<td>N</td>
<td>N</td>
<td>Für diesen GV ist der Benutzer nicht berechtigt.</td>
</tr>
<tr>
<td>[Z2]</td>
<td>J</td>
<td>N</td>
<td>N</td>
<td>Für diesen GV bietet das Institut keine Information zur Aktualität des Bestandes an.</td>
</tr>
<tr>
<td>[Z3]</td>
<td>J</td>
<td>J</td>
<td>N</td>
<td>Für diesen GV bietet das Institut ein Information über die Aktualität des Bestands, aber der Benutzer hat keinen Bestand.</td>
</tr>
<tr>
<td>[Z4]</td>
<td>J</td>
<td>J</td>
<td>J</td>
<td>Für diesen GV bietet das Institut</td>
</tr>
</table>


<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th rowspan="2">Version: 3.0-FV</th>
<th rowspan="2">Kapitel: E</th>
</tr>
<tr>
<th>Dokument:</th>
<th>Formals</th>
</tr>
<tr>
<td>Kapitel: Abschnitt:</td>
<td>Userparameterdaten (UPD) Kontoinformation</td>
<td>Stand: 06.10.2017</td>
<td>Seite: 95</td>
</tr>
</table>


<table>
<tr>
<th>Element</th>
<th colspan="2">Belegungsvorschriften und Festlegungen</th>
</tr>
<tr>
<td></td>
<td>[Z1]<br>[Z2]<br>[Z3]<br>[Z4]<br>Erforderliche Reaktion<br>Es sollte kein<br>Es kann ein<br>Es sollte kein<br>Ein Bestandsabruf<br>wenn die ID<br>Bestands</td>
<td>eine Information über die Aktuali- tät des Bestands, der Benutzer führt einen solchen Bestand, die ID kennzeichnet die Aktualität des Bestandes.<br>des Kundenprodukts:<br>Bestandsabruf durchgeführt werden.<br>Bestandsabruf durchgeführt werden.<br>Bestandsabruf durchgeführt werden.<br>sollte nur durchgeführt werden,<br>sich von der ID des lokal gespeicherten<br>unterscheidet.</td>
</tr>
<tr>
<td>Inventory (SegID)</td>
<td colspan="2">Segmentkennung des Abholauftrags<br>Für jeden für den Benutzer angelegten Bestand wird die Seg- mentkennung des zugehörigen Abholauftrags eingestellt.<br>Gültig sind folgende Segmentkennungen:<br>HKKAZ: Umsatzbestand (MT940), impliziert HKKAN<br>HKCAZ: Umsatzbestand (camt), impliziert HKCAN<br>HKKIF: Bestand Kontoinformationen<br>ΗΚΕΚΑ: Bestand elektronischer Kontoauszüge ( MT940,PDF )<br>HKECA:<br>Bestand elektronischer Kontoauszüge (camt)<br>ΗΚΕΚP:<br>Bestand elektronischer Kontoauszüge (PDF)<br>HKFGB:<br>Bestand Festgeld<br>HKWPD:<br>Bestand Depotaufstellung<br>HKWDU:<br>Bestand Depotumsätze<br>HKFRD:<br>Bestand Freistellungsdaten<br>HKFDL:<br>Bestand Finanzdatenformate<br>HKPPE:<br>Bestand Daueraufträge Prepaid-Laden<br>HKPOF:<br>Bestand Postfachnachrichten<br>HKCSB:<br>Bestand terminierter SEPA-Einzelüberweisungen<br>HKCMB:<br>Bestand terminierter SEPA-Sammelüberw.<br>HKCDB:<br>Bestand SEPA-Daueraufträge<br>HKCVB:<br>Bestand vorbereiteter SEPA-Überweisungen<br>HKDSB:<br>Bestand rückgabefähiger SEPA-Lastschriften</td>
</tr>
<tr>
<td>Kapitel: E</td>
<td>Version: 3.0-FV</td>
<td>Financial Transaction Services (FinTS) Dokument: Formals</td>
</tr>
<tr>
<td>Seite:<br>96</td>
<td>Stand: 06.10.2017</td>
<td>Kapitel: Userparameterdaten (UPD)<br>Abschnitt: Kontoinformation</td>
</tr>
</table>


<table>
<tr>
<td>Element</td>
<td>Belegungsvorschriften und Festlegungen</td>
</tr>
<tr>
<td></td>
<td>HKDBS:<br>Bestand SEPA-Einzellastschriften (CORE/COR1)<br>HKDMB:<br>Bestand terminierter SEPA-Sammellastschriften<br>HKBBS:<br>Bestand SEPA-Firmeneinzellastschriften (B2B)<br>HKBMB:<br>Bestand term. SEPA-Firmensammellastschriften<br>HKDDB:<br>Bestand SEPA-Dauerlastschriften<br>HKCUB:<br>Bestand Empfängerkonten für SEPA-Übertrag<br>HKSSR:<br>SEPA-Statusreport<br>HKTAB:<br>TAN-Medien anzeigen<br>Belegung: Gültige FinTS Segmentkennungen für Benutzernach- richten.</td>
</tr>
<tr>
<td>Inventory[1] (ID)</td>
<td>ID für die jeweilige Bestandsart pro Segmentkennung<br>Vom Kreditinstitut wird optional eine maximal 30-stellige ID des letzten Bestandsabrufs geliefert.<br>Format: analog FinTS-Format ID.<br>Erforderliche Reaktion des Kundenprodukts:<br>Lokal gespeicherte Bestände sollten mit einem entsprechenden ID-Element versehen werden. Bei lokalem Vorhandensein eines Umsatzes mit identischer ID sollte kein erneuter Bestandsabruf erfolgen.</td>
</tr>
<tr>
<td>BIC</td>
<td>BIC<br>Das Kreditinstitut teilt in diesem Element den BIC zu dem ge- wählten Konto mit. Dadurch kann in vielen Fällen die Verwen- dung des HKSPA - SEPA Kontoverbindung anfordern obsolet werden. Handelt es sich bei dem betroffenen Konto um ein SEPA-fähiges Konto, soll das Element BIC möglichst vom Institut belegt werden. Sollte aus anderen Gründen HKSPA ver- wendet werden, so hat der dort übermittelte BIC Vorrang.</td>
</tr>
<tr>
<td>SEPAFmt</td>
<td>Format des SEPA-Namens<br>Durch dieses Element wird gesteuert, ob das Element SEPA- Name base64-kodiert ist oder nicht:<br>0: SEPAName wird im FinTS-Zeichensatz, maximal 70-stellig eingestellt<br>1: SEPAName wird im UTF-8-Zeichensatz, base64-kodiert mit maximal 100 Zeichen eingestellt.</td>
</tr>
<tr>
<td>SEPAName</td>
<td>SEPA-konformer Name des Kontoinhabers</td>
</tr>
</table>


<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th rowspan="2">Version: 3.0-FV</th>
<th rowspan="2">Kapitel: E</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Formals</td>
</tr>
<tr>
<td>Kapitel: Abschnitt:</td>
<td>Userparameterdaten (UPD) Kontoinformation</td>
<td>Stand: 06.10.2017</td>
<td>Seite: 97</td>
</tr>
</table>


<table>
<tr>
<td>Element</td>
<td>Belegungsvorschriften und Festlegungen</td>
</tr>
<tr>
<td></td>
<td>Im Rahmen der Umsetzung zur Geldtransferverordnung (GTVO) muss zukünftig ein SEPA-konformer, bis zu 70-stelliger Name (Länge ggf. vor der base64-Kodierung) des Kontoinhabers ba- sierend auf dem KWG24c-Namen verwendet werden. Lt. Artikel 4 ff. der Verordnung (EG) Nr. 1781/2006 (GTVO) gehört es zur Pflicht des Zahlungsdienstleisters des Auftraggebers sicherzu- stellen, dass die vollständigen Informationen über den Auftrag- geber weitergeleitet werden. Auftraggeber ist ausschließlich der Kontoinhaber. Das Format des SEPA-Namens wird durch das Element SEPAFmt festgelegt. Bei SEPA-fähigen Konten sollte das Institut den SEPA-Namen möglichst mitliefern. Sendet ein Kreditinstitut für ein Konto das Element SEPAName, so muss der hier übermittelte SEPA-Name im Sinn der o. g. Verordnung vom Kundenprodukt verwendet werden.</td>
</tr>
<tr>
<td>umsltzt</td>
<td>Timestamp des letzten Umsatzabrufs (nur bei ,,Version 00.00")<br>Vom Kreditinstitut wird der Timestamp des letzten Umsatzabrufs im Format ,,yyyy-mm-tt-hh.mm.ss.mmmmmm" geliefert.<br>Erforderliche Reaktion des Kundenprodukts:<br>Lokal gespeicherte Umsätze sollten mit einem entsprechenden Timestamp (hier: Spezialfall der ID) versehen werden. Bei loka- lem Vorhandensein eines Umsatzes mit identischem Timestamp darf kein erneuter Umsatzabruf erfolgen.</td>
</tr>
</table>


## E.3.1.2 Beispiel für die Verwendung der UPD-Erweiterung zur Bestandsoptimierung

Das folgende Beispiel soll die Verwendung der Elemente Inventory, SegID und
ID zeigen.

Alle im Beispiel genannten Geschäftsvorfälle befinden sich in den BPD.

In den UPD finden sich unter Erlaubte Geschäftsvorfälle die Segmentken-
nungen HKKAZ, HKCAZ, HKKIF, HKEKA, HKECA, HKCSB und HKCDB.

Beispiel für den fachlichen Inhalt von Inventory:

SegID

ID

HKKAZ

2015-11-24-15.06.38.2539850000

HKCAZ

2015-11-24-15.06.38.2539850000

HKEKA

HKECA

HKCDB

MBLTJ4bAa5kCLCglcFGuWdVZoPKuBE

Bedeutung analog der Definition der Zustände:

[Z2] der in den UPD des Benutzers gelistete Geschäftsvorfall HKCSB ist in der

<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: E</td>
<td>Version: 3.0-FV</td>
<td>Financial Transaction Services (FinTS) Dokument: Formals</td>
</tr>
<tr>
<td>Seite:<br>98</td>
<td>Stand: 06.10.2017</td>
<td>Kapitel: Userparameterdaten (UPD)<br>Abschnitt: Kontoinformation</td>
</tr>
</table>


UPD-Erweiterung, kontobezogen nicht gelistet. Für diesen GV bietet das
Kreditinstitut keine Information zur Aktualität des Bestands an.
Es kann ein Bestandsabruf durchgeführt werden.

[Z3] Der Benutzer besitzt keine Bestände für die Abholaufträge HKEKA und
HKECA. Für diese Bestände sollten keine Abholaufträge gesendet werden.

[Z4] Für die Abholaufträge HKKAZ, HKCAZ und HKCDB sind aktuelle IDs vorhan-
den. Bestände sollten nur abgerufen werden, wenn die IDs sich von den lokal ge-
speicherten IDs unterscheiden.

<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th rowspan="2">Version: 3.0-FV</th>
<th rowspan="2">Kapitel: F</th>
</tr>
<tr>
<th>Dokument:</th>
<th>Formals</th>
</tr>
<tr>
<td>Kapitel:<br>Abschnitt:</td>
<td>FinTS Prozesse Buchstabe A</td>
<td>Stand: 06.10.2017</td>
<td>Seite: 99</td>
</tr>
</table>


# F. FINTS PROZESSE

FinTS ist als offene Schnittstelle zwischen Benutzer und Kreditinstitut konzipiert und
spezifiziert Schnittstellenprotokoll, Daten und Sicherheitsverfahren. Dem Gedanken
der offenen Schnittstelle widerspricht allerdings, dass jede von einem Kundenpro-
dukt ausgelöste FinTS-Nachricht beim empfangenden Rechenzentrum Kosten ver-
ursacht, die durch das Kreditinstitut zu tragen sind. Viele dieser Kosten sind jedoch
vermeidbar, da z. B. immer auf gleiche Datenbestände zugegriffen wird, die sich
zwischen den Abrufen nicht geändert haben oder Bestände abgefragt werden, über
die der Benutzer gar nicht verfügt.

Daher enthält dieses Kapitel idealtypische Abläufe und Rahmenbedingungen, die
von Kreditinstituten und Kundenprodukten teils verpflichtend einzuhalten oder als
Empfehlung anzusehen sind. Aufgrund der Dringlichkeit des Themas und der Ver-
meidung unnötiger Kosten sind die im Folgenden dargestellten Prozesse mit Veröf-
fentlichung auch als verbindlich anzusehen.

Bei der Beschreibung der Prozesse werden folgende Abstufungen und Begrifflich-
keiten verwendet:

Verpflichtung

Das beschriebene Verhalten ist zwingend vorgeschrieben. Bei
Nicht-Einhaltung der Vorgabe ist die Gegenseite berechtigt, die
Kommunikation mit einer entsprechenden Fehlermeldung zu
beenden, auch wenn die eingereichten Nachrichten / Segmente
syntaktisch fehlerfrei sind.

In der Beschreibung werden die Begriffe MUSS, IST ZU bzw.
DARF NICHT verwendet.

Empfehlung

Das Verhalten hat Empfehlungscharakter, sollte aber nach Mög-
lichkeit eingehalten werden. Eine Ablehnung einer Kommunika-
tion bei Verstoß gegen diese Empfehlung findet jedoch nicht
statt.

In der Beschreibung werden die Begriffe SOLL / SOLLTE bzw.
SOLL / SOLLTE NICHT verwendet.

Option
Das Verhalten ist wahlfrei einzusetzen. Eine Verpflichtung für
die Unterstützung des Prozesses besteht nicht. Falls der Ablauf
jedoch unterstützt wird, dann genau in der beschriebenen Form.
Eine Ablehnung der Kommunikation findet nicht bzw. nur bei
Abweichen von dem beschriebenen Verhalten statt.

In der Beschreibung werden die Begriffe KANN bzw. MUSS
NICHT verwendet.


## F.1 Versionsverwaltung

Soweit diese Abläufe in Zusammenhang mit den Vorgaben aus einer neuen Version
der UPD-Erweiterung, kontobezogen (vgl. Kapitel E.3.1) stehen, werden die
jeweiligen Übergangsfristen durch die Deutsche Kreditwirtschaft frühzeitig bekannt-
gegeben.

<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: F</td>
<td>Version: 3.0-FV</td>
<td>Financial Transaction Services (FinTS) Dokument: Formals</td>
</tr>
<tr>
<td>Seite:<br>100</td>
<td>Stand: 06.10.2017</td>
<td>Kapitel: FinTS Prozesse<br>Abschnitt: Buchstabe A</td>
</tr>
</table>


Gleiches gilt für die Abkündigung von Versionen der UPD-Erweiterung, kon-
tobezogen. Als Ziel wird verfolgt, jeweils zwei aktive Versionen gleichzeitig zu un-
terstützen.

Diese Mechanismen zum gezielten Bestandsabruf gelten im Allgemeinen nur für die
FinTS-Kommunikation, nicht für den Abruf über andere Vertriebskanäle wie z. B.
EBICS.


## F.2 Generelle Festlegungen

Dieser Abschnitt enthält generelle Prozessfestlegungen zum Umgang mit dem
FinTS-Protokoll, die unabhängig von den nachfolgenden Einzelprozessen eingehal-
ten werden sollten, dort jedoch nicht verfeinert werden:

Generelle Festlegungen für die Institutsseite


<table>
<tr>
<td>Nr.</td>
<td>Festlegung</td>
</tr>
<tr>
<td>[IF1]</td>
<td>Das Datenelement Erweiterung, kontobezogen soll vom Institut be- legt werden.</td>
</tr>
<tr>
<td>[IF2]</td>
<td>Es können die JSON-Struktur der ,,Version 00.00" oder ab Version 01.00 verwendet werden.</td>
</tr>
<tr>
<td>[IF3]</td>
<td>Bietet ein Institut die Belegung des Elements UPD-Version an, so muss bei jeder Änderung eines UPD-Elementes und im Speziellen der UPD- Erweiterung inkl. der JSON-Struktur die UPD-Version hochgezählt und ei- ne neue UPD bereitgestellt werden. Gleiches gilt bei der Verwendung von UPD-Version=0.<br>![](figures/108.1)<br>Ein Kundenprodukt muss bei einem wrap around den Sprung von UPD-Version=999 auf UPD-Version=1 korrekt verarbeiten können.</td>
</tr>
<tr>
<td>[IF4]</td>
<td>Es darf immer nur eine JSON-Struktur in das Datenelement Erweite- rung, kontobezogen eingestellt werden.</td>
</tr>
<tr>
<td>[IF4]</td>
<td>Jede Segmentkennung und die zugehörige optionale ID darf in einer JSON-Struktur nur einmal auftreten.</td>
</tr>
<tr>
<td>[IF5]</td>
<td>Es dürfen nur in der vorliegenden Spezifikation veröffentlichte Versionen verwendet werden. Im Rahmen der FinTS Formals wird auch festgelegt, welche Versionen zugelassen sind. Im Maximum sollen zwei Versionen parallel unterstützt werden. Dies wird über die Versionsverwaltung gere- gelt.</td>
</tr>
<tr>
<td>[IF6]</td>
<td>Verbands- oder institutsspezifische Versionen und Belegungen sind nicht vorgesehen.</td>
</tr>
<tr>
<td>[IF7]</td>
<td>Optionale JSON-Elemente können weggelassen werden.</td>
</tr>
</table>


<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th rowspan="2">Version: 3.0-FV</th>
<th rowspan="2">Kapitel: F</th>
</tr>
<tr>
<th>Dokument:</th>
<th>Formals</th>
</tr>
<tr>
<td>Kapitel:<br>Abschnitt:</td>
<td>FinTS Prozesse Buchstabe A</td>
<td>Stand: 06.10.2017</td>
<td>Seite: 101</td>
</tr>
</table>


### Generelle Festlegungen für die Kundenseite


<table>
<tr>
<td>Nr.</td>
<td>Festlegung</td>
</tr>
<tr>
<td>[KF1]</td>
<td>Ein vom Kreditinstitut belegtes Erweiterung, kontobezogen soll in- terpretiert und entsprechend den Vorgaben und Prozessen in Abschnitt F verarbeitet werden.</td>
</tr>
<tr>
<td>[KF2]</td>
<td>Ein Kundenprodukt soll aktuell die JSON-Struktur der ,,Version 00.00" so- wie die im Rahmen der FinTS Formals spezifizierten JSON-Strukturen der Version 01.00 korrekt verarbeiten können.</td>
</tr>
<tr>
<td>[KF3]</td>
<td>Auch wenn einzelne JSON-Elemente vom Institut nicht bereitgestellt wer- den, müssen die vorhandenen Elemente korrekt verarbeitet werden. Wird bei der Interpretation der UPD-Erweiterung ein Syntaxfehler festgestellt, wird der Inhalt der gesamten UPD-Erweiterung ignoriert.</td>
</tr>
<tr>
<td>[KF4]</td>
<td>Ein Kundenprodukt sollte nur durch den Benutzer manuell initiierte FinTS-Dialoge durchführen. Es kann Möglichkeiten zum zeitgesteuerten Abruf von Informationen anbieten, jedoch sollten Zeitintervalle so gewählt werden, dass die Anzahl der Anfragen auf ein Minimum reduziert ist.</td>
</tr>
<tr>
<td>[KF5]</td>
<td>Ein Kundenprodukt darf Abholaufträge und Bestandsabfragen nur einrei- chen, wenn dies ausdrücklich mit dem Benutzer vereinbart ist. Hierzu gehören auch mit dem Benutzer vereinbarte zeitlich automatisierte Abru- fe. Die Zeitintervalle sollten in Abstimmung mit dem Kunden so gewählt werden, dass die Anzahl der Anfragen auf ein Minimum reduziert ist.</td>
</tr>
<tr>
<td>[KF6]</td>
<td>Ein Kundenprodukt muss wo immer möglich für den Einsatzzweck opti- male Abfragetechniken nutzen und darf generalisierte Abholaufträge nur einreichen, wenn dies vom Nutzer ausdrücklich gewünscht ist. Ausge- nommen hiervon sind technisch bedingte Abrufe z. B. bei Timeouts.</td>
</tr>
<tr>
<td>[KF7]</td>
<td>Ein Kundenprodukt soll keine separaten Abfragen des aktuellen Saldo durchführen, wenn der aktuelle Saldo bereits in den Umsätzen enthalten ist.</td>
</tr>
<tr>
<td>[KF8]</td>
<td>Die Aussagen beziehen sich jeweils nur auf eine spezifische Installation eines Kundenproduktes. Betreibt ein Benutzer mehrere Installationen mit getrennter Bestandshaltung, so gelten die Festlegungen pro Bestands- haltung.</td>
</tr>
<tr>
<td>[KF9]</td>
<td>Führt ein Kundenprodukt keine lokalen Bestände, so gelten nur die Fest- legungen [KF4] bis [KF7].</td>
</tr>
<tr>
<td>[KF10]</td>
<td>Bei technischen Problemen wie z. B. Timeouts können Bestände auch ohne Berücksichtigung der Angaben in der UPD-Erweiterung, kon- tobezogen abgeholt werden.</td>
</tr>
</table>


## F.3 Spezielle Prozesse

Die folgenden speziellen Prozesse verfeinern die in den generellen Prozessfestle-
gungen definierten Regeln anhand der Informationen, die über das Datenelement
,,Erweiterung, kontobezogen" vom Kreditinstitut geliefert werden.

<!-- PageBreak -->


<table>
<tr>
<th>Kapitel: F</th>
<th>Version: 3.0-FV</th>
<th>Financial Transaction Services (FinTS) Dokument: Formals</th>
</tr>
<tr>
<td>Seite:<br>102</td>
<td>Stand: 06.10.2017</td>
<td>Kapitel: FinTS Prozesse<br>Abschnitt: Buchstabe A</td>
</tr>
</table>


### F.3.1 Abruf von Umsätzen

Umsatzabrufe dienen dazu, dem Kundenprodukt aktuell und lückenlos alle Konto-
bewegungen mitzuteilen. Im Idealfall sollte jeder Umsatz pro Kundenprodukt nur
einmal abgerufen und dann lokal im Kundenprodukt gespeichert werden (falls das
Kundenprodukt eine Speicherung zulässt).

Zum Umsatzabruf werden folgende Geschäftsvorfälle verwendet:

HKKAZ: Kontoumsätze/Zeitraum (MT940)

HKKAN: Kontoumsätze/Neue Umsätze (MT940)

HKCAZ: Kontoumsätze/Zeitraum (camt)

HKCAN: Kontoumsätze/Neue Umsätze (camt)

Ein Kundenprodukt muss die folgenden Informationen aus dem Datenelement „Er-
weiterung, kontobezogen“ berücksichtigen:

Version 00.00: umsltzt

Version 01:00: BalStatAct, AcctStatNext, Inventory

Basierend auf diesen Informationen muss ein Kundenprodukt folgendermaßen rea-
gieren:


<table>
<tr>
<td>umsltzt, Inventory</td>
<td>Wenn der Benutzer eine Umsatzabfrage initiiert muss in der Dialoginitialisierungsantwort die übermittelte ID mit der des letzten lokal gespeicherten Umsatzes ver- glichen werden. Bei Gleichheit darf das Kundenprodukt keine Umsatzabfrage starten, sondern muss den Be- nutzer in geeigneter Weise informieren, dass keine neuen Umsätze vorliegen.</td>
</tr>
<tr>
<td>AcctStatNext</td>
<td>Hat ein Kundenprodukt beim vorherigen Abruf den Zeitpunkt der nächsten Umsatzbereitstellung erhalten, darf es vor diesem Zeitpunkt keinen Dialog zum Zweck der Umsatzabfrage aufbauen und innerhalb eines Dia- loges, z. B. um eine Überweisung einzureichen, auch keinen Umsatzabruf starten.</td>
</tr>
</table>


### F.3.2 Abruf von Salden

Saldenabrufe sollten in zwei Situationen verwendet werden:

(a) Abfragen eines aktuellen Saldo ohne Umsatzabruf, wenn das Kreditinstitut aktu-
elle Saldeninformationen anbietet

(b) Abfragen von Zusatzinformationen wie z. B. dem verfügbaren Betrag, wenn das
Institut die Saldeninformationen nicht in der UPD-Erweiterung, kontobezo-
gen im Element AcctBal komplett liefert. Dies wird durch das Institut auch
durch das Flag BalComplete gekennzeichnet.

Zum Saldenabruf wird folgender Geschäftsvorfall verwendet:

HKSAL: Saldenabfrage

Ein Kundenprodukt soll die folgende Information aus dem Datenelement ,Erweite-
rung, kontobezogen“ berücksichtigen:

<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th rowspan="2">Version: 3.0-FV</th>
<th rowspan="2">Kapitel: F</th>
</tr>
<tr>
<th>Dokument:</th>
<th>Formals</th>
</tr>
<tr>
<td>Kapitel:<br>Abschnitt:</td>
<td>FinTS Prozesse Buchstabe A</td>
<td>Stand: 06.10.2017</td>
<td>Seite: 103</td>
</tr>
</table>


Version 01:00: BalStatAct

Basierend auf dieser Information muss ein Kundenprodukt folgendermaßen reagie-
ren:


<table>
<tr>
<td>BalStatAct</td>
<td>Wird über dieses Element mitgeteilt, dass der aktuelle Saldo in den übermittelten Umsätzen dem gebuchten Saldo bzw. dem Saldo der vorgemerkten Umsätze ent- spricht, darf das Kundenprodukt keine separate Sal- denabfrage einreichen, um den aktuellen Saldo noch- mals zu erhalten. Ausnahme: die Saldenabfrage wird benötigt, um andere der in HKSAL definierten Werte zu ermitteln, die nicht in AcctBal der UPD-Erweiterung geliefert werden.</td>
</tr>
</table>


### F.3.3 Abruf von Beständen

Bestandsabrufe sollten nur beim erstmaligen Einrichten eines Kundenprodukts, bei
Änderungen in den Beständen oder auf expliziten Wunsch eines Benutzers durch-
geführt werden.

Die einzelnen Bestände sind mit Ihren Segmentkennungen im Element Inventory
definiert.

Ein Kundenprodukt soll die folgende Information aus dem Datenelement Erweite-
rung, kontobezogen berücksichtigen:

Version 01:00: Inventory

Basierend auf dieser Information muss ein Kundenprodukt folgendermaßen reagie-
ren:


<table>
<tr>
<td>Inventory</td>
<td>Ein Kreditinstitut kann hiermit eine Liste der vorhande- nen Bestände eines Benutzers an das Kundenprodukt melden.<br>Ein Kundenprodukt darf nur Bestandsgeschäftsvorfälle einreichen, für die auch aktive Bestände gemeldet sind.<br>Ausnahmen: es soll z. B. die Änderung oder Löschung in einem Bestand durchgeführt werden; dann ist die Abholung des aktuellen Bestands durch die Spezifikati- on als obligatorisch festgelegt. Gleiches gilt auch bei technischen Problemen wie z. B. Timeouts.</td>
</tr>
</table>


## F.3.4 Abruf von SEPA-Kontoverbindungsdaten

Der Abruf von SEPA-Kontoverbindungen wird benötigt, um IBAN und BIC zu einer
nationalen Kontoverbindung zu erhalten. Mit HIUPD#6 kann die IBAN zu einer Kon-
toverbindung einfacher mitgeteilt werden. Da der BIC der Auftraggeber-
Kontoverbindung in der UPD-Erweiterung, kontobezogen verpflichtend enthal-
ten ist, wird der Geschäftsvorfall SEPA-Kontoverbindung anfordern (HKSPA)
für die Abfrage nicht mehr benötigt.

In diesem Fall sollte ein Kreditinstitut den HKSPA aus der Liste der erlaubten Ge-
schäftsvorfälle in den UPD des Benutzers entfernen.

<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: F</td>
<td>Version: 3.0-FV</td>
<td>Financial Transaction Services (FinTS) Dokument: Formals</td>
</tr>
<tr>
<td>Seite:<br>104</td>
<td>Stand: 06.10.2017</td>
<td>Kapitel: FinTS Prozesse<br>Abschnitt:<br>Buchstabe A</td>
</tr>
</table>


Das Parametersegment HISPAS kann jedoch in den BPD erhalten bleiben, um z. B.
die zugelassenen pain messages beschreiben zu können.

Ein Kundenprodukt muss den BIC aus der UPD-Erweiterung entsprechend berück-
sichtigen. Weitere Vorgaben bestehen nicht, da der HKSPA ohne Eintrag in den UPD
ohnehin nicht mehr eingereicht werden darf.


## F.3.5 Anzeige der verfügbaren TAN-Medien

Ein Abruf der TAN-Medien erfolgt, um die benötigten Parameter zur Unterstützung
eines Sicherheitsverfahrens zu erhalten.

Zum Abruf der TAN-Medien wird folgender Geschäftsvorfall verwendet:

Anzeige der verfügbaren TAN-Medien (HKTAB)

Ein Kundenprodukt sollte bei einem generellen Bestandsabruf das Datenelement
„TAN-Medium-Klasse“ mit A = Alle Medien belegen, um nicht unnötigerweise
mehrere HKTAB-Geschäftsvorfälle einreichen zu müssen.

HKTAB ist auch in der Bestandsverwaltung Inventory enthalten, so dass ein Kun-
denprodukt ggf. informiert wird, falls die TAN-Medien sich ändern.

<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th rowspan="2">Version: 3.0-FV</th>
<th rowspan="2">Kapitel: F</th>
</tr>
<tr>
<th>Dokument:</th>
<th>Formals</th>
</tr>
<tr>
<td>Kapitel:<br>Abschnitt:</td>
<td>Buchstabe A<br>Data Dictionary</td>
<td>Stand:<br>06.10.2017</td>
<td>Seite: 105</td>
</tr>
</table>


# G. DATA DICTIONARY

A


## Anzahl benötigter Signaturen

Anzahl der Signaturen, die zur Ausführung eines Geschäftsvorfalls als erfor-
derlich definiert ist.

Falls 0 angegeben ist, handelt es sich um einen nicht signierungspflichtigen
Geschäftsvorfall, der auch über einen anonymen Zugang ohne Signierungs-
möglichkeit ausgeführt werden kann.

Falls die Anzahl der benötigten Signaturen größer als 1 ist, bedeutet dies,
dass dieser Geschäftsvorfall zusätzlich von mindestens einem anderen be-
rechtigten Benutzer signiert werden muss, über dessen Identität in den UPD
jedoch nichts ausgesagt wird.

In bestimmten Fällen ist die Anzahl der Signaturen durch die Art des Ge-
schäftsvorfalls vorgegeben (z. B. sind bei Keymanagement-Aufträgen nicht
mehrere Signaturen möglich).


<table>
<tr>
<td>Typ:</td>
<td>DE</td>
</tr>
<tr>
<td>Format:</td>
<td>num</td>
</tr>
<tr>
<td>Länge:</td>
<td>..2</td>
</tr>
<tr>
<td>Version:</td>
<td>1</td>
</tr>
</table>


## Anzahl Geschäftsvorfallsarten

Maximale Anzahl an Geschäftsvorfallsarten, die pro Nachricht zulässig ist.

Der Wert ,0' gibt an, dass keine Restriktionen bzgl. der Anzahl an Ge-
schäftsvorfallsarten bestehen.


<table>
<tr>
<td>Typ:</td>
<td>DE</td>
</tr>
<tr>
<td>Format:</td>
<td>num</td>
</tr>
<tr>
<td>Länge:</td>
<td>..3</td>
</tr>
<tr>
<td>Version:</td>
<td>1</td>
</tr>
</table>


## Anzahl Signaturen mindestens

Mindestanzahl der Signaturen, die für einen Geschäftsvorfall als erforderlich
definiert ist.

Vom Kreditinstitut wird immer die Minimalanforderung an einen Geschäfts-
vorfall mitgeteilt, d. h. '0', wenn der Geschäftsvorfall auch über den anony-
men Zugang angeboten wird, ansonsten mindestens '1', da Aufträge von
Kunden immer signiert werden müssen.

Die für Kunden jeweils genaue Angabe der Signaturanzahl ergibt sich in den
UPD aus dem DE ,,Anzahl benötigter Signaturen“. Dabei muss die in den
UPD angegebene Signaturanzahl größer oder gleich der in den BPD ange-
gebene Anzahl sein. Für Institute, die keine UPD unterstützen, bedeutet
dies, dass der Eintrag '0' in den BPD nur für Nichtkunden gilt und für Kunden
als 'mindestens 1' zu interpretieren ist.

Der Wert gilt für alle Signaturverfahren.

<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: F</td>
<td>Version: 3.0-FV</td>
<td>Financial Transaction Services (FinTS) Dokument: Formals</td>
</tr>
<tr>
<td>Seite:<br>106</td>
<td>Stand:<br>06.10.2017</td>
<td>Kapitel: Data Dictionary<br>Abschnitt: Buchstabe B</td>
</tr>
</table>


<table>
<tr>
<td>Typ:</td>
<td>DE</td>
</tr>
<tr>
<td>Format:</td>
<td>num</td>
</tr>
<tr>
<td>Länge:</td>
<td>1</td>
</tr>
<tr>
<td>Version:</td>
<td>1</td>
</tr>
</table>


## Aufsetzpunkt

Information darüber, wie die Beantwortung des Kundenauftrags an einem
bestimmten Punkt kontrolliert beendet und aufgesetzt werden kann, falls die
Rückmeldung des Kreditinstituts nicht in einem einzigen Auftragssegment er-
folgen kann (s. Kap. B.6.3).


<table>
<tr>
<td>Typ:</td>
<td>DE</td>
</tr>
<tr>
<td>Format:</td>
<td>an</td>
</tr>
<tr>
<td>Länge:</td>
<td>..35</td>
</tr>
<tr>
<td>Version:</td>
<td>1</td>
</tr>
</table>


# B


## Benutzerkennung

Eindeutig vergebene Kennung, anhand deren die Identifizierung des Benut-
zers erfolgt. Die Vergabe obliegt dem Kreditinstitut. Das Kreditinstitut hat zu
gewährleisten, dass die Benutzerkennung institutsweit eindeutig ist. Sie kann
beliebige Informationen enthalten, darf aber bei Verwendung des RAH- oder
RDH-Verfahrens aus Sicherheitsgründen nicht aus benutzer- oder kreditinsti-
tutsspezifischen Merkmalen hergeleitet werden.


<table>
<tr>
<td>Typ:</td>
<td>DE</td>
</tr>
<tr>
<td>Format:</td>
<td>id</td>
</tr>
<tr>
<td>Länge:</td>
<td>#</td>
</tr>
<tr>
<td>Version:</td>
<td>1</td>
</tr>
</table>


## Benutzername

Name des Benutzers. Diese Information dient insbesondere dazu, den Be-
nutzer im Kundenprodukt mit seinem Namen persönlich ansprechen zu kön-
nen.


<table>
<tr>
<td>Typ:</td>
<td>DE</td>
</tr>
<tr>
<td>Format:</td>
<td>an</td>
</tr>
<tr>
<td>Länge:</td>
<td>..35</td>
</tr>
<tr>
<td>Version:</td>
<td>1</td>
</tr>
</table>


## Betreff

Thema einer Textnachricht (Betreffzeile).


<table>
<tr>
<td>Typ:</td>
<td>DE</td>
</tr>
<tr>
<td>Format:</td>
<td>an</td>
</tr>
<tr>
<td>Länge:</td>
<td>..35</td>
</tr>
<tr>
<td>Version:</td>
<td>1</td>
</tr>
</table>


<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th rowspan="2">Version: 3.0-FV</th>
<th rowspan="2">Kapitel: F</th>
</tr>
<tr>
<th>Dokument:</th>
<th>Formals</th>
</tr>
<tr>
<td>Kapitel: Abschnitt:</td>
<td>Data Dictionary Buchstabe B</td>
<td>Stand: 06.10.2017</td>
<td>Seite: 107</td>
</tr>
</table>


### Bezugsdatenelement

Die Position des Datenelements bzw. Gruppendatenelements, auf das sich
der Rückmeldungscode bezieht (z. B. die Position des fehlerhaften Elemen-
tes bei Syntaxfehlern).

Bei Rückmeldecodes, die sich auf eine Nachricht oder ein Segment (Auftrag)
beziehen, darf dieses DE nicht belegt werden.


![](figures/115.1)


Die Angabe des Bezugsdatenelements erlaubt u.U. eine au-
tomatische Reaktion des Kundenproduktes. So kann bspw.
bei fehlerhaften Eingaben des Kunden direkt auf das betref-
fende Eingabefeld positioniert werden.


#### Die Referenzierung erfolgt

• bei DE durch die Position

· bei GD durch die Position der DEG und die Position des GD (die beiden
Werte sind durch Komma getrennt)


#### Position des DE:

Position des DE = Anzahl der vorstehenden DE-Trennzeichen + 1.

Die Anzahl der vorstehenden DE-Trennzeichen ist gleich der Anzahl der vor-
stehenden DE + Anzahl der vorstehenden DEGs (GD sind nicht separat zu
zählen, sondern gehen in die DEGs ein). Entwertete Pluszeichen sind nicht
zu zählen.


##### Position des GD innerhalb einer DEG:

Position des GD = Anzahl der vorstehenden GD-Trennzeichen innerhalb der
DEG + 1


##### Beispiele:

Segmentkopf+DE+GD:GD:GD:GD+DE+GD:GD' : 4

Segmentkopf+DE+GD:GD:GD:GD+DE+GD:GD' : 3,4

Segmentkopf+DE+GD:GD:GD:GD+DE+GD:GD' : 5,2


<table>
<tr>
<td>Typ:</td>
<td>DE</td>
</tr>
<tr>
<td>Format:</td>
<td>an</td>
</tr>
<tr>
<td>Länge:</td>
<td>..7</td>
</tr>
<tr>
<td>Version:</td>
<td>1</td>
</tr>
</table>


## Bezugsnachricht

Eindeutige Referenz für Kundennachrichten. Die eindeutige Referenzierung
erfolgt anhand der Dialog-ID und der Nachrichtennummer der Kundennach-
richt. Falls auf eine Dialoginitialisierungsnachricht des Kunden referenziert
werden soll, ist nicht die vom Kunden übermittelte Dialog-ID (0), sondern die
vom Kreditinstitut neu vergebene Dialog-ID einzustellen.

<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: F</td>
<td>Version: 3.0-FV</td>
<td>Financial Transaction Services (FinTS) Dokument: Formals</td>
</tr>
<tr>
<td>Seite:<br>108</td>
<td>Stand: 06.10.2017</td>
<td>Kapitel: Data Dictionary<br>Abschnitt: Buchstabe B</td>
</tr>
</table>


Es darf nur auf Nachrichten des dialogführenden Benutzers referenziert wer-
den. Eine explizite Angabe der Benutzerkennung als Referenzierungskriteri-
um ist nicht erforderlich, da diese bereits im Signaturkopf spezifiziert wurde.


<table>
<tr>
<th>Nr.</th>
<th>Name</th>
<th>Ver- sion</th>
<th>Typ</th>
<th>For- mat</th>
<th>Län- ge</th>
<th>Sta- tus</th>
<th>An- zahl</th>
<th>Restriktionen</th>
</tr>
<tr>
<td>1</td>
<td>Dialog-ID</td>
<td>1</td>
<td>DE</td>
<td>id</td>
<td>#</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>2</td>
<td>Nachrichten- nummer</td>
<td>1</td>
<td>DE</td>
<td>num</td>
<td>..4</td>
<td>M</td>
<td>1</td>
<td>&gt;0</td>
</tr>
</table>


<table>
<tr>
<td>Typ:</td>
<td>DEG</td>
</tr>
<tr>
<td>Format:</td>
<td></td>
</tr>
<tr>
<td>Länge:</td>
<td></td>
</tr>
<tr>
<td>Version:</td>
<td>1</td>
</tr>
</table>


# Bezugssegment

Sofern sich ein Kreditinstitutssegment auf ein bestimmtes Kundensegment
bezieht (z. B. Antwortrückmeldung auf einen Kundenauftrag) hat das Kredit-
institut die Segmentnummer des Segments der Kundennachricht einzustel-
len, auf das sich das aktuelle Segment bezieht (s. DE ,,Segmentnummer“). In
Zusammenhang mit den Angaben zur Bezugsnachricht aus dem Nachrich-
tenkopf ist hierdurch eine eindeutige Referenz auf das Segment einer Kun-
dennachricht möglich.

Falls die Angabe eines Bezugssegments erforderlich ist, ist dieses bei der
Formatbeschreibung eines Kreditinstitutsegments angegeben.


<table>
<tr>
<td>Typ:</td>
<td>DE</td>
</tr>
<tr>
<td>Format:</td>
<td>num</td>
</tr>
<tr>
<td>Länge:</td>
<td>..3</td>
</tr>
<tr>
<td>Version:</td>
<td>1</td>
</tr>
</table>


# Bis Datum

Endedatum eines Zeitraums.

Durch die Eingabe von Von- und Bis-Datum kann ein Zeitraum eingegrenzt
werden, für den Informationseinträge vom Kreditinstitut rückzumelden sind.


<table>
<tr>
<td>Typ:</td>
<td>DE</td>
</tr>
<tr>
<td>Format:</td>
<td>dat</td>
</tr>
<tr>
<td>Länge:</td>
<td>#</td>
</tr>
<tr>
<td>Version:</td>
<td>1</td>
</tr>
</table>


## Bis Kreditinstitutskennung

Ende eines Bereichs von Kreditinstitutskennungen (s. auch „Von Kreditinsti-
tutskennung“)

<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th rowspan="2">Version: 3.0-FV</th>
<th rowspan="2">Kapitel: F</th>
</tr>
<tr>
<th>Dokument:</th>
<th>Formals</th>
</tr>
<tr>
<td>Kapitel:<br>Abschnitt:</td>
<td>Data Dictionary Buchstabe D</td>
<td>Stand: 06.10.2017</td>
<td>Seite: 109</td>
</tr>
</table>


<table>
<tr>
<td>Typ:</td>
<td>DEG</td>
</tr>
<tr>
<td>Format:</td>
<td>kik</td>
</tr>
<tr>
<td>Länge:</td>
<td>#</td>
</tr>
<tr>
<td>Version:</td>
<td>2</td>
</tr>
</table>


### BPD-Version

Es handelt sich um eine kreditinstitutsseitig vergebene Versionsnummer der
Bankparameterdaten (BPD), die den jeweiligen Stand der instituts-
spezifischen Unterstützung des Systems kennzeichnet (bei jeder für das
Kundensystem relevanten Änderung des Kreditinstitutssystems werden neue
BPD mit einer neuen BPD-Versionsnummer kreditinstitutsseitig bereitge-
stellt).

Diese BPD-Versionsnummer ist unabhängig von der Version des BPD-
Nachrichtenformats, die im Nachrichtenkopf eingestellt ist und lediglich das
syntaktische Format der Nachricht, nicht jedoch deren Inhalt kennzeichnet.


<table>
<tr>
<td>Typ:</td>
<td>DE</td>
</tr>
<tr>
<td>Format:</td>
<td>num</td>
</tr>
<tr>
<td>Länge:</td>
<td>..3</td>
</tr>
<tr>
<td>Version:</td>
<td>1</td>
</tr>
</table>


D


# Datum

Datumsangabe, zur Bestimmung eines Zeitpunktes.


<table>
<tr>
<td>Typ:</td>
<td>DE</td>
</tr>
<tr>
<td>Format:</td>
<td>dat</td>
</tr>
<tr>
<td>Länge:</td>
<td>#</td>
</tr>
<tr>
<td>Version:</td>
<td>1</td>
</tr>
</table>


# Dialog-ID

Die Dialog-ID dient der eindeutigen Zuordnung einer Nachricht zu einem
FinTS-Dialog. Die erste Kundennachricht (Dialoginitialisierung) enthält als Di-
alog-ID den Wert 0. In der ersten Antwortnachricht wird vom Kreditinstitut ei-
ne Dialog-ID vorgegeben, die für alle nachfolgenden Nachrichten dieses Dia-
logs einzustellen ist. Es ist Aufgabe des Kreditinstituts, dafür zu sorgen, dass
diese Dialog-ID dialogübergreifend und systemweit eindeutig ist.


<table>
<tr>
<td>Typ:</td>
<td>DE</td>
</tr>
<tr>
<td>Format:</td>
<td>id</td>
</tr>
<tr>
<td>Länge:</td>
<td>#</td>
</tr>
<tr>
<td>Version:</td>
<td>1</td>
</tr>
</table>


# Dialogsprache

Über dieses DE spezifiziert der Kunde die Sprache, in der er im laufenden
Dialog mit dem Kreditinstitut kommunizieren möchte. Rückmeldungen und
Kreditinstitutsmeldungen werden (soweit kreditinstitutsseitig unterstützt) in
der zuvor spezifizierten Sprache an den Kunden übermittelt. Damit ver-
bunden wird ein zugehöriger FinTS-Basiszeichensatz (s. Kap. B.1), der sich
durch einen ISO 8859-Codeset und einen ISO 8859-Subset definiert, aus-
gewählt. Die Definition des Subsets ist den Anlagen (Kap. I.3) zu entneh-

<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: F</td>
<td>Version: 3.0-FV</td>
<td>Financial Transaction Services (FinTS) Dokument: Formals</td>
</tr>
<tr>
<td>Seite:<br>110</td>
<td>Stand: 06.10.2017</td>
<td>Kapitel: Data Dictionary<br>Abschnitt:<br>Buchstabe E</td>
</tr>
</table>


men. Der Codeset soll ermöglichen, zu einem späteren Zeitpunkt evtl. auch
nicht-lateinische Zeichensätze zuzulassen.

Codierung:

0: Standard

1: Deutsch, Code ,de' (German), Subset Deutsch, Codeset 1 (Latin 1)

2: Englisch, Code ,en' (English), Subset Englisch, Codeset 1 (Latin 1)

3: Französisch, Code ,fr' (French), Subset Französisch, Codeset 1 (Latin 1)


<table>
<tr>
<td>Typ:</td>
<td>DE</td>
</tr>
<tr>
<td>Format:</td>
<td>code</td>
</tr>
<tr>
<td>Länge:</td>
<td>..3</td>
</tr>
<tr>
<td>Version:</td>
<td>2</td>
</tr>
</table>


E


## Erlaubte Geschäftsvorfälle

Information darüber, ob der Kunde zur Ausführung des jeweiligen Ge-
schäftsvorfalls zugelassen ist und wie viele Signaturen hierzu mindestens er-
forderlich sind. Ferner können für jeden Geschäftsvorfall Einzelauftragslimite
angegeben werden, sofern dies bankfachlich möglich ist. Die Reihenfolge
der Geschäftsvorfälle ist unerheblich.


<table>
<tr>
<th>Nr.</th>
<th>Name</th>
<th>Ver- sion</th>
<th>Typ</th>
<th>For- mat</th>
<th>Län- ge</th>
<th>Sta- tus</th>
<th>An- zahl</th>
<th>Restriktionen</th>
</tr>
<tr>
<td>1</td>
<td>Geschäftsvorfall</td>
<td>1</td>
<td>DE</td>
<td>an</td>
<td>..6</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>2</td>
<td>Anzahl benötig- ter Signaturen</td>
<td>1</td>
<td>DE</td>
<td>num</td>
<td>..2</td>
<td>M</td>
<td>1</td>
<td>0, 1, 2, 3</td>
</tr>
<tr>
<td>3</td>
<td>Limitart</td>
<td>2</td>
<td>DE</td>
<td>code</td>
<td>1</td>
<td>O</td>
<td>1</td>
<td>E, T, W, M, Z</td>
</tr>
<tr>
<td>4</td>
<td>Limitbetrag</td>
<td>1</td>
<td>DEG</td>
<td>btg</td>
<td>#</td>
<td>C</td>
<td>1</td>
<td>O: Limitart &lt;&gt; „Z“ N: sonst</td>
</tr>
<tr>
<td>5</td>
<td>Limit-Tage</td>
<td>1</td>
<td>DE</td>
<td>num</td>
<td>..3</td>
<td>C</td>
<td>1</td>
<td>&gt;0<br>O: Limitart = ,,Z" N: sonst</td>
</tr>
</table>


<table>
<tr>
<td>Typ:</td>
<td>DEG</td>
</tr>
<tr>
<td>Format:</td>
<td></td>
</tr>
<tr>
<td>Länge:</td>
<td></td>
</tr>
<tr>
<td>Version:</td>
<td>2</td>
</tr>
</table>


### Erweiterung, allgemein

Zwischen Kreditinstitut und Kunde bilateral vereinbarte Erweiterung der all-
gemeinen Userparameter.

<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th rowspan="2">Version: 3.0-FV</th>
<th rowspan="2">Kapitel: F</th>
</tr>
<tr>
<th>Dokument:</th>
<th>Formals</th>
</tr>
<tr>
<td>Kapitel:<br>Abschnitt:</td>
<td>Buchstabe F<br>Data Dictionary</td>
<td>Stand: 06.10.2017</td>
<td>Seite: 111</td>
</tr>
</table>


Typ:

DE


<table>
<tr>
<td>Format:</td>
<td>an</td>
</tr>
<tr>
<td>Länge:</td>
<td>..2048</td>
</tr>
<tr>
<td>Version:</td>
<td>1</td>
</tr>
</table>


## Erweiterung, kontobezogen

Das Datenelement wurde ursprünglich als bilateral zwischen Kreditinstitut
und Kunde vereinbarte Erweiterung der kontobezogenen Userparameter
vorgesehen. Diese Verwendung ist mit Einführung der DK-weit einheitlichen
Festlegung nicht mehr zulässig. Es wird stattdessen auf eine definierte
Struktur verwiesen (vgl. Kapitel E.3.1ff).

Für die Struktur wird je Version eine eigene JSON Schema-Datei definiert,
mit deren Hilfe automatisiert Wandlungen durchgeführt werden können.


<table>
<tr>
<td>Typ:</td>
<td>DE</td>
</tr>
<tr>
<td>Format:</td>
<td>an</td>
</tr>
<tr>
<td>Länge:</td>
<td>..2048</td>
</tr>
<tr>
<td>Version:</td>
<td>1</td>
</tr>
</table>


F


### Freitextmeldung

Inhalt einer Freitextinformation

Die maximale Länge der Freitextmeldung ist den BPD zu entnehmen. Mel-
dungen, deren Länge diesen Wert übersteigen, werden abgelehnt. Die Daten
dürfen nicht um führende oder nachfolgende Leerzeichen gekürzt werden.


<table>
<tr>
<td>Typ:</td>
<td>DE</td>
</tr>
<tr>
<td>Format:</td>
<td>txt</td>
</tr>
<tr>
<td>Länge:</td>
<td>.2048</td>
</tr>
<tr>
<td>Version:</td>
<td>1</td>
</tr>
</table>


### Filterfunktion

Falls das Übertragungsverfahren eine Umwandlung der Nachricht in eine
7 Bit-Zeichendarstellung erfordert (z. B. Internet), so ist hier das anzuwen-
dende Filterverfahren anzugeben. Die Nachricht ist stets komplett zu filtern,
auch wenn eine Filterung nicht notwendig wäre, da bspw. keine binären Da-
ten enthalten sind. Ein Kreditinstitut darf jeweils nur eine Filterfunktion unter-
stützen.

Codierung:

MIM: MIME Base 64

UUE: Uuencode/Uudecode


<table>
<tr>
<td>Typ:</td>
<td>DE</td>
</tr>
<tr>
<td>Format:</td>
<td>an</td>
</tr>
<tr>
<td>Länge:</td>
<td>3</td>
</tr>
<tr>
<td>Version:</td>
<td>1</td>
</tr>
</table>


<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: F</td>
<td>Version: 3.0-FV</td>
<td>Financial Transaction Services (FinTS) Dokument: Formals</td>
</tr>
<tr>
<td>Seite:<br>112</td>
<td>Stand:<br>06.10.2017</td>
<td>Kapitel: Data Dictionary<br>Abschnitt:<br>Buchstabe G</td>
</tr>
</table>


G


### Geschäftsvorfall

Geschäftsvorfälle, für deren Ausführung der Benutzer berechtigt ist. Hierzu
gehören neben den Auftragssegmenten mit der Segmentart „Geschäftsvor-
fall" auch die Segmente der Key-Management-Nachrichten. Einzustellen ist
jeweils die Segmentkennung des Kundensegments.


<table>
<tr>
<td>Typ:</td>
<td>DE</td>
</tr>
<tr>
<td>Format:</td>
<td>an</td>
</tr>
<tr>
<td>Länge:</td>
<td>..6</td>
</tr>
<tr>
<td>Version:</td>
<td>1</td>
</tr>
</table>


H


### HBCI-Version

Version der HBCI-/FinTS-Schnittstellenspezifikation, die der jeweiligen Rea-
lisierung zugrunde liegt.

HBCI- bzw. FinTS-Versionen, die vor Version 2.0.1 veröffentlicht wurden,
werden kreditinstitutsseitig nicht unterstützt.

Ein geregelter Dialog ist nur zwischen Systemen möglich, die mit derselben
HBCI-/FinTS-Version arbeiten. Stimmt die vom Kunden übermittelte HBCI-
/FinTS-Version nicht mit einer der vom Kreditinstitut in den BPD mitgeteilten
unterstützten HBCI-/FinTS-Versionen überein, so muss der Dialog vom Kre-
ditinstitut beendet werden. Innerhalb eines Dialoges dürfen nicht Nachrichten
unterschiedlicher HBCI-/FinTS-Versionen gesendet werden.

Segment- und HBCI-/FinTS-Versionen werden unabhängig voneinander ge-
führt. Innerhalb eines HBCI-/FinTS-Dialoges dürfen nur Versionen administ-
rativer Segmente gesendet werden, die der angegebenen HBCI-/FinTS-
Version entsprechen. Im Rahmen einer HBCI-/FinTS-Version wird eine Liste
der zugehörigen Segmentversionen veröffentlicht (s. [Messages], Anlagen).
Weiterhin werden in dieser Liste auch die zusätzlich noch unterstützten Se-
gmentversionen genannt.

Der Zeitpunkt der Unterstützung einer neuen HBCI-/FinTS-Version kann zwi-
schen den Kreditinstituten variieren.

Zulässige Werte:

Version 2.0.1 : 201 (Spezifikationsstatus: obsolet)

Version 2.1 : 210 (Spezifikationsstatus: obsolet)

Version 2.2 : 220 (Spezifikationsstatus: obsolet)

Version 3.0 : 300


<table>
<tr>
<td>Typ:</td>
<td>DE</td>
</tr>
<tr>
<td>Format:</td>
<td>num</td>
</tr>
<tr>
<td>Länge:</td>
<td>..3</td>
</tr>
<tr>
<td>Version:</td>
<td>1</td>
</tr>
</table>


<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th rowspan="2">Version: 3.0-FV</th>
<th rowspan="2">Kapitel: F</th>
</tr>
<tr>
<th>Dokument:</th>
<th>Formals</th>
</tr>
<tr>
<td>Kapitel:<br>Abschnitt:</td>
<td>Data Dictionary<br>Buchstabe I</td>
<td>Stand: 06.10.2017</td>
<td>Seite: 113</td>
</tr>
</table>


<!-- PageNumber: I -->


# IBAN

IBAN


<table>
<tr>
<td>Typ:</td>
<td>DE</td>
</tr>
<tr>
<td>Format:</td>
<td>an</td>
</tr>
<tr>
<td>Länge:</td>
<td>..34</td>
</tr>
<tr>
<td>Version:</td>
<td>1</td>
</tr>
</table>


K


## Kommunikationsadresse

Beim Zugang über T-Online ist die Gateway-Seite als numerischer Wert (oh-
ne die Steuerzeichen * und #) einzustellen.

Beim Zugang über TCP/IP ist die IP-Adresse als alphanumerischer Wert (z.
B. '123.123.123.123') einzustellen.

Beim Zugang über https ist die Adresse des Servlets als alphanumerischer
Wert (z. B. [,,https://www.xyz.de:7000/Servlet"](https://www.xyz.de:7000/Servlet)) einzustellen.


<table>
<tr>
<td>Typ:</td>
<td>DE</td>
</tr>
<tr>
<td>Format:</td>
<td>an</td>
</tr>
<tr>
<td>Länge:</td>
<td>..512</td>
</tr>
<tr>
<td>Version:</td>
<td>1</td>
</tr>
</table>


## Kommunikationsadressenzusatz

Beim Zugang über T-Online ist der Regionalbereich einzustellen (,00' für ein
bundesweites Angebot). Beim Zugang über TCP/IP und https wird das Feld
nicht belegt.


<table>
<tr>
<td>Typ:</td>
<td>DE</td>
</tr>
<tr>
<td>Format:</td>
<td>an</td>
</tr>
<tr>
<td>Länge:</td>
<td>..512</td>
</tr>
<tr>
<td>Version:</td>
<td>1</td>
</tr>
</table>


## Kommunikationsdienst

Unterstütztes Kommunikationsverfahren (Protokollstack).

Zur Zeit unterstützte Kommunikationsverfahren:

1: T-Online (mit FinTS V3.0 nicht mehr unterstützt)

2: TCP/IP (Protokollstack SLIP/PPP)

3: https1 (verwendet im Sicherheitsverfahren PIN/TAN)

<!-- PageFooter: 1 Das SSL-Protokoll ist für https nicht mehr zugelassen (vgl. Kap. I.4) -->
<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: F</td>
<td>Version: 3.0-FV</td>
<td>Financial Transaction Services (FinTS) Dokument: Formals</td>
</tr>
<tr>
<td>Seite:<br>114</td>
<td>Stand: 06.10.2017</td>
<td>Kapitel: Data Dictionary<br>Abschnitt: Buchstabe K</td>
</tr>
</table>


<table>
<tr>
<td>Typ:</td>
<td>DE</td>
</tr>
<tr>
<td>Format:</td>
<td>code</td>
</tr>
<tr>
<td>Länge:</td>
<td>..2</td>
</tr>
<tr>
<td>Version:</td>
<td>2</td>
</tr>
</table>


# Kommunikationsparameter

Die Kommunikationsparameter enthalten Informationen für den Aufbau der
Transportverbindung.


<table>
<tr>
<th>Nr.</th>
<th>Name</th>
<th>Ver- sion</th>
<th>Typ</th>
<th>For- mat</th>
<th>Län- ge</th>
<th>Sta- tus</th>
<th>An- zahl</th>
<th>Restriktionen</th>
</tr>
<tr>
<td>1</td>
<td>Kommunikati- onsdienst</td>
<td>2</td>
<td>DE</td>
<td>num</td>
<td>..2</td>
<td>M</td>
<td>1</td>
<td>1,2,3</td>
</tr>
<tr>
<td>2</td>
<td>Kommunikati- onsadresse</td>
<td>1</td>
<td>DE</td>
<td>an</td>
<td>..512</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>3</td>
<td>Kommunikati- onsadres- senzusatz</td>
<td>1</td>
<td>DE</td>
<td>an</td>
<td>..512</td>
<td>C</td>
<td>1</td>
<td>M: ,Kommunikations- dienst = 1 N: sonst</td>
</tr>
<tr>
<td>4</td>
<td>Filterfunktion</td>
<td>1</td>
<td>DE</td>
<td>an</td>
<td>3</td>
<td>C</td>
<td>1</td>
<td>MIM, UUE M: ,Kommunikations- dienst = 2 N: sonst</td>
</tr>
<tr>
<td>5</td>
<td>Version der Fil- terfunktion</td>
<td>1</td>
<td>DE</td>
<td>num</td>
<td>..3</td>
<td>C</td>
<td>1</td>
<td>O: ,Filterfunktion' belegt N: sonst</td>
</tr>
</table>


<table>
<tr>
<td>Typ:</td>
<td>DEG</td>
</tr>
<tr>
<td>Format:</td>
<td></td>
</tr>
<tr>
<td>Länge:</td>
<td></td>
</tr>
<tr>
<td>Version:</td>
<td>2</td>
</tr>
</table>


## Kontoart

Klassifizierung der Konten. Innerhalb der vorgegebenen Codebereiche sind
kreditinstitutsindividuell bei Bedarf weitere Kontoarten möglich.

Codierung:

1 - 9: Kontokorrent-/Girokonto

10 - 19: Sparkonto

20-29: Festgeldkonto (Termineinlagen)

30 - 39: Wertpapierdepot

40 - 49: Kredit-/Darlehenskonto

50 - 59: Kreditkartenkonto

60 - 69: Fonds-Depot bei einer Kapitalanlagegesellschaft

70 - 79: Bausparvertrag

80 - 89: Versicherungsvertrag

90 - 99: Sonstige (nicht zuordenbar)

<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th rowspan="2">Version: 3.0-FV</th>
<th rowspan="2">Kapitel: F</th>
</tr>
<tr>
<th>Dokument:</th>
<th>Formals</th>
</tr>
<tr>
<td>Kapitel:<br>Abschnitt:</td>
<td>Buchstabe K<br>Data Dictionary</td>
<td>Stand: 06.10.2017</td>
<td>Seite: 115</td>
</tr>
</table>


<table>
<tr>
<td>Typ:</td>
<td>DE</td>
</tr>
<tr>
<td>Format:</td>
<td>num</td>
</tr>
<tr>
<td>Länge:</td>
<td>..2</td>
</tr>
<tr>
<td>Version:</td>
<td>1</td>
</tr>
</table>


# Kontolimit

Kontobezogenes Limit für Verfügungen am Konto.

Die Angabe eines Kontolimits ist kreditinstitutsseitig optional, so dass für den
Kunden ein Limit bestehen kann, auch wenn dieses nicht in die UPD einge-
stellt wurde. Ein kontobezogenes Limit darf nicht gleichzeitig mit geschäfts-
vorfallbezogenen Limiten angegeben werden.


<table>
<tr>
<th>Nr.</th>
<th>Name</th>
<th>Ver- sion</th>
<th>Typ</th>
<th>For- mat</th>
<th>Län- ge</th>
<th>Sta- tus</th>
<th>An- zahl</th>
<th>Restriktionen</th>
</tr>
<tr>
<td>1</td>
<td>Limitart</td>
<td>2</td>
<td>DE</td>
<td>code</td>
<td>1</td>
<td>M</td>
<td>1</td>
<td>E, T, W, M, Z</td>
</tr>
<tr>
<td>2</td>
<td>Limitbetrag</td>
<td>1</td>
<td>DEG</td>
<td>btg</td>
<td>#</td>
<td>C</td>
<td>1</td>
<td>O: Limitart &lt;&gt; ,Z" N: sonst</td>
</tr>
<tr>
<td>3</td>
<td>Limit-Tage</td>
<td>1</td>
<td>DE</td>
<td>num</td>
<td>..3</td>
<td>C</td>
<td>1</td>
<td>&gt;0<br>O: Limitart = ,,Z" N: sonst</td>
</tr>
</table>


<table>
<tr>
<td>Typ:</td>
<td>DEG</td>
</tr>
<tr>
<td>Format:</td>
<td></td>
</tr>
<tr>
<td>Länge:</td>
<td></td>
</tr>
<tr>
<td>Version:</td>
<td>2</td>
</tr>
</table>


# Kontoproduktbezeichnung

Produktbezeichnung des Kontos. Diese Bezeichnung ist vom Kreditinstitut
frei wählbar.


<table>
<tr>
<td>Typ:</td>
<td>DE</td>
</tr>
<tr>
<td>Format:</td>
<td>an</td>
</tr>
<tr>
<td>Länge:</td>
<td>..30</td>
</tr>
<tr>
<td>Version:</td>
<td>1</td>
</tr>
</table>


# Kontoverbindung

Deutsche oder internationale Kontoverbindung, die im Rahmen der Abwick-
lung eines Auftrags benötigt wird.


<table>
<tr>
<td>Typ:</td>
<td>DEG</td>
</tr>
<tr>
<td>Formatkennung:</td>
<td>ktv</td>
</tr>
<tr>
<td>Länge:</td>
<td>#</td>
</tr>
<tr>
<td>Version:</td>
<td>2</td>
</tr>
</table>


# Kontowährung

Angabe der Währung, in der ein Konto geführt wird. Die Währung wird als
ISO-Währungscode angegeben.

Bei Depotkonten kann auf die Angabe der Kontowährung verzichtet werden.

<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: F</td>
<td>Version: 3.0-FV</td>
<td>Financial Transaction Services (FinTS) Dokument: Formals</td>
</tr>
<tr>
<td>Seite:<br>116</td>
<td>Stand:<br>06.10.2017</td>
<td>Kapitel: Data Dictionary<br>Abschnitt:<br>Buchstabe K</td>
</tr>
</table>


<table>
<tr>
<td>Typ:</td>
<td>DE</td>
</tr>
<tr>
<td>Format:</td>
<td>cur</td>
</tr>
<tr>
<td>Länge:</td>
<td>#</td>
</tr>
<tr>
<td>Version:</td>
<td>1</td>
</tr>
</table>


# Kreditinstitutsbezeichnung

Bezeichnung des Kreditinstituts, die vom Kreditinstitut frei wählbar ist.


<table>
<tr>
<td>Typ:</td>
<td>DE</td>
</tr>
<tr>
<td>Format:</td>
<td>an</td>
</tr>
<tr>
<td>Länge:</td>
<td>..60</td>
</tr>
<tr>
<td>Version:</td>
<td>1</td>
</tr>
</table>


# Kreditinstitutskennung

Kennung eines Kreditinstituts.


<table>
<tr>
<td>Typ:</td>
<td>DEG</td>
</tr>
<tr>
<td>Formatkennung</td>
<td>kik</td>
</tr>
<tr>
<td>Länge:</td>
<td>#</td>
</tr>
<tr>
<td>Version:</td>
<td>1</td>
</tr>
</table>


# Kunden-ID

Institutsweit eindeutige Identifikation des Kunden. Die Vergabe obliegt dem
Kreditinstitut. Die Kunden-ID kann beliebige Informationen enthalten. Es
steht dem Kreditinstitut frei, ob es jedem Kunden genau eine Kunden-ID zu-
ordnet oder dem Kunden in Abhängigkeit vom Benutzer jeweils eine unter-
schiedliche Kunden-ID zuordnet.


<table>
<tr>
<td>Typ:</td>
<td>DE</td>
</tr>
<tr>
<td>Format:</td>
<td>id</td>
</tr>
<tr>
<td>Länge:</td>
<td>#</td>
</tr>
<tr>
<td>Version:</td>
<td>1</td>
</tr>
</table>


# Kundensystem-ID

Eindeutige Kennzeichnung des Kundensystems, die in Kombination mit der
Signatur-ID die Validität (Eindeutigkeit) der Signatur sichert.

Die Kundensystem-ID ist nicht eindeutig für das Endgerät (PC), sondern für
die Anwendung auf einem Endgerät, d. h., wenn der Kunde auf einem End-
gerät mit mehreren Homebanking-Anwendungen arbeitet, muss für jede An-
wendung eine eigene Kundensystem-ID geführt werden.

Die Kundensystem-ID ist beim HBCI RAH- / RDH- sowie dem PIN/TAN-
Verfahren erforderlich. Bei der Verwendung von RAH-/RDH-Chipkarten ab
Sicherheitsprofil-Version 3 wird anstatt der Kundensystem-ID die CID der
gesteckten Karte verwendet. Beim HBCI DDV-Verfahren und bei TAN-
Verfahren ist dieses DE mit dem Wert 0 zu belegen.


<table>
<tr>
<td>Typ:</td>
<td>DE</td>
</tr>
<tr>
<td>Format:</td>
<td>id</td>
</tr>
<tr>
<td>Länge:</td>
<td>#</td>
</tr>
<tr>
<td>Version:</td>
<td>1</td>
</tr>
</table>


<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th rowspan="2">Version: 3.0-FV</th>
<th rowspan="2">Kapitel: F</th>
</tr>
<tr>
<th>Dokument:</th>
<th>Formals</th>
</tr>
<tr>
<td>Kapitel:<br>Abschnitt:</td>
<td>Data Dictionary Buchstabe L</td>
<td>Stand: 06.10.2017</td>
<td>Seite: 117</td>
</tr>
</table>


# Kundensystem-Status

Information darüber, ob die Kundensystem-ID erforderlich ist:

Codierung:

0:
Kundensystem-ID wird nicht benötigt (HBCI DDV-Verfahren und
chipkartenbasierte Verfahren ab Sicherheitsprofil-Version 3)

1:
Kundensystem-ID wird benötigt (sonstige HBCI RAH- /
RDH- und PIN/TAN-Verfahren)


<table>
<tr>
<td>Typ:</td>
<td>DE</td>
</tr>
<tr>
<td>Format:</td>
<td>code</td>
</tr>
<tr>
<td>Länge:</td>
<td>1</td>
</tr>
<tr>
<td>Version:</td>
<td>2</td>
</tr>
</table>


L


## Limitart

Information über die Art des geschäftsvorfallbezogenen Limits.

Ein geschäftsvorfallbezogenes Limit kann nur eingestellt werden, wenn nicht
gleichzeitig ein kontobezogenes Limit angegeben wurde. Die Angabe eines
Limits ist kreditinstitutsseitig optional. Daher kann für den Kunden ein Limit
bestehen, auch wenn dieses nicht in die UPD eingestellt wurde.

Codierung:

E: Einzelauftragslimit

T: Tageslimit

W: Wochenlimit

M: Monatslimit

Z: Zeitlimit


<table>
<tr>
<td>Typ:</td>
<td>DE</td>
</tr>
<tr>
<td>Format:</td>
<td>code</td>
</tr>
<tr>
<td>Länge:</td>
<td>1</td>
</tr>
<tr>
<td>Version:</td>
<td>2</td>
</tr>
</table>


## Limitbetrag

Betrag für Userlimit.


<table>
<tr>
<td>Typ:</td>
<td>DEG</td>
</tr>
<tr>
<td>Format:</td>
<td>btg</td>
</tr>
<tr>
<td>Länge:</td>
<td>#</td>
</tr>
<tr>
<td>Version:</td>
<td>1</td>
</tr>
</table>


## Limit-Tage

Anzahl Tage für rollierendes Zeitlimit (Limitart 'Z').

<!-- PageBreak -->


<table>
<tr>
<th>Kapitel: F</th>
<th>Version: 3.0-FV</th>
<th>Financial Transaction Services (FinTS) Dokument: Formals</th>
</tr>
<tr>
<td>Seite:<br>118</td>
<td>Stand:<br>06.10.2017</td>
<td>Kapitel: Data Dictionary<br>Abschnitt: Buchstabe M</td>
</tr>
</table>


<table>
<tr>
<td>Typ:</td>
<td>DE</td>
</tr>
<tr>
<td>Format:</td>
<td>num</td>
</tr>
<tr>
<td>Länge:</td>
<td>..3</td>
</tr>
<tr>
<td>Version:</td>
<td>1</td>
</tr>
</table>


M


# Maximale Anzahl Aufträge

Höchstens zulässige Anzahl an Segmenten der jeweiligen Auftragsart je
Kundennachricht. Übersteigt die Anzahl der vom Kunden übermittelten Seg-
mente pro Auftragsart die zugelassene Maximalanzahl, so wird die gesamte
Nachricht abgelehnt.


<table>
<tr>
<td>Typ:</td>
<td>DE</td>
</tr>
<tr>
<td>Format:</td>
<td>num</td>
</tr>
<tr>
<td>Länge:</td>
<td>..3</td>
</tr>
<tr>
<td>Version:</td>
<td>1</td>
</tr>
</table>


# Maximale Anzahl Einträge

Maximale Anzahl rückzumeldender Einträge bei Abholaufträgen, Kreditinsti-
tutsangeboten oder -informationen (vgl. Kap. B.6.3).


<table>
<tr>
<td>Typ:</td>
<td>DE</td>
</tr>
<tr>
<td>Format:</td>
<td>num</td>
</tr>
<tr>
<td>Länge:</td>
<td>..4</td>
</tr>
<tr>
<td>Version:</td>
<td>1</td>
</tr>
</table>


# Maximale Nachrichtengröße

Obergrenze in Kilobyte (=1024 Byte) für die Nachrichtengröße. Dies kann
kreditinstitutsindividuell je nach technischen Restriktionen bzgl. der Verarbei-
tung umfangreicher Kundennachrichten vorgegeben werden.

Der Wert ,0' gibt an, dass keine Restriktionen bzgl. der Nachrichtengröße
bestehen.

Eingehende Nachrichten, die dekomprimiert und entschlüsselt diese Grenze
überschreiten, können dann abgelehnt werden.


<table>
<tr>
<td>Typ:</td>
<td>DE</td>
</tr>
<tr>
<td>Format:</td>
<td>num</td>
</tr>
<tr>
<td>Länge:</td>
<td>..4</td>
</tr>
<tr>
<td>Version:</td>
<td>1</td>
</tr>
</table>


# Maximaler Timeout-Wert

Zeitraum, nach dem das Kreditinstitut einen Dialog voraussichtlich beenden
wird, sofern keine weiteren Kundennachrichten gesendet wurden. Die Anga-
be erfolgt in Sekunden. Liegt keine Begrenzung vor, kann der Wert ,0' ange-
geben werden.

<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th rowspan="2">Version: 3.0-FV</th>
<th rowspan="2">Kapitel: F</th>
</tr>
<tr>
<th>Dokument:</th>
<th>Formals</th>
</tr>
<tr>
<td>Kapitel:<br>Abschnitt:</td>
<td>Data Dictionary Buchstabe M</td>
<td>Stand: 06.10.2017</td>
<td>Seite: 119</td>
</tr>
</table>


<table>
<tr>
<td>Typ:</td>
<td>DE</td>
</tr>
<tr>
<td>Format:</td>
<td>num</td>
</tr>
<tr>
<td>Länge:</td>
<td>..4</td>
</tr>
<tr>
<td>Version:</td>
<td>1</td>
</tr>
</table>


## Minimaler Timeout-Wert

Zeitraum, nach dem frühestens eine weitere Life-Indikator-Nachricht gesen-
det werden darf. Die Angabe erfolgt in Sekunden. Liegt keine Begrenzung
vor, kann der Wert ,0' angegeben werden.


<table>
<tr>
<td>Typ:</td>
<td>DE</td>
</tr>
<tr>
<td>Format:</td>
<td>num</td>
</tr>
<tr>
<td>Länge:</td>
<td>..4</td>
</tr>
<tr>
<td>Version:</td>
<td>1</td>
</tr>
</table>


## Mischung zulässig

Kennzeichen dafür, ob das Kreditinstitut die Mischung von Sicherheitsverfah-
ren zulässt, sofern es mehrere Sicherheitsverfahren anbietet. Hierunter ist zu
verstehen,

· dass eine Nachricht von mehreren Benutzern mit unterschiedlichen Ver-
fahren signiert wird.

• dass ein Benutzer die Nachrichten eines Dialoges mit verschiedenen Ver-
fahren signiert.

· dass Signatur und Verschlüsselung einer Nachricht mit verschiedenen
Verfahren durchgeführt werden.

. dass zwischen den folgenden Gruppen gemischt werden soll:

\- RAH-7, RAH-9, RDH-3, RDH-5, RDH-6, RDH-7, RDH-8 und RDH-9

\- RAH-10, RDH-2 und RDH-10

\- DDV

\- PIN

Eine Verwendung von Sicherheitsverfahren innerhalb dieser Gruppen gilt
nicht als Mischung.

Ist hier 'N' eingestellt, so sind die genannten Fälle nicht zulässig, d. h. alle
Signaturen und Verschlüsselungen eines Dialoges müssen mit demselben
Sicherheitsverfahren bzw. mit Verfahren aus der gleichen Gruppe vorge-
nommen werden. Ist 'J' eingestellt, so müssen kreditinstitutsseitig alle vorge-
nannten Fälle unterstützt werden.

Falls das Kreditinstitut nur ein Sicherheitsverfahren anbietet, ist 'N' einzustel-
len.


<table>
<tr>
<td>Typ:</td>
<td>DE</td>
</tr>
<tr>
<td>Format:</td>
<td>jn</td>
</tr>
<tr>
<td>Länge:</td>
<td>#</td>
</tr>
<tr>
<td>Version:</td>
<td>1</td>
</tr>
</table>


<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: F</td>
<td>Version: 3.0-FV</td>
<td>Financial Transaction Services (FinTS) Dokument: Formals</td>
</tr>
<tr>
<td>Seite:<br>120</td>
<td>Stand:<br>06.10.2017</td>
<td>Kapitel: Data Dictionary<br>Abschnitt:<br>Buchstabe N</td>
</tr>
</table>


N


## Nachrichtengröße

Größe der Nachricht (nach Verschlüsselung und Komprimierung) in Byte.
Das DE ist mit führenden Nullen auf die vorgegebene feste Länge aufzufül-
len. Dies ist erforderlich, damit die Nachrichtenlänge nicht mit der Länge des
DE variiert.


<table>
<tr>
<td>Typ:</td>
<td>DE</td>
</tr>
<tr>
<td>Format:</td>
<td>dig</td>
</tr>
<tr>
<td>Länge:</td>
<td>12</td>
</tr>
<tr>
<td>Version:</td>
<td>1</td>
</tr>
</table>


### Nachrichtennummer

Information zur Referenzierung von Nachrichten innerhalb eines Dialoges. In
Zusammenhang mit der Dialog-ID und der Kundensystem-ID können Nach-
richten über die Nachrichtennummer auch dialogübergreifend eindeutig refe-
renziert werden. Eine Doppeleinreichungskontrolle ist mit Hilfe der Nachrich-
tennummer nicht möglich.

Mit Hilfe der Nachrichtennummer nummerieren sowohl das Kundensystem
als auch das Kreditinstitutssystem seine Nachrichten unabhängig von-
einander innerhalb eines Dialoges in Einerschritten streng monoton aufstei-
gend. Die Nummerierung beginnt sowohl beim Kunden- als auch beim Kre-
ditinstitutssystem mit der Dialoginitialisierungsnachricht bei '1'. Nachrichten,
deren Nummerierung nicht streng monoton aufsteigend erfolgt ist, werden
institutsseitig bzw. kundenseitig abgelehnt.


<table>
<tr>
<td>Typ:</td>
<td>DE</td>
</tr>
<tr>
<td>Format:</td>
<td>num</td>
</tr>
<tr>
<td>Länge:</td>
<td>..4</td>
</tr>
<tr>
<td>Version:</td>
<td>1</td>
</tr>
</table>


### Name des Kontoinhabers 1

Name des Kontoinhabers.


<table>
<tr>
<td>Typ:</td>
<td>DE</td>
</tr>
<tr>
<td>Format:</td>
<td>an</td>
</tr>
<tr>
<td>Länge:</td>
<td>.27</td>
</tr>
<tr>
<td>Version:</td>
<td>1</td>
</tr>
</table>


### Name des Kontoinhabers 2

Zusätzliche Angaben zum Kontoinhaber.


<table>
<tr>
<td>Typ:</td>
<td>DE</td>
</tr>
<tr>
<td>Format:</td>
<td>an</td>
</tr>
<tr>
<td>Länge:</td>
<td>..27</td>
</tr>
<tr>
<td>Version:</td>
<td>1</td>
</tr>
</table>


<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th rowspan="2">Version: 3.0-FV</th>
<th rowspan="2">Kapitel: F</th>
</tr>
<tr>
<th>Dokument:</th>
<th>Formals</th>
</tr>
<tr>
<td>Kapitel:<br>Abschnitt:</td>
<td>Data Dictionary Buchstabe P</td>
<td>Stand: 06.10.2017</td>
<td>Seite: 121</td>
</tr>
</table>


<!-- PageNumber: P -->


### Produktbezeichnung

Name des Kundenproduktes, mit dem kundenseitig die Nachrichten erzeugt
wurden. Diese Angabe dient dem Kreditinstitut, um Kundenprodukthersteller
gezielt unterstützen zu können.

Die Produktbezeichnung ist verpflichtend mit aussagekräftigen Informationen
über das verwendete Kundenprodukt, nicht eine ggf. verwendete interne
FinTS-/HBCI-Bibliothek, zu füllen, um Support-Anfragen leichter beantworten
zu können.

Kundenprodukte, die nach dem durch die Deutsche Kreditwirtschaft festge-
legten Verfahren registriert sind, müssen in dieses DE die vergebene Pro-
duktregistrierungsnummer einstellen.


<table>
<tr>
<td>Typ:</td>
<td>DE</td>
</tr>
<tr>
<td>Format:</td>
<td>an</td>
</tr>
<tr>
<td>Länge:</td>
<td>..25</td>
</tr>
<tr>
<td>Version:</td>
<td>1</td>
</tr>
</table>


### Produktversion

Version des Kundenproduktes, mit dem kundenseitig die Nachrichten er-
zeugt wurden.

Die Produktversion ist verpflichtend mit aussagekräftigen Informationen über
das verwendete Kundenprodukt, nicht eine ggf. verwendete interne FinTS-
/HBCI-Bibliothek, zu füllen, um Support-Anfragen leichter beantworten zu
können.


<table>
<tr>
<td>Typ:</td>
<td>DE</td>
</tr>
<tr>
<td>Format:</td>
<td>an</td>
</tr>
<tr>
<td>Länge:</td>
<td>..5</td>
</tr>
<tr>
<td>Version:</td>
<td>1</td>
</tr>
</table>


R


## Rückmeldung

Rückmeldung des Kreditinstitutes.


<table>
<tr>
<th>Nr.</th>
<th>Name</th>
<th>Ver- sion</th>
<th>Typ</th>
<th>For- mat</th>
<th>Län- ge</th>
<th>Sta- tus</th>
<th>An- zahl</th>
<th>Restriktionen</th>
</tr>
<tr>
<td>1</td>
<td>Rückmel- dungscode</td>
<td>1</td>
<td>DE</td>
<td>dig</td>
<td>4</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>2</td>
<td>Bezugsdaten- element</td>
<td>1</td>
<td>DE</td>
<td>an</td>
<td>..7</td>
<td>C</td>
<td>1</td>
<td>O: bei Verwendung im Segment HIRMS N: bei Verwendung im Segment HIRMG</td>
</tr>
<tr>
<td>3</td>
<td>Rückmel- dungstext</td>
<td>1</td>
<td>DE</td>
<td>an</td>
<td>.80</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>4</td>
<td>Rückmel- dungspara- meter</td>
<td>1</td>
<td>DE</td>
<td>an</td>
<td>..35</td>
<td>O</td>
<td>10</td>
<td></td>
</tr>
</table>


<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: F</td>
<td>Version: 3.0-FV</td>
<td>Financial Transaction Services (FinTS) Dokument: Formals</td>
</tr>
<tr>
<td>Seite:<br>122</td>
<td>Stand:<br>06.10.2017</td>
<td>Kapitel: Data Dictionary<br>Abschnitt: Buchstabe R</td>
</tr>
</table>


<table>
<tr>
<td>Format:</td>
<td></td>
</tr>
<tr>
<td>Länge:</td>
<td></td>
</tr>
<tr>
<td>Version:</td>
<td>1</td>
</tr>
</table>


### Rückmeldungscode

Strukturierte Information, die die Rückmeldung genau spezifiziert.

Die erste Ziffer des Codes beschreibt die Meldungsklasse:

Codierung der 1. Ziffer:

0: Erfolg

3: Warnung

9: Fehler

Die restlichen drei Ziffern geben den Inhalt der Meldung an.


<table>
<tr>
<td>Typ:</td>
<td>DE</td>
</tr>
<tr>
<td>Format:</td>
<td>dig</td>
</tr>
<tr>
<td>Länge:</td>
<td>4</td>
</tr>
<tr>
<td>Version:</td>
<td>1</td>
</tr>
</table>


### Rückmeldungsparameter

Informationen, die die Art der Meldung weiter spezifizieren, um z. B. einen
Fehler weiter eingrenzen zu können und eine automatische Reaktion des
Kundenprodukts zu ermöglichen. Es dürfen nur die zum jeweiligen Rück-
meldungscode angegebenen Parameter eingestellt werden.

Es ist zu beachten, dass die einzustellenden Daten den Formatvorschriften
entsprechen.


<table>
<tr>
<td>Typ:</td>
<td>DE</td>
</tr>
<tr>
<td>Format:</td>
<td>an</td>
</tr>
<tr>
<td>Länge:</td>
<td>..35</td>
</tr>
<tr>
<td>Version:</td>
<td>1</td>
</tr>
</table>


### Rückmeldungstext

Inhalt der Rückmeldung im Klartext.


<table>
<tr>
<td>Typ:</td>
<td>DE</td>
</tr>
<tr>
<td>Format:</td>
<td>an</td>
</tr>
<tr>
<td>Länge:</td>
<td>..80</td>
</tr>
<tr>
<td>Version:</td>
<td>1</td>
</tr>
</table>


![へ](figures/130.1)


Der in die Rückmeldung einzustellende Text kann vom Kre-
ditinstitut frei gewählt werden. So können diese Texte an in-
dividuelle Anforderungen der einzelnen Institute angepasst
werden, um z. B. institutsspezifische Besonderheiten zu be-
rücksichtigen. Anstatt eines frei definierten Textes kann das
Institut auch den in der Spalte „Code-Bedeutung“ definierten
Text einstellen. Es ist zu beachten, dass der einzustellende
Text den Formatvorschriften entspricht.

Typ:

DEG

<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th rowspan="2">Version: 3.0-FV</th>
<th rowspan="2">Kapitel: F</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Formals</td>
</tr>
<tr>
<td>Kapitel:</td>
<td>Data Dictionary</td>
<td>Stand:</td>
<td>Seite:</td>
</tr>
<tr>
<td>Abschnitt:</td>
<td>Buchstabe S</td>
<td>06.10.2017</td>
<td>123</td>
</tr>
</table>


Das Kreditinstitut hat den Rückmeldungstext in einer Form
einzustellen, dass dieser unverändert im Kundenprodukt an-
gezeigt werden kann. Insbesondere ist der Text in der vom
Kunden mit dem Sprachkennzeichen gewählten Sprache und
unter Berücksichtigung der jeweiligen landesspezifischen Be-
sonderheiten (z. B. Formatierung des Datums) darzustellen.

Bei Syntaxfehlern ist es ausreichend, dem Kunden den Text
„Syntaxfehler“ ohne weitere Erläuterung zurückzumelden, da
der Fehler im Regelfall vom Kundenprodukt verursacht wurde
und nicht von Kunden behoben werden kann.

S


### Segmentkennung

Segmentspezifische Kennung, die jedem Segment bzw. Auftrag zugeordnet
ist (z. B. "HKCCS" für "SEPA Einzelüberweisung"). Die Angabe hat in Groß-
schreibung zu erfolgen.


<table>
<tr>
<td>Typ:</td>
<td>DE</td>
</tr>
<tr>
<td>Format:</td>
<td>an</td>
</tr>
<tr>
<td>Länge:</td>
<td>..6</td>
</tr>
<tr>
<td>Version:</td>
<td>1</td>
</tr>
</table>


### Segmentkopf

Informationen, die jedem Segment als Kopfteil vorangestellt sind. Im Unter-
schied zu Nachrichten enthalten Segmente jedoch keinen Abschlussteil, da
das Segmentende durch das Segmentende-Zeichen markiert ist.

Im Segmentkopf stehen die Segmentkennung und Segmentversion unab-
hängig von der HBCI-Version (s. DE HBCI-Version) immer an derselben
Stelle, damit ein Segment auch in späteren HBCI-Versionen immer eindeutig
als solches identifiziert werden kann.


<table>
<tr>
<th>Nr.</th>
<th>Name</th>
<th></th>
<th>Ver- sion</th>
<th>Typ</th>
<th>For- mat</th>
<th>Län- ge</th>
<th>Sta- tus</th>
<th>An- zahl</th>
<th>Restriktionen</th>
</tr>
<tr>
<td>1</td>
<td colspan="2">Segment- kennung</td>
<td>1</td>
<td>DE</td>
<td>an</td>
<td>..6</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>2</td>
<td colspan="2">Segmentnum- mer</td>
<td>1</td>
<td>DE</td>
<td>num</td>
<td>..3</td>
<td>M</td>
<td>1</td>
<td>&gt;=1</td>
</tr>
<tr>
<td>3</td>
<td colspan="2">Segment- version</td>
<td>1</td>
<td>DE</td>
<td>num</td>
<td>..3</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>4</td>
<td colspan="2">Bezugsseg- ment</td>
<td>1</td>
<td>DE</td>
<td>num</td>
<td>..3</td>
<td>C</td>
<td>1</td>
<td>&gt;=1<br>O: Verwendung in Kre- ditinstitutsnachricht N: Verwendung in Kun- dennachricht</td>
</tr>
</table>


<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: F</td>
<td>Version: 3.0-FV</td>
<td>Financial Transaction Services (FinTS) Dokument: Formals</td>
</tr>
<tr>
<td>Seite:<br>124</td>
<td>Stand:<br>06.10.2017</td>
<td>Kapitel: Data Dictionary<br>Abschnitt: Buchstabe S</td>
</tr>
</table>


<table>
<tr>
<td>Format:</td>
<td></td>
</tr>
<tr>
<td>Länge:</td>
<td></td>
</tr>
<tr>
<td>Version:</td>
<td>1</td>
</tr>
</table>


### Segmentnummer

Information zur eindeutigen Identifizierung eines Segments innerhalb einer
Nachricht. Die Segmente einer Nachricht werden in Einerschritten streng
monoton aufsteigend nummeriert. Die Nummerierung beginnt mit 1 im ersten
Segment der Nachricht (Nachrichtenkopf).


<table>
<tr>
<td>Typ:</td>
<td>DE</td>
</tr>
<tr>
<td>Format:</td>
<td>num</td>
</tr>
<tr>
<td>Länge:</td>
<td>..3</td>
</tr>
<tr>
<td>Version:</td>
<td>1</td>
</tr>
</table>


### Segmentversion

Versionsnummer zur Dokumentation von Änderungen eines Segmentfor-
mats.

Die Segmentversion von administrativen Segmenten (die Segmentart 'Admi-
nistration' bzw. 'Geschäftsvorfall' ist bei jeder Segmentbeschreibung ange-
geben) wird bei jeder Änderung des Segmentformats inkrementiert.

Bei Geschäftsvorfallssegmenten wird die Segmentversion auf logischer Ebe-
ne verwaltet, d. h. sie ist für das Auftrags-, das Antwort- und das Parame-
tersegment des Geschäftsvorfalls stets identisch und wird inkrementiert,
wenn sich das Format von mindestens einem der drei Segmente ändert.

Dieses Verfahren gilt bei Standardsegmenten einheitlich für alle Kreditinsti-
tute. Bei verbandsindividuellen Segmenten obliegt die Versionssteuerung
dem jeweiligen Verband. Der Zeitpunkt der Unterstützung einer neuen Seg-
mentversion kann jedoch zwischen den Verbänden variieren.

Die für die jeweilige HBCI-Version gültige Segmentversion ist bei der jeweili-
gen Segmentbeschreibung vermerkt.

Falls der Kunde ein Segment mit einer veralteten Versionsnummer einreicht,
sollte ihm in einer entsprechenden Warnung rückgemeldet werden, dass
sein Kundenprodukt aktualisiert werden sollte.


<table>
<tr>
<td>Typ:</td>
<td>DE</td>
</tr>
<tr>
<td>Format:</td>
<td>num</td>
</tr>
<tr>
<td>Länge:</td>
<td>..3</td>
</tr>
<tr>
<td>Version:</td>
<td>1</td>
</tr>
</table>


### Sicherheitsklasse

Die Sicherheitsklasse gibt für jede Signatur den erforderlichen Sicherheits-
dienst an. Als Sicherheitsdienst gelten derzeit ,,Authentikation" und ,Non-
Repudiation".

Der Sicherheitsdienst ,,Authentikation" erfordert die Signatur mit der Schlüs-
selart ,S“ (Schlüssel auf Kundenseite: Sk.CH.AUT c/s). Der Sicherheitsdienst
,Non-Repudiation“ erfordert die Signatur mit der Schlüsselart „D“ (Schlüssel
auf Kundenseite: SK.CH.DS).

Typ:

DEG

<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th rowspan="2">Version: 3.0-FV</th>
<th rowspan="2">Kapitel: F</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Formals</td>
</tr>
<tr>
<td>Kapitel:</td>
<td>Data Dictionary</td>
<td>Stand:</td>
<td>Seite:</td>
</tr>
<tr>
<td>Abschnitt:</td>
<td>Buchstabe S</td>
<td>06.10.2017</td>
<td>125</td>
</tr>
</table>


Derzeit sind folgende Sicherheitsklassen zulässig:


<table>
<tr>
<td>Code</td>
<td>Bedeutung</td>
</tr>
<tr>
<td>0</td>
<td>kein Sicherheitsdienst erforderlich</td>
</tr>
<tr>
<td>1</td>
<td>Sicherheitsdienst ,,Authentikation“</td>
</tr>
<tr>
<td>2</td>
<td>Sicherheitsdienst ,,Authentikation" mit fortgeschrittener elektronischer Signatur gemäß §2, SigG und optionaler Zertifikatsprüfung unter Ver- wendung des S-Schlüssels (Schlüssel Sk.CH.AUTc/s)</td>
</tr>
<tr>
<td>3</td>
<td>Sicherheitsdienst ,,Non-Repudiation" mit fortgeschrittener elektronischer Signatur gemäß §2, SigG und optionaler Zertifikatsprüfung unter Ver- wendung des DS-Schlüssels (Sk.CH.DS)</td>
</tr>
<tr>
<td>4</td>
<td>Sicherheitsdienst ,,Non-Repudiation" mit fortgeschrittener elektronischer Signatur gemäß §2, SigG und zwingender Zertifikatsprüfung unter Ver- wendung des DS-Schlüssels (SK.CH.DS)</td>
</tr>
</table>


Zu einem späteren Zeitpunkt kann die Notwendigkeit einer weiteren Sicher-
heitsklasse überprüft werden, die qualifizierte Signaturen mit zwingender
Zertifikatsprüfung erfordert.

Weitere Informationen hierzu befinden sich im Band [HBCI].


<table>
<tr>
<td>Typ:</td>
<td>DE</td>
</tr>
<tr>
<td>Format:</td>
<td>code</td>
</tr>
<tr>
<td>Länge:</td>
<td>1</td>
</tr>
<tr>
<td>Version:</td>
<td>1</td>
</tr>
</table>


### Sicherheitsreferenznummer für Digitale Signatur

(s. Sicherheitsreferenznummer) Signatur-ID des Schlüssels für Digitale Sig-
naturen (Schlüsselart „D“).


<table>
<tr>
<td>Typ:</td>
<td>DE</td>
</tr>
<tr>
<td>Format:</td>
<td>num</td>
</tr>
<tr>
<td>Länge:</td>
<td>.. 16</td>
</tr>
<tr>
<td>Version:</td>
<td>1</td>
</tr>
</table>


### Sicherheitsreferenznummer für Signierschlüssel

(s. Sicherheitsreferenznummer) Signatur-ID des Signierschlüssels (Schlüs-
selart „S“).


<table>
<tr>
<td>Typ:</td>
<td>DE</td>
</tr>
<tr>
<td>Format:</td>
<td>num</td>
</tr>
<tr>
<td>Länge:</td>
<td>.. 16</td>
</tr>
<tr>
<td>Version:</td>
<td>1</td>
</tr>
</table>


### Standardsprache

Es ist ein Sprachkennzeichen einzustellen, welches Standardsprache
und -zeichensatz des Kreditinstituts festlegt (s. auch DE ,,Dialogsprache“).
Dieses Kennzeichen bestimmt, mit welchem Zeichensatz die Dialoginitialisie-
rungsnachricht des Kunden gebildet werden muss. Nach dieser Nachricht
verliert die Standardsprache ihre Gültigkeit, da der Kunde in der Dialoginitia-
lisierung die Dialogsprache wählt, welche evtl. von der Standardsprache ab-
weicht.

Codierung:

<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: F</td>
<td>Version: 3.0-FV</td>
<td>Financial Transaction Services (FinTS) Dokument: Formals</td>
</tr>
<tr>
<td>Seite:<br>126</td>
<td>Stand:<br>06.10.2017</td>
<td>Kapitel: Data Dictionary<br>Abschnitt:<br>Buchstabe U</td>
</tr>
</table>


1: Deutsch, Code ,de' (German), Subset Deutsch, Codeset 1 (Latin 1)

2: Englisch, Code ,en' (English), Subset Englisch, Codeset 1 (Latin 1)

3: Französisch, Code ,fr' (French), Subset Französisch, Codeset 1 (Latin 1)


<table>
<tr>
<td>Typ:</td>
<td>DE</td>
</tr>
<tr>
<td>Format:</td>
<td>code</td>
</tr>
<tr>
<td>Länge:</td>
<td>..3</td>
</tr>
<tr>
<td>Version:</td>
<td>2</td>
</tr>
</table>


### Synchronisierungsmodus

Information über den Synchronisierungsmodus.

Codierung:

0: Neue Kundensystem-ID zurückmelden

1: Letzte verarbeitete Nachrichtennummer zurückmelden

2: Signatur-ID zurückmelden


<table>
<tr>
<td>Typ:</td>
<td>DE</td>
</tr>
<tr>
<td>Format:</td>
<td>code</td>
</tr>
<tr>
<td>Länge:</td>
<td>1</td>
</tr>
<tr>
<td>Version:</td>
<td>2</td>
</tr>
</table>


U


### Uhrzeit

Uhrzeit eines Ereignisses (meist zusammen mit „Datum“ verwendet).


<table>
<tr>
<td>Typ:</td>
<td>DE</td>
</tr>
<tr>
<td>Format:</td>
<td>tim</td>
</tr>
<tr>
<td>Länge:</td>
<td>#</td>
</tr>
<tr>
<td>Version:</td>
<td>1</td>
</tr>
</table>


#### Unterstützte HBCI-Version

HBCI-Version, die das Kreditinstitut für den Aufbau der Nachrichten akzep-
tiert.


<table>
<tr>
<td>Typ:</td>
<td>DE</td>
</tr>
<tr>
<td>Format:</td>
<td>num</td>
</tr>
<tr>
<td>Länge:</td>
<td>..3</td>
</tr>
<tr>
<td>Version:</td>
<td>2</td>
</tr>
</table>


#### Unterstützte HBCI-Versionen

Alle HBCI-/FinTS-Versionen, die das Kreditinstitut akzeptiert.


<table>
<tr>
<th>Nr.</th>
<th>Name</th>
<th>Ver- sion</th>
<th>Typ</th>
<th>For- mat</th>
<th>Län- ge</th>
<th>Sta- tus</th>
<th>An- zahl</th>
<th>Restriktionen</th>
</tr>
<tr>
<td>1</td>
<td>Unterstützte HBCI-Version</td>
<td>2</td>
<td>DE</td>
<td>num</td>
<td>..3</td>
<td>M</td>
<td>1..9</td>
<td></td>
</tr>
</table>


<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th rowspan="2">Version: 3.0-FV</th>
<th rowspan="2">Kapitel: F</th>
</tr>
<tr>
<th>Dokument:</th>
<th>Formals</th>
</tr>
<tr>
<td>Kapitel:<br>Abschnitt:</td>
<td>Data Dictionary Buchstabe U</td>
<td>Stand: 06.10.2017</td>
<td>Seite: 127</td>
</tr>
</table>


Typ:

DEG


<table>
<tr>
<td>Format:</td>
<td></td>
</tr>
<tr>
<td>Länge:</td>
<td></td>
</tr>
<tr>
<td>Version:</td>
<td>2</td>
</tr>
</table>


##### Unterstützte Komprimierungsverfahren

Information über das kreditinstitutsseitig unterstützte Komprimierungs-
verfahren.

Die Definition der Felder ist in [HBCI] enthalten.


<table>
<tr>
<th>Nr.</th>
<th>Name</th>
<th>Ver- sion</th>
<th>Typ</th>
<th>For- mat</th>
<th>Län- ge</th>
<th>Sta- tus</th>
<th>An- zahl</th>
<th>Restriktionen</th>
</tr>
<tr>
<td>1</td>
<td>Komprimierungs- funktion</td>
<td>1</td>
<td>DE</td>
<td>code</td>
<td>..3</td>
<td>M</td>
<td>1</td>
<td>0,1,2,3,4,5,6,7,999</td>
</tr>
<tr>
<td>2</td>
<td>Komprimie- rungsversion</td>
<td>1</td>
<td>DE</td>
<td>num</td>
<td>..3</td>
<td>M</td>
<td>1..9</td>
<td></td>
</tr>
</table>


<table>
<tr>
<td>Typ:</td>
<td>DEG</td>
</tr>
<tr>
<td>Format:</td>
<td></td>
</tr>
<tr>
<td>Länge:</td>
<td></td>
</tr>
<tr>
<td>Version:</td>
<td>2</td>
</tr>
</table>


### Unterstützte Sicherheitsverfahren

Information über die kreditinstitutsseitig unterstützten Sicherheitsverfahren.
Anhand der Kombination der beiden Elemente ,,Sicherheitsverfahren“ und
,Version" wird das Sicherheitsprofil (z. B. RAH-7) bestimmt.

Die Definition der Felder ist in [HBCI] enthalten.


<table>
<tr>
<th>Nr.</th>
<th>Name</th>
<th>Ver- sion</th>
<th>Typ</th>
<th>For- mat</th>
<th>Län- ge</th>
<th>Sta- tus</th>
<th>An- zahl</th>
<th>Restriktionen</th>
</tr>
<tr>
<td>1</td>
<td>Sicherheitsver- fahren, Code</td>
<td>1</td>
<td>DE</td>
<td>code</td>
<td>3</td>
<td>M</td>
<td>1</td>
<td>DDV, RAH, RDH und PIN</td>
</tr>
<tr>
<td>2</td>
<td>Version des Si- cherheitsverfah- rens</td>
<td>1</td>
<td>DE</td>
<td>num</td>
<td>..3</td>
<td>M</td>
<td>1..9</td>
<td>1, 2, 3, 4, 5, 6, 7, 8, 9, 10</td>
</tr>
</table>


![](figures/135.1)


Um Multibankfähigkeit zu gewährleisten, ist die Unterstüt-
zung eines der Verfahren RAH-9 bzw. übergangsweise
RDH-9 kunden- und kreditinstitutsseitig verpflichtend.


<table>
<tr>
<td>Typ:</td>
<td>DEG</td>
</tr>
<tr>
<td>Format:</td>
<td></td>
</tr>
<tr>
<td>Länge:</td>
<td></td>
</tr>
<tr>
<td>Version:</td>
<td>3</td>
</tr>
</table>


### Unterstützte Sprache

Information darüber, in welcher Sprache der Kunde mit dem Kreditinstitut
kommunizieren kann. Die derzeit gültigen Sprachkennzeichen sind beim
Element ,,Dialogsprache“ aufgeführt.

Codierung : s. „Dialogsprache“

<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: F</td>
<td>Version: 3.0-FV</td>
<td>Financial Transaction Services (FinTS) Dokument: Formals</td>
</tr>
<tr>
<td>Seite:<br>128</td>
<td>Stand:<br>06.10.2017</td>
<td>Kapitel: Data Dictionary<br>Abschnitt:<br>Buchstabe U</td>
</tr>
</table>


<table>
<tr>
<td>Typ:</td>
<td>DE</td>
</tr>
<tr>
<td>Format:</td>
<td>code</td>
</tr>
<tr>
<td>Länge:</td>
<td>..3</td>
</tr>
<tr>
<td>Version:</td>
<td>2</td>
</tr>
</table>


#### Unterstützte Sprachen

Information darüber, in welchen Sprachen der Kunde mit dem Kreditinstitut
kommunizieren kann.


<table>
<tr>
<th>Nr.</th>
<th>Name</th>
<th>Ver- sion</th>
<th>Typ</th>
<th>For- mat</th>
<th>Län- ge</th>
<th>Sta- tus</th>
<th>An- zahl</th>
<th>Restriktionen</th>
</tr>
<tr>
<td>1</td>
<td>Unterstützte Sprache</td>
<td>2</td>
<td>DE</td>
<td>code</td>
<td>..3</td>
<td>M</td>
<td>1..9</td>
<td>1, 2, 3</td>
</tr>
</table>


<table>
<tr>
<td>Typ:</td>
<td>DEG</td>
</tr>
<tr>
<td>Format:</td>
<td></td>
</tr>
<tr>
<td>Länge:</td>
<td></td>
</tr>
<tr>
<td>Version:</td>
<td>2</td>
</tr>
</table>


![](figures/136.1)


Bei Bedarf kann das Kundenprodukt auf dieses Kennzeichen
reagieren und die Sprache des Kundenproduktes entspre-
chend automatisiert anpassen.


##### UPD-Version

Versionsnummer der Userparameterdaten (UPD). Bei jeder kreditinstitutssei-
tigen Änderung wird die Version inkrementiert. (S. auch DE BPD-Version).


<table>
<tr>
<td>Typ:</td>
<td>DE</td>
</tr>
<tr>
<td>Format:</td>
<td>num</td>
</tr>
<tr>
<td>Länge:</td>
<td>..3</td>
</tr>
<tr>
<td>Version:</td>
<td>1</td>
</tr>
</table>


##### UPD-Verwendung

Kennzeichen dafür, wie diejenigen Geschäftsvorfälle zu interpretieren sind,
die bei der Beschreibung der Kontoinformationen nicht unter den erlaubten
Geschäftsvorfällen aufgeführt sind.


###### Codierung:

0: Die nicht aufgeführten Geschäftsvorfälle sind gesperrt (die aufgeführten
Geschäftsvorfälle sind zugelassen).

1: Bei den nicht aufgeführten Geschäftsvorfällen ist anhand der UPD keine
Aussage darüber möglich, ob diese erlaubt oder gesperrt sind. Diese Prü-
fung kann nur online vom Kreditinstitutssystem vorgenommen werden.

<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th rowspan="2">Version: 3.0-FV</th>
<th rowspan="2">Kapitel: F</th>
</tr>
<tr>
<th>Dokument:</th>
<th>Formals</th>
</tr>
<tr>
<td>Kapitel:<br>Abschnitt:</td>
<td>Data Dictionary<br>Buchstabe V</td>
<td>Stand: 06.10.2017</td>
<td>Seite: 129</td>
</tr>
</table>


<table>
<tr>
<td>Typ:</td>
<td>DE</td>
</tr>
<tr>
<td>Format:</td>
<td>code</td>
</tr>
<tr>
<td>Länge:</td>
<td>1</td>
</tr>
<tr>
<td>Version:</td>
<td>2</td>
</tr>
</table>


V


####### Version der Filterfunktion

Version der Filterfunktion.


<table>
<tr>
<td>Typ:</td>
<td>DE</td>
</tr>
<tr>
<td>Format:</td>
<td>num</td>
</tr>
<tr>
<td>Länge:</td>
<td>..3</td>
</tr>
<tr>
<td>Version:</td>
<td>1</td>
</tr>
</table>


######## Von Datum

Anfangsdatum eines Zeitraums (s. Kap. B.6.3).

Durch die Eingabe von Von- und Bis-Datum kann ein Zeitraum eingegrenzt
werden, für den Informationseinträge vom Kreditinstitut rückzumelden sind.


<table>
<tr>
<td>Typ:</td>
<td>DE</td>
</tr>
<tr>
<td>Format:</td>
<td>dat</td>
</tr>
<tr>
<td>Länge:</td>
<td>#</td>
</tr>
<tr>
<td>Version:</td>
<td>1</td>
</tr>
</table>


######## Von Kreditinstitutskennung

Start eines Bereichs von Kreditinstitutskennungen (s. auch „Bis Kredit-
institutskennung")


<table>
<tr>
<td>Typ:</td>
<td>DEG</td>
</tr>
<tr>
<td>Format:</td>
<td>kik</td>
</tr>
<tr>
<td>Länge:</td>
<td>#</td>
</tr>
<tr>
<td>Version:</td>
<td>2</td>
</tr>
</table>


W


######## Währung

Angabe der Währung im Format ISO 4217.


<table>
<tr>
<td>Typ:</td>
<td>DE</td>
</tr>
<tr>
<td>Format:</td>
<td>cur</td>
</tr>
<tr>
<td>Länge:</td>
<td>#</td>
</tr>
<tr>
<td>Version:</td>
<td>1</td>
</tr>
</table>


######## Wert

Monetärer Wert z. B. als Bestandteil eines Geldbetrags.


<table>
<tr>
<td>Typ:</td>
<td>DE</td>
</tr>
<tr>
<td>Format:</td>
<td>wrt</td>
</tr>
<tr>
<td>Länge:</td>
<td>#</td>
</tr>
<tr>
<td>Version:</td>
<td>1</td>
</tr>
</table>


<!-- PageBreak -->

<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th rowspan="2">Version: 3.0-FV</th>
<th rowspan="2">Kapitel: G</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Formals</td>
</tr>
<tr>
<td>Kapitel:</td>
<td>Syntax</td>
<td>Stand:</td>
<td>Seite:</td>
</tr>
<tr>
<td>Abschnitt:</td>
<td>Nachrichtensyntax</td>
<td>06.10.2017</td>
<td>131</td>
</tr>
</table>


# H. SYNTAX


## H.1 Nachrichtensyntax


### H.1.1 Syntaxzeichen

Es wird eine Trennzeichensyntax mit Freigabezeichen verwendet.

Folgende Syntaxzeichen werden vereinbart:


<table>
<tr>
<td>Zeichen</td>
<td>Bedeutung</td>
</tr>
<tr>
<td>+</td>
<td>Trennzeichen zwischen Datenelementen</td>
</tr>
<tr>
<td>:</td>
<td>Trennzeichen zwischen Datenelementen innerhalb einer DEG</td>
</tr>
<tr>
<td>'</td>
<td>Segmentende-Zeichen</td>
</tr>
<tr>
<td>?</td>
<td>Freigabezeichen</td>
</tr>
<tr>
<td>@</td>
<td>Binärdatenkennzeichen</td>
</tr>
</table>


## H.1.2 Nachrichtenaufbau


### ◆ Datenelemente

Datenelemente werden durch das DE-Trennzeichen '+' syntaktisch getrennt.

...+DE+DE+DE+...


### . Datenelementgruppen

Datenelemente innerhalb einer Datenelementgruppe werden durch das Trenn-
zeichen ':' getrennt. Die Datenelementgruppe wird vom vorausgehenden und nach-
folgenden Element durch das Trennzeichen ,,+" getrennt.

. .+DE+DE : DE : DE : DE+DE+...


### . Segmente

Jedes Segment wird mit der DEG ,,Segmentkopf" (s. u.) eingeleitet. Das Ende eines
Segmentes wird stets durch das Segmentende-Zeichen (') signalisiert. Vor dem ers-
ten und nach dem letzten DE eines Segments darf kein DE-Trennzeichen erschei-
nen.

Segmentkopf+DE+DE+...+DE'


### . Nachrichten

Die Kommunikation zwischen Kunde und Kreditinstitut erfolgt über Nachrichten.
Nachrichten setzen sich aus einer vorgegebenen Segmentabfolge zusammen (s.
Abb. 2). Ausnahmslos alle Nachrichten (Kunde an Kreditinstitut und umgekehrt)
enthalten je ein Kopf- und ein Abschlusssegment. Alle weiteren Nachrichteninhalte
werden ebenfalls in Segmente, die vom Aufbau her dem allgemeinen festen Seg-
mentformat entsprechen, eingestellt. Der allgemeine Nachrichtenaufbau (Segment-
abfolge) ist in den jeweiligen Kapiteln zu Kunden- und Kreditinstitutsnachrichten be-
schrieben.

<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: G</td>
<td>Version: 3.0-FV</td>
<td>Financial Transaction Services (FinTS) Dokument: Formals</td>
</tr>
<tr>
<td>Seite:<br>132</td>
<td>Stand: 06.10.2017</td>
<td>Kapitel: Syntax Abschnitt: Nachrichtensyntax</td>
</tr>
</table>


## . Sonderfall: Verwendung von Datenelementgruppen innerhalb von Datenele- mentgruppen

DEGs (z. B. mehrfach verwendete Elemente) können im Ausnahmefall auch wiede-
rum in Datenelementgruppen eingestellt werden. In diesem Fall dürfen sie nicht
durch Auslassen von Kann-Elementen gekürzt werden.

Beispiel: MVE ,,Saldo" innerhalb einer DEG

Girokonto: C:1000,:EUR:20020701::Beschreibung


## . Sonderfall: Mehrfach auftretende optionale Datenstrukturen

Wenn DE bzw. DEG mit dem Status ,,Optional" mehrfach auftreten können (Anzahl
\> 1), sollten sie als letztes Element der jeweiligen syntaktischen Einheit eingestellt
werden, da ansonsten die Struktur u.U. nicht eindeutig zugeordnet werden kann.
Falls sie innerhalb der syntaktischen Einheit auftreten sollen, dürfen keine Auslas-
sungen von Syntaxzeichen vorgenommen werden.

Beispiel:


<table>
<tr>
<th>Nr.</th>
<th>Name</th>
<th>Ver- sion</th>
<th>Typ</th>
<th>For- mat</th>
<th>Län- ge</th>
<th>Sta- tus</th>
<th>An- zahl</th>
<th>Restriktionen</th>
</tr>
<tr>
<td>1</td>
<td>Segmentkopf</td>
<td>1</td>
<td>DEG</td>
<td></td>
<td></td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>2</td>
<td>DE1</td>
<td>1</td>
<td>DE</td>
<td></td>
<td></td>
<td>O</td>
<td>5</td>
<td></td>
</tr>
<tr>
<td>3</td>
<td>DE2</td>
<td>1</td>
<td>DE</td>
<td></td>
<td></td>
<td>O</td>
<td>4</td>
<td></td>
</tr>
</table>


DE1 und DE2 sollen jeweils genau 2 mal belegt werden:

<Segmentkopf>+DE1+DE1++++DE2+DE2'


## H.1.3 Entwertung

Kommen Syntaxzeichen in einzustellenden Daten vor, sind diese durch Voranstel-
lung des Freigabezeichens '?' zu entwerten. Die Entwertung hat bei allen einzustel-
lenden Daten, außer bei binären Daten zu erfolgen.

Beispiel 1:

vor Entwertung:

Taschengeld für Hans + Franz

nach Entwertung:

Taschengeld für Hans ?+ Franz


### Beispiel 2:

vor Entwertung:

Ist das so richtig??

nach Entwertung:

Ist das so richtig????

<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th>Version:</th>
<th rowspan="2">Kapitel: G</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Formals</td>
<td>3.0-FV</td>
</tr>
<tr>
<td>Kapitel:</td>
<td>Syntax</td>
<td>Stand:</td>
<td>Seite:</td>
</tr>
<tr>
<td>Abschnitt:</td>
<td>Nachrichtensyntax</td>
<td>06.10.2017</td>
<td>133</td>
</tr>
</table>


## H.1.4 Binäre Daten

Für binäre Daten gilt eine besondere Syntaxregelung: Das Auftreten dieser Daten
wird eingeleitet mit dem Binärdatenkennzeichen (@). Anschließend folgt die Län-
genangabe zu den binären Daten und der binäre Wert selbst, der ebenfalls mit dem
Binärdatenkennzeichen eingeleitet wird. Die Länge wird angegeben in Byte (nicht
die Länge der darstellbaren Zeichen). Hierzu muss sichergestellt sein, dass der bi-
näre Datenstrom in vollen Byte dargestellt werden kann (binäre Daten, die nicht im
Byteformat vorliegen, können nicht über FinTS transportiert werden). Syntaxzei-
chen, die in binären Daten auftreten, dürfen nicht als solche interpretiert werden.

Bei Elementen, die entsprechende Zeichen enthalten können (z. B. DE „SEPANa-
me) ist eine base64-Kodierung in der Spezifikation vorzusehen.

...+DE+@<Länge>@<Binärdaten>+DE...


## H.1.5 Auslassen von Datenstrukturen


### . Auslassen von Segmenten

Kann-Segmente, die keine Daten enthalten, werden einschließlich ihres Segment-
kopfes ausgelassen.


### . Auslassen von Datenelementen

DE werden anhand ihrer Reihenfolge innerhalb des Segmentes identifiziert. DE für
die kein Inhalt vorhanden ist, können, sofern sie den Status ,,Kann" haben, aus-
gelassen werden. Ihre Position wird, sofern noch signifikante (mit Inhalt gefüllte) DE
folgen, durch ein DE-Trennzeichen dargestellt.

Beispiel 1:

Segmentkopf+DE+DE+++DE+DE+DE'

Die DE 3 und 4 nach dem Segmentkopf wurden ausgelassen.


### . Auslassen von Datenelementen durch Abschneiden

Ist für DE, die am Ende eines Segments stehen, kein Inhalt vorhanden, können sie
ausgelassen werden. In diesem Fall wird das Segmentende-Zeichen unmittelbar
nach dem letzten mit Inhalt belegten DE angegeben.

Beispiel 2:

Segmentkopf+DE+DE+++DE'

In Fortführung von Beispiel 1 wurden die letzten beiden DE (6. und 7. DE nach dem
Segmentkopf) abgeschnitten.


![](figures/141.1)


![](figures/141.2)


Da das Abschneiden von Datenelementen nicht verpflichtend ist,
sollte das empfangende System sowohl die abgeschnittene als
auch die nicht abgeschnittene Variante entgegennehmen können.
Dies gilt ebenso auch für das Abschneiden von Gruppendatenele-
menten.


### ◆ Auslassen von Gruppendatenelementen

Es gelten analog die Ausführungen zur Auslassung von Datenelementen.

<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: G</td>
<td>Version: 3.0-FV</td>
<td>Financial Transaction Services (FinTS) Dokument: Formals</td>
</tr>
<tr>
<td>Seite: 134</td>
<td>Stand: 06.10.2017</td>
<td>Kapitel: Syntax<br>Abschnitt: Nachrichtensyntax</td>
</tr>
</table>


Beispiel 3:

Segmentkopf+DE+GD : GD+GD: : : GD'

In der letzten Datenelementgruppe wurden zwei GD ausgelassen.


### . Auslassen von Gruppendatenelementen durch Abschneiden

Falls ein oder mehrere GD am Ende einer DEG ausgelassen werden, können sie
durch das DE-Trennzeichen abgeschnitten werden. Stehen sie als letzte im Se-
gment, wird das Segmentende-Zeichen unmittelbar nach dem letzten mit Inhalt be-
legten GD angegeben.

Beispiel 4:

Segmentkopf+DE+GD+GD'

In Fortführung von Beispiel 3 wurde das letzte GD im zweiten DE (erste DEG) nach
dem Segmentkopf unterdrückt. Die letzten drei GD in der letzten DEG wurden ab-
geschnitten.

Kann-DE sollten am Ende des Segmentes stehen, um eine Reduzierung des Da-
tenvolumens durch Abschneiden zu ermöglichen, sofern dies keine Auswirkungen
auf die logische Reihenfolge der Daten hat. Ebenso sollten Kann-GD am Ende einer
DEG stehen.

<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th rowspan="2">Version: 3.0-FV</th>
<th rowspan="2">Kapitel: G</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Formals</td>
</tr>
<tr>
<td>Kapitel: Abschnitt:</td>
<td>Syntax Beispiele</td>
<td>Stand: 06.10.2017</td>
<td>Seite: 135</td>
</tr>
</table>


## H.2 Beispiele


### H.2.1 Datenelementgruppen


#### . Adresse

Ernst Müller::Bahnhofstr. 17:12345:Berlin:280:03
0/1234-567


#### . Betrag

4567,89:EUR

. Hashalgorithmus

1:999:1


#### . Kontoverbindung

1234567:EUR:280:10020030

. Kreditinstitutskennung

280:10020030


#### ◆ Saldo

C:1000, :EUR:20020710:123015


#### . Segmentkopf

HIKAZ:5:1:3


#### . Signaturalgorithmus

6:10:16


#### ◆ Verschlüsselungsalgorithmus

2:2:13:@96@<chiffrierter Schlüssel>:6:1


### H.2.2 Segmente


#### . Anforderung eines öffentlichen Schlüssels

HKISA:8:3+2+124+RDH:3+280:10020030:12345:D:1:1'


#### ◆ Auslandsüberweisung

HKAUB:3:6+1234567::280:10020030+@1280@<DTAZV>'


#### ◆ Auslandsüberweisung ohne Meldeteil

HKAOM:4:2+1234567::280:10020030+MUSTERMANN AG, 1
2345 BERLIN++GB14742398061542312341+BANK OF SCOT
LAND, EDINBURGH+JOHN SMITH, PO BOX 1234, EDINBUR
GH, UK+1000,:GBP+1+INVOICE NR. 765-4321'

<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: G</td>
<td>Version: 3.0-FV</td>
<td>Financial Transaction Services (FinTS) Dokument: Formals</td>
</tr>
<tr>
<td>Seite: 136</td>
<td>Stand: 06.10.2017</td>
<td>Kapitel: Syntax Abschnitt: Beispiele</td>
</tr>
</table>


## ◆ Auslandsüberweisung ohne Meldeteil Parameter

HIAOMS:18:2:5+1+2+2+J:250;24;23;24;64;15000,; EUR
:826; 18; 14;18; 18; ; ;6500,;GBP:756;96;22;96;140; ; ;
500000,;CHF:380;70;23;99140;5500,;EUR:724;70;20;
70;105;3000,;EUR'


## ◆ Auslandsüberweisung Parameter

HIAUBS:31:6:5+1+2+2+0'


## . Bankparameter allgemein

HIBPA:3:3:7+3+280:10020030+Musterbank in Musters
tadt+1+1:2:3+201:210:220:300+100'


## . Bearbeitungsstatus Finanzdatenformat anfordern

HKFDB:4:2+1234567::280:10020030+123456789'


## . Bearbeitungsstatus Finanzdatenformat Parameter

HIFDBS:4:2:5+1+2+1'


## . Bearbeitungsstatus Finanzdatenformat rückmelden

HIFDB:4:2:4+1:509:9909+@176@<MT 509>+20021013:14
3725'


## ◆ Bestätigung der Schlüsselsperrung

HISSP:8:3:8+1+4711+2+231+280:10020030:12345:S:1:
1+501+6:20020611:111734'


## . Depotaufstellung anfordern

HKWPD:3:7+23456::280:10020030+USD+2'


## . Depotaufstellung Parameter

HIWPDS:31:7:5+1+2+1+J:N:J'


## ◆ Depotaufstellung rückmelden

HIWPD:3:6:3+@318@<MT571>'

HIWPD:3:7:3+@356@<MT535>'


## ◆ Depotumsätze anfordern

HKWDU:4:6+1357924::280:10020030+N+1:723600+20020
527+20020712'

◆ Depotumsätze Parameter

HIWDUS:6:6:5+1+2+60'


## ◆ Depotumsätze rückmelden

HIWDU:5:5:4+@287@<MT572>'

<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th rowspan="2">Version: 3.0-FV</th>
<th rowspan="2">Kapitel: G</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Formals</td>
</tr>
<tr>
<td>Kapitel:</td>
<td>Syntax</td>
<td>Stand:</td>
<td>Seite:</td>
</tr>
<tr>
<td>Abschnitt:</td>
<td>Beispiele</td>
<td>06.10.2017</td>
<td>137</td>
</tr>
</table>


HIWDU:5:6:4+@324@<MT536>'


## . Devisenkurse anfordern

HKDVK:3:2+CHF+EUR'


## . Devisenkurse Parameter

HIDVKS:27:2:5+1+0+0+J:N'


## ◆ Devisenkurse rückmelden

Preisnotierung: 1 EUR = 0,8675/0,8840 CHF

HIDVK:3:2:3+CHF+Schweizer Franken+1+1+0,8675:EUR
+0,884: EUR::20020701'

Mengennotierung: 100 BEF = 1,1275/1,1275 EUR

HIDVK:3:2:3+BEF+Belgische Franken+100+2+1,1275+1
,1275+EUR+20020701'


## . Dialogende

HKEND:11:1+4711'


## ◆ Einreichung Zeichnung bestätigen

HINEZ:5:2:4+J+1234567+++2'


## . Empfangsquittung

HKQTG:3:1+@12@<Quittungscode>'


## . Empfangsquittung Parameter

HIQTGS:6:1:3+1+2+1'


## ◆ Festgeld ändern Parameter

HIFGAS:28:4:5+1+2+2+N:J:J:J:N'


## ◆ Festgeldänderung bestätigen

HIFGA:3:4:3+7654322::280:10020030+124+7654321::2
80:10020030+123'


## ◆ Festgeldanlage ändern

HKFGA:4:4+7654321::280:10020030+123+10000,:EUR+2
0020701:20020831:3,25: A:10000,: EUR:19999, : EUR:4:
60 Tage, 3,25%+1234567::280:10020030+J+2+1+12345
67::280:10020030'


## . Festgeldanlage prolongieren

HKFGP:3:4+7654321::280:10020030+123+10000,:EUR+2
0020701:20020831:3,25: A:10000,: EUR:19999, : EUR:4:
60 Tage, 3,25%+1234567::280:10020030+J+1+1+12345
67::280:10020030+++++30:10000,:EUR:1'

<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: G</td>
<td>Version: 3.0-FV</td>
<td>Financial Transaction Services (FinTS) Dokument: Formals</td>
</tr>
<tr>
<td>Seite: 138</td>
<td>Stand: 06.10.2017</td>
<td>Kapitel: Syntax Abschnitt: Beispiele</td>
</tr>
</table>


## . Festgeldbestand anfordern

HKFGB:3:4+7654321::280:10020030+123+N'


## . Festgeldbestand Parameter

HIFGBS:30:4:5+1+2+1'


## ◆ Festgeldbestand rückmelden

HIFGB:3:4:3+7654321::280:10020030+123+10000, : EUR
+20020701:20020831: 3,25: A:10000,:EUR:19999, :EUR:
4:60 Tage, 3,25%+1234567::280:10020030+J+1+1+123
4567::280:10020030+++345,67:EUR+1+30:10000,:EUR:
1'


## . Festgeldkonditionen anfordern

HKFGK:3:3+EUR'


## . Festgeldkonditionen Parameter

HIFGKS:26:3:5+1+0+0+EUR:CHF:FRF'


## ◆ Festgeldkonditionen rückmelden

HIFGK:3:3:3+38516:20020701:152245+20020701:20020
731:3,: A:10000,: EUR:19999,:EUR:1:30 Tage, 3%+200
20701:20020731:3,125: A:20000,: EUR: 29999,: EUR: 2:3
0 Tage, 3,125%+20020701:20020731:3,25: A:30000,:E
UR:::3:30 Tage, 3,25%+20020701:20020831:3, 25: A:1
0000,:EUR: 19999,:EUR:4:60 Tage, 3,25%+20020701:2
0020831:3,375: A:20000, : EUR:29999, : EUR:5:60 Tage,
3,375%+20020701:20020831:3,5: A:30000,: EUR: ::6:6
0 Tage, 3,5%+20020701:20020930: 3,5: A:10000,:EUR:
19999, :EUR:7:90 Tage, 3,5%+20020701:20020930:3,7
5:A:20000,:EUR:29999,:EUR:8:90 Tage, 3,75%+20020
701:20020930:3,875: A:30000,:EUR:::9:90 Tage, 3,8
75%'


## . Festgeldneuanlage

HKFGN:3:4+++10000,:EUR+20020701:20020831:3,25: A:
10000,:EUR:19999,:EUR:4:60 Tage, 3,25%+1234567::
280:10020030+J+1+1+1234567::280:10020030++38516:
20020701:152245'


## ◆ Festgeldneuanlage bestätigen

HIFGN:3:4:3+7654321::280:10020030+123'


## . Festgeldneuanlage Parameter

HIFGNS:27:4:5+1+2+2+N:J:J:1'

<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th rowspan="2">Version: 3.0-FV</th>
<th rowspan="2">Kapitel: G</th>
</tr>
<tr>
<th>Dokument:</th>
<th>Formals</th>
</tr>
<tr>
<td>Kapitel: Abschnitt:</td>
<td>Syntax Beispiele</td>
<td>Stand: 06.10.2017</td>
<td>Seite: 139</td>
</tr>
</table>


## . Festgeldneuanlage widerrufen

HKFGW:3:4+7654321::280:10020030+123+10000,:EUR+2
0020701:20020831:3,25: A:10000,: EUR:19999, : EUR:4:
60 Tage, 3,25%+1234567::280:10020030+J+1+1+12345
67::280:10020030++38516:20020701:152245'


## . Festgeldneuanlage widerrufen Parameter

HIFGWS:31:4:5+1+2+2'


## ◆ Festgeldprolongation bestätigen

HIFGP:3:4:3+7654322::280:10020030+124+7654321::2
80:10020030+123'


## . Festgeldprolongation Parameter

HIFGPS:29:4:5+1+2+2'


## . Festgeldprolongation widerrufen

HKFPW:3:4+7654321::280:10020030+123+10000,:EUR+2
0020701:20020831:3,25: A:10000,: EUR:19999, : EUR:4:
60 Tage, 3,25%+1234567::280:10020030+J+1+1+12345
67::280:10020030+++++30:10000,:EUR:1'


## . Festgeldprolongation widerrufen Parameter

HIFPWS:32:4:5+1+2+2'


## . Festpreisangebote anfordern

HKWFP:4:3+Renten'


## . Festpreisangebote Parameter

HIWFPS:6:3:5+1+0+0+Aktien:Renten:Optionen: Bundes
obligationen:Bundesschatzbriefe'


## ◆ Festpreisangebote rückmelden

HIWFP:5:3:4+12345+2:620597+Stadtsparkasse Köln I
nhaberschuldverschrei-
bung Serie 63+IHS+100,+1000, :EUR+0101+5000, :EUR+
2+100,75+20031025+1000,+5,46'


## . Festpreisorder

HKFPO:4:2+1234567::280:10020030+++@378@<MT502>+1
234567++1::20021012:1+2:Aktien:20021012:1'


## . Festpreisorder Parameter

HIFPOS:6:2:5+1+2+2+J:2:J:J:10000,:EUR'


## . Festpreisordereinreichung bestätigen

HIFPO:5:2:4+N+1234567+++6'

<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: G</td>
<td>Version: 3.0-FV</td>
<td>Financial Transaction Services (FinTS) Dokument: Formals</td>
</tr>
<tr>
<td>Seite: 140</td>
<td>Stand: 06.10.2017</td>
<td>Kapitel: Syntax Abschnitt: Beispiele</td>
</tr>
</table>


## . Finanzdatenformat anfordern

HKFDA:4:2+1234567::280:10020030+1:950:9909+20021
013'


## . Finanzdatenformat anfordern Parameter

HIFDAS:4:2:5+1+2+1+1;950;9810:1;950;9909:1;951;9
810'


## ◆ Finanzdatenformat rückmelden

HIFDA:4:2:4+1:950:9909+@2048@<MT 950>+20021013:1
43725'


## . Finanzdatenformat senden

HKFDS:5:2+1234567::280:10020030+1:101:9810+@768@
<SWIFT MT101>+20020712:163045'


## . Finanzdatenformat senden Parameter

HIFDSS:4:2:5+1+2+2+1;100;9810:1;101;9901'


## . Finanzdatenformatliste anfordern

HKFDL:4:2+1234567::280:10020030'


## . Finanzdatenformatliste anfordern Parameter

HIFDLS:4:2:5+1+2+1'


## ◆ Finanzdatenformatliste rückmelden

HIFDL:4:2:4+1:950:9810+20021013:143725'


## . Fondsorder einreichen

HKWFO:4:2+1234567::280:10020030+++@378@<MT502>+1
234568::280:10020030+N+1::20021012:1+2:Aktien:20
021012:1'


## . Fondsorder Parameter

HIWFOS:6:2:5+1+2+2+J:2:J:N:J:123456;123457;12345
8:10000, :EUR: MAKT; LMTO '


## . Fondsordereinreichung bestätigen

HIWFO:5:2:4+J+1234567+++2'


## . Freistellungsdaten abfragen

HKFRD:3:2+280:10020030+1234567+2002+2003'


## . Freistellungsdaten Parameter

HIFRDS:13:2:5+1+2+1'

<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th rowspan="2">Version: 3.0-FV</th>
<th rowspan="2">Kapitel: G</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Formals</td>
</tr>
<tr>
<td>Kapitel: Abschnitt:</td>
<td>Syntax Beispiele</td>
<td>Stand: 06.10.2017</td>
<td>Seite: 141</td>
</tr>
</table>


## ◆ Freistellungsdaten rückmelden

HIFRD:3:2+280:10020030+20020101+20021231+300,:EU
R+200, :EUR+20020110'


## . Gastmeldung

HKGAM:4:4++Bitte schicken Sie mir Informationen
zu Ihrem Leistungsspektrum. Danke Ernst Müller++
Ernst Müller::Bahnhofstr. 17:12345:Berlin'


## . Gastmeldung Parameter

HIGAMS: 48:4:5+1+0+0+512'


## . Identifikation

HKIDN:5:2+280:10020030+12345+2+1'


## . Informationen anfordern

HKINF:3:4+3511:3512:3513:5110+Ernst Müller::Bahn
hofstr. 17:12345:Berlin'


## ◆ Informationen rückmelden

HIINF:3:4:3+5110:Der Zinssatz für Immobilienkred
i-

te bei 10-jähriger Laufzeit beträgt aktuell 6,75
응. '


## . Informationsanforderung Parameter

HIINFS:50:4:5+1+2+1'


## . Kartenanzeige

HIAZK:3:2:3+10+ec-Karte+1234567890+1+Franz Meier
+20020101+20031231'

HIAZK:4:2:3+11+Service-Card+9876543210++Franz Me
ier++20021231+10000, :EUR'


## . Kartenanzeige anfordern

HKAZK:3:2+1234567::280:10020030'


## . Kartenanzeige Parameter

HIAZKS:22:2:5+1+2+1'


## . Kartensperre beantragen

HKKAS:3:2+1234567::280:10020030+1+123456789+++20
021231'

<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: G</td>
<td>Version: 3.0-FV</td>
<td>Financial Transaction Services (FinTS) Dokument: Formals</td>
</tr>
<tr>
<td>Seite: 142</td>
<td>Stand: 06.10.2017</td>
<td>Kapitel: Syntax Abschnitt: Beispiele</td>
</tr>
</table>


## . Kartensperre beantragen Parameter

HIKASS:22:2:5+1+2+2+10;ec-Karte:11;Service-Card:
12; Kreditkarte'


## . Kommunikationszugang anfordern

Alle Kommunikationszugänge:
HKKOM:2:4'

Kommunikationszugänge für BLZ 100 200 30:

HKKOM:2:4+280:10020030+280:10020030


## . Kommunikationszugang Parameter

HIKOMS: 11:4:5+1+0+0'


## ◆ Kommunikationszugang rückmelden

HIKOM:3:4:2+280:10020030+1+1:12345678:00+2:123.1
23.123.123: :UUE:1+2:www.bankname.de:: UUE:1'

HIKOM:4:4:2+280:20030040+1+1:54321:00'

HIKOM:5:4:2+280:30040050+2+1:12345:22'


## . Komprimierungsverfahren

HIKPV:6:1:7+0:0'


## . Kontoauszug

HIEKA:4:1:3+1+20021101:20021130+@362@<MT940>'


## . Kontoauszug anfordern

HKEKA:3:1+1234567::280:10020030+1+15'


## . Kontoauszug Parameter

HIEKAS:12:1:5+1+2+2+J:N:N:1:2'


## . Kontoinformation

HIUPD:15:5:7+1234567::280:10020030+12345+1+EUR+E
rnst Müller++Giro Spezial+T:2000, :EUR+HKPRO:1+HK
SAK:1+HKISA:1+HKSSP:1+HKCCS:1+HKLAS: 1+HKKAN :1+HK
KAZ:1+HKSAL:1'

HIUPD:16:5:7+1234568::280:10020030+12345+10+EUR+
Ernst Müller++Sparkonto 2000++HKPRO:1+HKSAK:0+HK
ISA:1+HKSSP:0+HKCCS:2:Z:1000,: EUR:7+HKKAN: 1+HKKA
Z:1+HKSAL:2'


## . Kontoinformationen anfordern

HKKIF:3:2+1234567::280:10020030+J'

<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th rowspan="2">Version: 3.0-FV</th>
<th rowspan="2">Kapitel: G</th>
</tr>
<tr>
<th>Dokument:</th>
<th>Formals</th>
</tr>
<tr>
<td>Kapitel: Abschnitt:</td>
<td>Syntax Beispiele</td>
<td>Stand: 06.10.2017</td>
<td>Seite: 143</td>
</tr>
</table>


# . Kontoinformationen Parameter

HIKIFS:14:2:5+1+2+1'


## ◆ Kontoinformationen rückmelden

HIKIF:3:2:6+1234567::280:10020030+1+Ernst Müller
++Giro 2000+EUR+200242105+8, 75+0, 5+12, 5+5000, :EU
R++Ernst Müller::Bahnhofstraße 17:12345:Berlin+2
++Geschäftskonto+Ernst Müller::1:2:10000,:EUR:2+
Gisela Müller::2:2:2000,:EUR:4'

HIKIF:4:2:6+7654321::280:10020030+30+Ernst Mülle
r++Depot 2000+EUR+20020410+++++1234567::280:1002
0030++1+3+Bewertung zu 60%'


## ◆ Kontoumsätze anfordern/neue Umsätze

HKKAN:3:6+1234567::280:10020030+J'


## ◆ Kontoumsätze anfordern/Zeitraum

HKKAZ:3:6+1234567::280:10020030+N+20020701+20020
730'


## ◆ Kontoumsätze rückmelden/neue Umsätze

HIKAN:4:6:3+@362@<MT940>+@102@<MT942>'


## ◆ Kontoumsätze rückmelden/Zeitraum

HIKAZ:4:6:3+@362@<MT940>+@102@<MT942>'


## ◆ Kontoumsätze/neu Parameter

HIKANS:12:6:5+1+2+1+60:J:N'


## ◆ Kontoumsätze/Zeitraum Parameter

HIKAZS:11:6:5+1+2+1+60:J:J'


## . Kreditinstitutsangebote anfordern

HKKIA:4:4'


## . Kreditinstitutsangebote Parameter

HIKIAS:49:4:5+1+0+0'


## . Kreditinstitutsangebote rückmelden

HIKIA:5:4:5+3500 : Lebensversicherungen:T+3510 : All
gemei-

nes: T+3511: Infos zur Lebensversicherung: S+3512: T
ari-

fe für Lebensversicherungen:S+TDDSG:Unterrichtun
g über die Verarbeitung personenbezogener Daten
gemäß TDDSG:F'

<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: G</td>
<td>Version: 3.0-FV</td>
<td>Financial Transaction Services (FinTS) Dokument: Formals</td>
</tr>
<tr>
<td>Seite: 144</td>
<td>Stand: 06.10.2017</td>
<td>Kapitel: Syntax Abschnitt: Beispiele</td>
</tr>
</table>


## . Kreditinstitutsmeldung

HIKIM:10:2+ec-Karte+Ihre neue ec-Karte liegt zur
Abholung bereit.'

HIKIM:11:2+Dispokredit+Ihr Dispokredit wurde auf
5.000 Euro erhöht.'


## . Kundenmeldung

HKKDM:4:5++Bitte schicken Sie mir Ihre Allgemein
en Geschäftsbedingungen. Danke Ernst Müller'

HKKDM:5:5+1234567::280:10020030+Bitte erhöhen Si
e den Dispokredit meines Kontos auf 5.000 Euro+D
ispokre-
dit+Herr Meier, Geschäftstelle Hauptstraße'


## . Kundenmeldung Parameter

HIKDMS:47:5:5+1+2+1+1024'


## . Laden GeldKarte abmelden

HKLGA:4:2+280:1234567::10020030+@22@<Kartenident
ifikationsdaten>'


## . Laden GeldKarte abmelden Parameter

HILGAS: 12:2:5+1+2+1'


## ◆ Laden GeldKarte bestätigen

HKLGB:4:2+1234567890+@24@<Chiffre>'


## ◆ Laden GeldKarte bestätigen Antwort

HILGB:4:2+1234567890+@8@<Chiffre>'


## ◆ Laden GeldKarte bestätigen Parameter

HILGBS:12:2:5+1+0+0'


## . Laden GeldKarte durchführen

HKLGD:4:2+1234567890+@80@<Chiffre>'


## . Laden GeldKarte durchführen Antwort

HILGD:4:2+1234567890+@72@<Chiffre>'


## ◆ Laden GeldKarte durchführen Parameter

HILGDS:12:2:5+1+0+0'


## . Laden GeldKarte einleiten

HKLGE:4:2+1234567890+@16@<Chiffre>'

<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th rowspan="2">Version: 3.0-FV</th>
<th rowspan="2">Kapitel: G</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Formals</td>
</tr>
<tr>
<td>Kapitel: Abschnitt:</td>
<td>Syntax Beispiele</td>
<td>Stand: 06.10.2017</td>
<td>Seite: 145</td>
</tr>
</table>


## . Laden GeldKarte einleiten Antwort

HILGE:4:2+1234567890+@56@<Chiffre>'

. Laden GeldKarte einleiten Parameter

HILGES:12:2:5+1+0+0'

. Laden GeldKarte registrieren

HKLGR:4:2+280:1234567::10020030+@22@<Kartenident
ifikationsdaten>'


## . Laden GeldKarte registrieren Parameter

HILGRS:12:2:5+1+2+1'

. Laden GeldKarte Status

HILGS: 4:2+7+Ladevorgang abgeschlossen'


## . Laden GeldKarte Statusanfrage

HKLGS:4:2+HEIMGAA0815+@22@<Kartenidentifikations
daten>+@33@<Eintrag Ladelogdatei>'


## . Laden GeldKarte Statusanfrage Parameter

HILGSS:12:2:5+1+2+1'


## . Laden GeldKarte Storno bestätigen

HKLGX:4:2+1234567890+@24@<Geldkartenkommando>'


## . Laden GeldKarte Storno bestätigen Parameter

HILGXS:12:2:5+1+0+0'

. Laden GeldKarte Storno Bestätigung

HILGX:4:2+1234567890+@8@<Geldkartenkommando>'


## . Laden GeldKarte Storno durchführen

HKLGT:4:2+1234567890+@80@<Geldkartenkommando>'


## . Laden GeldKarte Storno durchführen Antwort

HILGT:4:2+1234567890+@72@<Geldkartenkommando>'

. Laden GeldKarte Storno durchführen Parameter

HILGTS:12:2:5+1+0+0'


## . Laden GeldKarte Storno vorbereiten

HKLGO:4:2+1234567890+@16@<Geldkartenkommando>'


## . Laden GeldKarte Storno vorbereiten Antwort

HILGO:4:2+1234567890+@56@<Geldkartenkommando>'

<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: G</td>
<td>Version: 3.0-FV</td>
<td>Financial Transaction Services (FinTS) Dokument: Formals</td>
</tr>
<tr>
<td>Seite: 146</td>
<td>Stand: 06.10.2017</td>
<td>Kapitel: Syntax Abschnitt: Beispiele</td>
</tr>
</table>


# . Laden GeldKarte Storno vorbereiten Parameter

HILGOS: 12:2:5+1+0+0'


## . Laden GeldKarte vorbereiten

HKLGV:4:2+1234567::280:10020030+@22@<Kartenident
ifikationsda-
ten>+200, :DEM+HEIMGAA0815+@1@<Geldkartenstatus>+
@16@<Sitzungsschlüssel skey1>'


## . Laden GeldKarte vorbereiten Antwort

HILGV:4:2+1234567890+@16@<Sitzungsschlüssel skey
2>'


## . Laden GeldKarte vorbereiten Parameter

HILGVS:12:2:5+1+0+0'


## . Life-Indikator

HKLIF:2:1'


## . Liste Neuemissionen

HINEA:5:2:4+2:666111+NeuerBörsenwert AG+2+J+EUR+
1+N+Maschinenbau+B+29, 9:EUR+voraussichtlich+Nenn
wertlo-

se Stückaktie mit Stimmrecht+20021121:120000+200
21126:120000++20021122:120000++20021215++100000
Stück+5%+1+22,1:EUR+25,4:EUR++100++5, +X-Bank AG+
vo-

rauss. 01.12.2002++Der Emittent haftet nicht für
die Richtigkeit der angegebene Informationen+ht
tp?://www.NeuerBoersenwert. com+XFRA : EUR:5, : :1+XD
US: EUR:10,::1'


## . Liste Neuemissionen anfordern

HKNEA:4:2+1234567::280:10020030+1:2:3'


## . Liste Neuemissionen Parameter

HINEAS:6:2:5+1+0+0+1:2:3'


## . Nachrichtenabschluss

HNHBS:5:1+3'


## . Nachrichtenkopf

HNHBK:1:3+000000000319+300+4711+3+4711:3'

<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th rowspan="2">Version: 3.0-FV</th>
<th rowspan="2">Kapitel: G</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Formals</td>
</tr>
<tr>
<td>Kapitel: Abschnitt:</td>
<td>Syntax Beispiele</td>
<td>Stand: 06.10.2017</td>
<td>Seite: 147</td>
</tr>
</table>


## . Neuemission zeichnen

HKNEZ:4:2+1234567::280:10020030+1234567++@565@<M
T 502>+Gerda Müller::Bahnhofstraße 17:12345:Berl
in+19581024++1::20021125:1+2:Aktien:20021125:1+2
: Neuemissionen : 20021126:2'


## . Neuemission zeichnen Parameter

HINEZS:6:2:5+1+2+2+J:N:1:J:N:10000,:EUR'


## . Orderanzeige

HIOAN:5:2:4+1234567::280:10020030+@512@<MT502>+N
+J+1234567++20020210:125430'


## . Orderanzeige anfordern

HKOAN:4:2+1234567::280:10020030+N+1234567'


## . Orderanzeige Parameter

HIOANS:6:2:5+1+2+1+J:180'


## . Orderstatus

HIWSO:5:3:4+1234567::280:10020030+6+N+J+1234567+
++20000215:103025+@512@<MT513>'

HIWSO:6:3:4+1234567::280:10020030+6+N+N+1234568+
3456789++20000217:163158++@346@<MT515>'


## . Orderstatus anfordern

HKWSO:4:3+1234567::280:10020030+N+J+N+++20021001
+20021010+1:2:3:4'


### . Orderstatus Parameter

HIWSOS:6:3:5+1+2+1+J:180:1:2:3:4:5:6'


#### ◆ PIN ändern

HKPAE:4:1+04321'


#### ◆ PIN ändern Parameter

HIPAES:4:1:5+1+1+0'


#### . PIN sperren

HKPSP:4:1'


### . PIN sperren Parameter

HIPSPS:4:1:5+1+2+0'


### . PIN-Sperre aufheben

HKPSA:4:1'

<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: G</td>
<td>Version: 3.0-FV</td>
<td>Financial Transaction Services (FinTS) Dokument: Formals</td>
</tr>
<tr>
<td>Seite: 148</td>
<td>Stand: 06.10.2017</td>
<td>Kapitel: Syntax Abschnitt: Beispiele</td>
</tr>
</table>


# . PIN-Sperre aufheben Parameter

HIPSAS:4:1:5+1+2+0'


# . PIN/TAN-spezifische Informationen

HIPINS:4:1:5+1+1+5:6:6:Kunden-Nr aus dem TAN-Bri
ef: :HKCCS:J:HKKAN:N:HKSAL:J:HKPAE:J:HKTLA:J:HKTL
F:J'


# ◆ Rückmeldung zu Segmenten

HIRMS:4:2:5+0010::Auftrag entgegengenommen '

HIRMS:5:2:6+9210:15:Kontonummer existiert nicht'


# ◆ Rückmeldung zur Gesamtnachricht

HIRMG:3:2+0010::Nachricht entgegengenommen '

HIRMG:3:2+9110::Unbekannter Nachrichtenaufbau'


# . Saldenabfrage

HKSAL:3:6+1234567::280:10020030+N'


## . Saldenabfrage Parameter

HISALS:13:6:5+1+2+1'


## ◆ Saldenrückmeldung

HISAL:4:6:3+1234567::280:10020030+Giro Spezial+E
UR+C:1000, :EUR:20020701+D:500, :EUR:20020701+5000
, : EUR+7138,35 : EUR+1476,98:EUR++20020501:121545'


## ◆ Schlüsseländerung

HKSAK:8:3+2+112+280:10020030:12345:S:1:1+6:16:10
:@12@<Modulus>:12:@3@<Exponent>:13'


# ◆ Schlüsselsperrung

HKSSP:8:3+2+130+280:10020030:12345:D:1:1+501'


# . Sicherheitsverfahren

HISHV:5:3:7+N+RDH: 3'


# . Signaturabschluss

Sicherheitsverfahren HBCI:
HNSHA:8:2+654321+@96@<Signatur>'

Sicherheitsverfahren PIN/TAN:

HNSHA:8:2+654321++83427:954378'

<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th rowspan="2">Version: 3.0-FV</th>
<th rowspan="2">Kapitel: G</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Formals</td>
</tr>
<tr>
<td>Kapitel: Abschnitt:</td>
<td>Syntax Beispiele</td>
<td>Stand: 06.10.2017</td>
<td>Seite: 149</td>
</tr>
</table>


# . Signaturkopf

HNSHK:2:4+1+654321+1+1+1::2+3234+1:20020605:1111
44+1:999:1+6:10:16+280:10020030:12345:S:1:1'


# . Sorten- und Reisescheckbestellung

HKSRB:4:2+1234567::280:10020030+2+1.0.2+2+Ernst
Mül-

ler::Bahnhofstr. 17:12345:Berlin++20020504+300,:
CHF::50,+1000,:USD:1'


# . Sorten- und Reisescheckbestellung Parameter

HISRBS:28:2:5+1+2+2+J:2:60:N:1;2;3:2;1;2;3'


# . Sorten- und Reisescheckkonditionen anfordern

HKSRK:3:2+2+CHF+EUR'


# . Sorten- und Reisescheckkonditionen Parameter

HISRKS:27:2:5+1+0+0+J:N:1:2'


# . Sorten- und Reisescheckkonditionen rückmelden

HISRK:3:2:3+2+CHF+Schweizer Franken Reiseschecks
+1+1+121, 147:EUR::20020901+122,243:EUR::20020901
+3+50, : CHF+50, : CHF+1+10000,:CHF+0++N+500,:200,:1
00,:50,+1:2:3+1.0.1:1::::10:EUR+1.0.2: 2::::7,5: E
UR'


# . Statusprotokoll anfordern

HKPRO:3:4+20020101+20020115'


# . Statusprotokoll Parameter

HIPROS:11:4:5+1+1+1'


# . Statusprotokoll rückmelden

HIPRO:4:4:3+4711:3+4+20020210+113025+0020: :Auftr
ag ausgeführt'

HIPRO:5:4:3+4711:3+5+20020210+113025+9210:3,1: Ko
ntonummer ungültig'


# . Synchronisierung

HKSYN:8:2+1'


# . Synchronisierungsantwort

HISYN:10:3:8+2'

HISYN:10:3:8++3'

<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: G</td>
<td>Version: 3.0-FV</td>
<td>Financial Transaction Services (FinTS) Dokument: Formals</td>
</tr>
<tr>
<td>Seite: 150</td>
<td>Stand: 06.10.2017</td>
<td>Kapitel: Syntax Abschnitt: Beispiele</td>
</tr>
</table>


# . TAN-Verbrauchsinformationen anfordern

HKTAZ:4:1'


## . TAN-Verbrauchsinformationen Parameter

HITAZS:4:1:5+1+2+0'


## . TAN-Verbrauchsinformationen rückmelden

HITAZ:4:1+A+4711+20010102+50+2+8:TAN1:20010509:1
03020+5:TAN2:20010619:114010+0+0'


## . Terminvereinbarung

HKTMV:4:3+1234567::280:10020030+20020701+160000+
+Herr Schulze+0228-1234567++Wertpapierberatung'


### . Terminvereinbarung Parameter

HITMVS:51:3:5+1+2+1'


### ◆ Übermittlung eines öffentlichen Schlüssels

HIISA:8:3:8+1+4711+1+224+280:10020030:12345:D:1:
1+6:17:10:@12@<Modulus>:12:@3@<Exponent>:13'


### . Userparameter allgemein

HIUPA:14:3:7+12345+4+0+Herr Meier'


#### . Verarbeitungsvorbereitung

HKVVB:7:2+2+3+1+Homebanking Plus+3.0'


#### ◆ Verschlüsselte Daten

HNVSD:999:1+@348@<Daten, verschlüsselt>'


#### ◆ Verschlüsselungskopf

HNVSK:998:3+4+1+1::1+1:20020610:102044+2:18:13:@
96@<chiffrierter Schlüssel>:6:1+280:10020030:123
45:V:1:1+0'


#### . Vordruckbestellung

HKVDB:3:3+1234567::280:10020030+2+10+20+N+Ernst
Müller::Bahnhofstr. 17:12345:Berlin'


### . Vordruckbestellung Parameter

HIVDBS:34:3:5+1+2+2+10:ec-Scheck:N:11:Barscheck:
J:12:Verrechnungsscheck:J:13:Überweisungsformula
r : J'


### . Wertpapierinformationen anfordern

HKWPI:4:3++2:723600'

<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th rowspan="2">Version: 3.0-FV</th>
<th rowspan="2">Kapitel: G</th>
</tr>
<tr>
<th>Dokument:</th>
<th>Formals</th>
</tr>
<tr>
<td>Kapitel: Abschnitt:</td>
<td>Syntax Beispiele</td>
<td>Stand: 06.10.2017</td>
<td>Seite: 151</td>
</tr>
</table>


# . Wertpapierinformationen Parameter

HIWPIS:6:3:5+1+2+1+J'


## ◆ Wertpapierinformationen rückmelden

HIWPI:5:3:4+2:723600+Siemens+Wertentwicklung der
letz-
ten 12 Monate+jpg+@485@<Grafik>+http?://www.siem
ens.de'


## . Wertpapierkurse anfordern

HKWPK:4:3++2:723600+XFRA'


## . Wertpapierkurse Parameter

HIWPKS:6:3:5+1+2+1+N : J : XFRA;XDUS; XISE; XNYS ; XTKS :
DAX-Werte:REX-Werte'


## . Wertpapierkurse rückmelden

HIWPK:5:3:4+2:723600+Siemens AG Stammaktie+XFRA+
1+1+340569,+123, 6 : EUR:b:20021112:112357+123,1:EU
R: :20021112+123,5:EUR::20021112+123,9:EUR::20021
112+124, 1:EUR::20021112+129, 8:EUR::20021111+143,
9: EUR::20020605+105,1: EUR::20020317'


## . Wertpapierorder einreichen

HKWPO:4:3+1234567::280:10020030+++@378@<MT502>+1
234568::280:10020030+1::20021012:1+2:Aktien:2002
1012:1'


### . Wertpapierorder Parameter

HIWPOS:6:3:5+1+2+2+0:J:2:J:N:XFRA;XDUS; XISE;XNYS
; XTKS; OTCO : 180: 2:10000, : EUR: MAKT; LMTO; STLI: ALNO;
CARE; FIKI : GTMO; GTHD; CLOS; OPEN'


### ◆ Wertpapierorderänderung

HKWOA:4:3+1234567::280:10020030++7654321+LMTO+13
5,:EUR+++++030/1234567+1::20021012:1+2:Aktien:20
021012:1'


### ◆ Wertpapierorderänderung bestätigen

HIWOA:5:3:4+N+2345678+1234567+++1'


### ◆ Wertpapierorderänderung Parameter

HIWOAS:6:3:5+1+2+2+J:MAKT;LMTO :J:J:GTMO; GTHD ; CLO
S; OPEN: N:1:J:J:J:10000, :EUR'

<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: G</td>
<td>Version: 3.0-FV</td>
<td>Financial Transaction Services (FinTS) Dokument: Formals</td>
</tr>
<tr>
<td>Seite: 152</td>
<td>Stand: 06.10.2017</td>
<td>Kapitel: Syntax Abschnitt: Beispiele</td>
</tr>
</table>


### . Wertpapierordereinreichung bestätigen

HIWPO:5:3:4+J+1234567+++6'


### . Wertpapierorderhistorie anfordern

HKWOH:4:3+1234567::280:10020030+N++7654321'


### . Wertpapierorderhistorie Parameter

HIWOHS:6:3:5+1+2+1+J:60'


### ◆ Wertpapierorderhistorie rückmelden

HIWOH:5:3:4+2+N+@372@<MT502>+1234567++20020712:1
11837'

HIWOH:5:3:5+2+N+@372@<MT502>+1234567++20020713:1
52142'


### . Wertpapierorderstreichung

HKWPS:4:3+1234567::280:10020030++7654321+1::2002
1012:1+2:Aktien:20021012:1'


#### . Wertpapierorderstreichung bestätigen

HIWPS:5:3:4+J+1234567++7'


#### . Wertpapierorderstreichung Parameter

HIWPSS:6:3:5+1+2+2+J:N'


#### . Wertpapierreferenznummern anfordern

HKWPR:4:3+Si+0+Aktien:Renten+N+N+XFRA'


#### . Wertpapierreferenznummern Parameter

HIWPRS:6:3:5+1+0+0+J:J:N:N:XFRA;XDUS ; XISE; XNYS; X
TKS:Aktien:Renten:Optionen'


#### . Wertpapierreferenznummern rückmelden

HIWPR:5:3:3+Siemens Stamm+J+J+J+1: 123456789012+2
:723600'

HIWPR:6:3:3+Siemens Vorzüge+J+J+N+1:123456789013
+2:723601'


#### . Wertpapierstammdaten anfordern

HKWSD:4:3++2:723600'


#### . Wertpapierstammdaten Parameter

HIWSDS:6:3:5+1+2+1+N : A; Inland DAX : B; Inland Sonst
ige: C; Ausland Europa : D; Ausland Sonstige'

<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th rowspan="2">Version: 3.0-FV</th>
<th rowspan="2">Kapitel: G</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Formals</td>
</tr>
<tr>
<td>Kapitel: Abschnitt:</td>
<td>Syntax Beispiele</td>
<td>Stand: 06.10.2017</td>
<td>Seite: 153</td>
</tr>
</table>


# ◆ Wertpapierstammdaten rückmelden

HIWSD:5:3:4+2:723600+Siemens AG Stammaktie+1+1+5
22+03+Deutsche Inhaberaktien (Stücknotiz) +EUR+EU
R+3+B+555555++XFRA:50,:1:2000000,: EUR:7,:2002021
5++++XFRA: EUR: ::5,: :1+XDUS: EUR: ::10,: :1'


# . Wichtige Informationen anfordern

HKWPH:4:3+1234567::280:10020030+1234567++1::2000
0215:1+2:Aktien:20000217:2'


# . Wichtige Informationen Parameter

HIWPHS:5:3:5+1+2+1+1+N:J:Aktien:Renten:Optionen'


# ◆ Wichtige Informationen rückmelden

HIWPH:5:3:4+1::20000218:1:Keine besonderen Hinwe
ise+2:Aktien:20000218:1:18.02.00?1: DaimlerChrysl
er?: Heute Veröffentlichung des Quartalsergebnis
ses+2:Renten:20000217:1:17.02.00?: Bundesbank be
schließt Leitzinssenkung'

<!-- PageFooter: 1 Das Fragezeichen ist auf eine syntaktische Entwertung des Doppelpunktes zurückzuführen. -->
<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: G</td>
<td>Version: 3.0-FV</td>
<td>Financial Transaction Services (FinTS) Dokument: Formals</td>
</tr>
<tr>
<td>Seite: 154</td>
<td>Stand: 06.10.2017</td>
<td>Kapitel: Syntax Abschnitt: Beispiele</td>
</tr>
</table>


## H.2.3 Segmentfolgen


### ◆ Aufträge

HKKAZ:4:6+1234567::280:10020030+20020701+2002073
0'

HKSAL:5:6+1234567::280:10020030+N'


### . Bankparameterdaten

HIBPA:4:3:4+3+280:10020030+Musterbank in Musters
tadt+1+1:2:3+201:210:220:300+100'

HIKOM:5:4:4+280:10020030+1+1:12345678:00+2:12345
679:00+3:123.123.123.123 : :UUE:1'

HISHV:6:3:4+N+RDH:3'

HICSES:7:4:4+1+2+7:51:53:54:67:69'

HICSES:8:5:4+1+2+2+14:51:53:54:67:69'

HILASS:9:5:4+1+2+2+14:04:05'

HISUBS:10:6:4+1+2+2+999:14:51:53:54'

HISLAS:11:6:4+1+2+2+99:14:04:05'

HIKAZS:12:6:4+1+2+1+60:J'

HIKANS:13:6:4+1+2+1+60:J'

HISALS:14:6:4+1+2+1'


### . Datensegmente

HIKAZ:4:6:3+@362@<MT 940>+@102@<MT 942>'

HISAL:5:6:4+1234567::280:10020030+Giro Spezial+E
UR+C:1000, :EUR:20020701+D:500, :EUR:20020701+5000
, : EUR+7138,35 : EUR+1476,98 : EUR'

HIDAB:6:4:5+1234567::280:10020030+7654321::280:2
0030040+MEIER FRANZ++1000,:EUR+52+000+MIETE : UND
NEBENKOSTEN+20020901+00001+20020701:M:1:1:200306
01+N: ::3'


#### . Parameterdaten

HICSES:6:4:5+1+2+7:51:53:54:67:69'

HICSES:7:5:5+1+2+2+14:51:53:54:67:69'

HIKAZS:8:6:5+1+2+1+60:J'

HISALS:9:6:5+1+2+1'

<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th rowspan="2">Version: 3.0-FV</th>
<th rowspan="2">Kapitel: G</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Formals</td>
</tr>
<tr>
<td>Kapitel: Abschnitt:</td>
<td>Syntax Beispiele</td>
<td>Stand: 06.10.2017</td>
<td>Seite: 155</td>
</tr>
</table>


# . Userparameterdaten

HIUPA:15:3:4+12345+4+0+Herr Meier'

HIUPD:16:5:4+1234567:280:10020030+12345+1+EUR+Er
nst Müller++Giro Spezial+T:2000, :EUR+HKPRO : 1+HKS
AK:1+HKISA:1+HKSSP: 1+HKCCS:1+HKLAS:1+HKKAN: 1+HKK
AZ:1+HKSAL:1'

HIUPD:17:5:4+1234568:280:10020030+12345+10+EUR+E
rnst Müller++Sparkonto 2000++HKPRO:1+HKSAK: 0+HKI
SA:1+HKSSP:0+HKKAN:1+HKKAZ:1+HKSAL:2'

<!-- PageBreak -->


<table>
<tr>
<th>Kapitel: G</th>
<th>Version: 3.0-FV</th>
<th>Financial Transaction Services (FinTS) Dokument: Formals</th>
</tr>
<tr>
<td>Seite: 156</td>
<td>Stand: 06.10.2017</td>
<td>Kapitel: Syntax Abschnitt: Beispiele</td>
</tr>
</table>


## H.2.4 Dialog

Im Beispiel arbeitet der Kunde mit einem Sicherheitsmedium, das asymmetrische
Sicherheitsverfahren (RDH) unterstützt.


### H.2.4.1 Nachricht ,,Dialoginitialisierung"


#### a) Kundennachricht

Die Kundennachricht wird von dem Benutzer mit der Kennung '12345' signiert.
Segment: Nachrichtenkopf2

HNHBK:1:3+000000000323+300+0+1'

Segment: Verschlüsselungskopf

HNVSK:998:2+4+1+1::2+1:20020610:102044+2:18:13:@
8@<X'00 00 00 00 00 00 00 00'>:5:1+280:10020030:
12345:V:1:1+0'

Segment: Verschlüsselte Daten

HNVSD:999:1+@348@<Daten>13

Segment: Signaturkopf

HNSHK:2:4+2+654321+1+1+1::2+3234+1:20020701:1111
44+1:999:1+6:10:17+280:10020030:12345:S:1:1'

Segment: Identifikation

HKIDN:3:2+280:10020030+12345+2+1'

Segment: Verarbeitungsvorbereitung

HKVVB:4:2+2+3+1+Homebanking Plus+3.0'

Segment: Zwei-Schritt-TAN-Einreichung

HKTAN:5:6+4+HKIDN+++1234567890ABCDEF'

Segment: Anforderung eines öffentlichen Schlüssels (Signierschlüssel)

HKISA:6:3+2+124+RDH:3+280:10020030:11111:D:1:1'

Segment: Anforderung eines öffentlichen Schlüssels (Authentikationsschlüssel)

HKISA:7:3+2+124+RDH:3+280:10020030:11111:S :1:1'

Segment: Anforderung eines öffentlichen Schlüssels (Chiffrierschlüssel)

<!-- PageFooter: 2 Aus Gründen der Übersichtlichkeit beginnen Segmente in diesem Beispiel jeweils in einer neuen Zeile. Dies bedeutet jedoch nicht, dass Segmente syntaktisch mit einem Zeilenvorschub beendet werden. -->
<!-- PageFooter: 3 <Daten> enthält hier und in allen weiteren Nachrichten jeweils alle nachfolgenden Segmente mit Ausnahme des Nachrichtenabschlusses -->
<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th rowspan="2">Version: 3.0-FV</th>
<th rowspan="2">Kapitel: G</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Formals</td>
</tr>
<tr>
<td>Kapitel:</td>
<td>Syntax</td>
<td>Stand:</td>
<td>Seite:</td>
</tr>
<tr>
<td>Abschnitt:</td>
<td>Beispiele</td>
<td>06.10.2017</td>
<td>157</td>
</tr>
</table>


HKISA:8:3+2+124+RDH:3+280:10020030:11111:V:1:1'

Segment: Signaturabschluss

HNSHA:9:1+654321+@96@<Signatur>'

Segment: Nachrichtenabschluss

HNHBS : 10:1+1'


#### b) Kreditinstitutsnachricht

Der Kunde erhält zusätzlich jeweils die aktuellen Bankparameterdaten, Userpara-
meterdaten und den aktuellen Signierschlüssel.

Segment: Nachrichtenkopf

HNHBK:1:3+000000000932+300+4711+1+4711:1'

Segment: Verschlüsselungskopf

HNVSK:998:2+4+1+1::2+1:20020610:102044+2:18:13:@
8@<X'00 00 00 00 00 00 00 00'>:5:1+280:10020030:
12345:V:1:1+0'

Segment: Verschlüsselte Daten

HNVSD:999:1+@348@<Daten>'

Segment: Signaturkopf

HNSHK:2:4+2+123456+1+1+1::2+3234+1:20020701:1111
45+1:999:1+6:10:17+280:10020030:1:S:1:1'

Segment: Rückmeldungen zur Gesamtnachricht

HIRMG:3:2+0010::Nachricht entgegengenommen '

Segment: Rückmeldungen zu Segmenten


#### Segmentfolge: Bankparameterdaten

HIBPA:4:3:4+3+280:10020030+Musterbank in Musters
tadt+1+1:2:3+201:210:220:300+100'

HIKOM:5:4:2+280:10020030+1+1:12345678:00+2:123.1
23.123.123::UUE:1+2:www.bankname.de:: UUE:1'

HISHV:6:3:4+N+RDH: 3'

HICSES:7:4:4+1+2+7:51:53:54:67:69'

HICSES:8:5:4+1+2+2+14:51:53:54:67:69'

HILASS:9:5:4+1+2+2+14:04:05'

HISUBS:10:6:4+1+2+2+999:14:51:53:54'

<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: G</td>
<td>Version: 3.0-FV</td>
<td>Financial Transaction Services (FinTS) Dokument: Formals</td>
</tr>
<tr>
<td>Seite: 158</td>
<td>Stand: 06.10.2017</td>
<td>Kapitel: Syntax Abschnitt: Beispiele</td>
</tr>
</table>


HISLAS:11:6:4+1+2+2+99:14:04:05'

HIKAZS:12:6:4+1+2+1+60:J'

HIKANS:13:6:4+1+2+1+60:J'

HISALS:14:6:4+1+2+1'


##### Segmentfolge: Userparameterdaten

HIUPA:15:3:4+12345+4+0+Herr Meier'

HIUPD:16:5:4+1234567:280:10020030+12345+1+EUR+Er
nst Müller++Giro Spezial+T:2000, :EUR+HKPRO : 1+HKS
AK:1+HKISA:1+HKSSP:1+HKLAS: 1+HKKAN:1+HKKAZ:1+HKS
AL:1'

HIUPD:17:5:4+1234568:280:10020030+12345+10+EUR+E
rnst Müller++Sparkonto 2000++HKPRO:1+HKSAK:0+HKI
SA:1+HKSSP:0+HKKAN:1+HKKAZ:1+HKSAL:2'


##### Segment: Übermittlung eines öffentlichen Schlüssels (DS-Schlüssel)

HIISA:18:3:5+1+333+1+224+280:10020030:11111:D:1:
1+6:17:10:@96@<Modulus>:12:@5@<Exponent>:13'

Segment: Übermittlung eines öffentlichen Schlüssels (Signierschlüssel)

HIISA:19:3:5+1+333+1+224+280:10020030:11111:S:1:
1+6:17:10:@96@<Modulus>:12:@5@<Exponent>:13'

Segment: Übermittlung eines öffentlichen Schlüssels (Chiffrierschlüssel)4


##### Segment: Kreditinstitutsmeldung

HIKIM:20:2+Bausparförderung+Informieren Sie sich
über die neue Bausparförderung. '

Segment: Signaturabschluss

HNSHA:21:2+123456+@96@<Signatur>'

Segment: Nachrichtenabschluss

HNHBS:22:1+1'

<!-- PageFooter: 4 Es wird angenommen, dass der öffentliche Chiffrierschlüssel noch aktuell ist, und daher nicht aktu- alisiert werden muss. -->
<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th rowspan="2">Version: 3.0-FV</th>
<th rowspan="2">Kapitel: G</th>
</tr>
<tr>
<th>Dokument:</th>
<th>Formals</th>
</tr>
<tr>
<td>Kapitel: Abschnitt:</td>
<td>Syntax Beispiele</td>
<td>Stand: 06.10.2017</td>
<td>Seite: 159</td>
</tr>
</table>


### H.2.4.2 Nachricht ,,SEPA-Einzelüberweisung“


#### a) Kundennachricht

Diese Nachricht wird sowohl von Benutzer '12345' als auch von Benutzer '76543'
signiert.

Segment: Nachrichtenkopf

HNHBK:1:3+000000000523+300+4711+2'

Segment: Verschlüsselungskopf

HNVSK:998:2+4+1+1::2+1:20020610:102044+2:18:13:@
8@<X'00 00 00 00 00 00 00 00'>:5:1+280:10020030:
12345:V:1:1+0'

Segment: Verschlüsselte Daten

HNVSD:999:1+@348@<Daten>'

Segment: Signaturkopf für Benutzer '76543'

HNSHK:2:4+1+765432+1+1+1::2+3234+1:20020701:1111
46+1:999:1+6:10:17+280:10020030:76543:D:1:1'

Segment: Signaturkopf für Benutzer '12345'

HNSHK:3:4+1+654321+1+1+1::2+3234+1:20020701:1111
47+1:999:1+6:10:17+280:10020030:12345:D:1:1'

Segment: SEPA-Einzelüberweisung

HKCCS:4:1+1234567+Depp100200300987654321+urn?:is
o?:std?:iso?:20022?:tech?:xsd?:pain.001.001.03+@
lll@<SEPA Single Credit Transfer message>'

Segment: Signaturabschluss für Benutzer '12345'

HNSHA:5:2+654321+@96@<Signatur>'

Segment: Signaturabschluss für Benutzer '76543'

HNSHA:6:2+765432+@96@<Signatur>'

Segment: Nachrichtenabschluss

HNHBS : 7:1+2'


#### b) Kreditinstitutsnachricht

Segment: Nachrichtenkopf
HNHBK:1:3+000000000140+300+4711+2+4711:2'

<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: G</td>
<td>Version: 3.0-FV</td>
<td>Financial Transaction Services (FinTS) Dokument: Formals</td>
</tr>
<tr>
<td>Seite: 160</td>
<td>Stand: 06.10.2017</td>
<td>Kapitel: Syntax Abschnitt: Beispiele</td>
</tr>
</table>


##### Segment: Verschlüsselungskopf

HNVSK:998:2+4+1+1::2+1:20020610:102044+2:18:13:@
8@<X'00 00 00 00 00 00 00 00'>:5:1+280:10020030:
12345:V:1:1+0'

Segment: Verschlüsselte Daten

HNVSD:999:1+@348@<Daten>'

Segment: Signaturkopf

HNSHK:2:4+1+123457+1+1+1::2+3234+1:20020701:1111
48+1:999:1+6:10:17+280:10020030:1:S:1:1'

Segment: Rückmeldungen zur Gesamtnachricht

HIRMG:3:2+0010::Nachricht entgegengenommen '

Segment: Rückmeldungen zu Segmenten

HIRMS:4:2:4+0010::Auftrag entgegengenommen'

Segment: Datensegmente

Segment: Signaturabschluss

HNSHA:5:2+123457+@96@<Signatur>'

Segment: Nachrichtenabschluss

HNHBS:6:1+2'


### H.2.4.3 Nachricht ,,Saldenabfrage"


#### a) Kundennachricht

Die Kundennachricht wird nur von Benutzer '12345' signiert.

Segment: Nachrichtenkopf

HNHBK:1:3+000000000257+300+4711+3'

Segment: Verschlüsselungskopf

HNVSK:998:2+4+1+1::2+1:20020610:102044+2:18:13:@
8@<X'00 00 00 00 00 00 00 00'>:5:1+280:10020030:
12345:V:1:1+0'

Segment: Verschlüsselte Daten
HNVSD:999:1+@348@<Daten>'

<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th rowspan="2">Version: 3.0-FV</th>
<th rowspan="2">Kapitel: G</th>
</tr>
<tr>
<th>Dokument:</th>
<th>Formals</th>
</tr>
<tr>
<td>Kapitel: Abschnitt:</td>
<td>Syntax Beispiele</td>
<td>Stand: 06.10.2017</td>
<td>Seite: 161</td>
</tr>
</table>


##### Segment: Signaturkopf

HNSHK:2:4+1+654321+1+1+1::2+3234+1:20020701:1111
49+1:999:1+6:10:17+280:10020030:12345:S:1:1'

Segment: Saldenabfrage

HKSAL:3:6+1234567::280:10020030+N'

Segment: Signaturabschluss

HNSHA:4:2+654321+@96@<Signatur>'

Segment: Nachrichtenabschluss

HNHBS:5:1+3'


#### b) Kreditinstitutsnachricht

Segment: Nachrichtenkopf

HNHBK:1:3+000000000213+300+4711+3+4711:3'

Segment: Verschlüsselungskopf

HNVSK:998:2+4+1+1::2+1:20020610:102044+2:18:13:@
8@<X'00 00 00 00 00 00 00 00'>:5:1+280:10020030:
12345:V:1:1+0'

Segment: Verschlüsselte Daten

HNVSD:999:1+@348@<Daten>'

Segment: Signaturkopf

HNSHK:2:4+1+123458+1+1+1::2+3234+1:20020701:1111
50+1:999:1+6:10:17+280:10020030:1:S:1:1'

Segment: Rückmeldungen zur Gesamtnachricht

HIRMG:3:2+0010::Nachricht entgegengenommen'

Segment: Rückmeldungen zu Segmenten

HIRMS:4:2:3+0020::Auftrag ausgeführt'

Segment: Datensegmente

HISAL:5:6:3+1234567::280:10020030+Giro Spezial+E

UR+C:1000, :EUR:20020701+D:500,:EUR:20020701+5000
, : EUR+7138,35: EUR+1476,98 : EUR'

Segment: Signaturabschluss

HNSHA:6:2+123458+@96@<Signatur>'

<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: G</td>
<td>Version: 3.0-FV</td>
<td>Financial Transaction Services (FinTS) Dokument: Formals</td>
</tr>
<tr>
<td>Seite: 162</td>
<td>Stand: 06.10.2017</td>
<td>Kapitel: Syntax Abschnitt: Beispiele</td>
</tr>
</table>


Segment: Nachrichtenabschluss

HNHBS : 7:1+3'


### H.2.4.4 Nachricht ,,Dialogbeendigung"


#### a) Kundennachricht

Segment: Nachrichtenkopf

HNHBK:1:3+0000000000475+300+4711+4'

Segment: Verschlüsselungskopf

HNVSK:998:2+4+1+1::2+1:20020610:102044+2:18:13:@
8@<X'00 00 00 00 00 00 00 00'>:5:1+280:10020030:
12345:V:1:1+0'

Segment: Verschlüsselte Daten

HNVSD:999:1+@348@<Daten>'

Segment: Signaturkopf

HNSHK:2:4+2+654321+1+1+1::2+3234+1:20020701:1111
51+1:999:1+6:10:17+280:10020030:12345:S:1:1'

Segment: Dialogende

HKEND:3:1+4711'

Segment: Signaturabschluss

HNSHA:4:2+654321+@96@<Signatur>'

Segment: Nachrichtenabschluss

HNHBS:5:1+4'


#### b) Kreditinstitutsnachricht

Segment: Nachrichtenkopf
HNHBK:1:3+000000000385+300+4711+4+4711:4'

Segment: Verschlüsselungskopf

HNVSK:998:2+4+1+1::2+1:20020610:102044+2:18:13:@
8@<X'00 00 00 00 00 00 00 00'>:5:1+280:10020030:
12345:V:1:1+0'

Segment: Verschlüsselte Daten

HNVSD:999:1+@348@<Daten>'

Segment: Signaturkopf

<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th rowspan="2">Version: 3.0-FV</th>
<th rowspan="2">Kapitel: G</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Formals</td>
</tr>
<tr>
<td>Kapitel:</td>
<td>Syntax</td>
<td>Stand:</td>
<td>Seite:</td>
</tr>
<tr>
<td>Abschnitt:</td>
<td>Beispiele</td>
<td>06.10.2017</td>
<td>163</td>
</tr>
</table>


HNSHK:2:4+2+123459+1+1+1::2+3234+1:20020701:1111
51+1:999:1+6:10:17+280:10020030:1:S:1:1'

Segment: Rückmeldungen zur Gesamtnachricht

HIRMG:3:2+0100::Dialog beendet'

Segment: Rückmeldungen zu Segmenten

HIRMS:4:2:3+0020::Auftrag ausgeführt'

Segment: Datensegmente

Segment: Signaturabschluss

HNSHA:5:2+123459+@96@<Signatur>'

Segment: Nachrichtenabschluss
HNHBS : 6:1+4'

<!-- PageBreak -->

<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th rowspan="2">Version: 3.0-FV</th>
<th rowspan="2">Kapitel: H</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Formals</td>
</tr>
<tr>
<td>Kapitel:</td>
<td>Anlagen</td>
<td>Stand:</td>
<td>Seite:</td>
</tr>
<tr>
<td>Abschnitt:</td>
<td>Übersicht der FinTS-Elemente</td>
<td>06.10.2017</td>
<td>165</td>
</tr>
</table>


# I. ANLAGEN


## I.1 Übersicht der FinTS-Elemente


### I.1.1 Nachrichten


<table>
<tr>
<th>Nr.</th>
<th>Name</th>
<th>Ken- nung</th>
<th>Sender</th>
<th>Version</th>
</tr>
<tr>
<td>1</td>
<td>Abbruchnachricht</td>
<td>N21</td>
<td>I</td>
<td>1</td>
</tr>
<tr>
<td>2</td>
<td>Änderung eines öffentlichen Schlüssels des Kunden</td>
<td>N1</td>
<td>K</td>
<td>4</td>
</tr>
<tr>
<td>3</td>
<td>Antwort auf Dialoginitialisierung</td>
<td>N2</td>
<td>I</td>
<td>4</td>
</tr>
<tr>
<td>4</td>
<td>Antwort auf anonyme Dialoginitialisierung</td>
<td>N3</td>
<td>I</td>
<td>3</td>
</tr>
<tr>
<td>5</td>
<td>Antwort auf Kommunikationszugang</td>
<td>N4</td>
<td>I</td>
<td>4</td>
</tr>
<tr>
<td>6</td>
<td>Bestätigung der Schlüsselsperrung durch das Kreditinsti- tut</td>
<td>N5</td>
<td>I</td>
<td>4</td>
</tr>
<tr>
<td>7</td>
<td>Dialoginitialisierung</td>
<td>N6</td>
<td>K</td>
<td>4</td>
</tr>
<tr>
<td>8</td>
<td>Dialoginitialisierung bei anonymem Zugang</td>
<td>N7</td>
<td>K</td>
<td>3</td>
</tr>
<tr>
<td>9</td>
<td>Dialogbeendigung</td>
<td>N8</td>
<td>K</td>
<td>3</td>
</tr>
<tr>
<td>10</td>
<td>Dialogbeendigung bei anonymem Zugang</td>
<td>N9</td>
<td>K</td>
<td>3</td>
</tr>
<tr>
<td>11</td>
<td>Erstmalige Anforderung der Schlüssel des Kreditinstituts</td>
<td>N10</td>
<td>K</td>
<td>4</td>
</tr>
<tr>
<td>12</td>
<td>Erstmalige Übermittlung der Schlüssel des Kreditinstituts</td>
<td>N11</td>
<td>I</td>
<td>4</td>
</tr>
<tr>
<td>13</td>
<td>Erstmalige Übermittlung der Schlüssel des Kunden</td>
<td>N12</td>
<td>K</td>
<td>4</td>
</tr>
<tr>
<td>14</td>
<td>Kommunikationszugang</td>
<td>N13</td>
<td>K</td>
<td>4</td>
</tr>
<tr>
<td>15</td>
<td>Kreditinstitutsnachricht allgemein</td>
<td>N14</td>
<td>I</td>
<td>4</td>
</tr>
<tr>
<td>16</td>
<td>Kundennachricht allgemein</td>
<td>N15</td>
<td>K</td>
<td>4</td>
</tr>
<tr>
<td>17</td>
<td>Kundennachricht allgemein bei anonymem Zugang</td>
<td>N16</td>
<td>K</td>
<td>4</td>
</tr>
<tr>
<td>18</td>
<td>Life-Indikator-Nachricht</td>
<td>N22</td>
<td>K</td>
<td>1</td>
</tr>
<tr>
<td>19</td>
<td>Sperrung eines Schlüssels durch den Kunden</td>
<td>N17</td>
<td>K</td>
<td>4</td>
</tr>
<tr>
<td>20</td>
<td>Synchronisierungsnachricht</td>
<td>N18</td>
<td>K</td>
<td>4</td>
</tr>
<tr>
<td>21</td>
<td>Synchronisierungsantwortnachricht</td>
<td>N19</td>
<td>I</td>
<td>4</td>
</tr>
<tr>
<td>22</td>
<td>Verschlüsselte Nachricht</td>
<td>N20</td>
<td>K/I</td>
<td>3</td>
</tr>
</table>


<!-- PageFooter: 1 K: Kunde, I: Kreditinstitut -->
<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: H</td>
<td>Version: 3.0-FV</td>
<td>Financial Transaction Services (FinTS) Dokument: Formals</td>
</tr>
<tr>
<td>Seite:<br>166</td>
<td>Stand: 06.10.2017</td>
<td>Kapitel: Anlagen<br>Abschnitt: Übersicht der FinTS-Elemente</td>
</tr>
</table>


### I.1.2 Segmentfolgen


<table>
<tr>
<th>Nr.</th>
<th>Name</th>
<th>Sender2</th>
<th>Version</th>
</tr>
<tr>
<td>1</td>
<td>Aufträge</td>
<td>K</td>
<td>2</td>
</tr>
<tr>
<td>2</td>
<td>Bankparameterdaten</td>
<td>I</td>
<td>3</td>
</tr>
<tr>
<td>3</td>
<td>Datensegmente</td>
<td>I</td>
<td>2</td>
</tr>
<tr>
<td>4</td>
<td>Parameterdaten</td>
<td>I</td>
<td>2</td>
</tr>
<tr>
<td>5</td>
<td>Userparameterdaten</td>
<td>I</td>
<td>3</td>
</tr>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th rowspan="2">Version: 3.0-FV</th>
<th rowspan="2">Kapitel: H</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Formals</td>
</tr>
<tr>
<td>Kapitel:</td>
<td>Anlagen</td>
<td>Stand:</td>
<td>Seite:</td>
</tr>
<tr>
<td>Abschnitt:</td>
<td>Übersicht der FinTS-Elemente</td>
<td>06.10.2017</td>
<td>167</td>
</tr>
</table>


### I.1.3 Segmente


<table>
<tr>
<th>Nr.</th>
<th>Segmentname</th>
<th>Kennung</th>
<th>Sen- der3</th>
<th>Version</th>
</tr>
<tr>
<td>1</td>
<td>Anforderung eines öffentlichen Schlüssels</td>
<td>HKISA</td>
<td>K</td>
<td>3</td>
</tr>
<tr>
<td>2</td>
<td>Bankparameter allgemein</td>
<td>HIBPA</td>
<td>I</td>
<td>3</td>
</tr>
<tr>
<td>3</td>
<td>Bestätigung der Schlüsselsperrung</td>
<td>HISSP</td>
<td>I</td>
<td>3</td>
</tr>
<tr>
<td>4</td>
<td>Dialogende</td>
<td>HKEND</td>
<td>K</td>
<td>1</td>
</tr>
<tr>
<td>5</td>
<td>Zwei-Schritt-TAN-Verfahren</td>
<td>HKTAN</td>
<td>K/I</td>
<td>6</td>
</tr>
<tr>
<td>6</td>
<td>Identifikation</td>
<td>HKIDN</td>
<td>K</td>
<td>2</td>
</tr>
<tr>
<td>7</td>
<td>Komprimierungsverfahren</td>
<td>HIKPV</td>
<td>I</td>
<td>1</td>
</tr>
<tr>
<td>8</td>
<td>Kommunikationszugang anfordern</td>
<td>HKKOM</td>
<td>K</td>
<td>4</td>
</tr>
<tr>
<td>9</td>
<td>Kommunikationszugang rückmelden</td>
<td>HIKOM</td>
<td>I</td>
<td>4</td>
</tr>
<tr>
<td>10</td>
<td>Kontoinformation</td>
<td>HIUPD</td>
<td>I</td>
<td>6</td>
</tr>
<tr>
<td>11</td>
<td>Kreditinstitutsmeldung</td>
<td>HIKIM</td>
<td>I</td>
<td>2</td>
</tr>
<tr>
<td>12</td>
<td>Life-Indikator</td>
<td>HKLIF</td>
<td>K</td>
<td>1</td>
</tr>
<tr>
<td>13</td>
<td>Nachrichtenkopf</td>
<td>HNHBK</td>
<td>K/I</td>
<td>3</td>
</tr>
<tr>
<td>14</td>
<td>Nachrichtenabschluss</td>
<td>HNHBS</td>
<td>K/I</td>
<td>1</td>
</tr>
<tr>
<td>15</td>
<td>Nachrichtenkopf</td>
<td>HNHBK</td>
<td>K/I</td>
<td>3</td>
</tr>
<tr>
<td>16</td>
<td>Rückmeldung zu Segmenten</td>
<td>HIRMS</td>
<td>I</td>
<td>2</td>
</tr>
<tr>
<td>17</td>
<td>Rückmeldungen zur Gesamtnachricht</td>
<td>HIRMG</td>
<td>I</td>
<td>2</td>
</tr>
<tr>
<td>18</td>
<td>Schlüsseländerung</td>
<td>HKSAK</td>
<td>K</td>
<td>3</td>
</tr>
<tr>
<td>19</td>
<td>Schlüsselsperrung</td>
<td>HKSSP</td>
<td>K</td>
<td>3</td>
</tr>
<tr>
<td>20</td>
<td>Sicherheitsverfahren</td>
<td>HISHV</td>
<td>I</td>
<td>3</td>
</tr>
<tr>
<td>21</td>
<td>Signaturabschluss</td>
<td>HNSHA</td>
<td>K/I</td>
<td>2</td>
</tr>
<tr>
<td>22</td>
<td>Signaturkopf</td>
<td>HNSHK</td>
<td>K/I</td>
<td>4</td>
</tr>
<tr>
<td>23</td>
<td>Synchronisierung</td>
<td>HKSYN</td>
<td>K</td>
<td>3</td>
</tr>
<tr>
<td>24</td>
<td>Synchronisierungsantwort</td>
<td>HISYN</td>
<td>I</td>
<td>4</td>
</tr>
<tr>
<td>25</td>
<td>Übermittlung eines öffentlichen Schlüssels</td>
<td>HIISA</td>
<td>I</td>
<td>3</td>
</tr>
<tr>
<td>26</td>
<td>Userparameter allgemein</td>
<td>HIUPA</td>
<td>I</td>
<td>4</td>
</tr>
<tr>
<td>27</td>
<td>Verarbeitungsvorbereitung</td>
<td>HKVVB</td>
<td>K</td>
<td>3</td>
</tr>
<tr>
<td>28</td>
<td>Verschlüsselte Daten</td>
<td>HNVSD</td>
<td>K/I</td>
<td>1</td>
</tr>
<tr>
<td>29</td>
<td>Verschlüsselungskopf</td>
<td>HNVSK</td>
<td>K/I</td>
<td>3</td>
</tr>
</table>


<!-- PageFooter: 3 K: Kunde, I: Kreditinstitut -->
<!-- PageBreak -->

<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th rowspan="2">Version: 3.0-FV</th>
<th rowspan="2">Kapitel: H</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Formals</td>
</tr>
<tr>
<td>Kapitel:</td>
<td>Anlagen</td>
<td>Stand:</td>
<td>Seite:</td>
</tr>
<tr>
<td>Abschnitt:</td>
<td>Übersicht Nachrichtenaufbau</td>
<td>06.10.2017</td>
<td>169</td>
</tr>
</table>


## I.2 Übersicht Nachrichtenaufbau

In den Tabellen ist zu den folgenden Dialogtypen jeweils die Reihenfolge und An-
zahl der möglichen Nachrichten und Segmente dargestellt:

. Standarddialog

. Anonymer Dialog

. Synchronisierung

· Kommunikationszugänge abholen

· Änderung eines öffentlichen Schlüssels des Kunden (HBCI RAH,RDH)

· Erstmalige Anforderung der öffentlichen Schlüssel des Kreditinstituts (HBCI RAH,
RDH)

· Erstmalige Übermittlung der öffentlichen Schlüssel des Kunden (HBCI RAH,
RDH)

· Schlüsselsperrung durch den Kunden (HBCI RAH, RDH)

· Schlüsselsperrung durch den Kunden (HBCI DDV)

Schreibweise in den Tabellen:

n: Beliebige Anzahl

m: Summe der Segmente der Kundennachricht

n/m: n gilt für symmetrische und m für asymmetrische Verfahren

Ob die Nachricht verschlüsselt wird, wird durch das Vorhandensein der Segmente
HNVSK und HNVSD angezeigt. In diesem Fall sind die verschlüsselten Segmente
eingerückt.

<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: H</td>
<td>Version: 3.0-FV</td>
<td>Financial Transaction Services (FinTS) Dokument: Formals</td>
</tr>
<tr>
<td>Seite: 170</td>
<td>Stand: 06.10.2017</td>
<td>Kapitel: Anlagen Abschnitt: Übersicht Nachrichtenaufbau</td>
</tr>
</table>


### I.2.1 Standarddialog


<table>
<tr>
<th rowspan="4">Segment</th>
<th colspan="6">Nachricht</th>
</tr>
<tr>
<th colspan="2">Dialoginitialisierung</th>
<th colspan="2">Auftragsnachricht</th>
<th colspan="2">Dialogbeendigung</th>
</tr>
<tr>
<th>Kunde</th>
<th>Kredit-</th>
<th>Kunde</th>
<th>Kredit-</th>
<th>Kunde</th>
<th>Kredit-</th>
</tr>
<tr>
<th>N6</th>
<th>N2</th>
<th>N15</th>
<th>N14</th>
<th>N8</th>
<th>N14</th>
</tr>
<tr>
<td>Nachricht</td>
<td>1</td>
<td>1</td>
<td>0-n</td>
<td>0-n</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td>HNHBK</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td>HNVSK</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td>HNVSD</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td>HNSHK</td>
<td>1</td>
<td>0-1</td>
<td>1-3</td>
<td>0-1</td>
<td>1</td>
<td>0-1</td>
</tr>
<tr>
<td>HIRMG</td>
<td>-</td>
<td>1</td>
<td>-</td>
<td>1</td>
<td>-</td>
<td>1</td>
</tr>
<tr>
<td>HIRMS</td>
<td>-</td>
<td>0-m</td>
<td>-</td>
<td>0-m</td>
<td>-</td>
<td>0-m</td>
</tr>
<tr>
<td>HKIDN</td>
<td>1</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HKVVB</td>
<td>1</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HKTAN</td>
<td>0/11</td>
<td>-</td>
<td>0/1</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HITAN</td>
<td></td>
<td>0/1</td>
<td>-</td>
<td>0/1</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HKISA</td>
<td>0/1-3</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HKSYN</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HIBPA</td>
<td>-</td>
<td>0-1</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HIKOM</td>
<td>-</td>
<td>0-1</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HISHV</td>
<td>-</td>
<td>0-1</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HIKPV</td>
<td>-</td>
<td>0-1</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HICSES</td>
<td>-</td>
<td>0-n</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>2<br>...</td>
<td>-</td>
<td>0-n</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HIUPA</td>
<td>-</td>
<td>0-1</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HIUPD</td>
<td>-</td>
<td>0-n</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HIISA</td>
<td>-</td>
<td>0/0-3</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HISYN</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HIKIM</td>
<td>-</td>
<td>0-n</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HKSAL3</td>
<td>-</td>
<td>-</td>
<td>1</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HISAL</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>0-n</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>...</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HKPRO</td>
<td>-</td>
<td>-</td>
<td>0-1</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HIPRO</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>0-n</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HKSAK</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HKSSP</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HISSP</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HKKOM</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HIKOM</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
</table>

1
Abhängig davon, ob für eine Auftragsnachricht eine starke Kundenauthentifizierung erforderlich ist,
sind die Segmente HKTAN und HITAN in der Nachricht enthalten.

2
Hier sind für die weiteren unterstützten Geschäftsvorfälle die entsprechenden Parameter-Segmente
einzustellen.

3
Exemplarisch wird hier der Geschäftsvorfall „Saldenabfrage“ angenommen.


<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th rowspan="2">Version: 3.0-FV</th>
<th rowspan="2">Kapitel: H</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Formals</td>
</tr>
<tr>
<td>Kapitel:</td>
<td>Anlagen</td>
<td>Stand:</td>
<td>Seite:</td>
</tr>
<tr>
<td>Abschnitt:</td>
<td>Übersicht Nachrichtenaufbau</td>
<td>06.10.2017</td>
<td>171</td>
</tr>
</table>


<table>
<tr>
<th rowspan="4">Segment</th>
<th colspan="6">Nachricht</th>
</tr>
<tr>
<th colspan="2">Dialoginitialisierung</th>
<th colspan="2">Auftragsnachricht</th>
<th colspan="2">Dialogbeendigung</th>
</tr>
<tr>
<th>Kunde</th>
<th>Kredit-</th>
<th>Kunde</th>
<th>Kredit-</th>
<th>Kunde</th>
<th>Kredit-</th>
</tr>
<tr>
<th>N6</th>
<th>N2</th>
<th>N15</th>
<th>N14</th>
<th>N8</th>
<th>N14</th>
</tr>
<tr>
<td>HKEND</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>1</td>
<td>-</td>
</tr>
<tr>
<td>HNSHA</td>
<td>1</td>
<td>0-1</td>
<td>1-3</td>
<td>0-1</td>
<td>1</td>
<td>0-1</td>
</tr>
<tr>
<td>HNHBS</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
</tr>
</table>


<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: H</td>
<td>Version: 3.0-FV</td>
<td>Financial Transaction Services (FinTS) Dokument: Formals</td>
</tr>
<tr>
<td>Seite: 172</td>
<td>Stand: 06.10.2017</td>
<td>Kapitel: Anlagen Abschnitt: Übersicht Nachrichtenaufbau</td>
</tr>
</table>


### I.2.2 Anonymer Dialog


<table>
<tr>
<th rowspan="4">Segment</th>
<th colspan="6">Nachricht</th>
</tr>
<tr>
<th colspan="2">Dialoginitialisierung</th>
<th colspan="2">Auftragsnachricht</th>
<th colspan="2">Dialogbeendigung</th>
</tr>
<tr>
<th>Kunde</th>
<th>Kredit- institut</th>
<th>Kunde</th>
<th>Kredit- institut</th>
<th>Kunde</th>
<th>Kredit- institut</th>
</tr>
<tr>
<th>N7</th>
<th>N3</th>
<th>N16</th>
<th>N14</th>
<th>N9</th>
<th>N14</th>
</tr>
<tr>
<td>Nachricht</td>
<td>1</td>
<td>1</td>
<td>0-n</td>
<td>0-n</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td>HNHBK</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td>HNSHK</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HIRMG</td>
<td>-</td>
<td>1</td>
<td>-</td>
<td>1</td>
<td>-</td>
<td>1</td>
</tr>
<tr>
<td>HIRMS</td>
<td>-</td>
<td>0-m</td>
<td>-</td>
<td>0-m</td>
<td>-</td>
<td>0-m</td>
</tr>
<tr>
<td>HKIDN</td>
<td>1</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HKVVB</td>
<td>1</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HKISA</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HKSYN</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HIBPA</td>
<td>-</td>
<td>0-1</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HIKOM</td>
<td>-</td>
<td>0-1</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HISHV</td>
<td>-</td>
<td>0-1</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HIKPV</td>
<td>-</td>
<td>0-1</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HICSES</td>
<td>-</td>
<td>0-n</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>...</td>
<td>-</td>
<td>0-n</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HIUPA</td>
<td>-</td>
<td>0-1</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HIUPD</td>
<td>-</td>
<td>0-n</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HIISA</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HISYN</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HIKIM</td>
<td>-</td>
<td>0-n</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HKSAL4</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HISAL</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>...</td>
<td>-</td>
<td>-</td>
<td>0-n</td>
<td>0-n</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HKPRO</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HIPRO</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HKSAK</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HKSSP</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HISSP</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HKKOM</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HIKOM</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HKEND</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>1</td>
<td>-</td>
</tr>
<tr>
<td>HNSHA</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HNHBS</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
</tr>
</table>

4
Der Kunde kann hier nicht-signierungspflichtige Auftragssegmente senden. Diese Geschäftsvorfälle
teilt das Kreditinstitut dem anonymen Kunden in der Gast-UPD mit.


<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th rowspan="2">Version: 3.0-FV</th>
<th rowspan="2">Kapitel: H</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Formals</td>
</tr>
<tr>
<td>Kapitel:</td>
<td>Anlagen</td>
<td>Stand:</td>
<td>Seite:</td>
</tr>
<tr>
<td>Abschnitt:</td>
<td>Übersicht Nachrichtenaufbau</td>
<td>06.10.2017</td>
<td>173</td>
</tr>
</table>


### I.2.3 Synchronisierung


<table>
<tr>
<th rowspan="4">Segment</th>
<th colspan="6">Nachricht</th>
</tr>
<tr>
<th colspan="2">Dialoginitialisierung</th>
<th colspan="2">Auftragsnachricht</th>
<th colspan="2">Dialogbeendigung</th>
</tr>
<tr>
<th>Kunde</th>
<th>Institut</th>
<th>Kunde</th>
<th>Institut</th>
<th>Kunde</th>
<th>Institut</th>
</tr>
<tr>
<th>N18</th>
<th>N19</th>
<th></th>
<th></th>
<th>N8</th>
<th>N14</th>
</tr>
<tr>
<td>Nachricht</td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td>HNHBK</td>
<td>1</td>
<td>1</td>
<td>-</td>
<td>-</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td>HNVSK</td>
<td>1</td>
<td>1</td>
<td>-</td>
<td>-</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td>HNVSD</td>
<td>1</td>
<td>1</td>
<td>-</td>
<td>-</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td>HNSHK</td>
<td>1</td>
<td>0-1</td>
<td>-</td>
<td>-</td>
<td>1</td>
<td>0-1</td>
</tr>
<tr>
<td>HIRMG</td>
<td>-</td>
<td>1</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>1</td>
</tr>
<tr>
<td>HIRMS</td>
<td>-</td>
<td>0-m</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>0-m</td>
</tr>
<tr>
<td>HKIDN</td>
<td>1</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HKVVB</td>
<td>1</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HKTAN</td>
<td>0/15</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HITAN</td>
<td>-</td>
<td>0/1</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HKISA</td>
<td>0/1-3</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HKSYN</td>
<td>1</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HIBPA</td>
<td>-</td>
<td>0-1</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HIKOM</td>
<td>-</td>
<td>0-1</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HISHV</td>
<td>-</td>
<td>0-1</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HIKPV</td>
<td>-</td>
<td>0-1</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HICSES</td>
<td>-</td>
<td>0-n</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>...</td>
<td>-</td>
<td>0-n</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HIUPA</td>
<td>-</td>
<td>0-1</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HIUPD</td>
<td>-</td>
<td>0-n</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HIISA</td>
<td>-</td>
<td>0/0-3</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HISYN</td>
<td>-</td>
<td>1</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HIKIM</td>
<td>-</td>
<td>0-n</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HKSAL</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HISAL</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>...</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HKPRO</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HIPRO</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HKSAK</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HKSSP</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HISSP</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HKKOM</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HIKOM</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HKEND</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>1</td>
<td>-</td>
</tr>
<tr>
<td>HNSHA</td>
<td>1</td>
<td>0-1</td>
<td>-</td>
<td>-</td>
<td>1</td>
<td>0-1</td>
</tr>
<tr>
<td>HNHBS</td>
<td>1</td>
<td>1</td>
<td>-</td>
<td>-</td>
<td>1</td>
<td>1</td>
</tr>
</table>

5
5 Abhängig davon, ob für die Synchronisation eine starke Kundenauthentifizierung erforderlich ist, sind
die Segmente HKTAN und HITAN in der Nachricht enthalten.


<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: H</td>
<td>Version: 3.0-FV</td>
<td>Financial Transaction Services (FinTS) Dokument: Formals</td>
</tr>
<tr>
<td>Seite: 174</td>
<td>Stand: 06.10.2017</td>
<td>Kapitel: Anlagen Abschnitt: Übersicht Nachrichtenaufbau</td>
</tr>
</table>


### I.2.4 Kommunikationszugang


<table>
<tr>
<th rowspan="4">Segment</th>
<th colspan="6">Nachricht</th>
</tr>
<tr>
<th colspan="2">Dialoginitialisierung</th>
<th colspan="2">Auftragsnachricht</th>
<th colspan="2">Dialogbeendigung</th>
</tr>
<tr>
<th>Kunde</th>
<th>Kredit- institut</th>
<th>Kunde</th>
<th>Kredit- institut</th>
<th>Kunde</th>
<th>Kredit- institut</th>
</tr>
<tr>
<th>N7</th>
<th>N3</th>
<th>N13</th>
<th>N4</th>
<th>N9</th>
<th>N14</th>
</tr>
<tr>
<td>Nachricht</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td>HNHBK</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td>HNSHK</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HIRMG</td>
<td>-</td>
<td>1</td>
<td>-</td>
<td>1</td>
<td>-</td>
<td>1</td>
</tr>
<tr>
<td>HIRMS</td>
<td>-</td>
<td>0-m</td>
<td>-</td>
<td>0-m</td>
<td>-</td>
<td>0-m</td>
</tr>
<tr>
<td>HKIDN</td>
<td>1</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HKVVB</td>
<td>1</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HKISA</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HKSYN</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HIBPA</td>
<td>-</td>
<td>0-1</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HIKOM</td>
<td>-</td>
<td>0-1</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HISHV</td>
<td>-</td>
<td>0-1</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HIKPV</td>
<td>-</td>
<td>0-1</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HICSES</td>
<td>-</td>
<td>0-n</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>...</td>
<td>-</td>
<td>0-n</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HIUPA</td>
<td>-</td>
<td>0-1</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HIUPD</td>
<td>-</td>
<td>0-n</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HIISA</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HISYN</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HIKIM</td>
<td>-</td>
<td>0-n</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HKSAL</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HISAL</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>...</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HKPRO</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HIPRO</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HKSAK</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HKSSP</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HISSP</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HKKOM</td>
<td>-</td>
<td>-</td>
<td>1</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HIKOM</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>0-n</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HKEND</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>1</td>
<td>-</td>
</tr>
<tr>
<td>HNSHA</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HNHBS</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
</tr>
</table>


<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th rowspan="2">Version: 3.0-FV</th>
<th rowspan="2">Kapitel: H</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Formals</td>
</tr>
<tr>
<td>Kapitel:</td>
<td>Anlagen</td>
<td>Stand:</td>
<td>Seite:</td>
</tr>
<tr>
<td>Abschnitt:</td>
<td>Übersicht Nachrichtenaufbau</td>
<td>06.10.2017</td>
<td>175</td>
</tr>
</table>


### I.2.5 Änderung eines öffentlichen Schlüssels des Kunden (HBCI RAH und RDH)


<table>
<tr>
<th rowspan="4">Segment</th>
<th colspan="6">Nachricht</th>
</tr>
<tr>
<th colspan="2">Dialoginitialisierung</th>
<th colspan="2">Auftragsnachricht</th>
<th colspan="2">Dialogbeendigung</th>
</tr>
<tr>
<th>Kunde</th>
<th>Kredit- institut</th>
<th>Kunde</th>
<th>Kredit- institut</th>
<th>Kunde</th>
<th>Kredit- institut</th>
</tr>
<tr>
<th>N6</th>
<th>N2</th>
<th>N1</th>
<th>N14</th>
<th>N8</th>
<th>N14</th>
</tr>
<tr>
<td>Nachricht</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td>HNHBK</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td>HNVSK</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td>HNVSD</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td>HNSHK</td>
<td>1</td>
<td>0-1</td>
<td>1</td>
<td>0-1</td>
<td>1</td>
<td>0-1</td>
</tr>
<tr>
<td>HIRMG</td>
<td>-</td>
<td>1</td>
<td>-</td>
<td>1</td>
<td>-</td>
<td>1</td>
</tr>
<tr>
<td>HIRMS</td>
<td>-</td>
<td>0-m</td>
<td>-</td>
<td>0-m</td>
<td>-</td>
<td>0-m</td>
</tr>
<tr>
<td>HKIDN</td>
<td>1</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HKVVB</td>
<td>1</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HKISA</td>
<td>0/1-3</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HKSYN</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HIBPA</td>
<td>-</td>
<td>0-1</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HIKOM</td>
<td>-</td>
<td>0-1</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HISHV</td>
<td>-</td>
<td>0-1</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HIKPV</td>
<td>-</td>
<td>0-1</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HICSES</td>
<td>-</td>
<td>0-n</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>...</td>
<td>-</td>
<td>0-n</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HIUPA</td>
<td>-</td>
<td>0-1</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HIUPD</td>
<td>-</td>
<td>0-n</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HIISA</td>
<td>-</td>
<td>0/0-3</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HISYN</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HIKIM</td>
<td>-</td>
<td>0-n</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HKSAL</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HISAL</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>...</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HKPRO</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HIPRO</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HKSAK</td>
<td>-</td>
<td>-</td>
<td>1-3</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HKSSP</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HISSP</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HKKOM</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HIKOM</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HKEND</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>1</td>
<td>-</td>
</tr>
<tr>
<td>HNSHA</td>
<td>1</td>
<td>0-1</td>
<td>1</td>
<td>0-1</td>
<td>1</td>
<td>0-1</td>
</tr>
<tr>
<td>HNHBS</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
</tr>
</table>


<!-- PageBreak -->


<table>
<tr>
<th>Kapitel: H</th>
<th>Version: 3.0-FV</th>
<th>Financial Transaction Services (FinTS) Dokument: Formals</th>
</tr>
<tr>
<td>Seite: 176</td>
<td>Stand: 06.10.2017</td>
<td>Kapitel: Anlagen Abschnitt: Übersicht Nachrichtenaufbau</td>
</tr>
</table>


## I.2.6 Erstmalige Anforderung der öffentlichen Schlüssel des Kreditinstituts (HBCI RAH und RDH)


<table>
<tr>
<th rowspan="4">Segment</th>
<th colspan="6">Nachricht</th>
</tr>
<tr>
<th colspan="2">Dialoginitialisierung</th>
<th colspan="2">Auftragsnachricht</th>
<th colspan="2">Dialogbeendigung</th>
</tr>
<tr>
<th>Kunde</th>
<th>Kredit- institut</th>
<th>Kunde</th>
<th>Kredit- institut</th>
<th>Kunde</th>
<th>Kredit- institut</th>
</tr>
<tr>
<th>N10</th>
<th>N11</th>
<th></th>
<th></th>
<th>N9</th>
<th>N14</th>
</tr>
<tr>
<td>Nachricht</td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td>HNHBK</td>
<td>1</td>
<td>1</td>
<td>-</td>
<td>-</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td>HNSHK</td>
<td>-</td>
<td>0-1</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>0-1</td>
</tr>
<tr>
<td>HIRMG</td>
<td>-</td>
<td>1</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>1</td>
</tr>
<tr>
<td>HIRMS</td>
<td>-</td>
<td>0-m</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>0-m</td>
</tr>
<tr>
<td>HKIDN</td>
<td>1</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HKVVB</td>
<td>1</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HKISA</td>
<td>3</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HKSYN</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HIBPA</td>
<td>-</td>
<td>0-1</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HIKOM</td>
<td>-</td>
<td>0-1</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HISHV</td>
<td>-</td>
<td>0-1</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HIKPV</td>
<td>-</td>
<td>0-1</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HICSES</td>
<td>-</td>
<td>0-n</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>...</td>
<td>-</td>
<td>0-n</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HIUPA</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HIUPD</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HIISA</td>
<td>-</td>
<td>1-3</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HISYN</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HIKIM</td>
<td>-</td>
<td>0-n</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HKSAL</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HISAL</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>...</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HKPRO</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HIPRO</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HKSAK</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HKSSP</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HISSP</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HKKOM</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HIKOM</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HKEND</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>1</td>
<td>-</td>
</tr>
<tr>
<td>HNSHA</td>
<td>-</td>
<td>0-1</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>0-1</td>
</tr>
<tr>
<td>HNHBS</td>
<td>1</td>
<td>1</td>
<td>-</td>
<td>-</td>
<td>1</td>
<td>1</td>
</tr>
</table>


<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th rowspan="2">Version: 3.0-FV</th>
<th rowspan="2">Kapitel: H</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Formals</td>
</tr>
<tr>
<td>Kapitel:</td>
<td>Anlagen</td>
<td>Stand:</td>
<td>Seite:</td>
</tr>
<tr>
<td>Abschnitt:</td>
<td>Übersicht Nachrichtenaufbau</td>
<td>06.10.2017</td>
<td>177</td>
</tr>
</table>


## I.2.7 Erstmalige Übermittlung der öffentlichen Schlüssel des Kunden (HBCI RAH und RDH)


<table>
<tr>
<th rowspan="4">Segment</th>
<th colspan="6">Nachricht</th>
</tr>
<tr>
<th colspan="2">Dialoginitialisierung</th>
<th colspan="2">Auftragsnachricht</th>
<th colspan="2">Dialogbeendigung</th>
</tr>
<tr>
<th>Kunde</th>
<th>Kredit- institut</th>
<th>Kunde</th>
<th>Kredit- institut</th>
<th>Kunde</th>
<th>Kredit- institut</th>
</tr>
<tr>
<th>N12</th>
<th>N14</th>
<th></th>
<th></th>
<th>N8</th>
<th>N14</th>
</tr>
<tr>
<td>Nachricht</td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td>HNHBK</td>
<td>1</td>
<td>1</td>
<td>-</td>
<td>-</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td>HNVSK</td>
<td>1</td>
<td>1</td>
<td>-</td>
<td>-</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td>HNVSD</td>
<td>1</td>
<td>1</td>
<td>-</td>
<td>-</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td>HNSHK</td>
<td>1</td>
<td>0-1</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>0-1</td>
</tr>
<tr>
<td>HIRMG</td>
<td>-</td>
<td>1</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>1</td>
</tr>
<tr>
<td>HIRMS</td>
<td>-</td>
<td>0-m</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>0-m</td>
</tr>
<tr>
<td>HKIDN</td>
<td>1</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HKVVB</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HKISA</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HKSYN</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HIBPA</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HIKOM</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HISHV</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HIKPV</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HICSES</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>...</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HIUPA</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HIUPD</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HIISA</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HISYN</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HIKIM</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HKSAL</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HISAL</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>...</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HKPRO</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HIPRO</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HKSAK</td>
<td>2-3</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HKSSP</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HISSP</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HKKOM</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HIKOM</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HKEND</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>1</td>
<td>-</td>
</tr>
<tr>
<td>HNSHA</td>
<td>1</td>
<td>0-1</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>0-1</td>
</tr>
<tr>
<td>HNHBS</td>
<td>1</td>
<td>1</td>
<td>-</td>
<td>-</td>
<td>1</td>
<td>1</td>
</tr>
</table>


<!-- PageBreak -->


<table>
<tr>
<th>Kapitel: H</th>
<th>Version: 3.0-FV</th>
<th>Financial Transaction Services (FinTS) Dokument: Formals</th>
</tr>
<tr>
<td>Seite: 178</td>
<td>Stand: 06.10.2017</td>
<td>Kapitel: Anlagen Abschnitt: Übersicht Nachrichtenaufbau</td>
</tr>
</table>


## I.2.8 Schlüsselsperrung durch den Kunden (HBCI RAH und RDH)


<table>
<tr>
<th rowspan="4">Segment</th>
<th colspan="6">Nachricht</th>
</tr>
<tr>
<th colspan="2">Dialoginitialisierung</th>
<th colspan="2">Auftragsnachricht</th>
<th colspan="2">Dialogbeendigung</th>
</tr>
<tr>
<th>Kunde</th>
<th>Kredit- institut</th>
<th>Kunde</th>
<th>Kredit- institut</th>
<th>Kunde</th>
<th>Kredit- institut</th>
</tr>
<tr>
<th>N6, N7</th>
<th>N2, N3</th>
<th>N17</th>
<th>N5</th>
<th>N8, N9</th>
<th>N14</th>
</tr>
<tr>
<td>Nachricht</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td>HNHBK</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td>HNVSK</td>
<td>0-1</td>
<td>0-1</td>
<td>0-1</td>
<td>-</td>
<td>0-1</td>
<td>-</td>
</tr>
<tr>
<td>HNVSD</td>
<td>0-1</td>
<td>0-1</td>
<td>0-1</td>
<td>-</td>
<td>0-1</td>
<td>-</td>
</tr>
<tr>
<td>HNSHK</td>
<td>0-1</td>
<td>0-1</td>
<td>0-1</td>
<td>0-1</td>
<td>-</td>
<td>0-1</td>
</tr>
<tr>
<td>HIRMG</td>
<td>-</td>
<td>1</td>
<td>-</td>
<td>1</td>
<td>-</td>
<td>1</td>
</tr>
<tr>
<td>HIRMS</td>
<td>-</td>
<td>0-m</td>
<td>-</td>
<td>0-m</td>
<td>-</td>
<td>0-m</td>
</tr>
<tr>
<td>HKIDN</td>
<td>1</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HKVVB</td>
<td>1</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HKISA</td>
<td>1-3</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HKSYN</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HIBPA</td>
<td>-</td>
<td>0-1</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HIKOM</td>
<td>-</td>
<td>0-1</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HISHV</td>
<td>-</td>
<td>0-1</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HIKPV</td>
<td>-</td>
<td>0-1</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HICSES</td>
<td>-</td>
<td>0-n</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>...</td>
<td>-</td>
<td>0-n</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HIUPA</td>
<td>-</td>
<td>0-1</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HIUPD</td>
<td>-</td>
<td>0-n</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HIISA</td>
<td>-</td>
<td>0-3</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HISYN</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HIKIM</td>
<td>-</td>
<td>0-n</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HKSAL</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HISAL</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>...</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HKPRO</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HIPRO</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HKSAK</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HKSSP</td>
<td>-</td>
<td>-</td>
<td>1</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HISSP</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>1</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HKKOM</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HIKOM</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HKEND</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>1</td>
<td>-</td>
</tr>
<tr>
<td>HNSHA</td>
<td>0-1</td>
<td>0-1</td>
<td>0-1</td>
<td>0-1</td>
<td>-</td>
<td>0-1</td>
</tr>
<tr>
<td>HNHBS</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
</tr>
</table>


<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th rowspan="2">Version: 3.0-FV</th>
<th rowspan="2">Kapitel: H</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Formals</td>
</tr>
<tr>
<td>Kapitel:</td>
<td>Anlagen</td>
<td>Stand:</td>
<td>Seite:</td>
</tr>
<tr>
<td>Abschnitt:</td>
<td>Übersicht Nachrichtenaufbau</td>
<td>06.10.2017</td>
<td>179</td>
</tr>
</table>


## I.2.9 Schlüsselsperrung durch den Kunden (HBCI DDV)


<table>
<tr>
<th rowspan="4">Segment</th>
<th colspan="6">Nachricht</th>
</tr>
<tr>
<th colspan="2">Dialoginitialisierung</th>
<th colspan="2">Auftragsnachricht</th>
<th colspan="2">Dialogbeendigung</th>
</tr>
<tr>
<th>Kunde</th>
<th>Kredit- institut</th>
<th>Kunde</th>
<th>Kredit- institut</th>
<th>Kunde</th>
<th>Kredit- institut</th>
</tr>
<tr>
<th>N6, N7</th>
<th>N2, N3</th>
<th>N17</th>
<th>N5</th>
<th>N8, N9</th>
<th>N14</th>
</tr>
<tr>
<td>Nachricht</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td>HNHBK</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td>HNVSK</td>
<td>0-1</td>
<td>0-1</td>
<td>0-1</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HNVSD</td>
<td>0-1</td>
<td>0-1</td>
<td>0-1</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HNSHK</td>
<td>0-1</td>
<td>0-1</td>
<td>0-1</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HIRMG</td>
<td>-</td>
<td>1</td>
<td>-</td>
<td>1</td>
<td>-</td>
<td>1</td>
</tr>
<tr>
<td>HIRMS</td>
<td>-</td>
<td>0-m</td>
<td>-</td>
<td>0-m</td>
<td>-</td>
<td>0-m</td>
</tr>
<tr>
<td>HKIDN</td>
<td>1</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HKVVB</td>
<td>1</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HKISA</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HKSYN</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HIBPA</td>
<td>-</td>
<td>0-1</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HIKOM</td>
<td>-</td>
<td>0-1</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HISHV</td>
<td>-</td>
<td>0-1</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HIKPV</td>
<td>-</td>
<td>0-1</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HICSES</td>
<td>-</td>
<td>0-n</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>...</td>
<td>-</td>
<td>0-n</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HIUPA</td>
<td>-</td>
<td>0-1</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HIUPD</td>
<td>-</td>
<td>0-n</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HIISA</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HISYN</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HIKIM</td>
<td>-</td>
<td>0-n</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HKSAL</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HISAL</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>...</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HKPRO</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HIPRO</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HKSAK</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HKSSP</td>
<td>-</td>
<td>-</td>
<td>1</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HISSP</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>1</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HKKOM</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HIKOM</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HKEND</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>1</td>
<td>-</td>
</tr>
<tr>
<td>HNSHA</td>
<td>0-1</td>
<td>0-1</td>
<td>0-1</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HNHBS</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
</tr>
</table>


<!-- PageBreak -->


<table>
<tr>
<th>Kapitel: Η</th>
<th>Version: 3.0-FV</th>
<th>Financial Transaction Services (FinTS) Dokument: Formals</th>
</tr>
<tr>
<td>Seite:<br>180</td>
<td>Stand: 06.10.2017</td>
<td>Kapitel: Anlagen Abschnitt: FinTS-Basiszeichensätze</td>
</tr>
</table>


## 1.3 FinTS-Basiszeichensätze

Die FinTS-Basiszeichensätze sind Subsets des ISO 8859. Erlaubt sind nur druckba-
re Zeichen des ISO 8859-Zeichensatzes, d. h. die Bereiche X'20' bis X'7E' und
X'A1' bis X'FF' sowie zusätzlich die Zeichen X'0A' (line feed) und X'OD' (carriage re-
turn):


## 1.3.1 ISO 8859-1 Subset Deutsch


<table>
<tr>
<th></th>
<th>0</th>
<th>1</th>
<th>2</th>
<th>3</th>
<th>4</th>
<th>5</th>
<th>6</th>
<th>7</th>
<th>8</th>
<th>9</th>
<th>A</th>
<th>B</th>
<th>C</th>
<th>D</th>
<th>E</th>
<th>F</th>
</tr>
<tr>
<td>0</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>LF</td>
<td></td>
<td></td>
<td>CR</td>
<td></td>
<td></td>
</tr>
<tr>
<td>1</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>2</td>
<td>SP</td>
<td>!</td>
<td>"</td>
<td>#</td>
<td>$</td>
<td>%</td>
<td>&amp;</td>
<td>1</td>
<td>(</td>
<td>)</td>
<td>*</td>
<td>+</td>
<td>,</td>
<td>-</td>
<td>.</td>
<td>/</td>
</tr>
<tr>
<td>3</td>
<td>0</td>
<td>1</td>
<td>2</td>
<td>3</td>
<td>4</td>
<td>5</td>
<td>6</td>
<td>7</td>
<td>8</td>
<td>9</td>
<td>:</td>
<td>;</td>
<td>&lt;</td>
<td>=</td>
<td>&gt;</td>
<td>?</td>
</tr>
<tr>
<td>4</td>
<td>@</td>
<td>A</td>
<td>B</td>
<td>C</td>
<td>D</td>
<td>E</td>
<td>F</td>
<td>G</td>
<td>H</td>
<td>I</td>
<td>J</td>
<td>K</td>
<td>L</td>
<td>M</td>
<td>NO</td>
<td></td>
</tr>
<tr>
<td>5</td>
<td>P</td>
<td>Q</td>
<td>R</td>
<td>S</td>
<td>T</td>
<td>U</td>
<td>V</td>
<td>W</td>
<td>X</td>
<td>Y</td>
<td>Z</td>
<td>[</td>
<td>1</td>
<td>]</td>
<td>1</td>
<td>-</td>
</tr>
<tr>
<td>6</td>
<td>1</td>
<td>a</td>
<td>b</td>
<td>C</td>
<td>d</td>
<td>e</td>
<td>f</td>
<td>g</td>
<td>h</td>
<td>i</td>
<td>j</td>
<td>k</td>
<td>I</td>
<td>m</td>
<td>n</td>
<td>O</td>
</tr>
<tr>
<td>7</td>
<td>p</td>
<td>b</td>
<td>r</td>
<td>S</td>
<td>t</td>
<td>u</td>
<td>V</td>
<td>W</td>
<td>X</td>
<td>y</td>
<td>Z</td>
<td>{</td>
<td>|</td>
<td>}</td>
<td>~</td>
<td></td>
</tr>
<tr>
<td>8</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>9</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>A</td>
<td></td>
<td>i</td>
<td>¢</td>
<td>£</td>
<td></td>
<td>¥</td>
<td></td>
<td>§</td>
<td></td>
<td>©</td>
<td>a</td>
<td>«</td>
<td></td>
<td>-</td>
<td>®</td>
<td>-</td>
</tr>
<tr>
<td>B</td>
<td>0</td>
<td>±</td>
<td>2</td>
<td>3</td>
<td>,</td>
<td>μ</td>
<td></td>
<td>.</td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>»</td>
<td>1/4</td>
<td>1/2</td>
<td>3/4</td>
<td>?</td>
</tr>
<tr>
<td>C</td>
<td>À</td>
<td>Á</td>
<td>Â</td>
<td>Ã</td>
<td>Ä</td>
<td>Å</td>
<td>Æ</td>
<td>Ç</td>
<td>È</td>
<td>É</td>
<td>Ê</td>
<td>Ё</td>
<td>Ì</td>
<td>Í</td>
<td>Î</td>
<td>Ï</td>
</tr>
<tr>
<td>D</td>
<td>Đ</td>
<td>Ñ</td>
<td>Ò</td>
<td>Ó</td>
<td>Ô</td>
<td>Õ</td>
<td>Ö</td>
<td>×</td>
<td>Ø</td>
<td>Ù</td>
<td>Ú</td>
<td>Û</td>
<td>Ü</td>
<td>Ý</td>
<td>Þ</td>
<td>B</td>
</tr>
<tr>
<td>E</td>
<td>à</td>
<td>á</td>
<td>â</td>
<td>ã</td>
<td>ä</td>
<td>å</td>
<td>æ</td>
<td>Ç</td>
<td>è</td>
<td>é</td>
<td>ê</td>
<td>ë</td>
<td>ì</td>
<td>í</td>
<td>Î</td>
<td>Ï</td>
</tr>
<tr>
<td>F</td>
<td>ð</td>
<td>ñ</td>
<td>Ò</td>
<td>ó</td>
<td>Ô</td>
<td>Õ</td>
<td>Ö</td>
<td></td>
<td>Ø</td>
<td>ù</td>
<td>ú</td>
<td>û</td>
<td>Ü</td>
<td>ý</td>
<td>þ</td>
<td>Ӱ</td>
</tr>
</table>


## 1.3.2 ISO 8859-1 Subset Englisch


<table>
<tr>
<th></th>
<th>0</th>
<th>1</th>
<th>2</th>
<th>3</th>
<th>4</th>
<th>5</th>
<th>6</th>
<th>7</th>
<th>8</th>
<th>9</th>
<th>A</th>
<th>B</th>
<th>C</th>
<th>D</th>
<th>E</th>
<th>F</th>
</tr>
<tr>
<td>0</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>LF</td>
<td></td>
<td></td>
<td>CR</td>
<td></td>
<td></td>
</tr>
<tr>
<td>1</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>2</td>
<td>SP</td>
<td>!</td>
<td>"</td>
<td>#</td>
<td>$</td>
<td>%</td>
<td>&amp;</td>
<td>1</td>
<td>(</td>
<td>)</td>
<td>*</td>
<td>+</td>
<td>,</td>
<td>-</td>
<td>.</td>
<td>/</td>
</tr>
<tr>
<td>3</td>
<td>0</td>
<td>1</td>
<td>2</td>
<td>3</td>
<td>4</td>
<td>5</td>
<td>6</td>
<td>7</td>
<td>8</td>
<td>9</td>
<td>:</td>
<td>;</td>
<td>&lt;</td>
<td>=</td>
<td>&gt;</td>
<td>?</td>
</tr>
<tr>
<td>4</td>
<td>@</td>
<td>A</td>
<td>B</td>
<td>C</td>
<td>D</td>
<td>E</td>
<td>F</td>
<td>G</td>
<td>H</td>
<td>I</td>
<td>J</td>
<td>K</td>
<td>L</td>
<td>M</td>
<td>N</td>
<td>O</td>
</tr>
<tr>
<td>5</td>
<td>P</td>
<td>Q</td>
<td>R</td>
<td>S</td>
<td>T</td>
<td>U</td>
<td>V</td>
<td>W</td>
<td>X</td>
<td>Y</td>
<td>Z</td>
<td>[</td>
<td>1</td>
<td>]</td>
<td>1</td>
<td>-</td>
</tr>
<tr>
<td>6</td>
<td>1</td>
<td>a</td>
<td>b</td>
<td>C</td>
<td>d</td>
<td>e</td>
<td>f</td>
<td>g</td>
<td>h</td>
<td>İ</td>
<td>j</td>
<td>k</td>
<td>I</td>
<td>m</td>
<td>n</td>
<td>0</td>
</tr>
<tr>
<td>7</td>
<td>p</td>
<td>q</td>
<td>r</td>
<td>S</td>
<td>t</td>
<td>u</td>
<td>V</td>
<td>W</td>
<td>X</td>
<td>y</td>
<td>Z</td>
<td>{</td>
<td>|</td>
<td>}</td>
<td>~</td>
<td></td>
</tr>
<tr>
<td>8</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>9</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>A</td>
<td></td>
<td>İ</td>
<td>¢</td>
<td>£</td>
<td>a</td>
<td>¥</td>
<td></td>
<td>§</td>
<td></td>
<td>C</td>
<td>a</td>
<td>«</td>
<td>7</td>
<td>-</td>
<td>®</td>
<td>-</td>
</tr>
<tr>
<td>B</td>
<td>0</td>
<td>±</td>
<td>2</td>
<td>3</td>
<td>.</td>
<td>μ</td>
<td></td>
<td>.</td>
<td>د</td>
<td>1</td>
<td>0</td>
<td>»</td>
<td>1/4</td>
<td>1/2</td>
<td>3/4</td>
<td>?</td>
</tr>
<tr>
<td>C</td>
<td>À</td>
<td>Á</td>
<td>Â</td>
<td>Ã</td>
<td>Ä</td>
<td>Å</td>
<td>Æ</td>
<td>Ç</td>
<td>È</td>
<td>É</td>
<td>Ê</td>
<td>Ë</td>
<td>Ì</td>
<td>Í</td>
<td>Î</td>
<td>Ï</td>
</tr>
<tr>
<td>D</td>
<td>Đ</td>
<td>Ñ</td>
<td>Ò</td>
<td>Ó</td>
<td>Ô</td>
<td>Õ</td>
<td>Ö</td>
<td>×</td>
<td>Ø</td>
<td>Ù</td>
<td>Ú</td>
<td>Û</td>
<td>Ü</td>
<td>Ý</td>
<td>Þ</td>
<td>ß</td>
</tr>
<tr>
<td>E</td>
<td>à</td>
<td>á</td>
<td>â</td>
<td>ã</td>
<td>ä</td>
<td>å</td>
<td>æ</td>
<td>Ç</td>
<td>è</td>
<td>é</td>
<td>ê</td>
<td>ë</td>
<td>ì</td>
<td>í</td>
<td>Î</td>
<td>Ï</td>
</tr>
<tr>
<td>F</td>
<td>ð</td>
<td>ñ</td>
<td>Ò</td>
<td>Ó</td>
<td>Ô</td>
<td>Õ</td>
<td>Ö</td>
<td></td>
<td>Ø</td>
<td>ù</td>
<td>ú</td>
<td>û</td>
<td>ü</td>
<td>ý</td>
<td>þ</td>
<td>ӱ</td>
</tr>
</table>


<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th rowspan="2">Version: 3.0-FV</th>
<th rowspan="2">Kapitel: Η</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Formals</td>
</tr>
<tr>
<td>Kapitel:</td>
<td>Anlagen</td>
<td>Stand:</td>
<td>Seite:</td>
</tr>
<tr>
<td>Abschnitt:</td>
<td>FinTS-Basiszeichensätze</td>
<td>06.10.2017</td>
<td>181</td>
</tr>
</table>


## 1.3.3 ISO 8859-1 Subset Französisch


<table>
<tr>
<th></th>
<th>0</th>
<th>1</th>
<th>2</th>
<th>3</th>
<th>4</th>
<th>5</th>
<th>6</th>
<th>7</th>
<th>8</th>
<th>9</th>
<th>A</th>
<th>B</th>
<th>C</th>
<th>D</th>
<th>E</th>
<th>F</th>
</tr>
<tr>
<td>0</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>LF</td>
<td></td>
<td></td>
<td>CR</td>
<td></td>
<td></td>
</tr>
<tr>
<td>1</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>2</td>
<td>SP</td>
<td>!</td>
<td>"</td>
<td>#</td>
<td>$</td>
<td>%</td>
<td>&amp;</td>
<td>1</td>
<td>(</td>
<td>)</td>
<td>*</td>
<td>+</td>
<td>,</td>
<td>-</td>
<td>.</td>
<td>/</td>
</tr>
<tr>
<td>3</td>
<td>0</td>
<td>1</td>
<td>2</td>
<td>3</td>
<td>4</td>
<td>5</td>
<td>6</td>
<td>7</td>
<td>8</td>
<td>9</td>
<td>:</td>
<td>;</td>
<td>&lt;</td>
<td>=</td>
<td>&gt;</td>
<td>?</td>
</tr>
<tr>
<td>4</td>
<td>@</td>
<td>A</td>
<td>B</td>
<td>C</td>
<td>D</td>
<td>E</td>
<td>F</td>
<td>G</td>
<td>H</td>
<td>I</td>
<td>J</td>
<td>K</td>
<td>L</td>
<td>M</td>
<td>N</td>
<td>O</td>
</tr>
<tr>
<td>5</td>
<td>P</td>
<td>Q</td>
<td>R</td>
<td>S</td>
<td>T</td>
<td>U</td>
<td>V</td>
<td>W</td>
<td>X</td>
<td>Y</td>
<td>Z</td>
<td>[</td>
<td>1</td>
<td>]</td>
<td>1</td>
<td>-</td>
</tr>
<tr>
<td>6</td>
<td>1</td>
<td>a</td>
<td>b</td>
<td>C</td>
<td>d</td>
<td>e</td>
<td>f</td>
<td>g</td>
<td>h</td>
<td>i</td>
<td>j</td>
<td>k</td>
<td>I</td>
<td>m</td>
<td>n</td>
<td>0</td>
</tr>
<tr>
<td>7</td>
<td>p</td>
<td>q</td>
<td>r</td>
<td>S</td>
<td>t</td>
<td>u</td>
<td>V</td>
<td>W</td>
<td>X</td>
<td>y</td>
<td>Z</td>
<td>{</td>
<td>|</td>
<td>}</td>
<td>~</td>
<td></td>
</tr>
<tr>
<td>8</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>9</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>A</td>
<td></td>
<td>i</td>
<td>¢</td>
<td>£</td>
<td>□</td>
<td>¥</td>
<td></td>
<td>§</td>
<td></td>
<td>©</td>
<td>a</td>
<td>«</td>
<td></td>
<td>-</td>
<td>®</td>
<td>-</td>
</tr>
<tr>
<td>B</td>
<td>0</td>
<td>±</td>
<td>2</td>
<td>3</td>
<td>,</td>
<td>μ</td>
<td></td>
<td>.</td>
<td>د</td>
<td>1</td>
<td>0</td>
<td>»</td>
<td>1/4</td>
<td>1/2</td>
<td>3/4</td>
<td>?</td>
</tr>
<tr>
<td>C</td>
<td>À</td>
<td>Á</td>
<td>Â</td>
<td>Ã</td>
<td>Ä</td>
<td>Å</td>
<td>Æ</td>
<td>Ç</td>
<td>È</td>
<td>É</td>
<td>Ê</td>
<td>Ё</td>
<td>ì</td>
<td>Í</td>
<td>Î</td>
<td>Ï</td>
</tr>
<tr>
<td>D</td>
<td>Đ</td>
<td>Ñ</td>
<td>Ò</td>
<td>Ó</td>
<td>Ô</td>
<td>Õ</td>
<td>Ö</td>
<td>×</td>
<td>Ø</td>
<td>Ù</td>
<td>Ú</td>
<td>Û</td>
<td>Ü</td>
<td>Ý</td>
<td>Þ</td>
<td>ß</td>
</tr>
<tr>
<td>E</td>
<td>à</td>
<td>á</td>
<td>â</td>
<td>ã</td>
<td>ä</td>
<td>å</td>
<td>æ</td>
<td>Ç</td>
<td>è</td>
<td>é</td>
<td>ê</td>
<td>ë</td>
<td>ì</td>
<td>í</td>
<td>Î</td>
<td>Ï</td>
</tr>
<tr>
<td>F</td>
<td>ð</td>
<td>ñ</td>
<td>Ò</td>
<td>Ó</td>
<td>Ô</td>
<td>Õ</td>
<td>Ö</td>
<td></td>
<td>Ø</td>
<td>ù</td>
<td>ú</td>
<td>û</td>
<td>ü</td>
<td>ý</td>
<td>þ</td>
<td>ÿ</td>
</tr>
</table>


<!-- PageBreak -->

<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th>Version:</th>
<th rowspan="2">Kapitel: H</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Formals</td>
<td>3.0-FV</td>
</tr>
<tr>
<td>Kapitel:</td>
<td>Anlagen</td>
<td>Stand:</td>
<td>Seite:</td>
</tr>
<tr>
<td>Abschnitt:</td>
<td>Transportmedienspezifische Festlegungen</td>
<td>06.10.2017</td>
<td>183</td>
</tr>
</table>


### I.4 Transportmedienspezifische Festlegungen

Obwohl FinTS grundsätzlich unabhängig von darunter liegenden Kommunikations-
schichten ist, müssen doch bestimmte Festlegungen für die zu liefernden Netze ge-
troffen werden, um FinTS multibankfähig und einheitlich zu definieren.

Hierbei handelt es sich um folgende Aspekte:

· Einschränkung der Kombinationsmöglichkeit von Protokollen, die für die gesi-
cherte Übertragung von FinTS-Datenströmen zugelassen werden.

. Festlegung von verwendeten Parametern.

· Abbilden von FinTS-Dialogabläufen auf die darunter liegenden Strukturen.

Zurzeit wird nur TCPIP als Transportdienst unterstützt:

<!-- PageBreak -->


<table>
<tr>
<th>Kapitel: H</th>
<th>Version: 3.0-FV</th>
<th>Financial Transaction Services (FinTS) Dokument: Formals</th>
</tr>
<tr>
<td>Seite:<br>184</td>
<td>Stand: 06.10.2017</td>
<td>Kapitel: Anlagen Abschnitt: Transportmedienspezifische Festlegungen</td>
</tr>
</table>


## I.4.1 TCP/IP


<table>
<tr>
<td>Realisierung Bank:</td>
<td>alternativ verpflichtend (es muss entweder der T-Online- oder der TCP/IP-Zugang realisiert werden)</td>
</tr>
<tr>
<td>Realisierung Kunde:</td>
<td>verpflichtend (sofern keine hardwaretechnischen Restriktionen vorliegen)</td>
</tr>
</table>


Das ,Transport Control Protocol" (TCP) stellt eine Anwendungsschnittstelle zur Ver-
fügung, auf der Applikationen aufsetzen können, um FinTS-Nachrichten auf gesi-
chertem Weg zwischen Kunde und Kreditinstitut zu übertragen. Da TCP/IP selbst
keinen Dialogbezug zwischen den einzelnen FinTS-Nachrichten herstellen kann,
muss dies durch ein auf TCP/IP aufsetzendes Dialogprotokoll sichergestellt werden.

Es ist darauf zu achten, dass nur der in RFC793 beschriebene Mindestumfang an
Protokollkommandos zum Einsatz kommt, um eine möglichst hohe Kompatibilität zu
erreichen.

Als zu verwendende Port Nummer wurde die Adresse 3000 bei der ,,Internet Assig-
ned Numbers Authority" (IANA) registriert. Als Schnittstelle zwischen dem TCP/IP-
Protokoll als Kommunikationspfad und dem FinTS-Kreditinstitutssystem auf der An-
wendungsseite ist ausschließlich die Verwendung von Streamsockets1 bzw. einer zu
der Socketschnittstelle 100% kompatiblen Netzwerkschnittstelle zulässig. Diese
Forderung ist hinsichtlich der bereits zu Anfang des Kapitels geschilderten Rah-
menbedingungen bezüglich der Einheitlichkeit und Multibankfähigkeit von FinTS auf
der Seite der Kommunikationsschnittstelle des Kunden erforderlich.

Der TCP/IP-Zugang kann verwendet werden, um einen FinTS-Zugang zum Internet
oder einen direkten Kreditinstitutszugang zu ermöglichen.


### I.4.1.1 Internet (WWW)

Das Sicherheitsverfahren FinTS ist unabhängig von der verwendeten Komponente
aus der Liste der Internet-Anwendungen (z. B. World Wide Web, FTP, Telnet). Zu
berücksichtigen ist allerdings die Transparenz des verwendeten Internet-Service, d.
h. es muss evtl. eine Filterfunktion eingesetzt werden.

Aufgrund der beim Sicherheitsverfahren HBCI verwendeten Sicherheitsmechanis-
men wird auf die Verwendung von Internet-spezifischen Sicherheitsprotokollen (z. B.
Transport Layer Security - TLS) bewusst verzichtet.

Im Fall des Sicherheitsverfahrens PIN/TAN wird das Vorhandensein einer alter-
nativen Transportsicherungskomponente wie z. B. TLS vorausgesetzt. Bei TLS wird
in gängigen Marktprodukten aktuell die Version 3.0 mit Clientzertifikaten unterstützt.
Dabei ist zwingend eine Schlüssellänge von mindestens 128 bit zu verwenden.

SSL (Secure Socket Layer) wird von HBCI / FinTS nicht mehr unterstützt.

<!-- PageFooter: 1 Die Implementierung der Socketschnittstelle setzt auf dem TCP/IP-Protokollstack auf und bietet ei- ne weitestgehend plattformunabhängige Kommunikationsschnittstelle auf der Basis des TCP/IP- Protokolls. Sockets - als Medium für eine netzwerkübergreifende Prozesskommunikation - sind ur- sprünglich ein Medium der Interprozesskommunikationsschnittstellen des UNIX-Betriebssystems und haben sich als Herstellerstandard in diesem Umfeld etabliert. Entsprechende Portierungen der Socketschnittstelle liegen heute auf allen gängigen Betriebssystemplattformen (Windows 8.1/ 10, MacOSX usw.) vor. -->
<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th rowspan="2">Version: 3.0-FV</th>
<th rowspan="2">Kapitel: H</th>
</tr>
<tr>
<th>Dokument:</th>
<th>Formals</th>
</tr>
<tr>
<td>Kapitel: Abschnitt:</td>
<td>Anlagen Abruf von Kommunikationszugangsdaten</td>
<td>Stand: 06.10.2017</td>
<td>Seite: 185</td>
</tr>
</table>


## I.5 Abruf von Kommunikationszugangsdaten

Für den Aufbau einer Verbindung zu einem Kreditinstitut sind bestimmte netz- und
dienstspezifische Zugangsdaten erforderlich. Diese Daten müssen dem Kundensys-
tem bereits vorliegen, bevor es die Verbindung aufbauen kann. Mit Hilfe dieses Auf-
trags wird dem Kunden die Möglichkeit gegeben, sich einen Zugangsdatenbestand
anzulegen bzw. diesen zu aktualisieren.


<table>
<tr>
<td>Realisierung Bank:</td>
<td>optional</td>
</tr>
<tr>
<td>Realisierung Kunde:</td>
<td>optional</td>
</tr>
</table>


## a) Kundenauftrag


### . Beschreibung

Eine Dialoginitialisierung als anonymer Benutzer ist erforderlich. AnschlieBend an
die Dialoginitialisierung darf nur eine Nachricht mit dem Segment „Kommunika-
tionszugang anfordern" folgen. Nach Erhalt der Antwortnachricht wird der Dialog in
jedem Fall beendet. Die Anforderung der Kommunikationszugänge darf nicht wäh-
rend eines „regulären“ FinTS-Dialogs erfolgen. Der Auftrag wird in diesem Fall ab-
gelehnt.


### . Format


<table>
<tr>
<td>Name:</td>
<td>Kommunikationszugang</td>
</tr>
<tr>
<td>Typ:</td>
<td>Nachricht</td>
</tr>
<tr>
<td>Version:</td>
<td>4</td>
</tr>
<tr>
<td>Sender:</td>
<td>Kunde</td>
</tr>
</table>


<table>
<tr>
<th>Nr.</th>
<th>Name</th>
<th>Ver- sion</th>
<th>Typ</th>
<th>Kennung</th>
<th>Sta- tus</th>
<th>An- zahl</th>
<th>Anmerkungen</th>
</tr>
<tr>
<td>1</td>
<td>Nachrichtenkopf</td>
<td>3</td>
<td>SEG</td>
<td>HNHBK</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>2</td>
<td>Kommunikations- zugang anfordern</td>
<td>4</td>
<td>SEG</td>
<td>HKKOM</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>3</td>
<td>Nachrichtenab- schluss</td>
<td>1</td>
<td>SEG</td>
<td>HNHBS</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
</table>


## . Beschreibung

Es kann ein Bereich von Kreditinstitutskennungen eingestellt werden, um die ge-
wünschten Kommunikationszugänge einzugrenzen. Wird kein Bereich eingestellt, so
werden alle verfügbaren Kommunikationszugänge rückgemeldet. Wenn ein Bereich
angegeben wird, muss das Länderkennzeichen des Bereichsanfangs und -endes
identisch sein.


### . Format


<table>
<tr>
<td>Name:</td>
<td>Kommunikationszugang anfordern</td>
</tr>
<tr>
<td>Typ:</td>
<td>Segment</td>
</tr>
<tr>
<td>Segmentart:</td>
<td>Geschäftsvorfall</td>
</tr>
<tr>
<td>Kennung:</td>
<td>HKKOM</td>
</tr>
<tr>
<td>Bezugssegment:</td>
<td>-</td>
</tr>
<tr>
<td>Version:</td>
<td>4</td>
</tr>
<tr>
<td>Sender:</td>
<td>Kunde</td>
</tr>
</table>


<!-- PageBreak -->


<table>
<tr>
<th>Kapitel: H</th>
<th>Version: 3.0-FV</th>
<th>Financial Transaction Services (FinTS) Dokument: Formals</th>
</tr>
<tr>
<td>Seite: 186</td>
<td>Stand: 06.10.2017</td>
<td>Kapitel: Anlagen Abschnitt: Abruf von Kommunikationszugangsdaten</td>
</tr>
</table>


<table>
<tr>
<th>Nr.</th>
<th>Name</th>
<th>Ver- sion</th>
<th>Typ</th>
<th>For- mat</th>
<th>Län- ge</th>
<th>Sta- tus</th>
<th>An- zahl</th>
<th>Restriktionen</th>
</tr>
<tr>
<td>1</td>
<td>Segmentkopf</td>
<td>1</td>
<td>DEG</td>
<td></td>
<td></td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>2</td>
<td>Von Kreditinstituts- kennung</td>
<td>2</td>
<td>DEG</td>
<td>kik</td>
<td>#</td>
<td>O</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>3</td>
<td>Bis Kreditinstituts- kennung</td>
<td>1</td>
<td>DEG</td>
<td>kik</td>
<td>#</td>
<td>O</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>4</td>
<td>Maximale Anzahl Einträge</td>
<td>1</td>
<td>DE</td>
<td>num</td>
<td>..4</td>
<td>O</td>
<td>1</td>
<td>&gt;0</td>
</tr>
<tr>
<td>5</td>
<td>Aufsetzpunkt</td>
<td>1</td>
<td>DE</td>
<td>an</td>
<td>..35</td>
<td>C</td>
<td>1</td>
<td>M: vom Kreditinstitut wurde ein Aufsetzpunkt rückge- meldet (s. Kap. B.6.3). N: sonst</td>
</tr>
</table>


## b) Kreditinstitutsrückmeldung


### . Beschreibung

Für jedes der vom Kunden angeforderten Kreditinstitute wird ein Segment des For-
mats „Kommunikationszugang rückmelden“ in die Kreditinstitutsnachricht eingestellt.
Für jedes Institut können wiederum bis zu 9 Zugänge angegeben werden.

Die Einstellung von Zeiten, während derer das Kreditinstitut erreichbar ist, erfolgt
nicht, da diese häufigeren Änderungen unterworfen sein können. Grundsätzlich ist
eine 24-stündige Erreichbarkeit anzustreben.


![](figures/194.1)


Falls das Kreditinstitut für einen Kommunikationsdienst mehr als
einen Zugang anbietet und über den vom Kundensystem ange-
wählten Zugang keine Verbindung hergestellt werden kann, so
sollte das Kundensystem auch die anderen Zugänge auspro-
bieren.


### . Format


<table>
<tr>
<td>Name:</td>
<td>Antwort auf Kommunikationszugang</td>
</tr>
<tr>
<td>Typ:</td>
<td>Nachricht</td>
</tr>
<tr>
<td>Version:</td>
<td>4</td>
</tr>
</table>


Sender:

Kreditinstitut


<table>
<tr>
<th>Nr.</th>
<th>Name</th>
<th>Ver- sion</th>
<th>Typ</th>
<th>Kennung</th>
<th>Sta- tus</th>
<th>An- zahl</th>
<th>Anmerkungen</th>
</tr>
<tr>
<td>1</td>
<td>Nachrichtenkopf</td>
<td>3</td>
<td>SEG</td>
<td>HNHBK</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>2</td>
<td>Rückmeldungen zur Gesamtnachricht</td>
<td>2</td>
<td>SEG</td>
<td>HIRMG</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>3</td>
<td>Rückmeldungen zu Segmenten</td>
<td>2</td>
<td>SEG</td>
<td>HIRMS</td>
<td>O</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>4</td>
<td>Kommunikations- zugang rückmelden</td>
<td>4</td>
<td>SEG</td>
<td>HIKOM</td>
<td>O</td>
<td>n</td>
<td></td>
</tr>
<tr>
<td>5</td>
<td>Nachrichtenab- schluss</td>
<td>1</td>
<td>SEG</td>
<td>HNHBS</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
</table>


<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th rowspan="2">Version: 3.0-FV</th>
<th rowspan="2">Kapitel: H</th>
</tr>
<tr>
<th>Dokument:</th>
<th>Formals</th>
</tr>
<tr>
<td>Kapitel: Abschnitt:</td>
<td>Anlagen Abruf von Kommunikationszugangsdaten</td>
<td>Stand: 06.10.2017</td>
<td>Seite: 187</td>
</tr>
</table>


### . Format


<table>
<tr>
<td>Name:</td>
<td>Kommunikationszugang rückmelden</td>
</tr>
<tr>
<td>Typ:</td>
<td>Segment</td>
</tr>
<tr>
<td>Segmentart:</td>
<td>Geschäftsvorfall</td>
</tr>
<tr>
<td>Kennung:</td>
<td>HIKOM</td>
</tr>
<tr>
<td>Bezugssegment:</td>
<td>HKKOM</td>
</tr>
<tr>
<td>Version:</td>
<td>4</td>
</tr>
<tr>
<td>Sender:</td>
<td>Kreditinstitut</td>
</tr>
</table>


<table>
<tr>
<th>Nr.</th>
<th>Name</th>
<th>Ver- sion</th>
<th>Typ</th>
<th>For- mat</th>
<th>Län- ge</th>
<th>Sta- tus</th>
<th>An- zahl</th>
<th>Restriktionen</th>
</tr>
<tr>
<td>1</td>
<td>Segmentkopf</td>
<td>1</td>
<td>DEG</td>
<td></td>
<td></td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>2</td>
<td>Kreditinstitutsken- nung</td>
<td>1</td>
<td>DEG</td>
<td>kik</td>
<td>#</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>3</td>
<td>Standardsprache</td>
<td>2</td>
<td>DE</td>
<td>num</td>
<td>..3</td>
<td>M</td>
<td>1</td>
<td>1,2,3</td>
</tr>
<tr>
<td>4</td>
<td>Kommunikationspa- rameter</td>
<td>2</td>
<td>DEG</td>
<td></td>
<td></td>
<td>M</td>
<td>1..9</td>
<td></td>
</tr>
</table>


### ◆ Ausgewählte Beispiele für Rückmeldungscodes


<table>
<tr>
<td>Code</td>
<td>Beispiel für Rückmeldungstext</td>
</tr>
<tr>
<td>0020</td>
<td>Auftrag ausgeführt</td>
</tr>
<tr>
<td>3010</td>
<td>Es liegen keine Einträge vor</td>
</tr>
<tr>
<td>3040</td>
<td>Auftrag nur teilweise ausgeführt</td>
</tr>
<tr>
<td>9210</td>
<td>Bereichende darf nicht vor Bereichanfang liegen</td>
</tr>
</table>


### c) Bankparameterdaten


#### . Beschreibung

Geschäftsvorfallspezifische Parameter existieren nicht.


#### . Format


<table>
<tr>
<td>Name:</td>
<td>Kommunikationszugang Parameter</td>
</tr>
<tr>
<td>Typ:</td>
<td>Segment</td>
</tr>
<tr>
<td>Segmentart:</td>
<td>Geschäftsvorfall</td>
</tr>
<tr>
<td>Kennung:</td>
<td>HIKOMS</td>
</tr>
<tr>
<td>Bezugssegment:</td>
<td>HKVVB</td>
</tr>
<tr>
<td>Version:</td>
<td>4</td>
</tr>
<tr>
<td>Sender:</td>
<td>Kreditinstitut</td>
</tr>
</table>


<table>
<tr>
<th>Nr.</th>
<th>Name</th>
<th>Ver- sion</th>
<th>Typ</th>
<th>For- mat</th>
<th>Län- ge</th>
<th>Sta- tus</th>
<th>An- zahl</th>
<th>Restriktionen</th>
</tr>
<tr>
<td>1</td>
<td>Segmentkopf</td>
<td>1</td>
<td>DEG</td>
<td></td>
<td></td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>2</td>
<td>Maximale Anzahl Aufträge</td>
<td>1</td>
<td>DE</td>
<td>num</td>
<td>..3</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>3</td>
<td>Anzahl Signaturen mindestens</td>
<td>1</td>
<td>DE</td>
<td>num</td>
<td>1</td>
<td>M</td>
<td>1</td>
<td>0, 1, 2, 3</td>
</tr>
<tr>
<td>4</td>
<td>Sicherheitsklasse</td>
<td>1</td>
<td>DE</td>
<td>code</td>
<td>1</td>
<td>M</td>
<td>1</td>
<td>0, 1, 2, 3, 4</td>
</tr>
</table>


<!-- PageBreak -->


<table>
<tr>
<th>Kapitel: H</th>
<th>Version: 3.0-FV</th>
<th>Financial Transaction Services (FinTS) Dokument: Formals</th>
</tr>
<tr>
<td>Seite:<br>188</td>
<td>Stand: 06.10.2017</td>
<td>Kapitel: Anlagen<br>Abschnitt: Abruf von Kommunikationszugangsdaten</td>
</tr>
</table>


![](figures/196.1)


Das Anfordern der Kommunikationszugänge ist insbesondere für
den Erstzugang erforderlich. Weiterhin werden Zugangsdaten für
den anonymen Zugang (Gastzugang) benötigt. Kommunikations-
zugänge sind keinen ständigen Änderungen unterworfen und müs-
sen daher nur in großen Zeitabständen aktualisiert werden. Eine Ak-
tualisierung kann auch automatisch erfolgen, sofern ein Verbin-
dungsaufbau aufgrund veralteter Zugangsdaten fehlschlägt.

Die Zugangsdaten sollten für spätere Zugänge im Kundenprodukt
gespeichert werden. Aus Effizienzgründen kann diese Zugangsda-
tenbank im Kundenprodukt mit einer lokalen Bankleitzahlendatei
verknüpft werden.

Es ist zu berücksichtigen, dass die Kommunikationsadresse, unter
der die Zugangsdaten abgerufen werden, im Regelfall nicht iden-
tisch ist mit der Adresse des Kreditinstituts, zu dem der Zugang auf-
gebaut werden soll, so dass u.U. nach dem Aktualisieren der Zu-
gangsdaten die physikalische Verbindung erst beendet und dann
mit den neuen Zugangsdaten erneut aufgebaut werden muss.

Jeder Verband pflegt die Zugangsdaten seiner angeschlossenen In-
stitute und bietet sie an zentraler Stelle zum Abruf an. Die jeweilige
Abrufadresse kann bei den in der Einleitung dieses Dokumentes
genannten Ansprechpartnern erfragt werden.
