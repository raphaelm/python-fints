# ZENTRALER KREDITAUSSCHUSS Financial Transaction Services (FinTS)

\- Security -
Sicherheitsverfahren HBCI

Herausgeber:
Bundesverband deutscher Banken e.V., Berlin
Deutscher Sparkassen- und Giroverband e.V., Bonn/Berlin
Bundesverband der Deutschen Volksbanken und Raiffeisenbanken e.V., Berlin
Bundesverband Öffentlicher Banken Deutschlands e.V., Berlin

Version: 3.0

Stand: 18.07.2013
Final Version

<!-- PageBreak -->

Die vorliegende Schnittstellenspezifikation für eine automatisiert nutzbare multibankfähige
Homebanking-Schnittstelle (im Folgenden: Schnittstellenspezifikation) wurde im Auftrag des
Zentralen Kreditausschusses entwickelt. Sie wird hiermit zur Implementation in Kunden- und
Kreditinstitutssysteme freigegeben.

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
on oder Multibankfähigkeit von Kundenprodukten behindern, dem Zentralen Kreditausschuss
zu melden. Es wird weiterhin ausdrücklich darauf hingewiesen, dass Änderungen der
Schnittstellenspezifikation durch den Zentralen Kreditausschuss jederzeit und ohne vorheri-
ge Ankündigung möglich sind.

Eine Weitergabe der Schnittstellenspezifikation durch den Hersteller an Dritte darf nur unent-
geltlich, in unveränderter Form und zu den vorstehenden Bedingungen erfolgen.

Dieses Dokument kann im Internet abgerufen werden unter http://www.fints.org.

<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th rowspan="2">Version: 3.0 - Final Version</th>
<th rowspan="2">Kapitel:</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Security - Sicherheitsverfahren HBCI</td>
</tr>
<tr>
<td>Kapitel:</td>
<td>Versionsführung</td>
<td>Stand: 18.07.2013</td>
<td>Seite: 1</td>
</tr>
</table>


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
<td>15.11.2002</td>
<td>3.0</td>
<td>FinTS 3.0 Security - Si- cherheitsverfahren HBCI.doc</td>
<td>Frühere Versionen wur- den im Rahmen der HBCI-Spezifikation ver- öffentlicht</td>
</tr>
<tr>
<td>Haubner</td>
<td>für SIZ</td>
<td>21.06.2005</td>
<td>3.0</td>
<td>FinTS 3.0 Security - Si- cherheitsverfahren HBCI Rel. 2005-06-21.doc</td>
<td>Enthält alle bekannt ge- wordenen Fehler und Klarstellungen bis zum Releasedatum 21.06.2005.</td>
</tr>
<tr>
<td>Haubner</td>
<td>für GAD</td>
<td>07.05.2007</td>
<td>3.0</td>
<td>FinTS 3.0 Security - Si- cherheitsverfahren HBCI Rel. 2007-05-07 final ver- sion.doc</td>
<td>Enthält die Anpassun- gen im Zusammenhang mit der Einführung von SECCOS 6 Bankensig- naturkarten</td>
</tr>
<tr>
<td>Haubner</td>
<td>für GAD</td>
<td>15.05.2008</td>
<td>3.0</td>
<td>FinTS 3.0 Security - Si- cherheitsverfahren HBCI Rel. 2008-05-15 final ver- sion.doc</td>
<td>Korrekturen und Klar- stellungen zur SECCOS 6 Unterstüt- zung.</td>
</tr>
<tr>
<td>Haubner</td>
<td>für SIZ</td>
<td>14.10.2011</td>
<td>3.0</td>
<td>FinTS 3.0 Security - Si- cherheitsverfahren HBCI Rel. 2011-09-23 final ver- sion.doc</td>
<td>Ergänzen RAH- Verfahren</td>
</tr>
<tr>
<td>Haubner</td>
<td>für SIZ</td>
<td>25.09.2012</td>
<td>3.0</td>
<td>FinTS 3.0 Security - Si- cherheitsverfahren HBCI Rel. 2012-09-25 final ver- sion.doc</td>
<td>Einführen DK-Padding bei RAH-Verfahren</td>
</tr>
<tr>
<td>Haubner</td>
<td>Für SIZ</td>
<td>18.07.2013</td>
<td>3.0</td>
<td>FinTS 3.0 Security - Si- cherheitsverfahren HBCI Rel. 2013-07-18 FV.doc</td>
<td>Klarstellungen und Feh- lerkorrekturen, Verweise auf DK Kryptokatalog</td>
</tr>
</table>


<!-- PageBreak -->


<table>
<tr>
<th>Kapitel:</th>
<th>Version: 3.0 - Final Version</th>
<th>Financial Transaction Services (FinTS) Dokument: Security - Sicherheitsverfahren HBCI</th>
</tr>
<tr>
<td>Seite: 2</td>
<td>Stand: 18.07.2013</td>
<td>Kapitel: Änderungen gegenüber der Vorversion</td>
</tr>
</table>


## Änderungen gegenüber der Vorversion

Hinzufügungen und Änderungen sind im Dokument in dieser Farbe und zusätzlich
durch Unterstreichung und einen Randbalken markiert. Löschungen sind aufgrund
der besseren Übersichtlichkeit nur durch einen Randbalken markiert. Hypertextlinks
sind in dieser Farbe markiert. Falls sich die Kapitelnummerierung geändert hat, be-
zieht sich die Kapitelangabe auf die neue Nummerierung. Aufgrund der umfangrei-
chen Textumstellungen wurden nicht alle Änderungen markiert.


<table>
<tr>
<th>lfd.<br>Nr.</th>
<th>Kapitel</th>
<th>Seiten- nummer</th>
<th>Ken- nung</th>
<th>Art</th>
<th>Beschreibung</th>
</tr>
<tr>
<td>1</td>
<td>Diverse</td>
<td>Diverse</td>
<td>0408</td>
<td>E</td>
<td>Ergänzen des RAH-Verfahrens und der damit verbundenen Sicherheitsprofile RAH-7, RAH-9 und RAH-10</td>
</tr>
<tr>
<td>2</td>
<td>B.2.2.</td>
<td>S. 17ff</td>
<td>0408, 0425</td>
<td>Ä</td>
<td>Anpassen der Abbildungen im Zuge der Einführung des RAH-Verfahrens. Ergän- zen des DK-Paddings. Ersetzen des Terminus ,,HBCI- Nachricht“ durch ,,FinTS-Nachricht“</td>
</tr>
<tr>
<td>3</td>
<td>B.1.1, S. 3</td>
<td></td>
<td></td>
<td>Ä</td>
<td>Anpassen des Passus zu verpflichten- den Sicherheitsprofilen</td>
</tr>
<tr>
<td>4</td>
<td>B.2.2.1</td>
<td></td>
<td></td>
<td>Ä</td>
<td>ZKA-Padding, einfügen der AES- Blocklänge=16 Byte für den Wert „L“ Fehlerbehebungen und Klarstellungen in den Abbildungen 1, 2 und 3</td>
</tr>
<tr>
<td>5</td>
<td>B.3.1.3.1</td>
<td></td>
<td></td>
<td>Ä</td>
<td>Löschen von Step 5, da nicht mehr rele- vant.</td>
</tr>
<tr>
<td>6</td>
<td>Diverse</td>
<td></td>
<td></td>
<td>Ä</td>
<td>Ersetzen der konkret angegebenen Schlüssellängen durch Referenz auf die Empfehlungen des DK Kryptokatalogs [DK Krypto]</td>
</tr>
<tr>
<td>7</td>
<td>C.1.3.2.4.1</td>
<td>S. 99</td>
<td></td>
<td>Ä</td>
<td>Wegfall der Prüfung, ob Ausgangswert = Verschlüsselungsergebnis ist.</td>
</tr>
</table>


<!-- PageFooter: 1 nur zur internen Zuordnung -->
<!-- PageFooter: 2 F = Fehler; Ä = Änderung; K = Klarstellung; E = Erweiterung -->
<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th rowspan="2">Version: 3.0 - Final Version</th>
<th rowspan="2">Kapitel:</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Security - Sicherheitsverfahren HBCI</td>
</tr>
<tr>
<td>Kapitel:</td>
<td>Inhaltsverzeichnis</td>
<td>Stand: 18.07.2013</td>
<td>Seite: 1</td>
</tr>
</table>


## Inhaltsverzeichnis


<table>
<tr>
<td>Versionsführung</td>
<td>1</td>
</tr>
<tr>
<td>Änderungen gegenüber der Vorversion.</td>
<td>2</td>
</tr>
<tr>
<td>Inhaltsverzeichnis</td>
<td>1</td>
</tr>
<tr>
<td>Abbildungsverzeichnis</td>
<td>3</td>
</tr>
<tr>
<td>Abkürzungen</td>
<td>5</td>
</tr>
<tr>
<td>Literaturhinweise</td>
<td>7</td>
</tr>
<tr>
<td>A. Einleitung</td>
<td>1</td>
</tr>
<tr>
<td>B. Verfahrensbeschreibung</td>
<td>2</td>
</tr>
<tr>
<td>B.1 Allgemeines</td>
<td>2</td>
</tr>
<tr>
<td>B.1.1 Sicherheitsprofile</td>
<td>3</td>
</tr>
<tr>
<td>B.1.2 Sicherheitsklassen</td>
<td>15</td>
</tr>
<tr>
<td>B.2 Mechanismen</td>
<td>18</td>
</tr>
<tr>
<td>B.2.1 Elektronische Signatur</td>
<td>18</td>
</tr>
<tr>
<td>B.2.2 Verschlüsselung</td>
<td>21</td>
</tr>
<tr>
<td>B.2.3 Sicherheitsmedien beim Kundenprodukt</td>
<td>30</td>
</tr>
<tr>
<td>B.3 Abläufe</td>
<td>31</td>
</tr>
<tr>
<td>B.3.1 Schlüsselverwaltung</td>
<td>31</td>
</tr>
<tr>
<td>B.3.2 Schlüsselsperrung</td>
<td>45</td>
</tr>
<tr>
<td>B.4 Bankfachliche Anforderungen</td>
<td>47</td>
</tr>
<tr>
<td>B.5 Formate für Signatur und Verschlüsselung</td>
<td>48</td>
</tr>
<tr>
<td>B.5.1 Signaturkopf</td>
<td>49</td>
</tr>
<tr>
<td>B.5.2 Signaturabschluss</td>
<td>52</td>
</tr>
<tr>
<td>B.5.3 Verschlüsselungskopf</td>
<td>53</td>
</tr>
<tr>
<td>B.5.4 Verschlüsselte Daten</td>
<td>54</td>
</tr>
<tr>
<td>B.6 Key-Management</td>
<td>55</td>
</tr>
<tr>
<td>B.6.1 Formate für Key-Management</td>
<td>55</td>
</tr>
<tr>
<td>B.6.2 Key-Management-Nachrichten</td>
<td>63</td>
</tr>
</table>


<!-- PageBreak -->


<table>
<tr>
<th>Kapitel:</th>
<th>Version: 3.0 - Final Version</th>
<th>Financial Transaction Services (FinTS) Dokument: Security - Sicherheitsverfahren HBCI</th>
</tr>
<tr>
<td>Seite:<br>2</td>
<td>Stand: 18.07.2013</td>
<td>Kapitel: Inhaltsverzeichnis</td>
</tr>
</table>


<table>
<tr>
<td>B.7 RDH-x / RAH-y (aktuelles Verfahren)<br>B.8 RDH-y / RAH-y (neues Verfahren)</td>
<td>66<br>66</td>
</tr>
<tr>
<td>C. Chipapplikationen</td>
<td>77</td>
</tr>
<tr>
<td>C.1 Chipapplikation für RAH / RDH</td>
<td>77</td>
</tr>
<tr>
<td>C.1.1 Applikation Notepad</td>
<td>77</td>
</tr>
<tr>
<td>C.1.2 EF_NOTEPAD</td>
<td>77</td>
</tr>
<tr>
<td>C.1.3 Terminalabläufe</td>
<td>91</td>
</tr>
<tr>
<td>C.2 Chipapplikation für DDV</td>
<td>105</td>
</tr>
<tr>
<td>C.2.1 Daten der Applikation HBCI-Banking für Typ 1</td>
<td>106</td>
</tr>
<tr>
<td>C.2.2 Daten der Applikation HBCI-Banking für SECCOS 6</td>
<td>124</td>
</tr>
<tr>
<td>C.2.3 Platzbedarf der Applikation im Chip</td>
<td>142</td>
</tr>
<tr>
<td>C.2.4 Terminalabläufe (Typ 1 und SECCOS 6)</td>
<td>143</td>
</tr>
<tr>
<td>C.2.5 Makros</td>
<td>154</td>
</tr>
<tr>
<td>C.2.6 Übersicht der Chip-Applikations-Parameter</td>
<td>158</td>
</tr>
<tr>
<td>D. Data Dictionary</td>
<td>159</td>
</tr>
<tr>
<td>E. Anlagen</td>
<td>183</td>
</tr>
<tr>
<td>E.1 Übersicht der Segmente</td>
<td>183</td>
</tr>
</table>


<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th rowspan="2">Version: 3.0 - Final Version</th>
<th rowspan="2">Kapitel:</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Security - Sicherheitsverfahren HBCI</td>
</tr>
<tr>
<td>Kapitel:</td>
<td>Abbildungsverzeichnis</td>
<td>Stand: 18.07.2013</td>
<td>Seite: 3</td>
</tr>
</table>


## Abbildungsverzeichnis


<table>
<tr>
<td>Abbildung 1: Nachrichtenverschlüsselung mit AES im CBC-Mode für RAH- Verfahren</td>
<td>22</td>
</tr>
<tr>
<td>Abbildung 2: Verschlüsselung bei RAH-7 und RAH-9</td>
<td>23</td>
</tr>
<tr>
<td>Abbildung 3: Verschlüsselung bei RAH-10</td>
<td>23</td>
</tr>
<tr>
<td>Abbildung 4: Nachrichtenverschlüsselung generell mit 2-Key-Triple-DES im CBC-Mode für RDH und DDV</td>
<td>25</td>
</tr>
<tr>
<td>Abbildung 5: Verschlüsselung bei 2-Key-Triple-DES im DDV-Verfahren</td>
<td>26</td>
</tr>
<tr>
<td>Abbildung 6: Entschlüsselung bei 2-Key-Triple-DES im DDV-Verfahren</td>
<td>26</td>
</tr>
<tr>
<td>Abbildung 7: Verschlüsselung bei 2-Key-Triple-DES im RDH-Verfahren</td>
<td>27</td>
</tr>
<tr>
<td>Abbildung 8: Entschlüsselung bei 2-Key-Triple-DES im RDH-Verfahren</td>
<td>28</td>
</tr>
<tr>
<td>Abbildung 9: Verschlüsselung bei RDH-1</td>
<td>28</td>
</tr>
<tr>
<td>Abbildung 10: Verschlüsselung bei RDH-3 und RDH-5</td>
<td>29</td>
</tr>
<tr>
<td>Abbildung 11: Verschlüsselung bei RDH-6 bis RDH-9</td>
<td>29</td>
</tr>
<tr>
<td>Abbildung 12: Verschlüsselung bei RDH-10</td>
<td>30</td>
</tr>
<tr>
<td>Abbildung 13: Ablauf der Erstinitialisierung bei RDH</td>
<td>41</td>
</tr>
<tr>
<td>Abbildung 14: Beispiel für die Gestaltung des Ini-Briefs bei RDH-2 oder RDH-5</td>
<td>42</td>
</tr>
<tr>
<td>Abbildung 15: Beispiel für die Gestaltung des Ini-Briefs bei RAH-9, RAH-10, RDH-8, RDH-9 oder RDH-10</td>
<td>43</td>
</tr>
<tr>
<td>Abbildung 16: Unterstützte Sicherheitsprofilwechsel RDH-1, RDH-2 und RDH-5 ...</td>
<td>64</td>
</tr>
<tr>
<td>Abbildung 17: Unterstützte Sicherheitsprofilwechsel RDH-1, RDH-2 RDH-5, RDH-9 und RDH-10</td>
<td>65</td>
</tr>
<tr>
<td>Abbildung 18: Unterstützte Sicherheitsprofilwechsel beim Übergang von RDH- auf RAH-Verfahren</td>
<td>67</td>
</tr>
<tr>
<td>Abbildung 19: Datenelemente der Applikation "HBCI", Bankensignaturkarte mit Zertifikat</td>
<td>106</td>
</tr>
<tr>
<td>Abbildung 20: Datenelemente der Applikation "HBCI", Bankensignaturkarte ohne Zertifikat</td>
<td>107</td>
</tr>
<tr>
<td rowspan="2">Abbildung 21: Datenelemente der Applikation "HBCI", Bankensignaturkarte mit Zertifikat</td>
<td></td>
</tr>
<tr>
<td>124</td>
</tr>
</table>


<!-- PageBreak -->


<table>
<tr>
<th>Kapitel:</th>
<th>Version: 3.0 - Final Version</th>
<th>Financial Transaction Services (FinTS) Dokument: Security - Sicherheitsverfahren HBCI</th>
</tr>
<tr>
<td>Seite:<br>4</td>
<td>Stand: 18.07.2013</td>
<td>Kapitel:<br>Abbildungsverzeichnis</td>
</tr>
</table>


Abbildung 22: Datenelemente der Applikation "HBCI", Bankensignaturkarte
ohne Zertifikat

<!-- PageNumber: 125 -->
<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th rowspan="2">Version: 3.0 - Final Version</th>
<th rowspan="2">Kapitel:</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Security - Sicherheitsverfahren HBCI</td>
</tr>
<tr>
<td>Kapitel:</td>
<td>Abkürzungen</td>
<td>Stand: 18.07.2013</td>
<td>Seite: 5</td>
</tr>
</table>


## Abkürzungen


<table>
<tr>
<td>Abkürzung</td>
<td>Bedeutung</td>
</tr>
<tr>
<td>AC</td>
<td>Access Condition</td>
</tr>
<tr>
<td>AEF</td>
<td>Application Elementary File</td>
</tr>
<tr>
<td>AES</td>
<td>Advanced Encryption Standard</td>
</tr>
<tr>
<td>AID</td>
<td>Application Identifier</td>
</tr>
<tr>
<td>BPD</td>
<td>Bankparameterdaten</td>
</tr>
<tr>
<td>C</td>
<td>Datenstruktur ist konditional</td>
</tr>
<tr>
<td>CBC</td>
<td>Cipher Block Chaining</td>
</tr>
<tr>
<td>CID</td>
<td>Cardholders Information Data (Kartenidentifikationsdaten der ZKA- Chipkarte)</td>
</tr>
<tr>
<td>CLA</td>
<td>Class Byte</td>
</tr>
<tr>
<td>CR</td>
<td>Carriage-Return (Wagenrücklauf)</td>
</tr>
<tr>
<td>DDV</td>
<td>DES-DES-Verfahren</td>
</tr>
<tr>
<td>DE</td>
<td>Datenelement</td>
</tr>
<tr>
<td>DEG</td>
<td>Datenelementgruppe</td>
</tr>
<tr>
<td>DES</td>
<td>Data Encryption Standard</td>
</tr>
<tr>
<td>DF</td>
<td>Dedicated File</td>
</tr>
<tr>
<td>DFÜ</td>
<td>Synonym verwendet für "Datenkommunikation, die in Form von Fi- letransfer, E-Mail, Online-Nachrichtenaustausch etc. erfolgen kann</td>
</tr>
<tr>
<td>DK</td>
<td>Die Deutsche Kreditwirtschaft</td>
</tr>
<tr>
<td>ECB</td>
<td>Electronic Code Book</td>
</tr>
<tr>
<td>EDIFACT</td>
<td>Electronic Data Interchange for Administration, Commerce and Transport</td>
</tr>
<tr>
<td>EF</td>
<td>Elementary File</td>
</tr>
<tr>
<td>EU</td>
<td>Elektronische Unterschrift; basiert auf dem asymmetrischen RSA- Verfahren</td>
</tr>
<tr>
<td>FCI</td>
<td>File Control Information</td>
</tr>
<tr>
<td>FCP</td>
<td>File Control Parameters</td>
</tr>
<tr>
<td>FCS</td>
<td>Frame Check Sequence</td>
</tr>
<tr>
<td>FMD</td>
<td>File Management Data</td>
</tr>
<tr>
<td>GD</td>
<td>Gruppendatenelement</td>
</tr>
<tr>
<td>GDG</td>
<td>Gruppendatenelementgruppe</td>
</tr>
<tr>
<td>HBCI</td>
<td>Homebanking Computer Interface</td>
</tr>
<tr>
<td>I</td>
<td>Information (z.B. Schlüsselart)</td>
</tr>
<tr>
<td>ID</td>
<td>Identifikationsmerkmal (Nummer oder alphanumerischer Code)</td>
</tr>
<tr>
<td>ISO</td>
<td>International Organisation for Standardisation</td>
</tr>
<tr>
<td>IV</td>
<td>Initialisierungsvektor</td>
</tr>
<tr>
<td>KGK</td>
<td>Key Generating Key</td>
</tr>
</table>


<!-- PageBreak -->


<table>
<tr>
<th>Kapitel:</th>
<th>Version: 3.0 - Final Version</th>
<th>Financial Transaction Services (FinTS) Dokument: Security - Sicherheitsverfahren HBCI</th>
</tr>
<tr>
<td>Seite:</td>
<td>Stand:</td>
<td>Kapitel: Abkürzungen</td>
</tr>
<tr>
<td>6</td>
<td>18.07.2013</td>
<td></td>
</tr>
</table>


<table>
<tr>
<td>Abkürzung</td>
<td>Bedeutung</td>
</tr>
<tr>
<td>LF</td>
<td>Line-Feed (neue Zeile)</td>
</tr>
<tr>
<td>M</td>
<td>Datenstruktur muss vorhanden sein und ist inhaltlich korrekt zu füllen</td>
</tr>
<tr>
<td>MAC</td>
<td>Message Authentication Code; Symmetrisches Verfahren zur Erzeu- gung einer elektronischen Signatur (derzeit für die ZKA-Chipkarte ein- gesetzt)</td>
</tr>
<tr>
<td>MF</td>
<td>Master File</td>
</tr>
<tr>
<td>MFC</td>
<td>Multifunktions-Chipkarte</td>
</tr>
<tr>
<td>MIME</td>
<td>Multipurpose Internet Mail Extensions</td>
</tr>
<tr>
<td>N</td>
<td>Nachricht</td>
</tr>
<tr>
<td>N</td>
<td>Nicht erlaubt (not allowed) (Datenstruktur darf nicht vorhanden sein)</td>
</tr>
<tr>
<td>O</td>
<td>Datenstruktur ist optional</td>
</tr>
<tr>
<td>OID</td>
<td>Object IDentifier</td>
</tr>
<tr>
<td>PKD</td>
<td>Public-Key-Daten</td>
</tr>
<tr>
<td>RAH</td>
<td>RSA-AES-Hybridverfahren</td>
</tr>
<tr>
<td>RDH</td>
<td>RSA-DES-Hybridverfahren</td>
</tr>
<tr>
<td>RFC</td>
<td>Request for Comment</td>
</tr>
<tr>
<td>RSA</td>
<td>Asymmetrischer Algorithmus für die elektronische Unterschrift (EU) (vgl. MAC), benannt nach den Erfindern Rivest, Shamir und Adleman.</td>
</tr>
<tr>
<td>SEG</td>
<td>Segment</td>
</tr>
<tr>
<td>SEQ</td>
<td>Sequenznummer</td>
</tr>
<tr>
<td>SF</td>
<td>Segmentfolge</td>
</tr>
<tr>
<td>SFI</td>
<td>Short File Identifier</td>
</tr>
<tr>
<td>SHA</td>
<td>Secure Hash Algorithm</td>
</tr>
<tr>
<td>SSL</td>
<td>Secure Socket Layer</td>
</tr>
<tr>
<td>T</td>
<td>Transaktion (z.B. Schlüsselart)</td>
</tr>
<tr>
<td>UN/EDIFACT</td>
<td>s. EDIFACT</td>
</tr>
<tr>
<td>UPD</td>
<td>Userparameterdaten</td>
</tr>
<tr>
<td>ZKA</td>
<td>Zentraler Kreditausschuss</td>
</tr>
</table>


<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th rowspan="2">Version: 3.0 - Final Version</th>
<th rowspan="2">Kapitel:</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Security - Sicherheitsverfahren HBCI</td>
</tr>
<tr>
<td>Kapitel:</td>
<td>Literaturhinweise</td>
<td>Stand: 18.07.2013</td>
<td>Seite: 7</td>
</tr>
</table>


## Literaturhinweise


### . Allgemeines

[DF_NOTEPAD] Genereller
Aufbau
der
SECCOS-Applikation
Notepad
(„DF_NOTEPAD“) für FinTS und das DFÜ-Abkommen , Version
3.0, 21.06.2005, Zentraler Kreditausschuss

[Formals]
Financial Transaction Services (FinTS) - Formals (Allgemeine
Festlegungen für multibankfähige Online-Verfahren der deutschen
Kreditwirtschaft), Version 3.0, 14.06.2011, Zentraler Kreditaus-
schuss

[HKAZS]
Financial Transaction Services (FinTS) - Security, Alternative Si-
cherheitsverfahren, Version 3.0, 22.01.2013, Die Deutsche Kredit-
wirtschaft

[ISO 3166]
ISO 3166-1:1996: Code for the representation of names of coun-
tries and their subdivisions - Part 1: Country code
http://www.din.de/gremien/nas/nabd/iso3166ma/ oder
http://www.unece.org/trade/lcode/loc99.zip)


### ◆ Verfahrensbeschreibung

[AES]
Federal Information Processing Standards 197 v. 26. November
2001, National Institute of Standards and Technology (NIST)

[SigG]
Gesetz über Rahmenbedingungen für elektronische Signaturen
und zur Änderung weiterer Vorschriften v. 16. Mai 2001, Bundes-
gesetzblatt Jahrgang 2001, Teil I Nr. 22

[SigV]
Verordnung zur elektronischen Signatur v. 16. November 2001,
Bundesgesetzblatt Jahrgang 2001, Teil I Nr. 59

[EU-Richtlinie]
Richtlinie 1999/93/EG des Europäischen Parlaments und des Ra-
tes vom 13. Dezember 1999 über gemeinschaftliche Rahmenbe-
dingungen für elektronische Signaturen, Amtsblatt der Europäi-
schen Gemeinschaften v. 19.01.2000

[FormAnpG]
Gesetz zur Anpassung der Formvorschriften des Privatrechts und
anderer Vorschriften an den modernen Rechtsgeschäftsverkehr,
13. Juli 2001, Bundesgesetzblatt Jahrgang 2001, Teil I Nr. 35

[DFÜ-Abkommen]

Kryptographische Verfahren des deutschen Kreditgewerbes für die
Elektronische Unterschrift und für die Verschlüsselung im Rahmen
der Kunde-Bank-Kommunikation

in: Anlage 1 der Schnittstellenspezifikation für die Datenfernüber-
tragung zwischen Kunde und Kreditinstitut gemäß DFÜ-
Abkommen - Spezifikation für die EBICS-Anbindung, Version 2.5,
16.05.2011

<!-- PageBreak -->


<table>
<tr>
<th>Kapitel:</th>
<th>Version: 3.0 - Final Version</th>
<th>Financial Transaction Services (FinTS) Dokument: Security - Sicherheitsverfahren HBCI</th>
</tr>
<tr>
<td>Seite:<br>8</td>
<td>Stand: 18.07.2013</td>
<td>Kapitel: Literaturhinweise</td>
</tr>
</table>


<table>
<tr>
<td>[DK Krypto]</td>
<td>ZKA Kryptographie - Teil 1: Empfohlene kryptographische Algo- rithmen, Version 1.0</td>
</tr>
<tr>
<td>[ISO 9735-5]</td>
<td>ISO 9735-5:1999 Electronic data interchange for administration, commerce and transport - (EDIFACT) - Application level syntax rules; (Syntax version number: 4) - Part 5: Security rules for batch EDI (Authenticity; Integrity and Non-repudiation of origin)</td>
</tr>
<tr>
<td>[ISO 9735-7]</td>
<td>ISO 9735-7:1999 Electronic data interchange for administration, commerce and transport - (EDIFACT) - Application level syntax rules; (Syntax version number: 4) - Part 7: Security rules for batch EDI (Confidentiality)</td>
</tr>
<tr>
<td>[ISO 9735-9]</td>
<td>ISO 9735-9:1999 Electronic data interchange for administration, commerce and transport - (EDIFACT) - Application level syntax rules; (Syntax version number: 4) - Part 9: Security key and certifi- cate management message (Message type - KEYMAN)</td>
</tr>
<tr>
<td>[ISO 9796]</td>
<td>ISO 9796:1991: Information technology - Security techniques - Digital signature scheme giving message recovery</td>
</tr>
<tr>
<td>[ISO 9796-2]</td>
<td>ISO 9796-2:1997: Information technology - Security techniques - Digital signature scheme giving message recovery - Part 2: Mech- anisms using a hash-function</td>
</tr>
<tr>
<td>[ISO 9796-3]</td>
<td>ISO 9796-3:2000 Information technology - Security techniques - Digital signature scheme giving message recovery - Part 3: Dis- crete logarithm based mechanisms</td>
</tr>
<tr>
<td>[ISO 10116]</td>
<td>ISO 10116:1997 Information technology Security techniques - Modes of operation for an n-bit block cipher algorithm</td>
</tr>
<tr>
<td>[ISO 10118-2]</td>
<td>ISO 10118-2:1994 Information technology - Security techniques - Hash functions Part 2: Hash functions using an n-bit block cipher algorithm</td>
</tr>
<tr>
<td>[ISO 10118-3]</td>
<td>ISO 10118-3:1998 Information technology - Security techniques - Hash functions Part 3: Dedicated hash-functions, 1998</td>
</tr>
<tr>
<td>[ISO 10126-1]</td>
<td>ISO 10126-1:1991: Banking - Procedures for message encipher- ment (wholesale) - Part 1: General principles</td>
</tr>
<tr>
<td>[ISO 10126-2]</td>
<td>ISO 10126-2:1991 Banking - Procedures for message encipher- ment (wholesale) - Part 2: DEA algorithm</td>
</tr>
<tr>
<td>[X3.92]</td>
<td>ANSI X3.92-1981 (R1987): Data Encryption Algorithm</td>
</tr>
<tr>
<td>[X3.106]</td>
<td>ANSI X3.106-1983 (R1996): Data Encryption Algorithm, Modes of operation for the</td>
</tr>
</table>


<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th rowspan="2">Version: 3.0 - Final Version</th>
<th rowspan="2">Kapitel:</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Security - Sicherheitsverfahren HBCI</td>
</tr>
<tr>
<td>Kapitel:</td>
<td>Literaturhinweise</td>
<td>Stand: 18.07.2013</td>
<td>Seite: 9</td>
</tr>
</table>


[X9.19]

ANSI X9.19-1996: Financial Institution Retail Message Authentica-
tion

[X9.23]

ANSI X9.23-1995 (R1995): Financial Institution Encryption of
Wholesale Financial Messages

[X509]

RFC 3039: Internet X.509 Public Key Infrastructure Qualified Cer-
tificates Profile

[PKCS1]

PKCS #1: RSA Cryptography Standard, Version 2.1, RSA Labora-
tories, June 2002
(ftp://ftp.rsasecurity.com/pub/pkcs/pkcs-1/pkcs-1v2-1.pdf)

[SHA-1]

FIPS 180-1, Secure Hash Standard, Federal Information Pro-
cessing Standards Publication 180-1, U. S. Department of Com-
merce / N.I.S.T., National Technical Information Service, 1995
(http://www.itl.nist.gov/fipspubs/fip180-1.htm)

[SHA-256]

Federal Information Processing Standards Publication
180-2 2002 August 1,
(http://csrc.nist.gov/publications/fips/fips180-2/fips180-2.pdf)

[ALGO]

Geeignete Kryptoalgorithmen gemäß Anlage 1, I 2, SigV vom 22.
November 2001,
aktueller Stand siehe unter http://www.bsi.de/esig/kryptoalg.htm

[ISIS/MTT]

ISIS/MTT (Industrial Signature Interoperability and MailTrusT
Specification / MailTrusT) Version 1 - Part 1: Certificate and CRL
Profiles.

[CIPHER]

EDIFACT Message Implementation Guidelines: Ciphered Text
Message. CIPHER, SJWG; Working Draft Version, Paris Septem-
ber 16th 1994

[EDIFACT SIG]

EDIFACT
Security
Implementation
Guidelines,
Trade/WP.4/R.1026/Add.2, 22 February

[KEYMAN]

MIG Handbook UN/EDIFACT Message KEYMAN (proposed draft),
June 30, 1995

[RSA]
R. Rivest, A. Shamir, L. Adleman: A method for obtaining digital
signatures and public key cryptosystems, Communications of the
ACM, vol. 21 no. 2, 1978.

[RIPEMD]
H. Dobbertin, A. Bosselaers, B. Preneel: ,RIPEMD-160, a
strengthened version of RIPEMD", Fast Software Encryption -
Cambridge Workshop 1996, LNCS, Band 1039, D. Gollmann, Ed.,
Springer-Verlag, 1996, S. 71-82
(http://www.esat.kuleuven.ac.be/~bosselae/ripemd160.html)

<!-- PageBreak -->


<table>
<tr>
<th>Kapitel:</th>
<th>Version: 3.0 - Final Version</th>
<th>Financial Transaction Services (FinTS) Dokument: Security - Sicherheitsverfahren HBCI</th>
</tr>
<tr>
<td>Seite:</td>
<td>Stand:</td>
<td>Kapitel: Literaturhinweise</td>
</tr>
<tr>
<td>10</td>
<td>18.07.2013</td>
<td></td>
</tr>
</table>


. Chipapplikationen

[ISO PIN1]
ISO 9564-1, Banking - Personal Identification Number Manage-
ment and Security, Part 1: PIN protection principles and tech-
niques, DIS 1999

[DAT-MF]
Schnittstellenspezifikation für die ec-Karte mit Chip, Dateien des
MF, Version 4.2, 01.12.1999

[LT]
Schnittstellenspezifikation für die ec-Karte mit Chip, Ladeterminal,
Version 3.0, 02.04.1998

[DATKOM]
Schnittstellenspezifikation für die ZKA-Chipkarte, Datenstrukturen
und Kommandos, Version 4.1, 01.07.1999

[KT-KONZEPT]
Schnittstellenspezifikation für die ZKA-Chipkarte, Konzept für die
Unterstützung der Signatur-Anwendung der ZKA-Chipkarte durch
das Internet-Kundenterminal, Version 1.0, 15. Februar 2002

[KT-SIG]
Schnittstellenspezifikation für die ZKA-Chipkarte, Spezifikation des
Internet-Kundenterminals für die Unterstützung der Signatur-
Anwendung der ZKA-Chipkarte (ZKA-SIG-API), Version 2.0, 10.
März 2008

[SECCOS]

Schnittstellenspezifikation für die ZKA-Chipkarte, Secure Chip
Card Operating System (SECCOS), Version 5.0, 5. Juni 2001 mit
Errata vom 13. Juni 2001

[SECCOS-6]
Interface Specifications for the SECCOS ICC Secure Chip Card
Operating System (SECCOS) Version 6.2.1, 11.11.2009

[ZKASIG]
Schnittstellenspezifikation für die ZKA-Chipkarte, Digital Signature
Application for SECCOS 6, Version 1.3.1, 10. März 2011

[DINSIG]
Chipcards with digital signature application/function according to
SigG and SigV, Part 4: Basic Security Services, DIN V66291-4
vom 14. September 2001

<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th>Version:</th>
<th>Kapitel:</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Security - Sicherheitsverfahren HBCI</td>
<td>3.0 - Final Version</td>
<td>A</td>
</tr>
<tr>
<td>Kapitel:</td>
<td>Einleitung</td>
<td>Stand:</td>
<td>Seite:</td>
</tr>
<tr>
<td>Abschnitt:</td>
<td>Allgemeines</td>
<td>18.07.2013</td>
<td>1</td>
</tr>
</table>


## A. EINLEITUNG

In diesem Dokument wird das Sicherheitsverfahren HBCI (,Homebanking Compu-
ter-Interface") beschrieben Dieses Verfahren beruht auf modernen kryptographi-
schen Methoden und Algorithmen, wie z.B. der Digitalen Signatur und Chipkarten-
technologie.

Dieses Sicherheitsverfahren kann in multibankfähigen Onlinebanking-Verfahren der
deutschen Kreditwirtschaft eingesetzt werden.

Informationen bzgl. Nachrichtenaufbau und Dialogablauf sind dem Dokument [For-
mals] zu entnehmen.

<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: B</td>
<td>Version: 3.0 - Final Version</td>
<td>Financial Transaction Services (FinTS) Dokument: Security - Sicherheitsverfahren HBCI</td>
</tr>
<tr>
<td>Seite:<br>2</td>
<td>Stand: 18.07.2013</td>
<td>Kapitel: Verfahrensbeschreibung<br>Abschnitt: Allgemeines</td>
</tr>
</table>


## B. VERFAHRENSBESCHREIBUNG


### B.1 Allgemeines

Im Rahmen von HBCI werden zeitgemäße Sicherheitsmechanismen und -methoden
eingesetzt, welche den Missbrauch der im Bereich des Homebankings eingesetzten
Systeme verhindern.

Das folgende Kapitel ist in sechs Abschnitte gegliedert, welche sich mit den verwen-
deten Sicherheitsmechanismen, den Abläufen, den bankfachlichen Anforderungen
sowie den Segmentformaten für Signatur, Verschlüsselung und Key-Management
beschäftigen.

Die Ausführungen lehnen sich an bestehende deutsche Kreditinstitutsstandards
(ZKA-Abkommen, z.B. DFÜ-Abkommen, ec-Chipkarte), sowie an internationale
Standards (z.B. ISO, UN/EDIFACT) an.

Grundsätzlich kommen im Rahmen von HBCI drei verschiedene Sicherheitslösun-
gen zum Einsatz:

· zwei auf dem asymmetrischen RSA-Verfahren basierende Lösungen

• eine auf dem symmetrischen DES-Verfahren basierende Chipkartenlösung

Die drei Varianten werden mit RAH (RSA-AES-Hybridverfahren), RDH (RSA-DES-
Hybridverfahren)_bzw. DDV (DES-DES-Verfahren) gekennzeichnet. RAH und RDH
signieren mit RSA-EU und chiffrieren den Nachrichtenschlüssel mittels RSA, wäh-
rend DDV den MAC als Signatur verwendet und den Nachrichtenschlüssel (nach-
richtenbezogener Chiffrierschlüssel) mittels 2-Key-Triple-DES verschlüsselt.

Die in Version 3.0 neu aufgenommene einheitliche Chipkartenlösung für das RAH-
respektive RDH-Verfahren ist das angestrebte Zielverfahren. Da diese Sicherheits-
konzeption momentan aufgrund technischer Restriktionen noch nicht flächende-
ckend umzusetzen ist, kommt bis zur durchgehenden Verfügbarkeit der RSA-
Chipkartenlösung zusätzlich sowohl die DDV-Lösung auf Chipkartenbasis als auch
RAH-/RDH-Lösungen auf reiner Softwarebasis oder auf Basis proprietärer Chipkar-
tenlösungen zum Einsatz.


## . RAH-Verfahren

Realisierung Bank:
verpflichtend

Realisierung Kunde: verpflichtend. Ausgenommen hiervon sind Endgeräte, die eine
RSA-EU-Lösung oder RAH-Verschlüsselung noch nicht erlau-
ben (z.B. Smartphones mit MAC-Chipkarte erlauben ggf. kei-
ne RSA-EU, PC-basierte Produkte müssen hingegen stets die
RSA-EU unterstützen).

<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th rowspan="2">Version: 3.0 - Final Version</th>
<th rowspan="2">Kapitel: B</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Security - Sicherheitsverfahren HBCI</td>
</tr>
<tr>
<td>Kapitel:</td>
<td>Verfahrensbeschreibung</td>
<td>Stand:</td>
<td>Seite:</td>
</tr>
<tr>
<td>Abschnitt:</td>
<td>Allgemeines</td>
<td>18.07.2013</td>
<td>3</td>
</tr>
</table>


## RDH-Verfahren

Realisierung Bank:

verpflichtend, falls übergangsweise das RAH-Verfahren noch
nicht angeboten werden kann

Realisierung Kunde:

verpflichtend,solange das RAH-Verfahren noch nicht flächen-
deckend eingeführt ist.

Ausgenommen hiervon sind Endgeräte, die eine RSA-EU-
Lösung oder RDH-Verschlüsselung noch nicht erlauben (z.B.
Smartphones mit MAC-Chipkarte erlauben ggf. keine RSA-
EU, PC-basierte Produkte müssen hingegen stets die RSA-
EU unterstützen).


## . DDV-Verfahren

Realisierung Bank:
optional (empfohlen)

Realisierung Kunde:
optional


### B.1.1 Sicherheitsprofile

Die Sicherheitsverfahren RAH, RDH und DDV können unterschiedlich parametrisiert
werden, wobei Sicherheitsprofile entstehen. Um Multibankfähigkeit zu gewährleis-
ten, ist bei Kommunikation auf Basis von FinTS 3.0 kundenproduktseitig die Unter-
stützung der Sicherheitsprofile RAH-7 und RDH-7, sowie RAH-9 und RDH-9 ver-
pflichtend. Aus Kompatibilitätsgründen sind die in den bisherigen FinTS-Versionen
genutzten Profile RDH-1, RDH-2, RDH-3, RDH-5, RDH-6, RDH-7, RDH-8, RDH-10,
und DDV-1 weiterhin gültig. Andere als die unten genannten Profile sind nicht zuläs-
sig.

Das Kreditinstitut teilt dem Kunden die bankseitig unterstützten Profile in den Bank-
parameterdaten mit. Der Kunde wählt aus diesen Verfahren das für ihn geeignete
Verfahren aus und bildet auf diese Weise Signatur und Verschlüsselung. Das Kre-
ditinstitut antwortet stets mit dem vom Kunden gewählten Verfahren.

Hier eine Übersicht der zugelassenen Sicherheitsprofile und deren Anwendungs-
spektrum:

<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: B</td>
<td>Version: 3.0 - Final Version</td>
<td>Financial Transaction Services (FinTS) Dokument: Security - Sicherheitsverfahren HBCI</td>
</tr>
<tr>
<td>Seite: 4</td>
<td>Stand: 18.07.2013</td>
<td>Kapitel: Verfahrensbeschreibung<br>Abschnitt: Allgemeines</td>
</tr>
</table>


<table>
<tr>
<th>Sicherheits- profil</th>
<th>Schlüssel- länge</th>
<th>Medium</th>
<th>Bemerkungen</th>
</tr>
<tr>
<td>RAH-7</td>
<td>gemäß [DK Krypto]1</td>
<td>Bankensignaturkarte SECCOS 6</td>
<td>mit SHA-256, PKCS#1 PSS Padding, AES-Verschlüsselung</td>
</tr>
<tr>
<td>RAH-9</td>
<td>gemäß [DK Krypto]</td>
<td>Bankensignaturkarte SECCOS 6</td>
<td>wie RAH-7 ohne Zertifikate</td>
</tr>
<tr>
<td>RAH-10</td>
<td>gemäß [DK Krypto]</td>
<td>RSA-SW-Lösung</td>
<td>mit SHA-256, PKCS#1 PSS Padding, AES-Verschlüsselung</td>
</tr>
<tr>
<td>RDH-1</td>
<td>708 bis 768 bit</td>
<td>RSA-SW-Lösung RSA-Chipkarte</td>
<td>RIPEMD-160_ISO 9796-1 Padding, Triple-DES-Verschlüsselung</td>
</tr>
<tr>
<td>RDH-2</td>
<td>1024 bis 2048 bit</td>
<td>RSA-SW-Lösung</td>
<td>RIPEMD-160, ISO 9796-2 Padding, Triple-DES-Verschlüsselung</td>
</tr>
<tr>
<td>RDH-3</td>
<td>1024 bis 2048 bit</td>
<td>Bankensignaturkarte SECCOS 5</td>
<td>RIPEMD-160, ISO 9796-2 Padding, Triple-DES-Verschlüsselung bzw. SHA-1_PKCS#1 V15 Padding, Triple-DES-Verschlüsselung</td>
</tr>
<tr>
<td>RDH-42</td>
<td>1024 bis 2048 bit</td>
<td>Bankensignaturkarte SECCOS 5</td>
<td>SHA-1_PKCS#1 V15 Padding, Triple-DES-Verschlüsselung</td>
</tr>
<tr>
<td>RDH-5</td>
<td>1024 bis 2048 bit</td>
<td>Bankensignaturkarte SECCOS 5</td>
<td>wie RDH-3 ohne Zertifikate</td>
</tr>
<tr>
<td>RDH-6</td>
<td>gemäß [DK Krypto]</td>
<td>Bankensignaturkarte SECCOS 5 / 6</td>
<td>mit SHA-256_PKCS#1 V15 Padding, Triple-DES-Verschlüsselung</td>
</tr>
<tr>
<td>RDH-7</td>
<td>gemäß [DK Krypto]</td>
<td>Bankensignaturkarte SECCOS 6</td>
<td>mit SHA-256_PKCS#1 PSS Padding, Triple-DES-Verschlüsselung</td>
</tr>
<tr>
<td>RDH-8</td>
<td>gemäß [DK Krypto]</td>
<td>Bankensignaturkarte SECCOS 5 / 6</td>
<td>wie RDH-6 ohne Zertifikate</td>
</tr>
<tr>
<td>RDH-9</td>
<td>gemäß [DK Krypto]</td>
<td>Bankensignaturkarte SECCOS 6</td>
<td>wie RDH-7 ohne Zertifikate</td>
</tr>
<tr>
<td>RDH-10</td>
<td>gemäß [DK Krypto]</td>
<td>RSA-SW-Lösung</td>
<td>mit SHA-256_PKCS#1 PSS Padding, Triple-DES-Verschlüsselung</td>
</tr>
</table>


Die Angaben zum SECCOS-Betriebssystem bzw. der Betriebssystemversion sind
nur als beispielhaft anzusehen; es kann auch jede gleichwertige Signaturkarte ver-
wendet werden, welche die geforderten Verfahren unterstützt.

Die Information über die Betriebssystemversion kann dem Byte 24 in EF_ID ent-
nommen werden. Dort sind derzeit folgende Werte vorgesehen:

X'01': SECCOS 5

X'06': SECCOS 6

<!-- PageFooter: 1 Die Schlüssellängen sind gemäß den Empfehlungen des DK-Kryptokatalogs [DK Krypto] zu verwen- den. -->
<!-- PageFooter: 2 2 RDH-4 ist als Verfahren obsolet, da SHA-1 als Hashverfahren für neue Einsatzzwecke nicht mehr als sicher einzustufen ist. -->
<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th rowspan="2">Version: 3.0 - Final Version</th>
<th rowspan="2">Kapitel: B</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Security - Sicherheitsverfahren HBCI</td>
</tr>
<tr>
<td>Kapitel:</td>
<td>Verfahrensbeschreibung</td>
<td>Stand:</td>
<td>Seite:</td>
</tr>
<tr>
<td>Abschnitt:</td>
<td>Allgemeines</td>
<td>18.07.2013</td>
<td>5</td>
</tr>
</table>


## RAH-7

Als Sicherheitsmedium für das Kundensystem ist nur die Bankensignaturkarte oder
eine gleichwertige Signaturkarte zugelassen.


<table>
<tr>
<th>Parameter</th>
<th>Wert</th>
<th>Bedeutung</th>
</tr>
<tr>
<td>Signaturalgorithmus, kodiert</td>
<td>10</td>
<td>RSA</td>
</tr>
<tr>
<td>Operationsmodus bei Signatur</td>
<td>19</td>
<td>Signier- und Signaturschlüs- sel - RSASSA- PSS [PKCS1]</td>
</tr>
<tr>
<td>Verwendung des Signaturalgorithmus</td>
<td>6</td>
<td>Owner Signing</td>
</tr>
<tr>
<td>Hashalgorithmus, kodiert</td>
<td>6<br>3</td>
<td>Signierschlüssel - SHA-256 / SHA-256 [SHA-256] Signaturschlüssel - SHA- 256 [SHA-256]</td>
</tr>
<tr>
<td>Verschlüsselungsalgorithmus, kodiert</td>
<td>14</td>
<td>AES-256 [AES]</td>
</tr>
<tr>
<td>Operationsmodus bei Verschlüsselung</td>
<td>18</td>
<td>RSAES-PKCS1-v1 5 [PKCS1]</td>
</tr>
<tr>
<td>Schlüsselart</td>
<td>S<br>V<br>D</td>
<td>Signierschlüssel Chiffrierschlüssel Schlüssel für Digitale Signa- turen</td>
</tr>
<tr>
<td>Schlüssellänge</td>
<td>gemäß [DK Krypto]</td>
<td></td>
</tr>
<tr>
<td>Zertifikatstyp</td>
<td>3</td>
<td>X.509</td>
</tr>
<tr>
<td>Zertifikatsinhalt</td>
<td>EF X509.CH.DS</td>
<td>fortgeschritten oder qualifi- ziert abh. von der Sicher- heitsklasse</td>
</tr>
</table>


Im Rahmen des Paddingverfahrens RSASSA-PSS wird als ,,Mask Generation Func-
tion" MGF1 verwendet. Beim Signierschlüssel wird ein doppeltes Hashing (Software
und Bankensignaturkarte) durchgeführt. Dies wird durch eine spezielle Ausprägung
des ,,Hashalgorithmus, kodiert“ gekennzeichnet.

Als Salt-Länge (Länge des Initialwertes) ist die Länge des Hashwertes zu verwen-
den. Diese Festlegung ist z. B. auch Bestandteil der SECCOS 6 Spezifikation.

<!-- PageNumber: I -->
<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: B</td>
<td>Version: 3.0 - Final Version</td>
<td>Financial Transaction Services (FinTS) Dokument: Security - Sicherheitsverfahren HBCI</td>
</tr>
<tr>
<td>Seite: 6</td>
<td>Stand: 18.07.2013</td>
<td>Kapitel: Verfahrensbeschreibung<br>Abschnitt: Allgemeines</td>
</tr>
</table>


## RAH-9

Als Sicherheitsmedium für das Kundensystem ist nur die Bankensignaturkarte oder
eine gleichwertige Signaturkarte zugelassen.


<table>
<tr>
<th>Parameter</th>
<th>Wert</th>
<th>Bedeutung/Anmerkung</th>
</tr>
<tr>
<td>Signaturalgorithmus, kodiert</td>
<td>10</td>
<td>RSA</td>
</tr>
<tr>
<td>Operationsmodus bei Signatur</td>
<td>19</td>
<td>RSASSA-PSS [PKCS1]</td>
</tr>
<tr>
<td>Verwendung des Signaturalgorithmus</td>
<td>6</td>
<td>Owner Signing</td>
</tr>
<tr>
<td>Hashalgorithmus, kodiert</td>
<td>6</td>
<td>SHA-256 / SHA-256 [SHA-256]</td>
</tr>
<tr>
<td>Verschlüsselungsalgorithmus, kodiert</td>
<td>14</td>
<td>AES-256 [AES]</td>
</tr>
<tr>
<td>Operationsmodus bei Verschlüsselung</td>
<td>18</td>
<td>RSAES-PKCS1-v1 5 [PKCS1]</td>
</tr>
<tr>
<td>Schlüsselart</td>
<td>V</td>
<td>Signierschlüssel Chiffrierschlüssel</td>
</tr>
<tr>
<td>Schlüssellänge</td>
<td>gemäß [DK Krypto]</td>
<td></td>
</tr>
<tr>
<td>Zertifikatstyp</td>
<td></td>
<td>ohne</td>
</tr>
<tr>
<td>Zertifikatsinhalt</td>
<td>nicht spezifiziert</td>
<td></td>
</tr>
</table>


Im Rahmen des Paddingverfahrens RSASSA-PSS wird als ,,Mask Generation Func-
tion" MGF1 verwendet. Beim Signierschlüssel wird ein doppeltes Hashing (Software
und Bankensignaturkarte) durchgeführt. Dies wird durch eine spezielle Ausprägung
des ,,Hashalgorithmus, kodiert" gekennzeichnet.

Als Salt-Länge (Länge des Initialwertes) ist die Länge des Hashwertes zu verwen-
den. Diese Festlegung ist z. B. auch Bestandteil der SECCOS 6 Spezifikation.


## RAH-10

Als Sicherheitsmedium für das Kundensystem ist eine RSA-Softwarelösung zuge-
lassen.


<table>
<tr>
<th>Parameter</th>
<th>Wert</th>
<th>Bedeutung/Anmerkung</th>
</tr>
<tr>
<td>Signaturalgorithmus, kodiert</td>
<td>10</td>
<td>RSA</td>
</tr>
<tr>
<td>Operationsmodus bei Signatur</td>
<td>19</td>
<td>RSASSA-PSS [PKCS1]</td>
</tr>
<tr>
<td>Verwendung des Signaturalgorithmus</td>
<td>6</td>
<td>Owner Signing</td>
</tr>
<tr>
<td>Hashalgorithmus, kodiert</td>
<td>6</td>
<td>SHA-256 / SHA-256 [SHA-256]</td>
</tr>
<tr>
<td>Verschlüsselungsalgorithmus, kodiert</td>
<td>14</td>
<td>AES-256 [AES]</td>
</tr>
<tr>
<td>Operationsmodus bei Verschlüsselung</td>
<td>2</td>
<td>CBC (0-Padding)</td>
</tr>
<tr>
<td>Schlüsselart</td>
<td>S<br>V</td>
<td>Signierschlüssel Chiffrierschlüssel</td>
</tr>
<tr>
<td>Schlüssellänge</td>
<td>gemäß [DK Krypto]</td>
<td></td>
</tr>
<tr>
<td>Zertifikatstyp</td>
<td>1 2<br>3</td>
<td>ZKA UN/EDIFACT X.509</td>
</tr>
<tr>
<td>Zertifikatsinhalt</td>
<td>nicht spezifiziert</td>
<td></td>
</tr>
</table>


Im Rahmen des Paddingverfahrens RSASSA-PSS wird als ,,Mask Generation Func-
tion" MGF1 verwendet. Beim Signierschlüssel wird ein doppeltes Hashing durchge-
führt. Dies wird durch eine spezielle Ausprägung des ,,Hashalgorithmus, kodiert" ge-
kennzeichnet.

<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th>Version:</th>
<th>Kapitel:</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Security - Sicherheitsverfahren HBCI</td>
<td>3.0 - Final Version</td>
<td>B</td>
</tr>
<tr>
<td>Kapitel:</td>
<td>Verfahrensbeschreibung</td>
<td>Stand:</td>
<td>Seite:</td>
</tr>
<tr>
<td>Abschnitt:</td>
<td>Allgemeines</td>
<td>18.07.2013</td>
<td>7</td>
</tr>
</table>


Als Salt-Länge (Länge des Initialwertes) ist die Länge des Hashwertes zu verwen-
den.

<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: B</td>
<td>Version: 3.0 - Final Version</td>
<td>Financial Transaction Services (FinTS) Dokument: Security - Sicherheitsverfahren HBCI</td>
</tr>
<tr>
<td>Seite: 8</td>
<td>Stand: 18.07.2013</td>
<td>Kapitel: Verfahrensbeschreibung<br>Abschnitt: Allgemeines</td>
</tr>
</table>


## . RDH-1

Als Sicherheitsmedien für das Kundensystem sind RSA-Softwarelösungen und
RSA-Chipkarten zugelassen.


<table>
<tr>
<th>Parameter</th>
<th>Wert</th>
<th>Bedeutung/Anmerkung</th>
</tr>
<tr>
<td>Signaturalgorithmus, kodiert</td>
<td>10</td>
<td>RSA</td>
</tr>
<tr>
<td>Operationsmodus bei Signatur</td>
<td>16</td>
<td>ISO 9796-1</td>
</tr>
<tr>
<td>Verwendung des Signaturalgorithmus</td>
<td>6</td>
<td>Owner Signing</td>
</tr>
<tr>
<td>Hashalgorithmus, kodiert</td>
<td>999</td>
<td>RIPEMD-160</td>
</tr>
<tr>
<td>Verschlüsselungsalgorithmus, kodiert</td>
<td>13</td>
<td>2-Key-Triple-DES</td>
</tr>
<tr>
<td>Operationsmodus bei Verschlüsselung</td>
<td>2</td>
<td>CBC (0-Padding)</td>
</tr>
<tr>
<td>Schlüsselart</td>
<td>S<br>V</td>
<td>Signierschlüssel Chiffrierschlüssel</td>
</tr>
<tr>
<td>Schlüssellänge</td>
<td>708-768 Bit</td>
<td></td>
</tr>
<tr>
<td>Zertifikatstyp</td>
<td>1<br>2<br>3</td>
<td>ZKA UN/EDIFACT X.509</td>
</tr>
<tr>
<td>Zertifikatsinhalt</td>
<td>nicht spezifiziert</td>
<td></td>
</tr>
</table>


## . RDH-2

Als Sicherheitsmedium für das Kundensystem ist eine RSA-Softwarelösung zuge-
lassen.


<table>
<tr>
<th>Parameter</th>
<th>Wert</th>
<th>Bedeutung/Anmerkung</th>
</tr>
<tr>
<td>Signaturalgorithmus, kodiert</td>
<td>10</td>
<td>RSA</td>
</tr>
<tr>
<td>Operationsmodus bei Signatur</td>
<td>17</td>
<td>ISO 9796-2</td>
</tr>
<tr>
<td>Verwendung des Signaturalgorithmus</td>
<td>6</td>
<td>Owner Signing</td>
</tr>
<tr>
<td>Hashalgorithmus, kodiert</td>
<td>999</td>
<td>RIPEMD-160</td>
</tr>
<tr>
<td>Verschlüsselungsalgorithmus, kodiert</td>
<td>13</td>
<td>2-Key-Triple-DES</td>
</tr>
<tr>
<td>Operationsmodus bei Verschlüsselung</td>
<td>2</td>
<td>CBC (0-Padding)</td>
</tr>
<tr>
<td>Schlüsselart</td>
<td>S<br>V</td>
<td>Signierschlüssel Chiffrierschlüssel</td>
</tr>
<tr>
<td>Schlüssellänge</td>
<td>1024-2048 Bit</td>
<td></td>
</tr>
<tr>
<td>Zertifikatstyp</td>
<td>1<br>2<br>3</td>
<td>ZKA UN/EDIFACT X.509</td>
</tr>
<tr>
<td>Zertifikatsinhalt</td>
<td>nicht spezifiziert</td>
<td></td>
</tr>
</table>


## . RDH-3

Als Sicherheitsmedium für das Kundensystem ist nur die Bankensignaturkarte oder
eine gleichwertige Signaturkarte zugelassen.

<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th>Version:</th>
<th>Kapitel:</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Security - Sicherheitsverfahren HBCI</td>
<td>3.0 - Final Version</td>
<td>B</td>
</tr>
<tr>
<td>Kapitel:</td>
<td>Verfahrensbeschreibung</td>
<td>Stand:</td>
<td>Seite:</td>
</tr>
<tr>
<td>Abschnitt:</td>
<td>Allgemeines</td>
<td>18.07.2013</td>
<td>9</td>
</tr>
</table>


<table>
<tr>
<th>Parameter</th>
<th>Wert</th>
<th>Bedeutung/Anmerkung</th>
</tr>
<tr>
<td>Signaturalgorithmus, kodiert</td>
<td>10</td>
<td>RSA</td>
</tr>
<tr>
<td>Operationsmodus bei Signatur</td>
<td>18 (bei S)<br>17 (bei D)</td>
<td>Signierschlüssel: RSASSA-PKCS1-v1_5 [PKCS1] Signaturschlüssel: ISO 9796-2</td>
</tr>
<tr>
<td>Verwendung des Signaturalgorithmus</td>
<td>6</td>
<td>Owner Signing</td>
</tr>
<tr>
<td>Hashalgorithmus, kodiert</td>
<td>1 (bei S) 999 (bei D)</td>
<td>Signierschlüssel: SHA-1 Signaturschlüssel: RIPEMD-160</td>
</tr>
<tr>
<td>Verschlüsselungsalgorithmus, kodiert</td>
<td>13</td>
<td>2-Key-Triple-DES</td>
</tr>
<tr>
<td>Operationsmodus bei Verschlüsselung4</td>
<td>18</td>
<td>RSAES-PKCS1-V1_5 [PKCS1]</td>
</tr>
<tr>
<td>Schlüsselart</td>
<td>S V<br>D</td>
<td>Signierschlüssel Chiffrierschlüssel Schlüssel für Digitale Signa- turen</td>
</tr>
<tr>
<td>Schlüssellänge</td>
<td>1024-2048 Bit</td>
<td></td>
</tr>
<tr>
<td>Zertifikatstyp</td>
<td>3</td>
<td>X.509</td>
</tr>
<tr>
<td>Zertifikatsinhalt</td>
<td>EF_X509.CH.DS</td>
<td>fortgeschritten oder qualifi- ziert abh. von der Sicher- heitsklasse</td>
</tr>
</table>


## . RDH-4

Das Verfahren RDH-4 ist obsolet, da es SHA-1 als Hashwertverfahren einsetzt und
daher für Neu-Anwendungen nicht mehr als sicher gelten kann.


## . RDH-5

Als Sicherheitsmedium für das Kundensystem ist eine Bankensignaturkarte oder ei-
ne gleichwertige Signaturkarte zugelassen.


<table>
<tr>
<th>Parameter</th>
<th>Wert</th>
<th>Bedeutung/Anmerkung</th>
</tr>
<tr>
<td>Signaturalgorithmus, kodiert</td>
<td>10</td>
<td>RSA</td>
</tr>
<tr>
<td>Operationsmodus bei Signatur</td>
<td>18</td>
<td>RSASSA-PKCS1-v1_5 [PKCS1]</td>
</tr>
<tr>
<td>Verwendung des Signaturalgorithmus</td>
<td>6</td>
<td>Owner Signing</td>
</tr>
<tr>
<td>Hashalgorithmus, kodiert</td>
<td>1</td>
<td>SHA1</td>
</tr>
<tr>
<td>Verschlüsselungsalgorithmus, kodiert</td>
<td>13</td>
<td>2-Key-Triple-DES</td>
</tr>
<tr>
<td>Operationsmodus bei Verschlüsselung</td>
<td>18</td>
<td>RSAES-PKCS1-v1_5 [PKCS1]</td>
</tr>
<tr>
<td>Schlüsselart</td>
<td>S V</td>
<td>Signierschlüssel Chiffrierschlüssel</td>
</tr>
<tr>
<td>Schlüssellänge</td>
<td>1024-2048 Bit</td>
<td></td>
</tr>
<tr>
<td>Zertifikatstyp</td>
<td></td>
<td>ohne</td>
</tr>
<tr>
<td>Zertifikatsinhalt</td>
<td>nicht spezifiziert</td>
<td></td>
</tr>
<tr>
<td>Kapitel: B</td>
<td>Version: 3.0 - Final Version</td>
<td>Financial Transaction Services (FinTS) Dokument: Security - Sicherheitsverfahren HBCI</td>
</tr>
<tr>
<td>Seite: 10</td>
<td>Stand: 18.07.2013</td>
<td>Kapitel: Verfahrensbeschreibung<br>Abschnitt: Allgemeines</td>
</tr>
</table>


## . RDH-6

Als Sicherheitsmedium für das Kundensystem ist nur die Bankensignaturkarte oder
eine gleichwertige Signaturkarte zugelassen.


<table>
<tr>
<th>Parameter</th>
<th>Wert</th>
<th>Bedeutung</th>
</tr>
<tr>
<td>Signaturalgorithmus, kodiert</td>
<td>10</td>
<td>RSA</td>
</tr>
<tr>
<td>Operationsmodus bei Signatur</td>
<td>18</td>
<td>Signier- und Signaturschlüs- sel - RSASSA -PKCS1- v1_5 [PKCS1]</td>
</tr>
<tr>
<td>Verwendung des Signaturalgorithmus</td>
<td>6</td>
<td>Owner Signing</td>
</tr>
<tr>
<td>Hashalgorithmus, kodiert</td>
<td>3</td>
<td>SHA-256 [SHA-256]</td>
</tr>
<tr>
<td>Verschlüsselungsalgorithmus, kodiert</td>
<td>13</td>
<td>2-Key-Triple-DES</td>
</tr>
<tr>
<td>Operationsmodus bei Verschlüsselung</td>
<td>18</td>
<td>RSAES-PKCS1-v1_5 [PKCS1]</td>
</tr>
<tr>
<td>Schlüsselart</td>
<td>S<br>V<br>D</td>
<td>Signierschlüssel Chiffrierschlüssel Schlüssel für Digitale Signa- turen</td>
</tr>
<tr>
<td>Schlüssellänge</td>
<td>gemäß [DK Krypto]</td>
<td></td>
</tr>
<tr>
<td>Zertifikatstyp</td>
<td>3</td>
<td>X.509</td>
</tr>
<tr>
<td>Zertifikatsinhalt</td>
<td>EF_X509.CH.DS</td>
<td>fortgeschritten oder qualifi- ziert abh. von der Sicher- heitsklasse</td>
</tr>
</table>


<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th>Version:</th>
<th rowspan="2">Kapitel: B</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Security - Sicherheitsverfahren HBCI</td>
<td>3.0 - Final Version</td>
</tr>
<tr>
<td>Kapitel:</td>
<td>Verfahrensbeschreibung</td>
<td>Stand:</td>
<td>Seite:</td>
</tr>
<tr>
<td>Abschnitt:</td>
<td>Allgemeines</td>
<td>18.07.2013</td>
<td>11</td>
</tr>
</table>


## . RDH-7

Als Sicherheitsmedium für das Kundensystem ist nur die Bankensignaturkarte oder
eine gleichwertige Signaturkarte zugelassen.


<table>
<tr>
<th>Parameter</th>
<th>Wert</th>
<th>Bedeutung</th>
</tr>
<tr>
<td>Signaturalgorithmus, kodiert</td>
<td>10</td>
<td>RSA</td>
</tr>
<tr>
<td>Operationsmodus bei Signatur</td>
<td>19</td>
<td>Signier- und Signaturschlüs- sel - RSASSA- PSS [PKCS1]</td>
</tr>
<tr>
<td>Verwendung des Signaturalgorithmus</td>
<td>6</td>
<td>Owner Signing</td>
</tr>
<tr>
<td>Hashalgorithmus, kodiert</td>
<td>6<br>3</td>
<td>Signierschlüssel - SHA-256 / SHA-256 [SHA-256] Signaturschlüssel - SHA- 256 [SHA-256]</td>
</tr>
<tr>
<td>Verschlüsselungsalgorithmus, kodiert</td>
<td>13</td>
<td>2-Key-Triple-DES</td>
</tr>
<tr>
<td>Operationsmodus bei Verschlüsselung</td>
<td>18</td>
<td>RSAES-PKCS1-v1_5 [PKCS1]</td>
</tr>
<tr>
<td>Schlüsselart</td>
<td>S V<br>D</td>
<td>Signierschlüssel Chiffrierschlüssel Schlüssel für Digitale Signa- turen</td>
</tr>
<tr>
<td>Schlüssellänge</td>
<td>gemäß [DK Krypto]</td>
<td></td>
</tr>
<tr>
<td>Zertifikatstyp</td>
<td>3</td>
<td>X.509</td>
</tr>
<tr>
<td>Zertifikatsinhalt</td>
<td>EF_X509.CH.DS</td>
<td>fortgeschritten oder qualifi- ziert abh. von der Sicher- heitsklasse</td>
</tr>
</table>


Im Rahmen des Paddingverfahrens RSASSA-PSS wird als ,,Mask Generation Func-
tion" MGF1 verwendet. Beim Signierschlüssel wird ein doppeltes Hashing (Software
und Bankensignaturkarte) durchgeführt. Dies wird durch eine spezielle Ausprägung
des ,,Hashalgorithmus, kodiert“ gekennzeichnet.

Als Salt-Länge (Länge des Initialwertes) ist die Länge des Hashwertes zu verwen-
den. Diese Festlegung ist z. B. auch Bestandteil der SECCOS 6 Spezifikation.

<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: B</td>
<td>Version: 3.0 - Final Version</td>
<td>Financial Transaction Services (FinTS) Dokument: Security - Sicherheitsverfahren HBCI</td>
</tr>
<tr>
<td>Seite: 12</td>
<td>Stand: 18.07.2013</td>
<td>Kapitel: Verfahrensbeschreibung<br>Abschnitt: Allgemeines</td>
</tr>
</table>


## . RDH-8

Als Sicherheitsmedium für das Kundensystem ist nur die Bankensignaturkarte oder
eine gleichwertige Signaturkarte zugelassen.


<table>
<tr>
<th>Parameter</th>
<th>Wert</th>
<th>Bedeutung/Anmerkung</th>
</tr>
<tr>
<td>Signaturalgorithmus, kodiert</td>
<td>10</td>
<td>RSA</td>
</tr>
<tr>
<td>Operationsmodus bei Signatur</td>
<td>18</td>
<td>RSASSA-PKCS1-v1_5 [PKCS1]</td>
</tr>
<tr>
<td>Verwendung des Signaturalgorithmus</td>
<td>6</td>
<td>Owner Signing</td>
</tr>
<tr>
<td>Hashalgorithmus, kodiert</td>
<td>3</td>
<td>SHA-256 [SHA-256]</td>
</tr>
<tr>
<td>Verschlüsselungsalgorithmus, kodiert</td>
<td>13</td>
<td>2-Key-Triple-DES</td>
</tr>
<tr>
<td>Operationsmodus bei Verschlüsselung</td>
<td>18</td>
<td>RSAES-PKCS1-v1_5 [PKCS1]</td>
</tr>
<tr>
<td>Schlüsselart</td>
<td>S V</td>
<td>Signierschlüssel Chiffrierschlüssel</td>
</tr>
<tr>
<td>Schlüssellänge</td>
<td>gemäß [DK Krypto]</td>
<td></td>
</tr>
<tr>
<td>Zertifikatstyp</td>
<td></td>
<td>ohne</td>
</tr>
<tr>
<td>Zertifikatsinhalt</td>
<td>nicht spezifiziert</td>
<td></td>
</tr>
</table>


## . RDH-9

Als Sicherheitsmedium für das Kundensystem ist nur die Bankensignaturkarte mit
oder eine gleichwertige Signaturkarte zugelassen.


<table>
<tr>
<th>Parameter</th>
<th>Wert</th>
<th>Bedeutung/Anmerkung</th>
</tr>
<tr>
<td>Signaturalgorithmus, kodiert</td>
<td>10</td>
<td>RSA</td>
</tr>
<tr>
<td>Operationsmodus bei Signatur</td>
<td>19</td>
<td>RSASSA-PSS [PKCS1]</td>
</tr>
<tr>
<td>Verwendung des Signaturalgorithmus</td>
<td>6</td>
<td>Owner Signing</td>
</tr>
<tr>
<td>Hashalgorithmus, kodiert</td>
<td>6</td>
<td>SHA-256 / SHA-256 [SHA-256]</td>
</tr>
<tr>
<td>Verschlüsselungsalgorithmus, kodiert</td>
<td>13</td>
<td>2-Key-Triple-DES</td>
</tr>
<tr>
<td>Operationsmodus bei Verschlüsselung</td>
<td>18</td>
<td>RSAES-PKCS1-v1_5 [PKCS1]</td>
</tr>
<tr>
<td>Schlüsselart</td>
<td>S V</td>
<td>Signierschlüssel Chiffrierschlüssel</td>
</tr>
<tr>
<td>Schlüssellänge</td>
<td>gemäß [DK Krypto]</td>
<td></td>
</tr>
<tr>
<td>Zertifikatstyp</td>
<td></td>
<td>ohne</td>
</tr>
<tr>
<td>Zertifikatsinhalt</td>
<td>nicht spezifiziert</td>
<td></td>
</tr>
</table>


Im Rahmen des Paddingverfahrens RSASSA-PSS wird als ,,Mask Generation Func-
tion" MGF1 verwendet. Beim Signierschlüssel wird ein doppeltes Hashing (Software
und Bankensignaturkarte) durchgeführt. Dies wird durch eine spezielle Ausprägung
des ,,Hashalgorithmus, kodiert" gekennzeichnet.

Als Salt-Länge (Länge des Initialwertes) ist die Länge des Hashwertes zu verwen-
den. Diese Festlegung ist z. B. auch Bestandteil der SECCOS 6 Spezifikation.

<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th>Version:</th>
<th rowspan="2">Kapitel: B</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Security - Sicherheitsverfahren HBCI</td>
<td>3.0 - Final Version</td>
</tr>
<tr>
<td>Kapitel:</td>
<td>Verfahrensbeschreibung</td>
<td>Stand:</td>
<td>Seite:</td>
</tr>
<tr>
<td>Abschnitt:</td>
<td>Allgemeines</td>
<td>18.07.2013</td>
<td>13</td>
</tr>
</table>


## . RDH-10

Als Sicherheitsmedium für das Kundensystem ist eine RSA-Softwarelösung zuge-
lassen.


<table>
<tr>
<th>Parameter</th>
<th>Wert</th>
<th>Bedeutung/Anmerkung</th>
</tr>
<tr>
<td>Signaturalgorithmus, kodiert</td>
<td>10</td>
<td>RSA</td>
</tr>
<tr>
<td>Operationsmodus bei Signatur</td>
<td>19</td>
<td>RSASSA-PSS [PKCS1]</td>
</tr>
<tr>
<td>Verwendung des Signaturalgorithmus</td>
<td>6</td>
<td>Owner Signing</td>
</tr>
<tr>
<td>Hashalgorithmus, kodiert</td>
<td>6</td>
<td>SHA-256 / SHA-256 [SHA-256]</td>
</tr>
<tr>
<td>Verschlüsselungsalgorithmus, kodiert</td>
<td>13</td>
<td>2-Key-Triple-DES</td>
</tr>
<tr>
<td>Operationsmodus bei Verschlüsselung</td>
<td>2</td>
<td>CBC (0-Padding)</td>
</tr>
<tr>
<td>Schlüsselart</td>
<td>S V</td>
<td>Signierschlüssel Chiffrierschlüssel</td>
</tr>
<tr>
<td>Schlüssellänge</td>
<td>gemäß [DK Krypto]</td>
<td></td>
</tr>
<tr>
<td>Zertifikatstyp</td>
<td>1<br>2<br>3</td>
<td>ZKA UN/EDIFACT X.509</td>
</tr>
<tr>
<td>Zertifikatsinhalt</td>
<td>nicht spezifiziert</td>
<td></td>
</tr>
</table>


Im Rahmen des Paddingverfahrens RSASSA-PSS wird als ,,Mask Generation Func-
tion" MGF1 verwendet. Beim Signierschlüssel wird ein doppeltes Hashing durchge-
führt. Dies wird durch eine spezielle Ausprägung des ,,Hashalgorithmus, kodiert" ge-
kennzeichnet.

Als Salt-Länge (Länge des Initialwertes) ist die Länge des Hashwertes zu verwen-
den.


## . DDV-1

Als Sicherheitsmedium für das Kundensystem ist nur die ec-Karte mit Chip zugelas-
sen.


<table>
<tr>
<th>Parameter</th>
<th>Wert</th>
<th>Bedeutung/Anmerkung</th>
</tr>
<tr>
<td>Signaturalgorithmus, kodiert</td>
<td>1</td>
<td>DES</td>
</tr>
<tr>
<td>Operationsmodus bei Signatur</td>
<td>999</td>
<td>Retail-MAC</td>
</tr>
<tr>
<td>Verwendung des Signaturalgorithmus</td>
<td>6</td>
<td>Owner Signing</td>
</tr>
<tr>
<td>Hashalgorithmus, kodiert</td>
<td>999</td>
<td>RIPEMD-160</td>
</tr>
<tr>
<td>Verschlüsselungsalgorithmus, kodiert</td>
<td>13</td>
<td>2-Key-Triple-DES</td>
</tr>
<tr>
<td>Operationsmodus bei Verschlüsselung</td>
<td>2</td>
<td>CBC (0-Padding)</td>
</tr>
<tr>
<td>Schlüsselart</td>
<td>S V</td>
<td>Signierschlüssel Chiffrierschlüssel</td>
</tr>
<tr>
<td>Schlüssellänge</td>
<td>128 Bit</td>
<td></td>
</tr>
<tr>
<td>Zertifikatstyp</td>
<td>-</td>
<td>nicht zulässig</td>
</tr>
<tr>
<td>Zertifikatsinhalt</td>
<td>-</td>
<td>nicht zulässig</td>
</tr>
<tr>
<td>Kapitel: B</td>
<td>Version: 3.0 - Final Version</td>
<td>Financial Transaction Services (FinTS) Dokument: Security - Sicherheitsverfahren HBCI</td>
</tr>
<tr>
<td>Seite: 14</td>
<td>Stand: 18.07.2013</td>
<td>Kapitel: Verfahrensbeschreibung<br>Abschnitt: Allgemeines</td>
</tr>
</table>


## B.1.1.1 Sicherheitsprofile im Secoder-Applikationsmodus

Für den Einsatz der folgenden Sicherheitsprofle ist als Chipkartenleser ein Secoder
mindestens in Version 2.1 Voraussetzung.


## RAH-7 im Secoder-Applikationsmodus

Als Sicherheitsmedium für das Kundensystem ist nur die Bankensignaturkarte oder
eine gleichwertige Signaturkarte zugelassen. Als Chipkartenleser ist ein Secoder ab
Version 2.1 zu verwenden. Im Applikationsmodus des Secoders haben Signaturen
z. B. bei Sicherheitsfunktion 811 folgenden Aufbau:


<table>
<tr>
<th>Parameter</th>
<th>Wert</th>
<th>Bedeutung</th>
</tr>
<tr>
<td>Signaturalgorithmus, kodiert</td>
<td>10</td>
<td>RSA</td>
</tr>
<tr>
<td>Operationsmodus bei Signatur</td>
<td>19</td>
<td>Signier- und Signaturschlüs- sel - RSASSA- PSS [PKCS1]</td>
</tr>
<tr>
<td>Verwendung des Signaturalgorithmus</td>
<td>6</td>
<td>Owner Signing</td>
</tr>
<tr>
<td>Hashalgorithmus, kodiert</td>
<td>6<br>3</td>
<td>Signierschlüssel - SHA-256 / SHA-256 [SHA-256] Signaturschlüssel - SHA- 256 [SHA-256]</td>
</tr>
<tr>
<td>Verschlüsselungsalgorithmus, kodiert</td>
<td>14</td>
<td>AES-256 [AES]</td>
</tr>
<tr>
<td>Operationsmodus bei Verschlüsselung</td>
<td>18</td>
<td>RSAES-PKCS1-v1 5 [PKCS1]</td>
</tr>
<tr>
<td>Schlüsselart</td>
<td>S<br>S|V|D|</td>
<td>Signierschlüssel Chiffrierschlüssel Schlüssel für Digitale Signa- turen</td>
</tr>
<tr>
<td>Schlüssellänge</td>
<td>gemäß [DK Krypto]</td>
<td></td>
</tr>
<tr>
<td>Zertifikatstyp</td>
<td>3</td>
<td>X.509</td>
</tr>
<tr>
<td>Zertifikatsinhalt</td>
<td>EF X509.CH.DS</td>
<td>fortgeschritten oder qualifi- ziert abh. von der Sicher- heitsklasse</td>
</tr>
</table>


Im Rahmen des Paddingverfahrens RSASSA-PSS wird als ,,Mask Generation Func-
tion" MGF1 verwendet. Beim Signierschlüssel wird ein doppeltes Hashing (Software
und Bankensignaturkarte) durchgeführt. Dies wird durch eine spezielle Ausprägung
des ,,Hashalgorithmus, kodiert" gekennzeichnet.

Als Salt-Länge (Länge des Initialwertes) ist die Länge des Hashwertes zu verwen-
den. Diese Festlegung ist z. B. auch Bestandteil der SECCOS 6 Spezifikation.

<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th rowspan="2">Version: 3.0 - Final Version</th>
<th rowspan="2">Kapitel: B</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Security - Sicherheitsverfahren HBCI</td>
</tr>
<tr>
<td>Kapitel:</td>
<td>Verfahrensbeschreibung</td>
<td>Stand:</td>
<td>Seite:</td>
</tr>
<tr>
<td>Abschnitt:</td>
<td>Allgemeines</td>
<td>18.07.2013</td>
<td>15</td>
</tr>
</table>


## RAH-9 im Secoder-Applikationsmodus

Als Sicherheitsmedium für das Kundensystem ist nur die Bankensignaturkarte oder
eine gleichwertige Signaturkarte zugelassen. Als Chipkartenleser ist ein Secoder ab
Version 2.1 zu verwenden. Im Applikationsmodus des Secoders haben Signaturen
z. B. bei Sicherheitsfunktion 811 folgenden Aufbau:


<table>
<tr>
<th>Parameter</th>
<th>Wert</th>
<th>Bedeutung/Anmerkung</th>
</tr>
<tr>
<td>Signaturalgorithmus, kodiert</td>
<td>10</td>
<td>RSA</td>
</tr>
<tr>
<td>Operationsmodus bei Signatur</td>
<td>19</td>
<td>RSASSA-PSS [PKCS1]</td>
</tr>
<tr>
<td>Verwendung des Signaturalgorithmus</td>
<td>6</td>
<td>Owner Signing</td>
</tr>
<tr>
<td>Hashalgorithmus, kodiert</td>
<td>6</td>
<td>SHA-256 / SHA-256 [SHA-256]</td>
</tr>
<tr>
<td>Verschlüsselungsalgorithmus, kodiert</td>
<td>14</td>
<td>AES-256 [AES]</td>
</tr>
<tr>
<td>Operationsmodus bei Verschlüsselung</td>
<td>18</td>
<td>RSAES-PKCS1-v1 5 [PKCS1]</td>
</tr>
<tr>
<td>Schlüsselart</td>
<td>V S</td>
<td>Signierschlüssel Chiffrierschlüssel</td>
</tr>
<tr>
<td>Schlüssellänge</td>
<td>gemäß [DK Krypto]</td>
<td></td>
</tr>
<tr>
<td>Zertifikatstyp</td>
<td></td>
<td>ohne</td>
</tr>
<tr>
<td>Zertifikatsinhalt</td>
<td>nicht spezifiziert</td>
<td></td>
</tr>
</table>


Im Rahmen des Paddingverfahrens RSASSA-PSS wird als ,,Mask Generation Func-
tion" MGF1 verwendet. Beim Signierschlüssel wird ein doppeltes Hashing (Software
und Bankensignaturkarte) durchgeführt. Dies wird durch eine spezielle Ausprägung
des ,,Hashalgorithmus, kodiert“ gekennzeichnet.

Als Salt-Länge (Länge des Initialwertes) ist die Länge des Hashwertes zu verwen-
den. Diese Festlegung ist z. B. auch Bestandteil der SECCOS 6 Spezifikation.


## B.1.2 Sicherheitsklassen

Die Sicherheitsklasse gibt für jede Signatur den erforderlichen Sicherheitsdienst an.
Als Sicherheitsdienst gelten derzeit „Authentikation“ und ,Non-Repudiation“.

Der Sicherheitsdienst ,,Authentikation“ erfordert die Signatur mit der Schlüsselart „S“
(Schlüssel auf Kundenseite: SK.CH.AUT c/s). Der Sicherheitsdienst „Non-Repudi-
ation" erfordert die Signatur mit der Schlüsselart „D“ (Schlüssel auf Kundenseite:
SK.CH.DS).

Derzeit sind folgende Sicherheitsklassen zulässig:

<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: B</td>
<td>Version: 3.0 - Final Version</td>
<td>Financial Transaction Services (FinTS) Dokument: Security - Sicherheitsverfahren HBCI</td>
</tr>
<tr>
<td>Seite:</td>
<td rowspan="2">Stand: 18.07.2013</td>
<td>Kapitel: Verfahrensbeschreibung</td>
</tr>
<tr>
<td>16</td>
<td>Abschnitt: Allgemeines</td>
</tr>
</table>


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
<td>Sicherheitsdienst ,,Authentikation" mit fortgeschrittener elektronischer Signatur ge- mäß §2, SigG und optionaler Zertifikatsprüfung unter Verwendung des S-Schlüssels (Schlüssel Sk.CH.AUT c/s)</td>
</tr>
<tr>
<td>3</td>
<td>Sicherheitsdienst ,,Non-Repudiation" mit fortgeschrittener elektronischer Signatur gemäß §2, SigG und optionaler Zertifikatsprüfung unter Verwendung des DS- Schlüssels (SK.CH.DS)</td>
</tr>
<tr>
<td>4</td>
<td>Sicherheitsdienst ,,Non-Repudiation" mit fortgeschrittener bzw. qualifizierter elektro- nischer Signatur gemäß §2, SigG und zwingender Zertifikatsprüfung unter Verwen- dung des DS-Schlüssels (SK.CH.DS)</td>
</tr>
</table>


Zu einem späteren Zeitpunkt kann die Notwendigkeit einer weiteren Sicherheits-
klasse überprüft werden, die qualifizierte Signaturen mit zwingender Zertifikatsprü-
fung erfordert.

Folgende Zuordnungen von Sicherheitsklassen auf Sicherheitsprofile sind möglich:


<table>
<tr>
<td>Sicherheitsprofil</td>
<td>Sicherheitsklasse(n)</td>
</tr>
<tr>
<td>DDV</td>
<td>1</td>
</tr>
<tr>
<td>RAH-7</td>
<td>1, 2, 3, 4</td>
</tr>
<tr>
<td>RAH-9</td>
<td>1,2</td>
</tr>
<tr>
<td>RAH-10</td>
<td>1</td>
</tr>
<tr>
<td>RDH-1</td>
<td>1</td>
</tr>
<tr>
<td>RDH-2</td>
<td>1</td>
</tr>
<tr>
<td>RDH-3</td>
<td>1, 2, 3, 4</td>
</tr>
<tr>
<td>RDH-5</td>
<td>1,2</td>
</tr>
<tr>
<td>RDH-6</td>
<td>1, 2, 3, 4</td>
</tr>
<tr>
<td>RDH-7</td>
<td>1, 2, 3, 4</td>
</tr>
<tr>
<td>RDH-8</td>
<td>1,2</td>
</tr>
<tr>
<td>RDH-9</td>
<td>1,2</td>
</tr>
<tr>
<td>RDH-10</td>
<td>1</td>
</tr>
</table>


Die Sicherheitsklasse gibt für jeden Geschäftsvorfall den erforderlichen Sicherheits-
dienst an. Signaturen gemäß der Sicherheitsklasse 2 und höher entsprechen den
Anforderungen des Signaturgesetzes und erlauben damit rechtsverbindliche Wil-
lenserklärungen unter der Voraussetzung, dass die außerhalb des HBCI-Protokolls
liegenden Anforderungen (z.B. Anforderungen an die Zertifizierungsinfrastruktur und
an die Endgeräte) ebenfalls erfüllt sind.

<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th>Version:</th>
<th>Kapitel:</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Security - Sicherheitsverfahren HBCI</td>
<td>3.0 - Final Version</td>
<td>B</td>
</tr>
<tr>
<td>Kapitel:</td>
<td>Verfahrensbeschreibung</td>
<td>Stand:</td>
<td>Seite:</td>
</tr>
<tr>
<td>Abschnitt:</td>
<td>Allgemeines</td>
<td>18.07.2013</td>
<td>17</td>
</tr>
</table>


Jede Signatur, die im Rahmen von HBCI generiert wird, muss der festgelegten Si-
cherheitsklasse entsprechen:

. Technische Signaturen (Dialoginitialisierung, Dialogendenachricht) erfolgen ge-
nerell mit Sicherheitsklasse 1 (Authentikation)

• Bei Geschäftsvorfällen kann das Kreditinstitut die Sicherheitsklasse individuell
festlegen (Die Sicherheitsklasse wird dem Kunden in den Bankparameterdaten
des betreffenden Geschäftsvorfalls mitgeteilt)


### Hinweis:

Sicherheitsklassen werden nur in Verbindung mit dem Sicherheitsverfahren HBCI
benutzt. Unterstützt ein Kreditinstitut ausschlieBlich das PIN/TAN-Verfahren, so ist
in das DE ,Sicherheitsklasse' des jeweiligen Geschäftsvorfallparametersegmentes
als Füllwert ,0' einzustellen. Die Sicherheitsklasse hat bei PIN/TAN für die Verarbei-
tung keine Bedeutung und darf vom Kundenprodukt für PIN/TAN nicht ausgewertet
werden. Stattdessen sind bei PIN/TAN die Informationen aus HIPINS für die Festle-
gung benötigter Sicherheitsmerkmale zu verwenden.

<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: B</td>
<td>Version: 3.0 - Final Version</td>
<td>Financial Transaction Services (FinTS) Dokument: Security - Sicherheitsverfahren HBCI</td>
</tr>
<tr>
<td>Seite:<br>18</td>
<td>Stand: 18.07.2013</td>
<td>Kapitel: Verfahrensbeschreibung<br>Abschnitt: Mechanismen</td>
</tr>
</table>


## B.2 Mechanismen


### B.2.1 Elektronische Signatur

Die Bildung der elektronischen Signatur erfolgt durch die Vorgänge

. Bildung des Hashwerts

• Ergänzen des Hashwerts auf eine vorgegebene Länge und

. Berechnung der elektronischen Signatur über den Hashwert.

Je nach Sicherheitsverfahren sind die Verarbeitungsschritte jeweils verschieden.


### B.2.1.1 Hashing

Als Hash-Funktion können im Rahmen von HBCI abhängig vom Sicherheitsprofil
entweder RIPEMD-160 [RIPEMD], SHA-1 [SHA-1] oder SHA-256 [SHA-256] einge-
setzt werden.


## . RIPEMD-160

Der Hash-Algorithmus RIPEMD-160 bildet Eingabe-Bitfolgen beliebiger Länge auf
einen als Bytefolge dargestellten Hash-Wert von 20 Byte (160 Bit) Länge ab. Teil
des Hash-Algorithmus ist das Padding von Eingabe-Bitfolgen auf ein Vielfaches von
64 Byte. Das Padding erfolgt auch dann, wenn die Eingabe-Bitfolge bereits eine
Länge hat, die ein Vielfaches von 64 Byte ist. RIPEMD-160 verarbeitet die Eingabe-
Bitfolgen in Blöcken von 64 Byte Länge.

Als Initialisierungsvektor dient die binäre Zeichenfolge X'01 23 45 67 89 AB CD EF
FE DC BA 98 76 54 32 10 F0 E1 D2 C3'5.

◆ SHA-1

Der Hash-Algorithmus SHA-1 bildet Eingabe-Bitfolgen beliebiger Länge auf Bytefol-
gen von 20 Byte Länge ab. Teil des Hash-Algorithmus ist das Padding von Eingabe-
Bitfolgen auf ein Vielfaches von 64 Byte. Das Padding erfolgt auch dann, wenn die
Eingabe-Bitfolge bereits eine Länge hat, die ein Vielfaches von 64 Byte ist. SHA-1
verarbeitet die Eingabe-Bitfolgen in Blöcken von 64 Byte Länge.


## . SHA-256

Der Hash-Algorithmus SHA-256 bildet Eingabe-Bitfolgen beliebiger Länge auf Byte-
folgen von 32 Byte Länge ab. Teil des Hash-Algorithmus ist das Padding von Ein-
gabe-Bitfolgen auf ein Vielfaches von 64 Byte. Das Padding erfolgt auch dann,
wenn die Eingabe-Bitfolge bereits eine Länge hat, die ein Vielfaches von 64 Byte ist.
SHA-256 verarbeitet die Eingabe-Bitfolgen in Blöcken von 64 Byte Länge.


### B.2.1.2 Elektronische Signatur bei DDV (DES-basierend)


#### 1. Hashing der Nachricht

Als Hash-Funktion kann, anhängig vom Sicherheitsprofil RIPEMD-160 oder
SHA-256 eingesetzt werden.

<!-- PageFooter: 5 Little-Endian-Notation -->
<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th>Version:</th>
<th>Kapitel:</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Security - Sicherheitsverfahren HBCI</td>
<td>3.0 - Final Version</td>
<td>B</td>
</tr>
<tr>
<td>Kapitel:</td>
<td>Verfahrensbeschreibung</td>
<td>Stand:</td>
<td>Seite:</td>
</tr>
<tr>
<td>Abschnitt:</td>
<td>Mechanismen</td>
<td>18.07.2013</td>
<td>19</td>
</tr>
</table>


## 2. Formatierung des Hashwerts


### Formatierung des Hashwerts bei RIPEMD-160

Das Padding ist je nach Typ der eingesetzten Chipkarte (Typ 0 oder Typ 1)
unterschiedlich:

Bei Typ 0-Karten erfolgt das Padding entsprechend der folgenden Abbildung
mit X'00' auf das nächste Vielfache von 8 Byte:

Byte-Position:

Padding


<table>
<tr>
<th>24</th>
<th>21</th>
<th>20<br>...<br>1</th>
</tr>
<tr>
<td>00</td>
<td>00 00 00</td>
<td>Hashwert</td>
</tr>
</table>


Bei Typ 1-Karten erfolgt das Padding entsprechend der folgenden Abbildung
auf das nächste Vielfache von 8 Byte: Sei der Hashwert = HashL | HashR,
wobei HashL die linken 8 Byte und HashR die rechten 12 Byte des Hashwerts
bezeichnet.

Byte-Position:

Padding


<table>
<tr>
<td>24 23</td>
<td>22 ... 11</td>
<td>10 9</td>
<td>8 ... 1</td>
</tr>
<tr>
<td>00 80</td>
<td>HashR</td>
<td>0C 81</td>
<td>HashL</td>
</tr>
</table>


Ob eine Karte vom Typ 0 oder Typ 1 vorliegt, kann anhand der Länge der
Kartenidentifikationsdaten (CID) ermittelt werden. Für Typ 0-Karten hat die
CID eine Länge von 22 Byte, für Typ 1-Karten mindestens eine Länge von
24 Byte.


### Formatierung des Hashwerts bei SHA-256

Da der Hashwert bei SHA-256 mit 32 Byte bereits ein Vielfaches von 8 dar-
stellt, muss bei diesem Verfahren kein Padding stattfinden.


## 3. Berechnung der elektronischen Signatur

Als Signatur wird ein Retail CBC-MAC gemäß ANSI X9.19 gebildet. Hierzu
wird der gepaddete Hashwert zunächst in 3 Blöcke der Länge 8 Byte aufge-
teilt. Als Zwischenresultat wird ein einfacher CBC-MAC über die ersten 2
Blöcke berechnet. Als Initialisierungsvektor kommt X'00 00 00 00 00 00 00
00' zum Einsatz. Dabei verwendet man als Schlüssel die linke Hälfte des
Signierschlüssels. Anschließend erfolgt eine 2-Key-Triple-DES-Verschlüsse-
lung mit dem Signierschlüssel des Kunden (muss beim Kreditinstitut herge-
leitet werden) über die XOR-Summe des Zwischenergebnisses mit dem letz-
ten Nachrichtenblock. Der so erhaltene 8 Byte(=64 bit)-Ausgabeblock ist der
Retail CBC-MAC.


### B.2.1.3 Elektronische Signatur bei RAH und RDH (RSA-basierend)


#### 1. Hashing der Nachricht

Als Hash-Funktion kann abhängig vom Sicherheitsprofil entweder RIPEMD-
160, SHA-1 oder SHA-256 eingesetzt werden.


#### 2. Formatierung des Hashwerts

Die Formatierung des Hashwerts erfolgt auf folgende Art und Weise:

<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: B</td>
<td>Version: 3.0 - Final Version</td>
<td>Financial Transaction Services (FinTS) Dokument: Security - Sicherheitsverfahren HBCI</td>
</tr>
<tr>
<td>Seite:<br>20</td>
<td>Stand: 18.07.2013</td>
<td>Kapitel: Verfahrensbeschreibung<br>Abschnitt:<br>Mechanismen</td>
</tr>
</table>


ISO 9796-2

RDH-2, RDH-3 und RDH-5

PKCS#1 V1.5

RDH-3, RDH-6 und RDH-8

PKCS#1 PSS

RAH-7, RAH-9 und RAH-10,
RDH-7, RDH-9 und RDH-10

ISO 9796:1991
(Kap. 5.1 - 5.4)

Übergangsweise für das Altverfahren RDH-1, wobei
der Hashwert wird für die nachfolgende Signaturbil-
dung als Langzahl6 interpretiert (s. auch die Beispiele
in der Anlage zu ISO 9796:1991).


#### 3. Berechnung der elektronischen Signatur

Der Hashwert wird mittels RSA entweder gemäß DIN/ISO 9796-2 (bei RDH-
2, RDH-3 und RDH-5), gemäß PKCS#1 V1.5 (bei RDH-6 und RDH-8) oder
gemäß PKCS#1 PSS (bei RAH-7, RAH-9 und RAH-10 bzw. RDH-7, RDH-9
und RDH-10) signiert. Übergangsweise ist für das Altverfahren RDH-1 auch
die Signatur gemäß ISO 9796-1 zulässig.7

<!-- PageFooter: 6 Unter Langzahl wird dabei die kanonische Darstellung einer natürlichen Zahl in einem Feld [0..n] bezeichnet, wobei die Wertigkeit der Felder von 0 bis n abnimmt. -->
<!-- PageFooter: 7 Im Falle von ISO 9796-1 sind auch die dort in den Anhängen A.4 ,,Signature function" und A.5 ,,Veri- fication function" beschriebenen Operationen durchzuführen und die Anhänge B und C zu berück- sichtigen. -->
<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th>Version:</th>
<th rowspan="2">Kapitel: B</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Security - Sicherheitsverfahren HBCI</td>
<td>3.0 - Final Version</td>
</tr>
<tr>
<td>Kapitel:</td>
<td>Verfahrensbeschreibung</td>
<td>Stand:</td>
<td>Seite:</td>
</tr>
<tr>
<td>Abschnitt:</td>
<td>Mechanismen</td>
<td>18.07.2013</td>
<td>21</td>
</tr>
</table>


##### B.2.2 Verschlüsselung

Bei der Verschlüsselung wird für jede Nachricht ein separater Nachrichtenschlüssel
verwendet. Die Verschlüsselung der HBCI-Nutzdaten erfolgt folgendermaßen:

. Bei RAH-7, RAH-9 und RAH-10

Die Verschlüsselung erfolgt mittels AES-256 gemaß [AES]. Der Nachrichten-
schlüssel wird mittels RSA (RAH) chiffriert und mit der verschlüsselten Nachricht
mitgeliefert.

. Sonst:

Die Verschlüsselung erfolgt mittels 2-Key-Triple-DES gemäß ANSI X3.92. Der
Nachrichtenschlüssel wird entweder mittels 2-Key-Triple-DES (DDV) oder RSA
(RDH) chiffriert und mit der verschlüsselten Nachricht mitgeliefert.


![](figures/35.1)


Der Nachrichtenschlüssel muss für jede Nachricht eines Dialoges
individuell verschieden sein. Dies muss gewährleistet werden, in-
dem das sendende System den Nachrichtenschlüssel dynamisch
generiert.


![](figures/35.2)


Sollte bei der Verarbeitung des Nachrichtenschlüssels, insbesonde-
re beim Padding ein Fehler auftreten, so sind außer dem negativen
Prüfergebnis selbst keine weiteren Details an die aufrufende Funkti-
on zurückzugeben, um keine Rückschlüsse über die Art des Fehlers
und damit ggf. auf den Schlüssel selbst zu geben.


###### B.2.2.1 Verschlüsselung bei RAH-7, RAH-9 und RAH-10:

Die Verschlüsselung und Entschlüsselung erfolgt bei den RAH-Verfahren in den fol-
genden drei Schritten:

1\. Der Sender erzeugt eine Zufallszahl als Nachrichtenschlüssel.

2\. Dieser Nachrichtenschlüssel wird verwendet, um die Daten mittels AES im CBC
Modus gemäß ISO 10116 (ANSI X3.106) zu verschlüsseln (vgl. Abbildung 1).
Das Padding der Nachricht erfolgt gemäß den Vorgaben des Kryptokatalogs der
Deutschen Kreditwirtschaft (vgl. [DK Krypto], Kapitel 4.3.1) (vgl.Abbildung 2 und
Abbildung 3).

<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: B</td>
<td>Version: 3.0 - Final Version</td>
<td>Financial Transaction Services (FinTS) Dokument: Security - Sicherheitsverfahren HBCI</td>
</tr>
<tr>
<td>Seite:<br>22</td>
<td>Stand: 18.07.2013</td>
<td>Kapitel: Verfahrensbeschreibung<br>Abschnitt: Mechanismen</td>
</tr>
</table>


###### ZKA-Padding" (vgl. [DK Krypto], Kapitel 4.3.1 auf S. 20):

Für die Verarbeitung von Daten durch einen kryptographischen Algorithmus kann deren Dar-
stellung als Folge von Byte-Blocken mit einer vorgegebenen Länge L erforderlich sein. Das
ZKA-Padding ist eine Methode zur Formatierung des letzten, möglicherweise unvollständi-
gen Datenblocks auf die Länge von L Byte. Die den Daten zugehörigen Bytes können ein-
deutig von den durch das Padding hinzugefügten Bytes unterschieden werden.

An die Daten M wird zunächst das Byte '80' angehängt. Falls M || '80' nun eine Byte-Länge
besitzt, die kein Vielfaches von L ist, werden weitere Bytes '00' angehängt, bis das Ergebnis
der Operation eine Byte-Länge besitzt, die ein Vielfaches von L ist.

ZKA-Padding (M) = M || '80' || '00' ||...|| '00'

Verkettung bis zur
Gesamtlänge der Byte-Folge
als Vielfaches von L Byte
(hier: AES-Blocklänge = 16 Byte)


Abbildung 1: Nachrichtenverschlüsselung mit AES im CBC-Mode für RAH-Verfahren

![Klartextblock 1 Klartextblock 2 Klartextblock n ZKA-Padding + + + Initialisierungsvektor=0 Schlüssel verschlüsseln AES Schlüssel verschlüsseln AES Schlüssel verschlüsseln AES 127 0 127 0 127 0 verschlüsselter Textblock 1 verschlüsselter Textblock 2 verschlüsselter Textblock n](figures/36.1)


3\. Der aktuelle Nachrichtenschlüssel wird mit dem öffentlichen Schlüssel des Emp-
fängers chiffriert. Da die Länge des Nachrichtenschlüssels bei AES nur 32 Byte,
d.h. 256 Bit beträgt, muss er auf die Moduluslänge des verwendeten öffentlichen
Chiffrierschlüssels ergänzt werden. Das Padding wird abhängig vom Sicherheits-
profil auf unterschiedliche Art und Weise vorgenommen, wie in den folgenden
Abbildungen gezeigt.

<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th>Version:</th>
<th rowspan="2">Kapitel: B</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Security - Sicherheitsverfahren HBCI</td>
<td>3.0 - Final Version</td>
</tr>
<tr>
<td>Kapitel:</td>
<td>Verfahrensbeschreibung</td>
<td>Stand:</td>
<td>Seite:</td>
</tr>
<tr>
<td>Abschnitt:</td>
<td>Mechanismen</td>
<td>18.07.2013</td>
<td>23</td>
</tr>
</table>


Abbildung 2: Verschlüsselung bei RAH-7 und RAH-9

![255 0 Zufallszahl = Nachrichtenschlüssel FinTS-Nachricht (Klartext) ZKA-Padding Initialisierungsvektor=0 1535<=n<=\\[DK Krypto\\]-1 0 Padn(Nachrichtenschlüssel) Pad=PKCS#1 AES CBC Mode RSA 1535<=n<=\\[DK Krypto\\]-1 Chiffrierschlüssel* 0 * Öffentlicher Chiffrierschlüssel des Partners 1535<=n<=\\[DK Krypto\\]-1 0 Nachrichtenschlüssel (chiffriert) FinTS-Nachricht (chiffriert) \\[DK Krypto\\]: In \\[DK Krypto\\] empfohlene maximale Schlüssellänge](figures/37.1)


Abbildung 3: Verschlüsselung bei RAH-10

![255 0 Zufallszahl = Nachrichtenschlüssel FinTS-Nachricht (Klartext) ZKA-Padding Initialisierungsvektor=0 1535<=n<=\\[DK Krypto\\]-1 0 Padn(Nachrichtenschlüssel) Pad=Zero AES CBC Mode RSA 1535<=n<=\\[DK Krypto\\]-1 0 Chiffrierschlüssel* * Öffentlicher Chiffrierschlüssel des Partners 1535<=n<=\\[DK Krypto\\]-1 0 Nachrichtenschlüssel (chiffriert) FinTS-Nachricht (chiffriert) \\[DK Krypto\\]: In \\[DK Krypto\\] empfohlene maximale Schlüssellänge](figures/37.2)


<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: B</td>
<td>Version: 3.0 - Final Version</td>
<td>Financial Transaction Services (FinTS) Dokument: Security - Sicherheitsverfahren HBCI</td>
</tr>
<tr>
<td>Seite: 24</td>
<td>Stand: 18.07.2013</td>
<td>Kapitel: Verfahrensbeschreibung<br>Abschnitt: Mechanismen</td>
</tr>
</table>


####### B.2.2.2 Verschlüsselung bei RDH und DDV:

Die ersten zwei Schritte sind für die beiden Verfahren RDH und DDV identisch:

1\. Der Sender erzeugt eine Zufallszahl als Nachrichtenschlüssel und stellt ungerade
Parität sicher. Bei der Auswahl der Zufallszahl ist darauf zu achten, dass keiner
der folgenden schwachen oder halbschwachen Schlüssel9 gewählt wird (vgl. Ka-
pitel B.3.1.1).

Die schwachen Schlüssel des DES-Algorithmus:

X'01 01 01 01 01 01 01 01'
X' FE FE FE FE FE FE FE FE'
X' 1F 1F 1F 1F 0E 0E OE OE'
X'EO EO EO E0 F1 F1 F1 F1'

Die halbschwachen Schlüssel des DES-Algorithmus:

X' 01 FE 01 FE 01 FE 01 FE'
X' FE 01 FE 01 FE 01 FE 01'
X' 1F E0 1F E0 OE F1 0E F1'
X'E0 1F E0 1F F1 0E F1 0E'
X' 01 E0 01 E0 01 F1 01 F1'
X'E0 01 E0 01 F1 01 F1 01'
X' 1F FE 1F FE OE FE OE FE'
X'FE 1F FE 1F FE 0E FE OE'
X'01 1F 01 1F 01 0E 01 0E'
X' 1F 01 1F 01 0E 01 0E 01'
X'EO FE EO FE F1 FE F1 FE'
X'FE E0 FE E0 FE F1 FE F1'

2\. Dieser Nachrichtenschlüssel wird verwendet, um die Daten mittels 2-Key-Triple-
DES im CBC Modus gemäß ISO 10116 (ANSI X3.106) zu verschlüsseln (vgl.
Abbildung 4). Das Padding der Nachricht erfolgt oktettorientiert gemäß ISO
10126 (ANSI X9.23), der Initialisierungsvektor ist X'00 00 00 00 00 00 00 00' (vgl.
Abbildung 5 und Abbildung 6).

<!-- PageFooter: 9 Die schwachen und halbschwachen Schlüssel entsprechen denen des DFÜ-Abkommens. -->
<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th>Version:</th>
<th>Kapitel:</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Security - Sicherheitsverfahren HBCI</td>
<td>3.0 - Final Version</td>
<td>B</td>
</tr>
<tr>
<td>Kapitel:</td>
<td>Verfahrensbeschreibung</td>
<td>Stand:</td>
<td>Seite:</td>
</tr>
<tr>
<td>Abschnitt:</td>
<td>Mechanismen</td>
<td>18.07.2013</td>
<td>25</td>
</tr>
</table>


Abbildung 4: Nachrichtenverschlüsselung generell mit 2-Key-Triple-DES im CBC-
Mode für RDH und DDV

![Klartextblock 1 Klartextblock 2 Klartextblock n + + + Schlüssel 1 verschlüsseln DES Schlüssel 1 verschlüsseln DES Schlüssel 1 verschlüsseln DES Initialisierungsvektor Schlüssel 2 entschlüsseln DES Schlüssel 2 entschlüsseln DES Schlüssel 2 entschlüsseln DES Schlüssel 1 verschlüsseln DES Schlüssel 1 verschlüsseln DES Schlüssel 1 verschlüsseln DES 63 0 63 0 63 0 verschlüsselter Textblock 1 verschlüsselter Textblock 2 verschlüsselter Textblock n Schlüssel 1: linke Schlüsselhälfte Schlüssel 2: rechte Schlüsselhälfte](figures/39.1)


Die weitere Verarbeitung ist bei DDV und RDH unterschiedlich:


####### B.2.2.2.1 Verschlüsselung bei DDV (DES-basierend)

3\. Der aktuelle Nachrichtenschlüssel für die Chiffrierung der Daten wird vom Kun-
denprodukt mit dem kundenindividuellen Chiffrierschlüssel der Chipkarte mittels
2-Key-Triple-DES im ECB-Mode (ISO 10116) verschlüsselt (vgl. Abbildung 5 und
Abbildung 6).

Aufgrund vorgegebener Verfahren bei der ZKA-Chipkarte wird zum Chiffrieren
und Dechiffrieren des Nachrichtenschlüssels, unabhängig von der Übertragungs-
richtung, kundensystemseitig immer die Routine ,Encrypt“ benutzt, kreditinstituts-
seitig immer die Routine „Decrypt" (vgl. Kapitel C.2.5.2).

<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: B</td>
<td>Version: 3.0 - Final Version</td>
<td>Financial Transaction Services (FinTS) Dokument: Security - Sicherheitsverfahren HBCI</td>
</tr>
<tr>
<td>Seite:<br>26</td>
<td>Stand:<br>18.07.2013</td>
<td>Kapitel: Verfahrensbeschreibung<br>Abschnitt:<br>Mechanismen</td>
</tr>
</table>


Abbildung 5: Verschlüsselung bei 2-Key-Triple-DES im DDV-Verfahren

![127 0 Zufallszahl = Nachrichtenschlüssel FinTS-Nachricht (Klartext) Padding nach ANSI X9.23 Initialisierungsvektor=0 3DES CBC Mode ECB Mode 3DES 127 0 Chiffrierschlüssel Kundensystem : Encrypt Kreditinstitut : Decrypt 127 0 Nachrichtenschlüssel (chiffriert) FinTS-Nachricht (chiffriert)](figures/40.1)


Abbildung 6: Entschlüsselung bei 2-Key-Triple-DES im DDV-Verfahren

![127 0 Nachrichtenschlüssel (chiffriert) FinTS-Nachricht (chiffriert) Padding nach ANSI X9.23 Initialisierungsvektor=0 ECB Mode 3DES 127 0 Chiffrierschlüssel Kundensystem : Encrypt Kreditinstitut : Decrypt 127 0 Nachrichtenschlüssel 3DES CBC Mode FinTS-Nachricht (Klartext)](figures/40.2)


<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th>Version:</th>
<th>Kapitel:</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Security - Sicherheitsverfahren HBCI</td>
<td>3.0 - Final Version</td>
<td>B</td>
</tr>
<tr>
<td>Kapitel:</td>
<td>Verfahrensbeschreibung</td>
<td>Stand:</td>
<td>Seite:</td>
</tr>
<tr>
<td>Abschnitt:</td>
<td>Mechanismen</td>
<td>18.07.2013</td>
<td>27</td>
</tr>
</table>


####### B.2.2.2.2 Verschlüsselung bei RDH (RSA-basierend)

3\. Der aktuelle Nachrichtenschlüssel wird mit dem öffentlichen Schlüssel des Emp-
fängers chiffriert. Da die Länge des Nachrichtenschlüssels nur 16 Byte, d.h. 128
Bit bei 2-Key-Triple-DES beträgt, muss er auf die Moduluslänge des verwende-
ten öffentlichen Chiffrierschlüssels ergänzt werden. Das Padding wird abhängig
vom Sicherheitsprofil auf unterschiedliche Art und Weise vorgenommen, wie in
den folgenden Abbildungen gezeigt.


Abbildung 7: Verschlüsselung bei 2-Key-Triple-DES im RDH-Verfahren

![127 0 Zufallszahl = Nachrichtenschlüssel FinTS-Nachricht (Klartext) Padding nach ANSI X9.23 Initialisierungsvektor=0 3DES CBC Mode RSA 127 0 Chiffrierschlüssel Kundensystem Kreditinstitut : Encrypt : Decrypt 127 0 Nachrichtenschlüssel (chiffriert) FinTS-Nachricht (chiffriert)](figures/41.1)


<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: B</td>
<td>Version: 3.0 - Final Version</td>
<td>Financial Transaction Services (FinTS) Dokument: Security - Sicherheitsverfahren HBCI</td>
</tr>
<tr>
<td>Seite:<br>28</td>
<td>Stand: 18.07.2013</td>
<td>Kapitel: Verfahrensbeschreibung<br>Abschnitt:<br>Mechanismen</td>
</tr>
</table>


Abbildung 8: Entschlüsselung bei 2-Key-Triple-DES im RDH-Verfahren

![127 0 Nachrichtenschlüssel (chiffriert) FinTS-Nachricht (chiffriert) Padding nach ANSI X9.23 Initialisierungsvektor=0 RSA 127 0 Chiffrierschlüssel Kundensystem Kreditinstitut : Encrypt : Decrypt 127 0 Nachrichtenschlüssel 3DES CBC Mode FinTS-Nachricht (Klartext)](figures/42.1)


Abbildung 9: Verschlüsselung bei RDH-1

![127 0 Zufallszahl = Nachrichtenschlüssel FinTS-Nachricht (Klartext) Padding nach ANSI X9.23 Initialisierungsvektor=0 767 127 0 00..00 Nachrichtenschlüssel Padding >707 0 3DES CBC Mode Chiffrierschlüssel* RSA 767 >707 0 00..00 Chiffrierschlüssel* Padding * Öffentlicher Chiffrierschlüssel des Partners 767 0 Nachrichtenschlüssel (chiffriert) FinTS-Nachricht (chiffriert)](figures/42.2)


<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th>Version:</th>
<th>Kapitel:</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Security - Sicherheitsverfahren HBCI</td>
<td>3.0 - Final Version</td>
<td>B</td>
</tr>
<tr>
<td>Kapitel:</td>
<td>Verfahrensbeschreibung</td>
<td>Stand:</td>
<td>Seite:</td>
</tr>
<tr>
<td>Abschnitt:</td>
<td>Mechanismen</td>
<td>18.07.2013</td>
<td>29</td>
</tr>
</table>


Abbildung 10: Verschlüsselung bei RDH-3 und RDH-5

![127 0 Zufallszahl = Nachrichtenschlüssel FinTS-Nachricht (Klartext) Padding nach ANSI X9.23 Initialisierungsvektor=0 1023<=n<=2047 0 Padn(Nachrichtenschlüssel) Pad=PKCS#1 3DES CBC Mode RSA 1023<=n<=2047 0 Chiffrierschlüssel* * Öffentlicher Chiffrierschlüssel des Partners 1023<=n<=2047 0 Nachrichtenschlüssel (chiffriert) FinTS-Nachricht (chiffriert)](figures/43.1)


Abbildung 11: Verschlüsselung bei RDH-6 bis RDH-9

![127 0 Zufallszahl = Nachrichtenschlüssel FinTS-Nachricht (Klartext) Padding nach ANSI X9.23 Initialisierungsvektor=0 1535<=n<=\\[DK Krypto\\]-1 0 Padn(Nachrichtenschlüssel) Pad=PKCS#1 3DES CBC Mode RSA 1535<=n<=\\[DK Krypto\\]-1 0 Chiffrierschlüssel* * Öffentlicher Chiffrierschlüssel des Partners 1535<=n<=\\[DK Krypto\\]-1 0 Nachrichtenschlüssel (chiffriert) FinTS-Nachricht (chiffriert) \\[DK Krypto\\]: In \\[DK Krypto\\] empfohlene maximale Schlüssellänge](figures/43.2)


<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: B</td>
<td>Version: 3.0 - Final Version</td>
<td>Financial Transaction Services (FinTS) Dokument: Security - Sicherheitsverfahren HBCI</td>
</tr>
<tr>
<td>Seite:<br>30</td>
<td>Stand: 18.07.2013</td>
<td>Kapitel: Verfahrensbeschreibung<br>Abschnitt:<br>Mechanismen</td>
</tr>
</table>


Abbildung 12: Verschlüsselung bei RDH-10

![127 0 Zufallszahl = Nachrichtenschlüssel FinTS-Nachricht (Klartext) Padding nach ANSI X9.23 Initialisierungsvektor=0 1535<=n<=4095 0 Padn(Nachrichtenschlüssel) Pad=Zero 3DES CBC Mode RSA 1535<=n<=4095 0 Chiffrierschlüssel* * Öffentlicher Chiffrierschlüssel des Partners 1535<=n<=4095 0 Nachrichtenschlüssel (chiffriert) FinTS-Nachricht (chiffriert)](figures/44.1)


##### B.2.3 Sicherheitsmedien beim Kundenprodukt

Bei Verwendung des symmetrischen Verfahrens (DDV) muss eine vom Kreditinstitut
ausgegebene ZKA-Chipkarte eingesetzt werden, welche die Berechnung der kryp-
tographischen Funktionen so durchführt, dass die kartenindividuellen Schlüssel
niemals die Chipkarte verlassen.

Werden asymmetrische Verfahren (RAH oder RDH) eingesetzt, so kann als Sicher-
heitsmedium eine vom Kreditinstitut ausgegebene RSA-Chipkarte oder eine Schlüs-
seldatei dienen.10 Falls eine Chipkarte zum Einsatz kommen soll, wird die in Kap.
C.1 beschriebene Bankensignaturkarte empfohlen. Auf dem Sicherheitsmedium
wird unter anderem der private Schlüssel des Kunden gespeichert. Es ist aber auch
möglich, öffentliche Schlüssel des Kreditinstitutes darauf abzulegen oder aber im
Falle einer Chipkarte die kryptographischen Operationen damit durchzuführen. Bei
Einsatz einer RSA-Chipkarte müssen die geheimen Daten (z.B. private Schlüssel,
Passworte) gegen unberechtigtes Auslesen geschützt sein.


![](figures/44.2)


Es ist zwingend erforderlich, die Daten auf dem Sicherheitsmedium
(kryptographisch) zu schützen. Speziell ist im Rahmen der Speiche-
rung der Schlüsselpaare in der Schlüsseldatei sicherzustellen, dass
die Daten unter Einbeziehung eines Passwortes (Banking-PIN o.ä.)
verschlüsselt werden und der Zugriff auf die verschlüsselten Daten
nur über die manuelle Eingabe des entsprechenden Passwortes
möglich ist.

<!-- PageFooter: 10 Der Aufbau des Dateiformats ist bei Bedarf bei den auf [www.fints.org](http://www.fints.org/) in der Rubrik ,,Impressum" ge- listeten Adressen erhältlich. -->
<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th rowspan="2">Version: 3.0 - Final Version</th>
<th rowspan="2">Kapitel: B</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Security - Sicherheitsverfahren HBCI</td>
</tr>
<tr>
<td>Kapitel:</td>
<td>Verfahrensbeschreibung</td>
<td>Stand:</td>
<td>Seite:</td>
</tr>
<tr>
<td>Abschnitt:</td>
<td>Abläufe</td>
<td>18.07.2013</td>
<td>31</td>
</tr>
</table>


### B.3 Abläufe


#### B.3.1 Schlüsselverwaltung

Bei der Schlüsselverwaltung muss zwischen der Verwendung von symmetrischen
Schlüsseln für DDV und asymmetrischen Schlüsseln für RAH und RDH unterschie-
den werden.

Gemeinsam gültig sind hingegen für beide Verfahren die verwendeten Schlüsselar-
ten, Schlüsselnamen und die Generierung von Nachrichtenschlüsseln.


#### B.3.1.1 Gemeinsam verwendete Verfahren zur Schlüsselverwaltung


##### ◆ Schlüsselarten

Bei den Sicherheitsverfahren DDV-1, RAH-9, RAH-10, RDH-1, RDH-2, RDH-5,
RDH-8, RDH-9 und RDH-10 können Kunde und Kreditinstitut über zwei Schlüssel
bzw. Schlüsselpaare verfügen:

• einen Signierschlüssel bzw. -schlüsselpaar

• einen Chiffrierschlüssel bzw. -schlüsselpaar

Der Signierschlüssel wird zum Unterzeichnen von Transaktionen verwendet, wäh-
rend der Chiffrierschlüssel zum Verschlüsseln von Nachrichten dient.

Bei den Verfahren RAH-7, RDH-3, RDH-6 und RDH-7 können Kunde und Kreditin-
stitut über bis zu drei Schlüssel bzw. Schlüsselpaare verfügen:

• einen Schlüssel für digitale Signaturen

• einen Signierschlüssel

• einen Chiffrierschlüssel

Abhängig von der Personalisierung der Chipkarte können Signier- und Chiffrier-
schlüssel identisch sein.

Der Signierschlüssel und der DS-Schlüssel werden zum Unterzeichnen von Trans-
aktionen verwendet, während der Chiffrierschlüssel zum Verschlüsseln von Nach-
richten dient. Falls kreditinstitutsseitig nur Geschäftsvorfälle angeboten werden, für
die gemäß Bankparameterdaten die Unterzeichnung mit dem Signierschlüssel aus-
reichend ist, ist der DS-Schlüssel nicht erforderlich.


![](figures/45.1)


Bei Verwendung von Schlüsseldateien (Sicherheitsprofil RAH,10,
RDH-1, RDH-2 und RDH-10) wird dringend empfohlen, dass ge-
trennte Signier- und Chiffrierschlüssel zum Einsatz kommen.


##### ◆ Schlüsselnamen

Der Schlüsselname bei den 2-Key-Triple-DES- und RSA-Schlüsseln setzt sich aus
den folgenden alphanumerischen Komponenten zusammen:

• Ländercode
(max. 3 Byte, es wird gemäß ISO 3166 der numerische Ländercode verwendet)

. Kreditinstitut

(max. 30 Byte, normalerweise Bankleitzahl, vgl. [Formals], Kapitel II.5.3.2)

<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: B</td>
<td>Version: 3.0 - Final Version</td>
<td>Financial Transaction Services (FinTS) Dokument: Security - Sicherheitsverfahren HBCI</td>
</tr>
<tr>
<td>Seite:<br>32</td>
<td>Stand: 18.07.2013</td>
<td>Kapitel: Verfahrensbeschreibung<br>Abschnitt: Abläufe</td>
</tr>
</table>


. Benutzerkennung

(max. 30 Byte, kann vom Kreditinstitut festgelegt werden, vgl. [Formals], Kapitel
III.1.1)

• Schlüsselart

(1 Byte, D: DS-Schlüssel; S: Signierschlüssel; V: Chiffrierschlüssel)

• Schlüsselnummer
(max. 3 Byte)

. Versionsnummer
(max. 3 Byte)

Falls kein öffentlicher Schlüssel des Kreditinstituts vorliegt, so ist als Versions-
nummer der Wert ,,999" einzustellen. Damit wird kreditinstitutsseitig auf den aktuell
gültigen Schlüssel referenziert (Ein Kreditinstitut kann während einer Übergangszeit
evtl. mehrere Schlüssel bis zu einem Verfallsdatum vorhalten. Aktuell gültig ist je-
weils der neueste Schlüssel).


##### ◆ Generierung von Nachrichtenschlüsseln

Zur Chiffrierung von Nachrichten wird ein dynamisch erzeugter Nachrichtenschlüs-
sel verwendet, der folgendermaßen gebildet wird:


##### RAH-Verfahren:

1\. Generieren einer 32 Byte langen Zufallszahl


##### RDH-Verfahren:

1\. Generieren einer 16 Byte langen Zufallszahl

2\. Erzeugung von ungerader Parität (optional)

3\. Testen, ob erste und zweite Schlüsselhälfte unterschiedlich (optional)

4\. Testen nach schwachen und semi-schwachen Schlüsseln (optional) (s. Kap.
B.2.2)

<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th rowspan="2">Version: 3.0 - Final Version</th>
<th rowspan="2">Kapitel: B</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Security - Sicherheitsverfahren HBCI</td>
</tr>
<tr>
<td>Kapitel:</td>
<td>Verfahrensbeschreibung</td>
<td>Stand:</td>
<td>Seite:</td>
</tr>
<tr>
<td>Abschnitt:</td>
<td>Abläufe</td>
<td>18.07.2013</td>
<td>33</td>
</tr>
</table>


#### B.3.1.2 Symmetrische Schlüssel für DDV

Für Verschlüsselung und MAC-Berechnung werden, wie unter VI.3.1.1 beschrieben,
unterschiedliche Schlüssel für Signatur und Chiffrierung verwendet.


#### B.3.1.2.1 Schlüsselgenerierung

Beim symmetrischen Verfahren (DDV) sind zur Bildung eines kundenindividuellen
Schlüssels beim Kreditinstitut zwei Voraussetzungen zu erfüllen:

· Generierung eines ZKA-weit eindeutigen 2-Key-Triple-DES-Masterkey pro
Schlüsselart und Ablegen in einer sicheren Umgebung (Hardwareeinrichtung) als
Key Generating Key (KGK).

. Herleiten des jeweiligen kundenindividuellen Schlüssels mittels CID-Feld (Card-
holders Information Data = Feld ,,EF_ID") auf der ZKA-Chipkarte und entspre-
chendem 2-Key-Triple-DES-Masterkey.


##### . Generierung eines 2-Key-Triple-DES-Masterkey:

Für die Generierung von ZKA-weit einheitlichen 2-Key-Triple-DES-Masterkeys (KGK
= Key Generating Key), die als Basis für die Herleitung der kundenindividuellen Sig-
nier- und Chiffrierschlüsseln dienen, ist folgendes Verfahren, analog der ZKA-
Chipkarte, zu verwenden:

1\. Generieren einer 16 Byte langen Zufallszahl

2\. Erzeugung von ungerader Parität (optional)

3\. Testen, ob erste und zweite Schlüsselhälfte unterschiedlich

4\. Testen nach schwachen und semi-schwachen Schlüsseln (s. Kap. B.2.2)


##### ◆ Herleitung von Kartenschlüsseln:

Zur eindeutigen Herleitung der symmetrischen Signier- und Chiffrierschlüssel wird
das Feld ,,EF_ID" im Master File (MF) der ZKA-Chipkarte (Cardholders Information
Data (CID) ohne Padding) zusätzlich übertragen (s. DEG „Sicherheitsidentifikation,
Details").

Ein kartenindividueller Schlüssel KK von 16 Byte Länge wird aus

. KGK (Key Generating Key, 16 Byte)

· CID (vollständiger Inhalt von EF_ID, mit X'00' auf das nächste Vielfache von 8
Byte Länge aufgefüllt) und

· dem öffentlich bekannten Initialwert I = X'52 52 52 52 52 52 52 52 25 25 25 25 25
25 25 25' (16 Byte)

zu

KK = P(d * KGK(H(I, CID)))

berechnet.

Hierbei bezeichnen

. 'P' die Funktion "Parity Adjustment" auf ungerade Parität, die wie folgt definiert
ist:

Sei b1,..,b8 die Darstellung eines Byte als Folge von 8 bit. Dann setzt P das nied-
rigstwertige bit b8 jedes Byte auf ungerade Parität, d.h. b8 wird in jedem Byte so
gesetzt, dass es eine ungerade Anzahl von 1 enthält.

<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: B</td>
<td>Version: 3.0 - Final Version</td>
<td>Financial Transaction Services (FinTS) Dokument: Security - Sicherheitsverfahren HBCI</td>
</tr>
<tr>
<td>Seite:<br>34</td>
<td>Stand: 18.07.2013</td>
<td>Kapitel: Verfahrensbeschreibung<br>Abschnitt: Abläufe</td>
</tr>
</table>


. 'd * KGK' die 2-Key-Triple-DES-Entschlüsselung im ECB-Mode (ISO 10116) mit
dem Schlüssel KGK.

. 'H' die in ISO 10118-2 definierte Hash-Funktion.


#### B.3.1.2.2 Initiale Schlüsselverteilung

Die initiale Schlüsselverteilung erfolgt implizit mit der Verteilung der Chipkarte.


#### B.3.1.2.3 Schlüsseländerungen

Beim symmetrischen Verfahren (DDV) ist wegen der Verknüpfung mit der Chipkarte
auf elektronische Weise keine Änderung einzelner kartenindividueller Schlüssel
möglich. Im Falle einer vermuteten Kompromittierung muss daher ein Kartenaus-
tausch oder ein Ersatz aller Schlüssel und des Feldes „EF_ID“ erfolgen.

Bei einer Schlüsseländerung wird die Signatur-ID (Sequenzzähler der Chipkarte) auf
1 zurückgesetzt. Die im Kreditinstitut geführte Liste der eingereichten bzw. noch
nicht eingereichten Signatur-IDs (s. Doppeleinreichungskontrolle) wird gelöscht.


#### B.3.1.2.4 Schlüsselverteilung nach Kompromittierung

Die Schlüsselverteilung nach einer Kompromittierung erfolgt ebenfalls mittels
Vergabe einer neuen Chipkarte bzw. Ersatz aller Schlüssel und des EF-ID-Feldes.
Die alte Chipkarte bzw. deren Schlüssel werden gesperrt.

<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th>Version:</th>
<th>Kapitel:</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Security - Sicherheitsverfahren HBCI</td>
<td>3.0 - Final Version</td>
<td>B</td>
</tr>
<tr>
<td>Kapitel:</td>
<td>Verfahrensbeschreibung</td>
<td>Stand:</td>
<td>Seite:</td>
</tr>
<tr>
<td>Abschnitt:</td>
<td>Abläufe</td>
<td>18.07.2013</td>
<td>35</td>
</tr>
</table>


#### B.3.1.3 Asymmetrische Schlüssel für RAH und RDH

Grundsätzlich können Kunde und Kreditinstitut beim asymmetrischen Verfahren
(RAH und RDH) über maximal drei Schlüsselpaare verfügen:

• ein Signierschlüsselpaar

• ein Chiffrierschlüsselpaar

• ein Schlüsselpaar für die Erzeugung Digitaler Signaturen (DS)

Der Signierschlüssel sowie der DS-Schlüssel werden zum Unterzeichnen von Nach-
richten verwendet, während der Chiffrierschlüssel zum Verschlüsseln von Nachrich-
ten dient (vgl. Kapitel B.1.1).

Falls ein Kreditinstitut seine Nachrichten nicht signiert, kann es auf das Signier-
Schlüsselpaar verzichten.


#### B.3.1.3.1 Schlüsselgenerierung

Die Schlüsselpaare des Kunden sind vom Kundenprodukt bzw. von der Chipkarte
zu erzeugen. Die Schlüsselpaare des Kreditinstituts sind vom Kreditinstitut zu er-
zeugen. Die privaten Schlüssel sind jeweils geheim zu halten.

Die Schlüsselgenerierung hat gemäß dem folgenden Ablauf stattzufinden:11

1\. Es wird ein konstanter öffentlicher Exponent e und ein für jeden Kunden individu-
eller Modulus n für jedes eingesetzte RSA-Schlüsselsystem verwendet.

2\. Der konstante öffentliche Exponent e wird auf die 4. Fermat'sche Primzahl fest-
gelegt: e = 216 + 1

3\. Der Modulus n eines jeden RSA-Schlüsselsystems hat eine Länge von N Bit. Es
sind keine führenden 0-Bits erlaubt, so dass auf jeden Fall gilt: 2N-1 ≤ n < 2N

4\. Der Zielwert für N ist bei RDH-1 768, wobei eine aus der Suche nach starken
Primzahlen resultierende Unterschreitung dieses Wertes um maximal 60 Bit zu-
lässig ist. Bei RDH-2, RDH-3 und RDH-5 liegt der Zielwert für N zwischen 1024
und 2048. Bei RAH-7, RAH-9 und RAH-10 sowie RDH-6, RDH-7, RDH-8, RDH-9
und RDH-10 ergibt sich der Zielwert für N gemäß den Empfehlungen aus [DK
Krypto].


![](figures/49.1)


Schlüsselgenerierung bei RAH10 und RDH-10:

Das Kundensystem muss sicher stellen, dass die Schlüssellänge
eines neu generierten Schlüsselpaares des Kunden gleich der
Länge des öffentlichen Signierschlüssels des Instituts ist, falls
das Institut Institutssignaturen unterstützt. Anderenfalls ist die
Länge des Chiffirierschlüssels maßgebend.

5\. n ist das Produkt zweier großer, zufällig ausgewählter Primzahlen p und q. Fol-
gende Anforderungen werden an die Faktoren p und q gestellt:

· p hat eine vorher festgelegte minimale Länge

<!-- PageFooter: 11 Das Verfahren entspricht dem des DFÜ-Abkommens. -->
<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: B</td>
<td>Version: 3.0 - Final Version</td>
<td>Financial Transaction Services (FinTS) Dokument: Security - Sicherheitsverfahren HBCI</td>
</tr>
<tr>
<td>Seite:<br>36</td>
<td>Stand: 18.07.2013</td>
<td>Kapitel: Verfahrensbeschreibung<br>Abschnitt:<br>Abläufe</td>
</tr>
</table>


• p - 1 hat einen großen Primteiler12 r

• p + 1 hat einen großen Primteiler s

• r - 1 hat einen großen Primteiler

Die entsprechenden Forderungen werden an q gestellt.

Die Längen von p und q sollen sich um höchstens 12 Bits unterscheiden.

Bei der Wahl von p und q ist sicherzustellen, dass e kein Primfaktor von p -1 o-
der q - 1 ist.


#### B.3.1.3.2 Behandlung von Zertifikaten

In FinTS ist die Verwendung von Zertifikaten durch die vorgesehenen Elemente un-
terstützt, es existieren jedoch keine Prozesse für das Zertifikatsmanagement. Diese
sollen zu einem späteren Zeitpunkt auf Basis einer standardisierten Zertifizierungs-
infrastruktur übernommen werden.

Folgende Festlegungen gelten für die Belegung der Zertifikatsfelder in den FinTS-
Segmenten:


##### 1. Allgemein

Bei Verwendung des Signaturschlüssels (D-Schlüssel) wird grundsätzlich in al-
len Nachrichten ein Zertifikat im Signaturkopf mitgeschickt.

Bei Verwendung des Authentifikationsschlüssels (S-Schlüssel) kann ein Zertifi-
kat in den Signaturkopf eingestellt werden.

Im Verschlüsselungskopf kann ebenfalls ein Zertifikat eingestellt werden.
Ggf. dort eingestellte Zertifikate können vom Institut ignoriert werden.


##### 2. Erstmalige Übermittlung Kundenschlüssel bzw. Schlüsseländerung

Bei der Erstmaligen Übermittlung der Kundenschlüssel bzw. bei der Schlüsse-
länderung wird grundsätzlich der Authentifikationsschlüssel (S-Schlüssel) und
wahlweise das zugehörige Zertifikat verwendet. Das Zertifikat wird nur in das
vorgesehene Element im Geschäftsvorfall (HKSAK bzw. HKISA) eingestellt
(nicht in den Signaturkopf).


## 3. Signaturkarten-Profil mit drei unterschiedlichen Schlüsseln

Wenn ein Signaturkarten-Profil mit 3 unterschiedlichen Schlüsseln verwendet
wird, muss bei der Erstmaligen Übermittlung der Kundenschlüssel bzw. der
Schlüsseländerung auch die Möglichkeit bestehen, das Zertifikat für den eige-
nen Verschlüsselungsschlüssel im jeweiligen Geschäftsvorfall (HKSAK bzw.
HKISA) mitzuschicken.

<!-- PageFooter: 12 Der Primteiler sollte dabei ungefähr der Länge des Schlüssels entsprechen. -->
<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th>Version:</th>
<th rowspan="2">Kapitel: B</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Security - Sicherheitsverfahren HBCI</td>
<td>3.0 - Final Version</td>
</tr>
<tr>
<td>Kapitel:</td>
<td>Verfahrensbeschreibung</td>
<td>Stand:</td>
<td>Seite:</td>
</tr>
<tr>
<td>Abschnitt:</td>
<td>Abläufe</td>
<td>18.07.2013</td>
<td>37</td>
</tr>
</table>


## ◆ Ausgewählte Beispiele für Rückmeldungscodes


<table>
<tr>
<td>Code</td>
<td>Beispiel</td>
</tr>
<tr>
<td>9351</td>
<td>Zertifikat noch nicht gültig</td>
</tr>
<tr>
<td>9352</td>
<td>Zertifikat zurückgezogen bzw. gesperrt</td>
</tr>
<tr>
<td>9353</td>
<td>Zertifikatssignatur falsch</td>
</tr>
<tr>
<td>9354</td>
<td>Zertifizierungsinstanz (Herausgeber) nicht akzeptiert</td>
</tr>
<tr>
<td>9355</td>
<td>Fehler im Zertifikatsaufbau</td>
</tr>
<tr>
<td>9356</td>
<td>Zertifikatstyp nicht akzeptiert</td>
</tr>
</table>


### B.3.1.3.3 Initiale Schlüsselverteilung

Der Kunde benötigt für das Einrichten eines neuen Zugangs folgende Initialinfor-
mationen:

. seine Benutzerkennung

. Informationen zum Kommunikationszugang

Die Übermittlung dieser Informationen ist auf folgenden Wegen denkbar:

· Schriftstück des Kreditinstitutes (Benutzerkennung und Zugangsdaten müssen
manuell vom Kunden eingegeben werden)

· Schlüsseldatei des Kreditinstitutes mit folgendem Inhalt:

\- Segment HIUPA der UPD inkl. Benutzerkennung

\- Aktuelle Version der Zugangsdatenbank des jeweiligen Verbandes bzw. Seg-
ment HIKOM mit den Kommunikationszugangsdaten des jeweiligen Instituts

. Chipkarte des Kreditinstitutes, die die Kommunikationszugangsdaten in der Ap-
plikation EF_NOTEPAD enthält.

Zu Beginn muss ein gegenseitiger Austausch der öffentlichen Schlüssel von Kunde
und Kreditinstitut erfolgen. Zukünftig soll dieser Austausch durch eine Anforderung
der Zertifikate bei den jeweiligen Zertifizierungsinstanzen erfolgen. Dieser Prozess
findet auBerhalb des HBCI-Protokolls statt und wird daher hier nicht näher beschrie-
ben. Übergangsweise kann der Schlüsselaustausch auch im Rahmen eines HBCI-
Dialoges erfolgen.

Hierzu ist folgender Ablauf vorgesehen:

1\. Das Kreditinstitut übermittelt seinen öffentlichen Chiffrierschlüssel an den Kun-
den. Falls es Nachrichten signiert, übermittelt es ebenfalls seinen öffentlichen
Signierschlüssel. Hierzu gibt es zwei Möglichkeiten:

· Zusenden bzw. Aushändigung der Schlüssel und anderer relevanter Daten auf
einem Medium (z.B. Schlüsseldatei13, Chipkarte) bei Vertragseröffnung.

Falls dem Kunden eine Schlüsseldatei zugesendet wird, hat diese folgende Da-
ten zu enthalten:

<!-- PageFooter: 13 Es kann sich hierbei um dieselbe Schlüsseldatei handeln, mit der dem Kunden seine Benutzerken- nung mitgeteilt wird (s.o.). -->
<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: B</td>
<td>Version: 3.0 - Final Version</td>
<td>Financial Transaction Services (FinTS) Dokument: Security - Sicherheitsverfahren HBCI</td>
</tr>
<tr>
<td>Seite:<br>38</td>
<td>Stand: 18.07.2013</td>
<td>Kapitel: Verfahrensbeschreibung<br>Abschnitt:<br>Abläufe</td>
</tr>
</table>


\- Datei mit bis zu drei Segmenten vom Typ HIISA, die jeweils einen öffent-
lichen Schlüssel des Kreditinstitutes enthalten

\- BPD des Kreditinstitutes

· Übertragung der Schlüssel beim Erstzugang

(1) Der Kunde fordert die öffentlichen Schlüssel und die BPD mit Hilfe der
Key-Management-Nachricht ,,Erstmalige Anforderung der Schlüssel des
Kreditinstituts" (s. Kap. B.6.2.1) an. Diese Nachricht ist weder signiert
noch chiffriert.

(2) Der weitere Ablauf ist abhängig davon, ob das Kreditinstitut seine Ant-
wortnachrichten signiert.

Fall A: Das Kreditinstitut signiert

Der Kunde erhält die öffentlichen Schlüssel des Kreditinstituts zu-
rückgemeldet. Während die Authentizität des Chiffrierschlüssels
dabei durch die Signatur gesichert ist, ist die Authentizität des
Signierschlüssels nicht gesichert, da das Kundensystem die
Echtheit der Signatur noch nicht prüfen kann.

Fall B: Das Kreditinstitut signiert nicht

Der Kunde erhält nur den öffentlichen Chiffrierschlüssel zurück-
gemeldet. Dessen Authentizität ist dabei nicht gesichert.

(3) Die Sicherung der Authentizität dieser Schlüssel kann über folgende Me-
chanismen erfolgen:

Fall A: Ini-Brief

Diese Nachricht wird von einem Ini-Brief an den Kunden beglei-
tet. Die Gestaltung ist dem Kreditinstitut freigestellt, sollte sich
aber am Muster in Abbildung 14 bzw. Abbildung 15 orientieren.
Der Ini-Brief enthält für den Fall A Exponent und Modulus des
Signierschlüssels sowie dessen Hashwert und für den Fall B Ex-
ponent und Modulus des Chiffrierschlüssels sowie dessen Hash-
wert.

Bei RDH-1 sind dabei Exponent und Modulus mit führenden Nul-
len (X'00') auf 768 Bit zu ergänzen (in den Abbildungen nicht
mehr berücksichtigt).

Bei RAH-7, RAH-9 und RAH-10 sowie RDH-2, RDH-3, RDH-5,
RDH-6, RDH-7, RDH-8, RDH-9 und RDH-10 ist hierbei der Ex-
ponent mit führenden Nullen (X'00') auf die reale Länge des Mo-
dulus zu ergänzen.

Für die Auswahl des zu verwendenden Hashwertverfahrens gel-
ten folgende Regeln:

RIPEMD-160:

Bei RDH-1, RDH-2, RDH-3 und RDH-5 generell;
bei RDH-6, RDH-7, RDH-8, RDH-9 oder RDH-10, wenn
EF_NOTEPAD, HBCI-Version C0=001 (vgl. Abschnitt C.1.2.2.2)

<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th>Version:</th>
<th>Kapitel:</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Security - Sicherheitsverfahren HBCI</td>
<td>3.0 - Final Version</td>
<td>B</td>
</tr>
<tr>
<td>Kapitel:</td>
<td>Verfahrensbeschreibung</td>
<td>Stand:</td>
<td>Seite:</td>
</tr>
<tr>
<td>Abschnitt:</td>
<td>Abläufe</td>
<td>18.07.2013</td>
<td>39</td>
</tr>
</table>


SHA-256:

bei RAH-7, RAH-9 und RAH-10 sowie RDH-6, RDH-7, RDH-8,
RDH-9 oder RDH-10, wenn EF_NOTEPAD, HBCI-Version
C0=002 (vgl. Abschnitt C.1.2.2.2)

Ferner enthält der Ini-Brief den jeweiligen Schlüsselnamen.

Bei der Hashwertbildung ist wie folgt vorzugehen:

a) RDH-1: Padding der höchstwertigen Bits von Exponent und
Modulus des Schlüssels mit Nullen (X'00') auf 1024 Bit

sonst: Padding der höchstwertigen Bits des Exponenten mit
Nullen (X'00') auf die reale Länge des Modulus

b) Konkatenierung von Exponent und Modulus (Exponent || Mo-
dulus)

c) Bildung des Hashwerts mittels RIPEMD-160 bzw. SHA-256
gemäß Kap. B.2.1.1 über diesen Ausdruck

Nach Erhalt des Ini-Briefs führt der Kunde einen Vergleich des im
Ini-Brief aufgeführten Hashwerts mit dem Hashwert des vom
Kreditinstitut übermittelten Schlüssels durch.

Bei Übereinstimmung der Hashwerte gelten der bzw. die öffentli-
chen Schlüssel des Kreditinstituts als authentisiert.


![](figures/53.1)


Das Kundenprodukt sollte den Hashwertver-
gleich für den Kunden in geeigneter Weise un-
terstützen.


#### Fall B: Übermittlung des Hashwerts auf der Chipkarte

Auf der Karte befindet sich in der Applikation EF_NOTEPAD (s.
Kap. C.1.1) für Fall A der Hashwert des öffentlichen Signier-
schlüssels des Kreditinstituts und für Fall B der Hashwert des öf-
fentlichen Chiffrierschlüssels des Kreditinstituts. Die Hashwertbil-
dung erfolgt wie in Fall A.

Dieser Hashwert wird vom Kundenprodukt mit dem Hashwert des
in der Nachricht übermittelten Schlüssels verglichen.


![](figures/53.2)


Das Kundenprodukt sollte den Kunden über
das Ergebnis des Hashwertvergleichs informie-
ren.

Bei Übereinstimmung der Hashwerte gelten der bzw. die öffentli-
chen Schlüssel des Kreditinstituts als authentisiert.

<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: B</td>
<td>Version: 3.0 - Final Version</td>
<td>Financial Transaction Services (FinTS) Dokument: Security - Sicherheitsverfahren HBCI</td>
</tr>
<tr>
<td>Seite:<br>40</td>
<td>Stand:<br>18.07.2013</td>
<td>Kapitel: Verfahrensbeschreibung<br>Abschnitt:<br>Abläufe</td>
</tr>
</table>


#### Fall C: Prüfung des übermittelten Zertifikates

Falls das Kreditinstitut über zertifikatsbasierte Schlüssel verfügt,
übermittelt es das jeweilige Zertifikat in der Nachricht zusammen
mit dem öffentlichen Schlüssel.

Somit ist der Kunde in der Lage, das Zertifikat bei der jeweiligen
Zertifizierungsinstanz zu verifizieren. Diese Verifikation findet au-
Berhalb des FinTS-Protokolls statt und wird daher hier nicht nä-
her beschrieben.

Ein Hashwertvergleich wie in den beiden anderen Fällen ist nicht
erforderlich.


![](figures/54.1)


Das Kundenprodukt sollte den Kunden über
das Ergebnis der Zertifikatsprüfung informieren.

2\. Der Kunde übermittelt alle seine öffentlichen Schlüssel, die mit dem privaten Si-
gnierschlüssel unterzeichnet wurden, im Rahmen der Key-Management-Nach-
richt „Erstmalige Übermittlung der Schlüssel des Kunden“ an das Kreditinstitut
(vgl. Kapitel B.8.1.3). Diese Nachricht muss sowohl signiert als auch chiffriert
sein.

3\. Um die Authentizität der Schlüssel zu gewährleisten, sind folgende Mechanismen
möglich:


##### Fall A: Ini-Brief

Der Kunde erfährt anhand des Rückmeldungscodes 3310 („Ini-Brief er-
forderlich“) in der Kreditinstitutsnachricht, dass diese Nachricht durch ei-
nen Ini-Brief gemäß dem in Abbildung 14 bzw. Abbildung 15 aufgeführ-
ten Muster begleitet werden muss. Im Ini-Brief bestätigt der Kunde aus-
schließlich den öffentlichen Signierschlüssel mit handschriftlicher Unter-
schrift. Eine Bestätigung des öffentlichen Chiffrierschlüssels ist nicht er-
forderlich, da dieser mit dem Signierschlüssel signiert wird und damit au-
thentifiziert ist. Neben dem Schlüssel und dem Schlüsselnamen wird im
Ini-Brief der Hashwert des Schlüssels aufgeführt. Dieser wird ebenso
gebildet wie der Hashwert im Ini-Brief des Kreditinstituts (s.o.).

Im Kreditinstitut findet ein Vergleich zwischen dem im Ini-Brief aufgeführ-
ten Hashwert und dem Hashwert des vom Kunden übermittelten öffentli-
chen Signierschlüssels statt.

Falls dieser Vergleich positiv verläuft, werden die öffentlichen Schlüssel
des Kunden freigeschaltet.


#### Fall B: Prüfung des übermittelten Zertifikates

Der Kunde erfährt anhand des Rückmeldungscodes 3320 (,Ini-Brief
nicht erforderlich") in der Kreditinstitutsnachricht, dass das Kreditinstitut
die Prüfung der Authentizität der Schlüssel auf Basis eines Zertifikates
vornehmen kann.

Falls der Kunde über zertifikatsbasierte Schlüssel verfügt, übermittelt er
daher das jeweilige Zertifikat in der Nachricht zusammen mit dem öffent-
lichen Schlüssel. Somit ist das Kreditinstitut in der Lage, das Zertifikat
bei der jeweiligen Zertifizierungsinstanz zu verifizieren.

<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th>Version:</th>
<th>Kapitel:</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Security - Sicherheitsverfahren HBCI</td>
<td>3.0 - Final Version</td>
<td>B</td>
</tr>
<tr>
<td>Kapitel:</td>
<td>Verfahrensbeschreibung</td>
<td>Stand:</td>
<td>Seite:</td>
</tr>
<tr>
<td>Abschnitt:</td>
<td>Abläufe</td>
<td>18.07.2013</td>
<td>41</td>
</tr>
</table>


Diese Verifikation findet auBerhalb des FinTS-Protokolls statt und wird
daher hier nicht näher beschrieben.

Ein Hashwertvergleich wie in Fall A ist nicht erforderlich.

4\. Im nächsten Schritt wird der Kunde freigeschaltet.

5\. Es hat eine Synchronisierung der Kundensystem-ID zu erfolgen (s. [Formals],
Kap. III.8).

6\. Hiermit ist die Erstinitialisierung abgeschlossen und der Kunde kann Auftrags-
nachrichten senden.


Abbildung 13: Ablauf der Erstinitialisierung bei RDH

![Erstmalige Anforderung der Schlüssel des Kreditinstituts Kunde Kreditinstitut Erstmalige Übermittlung der Schlüssel des Kunden Synchronisierung der Kundensystem-ID Auftragsdialog](figures/55.1)


Um die Multibankfähigkeit verschiedener Kundenprodukte zu sichern, gelten für die
Ini-Schlüsseldatei folgende Namenskonventionen:

. Segment HIUPA:
<Benutzerkennung>.UPA

· Datei mit den öffentlichen Schlüsseln:
<Benutzerkennung>.PKD

. BPD:

<Bankleitzahl>.BPD

· Segment mit Kommunikationszugang:
<Bankleitzahl>.KOM

· Zugangsdatenbank des Verbandes:
BDB.KOM, BVR.KOM, DSGV.KOM bzw.
VOEB.KOM

Falls die Benutzerkennung nicht im Dateisystem darstellbar ist, ist sie entsprechend
zu kürzen. Die Schlüsseldatei muss im Standardformat des jeweiligen Betriebssys-
tems formatiert sein. Die Dateien sind im Stammverzeichnis der Schlüsseldatei ab-
zulegen.

<!-- PageBreak -->


<table>
<tr>
<td>Kapitel:<br>B</td>
<td>Version: 3.0 - Final Version</td>
<td>Financial Transaction Services (FinTS) Dokument: Security - Sicherheitsverfahren HBCI</td>
</tr>
<tr>
<td>Seite:</td>
<td>Stand:</td>
<td>Kapitel: Verfahrensbeschreibung</td>
</tr>
<tr>
<td>42</td>
<td>18.07.2013</td>
<td>Abschnitt:<br>Abläufe</td>
</tr>
</table>


Abbildung 14: Beispiel für die Gestaltung des Ini-Briefs bei RDH-2 oder RDH-5

![Ini-Brief HBCI Benutzername Kundensoftware-interner Name (Angabe freigestellt) Datum Datum der Erstellung des Initialisierungsauftrags (TT.MM.JJJJ) Uhrzeit Uhrzeit der Erstellung des Initialisierungsauftrags (hh:mm) Empfänger Kreditinstitutskennung (wird vom jeweiligen Kreditinstitut mitgeteilt) Benutzerkennung max. 30 Stellen alphanumerisch (wird vom jeweiligen Kreditinstitut mitgeteilt) Schlüsselnummer Nummer des Signierschlüssels (max. 3 Stellen) Schlüsselversion Version des Signierschlüssels (max. 3 Stellen) HBCI-Version derzeit 3.0 Sicherheitsprofil RDH-2, RDH-3 oder RDH-5 Öffentlicher Schlüssel für die elektronische Signatur: Exponent <Reale Moduluslänge> 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 01 00 01 Modulus .2048 97 A9 D8 FD 68 46 BA 5E DB E0 F5 35 41 3C B3 7C 95 6A 8C 11 29 63 1C 41 4A CC E3 A7 A6 7B A8 6D E8 1D 99 D2 BF 2A 5D B6 74 24 6E 6C C6 FD A9 9C 19 15 44 FB 88 19 66 2D 93 5B 80 FA 9B 42 FE 8C B2 A2 1C 96 FB 4F 5E 6A 5E 84 E6 9A 76 AB 52 5A 36 C1 6D F8 B1 EF E0 D1 65 0A BC 86 35 86 5B ฿5 84 A1 44 76 69 DE 34 D5 31 E7 8E A2 D0 25 02 78 B5 24 BE 57 AB C0 D9 30 13 B1 04 95 91 DF 23 0D 81 3B 58 E1 91 33 CD E5 3D E7 39 00 A2 EF 4B 60 85 71 3E 39 92 7C 14 F9 06 3A 97 3D 37 F1 9E A5 71 30 33 E2 60 3F 87 52 80 AF 4E E4 DD 38 66 E8 B2 29 6B BF 25 36 3E 0F A0 55 39 4A 31 7A 69 88 9B D6 3B 26 B6 B6 53 44 CA 33 C7 E0 40 4A 60 79 43 29 97 43 A6 50 C4 DC F2 EF 54 B6 E8 BD 05 95 17 56 93 13 EΕ B2 2A B9 87 52 FC 24 75 D4 F2 A7 E7 D1 CD 90 9A D3 D8 78 99 1D C3 21 4D 2F 5A A3 Hashwert (RIPEMD-160): 0B AD D5 D5 FD 57 0D 34 E7 84 7C ED AE 4B 3D EE 6B EB 98 AC Ich bestätige hiermit den obigen öffentlichen Schlüssel für meine elektronische Signatur. Ort / Datum Fima/Name Unterschrift](figures/56.1)


Die folgende Abbildung zeigt ein Beispiel für einen Ini-Brief bei Verwendung der Si-
cherheitsprofile RAH-9, RAH-10, RDH-8, RDH-9 oder RDH-10 unter Verwendung
von SHA-256 als Hashwertverfahren14.

<!-- PageFooter: 14 SHA-256 als Haswertverfahren kann nur bei Bankensignaturkarten zum Einsatz kommen, die über die EF_NOTEPAD HBCI-Version C0=002 verfügen (vgl Abschnitt C.1.2.2.2). -->
<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th>Version:</th>
<th>Kapitel:</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Security - Sicherheitsverfahren HBCI</td>
<td>3.0 - Final Version</td>
<td>B</td>
</tr>
<tr>
<td>Kapitel:</td>
<td>Verfahrensbeschreibung</td>
<td>Stand:</td>
<td>Seite:</td>
</tr>
<tr>
<td>Abschnitt:</td>
<td>Abläufe</td>
<td>18.07.2013</td>
<td>43</td>
</tr>
</table>


Abbildung 15: Beispiel für die Gestaltung des Ini-Briefs bei RAH-9, RAH-10, RDH-8,
RDH-9 oder RDH-10

![Ini-Brief HBCI Benutzemame Kundensoftware-interner Name (Angabe freigestellt) Datum Datum der Erstellung des Initialisierungsauftrags (TT.MM.JJJJ) Uhrzeit Uhrzeit der Erstellung des Initialisierungsauftrags (hh:mm) Empfänger Kreditinstitutskennung (wird vom jeweiligen Kreditinstitut mitgeteilt) Benutzerkennung max. 30 Stellen alphanumerisch (wird vom jeweiligen Kreditinstitut mitgeteilt) Schlüsselnummer Nummer des Signierschlüssels (max. 3 Stellen) Schlüsselversion Version des Signierschlüssels (max. 3 Stellen) HBCI-Version derzeit 3.0 Sicherheitsprofil RAH-9, RAH-10, RDH-8, RDH-9 oder RDH-10 Öffentlicher Schlüssel für die elektronische Signatur: Exponent <Reale Moduluslänge> 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 0 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 01 00 01 Modulus .2048 97 A9 D8 FD 3C 68 46 BA 8C 5E DB E0 1C 35 41 41 4A B3 7C F5 E8 D2 95 74 6A 24 CC 11 29 E3 A7 63 A6 1D 99 6E 6C C6 FD A9 9C A2 7B A8 6D 19 15 44 BF 2A 5D B6 2D 93 5B FA FB 88 19 FE B2 1C 5E 96 FB 4F 5E 66 6A F8 80 84 81 9B 42 8C E6 9A 76 AB 52 5A EF 36 E0 C1 6D D1 65 0A BC 86 35 86 E7 8E 5B B5 84 A1 44 76 69 DE 34 D5 31 A2 D0 25 02 78 B5 24 BE 57 AB C0 D9 30 B1 0D E1 33 CD E5 A2 13 04 91 DF 3B 3D E7 EF 95 23 81 58 91 71 39 37 3E 00 92 7C F9 06 4B 60 97 3D 3F 85 3A 87 52 80 AF 4E 39 F1 9E 14 A5 71 30 33 29 6C E4 DD 38 66 E8 B2 6B BF F2 25 36 3E 0F A0 55 39 C7 4A 31 7A 69 88 9B D6 26 B6 B6 53 CA 40 4A 60 79 29 C4 97 DC 43 F2 3B 54 A6 B6 44 33 E0 E8 52 05 43 50 EF 87 17 13 EE D4 F2 BD B2 2A B9 95 FC 56 93 24 75 A7 E7 D1 CD 90 9A D3 D8 78 99 1D C3 21 4D 2F 5A A3 Hashwert (SHA-256): BF C2 A1 01 7C 65 31 9C BB 1B D8 26 09 85 E6 1F A9 99 1A 65 17 BF 67 86 17 D8 7C EE DC C3 61 11 Ich bestätige hiermit den obigen öffentlichen Schlüssel für meine elektronische Signatur. Ort / Datum Firma/Name Unterschrift](figures/57.1)


##### B.3.1.3.4 Schlüsseländerungen


###### ◆ Routinemäßige Schlüsseländerung des Kunden

Bei Speicherung der Schlüssel auf einer Chipkarte ist i.d.R. auf elektronische Weise
keine Änderung einzelner kartenindividueller Schlüssel möglich. Im Falle einer routi-
nemäßigen Schlüsseländerung (z.B. bei Ablauf des Zertifikates) oder einer vermute-
ten Kompromittierung muss daher ein Kartenaustausch oder ein Ersatz aller
Schlüssel erfolgen.

Falls die Karte die Generierung neuer Schlüssel zulässt oder im Falle anderer Spei-
chermedien (Schlüsseldatei) ändert der Kunde seine Schlüsselpaare unabhängig
voneinander.

Der Kunde sendet je Kreditinstitut im Rahmen eines HBCI-Dialoges eine Nachricht,
in welcher dieses über einen neuen öffentlichen Schlüssel informiert wird (vgl. Kapi-
tel B.6.2.1). Die Nachricht ist mit dem alten (bei Wechsel des Signierschlüssels),
respektive dem aktuellen (bei Wechsel des DS-Schlüssels oder des Chiffrierschlüs-
sels) privaten Signierschlüssel des Kunden zu signieren und mit dem aktuellen
Chiffrierschlüssel des Kreditinstituts zu chiffrieren.

<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: B</td>
<td>Version: 3.0 - Final Version</td>
<td>Financial Transaction Services (FinTS) Dokument: Security - Sicherheitsverfahren HBCI</td>
</tr>
<tr>
<td>Seite:<br>44</td>
<td>Stand: 18.07.2013</td>
<td>Kapitel: Verfahrensbeschreibung<br>Abschnitt: Abläufe</td>
</tr>
</table>


Das Kreditinstitut speichert diesen neuen öffentlichen Schlüssel des Kunden und
verwendet ihn ab sofort (d.h. bereits in der Antwortnachricht) für alle Verschlüsse-
lungen bzw. Verifikationen von Signaturen. Gleichzeitig kann der alte Schlüssel ge-
sperrt werden. Zusätzlich ist es jedoch bei kartengestützten Verfahren – unabhängig
von der Nutzung von Zertifikaten – erlaubt, einen Schlüssel für die Laufzeit der Kar-
te weiter aktiv zu halten und somit zwei Schlüssel parallel zu unterstützen.

Falls die Übermittlung der neuen Schlüssel aus irgendeinem Grunde fehlschlägt,
kann der Kunde den Vorgang beliebig wiederholen.

Bei einer Schlüsseländerung wird die Signatur-ID auf 1 zurückgesetzt. Die Liste der
eingereichten bzw. noch nicht eingereichten Signatur-IDs (s. Doppeleinreichungs-
kontrolle) wird gelöscht.


###### ◆ Routinemäßige Schlüsseländerung des Kreditinstituts

Ein Kreditinstitut generiert bei Bedarf ein neues Schlüsselpaar.

Der Kunde sendet jeweils bei der Dialoginitialisierung die Referenz auf die öffent-
lichen Schlüssel des Kreditinstitutes mit (vgl. [Formals], Kapitel III.3.1). Falls das
Kreditinstitut über aktuellere öffentliche Schlüssel verfügt, werden diese in der Kre-
ditinstitutsnachricht mitübertragen (vgl. [Formals], Kapitel III.3.2 respektive B.6.1.3).
Die neuen Schlüssel gelten ab sofort, d.h. bereits für die erste Auftragsnachricht
nach der Dialoginitialisierung. Da das Kreditinstitut i.d.R. aber auch noch die alten
Schlüssel aktiv hält, werden für einen begrenzten Zeitraum auch noch Nachrichten
akzeptiert, die mit den alten Kreditinstitutsschlüsseln chiffriert wurden.

Zur Verifikation des kreditinstitutsseitigen öffentlichen Schlüssels auf dem Kunden-
system kann das entsprechende Kreditinstitut die Kreditinstitutsnachricht mit dem al-
ten Signierschlüssel signieren (wenn eine kreditinstitutsseitige Signatur vorgesehen
ist) oder den Hashwert des öffentlichen Schlüssels analog der initialen Schlüssel-
verteilung an den Kunden übermitteln. Die Verifikation ist grundsätzlich optional.

Für den Fall, dass der alte Kreditinstitutsschlüssel nicht mehr zur Verfügung steht
oder gesperrt werden musste, wird dem Kunden - falls er den alten Kreditinstituts-
schlüssel zur Chiffrierung der Dialoginitialisierung verwendet – der Rückmeldungs-
code "9030" mit dem Hinweis "Fehler beim Entschlüsseln" gesendet. Ggf. kann die
Dialoginitialisierung vom Kreditinstitutssystem auch gar nicht verarbeitet werden, so
dass keine Antwort gesendet wird. Daraufhin sollte das Kundenprodukt über den
anonymen Dialog mit Hilfe der Nachricht ,Erstmalige Anforderung der Schlüssel des
Kreditinstituts" (s. Kap. B.6.2.1) die neuen Kreditinstitutsschlüssel anfordern. Zur Ve-
rifikation der neuen Schlüssel muss dem Kunden in diesem Fall zusätzlich ein Ini-
Brief mit dem Hashwert des neuen Kreditinstitutsschlüssels zugeschickt werden.


##### B.3.1.3.5 Schlüsselverteilung nach Kompromittierung

Die Verteilung der Schlüssel nach einer Kompromittierung erfolgt analog der Schlüs-
selverteilung bei der Initialisierung. Es findet immer ein Austausch aller Schlüssel
statt, auch dann, wenn nur einer der Schlüssel kompromittiert wurde.

<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th>Version:</th>
<th rowspan="2">Kapitel: B</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Security - Sicherheitsverfahren HBCI</td>
<td>3.0 - Final Version</td>
</tr>
<tr>
<td>Kapitel:</td>
<td>Verfahrensbeschreibung</td>
<td>Stand:</td>
<td>Seite:</td>
</tr>
<tr>
<td>Abschnitt:</td>
<td>Abläufe</td>
<td>18.07.2013</td>
<td>45</td>
</tr>
</table>


###### B.3.2 Schlüsselsperrung

Bei der Schlüssel- bzw. Benutzersperrung muss zwischen folgenden Fällen unter-
schieden werden:

· Kompromittierung des eigenen Schlüssels

• Verlust des eigenen Schlüssels

· Überschreiten der Anzahl der Falschsignaturen

Zusätzlich müssen bei der Sperrung noch folgende Punkte berücksichtigt werden:

. Information des Kunden

. Entsperrung

Die Sperrung anderer Benutzer wird als eigenständiger Auftrag behandelt und zu
einem späteren Zeitpunkt realisiert.


####### . Kompromittierung des eigenen Schlüssels

Bei Verdacht auf Kompromittierung des eigenen Schlüssels kann die Sperrung mit-
tels einer speziellen Nachricht (vgl. Kapitel B.8.1.4) erfolgen, welche signiert sein
muss.


####### ◆ Verlust des eigenen Schlüssels

Bei einem Verlust (inkl. Diebstahl) des eigenen Schlüssels (respektive des Spei-
chermediums) muss der Kunde Schlüssel bzw. Medium sperren und beim Kreditin-
stitut ein anderes Medium inkl. Schlüssel beantragen.

Eine nicht-signierungspflichtige Sperrmöglichkeit ist optional, da hierdurch die Ge-
fahr des Mißbrauchs gegeben ist (absichtliche Sperrung fremder Anschlüsse). Der
Segmentaufbau erfolgt analog der oben beschriebenen Nachricht, jedoch ist keine
Signatur nötig (möglich). Die Steuerung hierfür erfolgt über das Feld „Anzahl benö-
tigter Signaturen" in der UPD.

Eine Sperrung auf anderem Weg (z.B. telefonische Sperrung über Servicezentralen)
muss immer möglich sein (z.B. Verlust der eigenen Infrastruktur).


####### ◆ Überschreiten der Anzahl der Falschsignaturen

Wird beim Einreichen von Aufträgen durch fehlerhafte Signaturen die festgelegte
Anzahl von n Falschsignaturen in Folge überschritten, werden kreditinstitutsseitig
die Schlüssel gesperrt. Als Falschsignaturen werden dabei fehlgeschlagene krypto-
graphische Operationen, jedoch z.B. keine fehlerhaften Berechtigungen verstanden.

Bei einer Sperrung aufgrund zu vieler Fehlsignaturen werden alle Kundenschlüssel
gesperrt. Sofern die Nachricht lediglich von einem einzigen Benutzer signiert wurde
oder falls bei einer mehrfach signierten Nachricht der Dialogführer von der Fehlsig-
naturensperre betroffen ist, wird der Dialog beendet. Der Dialogabbruch erfolgt da-
bei kreditinstitutsseitig im Anschluss an die Antwortnachricht, d.h. ein Austausch von
Dialogbeendigungsnachrichten findet nicht statt. Die Antwort ist beim DDV-
Verfahren weder signiert noch verschlüsselt. Beim RAH- bzw. RDH-Verfahren ist die
Antwort signiert (sofern kreditinstitutsseitig signiert wird) aber nicht verschlüsselt. In
der Antwortnachricht teilt das Kreditinstitut lediglich den Grund des Dialogendes mit.
Antworten auf Aufträge dürfen nicht mitgesendet werden, da diese aufgrund der
Sperrung nicht abgesichert werden können.

<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: B</td>
<td>Version: 3.0 - Final Version</td>
<td>Financial Transaction Services (FinTS) Dokument: Security - Sicherheitsverfahren HBCI</td>
</tr>
<tr>
<td>Seite:<br>46</td>
<td>Stand: 18.07.2013</td>
<td>Kapitel: Verfahrensbeschreibung<br>Abschnitt: Abläufe</td>
</tr>
</table>


## . Information des Kunden

Im Falle einer Sperrung aufgrund von Schlüsselkompromittierung oder Schlüs-
selverlust erhält der Kunde auf die Sperrnachricht eine Antwortnachricht (vgl. Kapitel
B.8.1.4 b), welche ihm die Sperrung bestätigt. Bei einer Sperrung wegen Über-
schreitung des Maximalwertes möglicher Falschsignaturen erhält er lediglich einen
entsprechenden Rückmeldungscode. In jedem Fall erhält er jedoch entsprechende
Fehlermeldungen bei der Einreichung nachfolgender Nachrichten.


## . Entsperrung der Benutzerkennung

Eine Entsperrung erfolgt nur gegen handschriftliche Unterschrift des Kunden.

Ist der Schlüssel kompromittiert oder nicht mehr auffindbar, so wird für den Benutzer
eine neue Chipkarte, respektive neue Schlüssel und ein neues EF_ID (DDV), oder
ein neues Schlüsselpaar (RAH bzw. RDH) erzeugt und der alte Schlüssel bleibt ge-
sperrt. Es werden in jedem Falle alle Schlüsselpaare neu vergeben, auch wenn nur
ein Schlüsselpaar kompromittiert sein sollte. Damit ein Benutzer nach einer Sper-
rung wieder zum Zugang zum System autorisiert werden kann, darf er in diesem
Fall ausnahmsweise einer erneute Erstinitialisierung durchführen und seine Schlüs-
sel über einen Ini-Brief freischalten lassen.

In den übrigen Fällen kann der Schlüssel einfach durch das Kreditinstitut entsperrt
werden.

<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th>Version:</th>
<th rowspan="2">Kapitel: B</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Security - Sicherheitsverfahren HBCI</td>
<td>3.0 - Final Version</td>
</tr>
<tr>
<td>Kapitel:</td>
<td>Verfahrensbeschreibung</td>
<td>Stand:</td>
<td>Seite:</td>
</tr>
<tr>
<td>Abschnitt:</td>
<td>Bankfachliche Anforderungen</td>
<td>18.07.2013</td>
<td>47</td>
</tr>
</table>


## B.4 Bankfachliche Anforderungen


### ◆ Zu signierende Nachrichten

Grundsätzlich sind alle Kundennachrichten zu signieren, bei Sicherheitsprofil
RAH-7, RDH-3, RDH-6 und RDH-7 gemäß den in den BPD vorgegebenen Sicher-
heitsklassen. Ausnahmen gelten beim anonymen Zugang, bei der Erstinitialisierung
und der Schlüsselsperrung.

Die Signatur von Kreditinstitutsnachrichten ist optional.


### . Doppeleinreichungskontrolle

Die Doppeleinreichungskontrolle wird mittels eines Zählers pro Signatur realisiert
(Signatur-ID), dessen Inhalt jeweils in die Signatur(en) der Nachricht einfließt. Falls
als Sicherheitsmedium keine Chipkarte verwendet wird, wird zur Doppeleinrei-
chungskontrolle zusätzlich zur Signatur-ID die Kundensystem-ID benötigt.

Bei der Doppeleinreichungskontrolle (Verhinderung von Replay-Attacken) ist zu be-
rücksichtigen, dass die sequentiell erzeugten Referenznummern (=Signatur-IDs)
beim Kreditinstitut nicht in derselben Reihenfolge eintreffen müssen, da diese kun-
denseitig auch offline (d.h. zeitlich voneinander unabhängig) generiert werden kön-
nen. Das Kreditinstitut muss deshalb sicherstellen, dass innerhalb eines bestimmten
Zeitraums keine Sequenznummer mehrfach erscheint.

Aus diesem Grund muss beim Kreditinstitut eine Liste mit den eingereichten (Posi-
tivliste) oder noch nicht eingereichten (Negativliste) Signatur-IDs geführt werden.
Nach einer festgelegten Aufbewahrungsfrist wird eine Referenznummer nicht mehr
akzeptiert. (Konkret wird ein Kreditinstitut eine Nachricht abweisen, welche länger
als die vereinbarte Frist nach einer Nachricht mit höherer Signatur-ID eintrifft). Diese
Liste muss je Signaturschlüsselpaar geführt werden, d.h., falls der Benutzer sowohl
mit dem Signierschlüssel- als auch mit dem DS-Schlüssel unterschreibt, sind zwei
Listen erforderlich.


### . Mehrfachsignaturen

Bei Mehrfachsignaturen kann unterschieden werden, ob die Reihenfolge der Unter-
zeichnung bedeutungslos oder relevant ist. Diese Unterscheidung muss nicht nur im
Kundenprodukt gemacht werden können, sondern hat auch Einfluss auf die Verar-
beitung und Kontrolle im Kreditinstitut. In der vorliegenden FinTS-Version ist die
Reihenfolge der Signaturen bedeutungslos.

Sind die Berechtigungsprofile mehrerer signierender Benutzer zueinander inkonsis-
tent, so liegt es im Ermessen des Kreditinstituts, ob es die Nachricht annimmt oder
ablehnt (Beispiel: Der Erfasser einer Nachricht, für deren Aufträge drei Signaturen
erforderlich sind, liefert nur eine zweite Signatur eines Benutzers mit, der über das
Recht verfügt, die Aufträge alleine zu signieren).

Ob es zulässig ist, dass bei Mehrfachsignaturen verschiedene Signaturverfahren
eingesetzt werden, gibt das Kreditinstitut in den BPD im Segment ,Sicherheitsver-
fahren“ ([Formals], Kap. IV.4) an.

<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: B</td>
<td>Version: 3.0 - Final Version</td>
<td>Financial Transaction Services (FinTS) Dokument: Security - Sicherheitsverfahren HBCI</td>
</tr>
<tr>
<td>Seite:<br>48</td>
<td>Stand: 18.07.2013</td>
<td>Kapitel: Verfahrensbeschreibung<br>Abschnitt: Formate für Signatur und Verschlüsselung</td>
</tr>
</table>


## B.5 Formate für Signatur und Verschlüsselung

Für die Speicherung der Sicherheitsinformationen für die Signatur(en) werden un-
mittelbar nach dem Nachrichtenkopf das (die) Segment(e) „Signaturkopf“ (HNSHK)
und unmittelbar vor dem Nachrichtenabschluss das (die) Segment(e) „Signaturab-
schluss“ (HNSHA) in die bestehende Nachricht eingeschoben.

Dies entspricht dem in UN/EDIFACT definierten Vorgehen und kann folgenderma-
Ben visualisiert werden:


<table>
<tr>
<td>HNHBK</td>
<td>HNSHK</td>
<td>HBCI-Nutzdaten</td>
<td>HNSHA</td>
<td>HNHBS</td>
</tr>
</table>


(Die grau hinterlegten Bereiche gehen in die Signatur mit ein.)

Falls mehrere Signaturen für HBCI-Nachrichten erforderlich sind, so wiederholen
sich Signaturkopf und -abschluss entsprechend:


<table>
<tr>
<td>HNHBK</td>
<td>HNSHK2</td>
<td>HNSHK1</td>
<td>HBCI-Nutzdaten</td>
<td>HNSHA1</td>
<td>HNSHA2</td>
<td>HNHBS</td>
</tr>
</table>


(Die grau hinterlegten Bereiche bezeichnen die Daten für die Zweit-Signatur bei be-
liebiger Reihenfolge der Signaturen (vgl. Kapitel B.4)).

Bei der Verschlüsselung wird nach dem Nachrichtenkopf ein Verschlüsselungskopf-
Segment (HNVSK) eingefügt. Dies bedeutet, dass alle Daten nach dem Segment-
endekennzeichen des Nachrichtenkopfes bis zum letzten Byte vor dem Nachrich-
tenabschluss inklusive aller Signaturen in die Verschlüsselung eingehen:


<table>
<tr>
<td>HNHBK</td>
<td>HNVSK</td>
<td>ek(HNSHKn | HBCI-Nutzdaten | HNSHAn)</td>
<td>HNHBS</td>
</tr>
</table>


Grundsätzlich erfolgt die Reihenfolge der Sicherheitsverarbeitung in folgender Rei-
henfolge:

1\. elektronische Signatur

2\. evtl. Zweit- und Drittsignatur

3\. (Komprimierung) und Verschlüsselung

Für die Übermittlung der sicherheitsrelevanten Informationen werden die folgenden
Segmente und Datenelementgruppen übertragen.

<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th>Version:</th>
<th>Kapitel:</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Security - Sicherheitsverfahren HBCI</td>
<td>3.0 - Final Version</td>
<td>B</td>
</tr>
<tr>
<td>Kapitel:</td>
<td>Verfahrensbeschreibung</td>
<td>Stand:</td>
<td>Seite:</td>
</tr>
<tr>
<td>Abschnitt:</td>
<td>Formate für Signatur und Verschlüsselung</td>
<td>18.07.2013</td>
<td>49</td>
</tr>
</table>


### B.5.1 Signaturkopf


#### . Beschreibung

Der Signaturkopf enthält Informationen über den damit verbundenen Sicherheitsser-
vice, sowie über den Absender.

. Format


<table>
<tr>
<td>Name:</td>
<td>Signaturkopf</td>
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
<td>HNSHK</td>
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
<td>Kunde/Kreditinstitut</td>
</tr>
</table>


<table>
<tr>
<th>Nr.</th>
<th>Name</th>
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
<td>DEG</td>
<td></td>
<td></td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>2</td>
<td>Sicherheitsprofil</td>
<td>DEG</td>
<td></td>
<td></td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>3</td>
<td>Sicherheitsfunktion, ko- diert</td>
<td>DE</td>
<td>code</td>
<td>..3</td>
<td>M</td>
<td>1</td>
<td>1,2</td>
</tr>
<tr>
<td>4</td>
<td>Sicherheitskontrollrefe- renz</td>
<td>DE</td>
<td>an</td>
<td>..14</td>
<td>M</td>
<td>1</td>
<td>&lt;&gt;0</td>
</tr>
<tr>
<td>5</td>
<td>Bereich der Sicherheits- applikation, kodiert</td>
<td>DE</td>
<td>code</td>
<td>..3</td>
<td>M</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td>6</td>
<td>Rolle des Sicherheits- lieferanten, kodiert</td>
<td>DE</td>
<td>code</td>
<td>..3</td>
<td>M</td>
<td>1</td>
<td>1, 3, 4</td>
</tr>
<tr>
<td>7</td>
<td>Sicherheitsidentifikation, Details</td>
<td>DEG</td>
<td></td>
<td></td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>8</td>
<td>Sicherheitsreferenznum- mer</td>
<td>DE</td>
<td>num</td>
<td>.. 16</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>9</td>
<td>Sicherheitsdatum und -uhrzeit</td>
<td>DEG</td>
<td></td>
<td></td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>10</td>
<td>Hashalgorithmus</td>
<td>DEG</td>
<td></td>
<td></td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>11</td>
<td>Signaturalgorithmus</td>
<td>DEG</td>
<td></td>
<td></td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>12</td>
<td>Schlüsselname</td>
<td>DEG</td>
<td></td>
<td></td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>13</td>
<td>Zertifikat</td>
<td>DEG</td>
<td></td>
<td></td>
<td>C</td>
<td>1</td>
<td>M: bei RAH-7, RDH-3, RDH-6 und RDH-7 in Ver- bindung mit mindestens ei- nem zu signierenden Ge- schäftsvorfall, der Sicher- heitsklasse 2, 3 oder 4 er- fordert.<br>O: bei RAH-9, RDH-1, RDH-5, RDH-8 und RDH-9 in Verbindung mit zu signie- renden Geschäftsvorfällen, die Sicherheitsklasse 1 bis 2 erfordern<br>N: bei DDV-1, RAH-10, RDH-2 und RDH-10</td>
</tr>
</table>


<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: B</td>
<td>Version: 3.0 - Final Version</td>
<td>Financial Transaction Services (FinTS) Dokument: Security - Sicherheitsverfahren HBCI</td>
</tr>
<tr>
<td>Seite: 50</td>
<td>Stand: 18.07.2013</td>
<td>Kapitel: Verfahrensbeschreibung<br>Abschnitt: Formate für Signatur und Verschlüsselung</td>
</tr>
</table>


## . Belegungsrichtlinien


### Sicherheitsfunktion, kodiert

Abhängig von Sicherheitsprofil und Schlüsseltyp und HBCI-Version ist fol-
gender Wert einzustellen:


<table>
<tr>
<th>Sicherheitsprofil</th>
<th>Schlüsseltyp</th>
<th>HBCI V2.x</th>
<th>FinTS V3.0</th>
</tr>
<tr>
<td>DDV-1</td>
<td>S</td>
<td>2</td>
<td>2</td>
</tr>
<tr>
<td>RAH-7</td>
<td>S</td>
<td>-</td>
<td>2</td>
</tr>
<tr>
<td>RAH-7</td>
<td>D</td>
<td>-</td>
<td>1</td>
</tr>
<tr>
<td>RAH-9</td>
<td>S</td>
<td>-</td>
<td>2</td>
</tr>
<tr>
<td>RAH-10</td>
<td>S</td>
<td>-</td>
<td>2</td>
</tr>
<tr>
<td>RDH-1</td>
<td>S</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td>RDH-2</td>
<td>S</td>
<td>-</td>
<td>2</td>
</tr>
<tr>
<td rowspan="2">RDH-3<br>RDH-3</td>
<td>S</td>
<td>-</td>
<td>2</td>
</tr>
<tr>
<td>D</td>
<td>-</td>
<td>1</td>
</tr>
<tr>
<td>RDH-5</td>
<td>S</td>
<td>-</td>
<td>2</td>
</tr>
<tr>
<td rowspan="2">RDH-6<br>RDH-6</td>
<td>S</td>
<td>-</td>
<td>2</td>
</tr>
<tr>
<td>D</td>
<td>-</td>
<td>1</td>
</tr>
<tr>
<td rowspan="2">RDH-7<br>RDH-7</td>
<td>S</td>
<td>-</td>
<td>2</td>
</tr>
<tr>
<td>D</td>
<td>-</td>
<td>1</td>
</tr>
<tr>
<td>RDH-8</td>
<td>S</td>
<td>-</td>
<td>2</td>
</tr>
<tr>
<td>RDH-9</td>
<td>S</td>
<td>-</td>
<td>2</td>
</tr>
<tr>
<td>RDH-10</td>
<td>S</td>
<td>-</td>
<td>2</td>
</tr>
</table>


RDH-1 bleibt 1 aus Kompatibilitätsgründen zu HBC V2.x.

Weitere Erläuterungen sind im Data Dictionary zu finden.


## Bereich der Sicherheitsapplikation, kodiert

Der einzig zugelassene Wert ist "1", d.h. SHM (nur Signaturkopf und HBCI-
Nutzdaten).


## Rolle des Sicherheitslieferanten, kodiert

Der Inhalt dieses Feldes sollte derzeit nicht ausgewertet werden. Optional
können aber die nachfolgenden Festlegungen angewendet werden, sofern
dies zwischen Kunde und Kreditinstitut zuvor vereinbart wurde:

<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th>Version:</th>
<th rowspan="2">Kapitel: B</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Security - Sicherheitsverfahren HBCI</td>
<td>3.0 - Final Version</td>
</tr>
<tr>
<td>Kapitel:</td>
<td>Verfahrensbeschreibung</td>
<td>Stand:</td>
<td>Seite:</td>
</tr>
<tr>
<td>Abschnitt:</td>
<td>Formate für Signatur und Verschlüsselung</td>
<td>18.07.2013</td>
<td>51</td>
</tr>
</table>


## 1. Dialoginitialisierung und -ende:

Die Rolle wird durch den Dialogführenden bestimmt. Es ist nur eine Sig-
natur erlaubt. Erlaubt ist nur der Wert ISS/wert115.


## 2. Auftragsnachricht:

Grundsätzlich gilt: Sobald die Rolle ,,WIT" verwendet wird, muss dieser
Benutzer mit der Benutzerkennung aus der Dialoginitialisierung arbeiten.
Auch der Benutzer ,,WIT" muss bankseitig entsprechend der Auftragsart
am Konto des Benutzers ,,ISS" berechtigt sein.

Die Reihenfolge der Signaturen ist beliebig.


<table>
<tr>
<th rowspan="2">Anzahl Signaturen</th>
<th colspan="3">Erlaubte Kombinationen</th>
</tr>
<tr>
<th>1. Signatur</th>
<th>2. Signatur</th>
<th>3. Signatur</th>
</tr>
<tr>
<td>1</td>
<td>ISS/wert1</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td rowspan="2">2</td>
<td>ISS/wert1</td>
<td>CON/beliebig</td>
<td>-</td>
</tr>
<tr>
<td>WIT/wert1</td>
<td>ISS/beliebig</td>
<td>-</td>
</tr>
<tr>
<td>3</td>
<td>WIT/wert1</td>
<td>ISS/beliebig</td>
<td>CON/beliebig</td>
</tr>
</table>


![](figures/65.1)


Auch bei Belegung dieses Feldes kann das Kunden-
produkt nicht davon ausgehen, dass das Feld kreditin-
stitutsseitig ausgewertet wird.


### Sicherheitsidentifikation, Details

Wenn eine Synchronisierung der Kundensystem-ID durchgeführt wird, ist als
Identifizierung der Partei ,0' einzustellen.


### Sicherheitsdatum und -uhrzeit

Als Bezeichner wird ,1" eingestellt, da es sich um einen Sicherheitszeitstem-
pel handelt.


### Zertifikat

Im Falle der Bankensignaturkarte ist je nach Signaturanforderung der Ge-
schäftsvorfälle entweder das Zertifikat C_X509.CH.DS oder das Zertifikat
C_X509.CH.AUT c/s[&KE] anzugeben.

<!-- PageFooter: 15 Die Notation gibt die Rolle gefolgt von der Benutzerkennung an. -->
<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: B</td>
<td>Version: 3.0 - Final Version</td>
<td>Financial Transaction Services (FinTS) Dokument: Security - Sicherheitsverfahren HBCI</td>
</tr>
<tr>
<td>Seite:<br>52</td>
<td>Stand: 18.07.2013</td>
<td>Kapitel: Verfahrensbeschreibung<br>Abschnitt: Formate für Signatur und Verschlüsselung</td>
</tr>
</table>


#### B.5.2 Signaturabschluss


##### . Beschreibung

Der Signaturabschluss stellt die Verbindung mit dem dazugehörigen Signaturkopf
her und enthält als "Validierungsresultat" die elektronische Signatur.

. Format


<table>
<tr>
<td>Name:</td>
<td>Signaturabschluss</td>
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
<td>HNSHA</td>
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
<td>Kunde/Kreditinstitut</td>
</tr>
</table>


<table>
<tr>
<th>Nr.</th>
<th>Name</th>
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
<td>DEG</td>
<td></td>
<td></td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>2</td>
<td>Sicherheitskontrollrefe- renz</td>
<td>DE</td>
<td>an</td>
<td>.. 14</td>
<td>M</td>
<td>1</td>
<td>&lt;&gt;0</td>
</tr>
<tr>
<td>3</td>
<td>Validierungsresultat</td>
<td>DE</td>
<td>bin</td>
<td>.512</td>
<td>C</td>
<td>1</td>
<td>M: bei HBCI N: bei PINTAN</td>
</tr>
<tr>
<td>4</td>
<td>Benutzerdefinierte Signa- tur</td>
<td>DEG</td>
<td></td>
<td></td>
<td>C</td>
<td>1</td>
<td>N: bei HBCI M/N/O bei anderen Verfah- ren</td>
</tr>
</table>


<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th>Version:</th>
<th>Kapitel:</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Security - Sicherheitsverfahren HBCI</td>
<td>3.0 - Final Version</td>
<td>B</td>
</tr>
<tr>
<td>Kapitel:</td>
<td>Verfahrensbeschreibung</td>
<td>Stand:</td>
<td>Seite:</td>
</tr>
<tr>
<td>Abschnitt:</td>
<td>Formate für Signatur und Verschlüsselung</td>
<td>18.07.2013</td>
<td>53</td>
</tr>
</table>


#### B.5.3 Verschlüsselungskopf


##### . Beschreibung

Der Verschlüsselungskopf enthält Informationen über die Art des Sicherheitsservice,
die Verschlüsselungsfunktion und die zu verwendenden Chiffrierschlüssel.

Zum Abgleich mit den in den BPD definierten Verschlüsselungsverfahren DDV bzw.
RAH und RDH wird das Feld ,,Bezeichner für Algorithmusparameter, Schlüssel“ in
I
der DEG „Verschlüsselungsalgorithmus“ herangezogen.


##### . Format


<table>
<tr>
<td>Name:</td>
<td>Verschlüsselungskopf</td>
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
<td>HNVSK</td>
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
<td>Kunde/Kreditinstitut</td>
</tr>
</table>


<table>
<tr>
<th>Nr.</th>
<th>Name</th>
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
<td>DEG</td>
<td></td>
<td></td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>2</td>
<td>Sicherheitsprofil</td>
<td>DEG</td>
<td></td>
<td></td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>3</td>
<td>Sicherheitsfunktion, ko- diert</td>
<td>DE</td>
<td>code</td>
<td>..3</td>
<td>M</td>
<td>1</td>
<td>4</td>
</tr>
<tr>
<td>4</td>
<td>Rolle des Sicherheits- lieferanten, kodiert</td>
<td>DE</td>
<td>code</td>
<td>..3</td>
<td>M</td>
<td>1</td>
<td>1, 4</td>
</tr>
<tr>
<td>5</td>
<td>Sicherheitsidentifikation, Details</td>
<td>DEG</td>
<td></td>
<td></td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>6</td>
<td>Sicherheitsdatum und -uhrzeit</td>
<td>DEG</td>
<td></td>
<td></td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>7</td>
<td>Verschlüsselungs- algorithmus</td>
<td>DEG</td>
<td></td>
<td></td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>8</td>
<td>Schlüsselname</td>
<td>DEG</td>
<td></td>
<td></td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>9</td>
<td>Komprimierungsfunktion</td>
<td>DE</td>
<td>code</td>
<td>..3</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>10</td>
<td>Zertifikat</td>
<td>DEG</td>
<td></td>
<td></td>
<td>C</td>
<td>1</td>
<td>O: kreditinstitutsseitig bei RAH-7, RAH-9, sowie RDH-1, RDH-2, RDH-3, RDH-5 RDH-6, RDH-7, RDH-8 und RDH-9 (vgl. B.3.1.3.2)<br>N: sonst</td>
</tr>
</table>


##### . Belegungsrichtlinien


###### Sicherheitsdatum und -uhrzeit

Als Bezeichner (DE Datum- und Zeitbezeichner, kodiert) wird ,1" (Sicher-
heitszeitstempel) eingestellt.


###### Zertifikat

Im Falle der Bankensignaturkarte ist das Zertifikat EF_C_X509.CH.KE anzu-
geben.

<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: B</td>
<td>Version: 3.0 - Final Version</td>
<td>Financial Transaction Services (FinTS) Dokument: Security - Sicherheitsverfahren HBCI</td>
</tr>
<tr>
<td>Seite:<br>54</td>
<td>Stand: 18.07.2013</td>
<td>Kapitel: Verfahrensbeschreibung<br>Abschnitt: Formate für Signatur und Verschlüsselung</td>
</tr>
</table>


#### B.5.4 Verschlüsselte Daten


##### . Beschreibung

Dieses Segment enthält die verschlüsselten (und komprimierten) Daten.

. Format


<table>
<tr>
<td>Name:</td>
<td>Verschlüsselte Daten</td>
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
<td>HNVSD</td>
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
<td>DEG</td>
<td></td>
<td></td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>2</td>
<td>Daten, verschlüsselt</td>
<td>DE</td>
<td>bin</td>
<td>..</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
</table>


<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th>Version:</th>
<th>Kapitel:</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Security - Sicherheitsverfahren HBCI</td>
<td>3.0 - Final Version</td>
<td>B</td>
</tr>
<tr>
<td>Kapitel:</td>
<td>Verfahrensbeschreibung</td>
<td>Stand:</td>
<td>Seite:</td>
</tr>
<tr>
<td>Abschnitt:</td>
<td>Key-Management</td>
<td>18.07.2013</td>
<td>55</td>
</tr>
</table>


# B.6 Key-Management


## B.6.1 Formate für Key-Management

Für die Schlüsseländerung, die Schlüsselverteilung sowie die Schlüsselsperrung
sind die nachfolgenden Segmente vorgesehen. Diese dürfen nur im Rahmen der
speziellen Key-Management-Nachrichten verwendet werden.


## B.6.1.1 Änderung eines öffentlichen Schlüssels


## . Beschreibung

Dieses Segment enthält einen neuen öffentlichen Schlüssel des Kunden.


## . Format


<table>
<tr>
<td>Name:</td>
<td>Schlüsseländerung</td>
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
<td>HKSAK</td>
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
<td>DEG</td>
<td></td>
<td></td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>2</td>
<td>Nachrichtenbeziehung, kodiert</td>
<td>DE</td>
<td>code</td>
<td>1</td>
<td>M</td>
<td>1</td>
<td>2</td>
</tr>
<tr>
<td>3</td>
<td>Bezeichner für Funktions- typ</td>
<td>DE</td>
<td>code</td>
<td>..3</td>
<td>M</td>
<td>1</td>
<td>112</td>
</tr>
<tr>
<td>4</td>
<td>Sicherheitsprofil</td>
<td>DEG</td>
<td></td>
<td></td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>5</td>
<td>Schlüsselname</td>
<td>DEG</td>
<td></td>
<td></td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>6</td>
<td>Öffentlicher Schlüssel</td>
<td>DEG</td>
<td></td>
<td></td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>7</td>
<td>Zertifikat</td>
<td>DEG</td>
<td></td>
<td></td>
<td>O</td>
<td>1</td>
<td></td>
</tr>
</table>


## . Belegungsrichtlinien


### Nachrichtenbeziehung, kodiert

Im Zusammenhang mit der Schlüsseländerung ist immer folgender Wert vor-
gesehen: "2" (Key-Management-Nachricht erwartet Antwort)


## Bezeichner für Funktionstyp

Im Zusammenhang mit der Schlüsseländerung ist folgender Wert vorgese-
hen: "112" (Certificate Replacement)


## Sicherheitsprofil

Es wird das den Schlüsseln entsprechende Sicherheitsprofil eingestellt.


## Schlüsselname

Es ist der Name des neuen öffentlichen Schlüssels des Kunden einzustellen.


## Zertifikat

Falls für den neuen öffentlichen Schlüssel ein Zertifikat verfügbar ist, kann es
dem Kreditinstitut auf diese Weise eingereicht werden.

<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: B</td>
<td>Version: 3.0 - Final Version</td>
<td>Financial Transaction Services (FinTS) Dokument: Security - Sicherheitsverfahren HBCI</td>
</tr>
<tr>
<td>Seite:<br>56</td>
<td>Stand: 18.07.2013</td>
<td>Kapitel: Verfahrensbeschreibung<br>Abschnitt: Key-Management</td>
</tr>
</table>


## B.6.1.2 Anforderung eines öffentlichen Schlüssels


# . Beschreibung

Dieses Segment enthält die Anfrage nach einem öffentlichen Schlüssel des Kredit-
instituts. Im Feld ,Sicherheitsprofil“ gibt der Kunde an, für welches Profil er die
Schlüssel anfordert. Das Segment wird entweder innerhalb der Dialoginitialisierung
(vgl. [Formals], Kapitel III.3.1) oder im Rahmen der erstmaligen Schlüsselanforde-
rung (vgl. Kapitel B.6.2.1) gesendet.


## . Format


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
<td>DEG</td>
<td></td>
<td></td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>2</td>
<td>Nachrichtenbeziehung, kodiert</td>
<td>DE</td>
<td>code</td>
<td>1</td>
<td>M</td>
<td>1</td>
<td>2</td>
</tr>
<tr>
<td>3</td>
<td>Bezeichner für Funktions- typ</td>
<td>DE</td>
<td>code</td>
<td>..3</td>
<td>M</td>
<td>1</td>
<td>124</td>
</tr>
<tr>
<td>4</td>
<td>Sicherheitsprofil</td>
<td>DEG</td>
<td></td>
<td></td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>5</td>
<td>Schlüsselname</td>
<td>DEG</td>
<td></td>
<td></td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>6</td>
<td>Zertifikat</td>
<td>DEG</td>
<td></td>
<td></td>
<td>O</td>
<td>1</td>
<td></td>
</tr>
</table>


## . Belegungsrichtlinien


### Nachrichtenbeziehung, kodiert

Im Zusammenhang mit der Anfrage nach einem öffentlichen Schlüssel ist
immer folgender Wert vorgesehen: "2" (Key-Management-Nachricht erwartet
Antwort)


### Bezeichner für Funktionstyp

Im Zusammenhang mit der Anfrage für einen öffentlichen Schlüssel ist fol-
gender Wert vorgesehen: "124" (Certificate Status Request)


### Schlüsselname

In den Schlüsselnamen ist die Schlüsselnummer und -version des Schlüs-
sels einzustellen, den das Kundenprodukt als aktuellen öffentlichen Schlüs-
sel des Kreditinstituts kennt. Falls dieser noch nicht vorliegt, ist in beide Fel-
der der Wert ,,999" einzustellen.

<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th>Version:</th>
<th rowspan="2">Kapitel: B</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Security - Sicherheitsverfahren HBCI</td>
<td>3.0 - Final Version</td>
</tr>
<tr>
<td>Kapitel:</td>
<td>Verfahrensbeschreibung</td>
<td>Stand:</td>
<td>Seite:</td>
</tr>
<tr>
<td>Abschnitt:</td>
<td>Key-Management</td>
<td>18.07.2013</td>
<td>57</td>
</tr>
</table>


#### B.6.1.3 Übermittlung eines öffentlichen Schlüssels


##### . Beschreibung

Dieses Segment wird zum einen innerhalb der Dialoginitialisierungsantwort (vgl.
[Formals], Kapitel III.3.2) an den Kunden übertragen, falls sich der öffentliche
Schlüssel des Kreditinstituts geändert hat. Es enthält dann jeweils einen öffentlichen
Schlüssel des Kreditinstituts.

Zum anderen wird das Segment im Rahmen der erstmaligen Anforderung der öf-
fentlichen Schlüssel des Kreditinstituts (vgl. Kapitel B.6.2.1) benötigt.


##### . Format


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
<td>DEG</td>
<td></td>
<td></td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>2</td>
<td>Nachrichtenbeziehung, kodiert</td>
<td>DE</td>
<td>code</td>
<td>1</td>
<td>M</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td>3</td>
<td>Austauschkontrollreferenz</td>
<td>DE</td>
<td>id</td>
<td>#</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>4</td>
<td>Nachrichtenreferenz- nummer</td>
<td>DE</td>
<td>num</td>
<td>..4</td>
<td>M</td>
<td>1</td>
<td>&gt;0</td>
</tr>
<tr>
<td>5</td>
<td>Bezeichner für Funktions- typ</td>
<td>DE</td>
<td>code</td>
<td>..3</td>
<td>M</td>
<td>1</td>
<td>224</td>
</tr>
<tr>
<td>6</td>
<td>Schlüsselname</td>
<td>DEG</td>
<td></td>
<td></td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>7</td>
<td>Öffentlicher Schlüssel</td>
<td>DEG</td>
<td></td>
<td></td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>8</td>
<td>Zertifikat</td>
<td>DEG</td>
<td></td>
<td></td>
<td>O</td>
<td>1</td>
<td></td>
</tr>
</table>


##### . Belegungsrichtlinien


###### Nachrichtenbeziehung, kodiert

Es ist folgender Wert vorgesehen: "1" (Key-Management-Nachricht ist Ant-
wort)


###### Austauschkontrollreferenz

Dialog-ID der Anfragenachricht des Kunden nach einem öffentlichen Schlüs-
sel (vgl. [Formals], Kapitel II.6.2).

Wird das Segment HIISA in einer Schlüsseldatei auf einem Medium abge-
legt, so kann dieses Feld mit dem Wert "0" belegt werden.


###### Nachrichtenreferenznummer

Nachrichtennummer der Anfragenachricht des Kunden nach einem öffentli-
chen Schlüssel (vgl. [Formals], Kapitel II.6.2).

Wird das Segment HIISA in einer Schlüsseldatei auf einem Medium abge-
legt, so kann dieses Feld mit einem beliebigen gültigen Wert belegt werden.

<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: B</td>
<td>Version: 3.0 - Final Version</td>
<td>Financial Transaction Services (FinTS) Dokument: Security - Sicherheitsverfahren HBCI</td>
</tr>
<tr>
<td>Seite:<br>58</td>
<td>Stand: 18.07.2013</td>
<td>Kapitel: Verfahrensbeschreibung<br>Abschnitt: Key-Management</td>
</tr>
</table>


# Bezeichner für Funktionstyp

Es ist folgender Wert vorgesehen: "224" (Certificate Status Notice)


## Schlüsselname

Der zurückgemeldete Schlüsselname enthält insbesondere die zugehörige
Schlüssel- und Versionsnummer, die das Kundenprodukt für die Referenzie-
rung des in der DEG „Öffentlicher Schlüssel“ übertragenen neuen öffentli-
chen Schlüssels verwendet.


## Öffentlicher Schlüssel

Diese Datenelementgruppe enthält den neuen öffentlichen Schlüssel des
Kreditinstitutes.

<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th>Version:</th>
<th rowspan="2">Kapitel: B</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Security - Sicherheitsverfahren HBCI</td>
<td>3.0 - Final Version</td>
</tr>
<tr>
<td>Kapitel:</td>
<td>Verfahrensbeschreibung</td>
<td>Stand:</td>
<td>Seite:</td>
</tr>
<tr>
<td>Abschnitt:</td>
<td>Key-Management</td>
<td>18.07.2013</td>
<td>59</td>
</tr>
</table>


### B.6.1.4 Schlüsselsperrung


#### . Beschreibung

Dieses Segment enthält die Anforderung für das Sperren eines Schlüssels.


<table>
<tr>
<td colspan="2">. Format</td>
</tr>
<tr>
<td>Name:</td>
<td>Schlüsselsperrung</td>
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
<td>HKSSP</td>
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
<td>DEG</td>
<td></td>
<td></td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>2</td>
<td>Nachrichtenbeziehung, kodiert</td>
<td>DE</td>
<td>code</td>
<td>1</td>
<td>M</td>
<td>1</td>
<td>2</td>
</tr>
<tr>
<td>3</td>
<td>Bezeichner für Funktions- typ</td>
<td>DE</td>
<td>code</td>
<td>..3</td>
<td>M</td>
<td>1</td>
<td>130</td>
</tr>
<tr>
<td>4</td>
<td>Sicherheitsprofil</td>
<td>DEG</td>
<td></td>
<td></td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>5</td>
<td>Schlüsselname</td>
<td>DEG</td>
<td></td>
<td></td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>6</td>
<td>Sperrenkennzeichen</td>
<td>DE</td>
<td>code</td>
<td>..3</td>
<td>M</td>
<td>1</td>
<td>1,501,999</td>
</tr>
<tr>
<td>7</td>
<td>Sicherheitsdatum und -uhrzeit</td>
<td>DEG</td>
<td></td>
<td></td>
<td>O</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>8</td>
<td>Zertifikat</td>
<td>DEG</td>
<td></td>
<td></td>
<td>O</td>
<td>1</td>
<td></td>
</tr>
</table>


#### . Belegungsrichtlinien


##### Nachrichtenbeziehung, kodiert

Im Zusammenhang mit der Schlüsselsperrung ist folgender Wert vorgese-
hen: "2" (Key-Management-Nachricht erwartet Antwort)


##### Bezeichner für Funktionstyp

Im Zusammenhang mit der Schlüsselsperrung ist folgender Wert vorgese-
hen: "130" (Certificate Revocation)


##### Sicherheitsprofil

Es wird das den Schlüsseln entsprechende Sicherheitsprofil eingestellt.


##### Schlüsselname

Es sind die Identifikationsmerkmale des zu sperrenden Signierschlüssels
einzustellen, unabhängig davon, dass grundsätzlich immer sowohl Signier-
als auch Chiffrierschlüssel gesperrt werden (s. Kap. B.8.1.4).


##### Sicherheitsdatum und -uhrzeit

Enthält optional Datum und Uhrzeit, ab welcher der Schlüssel nicht mehr gül-
tig ist. Als Bedeutung wird „6“ (für CRT, Certificate Revocation Time) einge-
stellt.

<!-- PageBreak -->


<table>
<tr>
<th>Kapitel: B</th>
<th>Version: 3.0 - Final Version</th>
<th>Financial Transaction Services (FinTS) Dokument: Security - Sicherheitsverfahren HBCI</th>
</tr>
<tr>
<td>Seite: 60</td>
<td>Stand: 18.07.2013</td>
<td>Kapitel: Verfahrensbeschreibung<br>Abschnitt: Key-Management</td>
</tr>
</table>


![](figures/74.1)


Es ist zu beachten, dass eine terminierte Sperre nicht von al-
len Kreditinstituten unterstützt wird. Das Kundenprodukt soll-
te den Kunden auf diesen Sachverhalt hinweisen.

<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th>Version:</th>
<th>Kapitel:</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Security - Sicherheitsverfahren HBCI</td>
<td>3.0 - Final Version</td>
<td>B</td>
</tr>
<tr>
<td>Kapitel:</td>
<td>Verfahrensbeschreibung</td>
<td>Stand:</td>
<td>Seite:</td>
</tr>
<tr>
<td>Abschnitt:</td>
<td>Key-Management</td>
<td>18.07.2013</td>
<td>61</td>
</tr>
</table>


### B.6.1.5 Bestätigung der Schlüsselsperrung


#### . Beschreibung

Dieses Segment enthält die Bestätigung für eine Schlüsselsperrung.


#### . Format


<table>
<tr>
<td>Name:</td>
<td>Bestätigung der Schlüsselsperrung</td>
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
<td>HISSP</td>
</tr>
<tr>
<td>Bezugssegment:</td>
<td>HKSSP</td>
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
<td>DEG</td>
<td></td>
<td></td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>2</td>
<td>Nachrichtenbeziehung, kodiert</td>
<td>DE</td>
<td>code</td>
<td>1</td>
<td>M</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td>3</td>
<td>Austauschkontrollreferenz</td>
<td>DE</td>
<td>id</td>
<td>#</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>4</td>
<td>Nachrichtenreferenz- nummer</td>
<td>DE</td>
<td>num</td>
<td>..4</td>
<td>M</td>
<td>1</td>
<td>&gt;0</td>
</tr>
<tr>
<td>5</td>
<td>Bezeichner für Funktions- typ</td>
<td>DE</td>
<td>code</td>
<td>..3</td>
<td>M</td>
<td>1</td>
<td>231</td>
</tr>
<tr>
<td>6</td>
<td>Schlüsselname</td>
<td>DEG</td>
<td></td>
<td></td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>7</td>
<td>Sperrenkennzeichen</td>
<td>DE</td>
<td>code</td>
<td>..3</td>
<td>M</td>
<td>1</td>
<td>1,501,999</td>
</tr>
<tr>
<td>8</td>
<td>Sicherheitsdatum und -uhrzeit</td>
<td>DEG</td>
<td></td>
<td></td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>9</td>
<td>Zertifikat</td>
<td>DEG</td>
<td></td>
<td></td>
<td>O</td>
<td>1</td>
<td></td>
</tr>
</table>


#### . Belegungsrichtlinien


## Nachrichtenbeziehung, kodiert

Im Zusammenhang mit der Bestätigung der Schlüsselsperrung ist folgender
Wert vorgesehen: "1" (Key-Management-Nachricht ist Antwort)


## Austauschkontrollreferenz

Dialog-ID der Sperranforderung des Kunden (vgl. [Formals], Kapitel II.6.2).


## Nachrichtenreferenznummer

Nachrichtennummer der Sperrenanforderung des Kunden (vgl. [Formals],
Kapitel II.6.2).


## Bezeichner für Funktionstyp

Im Zusammenhang mit der Bestätigung der Schlüsselsperrung ist folgender
Wert vorgesehen: "231" (Revocation Confirmation)


## Schlüsselname

Es sind die Identifikationsmerkmale des gesperrten Signierschlüssels einzu-
stellen, unabhängig davon, dass grundsätzlich immer sowohl Signier- als
auch Chiffrierschlüssel gesperrt werden (s. Kap. B.8.1.4).

<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: B</td>
<td>Version: 3.0 - Final Version</td>
<td>Financial Transaction Services (FinTS) Dokument: Security - Sicherheitsverfahren HBCI</td>
</tr>
<tr>
<td>Seite: 62</td>
<td>Stand: 18.07.2013</td>
<td>Kapitel: Verfahrensbeschreibung<br>Abschnitt: Key-Management</td>
</tr>
</table>


### Sicherheitsdatum und -uhrzeit

Enthält optional Datum und Uhrzeit, ab welcher der Schlüssel nicht mehr gül-
tig ist. Als Bedeutung wird „6“ (für CRT, Certificate Revocation Time) einge-
stellt.

<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th rowspan="2">Version: 3.0 - Final Version</th>
<th rowspan="2">Kapitel: B</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Security - Sicherheitsverfahren HBCI</td>
</tr>
<tr>
<td>Kapitel:</td>
<td>Verfahrensbeschreibung</td>
<td>Stand:</td>
<td>Seite:</td>
</tr>
<tr>
<td>Abschnitt:</td>
<td>Key-Management</td>
<td>18.07.2013</td>
<td>63</td>
</tr>
</table>


### B.6.2 Key-Management-Nachrichten

Aufträge des Key-Managements dürfen nur in den folgenden separaten Nachrichten
übertragen werden.

Hiervon abweichend wird der Auftrag „Anforderung eines öffentlichen Schlüssels
des Kreditinstituts" nicht als eigene Nachricht, sondern innerhalb der Dialoginitiali-
sierung übertragen.

Die Nachrichten für das Key-Management müssen zum Teil kryptographisch ge-
schützt werden. Alternativ können auch Offline-Sicherungsverfahren (z.B. Brief) zum
Einsatz kommen (vgl. Kapitel B.3.1.3).

Es sind folgende Key-Management-Nachrichten vorgesehen:

· Änderung eines öffentlichen Schlüssels des Kunden

. Erstmalige Anforderung der Schlüssel des Kreditinstituts

· Erstmalige Übermittlung der Schlüssel des Kunden

· Schlüsselsperrung durch den Kunden

Mit Ausnahme der Sperrnachricht sind alle Key-Management-Nachrichten nur bei
Einsatz des RAH- und RDH-Verfahrens möglich.

<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: B</td>
<td>Version: 3.0 - Final Version</td>
<td>Financial Transaction Services (FinTS) Dokument: Security - Sicherheitsverfahren HBCI</td>
</tr>
<tr>
<td>Seite: 64</td>
<td>Stand: 18.07.2013</td>
<td>Kapitel: Verfahrensbeschreibung<br>Abschnitt: Key-Management</td>
</tr>
</table>


#### B.6.2.1 Änderung eines öffentlichen Schlüssels des Kunden

Realisierung Bank:
verpflichtend

Realisierung Kunde: verpflichtend


##### a) Kundennachricht


###### . Beschreibung

Diese Nachricht ist nur bei Verwendung des RAH- bzw. RDH-Verfahrens möglich.
Der Nachricht muss eine Dialoginitialisierung vorausgehen. Der Auftrag muss mit
dem alten Signierschlüssel signiert werden.

Es muss unterschieden werden, ob die Schlüsseländerung auch das Sicherheitspro-
fil wechselt oder nicht.

Die folgenden Wechselmöglichkeiten bestehen, falls Sicherheitsprofilwechsel unter-
stützt sind:


Abbildung 16: Unterstützte Sicherheitsprofilwechsel RDH-1, RDH-2 und RDH-5

![RDH-1 RDH-2 Schlüssel- datei Schlüssel- datei RDH-1 Karte ohne Zertifikat RDH-5 Karte ohne Zertifikat](figures/78.1)


<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th>Version:</th>
<th rowspan="2">Kapitel: B</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Security - Sicherheitsverfahren HBCI</td>
<td>3.0 - Final Version</td>
</tr>
<tr>
<td>Kapitel:</td>
<td>Verfahrensbeschreibung</td>
<td>Stand:</td>
<td>Seite:</td>
</tr>
<tr>
<td>Abschnitt:</td>
<td>Key-Management</td>
<td>18.07.2013</td>
<td>65</td>
</tr>
</table>


Abbildung 17: Unterstützte Sicherheitsprofilwechsel RDH-1, RDH-2 RDH-5, RDH-9
und RDH-10

![RDH-1 Schlüssel- datei RDH-9 Karte ohne Zertifikat RDH-1 Karte ohne Zertifikat RDH-2 RDH-10 Schlüssel- datei Schlüssel- datei RDH-5 Karte ohne Zertifikat](figures/79.1)


Zusammengefasst ergeben sich folgende Wechselmöglichkeiten:

<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: B</td>
<td>Version: 3.0 - Final Version</td>
<td>Financial Transaction Services (FinTS) Dokument: Security - Sicherheitsverfahren HBCI</td>
</tr>
<tr>
<td>Seite:<br>66</td>
<td>Stand: 18.07.2013</td>
<td>Kapitel: Verfahrensbeschreibung<br>Abschnitt: Key-Management</td>
</tr>
</table>


<table>
<tr>
<td>Β.7<br>RDH-x / RAH-y (aktuelles Verfahren)</td>
<td>B.8 RDH-y / RAH-y (neues Verfahren)</td>
</tr>
<tr>
<td>RDH-9 Bankensignaturkarte ohne Zertifikat</td>
<td>RAH-9 Bankensignaturkarte ohne Zertifikat</td>
</tr>
<tr>
<td>RDH-10 Schlüsseldatei</td>
<td>RAH-10 Schlüsseldatei</td>
</tr>
<tr>
<td>RDH-10 Schlüsseldatei</td>
<td>RAH-9 Bankensignaturkarte ohne Zertifikat</td>
</tr>
<tr>
<td>RAH-10 Schlüsseldatei</td>
<td>RAH-9 Bankensignaturkarte ohne Zertifikat</td>
</tr>
<tr>
<td>RDH-1 Schlüsseldatei</td>
<td>RDH-2 Schlüsseldatei</td>
</tr>
<tr>
<td>RDH-1 Schlüsseldatei</td>
<td>RDH-5 Bankensignaturkarte ohne Zertifikat</td>
</tr>
<tr>
<td>RDH-1 Schlüsseldatei</td>
<td>RDH-9 Bankensignaturkarte ohne Zertifikat</td>
</tr>
<tr>
<td>RDH-1 Schlüsseldatei</td>
<td>RDH-10 Schlüsseldatei</td>
</tr>
<tr>
<td>RDH-1 Bankensignaturkarte ohne Zertifikat</td>
<td>RDH-5 Bankensignaturkarte ohne Zertifikat</td>
</tr>
<tr>
<td>RDH-1 Bankensignaturkarte ohne Zertifikat</td>
<td>RDH-9 Bankensignaturkarte_ohne Zertifikat</td>
</tr>
<tr>
<td>RDH-2 Schlüsseldatei</td>
<td>RDH-5 Bankensignaturkarte ohne Zertifikat</td>
</tr>
<tr>
<td>RDH-2 Schlüsseldatei</td>
<td>RDH-9 Bankensignaturkarte ohne Zertifikat</td>
</tr>
<tr>
<td>RDH-2 Schlüsseldatei</td>
<td>RDH-10 Schlüsseldatei</td>
</tr>
<tr>
<td>RDH-5 Bankensignaturkarte ohne Zertifikat</td>
<td>RDH-9 Bankensignaturkarte ohne Zertifikat</td>
</tr>
<tr>
<td>RDH-10 Schlüsseldatei</td>
<td>RDH-9 Bankensignaturkarte ohne Zertifikat</td>
</tr>
</table>


##### 1. ohne Wechsel des Sicherheitsprofils:

Nach der erfolgreichen Durchführung der Schlüsseländerung wird der vorher ak-
tuelle Schlüssel automatisch gesperrt. Es ist darauf zu achten, dass die Version
des neuen Schlüssels höher ist als die des alten Schlüssels.


##### 2. mit Wechsel des Sicherheitsprofils

(vgl. Abbildung 16 und Abbildung 17):

Bei einem Sicherheitsprofilwechsel muss der Kunde immer beide HKSAK-
Segmente einstellen. Nach der erfolgreichen Durchführung der Schlüsselände-
rung wird durch das Kreditinstitut mitgeteilt, ob der vorher aktuelle RAH-x bzw.
RDH-x-Schlüssel automatisch gesperrt wurde. Diese Nachricht wird mit den
RAH-x bzw. RDH-x-Schlüsseln abgesichert. Wurden die RAH-x bzw. RDH-x-
Schlüssel institutsseitig nicht gesperrt, wird der Dialog unter Absicherung der
RAH-x bzw. RDH-x-Schlüssel beendet. Es ist darauf zu achten, dass die Num-
mer der RDH-2-Schlüssel 2 ist, die Version kann mit 1 beginnen. Ab RDH-5 und
bei RAH-x sind Schlüsselnummer und -version vorgegeben.


![](figures/80.1)


Falls das Kreditinstitut nicht in der Lage ist, zwei Schlüsselpaare zu
einem Kunden gleichzeitig zu halten und somit die Endenachricht
mit den RAH-x bzw. RDH-x-Schlüsseln nicht mehr bedienen kann, ist
dies dem_Kundenprodukt durch den Rückmeldungscode 3250 mitzutei-
len. Das Kundenprodukt soll dann keine Endenachricht mehr senden und
den Bankdatensatz von der RAH-x bzw. RDH-x-Schlüsseldatei löschen.

<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th>Version:</th>
<th>Kapitel:</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Security - Sicherheitsverfahren HBCI</td>
<td>3.0 - Final Version</td>
<td>B</td>
</tr>
<tr>
<td>Kapitel:</td>
<td>Verfahrensbeschreibung</td>
<td>Stand:</td>
<td>Seite:</td>
</tr>
<tr>
<td>Abschnitt:</td>
<td>Key-Management</td>
<td>18.07.2013</td>
<td>67</td>
</tr>
</table>


Es empfiehlt sich, die RAH-x bzw. RDH-x-Schlüssel nach einem erfolgreichen Ab-
schluss des Dialoges durch einen Sperrdialog ungültig zu machen.


![](figures/81.1)


Falls der Kunde eine Schlüsseländerungsnachricht sendet, diese
aber aus kreditinstitutsinternen Verarbeitungsgründen nicht beant-
wortet wird, sollte das Kundenprodukt zunächst einen neuen Dialog
auf Basis eines der Schlüsselpaare aufbauen. Falls diese Nachricht
abgelehnt wird ist ein erneuter Versuch auf Basis eines anderen
Schlüsselpaares vorzunehmen. Aus der Reaktion des Kre-
ditinstituts ist für das Kundenprodukt ersichtlich, ob die Schlüssel-
änderung erfolgreich war oder wiederholt werden muss.

Da es nicht möglich ist, einen DS-Schlüssel, der ja eine natürliche
Person identifiziert, über die HBCI-Schlüsseländerung zu ändern,
dürften nur "1..2" HKSAK-Segmente eingestellt werden.


### B.8.1.1.1 Wechsel des Sicherheitsprofils ohne Schlüsselwechsel

Diese Situation tritt bei der Migration von RDH- nach gleichrangigen RAH-Verfahren
auf. Beim Übergang von gleichartigen Sicherheitsprofilen (z. B. RDH-9 auf RAH-9
oder RDH-10 auf RAH-10) muss zwar eine erneute Übermittlung der bestehenden
öffentlichen Schlüssel durch entsprechende HKSAK-Segmente erfolgen, diese die-
nen jedoch nur dazu, die Änderung des Sicherheitsprofils bzgl. des Verschlüsse-
lungsalgorithmus (RDH: 2-Key-Triple-DES nach RAH: AES-256) mitzuteilen. Die
Schlüsselpaare selbst bleiben unverändert, d. h. weder im Kundenprodukt noch im
Kreditinstitut werden Änderungen an den bestehenden Schlüsseln vorgenommen.

Beim Übergang von RDH- auf RAH-Verfahren ergeben sich folgende Möglichkeiten
des Schlüsselwechsels (RDH-10 auf RAH-9) bzw. des Wechsel des Verschlüsse-
lungsverfahrens von RDH auf RAH:


Abbildung 18: Unterstützte Sicherheitsprofilwechsel beim Übergang von RDH- auf
RAH-Verfahren

![Karte ohne Zertifikat RAH-9 Karte ohne Zertifikat RDH-10 RAH-10 Schlüssel- datei Schlüssel- datei](figures/81.2)


RDH-9

<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: B</td>
<td>Version: 3.0 - Final Version</td>
<td>Financial Transaction Services (FinTS) Dokument: Security - Sicherheitsverfahren HBCI</td>
</tr>
<tr>
<td>Seite:<br>68</td>
<td>Stand: 18.07.2013</td>
<td>Kapitel: Verfahrensbeschreibung<br>Abschnitt: Key-Management</td>
</tr>
</table>


Zum Verfahren s. Kap. B.3.1.3.4.


#### . Format


<table>
<tr>
<td>Name:</td>
<td>Änderung eines öffentlichen Schlüssels des Kunden</td>
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


<table>
<tr>
<th>Nr.</th>
<th>Name</th>
<th>Typ</th>
<th>Ken- nung</th>
<th>Sta- tus</th>
<th>An- zahl</th>
<th>Anmerkungen</th>
</tr>
<tr>
<td>1</td>
<td>Nachrichtenkopf</td>
<td>SEG</td>
<td>HNHBK</td>
<td>M</td>
<td>1</td>
<td>s. [Formals], Kap. II.5.1</td>
</tr>
<tr>
<td>2</td>
<td>Signaturkopf</td>
<td>SEG</td>
<td>HNSHK</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>3</td>
<td>Schlüsseländerung</td>
<td>SEG</td>
<td>HKSAK</td>
<td>M</td>
<td>1..3</td>
<td></td>
</tr>
<tr>
<td>4</td>
<td>Signaturabschluss</td>
<td>SEG</td>
<td>HNSHA</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>5</td>
<td>Nachrichtenabschluss</td>
<td>SEG</td>
<td>HNHBS</td>
<td>M</td>
<td>1</td>
<td>s. [Formals], Kap. II.5.2</td>
</tr>
</table>


#### . Belegungsrichtlinien

Der Kunde stellt entweder seinen neuen öffentlichen Signierschlüssel, seinen neuen
öffentlichen Chiffrierschlüssel oder beide Schlüssel ein.


#### a) Kreditinstitutsnachricht


##### . Format


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
<td>s. [Formals], Kap. II.8.1</td>
</tr>
</table>


##### ◆ Erläuterungen

Es werden keine Datensegmente zurückgemeldet.


##### ◆ Ausgewählte Beispiele für Rückmeldungscodes


<table>
<tr>
<td>Code</td>
<td>Beispiel</td>
</tr>
<tr>
<td>0020</td>
<td>Öffentlicher Schlüssel wurde geändert</td>
</tr>
<tr>
<td>3250</td>
<td>RDH-1-Schlüssel wurden gesperrt. Endenachricht nicht mehr möglich.</td>
</tr>
<tr>
<td>3260</td>
<td>RDH-1-Schlüssel weiterhin gültig. Schlüsselsperre wird empfohlen.</td>
</tr>
<tr>
<td>9210</td>
<td>Schlüsseländerung von RDH-1 auf RDH-2 zur Zeit nicht möglich</td>
</tr>
<tr>
<td>9010</td>
<td>Schlüsseländerung zur Zeit nicht möglich</td>
</tr>
<tr>
<td>9010</td>
<td>Sicherheitsverfahren unterstützt keine öffentlichen Schlüssel</td>
</tr>
<tr>
<td>9210</td>
<td>Eingereichter Schlüssel ist mit dem aktuellen Schlüssel identisch</td>
</tr>
</table>


Sender:

Kunde

<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th>Version:</th>
<th>Kapitel:</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Security - Sicherheitsverfahren HBCI</td>
<td>3.0 - Final Version</td>
<td>B</td>
</tr>
<tr>
<td>Kapitel:</td>
<td>Verfahrensbeschreibung</td>
<td>Stand:</td>
<td>Seite:</td>
</tr>
<tr>
<td>Abschnitt:</td>
<td>Key-Management</td>
<td>18.07.2013</td>
<td>69</td>
</tr>
</table>


### B.8.1.2 Erstmalige Anforderung der Schlüssel des Kreditinstituts

Mit Hilfe dieser Nachricht fordert der Kunde erstmalig den öffentlichen Signier- und
Chiffrierschlüssel des Kreditinstituts an. Gleichzeitig erhält er die aktuellen Bankpa-
rameterdaten, die er benötigt, um die unterstützten Verschlüsselungsverfahren des
Kreditinstituts in Erfahrung zu bringen. Mit Hilfe dieser Informationen wird der Kunde
in die Lage versetzt, beliebige Nachrichten zu verschlüsseln.

Realisierung Bank: optional

Realisierung Kunde: verpflichtend


### a) Kundennachricht


#### . Beschreibung

Diese Nachricht wird an Stelle einer Dialoginitialisierung gesendet. Es dürfen keine
Auftragsnachrichten folgen. Der Dialog ist vom Kunden nach Erhalt der Antwort-
nachricht mit einer Dialogendenachricht zu beendigen. Die Nachricht wird weder
signiert noch verschlüsselt.


#### . Format


<table>
<tr>
<td>Name:</td>
<td>Erstmalige Anforderung der Schlüssel des Kreditinstituts</td>
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
<th>Typ</th>
<th>Ken- nung</th>
<th>Sta- tus</th>
<th>An- zahl</th>
<th>Anmerkungen</th>
</tr>
<tr>
<td>1</td>
<td>Nachrichtenkopf</td>
<td>SEG</td>
<td>HNHBK</td>
<td>M</td>
<td>1</td>
<td>s. [Formals], Kap. II.5.1</td>
</tr>
<tr>
<td>2</td>
<td>Identifikation</td>
<td>SEG</td>
<td>HKIDN</td>
<td>M</td>
<td>1</td>
<td>s. [Formals], Kap. III.3.1.2</td>
</tr>
<tr>
<td>3</td>
<td>Verarbeitungsvorberei- tung</td>
<td>SEG</td>
<td>HKVVB</td>
<td>M</td>
<td>1</td>
<td>s. [Formals], Kap. III.3.1.3</td>
</tr>
<tr>
<td>4</td>
<td>Anforderung eines öffent- lichen Schlüssels</td>
<td>SEG</td>
<td>HKISA</td>
<td>M</td>
<td>3</td>
<td></td>
</tr>
<tr>
<td>5</td>
<td>Nachrichtenabschluss</td>
<td>SEG</td>
<td>HNHBS</td>
<td>M</td>
<td>1</td>
<td>s. [Formals],Kap. II.5.2</td>
</tr>
</table>


#### . Belegungsrichtlinien


#### Identifikation

Die Datenelemente des Segments sind wie beim anonymen Zugang zu bele-
gen (s. [Formals], Kap. III.5).


#### Verarbeitungsvorbereitung

Mit diesem Segment fordert der Kunde die Bankparameterdaten an.


#### Anforderung eines öffentlichen Schlüssels

Mit diesen Segmenten fordert der Kunde jeweils den öffentlichen Signier-
schlüssel und den öffentlichen Chiffrierschlüssel des Kreditinstituts an. Es
sind stets alle Schlüssel eines Sicherheitsprofils anzufordern, auch wenn das
Kreditinstitut nicht signiert.

In die DEG „Schlüsselname“ ist für die Benutzerkennung der Standardwert
'999' einzustellen. In der Rückmeldung wird dem Kunden die korrekte Benut-
zerkennung des Kreditinstituts mitgeteilt.

<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: B</td>
<td>Version: 3.0 - Final Version</td>
<td>Financial Transaction Services (FinTS) Dokument: Security - Sicherheitsverfahren HBCI</td>
</tr>
<tr>
<td>Seite:<br>70</td>
<td>Stand:<br>18.07.2013</td>
<td>Kapitel: Verfahrensbeschreibung<br>Abschnitt: Key-Management</td>
</tr>
</table>


![](figures/84.1)


Da bei der Erstinitialisierung noch keine BPD vorliegt, ist es
für das Kundenprodukt evtl. problematisch, zu ermitteln
welche Sicherheitsprofile das Kreditinstitut anbietet und -
wenn mehrere möglich sind - welches Profil für den Kunden
gilt. Falls dem Kunden diese Information nicht von seinem
Kreditinstitut mitgeteilt wurde, sollte das Kundenprodukt
versuchen, das Sicherheitsmedium zu lesen und daraus
das richtige Sicherheitsprofil zu erschließen.

Da ein Kreditinstitut über keinen D-Schlüssel verfügt bzw.
verfügen kann (Voraussetzung ist eine "natürliche Per-
son"), dürfen nur zwei HKISA-Segmente eingestellt wer-
den.


##### b) Kreditinstitutsnachricht

. Format


<table>
<tr>
<td>Name:</td>
<td>Erstmalige Übermittlung der Schlüssel des Kreditinstituts</td>
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
<th>Typ</th>
<th>Ken- nung</th>
<th>Sta- tus</th>
<th>An- zahl</th>
<th>Anmerkungen</th>
</tr>
<tr>
<td>1</td>
<td>Nachrichtenkopf</td>
<td>SEG</td>
<td>HNHBK</td>
<td>M</td>
<td>1</td>
<td>s. [Formals], Kap. II.5.1</td>
</tr>
<tr>
<td>2</td>
<td>Signaturkopf</td>
<td>SEG</td>
<td>HNSHK</td>
<td>O</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>3</td>
<td>Rückmeldungen zur Ge- samtnachricht</td>
<td>SEG</td>
<td>HIRMG</td>
<td>M</td>
<td>1</td>
<td>s. [Formals], Kap. II.7.2</td>
</tr>
<tr>
<td>4</td>
<td>Rückmeldungen zu Seg- menten</td>
<td>SEG</td>
<td>HIRMS</td>
<td>O</td>
<td>n</td>
<td>s. [Formals], Kap. II.7.3</td>
</tr>
<tr>
<td>5</td>
<td>Bankparameterdaten</td>
<td>SF</td>
<td>#</td>
<td>O</td>
<td>1</td>
<td>s. [Formals], Kap. III.3.2.2</td>
</tr>
<tr>
<td>6</td>
<td>Übermittlung eines öffent- lichen Schlüssels</td>
<td>SEG</td>
<td>HIISA</td>
<td>M</td>
<td>1..3</td>
<td></td>
</tr>
<tr>
<td>7</td>
<td>Kreditinstitutsmeldung</td>
<td>SEG</td>
<td>HIKIM</td>
<td>O</td>
<td>n</td>
<td>s. [Formals], Kap. III.3.2.5</td>
</tr>
<tr>
<td>8</td>
<td>Signaturabschluss</td>
<td>SEG</td>
<td>HNSHA</td>
<td>O</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>9</td>
<td>Nachrichtenabschluss</td>
<td>SEG</td>
<td>HNHBS</td>
<td>M</td>
<td>1</td>
<td>s. [Formals], Kap. II.5.2</td>
</tr>
</table>


### . Belegungsrichtlinien


#### Signaturkopf

Falls das Kreditinstitut einen Signierschlüssel besitzt, d.h. seine Nachrichten
grundsätzlich signiert, hat es auch diese Nachricht zu signieren, um die Au-
thentizität des Chiffrierschlüssels zu sichern (s.u.).


#### Übermittlung eines öffentlichen Schlüssels

In diesen Segmenten werden dem Kunden die öffentlichen Schlüssel des
Kreditinstituts mitgeteilt.

Falls das Kreditinstitut seine Nachrichten nicht signiert, erhält der Kunde nur
den öffentlichen Chiffrierschlüssel zurückgemeldet. Auf die Anforderung des
Signierschlüssels erhält er einen entsprechenden Rückmeldungscode der
Kategorie ,,Warnungen und Hinweise", der ihm anzeigt, dass das Kreditinsti-
tut seine Nachrichten nicht signiert.

<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th>Version:</th>
<th rowspan="2">Kapitel: B</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Security - Sicherheitsverfahren HBCI</td>
<td>3.0 - Final Version</td>
</tr>
<tr>
<td>Kapitel:</td>
<td>Verfahrensbeschreibung</td>
<td>Stand:</td>
<td>Seite:</td>
</tr>
<tr>
<td>Abschnitt:</td>
<td>Key-Management</td>
<td>18.07.2013</td>
<td>71</td>
</tr>
</table>


Da die Authentizität des Chiffrierschlüssels nicht gesichert ist, muss diese
Nachricht durch einen Ini-Brief an den Kunden mit dem Hashwert des Chiff-
rierschlüssels begleitet werden (s. Kap. B.3.1.3.2).

Falls das Kreditinstitut seine Nachrichten signiert, erhält der Kunde sowohl
den öffentlichen Chiffrier- als auch Signierschlüssel zurückgemeldet. Die Au-
thentizität des Chiffrierschlüssels ist dabei durch die Signatur gesichert. Die
Authentizität des Signierschlüssels ist jedoch nicht gesichert, da das Kun-
densystem die Echtheit der Signatur nicht prüfen kann. Daher muss in die-
sem Fall die Nachricht durch einen Ini-Brief mit dem Hashwert des Signier-
schlüssels begleitet werden.


## ◆ Ausgewählte Beispiele für Rückmeldungscodes


<table>
<tr>
<td>Code</td>
<td>Beispiel</td>
</tr>
<tr>
<td>0020</td>
<td>Auftrag ausgeführt</td>
</tr>
<tr>
<td>3310</td>
<td>Kein Schlüssel verfügbar, da Kreditinstitutsnachrichten nicht signiert werden</td>
</tr>
</table>


<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: B</td>
<td>Version: 3.0 - Final Version</td>
<td>Financial Transaction Services (FinTS) Dokument: Security - Sicherheitsverfahren HBCI</td>
</tr>
<tr>
<td>Seite:<br>72</td>
<td>Stand: 18.07.2013</td>
<td>Kapitel: Verfahrensbeschreibung<br>Abschnitt: Key-Management</td>
</tr>
</table>


### B.8.1.3 Erstmalige Übermittlung der Schlüssel des Kunden

Mit Hilfe dieser Nachricht übermittelt der Kunde erstmalig seinen öffentlichen Si-
gnier- und Chiffrierschlüssel an das Kreditinstitut („Erstinitialisierungsnachricht“).

Da der Absender des öffentlichen Schlüssels den Beweis erbringen muss, dass er
auch im Besitz des zugehörigen privaten Schlüssels ist, muss die Nachricht des
Kunden signiert sein.


![](figures/86.1)


Das Kreditinstitut darf eine Nachricht nicht ablehnen, nur weil für
den Kunden noch kein öffentlicher Schlüssel in der Schlüsselverwal-
tung existiert. Falls die normale Signaturprüfung aus diesem Grund
negativ verläuft, muss zunächst geprüft werden, ob es sich um eine
Erstinitialisierung handelt. In diesem Fall ist der öffentliche Schlüs-
sel aus der Erstinitialisierungsnachricht zu extrahieren und die Sig-
naturprüfung auf der Basis dieses Schlüssels erneut vorzunehmen.

Die Erstinitialisierungsnachricht des Kunden ist zu verschlüsseln, da die darin ent-
haltenen benutzerbezogenen Daten (Kunden-ID, Benutzerkennung) als vertraulich
einzustufen sind. Dies erfordert, dass sich der öffentliche Chiffrierschlüssel des Kre-
ditinstituts schon vor dem Senden der Erstinitialisierung im Besitz des Kunden be-
finden muss. Ferner muss dem Kunden das Verschlüsselungsverfahren bekannt
sein, das ihm in den Bankparameterdaten mitgeteilt wird. Um dem Kunden diese
Daten vorab zukommen zu lassen bieten sich folgende Lösungen an:

. Das Kreditinstitut sendet dem Kunden eine Schlüsseldatei zu, die die Schlüssel
und die aktuelle BPD enthält, wie in VI.3.1.3.2 beschrieben.

. Der Kunde sendet die Key-Management-Nachricht ,,Erstmalige Anforderung der
Schlüssel des Kreditinstituts“ (s. Kap. B.6.2.1). Diese Nachricht wird begleitet von
einem Ini-Brief.


![](figures/86.2)


Um die wiederholte Ausführung unberechtigter Initialisierungsversu-
che zu verhindern, sind kreditinstitutsseitig folgende Vorkehrungen
zu treffen:

· Die Benutzerkennung sollte bei Verwendung des RAH- bzw.
RDH-Verfahrens nicht durch benutzerindividuelle Merkmale (z.B.
Kontonummer) hergeleitet werden können.

· Eine erneute Erstinitialisierung ist nur zulässig, wenn zuvor eine
Sperrung der Schlüssel des Benutzers erfolgt ist. In allen ande-
ren Fällen ist eine erneute Erstinitialisierungsnachricht abzuleh-
nen.


![](figures/86.3)


Auf der Chipkarte können Kommunikationszugänge abgelegt wer-
den (s. Kap. C). Da pro Institut jedoch mehrere Kommunikationszu-
gänge gespeichert sein können (z.B. TCP/IP und HTTPS), muss ein
Kundenprodukt zunächst prüfen, ob für dieses Institut bereits die
Schlüssel eingereicht wurden, bevor eine erstmalige Übermittlung
der Schlüssel des Kunden durchgeführt wird. Für den Fall, dass das
Kundenprodukt die Schlüssel dennoch sendet, sollte das Institut die
Warnung 3330 „Schlüssel liegen bereits vor“ zurückmelden.

<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th rowspan="2">Version: 3.0 - Final Version</th>
<th rowspan="2">Kapitel: B</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Security - Sicherheitsverfahren HBCI</td>
</tr>
<tr>
<td>Kapitel:</td>
<td>Verfahrensbeschreibung</td>
<td>Stand:</td>
<td>Seite:</td>
</tr>
<tr>
<td>Abschnitt:</td>
<td>Key-Management</td>
<td>18.07.2013</td>
<td>73</td>
</tr>
</table>


<table>
<tr>
<td>Realisierung Bank:</td>
<td>verpflichtend</td>
</tr>
<tr>
<td>Realisierung Kunde:</td>
<td>verpflichtend</td>
</tr>
</table>


## a) Kundennachricht


### . Beschreibung

Diese Nachricht wird an Stelle einer Dialoginitialisierung gesendet. Es dürfen keine
Auftragsnachrichten folgen. Die Nachricht muss signiert und verschlüsselt werden.
Der Dialog ist vom Kunden nach Erhalt der Antwortnachricht mit einer Dialogen-
denachricht zu beendigen. Die Dialogendenachricht ist nicht zu signieren, da der
übermittelte Kundenschlüssel zu diesem Zeitpunkt i.d.R. noch nicht freigeschaltet
ist.


### . Format


<table>
<tr>
<td>Name:</td>
<td>Erstmalige Übermittlung der Schlüssel des Kunden</td>
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
<th>Typ</th>
<th>Ken- nung</th>
<th>Sta- tus</th>
<th>An- zahl</th>
<th>Anmerkungen</th>
</tr>
<tr>
<td>1</td>
<td>Nachrichtenkopf</td>
<td>SEG</td>
<td>HNHBK</td>
<td>M</td>
<td>1</td>
<td>s. [Formals], Kap. II.5.1</td>
</tr>
<tr>
<td>2</td>
<td>Signaturkopf</td>
<td>SEG</td>
<td>HNSHK</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>3</td>
<td>Identifikation</td>
<td>SEG</td>
<td>HKIDN</td>
<td>M</td>
<td>1</td>
<td>s. [Formals], Kap. III.3.1.2</td>
</tr>
<tr>
<td>4</td>
<td>Schlüsseländerung</td>
<td>SEG</td>
<td>HKSAK</td>
<td>M</td>
<td>2-3</td>
<td></td>
</tr>
<tr>
<td>5</td>
<td>Signaturabschluss</td>
<td>SEG</td>
<td>HNSHA</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>6</td>
<td>Nachrichtenabschluss</td>
<td>SEG</td>
<td>HNHBS</td>
<td>M</td>
<td>1</td>
<td>s. [Formals], Kap. II.5.2</td>
</tr>
</table>


## . Belegungsrichtlinien


### Identifikation

Der Benutzer hat die ihm zur Initialisierung mitgeteilten Daten einzustellen.
Wenn die Erstinitialisierung mit der alten Benutzerkennung durchgeführt
wird, ist - sofern noch vorhanden - die alte Kundensystem-ID anzugeben,
andernfalls ist als Kundensystem-ID der Wert ,0' anzugeben. Falls zu diesem
Zeitpunkt noch keine Synchronisierung durchgeführt wurde, ist als Kunden-
system-ID der Wert '0' einzustellen.


### Schlüsseländerung

Der Kunde stellt seine öffentlichen Schlüssel ein. Dies können Signier-, Chiff-
rier- oder Authentikationsschlüssel sein.

Die Authentizität des Chiffrierschlüssels ist dabei durch die Signatur gesi-
chert. Die Authentizität des Signierschlüssels ist jedoch nicht gesichert, da
das Kreditinstitut die Echtheit der Signatur nicht prüfen kann. Daher muss die
Nachricht durch einen Ini-Brief an das Kreditinstitut mit dem Hashwert des
Signierschlüssels begleitet werden (s. Kap. B.3.1.3.2).

<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: B</td>
<td>Version: 3.0 - Final Version</td>
<td>Financial Transaction Services (FinTS) Dokument: Security - Sicherheitsverfahren HBCI</td>
</tr>
<tr>
<td>Seite:<br>74</td>
<td>Stand: 18.07.2013</td>
<td>Kapitel: Verfahrensbeschreibung<br>Abschnitt: Key-Management</td>
</tr>
</table>


## b) Kreditinstitutsnachricht


### . Beschreibung


![](figures/88.1)


Die Ablehnung der Erstinitialisierungsnachricht darf aus sicherheits-
technischen Aspekten im Rahmen der Rückmeldungscodes nicht
inhaltlich begründet werden. Fehlermeldungen, die sich auf den
syntaktischen Aufbau der Nachricht bzw. der Segmente beziehen,
sind hiervon unberührt.


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
<td>s. [Formals], Kap. II.8.1</td>
</tr>
</table>


### ◆ Erläuterungen

Es werden keine Datensegmente zurückgemeldet.


### ◆ Ausgewählte Beispiele für Rückmeldungscodes


<table>
<tr>
<td>Code</td>
<td>Beispiel</td>
</tr>
<tr>
<td>0010</td>
<td>Öffentlicher Schlüssel wurde entgegengenommen</td>
</tr>
<tr>
<td>0020</td>
<td>Öffentlicher Schlüssel wurde freigeschaltet</td>
</tr>
<tr>
<td>0020</td>
<td>Kunde wurde freigeschaltet</td>
</tr>
<tr>
<td>9010</td>
<td>Auftrag abgelehnt</td>
</tr>
</table>


<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th>Version:</th>
<th>Kapitel:</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Security - Sicherheitsverfahren HBCI</td>
<td>3.0 - Final Version</td>
<td>B</td>
</tr>
<tr>
<td>Kapitel:</td>
<td>Verfahrensbeschreibung</td>
<td>Stand:</td>
<td>Seite:</td>
</tr>
<tr>
<td>Abschnitt:</td>
<td>Key-Management</td>
<td>18.07.2013</td>
<td>75</td>
</tr>
</table>


#### B.8.1.4 Schlüsselsperrung durch den Kunden

Diese Nachricht beschreibt die Anforderung zum Sperren der Schlüssel durch den
Kunden und die Bestätigung der Schlüsselsperrung durch das Kreditinstitut (vgl.
Kapitel B.3.2).

Realisierung Bank: verpflichtend

Realisierung Kunde: verpflichtend


## a) Kundennachricht


### . Beschreibung

Es werden immer alle Schlüssel gesperrt. Eine selektive Schlüsselsperrung (z.B.
nur Chiffrierschlüssel) ist gegenwärtig nicht zulässig.

Der Nachricht muss eine Dialoginitialisierung vorausgehen. Die Nachricht muss bei
Kompromittierung signiert sein. Es liegt in der Entscheidung des Kreditinstituts, ob
es auch nicht signierte (anonyme) Schlüsselsperrungen erlaubt (z.B. bei Verlust des
Sicherheitsmediums). Die Steuerung erfolgt in den Userparameterdaten über das
Feld „Anzahl benötigter Signaturen“. Die Nachricht darf maximal eine Signatur tra-
gen.

Bei Verlust des Sicherheitsmediums liegen dem Benutzer u.U. die zur Durchführung
der Sperrung erforderlichen Daten (Schlüsselnummer und -version) nicht vor. In
diesem Fall ist zur Referenzierung auf den aktuellen Schlüssel jeweils der Wert
'999' einzustellen. Es ist daher darauf zu achten, dass dieser Wert reserviert ist und
nicht im Rahmen der Versionszählung belegt wird.


![](figures/89.1)


Falls das Kreditinstitut unsignierte Sperrungen zulässt, muss dem
Benutzer darüber hinaus explizit seine Benutzerkennung mitgeteilt
werden. Beim RAH- bzw. RDH-Verfahren erfolgt dies im Rahmen
des Ini-Briefs. Beim DDV-Verfahren kann diese dem Benutzer bei
der Aushändigung der Chipkarte mitgeteilt werden.

Beim DDV-Verfahren wird der Dialog im Anschluss an die Sperrnachricht ungesi-
chert beendet, d.h. die Kreditinstitutsantwortnachricht sowie die Dialogbeendi-
gungsnachrichten werden weder signiert noch verschlüsselt.

Beim RAH- sowie RDH-Verfahren wird im Anschluss an die Sperrnachricht

. die Antwortnachricht sowie die Dialogendenachricht des Kreditinstituts nicht chif-
friert, aber signiert (sofern das Kreditinstitut grundsätzlich signiert) und

· die Dialogendenachricht des Kunden chiffriert, aber nicht signiert

Diese Verfahren gelten nur bei einer erfolgreichen Sperrung. Bei einer fehlgeschla-
genen Sperrung ist der Dialog gesichert zu Ende zu führen, da die Schlüssel des
Kunden weiterhin aktiv sind.

Beim RAH- und RDH-Verfahren muss der Kunde nach einer Schlüsselsperrung zur
Entsperrung eine erneute Erstinitialisierung durchführen.

<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: B</td>
<td>Version: 3.0 - Final Version</td>
<td>Financial Transaction Services (FinTS) Dokument: Security - Sicherheitsverfahren HBCI</td>
</tr>
<tr>
<td>Seite: 76</td>
<td>Stand: 18.07.2013</td>
<td>Kapitel: Verfahrensbeschreibung<br>Abschnitt: Key-Management</td>
</tr>
</table>


## . Format


<table>
<tr>
<td>Name:</td>
<td>Sperrung eines Schlüssels durch den Kunden</td>
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


<table>
<tr>
<th>Nr.</th>
<th>Name</th>
<th>Typ</th>
<th>Ken- nung</th>
<th>Sta- tus</th>
<th>An- zahl</th>
<th>Anmerkungen</th>
</tr>
<tr>
<td>1</td>
<td>Nachrichtenkopf</td>
<td>SEG</td>
<td>HNHBK</td>
<td>M</td>
<td>1</td>
<td>s. [Formals], Kap. II.5.1</td>
</tr>
<tr>
<td>2</td>
<td>Signaturkopf</td>
<td>SEG</td>
<td>HNSHK</td>
<td>O</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>3</td>
<td>Schlüsselsperrung</td>
<td>SEG</td>
<td>HKSSP</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>4</td>
<td>Signaturabschluss</td>
<td>SEG</td>
<td>HNSHA</td>
<td>O</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>5</td>
<td>Nachrichtenabschluss</td>
<td>SEG</td>
<td>HNHBS</td>
<td>M</td>
<td>1</td>
<td>s. [Formals], Kap. II.5.2</td>
</tr>
</table>


## . Belegungsrichtlinien


### Schlüsselsperrung

Dieses Segment enthält die Anforderung für die Schlüsselsperrung.

Eine selektive Schlüsselsperrung ist gegenwärtig nicht zulässig, d.h. es wer-
den immer alle Kundenschlüssel gleichzeitig gesperrt. In der DEG „Schlüs-
selname" sind die Merkmale des Signierschlüssels einzustellen (s. Kap.
Β.6.1.4).


## b) Kreditinstitutsnachricht


### . Format


<table>
<tr>
<td>Name:</td>
<td>Bestätigung der Schlüsselsperrung durch das Kreditinstitut</td>
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
<th>Typ</th>
<th>Ken- nung</th>
<th>Sta- tus</th>
<th>An- zahl</th>
<th>Anmerkungen</th>
</tr>
<tr>
<td>1</td>
<td>Nachrichtenkopf</td>
<td>SEG</td>
<td>HNHBK</td>
<td>M</td>
<td>1</td>
<td>s. [Formals], Kap. II.5.1</td>
</tr>
<tr>
<td>2</td>
<td>Signaturkopf</td>
<td>SEG</td>
<td>HNSHK</td>
<td>O</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>3</td>
<td>Rückmeldungen zur Ge- samtnachricht</td>
<td>SEG</td>
<td>HIRMG</td>
<td>M</td>
<td>1</td>
<td>s. [Formals], Kap. II.7.2</td>
</tr>
<tr>
<td>4</td>
<td>Rückmeldungen zu Seg- menten</td>
<td>SEG</td>
<td>HIRMS</td>
<td>O</td>
<td>n</td>
<td>s. [Formals], Kap. II.7.3</td>
</tr>
<tr>
<td>5</td>
<td>Bestätigung der Schlüs- selsperrung</td>
<td>SEG</td>
<td>HISSP</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>6</td>
<td>Signaturabschluss</td>
<td>SEG</td>
<td>HNSHA</td>
<td>O</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>7</td>
<td>Nachrichtenabschluss</td>
<td>SEG</td>
<td>HNHBS</td>
<td>M</td>
<td>1</td>
<td>s. [Formals], Kap. II.5.2</td>
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
<td>Schlüssel wurde erfolgreich gesperrt</td>
</tr>
<tr>
<td>9010</td>
<td>Schlüssel ist bereits gesperrt</td>
</tr>
<tr>
<td>9010</td>
<td>Terminierte Sperren werden nicht unterstützt</td>
</tr>
<tr>
<td>9210</td>
<td>Unbekanntes Sperrenkennzeichen</td>
</tr>
<tr>
<td>9210</td>
<td>Sperrdatum liegt zu weit in der Zukunft</td>
</tr>
</table>


Sender:

Kunde

<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th>Version:</th>
<th>Kapitel:</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Security - Sicherheitsverfahren HBCI</td>
<td>3.0 - Final Version</td>
<td>C</td>
</tr>
<tr>
<td>Kapitel:</td>
<td>Chipapplikationen</td>
<td>Stand:</td>
<td>Seite:</td>
</tr>
<tr>
<td>Abschnitt:</td>
<td>Chipapplikation für RAH / RDH</td>
<td>18.07.2013</td>
<td>77</td>
</tr>
</table>


# C. CHIPAPPLIKATIONEN


## C.1 Chipapplikation für RAH / RDH

Kapitel C.1.1 dient als Überblick für die Datenstrukturen und Zugriffsregeln der Chi-
papplikation "DF_NOTEPAD" für SECCOS-Chipkarten [SECCOS] bzw. [SECCOS-
6]. Die Spezifikation des DF_NOTEPAD selbst und die Terminalabläufe sind im Do-
kument [DF_NOTEPAD] enthalten.

Im Verlauf dieses Kapitels ist mit "Bankensignaturkarte" eine Chipkarte mit
SECCOS-Betriebssystem und Signaturanwendung gemeint, die u.U. auch die Note-
pad-Applikation aus Kap. C.1.1 enthält. Weitere Applikationen, wie z.B. die elektro-
nische Geldbörse, sind nicht notwendigerweise auf der Chipkarte enthalten. Ebenso
kann die Bankensignaturkarte mit oder ohne Zertifikat ausgeliefert werden.


## C.1.1 Applikation Notepad

Die Anwendung ,,Notepad" dient als ,Notizbuch" zur Aufnahme von Daten anderer
Anwendungen. Durch das Notizbuch wird somit ein mobiler Datenspeicher geschaf-
fen, in dem bestimmte anwendungs- bzw. kundenspezifische Parameter abgelegt
werden können, z.B. für die Bankverbindungsdaten in HBCI.

Wenn eine Anwendung auf die Karte zugreift, wird geprüft, ob auf der Chipkarte das
Notizbuch DF_NOTEPAD vorhanden ist. Falls ja werden die Daten ausgelesen, falls
nein, muss der Benutzer die Zugangsdaten selbst eingeben bzw. die Zugangsdaten
werden im Kundenprodukt selber verwaltet.

Im Datenspeicher EF_NOTEPAD kann jeder Record durch eine Anwendung belegt
werden. Die Unterscheidung der Zugehörigkeit bestimmter Dateninhalte erfolgt an
Hand der Tags eines Records:

. '00' bedeutet, dass der Record nicht belegt ist

. 'F0' bedeutet, dass der Record HBCI-Bankverbindungsdaten (HBCI-Parameter-
block) enthält.

. 'F1' bedeutet, dass der Record Bankverbindungsdaten analog dem DFÜ-
Abkommen enthält.

Weitere Kennungen sind für den späteren Gebrauch durch andere Anwendungen
vorgesehen (Tag 'F2' bis 'FE').

Somit können mehrere HBCI-Bankverbindungsdaten (im Sinne der Multibankfähig-
keit) in unterschiedlichen Records, jeweils mit Kennung/Tag 'F0' abgelegt werden.
Jede HBCI-Bankverbindung belegt dabei einen Record analog der im Folgenden
beschriebenen Struktur EF_NOTEPAD.


## C.1.2 EF_NOTEPAD

Bei dem EF_NOTEPAD handelt es sich um ein lineares EF mit einer variablen Re-
cordlänge, die aus technischen Gründen auf maximal 2391 Byte begrenzt ist. Es
dient der Ablage beliebiger Daten.

<!-- PageFooter: 1 Nach ISO 7816-4 ist eine APDU maximal 255 Bytes lang. Nach Abzug der Protokolldaten steht ei- ne netto Datenlänge von maximal 239 Byte zur Verfügung. -->
<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: C</td>
<td>Version: 3.0 - Final Version</td>
<td>Financial Transaction Services (FinTS) Dokument: Security - Sicherheitsverfahren HBCI</td>
</tr>
<tr>
<td>Seite:<br>78</td>
<td>Stand: 18.07.2013</td>
<td>Kapitel: Chipapplikationen<br>Abschnitt: Chipapplikation für RAH / RDH</td>
</tr>
</table>


Die HBCI Anwendung nutzt das EF_NOTEPAD zur Speicherung von Zugangsspezi-
fischen Daten, den HBCI-Parameterblöcken. So kann ein Online-Banking-
Kundenprodukt in einem HBCI-Parameterblock und damit in einem Record des
EF_NOTEPADs Informationen wie z.B. die HBCI-Benutzerkennung ablegen. Dar-
über hinaus können vom Kundenprodukt in einem separaten weiteren Record aber
auch (produktspezifische) Informationen zu Kundenpräferenzen und -einstellungen
(z.B. Sprache, Anzeigeparameter etc.) abgelegt werden.


![](figures/92.1)


Den Herstellern von Kundensystemen wird vorgeschlagen, beim
EF_NOTEPAD neben einer Länge von 239 Byte auch Karten mit
einer Maximallänge von nur 200 Byte zu unterstützen. Zur Ermitt-
lung der Maximallänge soll der Tag ,,82“ des Bereiches FCP ausge-
lesen werden.

Der Inhalt des Notepad kann im Wesentlichen nur nach vorhergehender, erfolgrei-
cher CSA-Passwort-Verifizierung gelesen und verändert werden. Somit ist der Inhalt
insbesondere vor unberechtigtem Auslesen geschützt (z.B. wenn die Kontonummer
als Bestandteil der Benutzerkennung gespeichert ist).

Das Auslesen der Records erfolgt über ein Read Record auf alle vorhandenen Re-
cords. Wird ein HBCI-Parameterblock gesucht so ist anschließend ein Vergleich
durchzuführen, ob der TAG des Records den Inhalt 'FO' enthält.

Alternativ können mit dem Kommando SEARCH RECORD mit dem Suchmuster 'F0'
für das erste Byte des Recordinhalts genau die für HBCI relevanten Records aus-
gelesen werden.


## ◆ FCP

Für das EF_NOTEPAD sind die folgenden FCP festzulegen:


<table>
<tr>
<th>Tag</th>
<th>Länge</th>
<th>Wert</th>
<th>Erläuterung</th>
</tr>
<tr>
<td>'62'</td>
<td>'1C'</td>
<td></td>
<td>Tag und Länge für FCP</td>
</tr>
<tr>
<td>'82'</td>
<td>'05'</td>
<td>'14 41 00 EF XX'</td>
<td>Datei-Deskriptor für lineares EF mit variabler Re- cordlänge bis zu 239 ('EF') Byte und XX Records</td>
</tr>
<tr>
<td>'83'</td>
<td>'02'</td>
<td>'A6 11'</td>
<td>Datei-ID des EF_NOTEPAD</td>
</tr>
<tr>
<td>'85'</td>
<td>'02'</td>
<td>'YY YY'</td>
<td>für Nutzdaten allokierter Speicherplatz in Byte (XX Records mal 239 Byte)2</td>
</tr>
<tr>
<td>'88'</td>
<td>'01'</td>
<td>'D0'</td>
<td>SFI '1A' für das EF_NOTEPAD</td>
</tr>
<tr>
<td>'A1'</td>
<td>'08'</td>
<td>'8B 06 00 30 01 04 02 05'</td>
<td>Zugriffsregel-Referenzen</td>
</tr>
</table>


Die maximale Anzahl der Records und deren maximale Länge wird bei der Produk-
tion der Karte festgelegt.

<!-- PageFooter: 2 Beispiel: für XX = '05' a 239 Byte ist ein Datenbereich von 1195 Byte anzulegen →YY YY = '04 AB'. -->
<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th>Version:</th>
<th>Kapitel:</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Security - Sicherheitsverfahren HBCI</td>
<td>3.0 - Final Version</td>
<td>C</td>
</tr>
<tr>
<td>Kapitel:</td>
<td>Chipapplikationen</td>
<td>Stand:</td>
<td>Seite:</td>
</tr>
<tr>
<td>Abschnitt:</td>
<td>Chipapplikation für RAH / RDH</td>
<td>18.07.2013</td>
<td>79</td>
</tr>
</table>


Im SE #1 durfen READ, SEARCH und UPDATE RECORD nur ausgeführt werden, wenn
zuvor eine Karteninhaberauthentikation mit dem globalen Passwort 3 (CSA-
Passwort) erfolgt ist. Der Returncode wird nicht MAC-gesichert (Zugriffsregeln im
Record 4 des EF_RULE).

Im SE #2 dürfen die Kommandos READ, SEARCH und UPDATE RECORD nur ausge-
führt werden, wenn sie mit Secure Messaging durchgeführt werden. Entweder ist
zuvor eine Karteninhaberauthentikation mit dem globalen Passwort 3 (CSA-
Passwort) erfolgt und die MAC-Bildung im Secure Messaging erfolgt für Kommando-
und Antwortnachricht mit dem Sessionkey SK2; oder (ohne vorherige Karteninha-
berauthentikation) die MAC-Bildung erfolgt für Kommando- und Antwortnachricht mit
dem KNotepad_Admin (Zugriffsregel im Record 5 des EF_RULE).

Im SE #2 darf das Kommando APPEND RECORD nur mit Secure Messaging durchge-
führt werden. Die MAC-Bildung erfolgt für Kommando- und Antwortnachricht mit
dem KNotepad_Admin.

Im SE #2 darf das Kommando SELECT FILE (EF) ohne Einhaltung von Zugriffsbedin-
gungen oder mit Secure Messaging durchgeführt werden. Die MAC-Bildung im
Secure Messaging erfolgt für Kommando- und Antwortnachricht mit dem Session-
key SK2.


## . Aufbau eines Records


<table>
<tr>
<th>POS</th>
<th>Länge</th>
<th>Wert</th>
<th>Erläuterung</th>
</tr>
<tr>
<td>1</td>
<td>1</td>
<td>'XX'</td>
<td>Tag</td>
</tr>
<tr>
<td>2</td>
<td>1 oder 2</td>
<td>'XX' oder '81 XX'</td>
<td>Länge (bei Längen über 127 Byte ist die Kodierung '81' 'xx' zu verwenden)</td>
</tr>
<tr>
<td>3</td>
<td>L</td>
<td>'XX..XX'</td>
<td>Nutzdaten</td>
</tr>
</table>


Als Tags werden festgelegt:


<table>
<tr>
<td>Byte 1</td>
<td>Bedeutung</td>
</tr>
<tr>
<td>'00'</td>
<td>freier Record</td>
</tr>
<tr>
<td>'F0'</td>
<td>Belegung mit HBCI-Parameterblock</td>
</tr>
<tr>
<td>'F1'-'FE'</td>
<td>RFU</td>
</tr>
</table>


Durch den Tag 'F0' wird ein Recordeintrag als HBCI-Parameterblock für die HBCI-
Anwendung gekennzeichnet. Für Belegungen der EF_NOTEPAD-Records durch
andere Anwendungen stehen die Tags 'F1' bis 'FE' zur Verfügung. Die Kennungen
werden durch den ZKA vergeben.

Initial werden alle Records mit '00..00' belegt und so als leere Records gekenn-
zeichnet.


## . Beispiel eines EF_NOTEPADs

In der folgenden Tabelle ist die beispielhafte Belegung eines EF_NOTEPAD mit 7
Records angegeben.

<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: C</td>
<td>Version: 3.0 - Final Version</td>
<td>Financial Transaction Services (FinTS) Dokument: Security - Sicherheitsverfahren HBCI</td>
</tr>
<tr>
<td>Seite: 80</td>
<td>Stand: 18.07.2013</td>
<td>Kapitel: Chipapplikationen<br>Abschnitt: Chipapplikation für RAH / RDH</td>
</tr>
</table>


<table>
<tr>
<th>Record</th>
<th>Eintrag</th>
<th>Erläuterung</th>
</tr>
<tr>
<td>1</td>
<td>'F0 XX…XX'</td>
<td>Erste HBCI-Bankverbindung</td>
</tr>
<tr>
<td>2</td>
<td>'F0 XX..XX'</td>
<td>Zweite HBCI-Bankverbindung</td>
</tr>
<tr>
<td>3</td>
<td>'F0 XX..XX'</td>
<td>Dritte HBCI-Bankverbindung</td>
</tr>
<tr>
<td>4</td>
<td>'00..00'</td>
<td>frei</td>
</tr>
<tr>
<td>5</td>
<td>'F1 XX..XX'</td>
<td>belegt durch Anwendung mit Kennung 'F1'</td>
</tr>
<tr>
<td>6</td>
<td>'00..00'</td>
<td>frei</td>
</tr>
<tr>
<td>7</td>
<td>'F0 XX…XX'</td>
<td>Vierte HBCI-Bankverbindung</td>
</tr>
</table>


## ◆ Umgang mit variablen Recordlängen

Durch die Definition des EF_NOTEPAD als lineares EF mit variabler Recordlänge
werden beim Lesen eines Records nur die tatsächlich vorhandenen Daten von der
Karte zurückgegeben.

Command APDU eines READ RECORD:


<table>
<tr>
<th>Byte</th>
<th>Wert</th>
<th>Erläuterung</th>
</tr>
<tr>
<td>1-2</td>
<td>'00 B2'</td>
<td>CLA, INS</td>
</tr>
<tr>
<td>3</td>
<td>'0X'</td>
<td>P1, Recordnummer X</td>
</tr>
<tr>
<td>4</td>
<td>'D4'</td>
<td>P2, Reference Control Byte</td>
</tr>
<tr>
<td>5</td>
<td>'00'</td>
<td>Le</td>
</tr>
</table>


Wenn das READ RECORD erfolgreich ausgeführt wird, gibt die Chipkarte eine Ant-
wortnachricht mit der folgenden Struktur zurück:


<table>
<tr>
<th>Byte</th>
<th>Länge</th>
<th>Wert</th>
<th>Erläuterung</th>
</tr>
<tr>
<td>1-L</td>
<td>L</td>
<td>'XX …XX'</td>
<td>Recordeintrag</td>
</tr>
<tr>
<td>(L+1)-(L+2)</td>
<td>2</td>
<td>'SW1 SW2'</td>
<td>Positiver Returncode SW1 SW2</td>
</tr>
</table>


Ein HBCI-Recordeintrag beginnt in diesem Fall mit dem Tag 'FO' und einem Län-
genbyte.

<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th>Version:</th>
<th>Kapitel:</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Security - Sicherheitsverfahren HBCI</td>
<td>3.0 - Final Version</td>
<td>C</td>
</tr>
<tr>
<td>Kapitel:</td>
<td>Chipapplikationen</td>
<td>Stand:</td>
<td>Seite:</td>
</tr>
<tr>
<td>Abschnitt:</td>
<td>Chipapplikation für RAH / RDH</td>
<td>18.07.2013</td>
<td>81</td>
</tr>
</table>


## C.1.2.1 Recordbelegung des EF_NOTEPAD mit einem HBCI-Parameterblock, Version 001

Bei Verwendung von SECCOS 6 muss mindestens die Version V002 des
EF_NOTEPAD eingesetzt werden.

<!-- PageBreak -->


<table>
<caption>Ein HBCI-Recordeintrag hat bei V001 folgenden prinzipiellen Aufbau:</caption>
<tr>
<td>Kapitel:</td>
<td>Version:</td>
<td>Financial Transaction Services (FinTS)</td>
</tr>
<tr>
<td>C</td>
<td>3.0 - Final Version</td>
<td>Dokument: Security - Sicherheitsverfahren HBCI</td>
</tr>
<tr>
<td>Seite:</td>
<td>Stand:</td>
<td>Kapitel: Chipapplikationen</td>
</tr>
<tr>
<td>82</td>
<td>18.07.2013</td>
<td>Abschnitt: Chipapplikation für RAH / RDH</td>
</tr>
</table>


<table>
<tr>
<th colspan="3">Tag</th>
<th>Länge (Byte)</th>
<th>Wert</th>
<th>For- mat</th>
<th>Sta tus</th>
<th>Erläuterung</th>
</tr>
<tr>
<td colspan="3">'F0'</td>
<td>Var. max 'EC'3</td>
<td></td>
<td></td>
<td></td>
<td>HBCI-Parameterblock</td>
</tr>
<tr>
<td colspan="2"></td>
<td>'CO'</td>
<td>'03'</td>
<td>'30' '30' '31'</td>
<td>3an</td>
<td>O</td>
<td>Version 001 des HBCI- Parameterblocks</td>
</tr>
<tr>
<td rowspan="5"></td>
<td colspan="2">'E1'</td>
<td>Var. max. '5B'</td>
<td></td>
<td></td>
<td>M</td>
<td>HBCI-Institutsparameterblock</td>
</tr>
<tr>
<td rowspan="4"></td>
<td>'C1'</td>
<td>'01'-'14'</td>
<td>Kreditinstituts- bezeichnung</td>
<td>..20an</td>
<td>O</td>
<td></td>
</tr>
<tr>
<td>'C2'</td>
<td>'03'</td>
<td>Länderkenn- zeichen</td>
<td>3an</td>
<td>M</td>
<td>ISO 3166 numerisch in 3 ASCII-Zeichen codiert</td>
</tr>
<tr>
<td>'C3'</td>
<td>'01'-'1E'</td>
<td>Kreditinstitutscode</td>
<td>..30an</td>
<td>M</td>
<td>in jeweils national bekannter Notation</td>
</tr>
<tr>
<td>'C4'</td>
<td>‘1B‘</td>
<td>Hashwert Instituts- schlüssel</td>
<td>27bin</td>
<td>O</td>
<td></td>
</tr>
<tr>
<td colspan="2"></td>
<td>'C5'</td>
<td>'01'</td>
<td>Schlüsselstatus</td>
<td>1bin</td>
<td>M</td>
<td>8 Statusflags</td>
</tr>
<tr>
<td></td>
<td colspan="2">‘E2‘</td>
<td>Var. max. '37'</td>
<td></td>
<td></td>
<td>M</td>
<td>HBCI-Kommunikations- parameterblock</td>
</tr>
<tr>
<td colspan="2" rowspan="2"></td>
<td>'C6'</td>
<td>'01'</td>
<td>Kommunikations- dienst</td>
<td>1n</td>
<td>M</td>
<td>2 = TCP/IP</td>
</tr>
<tr>
<td>'C7'</td>
<td>'01'-'32'</td>
<td>Kommunikations- adresse</td>
<td>..50an</td>
<td>M</td>
<td></td>
</tr>
<tr>
<td></td>
<td colspan="2">'E2'</td>
<td>Var. max. '37'</td>
<td></td>
<td></td>
<td>O</td>
<td>2. HBCI-Kommunikations- parameterblock</td>
</tr>
<tr>
<td colspan="2" rowspan="3"></td>
<td>'C6'</td>
<td>'01'</td>
<td>Kommunikations- dienst</td>
<td>1n</td>
<td>M</td>
<td>2 = TCP/IP</td>
</tr>
<tr>
<td>'C7'</td>
<td>'01'-'32'</td>
<td>Kommunikations- adresse</td>
<td>..50an</td>
<td>M</td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td rowspan="4"></td>
<td colspan="2">‘E3‘</td>
<td>Var. max. '54'</td>
<td></td>
<td></td>
<td>O</td>
<td>HBCI-Kundenparameterblock</td>
</tr>
<tr>
<td rowspan="3"></td>
<td>‘C8‘</td>
<td>'01'-'1E'</td>
<td>Benutzerkennung</td>
<td>..30an</td>
<td>M</td>
<td></td>
</tr>
<tr>
<td>'C9'</td>
<td>'01'-'1E'</td>
<td>Kunden-ID</td>
<td>.30an</td>
<td>O</td>
<td></td>
</tr>
<tr>
<td>'CA'</td>
<td>'0C' oder '12"</td>
<td>Info Inhaber- schlüssel</td>
<td>12an oder 18an</td>
<td>M</td>
<td>Schlüsselnummer und Schlüs- selversion jeweils für den Sig- nierschlüssel, den Chiffrier- schlüssels und optional für den Signaturschlüssel des Karten- inhabers</td>
</tr>
</table>


Die Längen der einzelnen Records werden wie folgt nach ASN.1 BER (Basic En-
coding Rules) kodiert:

<!-- PageFooter: 3 Nettodatenlänge ,EC'=236 Byte + 3 Byte Längenfeld ergibt die maximale Recordlänge von 239 Byte -->
<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th>Version:</th>
<th rowspan="2">Kapitel: C</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Security - Sicherheitsverfahren HBCI</td>
<td>3.0 - Final Version</td>
</tr>
<tr>
<td>Kapitel:</td>
<td>Chipapplikationen</td>
<td>Stand:</td>
<td>Seite:</td>
</tr>
<tr>
<td>Abschnitt:</td>
<td>Chipapplikation für RAH / RDH</td>
<td>18.07.2013</td>
<td>83</td>
</tr>
</table>


Längen 'XX', wobei 'XX' die hexadezimale Darstellung eines Wertes zwischen 0 und
127 ist, werden als 'XX' in ein Byte kodiert werden.

Längen 'XX', wobei 'XX' die hexadezimale Darstellung eines Wertes zwischen 128
und 255 ist, müssen als '81 XX' in zwei Byte kodiert werden

Ausnahme ist hier die Länge des TAG 'F0', dieser wird immer in der Form 'F0' '81
XX' kodiert.

Ist der Record länger als die tatsächliche ASN.1 Struktur so kann der überschüssige
Speicherplatz im Record mit '00' belegt (z.B. ASN.1 Struktur 170 Byte, Recordlänge
239 Byte → Filler 69 Byte mit '00'). Das Kundenprodukt soll nur die Nutzdaten über-
tragen,

<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: C</td>
<td>Version: 3.0 - Final Version</td>
<td>Financial Transaction Services (FinTS) Dokument: Security - Sicherheitsverfahren HBCI</td>
</tr>
<tr>
<td>Seite: 84</td>
<td>Stand: 18.07.2013</td>
<td>Kapitel: Chipapplikationen<br>Abschnitt: Chipapplikation für RAH / RDH</td>
</tr>
</table>


## C.1.2.2Recordbelegung des EF_NOTEPAD mit einem HBCI-Parameterblock, Version 002

Bei Verwendung von SECCOS 6 muss mindestens die Version V002 des
EF_NOTEPAD eingesetzt werden.

Ein HBCI-Recordeintrag hat bei V002 folgenden prinzipiellen Aufbau:


<table>
<tr>
<th colspan="3">Tag</th>
<th>Länge</th>
<th>Wert</th>
<th rowspan="2">For- mat</th>
<th rowspan="2">Sta tus</th>
<th rowspan="2">Erläuterung</th>
</tr>
<tr>
<th colspan="3"></th>
<th>(Byte)</th>
<th></th>
</tr>
<tr>
<td colspan="3">'F0'</td>
<td>Var. max 'EC'4</td>
<td></td>
<td></td>
<td></td>
<td>HBCI-Parameterblock</td>
</tr>
<tr>
<td colspan="2"></td>
<td>'C0'</td>
<td>'03'</td>
<td>'30' '30' '32'</td>
<td>3an</td>
<td>M</td>
<td>Version 002 des HBCI- Parameterblocks</td>
</tr>
<tr>
<td rowspan="7"></td>
<td colspan="2">'E1'</td>
<td>Var. max. '5B'</td>
<td></td>
<td></td>
<td>M</td>
<td>HBCI-Institutsparameterblock</td>
</tr>
<tr>
<td rowspan="5"></td>
<td>'C1'</td>
<td>'01'-'14'</td>
<td>Kreditinstituts- bezeichnung</td>
<td>..20an</td>
<td>O</td>
<td></td>
</tr>
<tr>
<td>'C2'</td>
<td>'03'</td>
<td>Länderkenn- zeichen</td>
<td>3an</td>
<td>M</td>
<td>ISO 3166 numerisch in 3 ASCII-Zeichen codiert</td>
</tr>
<tr>
<td>'C3'</td>
<td>'01'-'1E'</td>
<td>Kreditinstitutscode</td>
<td>..30an</td>
<td>M</td>
<td>in jeweils national bekannter Notation</td>
</tr>
<tr>
<td>'C4'</td>
<td>'27'</td>
<td>Hashwert Instituts- schlüssel</td>
<td>39bin</td>
<td>O</td>
<td></td>
</tr>
<tr>
<td>'C5'</td>
<td>'01'</td>
<td>Schlüsselstatus</td>
<td>1bin</td>
<td>M</td>
<td>8 Statusflags</td>
</tr>
<tr>
<td colspan="2">‘E2‘</td>
<td>Var. max. '37'</td>
<td></td>
<td></td>
<td>M</td>
<td>HBCI-Kommunikations- parameterblock</td>
</tr>
<tr>
<td colspan="2" rowspan="2"></td>
<td>‘C6‘</td>
<td>'01'</td>
<td>Kommunikations- dienst</td>
<td>1n</td>
<td>M</td>
<td>2 = TCP/IP</td>
</tr>
<tr>
<td>'C7'</td>
<td>'01'-'32'</td>
<td>Kommunikations- adresse</td>
<td>..50an</td>
<td>M</td>
<td></td>
</tr>
<tr>
<td></td>
<td colspan="2">'E2'</td>
<td>Var. max. '37'</td>
<td></td>
<td></td>
<td>O</td>
<td>2. HBCI-Kommunikations- parameterblock</td>
</tr>
<tr>
<td colspan="2" rowspan="2"></td>
<td>‘C6‘</td>
<td>'01'</td>
<td>Kommunikations- dienst</td>
<td>1n</td>
<td>M</td>
<td>2 = TCP/IP</td>
</tr>
<tr>
<td>‘C7‘</td>
<td>'01'-'32'</td>
<td>Kommunikations- adresse</td>
<td>..50an</td>
<td>M</td>
<td></td>
</tr>
<tr>
<td></td>
<td colspan="2">‘E3‘</td>
<td>Var. max. '54'</td>
<td></td>
<td></td>
<td>O</td>
<td>HBCI-Kundenparameterblock</td>
</tr>
<tr>
<td colspan="2" rowspan="3"></td>
<td>‘C8‘</td>
<td>'01'-'1E'</td>
<td>Benutzerkennung</td>
<td>..30an</td>
<td>M</td>
<td></td>
</tr>
<tr>
<td>'C9'</td>
<td>'01'-'1E'</td>
<td>Kunden-ID</td>
<td>..30an</td>
<td>O</td>
<td></td>
</tr>
<tr>
<td>'CA'</td>
<td>'0C' oder '12"</td>
<td>Info Inhaber- schlüssel</td>
<td>12an oder 18an</td>
<td>M</td>
<td>Schlüsselnummer und Schlüs- selversion jeweils für den Sig- nierschlüssel, den Chiffrier- schlüssels und optional für den Signaturschlüssel des Karten- inhabers</td>
</tr>
</table>

4 Nettodatenlänge ,EC'=236 Byte + 3 Byte Längenfeld ergibt die maximale Recordlänge von 239 Byte


<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th>Version:</th>
<th rowspan="2">Kapitel: C</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Security - Sicherheitsverfahren HBCI</td>
<td>3.0 - Final Version</td>
</tr>
<tr>
<td>Kapitel:</td>
<td>Chipapplikationen</td>
<td>Stand:</td>
<td>Seite:</td>
</tr>
<tr>
<td>Abschnitt:</td>
<td>Chipapplikation für RAH / RDH</td>
<td>18.07.2013</td>
<td>85</td>
</tr>
</table>


### C.1.2.2.1 Tag 'F0': HBCI-Parameterblock

Durch den Tag 'F0' wird ein Record mit HBCI-Parameterblock für die HBCI-
Anwendung gekennzeichnet. Für Belegungen der EF_NOTEPAD-Records durch
andere Anwendungen stehen die Tags 'F1' bis 'FE' zur Verfügung.

Ein HBCI-Parameterblock enthält in der angegebenen Reihenfolge:

· optional ein Versionskennzeichen

· genau einen HBCI-Institutsparameterblock mit Tag 'E1'

· genau einen HBCI-Kommunikationsparameterblöcke mit Tag 'E2'

· optional einen weiteren HBCI-Kommunikationsparameterblöcke mit Tag 'E25

· optional einen HBCI-Kundenparameterblock mit Tag 'E3'

Die maximale Länge des HBCI-Parameterblocks wird beschränkt durch die maxima-
le Recordlänge von 239 Byte6.


### C.1.2.2.2 Tag 'C0': HBCI-Version

In jedem 'F0' Record kann zur Kennzeichnung der Version des EF-NOTEPAD ein
Sub-Record (z. B 'C0' '03' '30' '30' '30') aufgenommen werden. Die Zählung der
Version beginnt bei 1. Ist kein Sub-Record 'C0' vorhanden, so bedeutet dieses, dass
die Belegung des EF-NOTEPAD gemäß der Version 1 erfolgt.

Anmerkung: In der vorhergehenden Version des Dokumentes wurde fälschlicher-
weise 'E0' als Tag verwendet. 'E0' kann für die erste HBCI-Version '000' weiter ver-
wendet werden. Seit der aktuellen HBCI-Version des EF_NOTEPAD wird durch-
gängig 'C0' verwendet.


### C.1.2.2.3 Tag 'E1': HBCI-Institutsparameterblock

Durch den Tag 'E1' wird der Block der institutsspezifischen Parameter gekenn-
zeichnet. Ein HBCI-Institutsparameterblock enthält in der angegebenen Reihenfol-
ge:

. optional eine Kreditinstitutsbezeichnung mit Tag 'C1', alphanumerisch mit bis zu
20 Zeichen

· genau ein Länderkennzeichen des kontoführenden Instituts mit Tag 'C2'. Ver-
wendet wird der numerische ISO 3166-Code als 3-stellige alphanumerische Zei-
chenkette (z.B. Deutschland = "280")

. genau eine Kreditinstitutskennung mit Tag 'C3', in einer jeweils national bekann-
ten Notation mit bis zu 30 Stellen. Für deutsche Kreditinstitute wird hier die 8-
stellige Bankleitzahl verwendet.

<!-- PageFooter: 5 Somit ist der erste HBCI-Kommunikationsparameterblock ist also verpflichtend, der zweite optional. -->
<!-- PageFooter: 6 In einer konkreten Umsetzung ist es nicht möglich einen HBCI-Parameterblock mit allen Felder in der maximalen Länge zu nutzen. Dabei würde die maximale Recordlänge von 239 Byte überschrit- ten. -->
<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: C</td>
<td>Version: 3.0 - Final Version</td>
<td>Financial Transaction Services (FinTS) Dokument: Security - Sicherheitsverfahren HBCI</td>
</tr>
<tr>
<td>Seite:<br>86</td>
<td>Stand: 18.07.2013</td>
<td>Kapitel: Chipapplikationen<br>Abschnitt: Chipapplikation für RAH / RDH</td>
</tr>
</table>


. V001: optional einen Hashwert des öffentlichen Signierschlüssels des Instituts
mit Tag 'C4', binär mit genau 27 Byte. Der Eintrag besteht aus

[3 Byte Schlüsselnummer | 3 Byte Schlüsselversion | 1 Byte Kennzeichen
Hashverfahren | 20 Byte Hashwert].

Als Kennzeichen für das Hashverfahren werden festgelegt:7

\- '02' = RIPEMD-160

Die Parameter Schlüsselnummer und Schlüsselversion des Institutsschlüssels
werden in je 3 Byte rechtsbündig mit führenden Nullen codiert (z.B. Schlüssel-
nummer 1 → die Bytefolge '30' '30' '31'.

. V002: optional einen Hashwert des öffentlichen Signierschlüssels des Instituts
mit Tag 'C4', binär mit genau 39 Byte für die Hashwertverfahren RIPEMD-160
und SHA-256. Das Verfahren ist abhängig vom Sicherheitsprofil zu wählen.

Der Eintrag besteht bei RIPEMD-160 aus

[3 Byte Schlüsselnummer | 3 Byte Schlüsselversion | 1 Byte Kennzeichen
Hashverfahren | 32 Byte Hashwert].

Der Hashwert ist hierbei folgendermaßen aufgebaut:
[12 Byte '00' | 20 Byte RIPEMD-160 Hashwert]

Der Eintrag besteht bei SHA-256 aus

[3 Byte Schlüsselnummer | 3 Byte Schlüsselversion | 1 Byte Kennzeichen
Hashverfahren | 32 Byte Hashwert].

Als Kennzeichen für das Hashverfahren werden festgelegt:

\- '02' = RIPEMD-160 für RDH-3 und RDH-5

\- '03' = SHA-256 für RAH-7, RAH-9 sowie RDH-6 bis RDH-9

Die Parameter Schlüsselnummer und Schlüsselversion des Institutsschlüssels
werden in je 3 Byte rechtsbündig mit führenden Nullen codiert (z.B. Schlüs-
selnummer 1 → die Bytefolge '30' '30' '31'.

• genau ein Schlüsselstatus mit Tag 'C5', binär von genau 1 Byte Länge. Der
Schlüsselstatus enthält acht Flags mit folgender Bedeutung:

<!-- PageFooter: 7 Aus folgenden Gründen wird nur ein fest zugeordnetes Hashverfahren verwendet: Generell könnte im Tag C4 jedes gültige Hashverfahren zum Einsatz kommen, wobei nur bei einer ZKA-Bankensignaturkarte mit zuvor aufgebrachtem Zertifikat im Grundsatz im Tag C4 beide Hash- verfahren denkbar sind. Sollte hierbei z. B. die automatische Hashwertprüfung fehlschlagen (z.B. weil das Institut zwischenzeitlich die Schlüssel geändert hat), so wird clientseitig auf das INI- Briefverfahren (und damit in V001 auf das Hashverfahren RIPEMD-160) gewechselt. Auch beim Aufbringen neuer zusätzlicher Bankverbindungen auf die Chipkarte wird das INI-Briefverfahren (und damit in V001 RIPEMD-160) verwendet. Bei ZKA-Bankensignaturkarten ohne Zertifikat wird der Eintrag neuer Bankverbindungen immer über das INI-Brief-Verfahren (und damit bei V001 über RIPEMD-160) abgesichert. -->
<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th>Version:</th>
<th>Kapitel:</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Security - Sicherheitsverfahren HBCI</td>
<td>3.0 - Final Version</td>
<td>C</td>
</tr>
<tr>
<td>Kapitel:</td>
<td>Chipapplikationen</td>
<td>Stand:</td>
<td>Seite:</td>
</tr>
<tr>
<td>Abschnitt:</td>
<td>Chipapplikation für RAH / RDH</td>
<td>18.07.2013</td>
<td>87</td>
</tr>
</table>


<table>
<tr>
<td>Bit1</td>
<td>Erstmalige Übermittlung der Kundenschlüssel notwendig</td>
<td>'1'b - Ja '0'b - Nein</td>
</tr>
<tr>
<td>Bit2</td>
<td>Institutsrechner erwartet Signaturen nach ISO9796 mit AnnexA</td>
<td>'1'b - Ja '0'b - Nein</td>
</tr>
<tr>
<td>Bit3</td>
<td>Institutsschlüssel validiert</td>
<td>'1'b - Ja '0'b - Nein</td>
</tr>
<tr>
<td>Bit4</td>
<td>Ausstehende Übermittlung des neuen öffentlichen Chiff- rierschlüssels des Kunden bei Schlüsseländerung8</td>
<td>'1'b - Ja '0'b - Nein</td>
</tr>
<tr>
<td>Bit5</td>
<td>Ausstehende Übermittlung des neuen öffentlichen Sig- nierschlüssels des Kunden bei Schlüsseländerung9</td>
<td>'1'b - Ja '0'b - Nein</td>
</tr>
<tr>
<td>Bit6</td>
<td>Schlüsselsperre mit Erfolg durchgeführt (Info, da termi- nierte Sperrung erst in der Zukunft wirksam werden kann)</td>
<td>'1'b - Ja '0'b - Nein</td>
</tr>
<tr>
<td>Bit7</td>
<td>Leitungsprobleme bei Übermittlung neuer Schlüssel</td>
<td>'1'b - Ja '0'b - Nein</td>
</tr>
<tr>
<td>Bit8</td>
<td>Reserviert</td>
<td>'0'b</td>
</tr>
</table>


Bei der Personalisierung muss als Initialisierungswert '01' aufgebracht werden.

Ein HBCI-Institutsparameterblock belegt inklusive der Tag- und Längenbytes somit
maximal 93 Byte.


### C.1.2.2.4 Tag 'E2': HBCI-Kommunikationsparameterblock

Durch das Tag 'E2' wird der Block der generellen Kommunikations-Parameter ge-
kennzeichnet. Ein HBCI-Kommunikationsparameterblock enthält in der angegebe-
nen Reihenfolge:

. genau einen Kommunikationsdienst mit Tag 'C6', 1 Stelle numerisch. Zurzeit de-
finiert ist der numerische Wert 2 (TCP/IP)

· genau eine Kommunikationsadresse mit Tag 'C7', alphanumerisch mit bis zu 50
Zeichen

Ein HBCI-Kommunikationsparameterblock belegt inklusive der Tag- und Längen-
bytes somit maximal 57 Byte.


### C.1.2.2.5 Tag 'E3': HBCI-Kundenparameterblock

Durch den Tag 'E3' wird der optional vorhandene Block der kundenspezifischen
Parameter gekennzeichnet. Ist der Block nicht vorhanden, so handelt es sich um ei-
ne im Rahmen der HBCI-Anwendung Bankensignaturkarte ohne Zertifikat. Ein
HBCI-Kundenparameterblock enthält in der angegebenen Reihenfolge:

· genau eine Benutzerkennung mit Tag 'C8', alphanumerisch mit bis zu 30 Zei-
chen

. optional eine Kunden-ID mit Tag 'C9', alphanumerisch mit bis zu 30 Zeichen

<!-- PageFooter: 8 Nicht zu belegen, da die ZKA-Bankensignaturkarte keinen Wechsel der Kundenschlüssel unter- stützt. -->
<!-- PageFooter: 9 Nicht zu belegen, da die ZKA-Bankensignaturkarte keinen Wechsel der Kundenschlüssel unter- stützt. -->
<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: C</td>
<td>Version: 3.0 - Final Version</td>
<td>Financial Transaction Services (FinTS) Dokument: Security - Sicherheitsverfahren HBCI</td>
</tr>
<tr>
<td>Seite: 88</td>
<td>Stand: 18.07.2013</td>
<td>Kapitel: Chipapplikationen<br>Abschnitt: Chipapplikation für RAH / RDH</td>
</tr>
</table>


• genau ein Info Inhaberschlüssel mit Tag 'CA', von genau 12 oder 18 numerischen
Zeichen.

Bei 12 Byte Länge des Blocks ist der Inhalt wie folgt definiert:

Schlüsselnummer Signierschlüssel [3n]
Schlüsselversion Signierschlüssel [3n]
Schlüsselnummer Chiffrierschlüssel [3n]
Schlüsselversion Chiffrierschlüssel [3n]

Bei 18 Byte Lange ist der Inhalt wie folgt definiert:

Schlüsselnummer Signierschlüssel [3n]
Schlüsselversion Signierschlüssel [3n]
Schlüsselnummer Chiffrierschlüssel [3n]
Schlüsselversion Chiffrierschlüssel [3n]
Schlüsselnummer Signaturschlüssel [3n]
Schlüsselversion Signaturschlüssel [3n]

Die Parameter Schlüsselnummer und Schlüsselversion werden in je 3 Byte nume-
risch rechtsbündig mit führenden Nullen angegeben. (z.B. Schlüsselnummer 1 →
"001" → die Bytefolge '30' '30' '31'.

Fehlen die Angaben für den Signaturschlüssel (CA Record der Länge 12 Byte) so
werden als Schlüsselnummer und Schlüsselversion des Signaturschlüssels die
Schlüsselnummer und Schlüsselversion des Signierschlüssels übernommen.

Fehlt der Teilrecord mit dem Tag 'CA' (nicht vorhandener Record E3 oder Record
CA oder fehlendes EF_NOTEPAD) und liegen somit weder für den Signierschlüssel
und den Chiffrierschlüssel noch für den Signaturschlüssel Schlüsselnummer und
Schlüsselversion vor so sind vom FinTS-Client die Schlüsselnummern und Schlüs-
selversionen aller Schlüssel nach folgenden Mechanismen vorzubesetzen.

Die Schlüsselnummer wird gemäß dem genutzten RAH- bzw. RDH-Verfahren be-
setzt. Die Schlüsselversion wird gängigerweise im ersten Ausgabejahr mit "001"
vorbesetzt und anschließend im jährlichen Turnus um 1 erhöht.


<table>
<tr>
<th>RDH Verfahren</th>
<th>Schlüsselnummer</th>
<th>Schlüsselversion</th>
</tr>
<tr>
<td>RDH3</td>
<td>"003" → '30' '30' 33'</td>
<td>"001" → '30' '30' '31'</td>
</tr>
<tr>
<td>RDH5</td>
<td>"005" → '30' '30' 35'</td>
<td>"001" → '30' '30' '31'</td>
</tr>
<tr>
<td>RDH6</td>
<td>"006" → '30' '30' 36'</td>
<td>"001" → '30' '30' '31'</td>
</tr>
<tr>
<td>RAH7, RDH7</td>
<td>"007" → '30' '30' 37'</td>
<td>"001" → '30' '30' '31'</td>
</tr>
<tr>
<td>RDH8</td>
<td>"008" → '30' '30' 38'</td>
<td>"001" → '30' '30' '31'</td>
</tr>
<tr>
<td>RAH9, RDH9</td>
<td>"009" → '30' '30' 39'</td>
<td>"001" → '30' '30' '31'</td>
</tr>
</table>


<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th>Version:</th>
<th>Kapitel:</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Security - Sicherheitsverfahren HBCI</td>
<td>3.0 - Final Version</td>
<td>C</td>
</tr>
<tr>
<td>Kapitel:</td>
<td>Chipapplikationen</td>
<td>Stand:</td>
<td>Seite:</td>
</tr>
<tr>
<td>Abschnitt:</td>
<td>Chipapplikation für RAH / RDH</td>
<td>18.07.2013</td>
<td>89</td>
</tr>
</table>


<table>
<tr>
<th>RDH Verfahren</th>
<th>Schlüsselnummer</th>
<th>Schlüsselversion</th>
</tr>
<tr>
<td>RAH10, RDH10</td>
<td>"010" → '30' '31' 30'</td>
<td>"001" → '30' '30' '31'</td>
</tr>
</table>


![](figures/103.1)


Über die Schlüsselnummer im EF_NOTEPAD kann das zu verwen-
dende Sicherheitsprofil ermittelt werden.

Wichtiger Hinweis:

Bei allen Verfahren ab RDH-3 müssen für die Schlüsselnummer die
entsprechenden Werte aus der obigen Tabelle verwendet werden.
Die Nutzung von Schlüsselnummer ,,001" ist nicht erlaubt.

Ein HBCI-Kundenparameterblock belegt inklusive der Tag- und Längenbytes somit
maximal 86 Byte.


## C.1.2.2.6 Beispiel

Beispiel für eine Recordbelegung für V001 (Tags und Längenbytes sind fett mar-
kiert)


<table>
<tr>
<td>Inhalt</td>
<td>Erläuterung</td>
</tr>
<tr>
<td>F0 81 76</td>
<td>HBCI-Parameterblock</td>
</tr>
<tr>
<td>E1 3D</td>
<td>Institutsparameterblock</td>
</tr>
<tr>
<td>C1 0C 54 45 53 54 49 4E 53 54 49 54 55 54</td>
<td>Institutsbezeichnung "TESTINSTITUT"</td>
</tr>
<tr>
<td>C2 03 32 38 30</td>
<td>Länderkennzeichen "280"</td>
</tr>
<tr>
<td>C3 08 31 32 33 34 35 36 37 38</td>
<td>BLZ 12345678</td>
</tr>
<tr>
<td>C4 1B 30 30 31 30 30 31 02 01 02<br>03 04 05 06 07 08 09 0A 0B<br>0C 0D 0E 0F 10 11 12 13 14</td>
<td>Schlüsselnummer 1, Schlüssel- version 1, Hashverfahren RIPEMD-160, Hashwert</td>
</tr>
<tr>
<td>C5 01 01</td>
<td>Schlüsselstatus '01'</td>
</tr>
<tr>
<td>E2 12</td>
<td>Kommunikationsparameterblock</td>
</tr>
<tr>
<td>C5 01 02</td>
<td>Kommunikationsdienst TCP/IP</td>
</tr>
<tr>
<td>C6 0D 31 39 32 2E 31 36 38 2E 31 31 2E 32 32</td>
<td>Kommunikationsadresse 192.168.11.22</td>
</tr>
<tr>
<td>E3 21</td>
<td>Kundenparameterblock</td>
</tr>
<tr>
<td>C8 0A 31 32 33 34 35 36 37 38 39 30</td>
<td>Benutzerkennung "1234567890"</td>
</tr>
<tr>
<td>C9 05 31 32 33 34 35</td>
<td>Kunden-ID "12345"</td>
</tr>
<tr>
<td>CA 0C 30 30 31 30 30 31 30 30 31 30 30 31</td>
<td>Info Inhaberschlüssel Schlüsselnummer SIG 1, Schlüsselversion SIG 1 Schlüsselnummer CHIF 1, Schlüsselversion CHIF 1</td>
</tr>
</table>


### C.1.2.2.7 Erreichen der maximalen Recordlänge

Bei Ausnutzung aller Maximallängen und Aufnahme aller optionalen Felder und Angabe
zweier Kommunikationsparameterblöcke und eines Kundenparameterblocks ergibt sich ein
maximaler Platzbedarf von 297 Byte. Dieser Platzbedarf ist aber in einem Record nicht ab-
bildbar. Normalerweise wird aber nur ein Kommunikationsparameterblock verwendet sowie

<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: C</td>
<td>Version: 3.0 - Final Version</td>
<td>Financial Transaction Services (FinTS) Dokument: Security - Sicherheitsverfahren HBCI</td>
</tr>
<tr>
<td>Seite: 90</td>
<td>Stand: 18.07.2013</td>
<td>Kapitel: Chipapplikationen<br>Abschnitt: Chipapplikation für RAH / RDH</td>
</tr>
</table>


selten alle Maximallängen ausgereizt, so dass meistens die maximale Recordlänge von 239
Byte genügt. Bei älteren bereits ausgegebenen Bankensignaturkarten ist nur eine maximale
Recordlänge von 200 Byte vorgesehen.

<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th>Version:</th>
<th rowspan="2">Kapitel: C</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Security - Sicherheitsverfahren HBCI</td>
<td>3.0 - Final Version</td>
</tr>
<tr>
<td>Kapitel:</td>
<td>Chipapplikationen</td>
<td>Stand:</td>
<td>Seite:</td>
</tr>
<tr>
<td>Abschnitt:</td>
<td>Chipapplikation für RAH / RDH</td>
<td>18.07.2013</td>
<td>91</td>
</tr>
</table>


## C.1.3 Terminalabläufe

Dieses Kapitel spezifiziert die Terminalabläufe im Umgang mit dem RAH- bzw.
RDH-Verfahren auf SECCOS-Chipkarten [SECCOS] bzw. [SECCOS-6]. Ein Online-
Banking-Kundenprodukt nutzt

• zur Verschlüsselung und Signierung von HBCI-Nachrichten die auf der Chipkarte
zur Verfügung stehende Signatur-Anwendung (DF_SIG, [ZKASIG]) und die durch
das Betriebssystem bereitgestellten Signatur-Funktionen,

· als Sequenzzähler (Signatur-ID) interne Bedienungszähler der Signatur-
Anwendung (siehe Kap. C.1.3.1),

• als Datenspeicher für die Zugangsdaten ein auf der Chipkarte optional vorhan-
denes DF_NOTEPAD ([DF_NOTEPAD], siehe Kap. C.1.1).

<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: C</td>
<td>Version: 3.0 - Final Version</td>
<td>Financial Transaction Services (FinTS) Dokument: Security - Sicherheitsverfahren HBCI</td>
</tr>
<tr>
<td>Seite:<br>92</td>
<td>Stand: 18.07.2013</td>
<td>Kapitel: Chipapplikationen<br>Abschnitt: Chipapplikation für RAH / RDH</td>
</tr>
</table>


### C.1.3.1 Verfahren zur Ermittlung der Sicherheitsreferenznummern

Auf der Bankensignaturkarte wird kein eigenständiger Sequenzzähler (wie das Ele-
ment EF_SEQ im HBCI DDV-Verfahren) verwaltet, sondern es werden jeweils chip-
karteninterne ,,Usage Counter" der beiden zur Signatur verwendeten Schlüssel
SK.CH.DS und SK.CH.AUT c/s herangezogen.

Für jedes Signaturschlüsselpaar wird ein separater Usage Counter verwaltet.Dieser
kann jeweils zwei, drei oder vier Byte lang sein.

Da die Usage Counter auf der Chipkarte dekrementiert werden, als Sicherheitsrefe-
renznummer (,Signatur-ID“) aber ein streng monoton aufsteigender Zähler gefordert
ist, wird die konkrete Sicherheitsreferenznummer nach folgendem Algorithmus er-
mittelt:

1\. Auslesen des 2 bis 4 Byte langen Usage Counter (UC) UCDs des Schlüssels
Sk.CH.DS bzw. UCAUT des Schlüssels Sk.CH.AUT c/s.

2\. Sei neg(UC) die bitweise logische Negation von UC. Dann ist die Sicherheitsrefe-
renznummer (SRN)

SRNDS = neg(UCDS)
SRNAUT = neg(UCAUT)

Die einzelnen Usage Counter haben folgende Wertebereiche:

von 0 bis 65.535
bei Länge(UC) = 2 Byte

von 0 bis 16.777.215
bei Länge(UC) = 3 Byte

von 0 bis 4.294.967.295
bei Länge(UC) = 4 Byte

Damit muss die Sicherheitsreferenznummer SRN über die entsprechenden Wer-
tebereiche verfügen und benötigt zur Darstellung ebenfalls mindestens 2, 3 oder 4
Byte.

Ein Wrap-Around bei Erreichen des jeweiligen Maximalwerts findet nicht statt, da
das Erreichen eines Usage Counter 0 den Schlüssel der Chipkarte für die weitere
Verwendung sperrt.

Beispiel:

UCDS = '00 0A' (dezimal 10) ⇒ SRNDS = neg(UCDS) = 'FF F5' (dezimal 65.525)

UCAUT = 'FA 1D' (dezimal 64.029) ⇒ SRNAUT = neg(UCAUT) = '05 E2'(dezimal 1506)

Dieser Algorithmus ist in der jeweiligen Anwendungssoftware zu realisieren.

<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th>Version:</th>
<th rowspan="2">Kapitel: C</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Security - Sicherheitsverfahren HBCI</td>
<td>3.0 - Final Version</td>
</tr>
<tr>
<td>Kapitel:</td>
<td>Chipapplikationen</td>
<td>Stand:</td>
<td>Seite:</td>
</tr>
<tr>
<td>Abschnitt:</td>
<td>Chipapplikation für RAH / RDH</td>
<td>18.07.2013</td>
<td>93</td>
</tr>
</table>


### C.1.3.2 Beschreibung der Terminalabläufe

Nachfolgend werden die Anwendungsabläufe aus Endgerätesicht an einem privaten
Signaturterminal [KT-KONZEPT] spezifiziert. Hierbei werden ausschließlich die
chipkartenbezogenen Aspekte berücksichtigt. Anwendungsbezogene Details sind
nicht Bestandteil dieser Spezifikation.

Um die Abläufe möglichst einfach beschreiben zu können, werden in der nachfol-
genden Beschreibung Befehle der ZKA-SIG-API [KT-SIG] verwendet. Hiermit ist je-
doch die Verwendung der ZKA-SIG-API für technische Implementierungen nicht
zwingend vorgeschrieben. Wird die ZKA-SIG-API nicht verwendet, so sind die in
[KT-SIG] angegebenen Abläufe zum Aufruf der KT-Kommandos zu berücksichtigen.

Die Anwendungsabläufe lassen sich auch auf öffentliche Signaturterminals (Ge-
schäftsterminals) erweitern. Zu beachten ist dabei insbesondere, dass in diesem
Fall zusätzlich eine

. Komponenten-Authentikation zwischen Chipkarte und Geschäftsterminal mit
Aushandlung eines Sessionkey-Paares (SK1, SK2) stattfindet;

· alle Befehle an die Chipkarte im Secure Messaging mit einem SK2-MAC durch-
geführt werden müssen.

Falls bei der Ausführung der Kommandos ein Fehler auftritt, bricht das Terminal den
Vorgang ab, es sei denn, es ist ein abweichendes Verhalten spezifiziert.


![](figures/107.1)


In den hier beschriebenen Abläufen ist das Kundenterminal durch
ein zka_sig_open (zu Beginn des Ablaufs „Signatur einleiten“) und
ein zka_sig_close (Am Ende des Ablaufs ,,Signatur beenden“) für
die gesamte Zeitdauer exklusiv für die Kundenanwendung reser-
viert.

Um zwischenzeitlich anderen Anwendungen die Möglichkeit zu ge-
ben, die Signaturdienste der Karte zu nutzen (z.B. für die Zeitdauer
der Nachrichtengenerierung), können die im Folgenden beschriebe-
nen Teilabläufe jeweils auch durch ein zka_sig_open und ein
zka_sig_close gekapselt werden. Dadurch wird die exklusive Re-
servierung des Kundenterminals aufgehoben, die internen Zwi-
schenwerte der ZKA-SIG-API (insbes. der Chipdaten) bleiben je-
doch erhalten. Erst durch Aufruf des
zka_sig_fini_signature_application im Ablauf ,,Signatur beenden“
werden die internen Zwischenwerte der ZKA-SIG-API gelöscht.


![](figures/107.2)


Zur Administration der Signaturkarten (z.B. Freischalten eines Zerti-
fikates, Rücksetzen des Fehlbedienungszählers) werden von den
Kreditinstituten bzw. den Kartenemittenten Softwarekomponenten
zur Verfügung gestellt werden, die in der privaten Kundenumgebung
zum Einsatz kommen sollen. In Kundenprodukten, die nicht von den
Kartenemittenten herausgegeben werden, sollen diese Administra-
tionsfunktionen nicht realisiert werden.

<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: C</td>
<td>Version: 3.0 - Final Version</td>
<td>Financial Transaction Services (FinTS) Dokument: Security - Sicherheitsverfahren HBCI</td>
</tr>
<tr>
<td>Seite:<br>94</td>
<td>Stand:<br>18.07.2013</td>
<td>Kapitel: Chipapplikationen<br>Abschnitt: Chipapplikation für RAH / RDH</td>
</tr>
</table>


![](figures/108.1)


Für die kreditinstitutsseitige Realisierung dieser Softwarekomponen-
ten hat der ZKA Anforderungen und Festlegungen formuliert, die bei
Bedarf über die jeweiligen Ansprechpartner der Standards erhältlich
sind.


#### C.1.3.2.1 Signatur einleiten


<table>
<tr>
<td colspan="2">Chipkarte</td>
<td></td>
<td colspan="2">Endgerät</td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td>M1</td>
<td>Aufruf der ZKA-SIG-API-Funktion zka_sig_open</td>
</tr>
<tr>
<td>R2</td>
<td>OK</td>
<td rowspan="4">←<br>→<br>←<br>→<br>← →<br>← →</td>
<td>M2</td>
<td>Aufruf der ZKA-SIG-API-Funktion zka_sig_init_signature_application</td>
</tr>
<tr>
<td>R3</td>
<td>OK</td>
<td>M3</td>
<td>Aufruf der ZKA-SIG-API-Funktion zka_sig_verify_CSA_password</td>
</tr>
<tr>
<td>R4</td>
<td>OK / ,File not found"</td>
<td>C4</td>
<td>SELECT FILE DF_NOTEPAD</td>
</tr>
<tr>
<td>R5</td>
<td>Bankverbindung</td>
<td>C5<br>A5</td>
<td>ggf. READ RECORD EF_NOTEPAD<br>Daten prüfen und speichern</td>
</tr>
</table>


## ◆ Erläuterung

1\. Die ZKA-SIG-API-Funktion zka_sig_open wird ausgeführt. Diese Funktion stellt
eine exklusive Verbindung zum Kundenterminal her.

2\. Die ZKA-SIG-API-Funktion zka_sig_init_signature_application wird ausgeführt.
Diese sorgt insbesondere für ein Reset der Karte und das Auslesen der relevan-
ten Basisinformationen der Karte.

3\. Die ZKA-SIG-API-Funktion zka_sig_verify_CSA_password wird ausgeführt. Die-
se Funktion liest das CSA-Passwort ein und führt eine Verifikation gegenüber der
Chipkarte durch.

4\. Die Applikation ,,Notepad" wird geöffnet, indem das ADF der Applikation,
DF_NOTEPAD durch das Terminal mittels des Kommandos SELECT FILE ausge-
wählt wird.


## . Command APDU


<table>
<tr>
<th>Byte</th>
<th>Wert</th>
<th>Erläuterung</th>
</tr>
<tr>
<td>1-2</td>
<td>'00 A4'</td>
<td>CLA, INS</td>
</tr>
<tr>
<td>3</td>
<td>'04'</td>
<td>P1, Selektion mit DF-Name</td>
</tr>
<tr>
<td>4</td>
<td>'0C'</td>
<td>P2, Keine Antwortdaten</td>
</tr>
<tr>
<td>5</td>
<td>'09'</td>
<td>Lc</td>
</tr>
<tr>
<td>6-14</td>
<td>'D2 76 00 00 25 4E 50 01 00'</td>
<td>AID der Notepad-Applikation</td>
</tr>
</table>


Wenn die Notepad-Applikation auf der Karte nicht vorhanden ist, wird der folgen-
de Schritt übersprungen. In diesem Fall müssen die Zugangsdaten von einer an-
deren Stelle gelesen oder vom Benutzer eingegeben werden.

<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th>Version:</th>
<th>Kapitel:</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Security - Sicherheitsverfahren HBCI</td>
<td>3.0 - Final Version</td>
<td>C</td>
</tr>
<tr>
<td>Kapitel:</td>
<td>Chipapplikationen</td>
<td>Stand:</td>
<td>Seite:</td>
</tr>
<tr>
<td>Abschnitt:</td>
<td>Chipapplikation für RAH / RDH</td>
<td>18.07.2013</td>
<td>95</td>
</tr>
</table>


4\. Das Terminal liest mittels READ RECORD sukzessive die Bankverbindungsdaten
in den Records des EF_NOTEPAD (SFI '1A'), bis der oder die "passenden" Ein-
träge gefunden wurden. Das Lesen von Einträgen ist erst nach erfolgreicher
CSA-Passwort-Verifikation (Schritt 2) möglich.


## . Command APDU


<table>
<tr>
<th>Byte</th>
<th>Wert</th>
<th>Erläuterung</th>
</tr>
<tr>
<td>1-2</td>
<td>'00 B2'</td>
<td>CLA, INS</td>
</tr>
<tr>
<td>3</td>
<td>'0X'</td>
<td>P1, Recordnummer X</td>
</tr>
<tr>
<td>4</td>
<td>'D4'</td>
<td>P2, Reference Control Byte</td>
</tr>
<tr>
<td>5</td>
<td>'00'</td>
<td>Le</td>
</tr>
</table>


Wenn das READ RECORD erfolgreich ausgeführt wird, gibt die Chipkarte eine Ant-
wortnachricht mit der folgenden Struktur zurück:


<table>
<tr>
<th>Byte</th>
<th>Länge</th>
<th>Wert</th>
<th>Erläuterung</th>
</tr>
<tr>
<td>1-2</td>
<td>2</td>
<td>'XX LL'</td>
<td>Kennung und Länge</td>
</tr>
<tr>
<td>3-LL</td>
<td>LL</td>
<td>'XX..XX'</td>
<td>Nutzdaten</td>
</tr>
<tr>
<td>(LL+1)- (LL+2)</td>
<td>2</td>
<td>'XX XX'</td>
<td>Positiver Returncode SW1 SW2</td>
</tr>
</table>


Ist die Kennung ungleich '00', so sind Parameterdaten gemäß Kap. C.1.1 enthalten.
Es werden alle weiteren Records gelesen, bis die Chipkarte das Ende der Datei
(keine weiteren Records) signalisiert.

Anstatt alle Records auszulesen und auf Übereinstimmung mit der Kennung zu
überprüfen, kann alternativ auch das Kommando SEARCH RECORD verwendet wer-
den, um mittels eines übergebenen Suchmusters vorab die "passenden" Record-
nummern in einem Schritt zu finden. Anschließend müssen dann nur diese Record-
nummern mittels READ RECORD ausgelesen werden.


## . Command APDU


<table>
<tr>
<th>Byte</th>
<th>Wert</th>
<th>Erläuterung</th>
</tr>
<tr>
<td>1-2</td>
<td>'00 A2'</td>
<td>CLA, INS für SEARCH RECORD</td>
</tr>
<tr>
<td>3</td>
<td>'01'</td>
<td>P1, Start mit Recordnummer 1</td>
</tr>
<tr>
<td>4</td>
<td>'D7'</td>
<td>P2, spezifische Suche im SFI '1A'</td>
</tr>
<tr>
<td>5</td>
<td>'04'</td>
<td>Lc</td>
</tr>
<tr>
<td>6</td>
<td>'04'</td>
<td>CTRLB</td>
</tr>
<tr>
<td>7</td>
<td>'00'</td>
<td>Offset Indicator Byte</td>
</tr>
<tr>
<td>8</td>
<td>'02'</td>
<td>Konfigurationsbyte</td>
</tr>
<tr>
<td>9</td>
<td>'FO'</td>
<td>Suchmuster</td>
</tr>
<tr>
<td>10</td>
<td>'00'</td>
<td>Le</td>
</tr>
</table>


Wenn das SEARCH RECORD erfolgreich ausgeführt wird, gibt die Chipkarte eine Ant-
wortnachricht mit der folgenden Struktur zurück:


<table>
<tr>
<th>Byte</th>
<th>Länge</th>
<th>Wert</th>
<th>Erläuterung</th>
</tr>
<tr>
<td>1-n</td>
<td>n</td>
<td>'XX XX'</td>
<td>Recordnummer(n)</td>
</tr>
<tr>
<td>n+1</td>
<td>1</td>
<td>'XX'</td>
<td>Statusbyte SW1</td>
</tr>
<tr>
<td>n+2</td>
<td>1</td>
<td>'XX'</td>
<td>Statusbyte SW2</td>
</tr>
</table>


Es können nun gezielt nur die in der Antwortnachricht angegebenen Records aus-
gelesen werden.

<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: C</td>
<td>Version: 3.0 - Final Version</td>
<td>Financial Transaction Services (FinTS) Dokument: Security - Sicherheitsverfahren HBCI</td>
</tr>
<tr>
<td>Seite:<br>96</td>
<td>Stand: 18.07.2013</td>
<td>Kapitel: Chipapplikationen<br>Abschnitt: Chipapplikation für RAH / RDH</td>
</tr>
</table>


### C.1.3.2.2 Nachrichten generieren

Dieser Teil des Gesamtablaufs ist nur insofern chipkartenrelevant, als (optional)
Bankverbindungsdaten, die für die Auftragsgenerierung benötigt werden, aus der
Chipkarte entnommen werden. Dies ist bereits im Schritt ,Signatur einleiten“ (Kap.
C.1.3.2.1) geschehen. Für die folgende Ablaufbeschreibung wird angenommen,
dass die Anwendung bereits Auftrags-Nachrichten generiert hat. Diese Nachrichten
müssen jetzt ggf. noch kryptographisch gesichert werden, d.h. es werden Segmente
für die elektronische(n) Signatur(en) und für die Verschlüsselung entsprechend den
jeweiligen Spezifikationen eingefügt.


#### C.1.3.2.3 Nachrichten signieren


##### C.1.3.2.3.1 Nachrichten signieren bei HBCI

Die folgenden Abläufe können im Falle von HBCI offline, d.h. außerhalb des Über-
tragungsdialogs vollzogen werden. Dies gilt für alle Nachrichten mit Ausnahme der
Dialoginitialisierung. Der Grund besteht darin, dass für die Absicherung aller Kredit-
institutsnachrichten der Schlüssel des Senders der Dialoginitialisierungsnachricht
erforderlich ist. Daher muss auch die Chipkarte des Senders während des gesam-
ten Dialogs im Endgerät stecken.

Die Abläufe für die Signatur der Dialoginitialisierungsnachricht sind grundsätzlich
identisch mit den im Folgenden beschriebenen Abläufen für die Signatur von Auf-
tragsnachrichten. Da aber für die Dialoginitialisierung anwendungsseitig noch weite-
re Chipkartendaten (Benutzerkennung, Dialog-ID, Kommunikationszugang etc.) be-
nötigt werden, wird der komplette Ablauf einschließlich der Signatur der Dialoginitia-
lisierung im Kap. C.1.3.2.6 "Übertragungsdialog" noch einmal beschrieben.


<table>
<tr>
<td colspan="2">Chipkarte</td>
<td></td>
<td colspan="2">Endgerät</td>
</tr>
<tr>
<td>R1</td>
<td>BZ</td>
<td>↑ ↓</td>
<td>M1</td>
<td>Sequenzzähler (Signatur-ID) ermitteln durch Aufruf der ZKA- SIG-API-Funktion zka_sig_read_key_usage_counter und an- schließende Invertierung des Rückgabewerts gemäß Abschnitt C.1.3.1)</td>
</tr>
<tr>
<td></td>
<td></td>
<td rowspan="2"></td>
<td>A2</td>
<td>Signaturkopf aufbauen und in HBCI-Nachricht einfügen</td>
</tr>
<tr>
<td></td>
<td></td>
<td>A3</td>
<td>Daten (Signaturkopf, HBCI-Nutzdaten) für Signatur bereitstellen</td>
</tr>
<tr>
<td></td>
<td></td>
<td rowspan="2">↑ ↓</td>
<td>M4</td>
<td>Signaturerstellung (siehe Kap. C.1.3.3.1)</td>
</tr>
<tr>
<td></td>
<td></td>
<td>A5</td>
<td>Signaturabschluss aufbauen und in HBCI-Nachricht einfügen</td>
</tr>
<tr>
<td></td>
<td></td>
<td rowspan="2"></td>
<td>A6</td>
<td>ggf. M1 bis A5 für weitere Nachrichten wiederholen</td>
</tr>
<tr>
<td></td>
<td></td>
<td>A7</td>
<td>signierte HBCI-Nachrichten zur Weiterverarbeitung speichern</td>
</tr>
</table>


## ◆ Erläuterung

1\. Der Sequenzzähler (Signatur-ID) wird durch Auslesen der Bedienungszähler der
Signaturanwendung und anschließende Berechnung ermittelt. Das Auslesen er-
folgt durch Aufruf der ZKA-SIG-API-Funktion zka_sig_read_key_usage_counter
mit der Parameterbelegung

. counter_type = '00' bei Verwendung des Sk.CH.DS, bzw.

. counter_type = '02' bei Verwendung des SK.CH.AUT c/S

Das Ergebnis BZ wird gemäß Kap. C.1.3.1 zu SZ = neg(BZ) invertiert und als
Sequenzzähler gespeichert.

<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th>Version:</th>
<th rowspan="2">Kapitel: C</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Security - Sicherheitsverfahren HBCI</td>
<td>3.0 - Final Version</td>
</tr>
<tr>
<td>Kapitel:</td>
<td>Chipapplikationen</td>
<td>Stand:</td>
<td>Seite:</td>
</tr>
<tr>
<td>Abschnitt:</td>
<td>Chipapplikation für RAH / RDH</td>
<td>18.07.2013</td>
<td>97</td>
</tr>
</table>


2\. Der Signaturkopf wird aufgebaut und in die HBCI-Nachricht eingefügt.

3\. Die Daten (Signaturkopf, HBCI-Nutzdaten) für die Signaturerstellung werden be-
reitgestellt.

4\. Die Signatur wird berechnet (siehe hierzu Kap. C.1.3.3).

5\. Der Signaturabschluss wird aufgebaut und in die HBCI-Nachricht eingefügt.

6\. Ggf. können die Schritte 1 bis 5 für weitere Nachrichten wiederholt werden.

7\. Die signierten HBCI-Nachrichten können zur Weiterverarbeitung gespeichert
werden.

Anmerkung: Für Mehrfachsignaturen wird jeweils die Abfolge „Signatur einleiten“ –
,Nachrichten signieren“ - ,Signatur beenden" wiederholt. Dies kann auch zu einem
späteren Zeitpunkt geschehen. Mehrfachsignaturen müssen jedoch abgeschlossen
sein, bevor die Verschlüsselung der Nachricht (Kap. C.1.3.2.4) durchgeführt wird.


### C.1.3.2.4 Nachrichten verschlüsseln


#### C.1.3.2.5 Nachrichten verschlüsseln bei RAH

Die Chipkarte ist bei der eigentlichen Nachrichtenverschlüsselung nicht involviert.
Die Software berechnet einen Einmalschlüssel, verschlüsselt das Dokument und
verschlüsselt den Einmalschlüssel zur Übertragung mit dem öffentlichen Key-
Encryption-Schlüssel PK.RECVINST.KE des empfangenden Kreditinstituts, welches
dem entsprechenden Zertifikat des Empfängers entnommen wurde10.

Allerdings wird die Chipkarte zur Berechnung von Zufallszahlen herangezogen, wel-
che den Einmalschlüssel bilden.

<!-- PageFooter: 10 [DIN-SIG4, Kapitel 6.10.1]: ,,If an enciphered document is sent, the card is not involved: the soft- ware computes the content encryption key, enciphers the document and finally enciphers the con- tent encryption key by applying the receiver's public key taken from the receiver's KE certificate." -->
<!-- PageBreak -->


<table>
<tr>
<td>Kapitel:<br>C</td>
<td>Version: 3.0 - Final Version</td>
<td>Financial Transaction Services (FinTS) Dokument: Security - Sicherheitsverfahren HBCI</td>
</tr>
<tr>
<td rowspan="2">Seite:<br>98</td>
<td rowspan="2">Stand:<br>18.07.2013</td>
<td>Kapitel: Chipapplikationen</td>
</tr>
<tr>
<td>Abschnitt:<br>Chipapplikation für RAH / RDH</td>
</tr>
</table>


<table>
<tr>
<th colspan="2">Chipkarte</th>
<th></th>
<th colspan="2">Endgerät</th>
</tr>
<tr>
<td></td>
<td></td>
<td rowspan="10">↓↑ ↓↑ ↓↑ ↓↑<br>![](figures/112.1)</td>
<td>A1</td>
<td>Daten (FinTS-Nutzdaten und ggf. Signatur) für die Verschlüsse- lung bereitstellen</td>
</tr>
<tr>
<td>R2</td>
<td>RND</td>
<td>C2<br>A2</td>
<td>Aufruf der ZKA-SIG-API-Funktion zka sig_get_challenge<br>RND als Einmalschlüssel-Fragment KSL speichern</td>
</tr>
<tr>
<td>R3</td>
<td>RND</td>
<td>C3<br>A3</td>
<td>Aufruf der ZKA-SIG-API-Funktion zka sig get challenge<br>RND als Einmalschlüssel-Fragment KSLR speichern</td>
</tr>
<tr>
<td>R4</td>
<td>RND</td>
<td>C4<br>A4</td>
<td>Aufruf der ZKA-SIG-API-Funktion zka sig get challenge<br>RND als Einmalschlüssel-Fragment KSRL speichern</td>
</tr>
<tr>
<td>R5</td>
<td>RND</td>
<td>C5<br>A5</td>
<td>Aufruf der ZKA-SIG-API-Funktion zka sig_get challenge<br>RND als Einmalschlüssel-Fragment KSRR speichern</td>
</tr>
<tr>
<td></td>
<td></td>
<td>A6</td>
<td>KSL, KS R, KSRL und KSRR zu KS konkatenieren und speichern</td>
</tr>
<tr>
<td></td>
<td></td>
<td>A7</td>
<td>Daten mit KS (symmetrisch) verschlüsseln</td>
</tr>
<tr>
<td></td>
<td></td>
<td>A8</td>
<td>KS mit PK.RECVINST.KE (asymmetrisch) verschlüsseln</td>
</tr>
<tr>
<td></td>
<td></td>
<td>A9</td>
<td>Verschlüsselungsdaten aufbauen und in FinTS-Nachricht einfü- gen</td>
</tr>
<tr>
<td></td>
<td></td>
<td>A10</td>
<td>Verschlüsselte Daten als Binärdaten in Verschlüsselungsdaten einfügen</td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td>A11</td>
<td>ggf. A1 bis A10 für weitere Nachrichten wiederholen</td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td>A12</td>
<td>Verschlüsselte und signierte FinTS-Nachrichten zur weiteren Be- arbeitung speichern</td>
</tr>
</table>


# Erläuterung

1\. Die Daten (FinTS-Nutzdaten und ggf. Signatur) für die Verschlüsselung werden be-
reitgestellt.

2\. Mit dem Aufruf der ZKA-SIG-API-Funktion zka sig get challenge lasst sich das
Terminal eine Zufallszahl von der HBCI-Karte geben.

Wenn das Kommando erfolgreich ausgeführt wurde, gibt die HBCI-Karte eine 8 Byte
lange Zufallszahl als Antwortdatum aus, die als Einmalschlüssel-Fragment KSLL ge-
speichert wird.

3\. Mit dem Aufruf der ZKA-SIG-API-Funktion zka sig get challenge lasst sich das
Terminal eine zweite Zufallszahl von der HBCI-Karte geben, die als Einmalschlüssel-
Fragment KSLR gespeichert wird.

4\. Mit dem Aufruf der ZKA-SIG-API-Funktion zka sig get challenge lasst sich das
Terminal eine dritte Zufallszahl von der HBCI-Karte geben, die als Einmalschlüssel-
Fragment KSRL gespeichert wird.

5\. Mit dem Aufruf der ZKA-SIG-API-Funktion zka sig get challenge lasst sich das
Terminal eine vierte Zufallszahl von der HBCI-Karte geben, die als Einmalschlüssel-
Fragment KSLL gespeichert wird.

6\. KSLL, KSLR, KSRL, und KSRR, werden zu KS konkateniert und gespeichert.

7\. Die zu übertragenden Daten werden mit KS symmetrisch verschlüsselt (AES CBC-
Mode, IV=0, ZKA-Padding).

8\. Der Einmalschlüssel KS wird linksbundig mit Nullbits auf die Schlussellänge aufge-
füllt und anschließend mit dem öffentlichen Key-Encryption-Schlüssel

<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th>Version:</th>
<th>Kapitel:</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Security - Sicherheitsverfahren HBCI</td>
<td>3.0 - Final Version</td>
<td>C</td>
</tr>
<tr>
<td>Kapitel:</td>
<td>Chipapplikationen</td>
<td>Stand:</td>
<td>Seite:</td>
</tr>
<tr>
<td>Abschnitt:</td>
<td>Chipapplikation für RAH / RDH</td>
<td>18.07.2013</td>
<td>99</td>
</tr>
</table>


PK.RECVINST.KE des empfangenden Instituts, welches dem entsprechenden Zertifikat
des Empfängers entnommen wurde, verschlusselt. Das Ergebnis wird mit fuhrenden
Nullbits auf die Schlüssellänge erweitert.

9\. Die Verschlüsselungsdaten werden aufgebaut und in die FinTS-Nachricht eingefügt.

10\. Die verschlüsselten Daten als Binärdaten in die Verschlüsselungsdaten eingefügt.

11\. Ggf. werden die Schritte 1 bis 10 für weitere Nachrichten wiederholt.

12\. Die verschlüsselten und signierten FinTS-Nachrichten werden zur weiteren Bearbei-
tung gespeichert.


## C.1.3.2.5.1 Nachrichten verschlüsseln bei DDV und RDH

Die Chipkarte ist bei der eigentlichen Nachrichtenverschlüsselung nicht involviert.
Die Software berechnet einen Nachrichtenschlüssel, verschlüsselt das Dokument
und verschlüsselt den Nachrichtenschlüssel zur Übertragung mit dem öffentlichen
Key-Encryption-Schlüssel PK.RECVINST.KE des empfangenden Instituts, welches der
übermittelten Kreditinstitutsnachricht entnommen wurde11.

Allerdings wird die Chipkarte zur Berechnung von Zufallszahlen herangezogen, wel-
che den Nachrichtenschlüssel bilden.


<table>
<tr>
<th colspan="2">Chipkarte</th>
<th></th>
<th colspan="2">Endgerät</th>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td>A1</td>
<td>Daten (FinTS-Nutzdaten und ggf. Signaturkopf/-abschluss) für die Verschlüsselung bereitstellen</td>
</tr>
<tr>
<td>R2</td>
<td>RND</td>
<td>↓↑ ↓↑</td>
<td>C2<br>A2<br>C3</td>
<td>Aufruf der ZKA-SIG-API-Funktion zka_sig_get_challenge<br>RND als Nachrichtenschlüssel-Hälfte KSL speichern<br>Aufruf der ZKA-SIG-API-Funktion zka_sig_get_challenge</td>
</tr>
<tr>
<td>R3</td>
<td>RND</td>
<td></td>
<td>A3</td>
<td>RND als Nachrichtenschlüssel-Hälfte KSR speichern</td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td>A4</td>
<td>KSL mit KSR zu KS konkatenieren und speichern</td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td>A5</td>
<td>KS auf Eigenschaft ,(halb-)schwacher Schlüssel“ überprüfen und ggfs. Schritte 2-4 wiederholen.</td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td>A6</td>
<td>Herstellung der Parität für KS (Parity Adjustment)</td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td>A7</td>
<td>Daten mit KS (symmetrisch) verschlüsseln</td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td>A8</td>
<td>KS mit PK.RECVINST.KE (asymmetrisch) verschlüsseln</td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td>A9</td>
<td>Verschlüsselungskopf aufbauen und in FinTS-Nachricht einfügen</td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td>A10</td>
<td>Verschlüsselte Daten als Binärdaten in FinTS-Nachricht einfügen</td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td>A11</td>
<td>ggf. A1 bis A10 für weitere Nachrichten wiederholen</td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td>A12</td>
<td>Verschlüsselte und signierte FinTS-Meldungen zur weiteren Be- arbeitung speichern</td>
</tr>
</table>


# ◆ Erläuterung

1\. Die Daten (FinTS-Nutzdaten und ggf. Signaturkopf/-abschluss) für die Verschlüs-
selung werden bereitgestellt.

<!-- PageFooter: 11 [DIN-SIG4, Kapitel 6.10.1]: ,If an enciphered document is sent, the card is not involved: the soft- ware computes the content encryption key, enciphers the document and finally enciphers the con- tent encryption key by applying the receiver's public key taken from the receiver's KE certificate." -->
<!-- PageBreak -->


<table>
<tr>
<td>Kapitel:<br>C</td>
<td>Version: 3.0 - Final Version</td>
<td>Financial Transaction Services (FinTS) Dokument: Security - Sicherheitsverfahren HBCI</td>
</tr>
<tr>
<td>Seite:<br>100</td>
<td>Stand:<br>18.07.2013</td>
<td>Kapitel: Chipapplikationen<br>Abschnitt: Chipapplikation für RAH / RDH</td>
</tr>
</table>


2\. Mit dem Aufruf der ZKA-SIG-API-Funktion zka_sig_get_challenge lässt sich das
Terminal eine Zufallszahl von der HBCI-Karte geben.

Wenn das Kommando erfolgreich ausgeführt wurde, gibt die HBCI-Karte eine Zu-
fallszahl als Antwortdatum aus, die als Nachrichtenschlüssel-Hälfte KSL gespei-
chert wird.

3\. Mit dem Aufruf der ZKA-SIG-API-Funktion zka_sig_get_challenge lässt sich das
Terminal eine weitere Zufallszahl von der HBCI-Karte geben, die als Nachrich-
tenschlüssel-Hälfte KSR gespeichert wird.

4\. KSL wird mit KSR zu KS konkateniert und gespeichert.

5\. KS wird auf die Eigenschaft „(halb-)schwacher Schlüssel“ überprüft. Liegt ein
(halb-)schwacher Schlüssel vor, so wird Schritt 2-4 wiederholt.


<table>
<caption>Schwache Schlüssel des DES:</caption>
<tr>
<td>01</td>
<td>01</td>
<td>01</td>
<td>01</td>
<td>01</td>
<td>01</td>
<td>01</td>
<td>01</td>
</tr>
<tr>
<td>FE</td>
<td>FE</td>
<td>FE</td>
<td>FE</td>
<td>FE</td>
<td>FE</td>
<td>FE</td>
<td>FE</td>
</tr>
<tr>
<td>1F</td>
<td>1F</td>
<td>1F</td>
<td>1F</td>
<td>0E</td>
<td>0E</td>
<td>0E</td>
<td>0E</td>
</tr>
<tr>
<td>E0</td>
<td>E0</td>
<td>E0</td>
<td>E0</td>
<td>F1</td>
<td>F1</td>
<td>F1</td>
<td>F1</td>
</tr>
</table>


Halbschwache Schlüssel des DES:


<table>
<tr>
<td>01</td>
<td>FE</td>
<td>01</td>
<td>FE</td>
<td>01</td>
<td>FE</td>
<td>01</td>
<td>FE</td>
</tr>
<tr>
<td>FE</td>
<td>01</td>
<td>FE</td>
<td>01</td>
<td>FE</td>
<td>01</td>
<td>FE</td>
<td>01</td>
</tr>
<tr>
<td>1F</td>
<td>E0</td>
<td>1F</td>
<td>E0</td>
<td>0E</td>
<td>F1</td>
<td>0E</td>
<td>F1</td>
</tr>
<tr>
<td>E0</td>
<td>1F</td>
<td>E0</td>
<td>1F</td>
<td>F1</td>
<td>0E</td>
<td>F1</td>
<td>0E</td>
</tr>
<tr>
<td>01</td>
<td>E0</td>
<td>01</td>
<td>E0</td>
<td>01</td>
<td>F1</td>
<td>01</td>
<td>F1</td>
</tr>
<tr>
<td>E0</td>
<td>01</td>
<td>E0</td>
<td>01</td>
<td>F1</td>
<td>01</td>
<td>F1</td>
<td>01</td>
</tr>
<tr>
<td>1F</td>
<td>FE</td>
<td>1F</td>
<td>FE</td>
<td>0E</td>
<td>FE</td>
<td>0E</td>
<td>FE</td>
</tr>
<tr>
<td>FE</td>
<td>1F</td>
<td>FE</td>
<td>1F</td>
<td>FE</td>
<td>0E</td>
<td>FE</td>
<td>0E</td>
</tr>
<tr>
<td>01</td>
<td>1F</td>
<td>01</td>
<td>1F</td>
<td>01</td>
<td>0E</td>
<td>01</td>
<td>0E</td>
</tr>
<tr>
<td>1F</td>
<td>01</td>
<td>1F</td>
<td>01</td>
<td>0E</td>
<td>01</td>
<td>0E</td>
<td>01</td>
</tr>
<tr>
<td>E0</td>
<td>FE</td>
<td>E0</td>
<td>FE</td>
<td>F1</td>
<td>FE</td>
<td>F1</td>
<td>FE</td>
</tr>
<tr>
<td>FE</td>
<td>E0</td>
<td>FE</td>
<td>E0</td>
<td>FE</td>
<td>F1</td>
<td>FE</td>
<td>F1</td>
</tr>
</table>


6\. Für KS wird_ein Parity Adjustment durchgeführt. Das Resultat ist der zu ver-
wendende Nachrichtenschlüssel.

7\. Die zu übertragenden Daten werden mit KS symmetrisch verschlüsselt.

8\. Der Nachrichtenschlüssel KS wird gemäß Paddingverfahren für das entspre-
chende Sicherheitsprofil auf die Länge des öffentlichen Key-Encryption-
Schlüssels PK.RECVINST.K des empfangenden Instituts, welches der übermittel-
ten Kreditinstitutsnachricht entnommen wurde, aufgefüllt und anschlieBend mit
dem PK.RECVINST.K verschlüsselt.. Stimmt das Verschlüsselungsergebnis mit
dem Ausgangswert überein, werden die Schritte 2 bis 8 wiederholt (Generie-
rung eines neuen Schlüssels); ansonsten wird Das Ergebnis wird mit führenden
Nullbits auf die Schlüssellänge erweitert. und es wird mit dem folgenden Schritt
9 fortgefahren.

9\. Der Verschlüsselungskopf wird aufgebaut und in die FinTS-Nachricht eingefügt.

10\. Die verschlüsselten Daten als Binärdaten in die FinTS-Nachricht eingefügt.

11\. Ggf. werden die Schritte 1 bis 10 für weitere Nachrichten wiederholt.

<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th>Version:</th>
<th>Kapitel:</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Security - Sicherheitsverfahren HBCI</td>
<td>3.0 - Final Version</td>
<td>C</td>
</tr>
<tr>
<td>Kapitel:</td>
<td>Chipapplikationen</td>
<td>Stand:</td>
<td>Seite:</td>
</tr>
<tr>
<td>Abschnitt:</td>
<td>Chipapplikation für RAH / RDH</td>
<td>18.07.2013</td>
<td>101</td>
</tr>
</table>


12\. Die verschlüsselten und signierten FinTS-Meldungen werden zur weiteren Be-
arbeitung gespeichert.


## C.1.3.2.6 Übertragungsdialog


<table>
<tr>
<td colspan="2">Chipkarte</td>
</tr>
<tr>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
</tr>
</table>


<table>
<tr>
<td rowspan="11">↑↓<br>↑↓</td>
<td colspan="2">Endgerät</td>
<td></td>
<td colspan="2">Kreditinstitut</td>
</tr>
<tr>
<td>A1</td>
<td>Benutzerkennung aus der bereits gelese- nen Bankverbindung extrahieren</td>
<td rowspan="10">↑↓</td>
<td></td>
<td></td>
</tr>
<tr>
<td>M2</td>
<td>Nachricht signieren (s. Kap. C.1.3.2.3)</td>
<td></td>
<td></td>
</tr>
<tr>
<td>A3</td>
<td>Kommunikationszugang aus Bankverbin- dung herstellen</td>
<td></td>
<td></td>
</tr>
<tr>
<td>C4</td>
<td>Nachricht (beginnend mit Dialoginitialisie- rungsnachricht) senden</td>
<td>R4</td>
<td>Antwort- nachricht</td>
</tr>
<tr>
<td>A5</td>
<td>falls Antwortnachricht verschlüsselt: Daten (Binärdaten nach dem Verschlüsse- lungskopf) und verschlüsselten Session- Key enc(KS) aus dem Signaturkopf für die Entschlüsselung bereitstellen</td>
<td></td>
<td></td>
</tr>
<tr>
<td>M6</td>
<td>Ausführung der ZKA-SIG-API-Funktion zka_sig_decrypt zur Session-Key- Entschlüsselung, Resultat ist der Session- Key KS</td>
<td></td>
<td></td>
</tr>
<tr>
<td>A7</td>
<td>Daten mit Session-Key KS entschlüsseln.</td>
<td></td>
<td></td>
</tr>
<tr>
<td>A8</td>
<td>falls Kreditinstitutsnachricht signiert: Daten (Signaturkopf, Nutzdaten, Signatur) für Signatur-Prüfung bereitstellen</td>
<td></td>
<td></td>
</tr>
<tr>
<td>M9</td>
<td>Signatur-Prüfung (siehe KapC.1.3.3.2)</td>
<td></td>
<td></td>
</tr>
<tr>
<td>A10</td>
<td>C4 bis M9 für alle weiteren HBCI-Nach- richten wiederholen</td>
<td></td>
<td></td>
</tr>
</table>


### C.1.3.2.7 Signatur beenden


<table>
<tr>
<th colspan="2">Chipkarte</th>
<th></th>
<th colspan="2">Endgerät</th>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td>M1</td>
<td>Aufruf der ZKA-SIG-API-Funktion zka_sig_fini_signature_application</td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
<td>M2</td>
<td>Aufruf der ZKA-SIG-API-Funktion zka_sig_close</td>
</tr>
</table>


#### ◆ Erläuterung

1\. Die ZKA-SIG-API-Funktion zka_sig_fini_signature_application wird ausgeführt.
Diese Funktion setzt die ZKA-SIG-API in den Zustand ,,passiv“ und löscht die da-
rin gespeicherten Werte.

2\. Die ZKA-SIG-API-Funktion zka_sig_close gibt die Verbindung zum Kundentermi-
nal wieder frei.

<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: C</td>
<td>Version: 3.0 - Final Version</td>
<td>Financial Transaction Services (FinTS) Dokument: Security - Sicherheitsverfahren HBCI</td>
</tr>
<tr>
<td>Seite:<br>102</td>
<td>Stand: 18.07.2013</td>
<td>Kapitel: Chipapplikationen<br>Abschnitt: Chipapplikation für RAH / RDH</td>
</tr>
</table>


### C.1.3.3 Makros


#### C.1.3.3.1 Signatur-Berechnung

Signaturen mit der Chipkarte werden im Rahmen der beiden Sicherheitsdienste „Au-
thentication" und ,,Non-Repudiation“ erzeugt.

. Sicherheitsdienst Authentication: Signatur mit Schlüssel SK.CH.AUT c/s (Client-
Server-Authentikations-Schlüssel)

. Sicherheitsdienst Non-Repudiation: Signatur mit Schlüssel SK.CH.DS (Digitaler
Signatur-Schlüssel)

Die tatsächliche Durchführung der Signatur durch die Chipkarte ist insbesondere an
die Erfüllung von Zugriffsbedingungen geknüpft, hier ist dies insbesondere eine vor-
hergehende Benutzer-Authentikation in Form der Verifikation

· des CSA-Passworts für die Erlaubnis zur Signatur mit dem Schlüssel
SK.CH.AUT C/S

• der Signatur-PIN für die Erlaubnis zur Signatur mit dem Schlüssel Sk.CH.DS

Durch einen in der Chipkarte personalisierten Parameter der Signatur-Anwendung
[ZKASIG] wird dabei festgelegt, nach wie vielen elektronischen Signaturen spätes-
tens die Benutzer-Authentikation zu wiederholen ist. Eine Benutzer-Authentikation
wird bei Bedarf innerhalb der ZKA-SIG-API-Funktionen zka_sig_digital_signature
bzw. zka_sig_cs_authentication durchgeführt.


<table>
<tr>
<td colspan="2">Chipkarte</td>
</tr>
<tr>
<td>R1</td>
<td>evtl. Hash- wert</td>
</tr>
<tr>
<td>R2a<br>R2b</td>
<td>Signatur<br>Signatur</td>
</tr>
</table>


←
→
←
→

←

→


<table>
<tr>
<td colspan="2">Endgerät</td>
</tr>
<tr>
<td>M1</td>
<td>Hashwert HASH berechnen, optional unter Verwendung der ZKA-SIG-API-Funktion zka_sig_hash</td>
</tr>
<tr>
<td>M2a</td>
<td>Sicherheitsdienst Non-Repudiation: Aufruf der ZKA-SIG-API- Funktion zka_sig_digital_signature<br>oder:</td>
</tr>
<tr>
<td>M2b</td>
<td>Sicherheitsdienst Authentication: Aufruf der ZKA-SIG-API- Funktion zka_sig_cs_authentication</td>
</tr>
</table>


##### ◆ Erläuterung

1\. Die Berechnung des Hashwertes erfolgt in der Regel außerhalb der Chipkarte
(Hashalgorithmus gemäß Vorgabe für den Sicherheitsdienst bzw. vom Institut
übermittelter BPD). Optional ist es auch möglich, den letzen Schritt oder alle
Schritte der Hashwert-Berechnung durch die Chipkarte durchführen zu lassen.
Diese Berechnung ist dann Bestandteil des Ablaufs der ZKA-SIG-API-Funktion
zka_sig_hash. Der zu verwendende Hash-Algorithmus wird dabei in Form der
zugehörigen OID übergeben:

• OID = 1.3.14.3.2.26 für SHA-1

• OID = 1.3.36.3.2.1 für RIPEMD-160

• OID = 2.16.840.1.101.3.4.2.1 für SHA-256

<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th>Version:</th>
<th>Kapitel:</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Security - Sicherheitsverfahren HBCI</td>
<td>3.0 - Final Version</td>
<td>C</td>
</tr>
<tr>
<td>Kapitel:</td>
<td>Chipapplikationen</td>
<td>Stand:</td>
<td>Seite:</td>
</tr>
<tr>
<td>Abschnitt:</td>
<td>Chipapplikation für RAH / RDH</td>
<td>18.07.2013</td>
<td>103</td>
</tr>
</table>


2a. Bei Verwendung des Schlüssels Sk.CH.DS (Sicherheitsdienst Non-Repudiation)
wird die Signatur durch Aufruf der ZKA-SIG-API-Funktion zka_sig_digital_sig-
nature erzeugt. Die Auswahl des Signaturalgorithmus und Paddingverfahrens
erfolgt gemäß Vorgabe für den Sicherheitsdienst bzw. vom Institut übermittelter
BPD. Die Signaturanwendung der Chipkarte bietet die Verfahren „sha-1-
WithRSAEncryption" (PKCS#1-Signaturverfahren, Standard-RSA, SHA-1) und
,sigS_ISO9796-2rndWithripemd160" (DIN-Signaturverfahren, Standard-RSA,
RIPEMD-160) an. Zusätzlich bieten Banken-Signaturkarten mit SECCOS 6
auch das Signaturverfahren RSASSA-PSS an.

Falls der Hashwert im vorangegangenen Schritt 1 durch die Chipkarte berech-
net wurde, ist er noch in der Chipkarte gespeichert und braucht nicht erneut als
Parameter des zka_sig_digital_signature übergeben zu werden.

2b. Bei Verwendung des Schlüssels SK.CH.AUT c/s (Sicherheitsdienst Authenticati-
on) wird die Signatur durch Aufruf der ZKA-SIG-API-Funktion zka_sig_cs_au-
thentication erzeugt. Die Chipkarte verwendet dabei intern ein Paddingformat
gemäß PKCS#1 ([SECCOS, Kapitel 8.3.2.1]12), wobei die Digest-Info nicht von
der Chipkarte selbst erzeugt wird, sondern als aufbereiteter „Authentication-
Input“ (= zu signierendes Datenfeld) übergeben werden muss.

Der Authentication-Input ist wie folgt aufgebaut ([SECCOS, Kapitel 8.1.8.3.1]):


<table>
<tr>
<th>Tag</th>
<th>Länge</th>
<th>Wert</th>
<th>Erläuterung</th>
</tr>
<tr>
<td>'30'</td>
<td>'21' bzw. '31'</td>
<td></td>
<td>Tag und Länge von SEQUENCE (SHA-1/RIPEMD-160 bzw. SHA-256)</td>
</tr>
<tr>
<td>'30'</td>
<td>'09' bzw. 'OD'</td>
<td></td>
<td>Tag und Länge von SEQUENCE (SHA-1/RIPEMD-160 bzw. SHA-256)</td>
</tr>
<tr>
<td>'06'</td>
<td>'05' bzw. '09'</td>
<td>'2B 0E 03 02 1A' bzw. '2B 24 03 02 01' bzw. '60 86 48 01 65 03 04 02 01'</td>
<td>OID des SHA-1 (1 3 14 3 2 26) bzw. OID des RIPEMD-160 (1 3 36 3 2 1) bzw. OID des SHA-256 (2 16 840 1 101 3 4 2 1)</td>
</tr>
<tr>
<td>'05'</td>
<td>'00'</td>
<td>-</td>
<td>TLV-Kodierung von NULL</td>
</tr>
<tr>
<td>'04'</td>
<td>'14'</td>
<td>'XX..XX'</td>
<td>Hash-Wert</td>
</tr>
</table>


Anmerkung: Die direkte Weiterverwendung eines eventuell im Chip berechneten
und dort zwischengespeicherten Hashwerts ist bei der Signatur im Sicherheitsdienst
„Authentication“ nicht möglich. Der Hashwert (als Ergebnis von Schritt 1) muss da-
her explizit als Aufrufparameter in der oben beschriebenen Form in Schritt 2 über-
geben werden.

<!-- PageFooter: 12 Auszug aus [SECCOS, Kapitel 8.3.2.1]: Falls der Authentication Input nicht zu lang ist, wird er zu einer Folge von N-1 Byte wie folgt formatiert: -->


<table>
<tr>
<th>Bezeichnung</th>
<th>Byte-Länge</th>
<th>Wert</th>
</tr>
<tr>
<td>Blocktyp</td>
<td>1</td>
<td>'01'</td>
</tr>
<tr>
<td>Paddingfeld (PS)</td>
<td>N-3-L</td>
<td>'FF...FF'</td>
</tr>
<tr>
<td>Separator</td>
<td>1</td>
<td>'00'</td>
</tr>
<tr>
<td>Datenfeld</td>
<td>L</td>
<td>Authentication Input (AI)</td>
</tr>
<tr>
<td>Kapitel: C</td>
<td>Version: 3.0 - Final Version</td>
<td>Financial Transaction Services (FinTS) Dokument: Security - Sicherheitsverfahren HBCI</td>
</tr>
<tr>
<td>Seite:<br>104</td>
<td>Stand: 18.07.2013</td>
<td>Kapitel: Chipapplikationen<br>Abschnitt: Chipapplikation für RAH / RDH</td>
</tr>
</table>


#### C.1.3.3.2 Signatur-Prüfung

Die ZKA-Chipkarte selbst unterstützt zurzeit keine Signatur-Prüfung13. Die Prüfung
einer Signatur wird vom Kundenterminal-Makro "Überprüfen der Korrektheit der
elektronischen Unterschrift" durchgeführt.

Die (mathematische) Korrektheit einer elektronischen Unterschrift wird überprüft, in
dem sie mit dem entsprechenden öffentlichen Schlüssel entschlüsselt wird und das
Ergebnis mit dem Hashwert über die signierten Daten verglichen wird. Der für die
Überprüfung der elektronischen Signatur eingesetzte öffentliche Schlüssel liegt in
dem Kundenterminal authentisch vor, falls die zu ihm gehörende Zertifikatshierar-
chie vorher ebenfalls in dem Kundenterminal überprüft wurde [KT-KONZEPT].

<!-- PageFooter: 13 [ZKASIG, Kapitel 1.1]: ,Die ZKA-Chipkarte unterstützt [die] Signaturprüfung zur Zeit aus dem fol- genden Grund nicht: Die Prüfung digitaler Signaturen, die mit beliebigen privaten Schlüsseln und/oder Algorithmen berechnet sind, würde voraussetzen, dass die Chipkarte X.509-Zertifikate auswertet. Dies ist gemäß Kapitel 16.1 von [DINSIG] zur Zeit nicht möglich.“ -->
<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th>Version:</th>
<th>Kapitel:</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Security - Sicherheitsverfahren HBCI</td>
<td>3.0 - Final Version</td>
<td>C</td>
</tr>
<tr>
<td>Kapitel:</td>
<td>Chipapplikationen</td>
<td>Stand:</td>
<td>Seite:</td>
</tr>
<tr>
<td>Abschnitt:</td>
<td>Chipapplikation für DDV</td>
<td>18.07.2013</td>
<td>105</td>
</tr>
</table>


##### C.2 Chipapplikation für DDV

Im Folgenden wird für das in Kap. B beschriebene DDV-Verfahren eine entspre-
chende Chipanwendung namens ,,Banking" synonym ,HBCI-Banking" spezifiziert.
Voraussetzung ist neben den nachfolgend beschriebenen Datenelementen zusätz-
lich das Vorhandensein des Datenelements EF_ID sowie des Kryptoalgorithmus
Triple-DES, wie sie in der ,Schnittstellenspezifikation für die ec-Karte mit Chip" vom
ZKA festgelegt wurden. Die Spezifikation bezieht sich allein auf die für HBCI erfor-
derlichen Datenelemente.

Die Anwendung ,Banking“ kann auf einer dedizierten Chipkarte (,HBCI-Karte“) oder
auf beliebigen multifunktionalen Chipkarten implementiert werden, sofern sie das
Betriebssystem der ec-Karte mit Chip einsetzen. Für die HBCI-Anwendung ist kein
ausführbarer Code über die Spezifikationen in ISO 7816-4 bzw. der ec-Karte mit
Chip hinaus erforderlich.

In diesem Kapitel werden die Datenstrukturen und Zugriffsregeln der Chipapplikati-
on "DF_BANKING_20" für Chipkarten vom Typ 1 (,altes ZKA-Betriebssystem") und
Typ SECCOS 6 (,,neues ZKA-Betriebssystem") spezifiziert. Die Kommandoabläufe
im Terminal sind gemeinsam für Chipkarten vom Typ 114 und SECCOS 6 spezifi-
ziert.

In Kap. C.2.1 wird explizit auf die Beschreibung für Typ 1 eingegangen. Im weiteren
Verlauf dieses Dokuments ist mit "HBCI-Chipkarte" eine Chipkarte mit neuem ZKA-
Betriebssystem gemäß [DATKOM] und [DAT-MF] gemeint, die die HBCI-Applikation
enthält. Weitere Applikationen, wie z.B. die elektronische Geldbörse, sind nicht not-
wendigerweise auf der Chipkarte enthalten. Ebenso kann die Bankensignaturkarte
mit oder ohne Zertifikat ausgeliefert werden.

Das ADF der Applikation HBCI-Banking wird mit DF_BANKING_20 bezeichnet. In
der vorliegenden Spezifikation ist es direkt im MF enthalten. Die für die Applikation
relevanten DF-spezifischen Schlüssel sind im EF_KEY abgelegt, das direkt im
DF_BANKING_20 enthalten ist.

In der vorliegenden Spezifikation werden im Kontext von Typ 1-Karten zwei Securi-
ty-Environments verwendet:

1 Das Security-Environment mit der Nummer 1 (SE #1) als Standard-SE legt die
Zugriffsregeln für die Dateien der Applikation HBCI-Banking für den Anwen-
dungsfall, d.h. für den Zugriff im Feld an HBCI-fähigen Terminals fest.

2 Das Security-Environment mit der Nummer 2 (SE #2) als Administrations-SE legt
die Zugriffsregeln für die Dateien und das Applikationsverzeichnis der Applikation
HBCI-Banking für den Fall von Administrationsvorgängen, z.B. Kontrolle, Ände-
rungen oder Erweiterungen, fest.

Die Selektion von SEs erfolgt, wie in [DATKOM] beschrieben, mit dem Kommando
MANAGE SECURITY ENVIRONMENT. Für den Anwendungsfall, d.h. an HBCI-
fähigen Terminals, ist eine Selektion des SE nicht notwendig, da mit der Selektion
einer Applikation implizit das SE #1 aktiviert wird.

<!-- PageFooter: 14 In den Abläufen befinden sich an wenigen Stellen aus Gründen der Vollständigkeit noch Verweise auf das Vorläuferbetriebssystem für Chipkarten vom Typ 0. -->
<!-- PageBreak -->


<table>
<tr>
<td>Kapitel:</td>
<td>Version:</td>
<td>Financial Transaction Services (FinTS)</td>
</tr>
<tr>
<td>C</td>
<td>3.0 - Final Version</td>
<td>Dokument: Security - Sicherheitsverfahren HBCI</td>
</tr>
<tr>
<td rowspan="2">Seite:<br>106</td>
<td>Stand:</td>
<td>Kapitel: Chipapplikationen</td>
</tr>
<tr>
<td>18.07.2013</td>
<td>Abschnitt: Chipapplikation für DDV</td>
</tr>
</table>


###### C.2.1 Daten der Applikation HBCI-Banking für Typ 1

Die folgende Grafik gibt eine Übersicht über die Dateien einer HBCI-Karte mit der
Applikation HBCI-Banking für Typ 1.


Abbildung 19: Datenelemente der Applikation "HBCI", Bankensignaturkarte mit Zerti-
fikat

![MF EF_KEY EF_KEYD EF_PWD EF_PWDD EF_FBZ EF_ID EF_INFO EF_RULE EF_SIG EF_SIGD DF_BANKING_20 EF_KEY EF_KEYD EF_RULE EF_BNK EF_MAC EF_SEQ EF_PWD EF_PWDD EF_FBZ](figures/120.1)


<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th>Version:</th>
<th>Kapitel:</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Security - Sicherheitsverfahren HBCI</td>
<td>3.0 - Final Version</td>
<td>C</td>
</tr>
<tr>
<td>Kapitel:</td>
<td>Chipapplikationen</td>
<td>Stand:</td>
<td>Seite:</td>
</tr>
<tr>
<td>Abschnitt:</td>
<td>Chipapplikation für DDV</td>
<td>18.07.2013</td>
<td>107</td>
</tr>
</table>


Abbildung 20: Datenelemente der Applikation "HBCI", Bankensignaturkarte ohne
Zertifikat

![MF EF_KEY EF_KEYD EF_ID EF_RULE EF_SIG EF_SIGD DF_BANKING_20 EF_KEY EF_KEYD EF_RULE EF_BNK EF_MAC EF_SEQ EF_PWD EF_PWDD EF_FBZ](figures/121.1)


<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: C</td>
<td>Version: 3.0 - Final Version</td>
<td>Financial Transaction Services (FinTS) Dokument: Security - Sicherheitsverfahren HBCI</td>
</tr>
<tr>
<td>Seite: 108</td>
<td>Stand: 18.07.2013</td>
<td>Kapitel: Chipapplikationen<br>Abschnitt: Chipapplikation für DDV</td>
</tr>
</table>


####### C.2.1.1 ADF der Applikation HBCI-Banking

Für das ADF der Applikation HBCI-Banking (DF_BANKING_20) sind beim Anlegen
die folgenden FCP festzulegen:


<table>
<tr>
<th>Tag</th>
<th>Länge</th>
<th>Wert</th>
<th>Erläuterung</th>
</tr>
<tr>
<td>'62'</td>
<td>'1A'</td>
<td></td>
<td>Tag und Länge für FCP</td>
</tr>
<tr>
<td>'82'</td>
<td>'01'</td>
<td>'38'</td>
<td>Datei-Deskriptor für DF</td>
</tr>
<tr>
<td>'83'</td>
<td>'02'</td>
<td>'A6 00'</td>
<td>Datei-ID des DF_BANKING_20</td>
</tr>
<tr>
<td>'84'</td>
<td>'09'</td>
<td>'D2 76 00 00 25 48 42 02 00'</td>
<td>DF-Name (AID) des DF_BANKING_20</td>
</tr>
<tr>
<td>'A1'</td>
<td>'06'</td>
<td>'8B 04 00 30 02 01'</td>
<td>Zugriffsregel-Referenzen</td>
</tr>
</table>


Der DF-Name (die AID) des DF_BANKING_20 bestehend aus der nationalen RID
des ZKA ('D2 76 00 00 25'), der ASCII-kodierten Kennung "HB" ('48 42') sowie der
Version der Applikation 2.0 ('02 00').

Die Zugriffsregeln für das DF_BANKING_20 stehen in der zugeordneten Regeldatei
EF_RULE. Durch die Zugriffsregeln werden für die DF-spezifischen Kommandos die
folgenden Festlegungen getroffen:

Wenn das DF_BANKING_20 selektiert ist, darf ein CREATE FILE (EF), DELETE
FILE (self), INCLUDE oder EXCLUDE nur ausgeführt werden, wenn die Komman-
donachricht mit Secure Messaging ausgeführt wird und mit einem korrekten MAC
versehen ist, der unter Verwendung des Schlüssels KHBCI Admin aus dem EF_KEY
des DF_BANKING_20 gebildet ist. Der Returncode wird für jedes dieser Komman-
dos durch die Karte mit einem MAC mit dem Schlüssel KHBCI_Admin versehen. Die
Kommandos CREATE FILE (DF) und DELETE FILE (child DF) dürfen nie ausge-
führt werden. Alle zulässigen Administrationskommandos dürfen nur im SE #2 aus-
geführt werden (Zugriffsregeln im Record 1 des EF_RULE).

Der Applikation HBCI-Banking sind 10 Dateien als AEF zuzuordnen:

SFI '01':
EF_RULE im DF_BANKING_20

SFI '02':
EF_KEY im DF_BANKING_20,

SFI '03':
EF_PWD im DF_BANKING_20,

SFI '04':
EF_PWDD im DF_BANKING_20,

SFI '05':
EF_FBZ im DF_BANKING_20,

SFI '19':
EF_ID im MF,

SFI '1A':
EF_BNK im DF_BANKING_20,

SFI '1B':
EF_MAC im DF_BANKING_20,

SFI '1C':
EF_SEQ im DF_BANKING_20,

SFI '1E':
EF_KEYD im DF_BANKING_20.

Wenn das DF_BANKING_20 mittels SELECT FILE selektiert wird und die entspre-
chende Option im Parameterbyte P2 des Kommandos gesetzt ist, wird die folgende
FCI ausgegeben:


<table>
<tr>
<th>Tag</th>
<th>Länge</th>
<th>Wert</th>
<th>Erläuterung</th>
</tr>
<tr>
<td>'6F'</td>
<td>'0D'</td>
<td></td>
<td>Tag und Länge für FCI</td>
</tr>
<tr>
<td>'84'</td>
<td>'09'</td>
<td>'D2 76 00 00 25 48 42 02 00'</td>
<td>DF-Name (AID) des DF_BANKING_20</td>
</tr>
<tr>
<td>'A5'</td>
<td>'00'</td>
<td></td>
<td>keine proprietären Informationen</td>
</tr>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th>Version:</th>
<th rowspan="2">Kapitel: C</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Security - Sicherheitsverfahren HBCI</td>
<td>3.0 - Final Version</td>
</tr>
<tr>
<td>Kapitel:</td>
<td>Chipapplikationen</td>
<td>Stand:</td>
<td>Seite:</td>
</tr>
<tr>
<td>Abschnitt:</td>
<td>Chipapplikation für DDV</td>
<td>18.07.2013</td>
<td>109</td>
</tr>
</table>


Wird das DF_BANKING_20 mittels SELECT FILE selektiert und die entsprechende
Option im Parameterbyte P2 des Kommandos gesetzt, werden die folgenden FMD
mit den Pfaden der AEFs ausgegeben (vorausgesetzt, das DF_BANKING_20 befin-
det sich direkt im MF):


<table>
<tr>
<th>Tag</th>
<th>Länge</th>
<th>Wert</th>
<th>Erläuterung</th>
</tr>
<tr>
<td>'64'</td>
<td>'44'</td>
<td></td>
<td>Tag und Länge für FMD</td>
</tr>
<tr>
<td>'85'</td>
<td>'03'</td>
<td>'C8 00 03'</td>
<td>Pfad für AEF mit SFI '19' (EF_ID im MF)</td>
</tr>
<tr>
<td>'85'</td>
<td>'05'</td>
<td>'08 A6 00 00 30'</td>
<td>Pfad für AEF mit SFI '01' (EF_RULE im DF_BANKING_20)</td>
</tr>
<tr>
<td>'85'</td>
<td>'05'</td>
<td>'10 A6 00 00 10'</td>
<td>Pfad für AEF mit SFI '02' (EF_KEY im DF_BANKING_20)</td>
</tr>
<tr>
<td>'85'</td>
<td>'05'</td>
<td>'18 A6 00 00 12'</td>
<td>Pfad für AEF mit SFI '03' (EF_PWD im DF_BANKING_20)</td>
</tr>
<tr>
<td>'85'</td>
<td>'05'</td>
<td>'20 A6 00 00 15'</td>
<td>Pfad für AEF mit SFI '04' (EF_PWDD im DF_BANKING_20)</td>
</tr>
<tr>
<td>'85'</td>
<td>'05'</td>
<td>'28 A6 00 00 16'</td>
<td>Pfad für AEF mit SFI '05' (EF_FBZ im DF_BANKING_20)</td>
</tr>
<tr>
<td>'85'</td>
<td>'05'</td>
<td>'D0 A6 00 03 01'</td>
<td>Pfad für AEF mit SFI '1A' (EF_BNK im DF_BANKING_20)</td>
</tr>
<tr>
<td>'85'</td>
<td>'05'</td>
<td>'D8 A6 00 03 02'</td>
<td>Pfad für AEF mit SFI '1B' (EF_MAC im DF_BANKING_20)</td>
</tr>
<tr>
<td>'85'</td>
<td>'05'</td>
<td>'E0 A6 00 03 03'</td>
<td>Pfad für AEF mit SFI '1C' (EF_SEQ im DF_BANKING_20)</td>
</tr>
<tr>
<td>'85'</td>
<td>'05'</td>
<td>'F0 A6 00 00 13'</td>
<td>Pfad für AEF mit SFI '1E' (EF_KEYD im DF_BANKING_20)</td>
</tr>
</table>


<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: C</td>
<td>Version: 3.0 - Final Version</td>
<td>Financial Transaction Services (FinTS) Dokument: Security - Sicherheitsverfahren HBCI</td>
</tr>
<tr>
<td>Seite: 110</td>
<td>Stand: 18.07.2013</td>
<td>Kapitel: Chipapplikationen<br>Abschnitt: Chipapplikation für DDV</td>
</tr>
</table>


#### C.2.1.2 EF_RULE


##### . Beschreibung

Die Datei EF_RULE enthält die Zugriffsregeln für die Applikation DF_BANKING_20.
In den FCP von Dateien und Verzeichnissen wird auf diese Zugriffsregeln referen-
ziert.


##### . Format

Für das EF_RULE des DF_BANKING_20 sind die folgenden FCP festzulegen:


<table>
<tr>
<th>Tag</th>
<th>Länge</th>
<th>Wert</th>
<th>Erläuterung</th>
</tr>
<tr>
<td>'62'</td>
<td>'1C'</td>
<td></td>
<td>Tag und Länge für FCP</td>
</tr>
<tr>
<td>'82'</td>
<td>'05'</td>
<td>'14 41 00 24 08'</td>
<td>Datei-Deskriptor für lineares EF mit variab- ler Recordlänge (max. 36 Byte), 8 Records</td>
</tr>
<tr>
<td>'83'</td>
<td>'02'</td>
<td>'00 30'</td>
<td>Datei-ID des EF_RULE</td>
</tr>
<tr>
<td>'85'</td>
<td>'02'</td>
<td>'00 7D'</td>
<td>für Nutzdaten allokierter Speicherplatz in Byte</td>
</tr>
<tr>
<td>'88'</td>
<td>'01'</td>
<td>'08'</td>
<td>SFI '01' für das EF_RULE</td>
</tr>
<tr>
<td>'A1'</td>
<td>'08'</td>
<td>'8B 06 00 30 01 02 02 03'</td>
<td>Zugriffsregel-Referenzen</td>
</tr>
</table>


Im SE #1 dürfen nur die Kommandos READ / SEARCH RECORD mit ungesicherter
Kommando und Antwortnachricht ausgeführt werden (Zugriffsregel im Record 2 des
EF_RULE).

Im SE #2 darf APPEND RECORD nur ausgeführt werden, wenn es mit Secure
Messaging ausgeführt wird. Die MAC-Bildung erfolgt für Kommando- und Antwort-
nachricht mit dem KHBCI_Admin. UPDATE RECORD darf nie ausgeführt werden (Zu-
griffsregel im Record 3 des EF_RULE).


##### . Daten

Das EF_RULE im DF_BANKING_20 enthält 8 Records mit den Zugriffsregeln für
das Verzeichnis und die Datenfelder des Verzeichnisses.

Die folgende Tabelle zeigt die Belegung dieser Records für eine HBCI-Chipkarte:


<table>
<tr>
<th>Rec.Nr.</th>
<th>Record-Inhalt</th>
<th>Byte</th>
</tr>
<tr>
<td>1</td>
<td>'80 01 DA B4 05 83 03 80 01 FF'</td>
<td>10</td>
</tr>
<tr>
<td>2</td>
<td>'80 01 81 90 00'</td>
<td>5</td>
</tr>
<tr>
<td>3</td>
<td>'80 01 84 B4 05 83 03 80 01 FF'</td>
<td>10</td>
</tr>
<tr>
<td>4</td>
<td>'80 01 86 AF 11 B4 05 83 03 80 01 FF B8 08 95 01 10 83 03 80 01 FF'</td>
<td>22</td>
</tr>
<tr>
<td>5</td>
<td>'80 01 86 B4 05 83 03 80 01 FF'</td>
<td>10</td>
</tr>
<tr>
<td>6</td>
<td>'80 01 82 A4 07 95 01 08 83 02 80 01 80 01 81 90 00'</td>
<td>17</td>
</tr>
<tr>
<td>7</td>
<td>'80 01 82 A4 07 95 01 08 83 02 80 01 80 01 81 AF 13 B4 08 95 01 20 83 03 80 02 FF A4 07 95 01 08 83 02 80 01'</td>
<td>36</td>
</tr>
<tr>
<td>8</td>
<td>'80 01 83 90 00 80 01 84 B4 05 83 03 80 01 FF'</td>
<td>15</td>
</tr>
</table>


Die Records 1 bis 5 enthalten jeweils eine, die Records 6 bis 8 jeweils zwei Zugriffs-
regeln.

Im folgenden werden die einzelnen Records des EF_RULE näher erläutert.

Record 1 wird referenziert als Zugriffsregel von DF_BANKING_20 in SE #2.

<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th>Version:</th>
<th>Kapitel:</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Security - Sicherheitsverfahren HBCI</td>
<td>3.0 - Final Version</td>
<td>C</td>
</tr>
<tr>
<td>Kapitel:</td>
<td>Chipapplikationen</td>
<td>Stand:</td>
<td>Seite:</td>
</tr>
<tr>
<td>Abschnitt:</td>
<td>Chipapplikation für DDV</td>
<td>18.07.2013</td>
<td>111</td>
</tr>
</table>


CREATE FILE (EF), DELETE FILE (self), INCLUDE, EXCLUDE: MAC-SM-AC für
Kommando- und Antwortnachricht mit KHBCI_Admin:


<table>
<tr>
<th>Tag</th>
<th>Länge</th>
<th>Wert</th>
<th>Erläuterung</th>
</tr>
<tr>
<td>'80'</td>
<td>'01'</td>
<td>'DA'</td>
<td>Zugriffsart für CREATE FILE (EF), DELETE FILE (self), INCLUDE, EXCLUDE</td>
</tr>
<tr>
<td>'B4'</td>
<td>'05'</td>
<td></td>
<td>CCT - Tag und Länge</td>
</tr>
<tr>
<td>'83'</td>
<td>'03'</td>
<td>'80 01 FF'</td>
<td>Schlüsselreferenz für KHBCI_Admin</td>
</tr>
</table>


Record 2 wird referenziert als Zugriffsregel von EF_RULE, EF_KEYD, EF_PWDD
und EF_FBZ in SE #1.

READ / SEARCH RECORD: ALW


<table>
<tr>
<th>Tag</th>
<th>Länge</th>
<th>Wert</th>
<th>Erläuterung</th>
</tr>
<tr>
<td>'80'</td>
<td>'01'</td>
<td>'81'</td>
<td>Zugriffsart für READ / SEARCH RECORD</td>
</tr>
<tr>
<td>'90'</td>
<td>'00'</td>
<td></td>
<td>Zugriffsbedingung ALW</td>
</tr>
</table>


Record 3 wird referenziert als Zugriffsregel von EF_RULE, EF_BNK und EF_MAC
in SE #2.

APPEND RECORD: MAC-SM-AC für Kommando- und Antwortnachricht mit dem
Schlüssel KHBCI_Admin.


<table>
<tr>
<th>Tag</th>
<th>Länge</th>
<th>Wert</th>
<th>Erläuterung</th>
</tr>
<tr>
<td>'80'</td>
<td>'01'</td>
<td>'84'</td>
<td>Zugriffsart für APPEND RECORD</td>
</tr>
<tr>
<td>'B4'</td>
<td>'05'</td>
<td></td>
<td>CCT - Tag und Länge</td>
</tr>
<tr>
<td>'83'</td>
<td>'03'</td>
<td>'80 01 FF'</td>
<td>Schlüsselreferenz für KHBCI_Admin</td>
</tr>
</table>


Record 4 wird referenziert als Zugriffsregel von EF_KEY und EF_PWD in SE #2.

APPEND RECORD, UPDATE RECORD: MAC-ENC-SM-AC für Kommandonach-
richt und MAC-SM-AC für Antwortnachricht mit KHBCI_Admin.


<table>
<tr>
<th>Tag</th>
<th>Länge</th>
<th>Wert</th>
<th>Erläuterung</th>
</tr>
<tr>
<td>'80'</td>
<td>'01'</td>
<td>'86'</td>
<td>Zugriffsart für APPEND RECORD, UPDATE RECORD</td>
</tr>
<tr>
<td>'AF'</td>
<td>'11'</td>
<td></td>
<td>AND- Template, Tag und Länge</td>
</tr>
<tr>
<td>'B4'</td>
<td>'05'</td>
<td></td>
<td>CCT - Tag und Länge</td>
</tr>
<tr>
<td>'83'</td>
<td>'03'</td>
<td>'80 01 FF'</td>
<td>Schlüsselreferenz für KHBCI_Admin</td>
</tr>
<tr>
<td>'B8'</td>
<td>'08'</td>
<td></td>
<td>CT - Tag und Länge</td>
</tr>
<tr>
<td>'95'</td>
<td>'01'</td>
<td>'10'</td>
<td>Usage Qualifier: Nur für Kommandonachricht</td>
</tr>
<tr>
<td>'83'</td>
<td>'03'</td>
<td>'80 01 FF'</td>
<td>Schlüsselreferenz für KHBCI_Admin</td>
</tr>
</table>


Record 5 wird referenziert als Zugriffsregel von EF_KEYD, EF_SEQ, EF_PWDD
und EF_FBZ in SE #2.

APPEND RECORD, UPDATE RECORD: MAC-SM-AC für Kommando- und Ant-
wortnachricht mit dem Schlüssel KHBCI_Admin-


<table>
<tr>
<th>Tag</th>
<th>Länge</th>
<th>Wert</th>
<th>Erläuterung</th>
</tr>
<tr>
<td>'80'</td>
<td>'01'</td>
<td>'86'</td>
<td>Zugriffsart für APPEND RECORD, UPDATE RECORD</td>
</tr>
<tr>
<td>'B4'</td>
<td>'05'</td>
<td></td>
<td>CCT - Tag und Länge</td>
</tr>
<tr>
<td>'83'</td>
<td>'03'</td>
<td>'80 01 FF'</td>
<td>Schlüsselreferenz für KHBCI_Admin</td>
</tr>
</table>


<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: C</td>
<td>Version: 3.0 - Final Version</td>
<td>Financial Transaction Services (FinTS) Dokument: Security - Sicherheitsverfahren HBCI</td>
</tr>
<tr>
<td>Seite:</td>
<td rowspan="2">Stand: 18.07.2013</td>
<td>Kapitel: Chipapplikationen</td>
</tr>
<tr>
<td>112</td>
<td>Abschnitt: Chipapplikation für DDV</td>
</tr>
</table>


Record 6 wird referenziert als Zugriffsregel von EF_BNK und EF_SEQ in SE #1.

UPDATE RECORD: Karteninhaber-Authentikation (PWD) mit lokalem Passwort 1.
READ / SEARCH RECORD: ALW


<table>
<tr>
<th>Tag</th>
<th>Länge</th>
<th>Wert</th>
<th>Erläuterung</th>
</tr>
<tr>
<td>'80'</td>
<td>'01'</td>
<td>'82'</td>
<td>Zugriffsart für UPDATE RECORD</td>
</tr>
<tr>
<td>'A4'</td>
<td>'07'</td>
<td></td>
<td>AT - Tag und Länge</td>
</tr>
<tr>
<td>'95'</td>
<td>'01'</td>
<td>'08'</td>
<td>Usage Qualifier für Karteninhaber-Authentikation</td>
</tr>
<tr>
<td>'83'</td>
<td>'02'</td>
<td>'80 01'</td>
<td>Passwort-Referenz, lokales Passwort mit der Nummer 1</td>
</tr>
<tr>
<td>'80'</td>
<td>'01'</td>
<td>'81'</td>
<td>Zugriffsart für READ / SEARCH RECORD</td>
</tr>
<tr>
<td>'90'</td>
<td>'00'</td>
<td></td>
<td>ALW</td>
</tr>
</table>


Record 7 wird referenziert als Zugriffsregel von EF_MAC in SE #1.

UPDATE RECORD: Karteninhaber-Authentikation (PWD) mit lokalem Passwort 1.

READ / SEARCH RECORD: Karteninhaber-Authentikation (PWD) mit lokalem
Passwort 1 und MAC-SM-AC für die Antwortnachricht mit dem Schlüssel KDAK.


<table>
<tr>
<th>Tag</th>
<th>Länge</th>
<th>Wert</th>
<th>Erläuterung</th>
</tr>
<tr>
<td>'80'</td>
<td>'01'</td>
<td>'82'</td>
<td>Zugriffsart für UPDATE RECORD</td>
</tr>
<tr>
<td>'A4'</td>
<td>'07'</td>
<td></td>
<td>AT - Tag und Länge</td>
</tr>
<tr>
<td>'95'</td>
<td>'01'</td>
<td>'08'</td>
<td>Usage Qualifier für Karteninhaber-Authentikation</td>
</tr>
<tr>
<td>'83'</td>
<td>'02'</td>
<td>'80 01'</td>
<td>Passwort-Referenz, lokales Passwort mit der Nummer 1</td>
</tr>
<tr>
<td>'80'</td>
<td>'01'</td>
<td>'81'</td>
<td>Zugriffsart für READ / SEARCH RECORD</td>
</tr>
<tr>
<td>'AF'</td>
<td>'13'</td>
<td></td>
<td>AND - Template, Tag und Länge</td>
</tr>
<tr>
<td>'B4'</td>
<td>'08'</td>
<td></td>
<td>CCT - Tag und Länge</td>
</tr>
<tr>
<td>'95'</td>
<td>'01'</td>
<td>'20'</td>
<td>Usage Qualifier: Nur Antwortnachricht</td>
</tr>
<tr>
<td>'83'</td>
<td>'03'</td>
<td>'80 02 FF'</td>
<td>Schlüsselreferenz für KDAK</td>
</tr>
<tr>
<td>'A4'</td>
<td>'07'</td>
<td></td>
<td>AT - Tag und Länge</td>
</tr>
<tr>
<td>'95'</td>
<td>'01'</td>
<td>'08'</td>
<td>Usage Qualifier für Karteninhaber-Authentikation</td>
</tr>
<tr>
<td>'83'</td>
<td>'02'</td>
<td>'80 01'</td>
<td>Passwort-Referenz, lokales Passwort mit der Nummer 1</td>
</tr>
</table>


Record 8 wird referenziert als Zugriffsregel im EF_PWDD.

VERIFY, CHANGE REFERENCE DATA: ALW

RESET RETRY COUNTER: MAC-SM-AC für Kommando- und Antwortnachricht mit
KHBCI_Admin


<table>
<tr>
<th>Tag</th>
<th>Länge</th>
<th>Wert</th>
<th>Beschreibung</th>
</tr>
<tr>
<td>'80'</td>
<td>'01'</td>
<td>'83'</td>
<td>Zugriffsart für VERIFY, CHANGE REFERENCE DATA</td>
</tr>
<tr>
<td>'90'</td>
<td>'00'</td>
<td></td>
<td>ALW</td>
</tr>
<tr>
<td>'80'</td>
<td>'01'</td>
<td>'84'</td>
<td>Zugriffsart für Kommando: RESET RETRY COUNTER</td>
</tr>
<tr>
<td>'B4'</td>
<td>'05'</td>
<td></td>
<td>CCT - Tag und Länge</td>
</tr>
<tr>
<td>'83'</td>
<td>'03'</td>
<td>'80 01 FF'</td>
<td>Schlüsselreferenz für KHBCI_Admin</td>
</tr>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th>Version:</th>
<th>Kapitel:</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Security - Sicherheitsverfahren HBCI</td>
<td>3.0 - Final Version</td>
<td>C</td>
</tr>
<tr>
<td>Kapitel:</td>
<td>Chipapplikationen</td>
<td>Stand:</td>
<td>Seite:</td>
</tr>
<tr>
<td>Abschnitt:</td>
<td>Chipapplikation für DDV</td>
<td>18.07.2013</td>
<td>113</td>
</tr>
</table>


#### C.2.1.3 EF_KEY


##### . Beschreibung

Die applikationsspezifischen Schlüssel der Applikation HBCI-Banking sind im
EF_KEY des Applikationsverzeichnisses DF_BANKING_20 gespeichert. Dies sind

. ein 16 Byte langer kartenindividueller Schlüssel KHBCI_Admin mit der Schlüsselnum-
mer '01' zur Administration der Applikation DF_BANKING_20,

. ein 16 Byte langer kartenindividueller Schlüssel KDAK mit der Schlüsselnummer
'02' als kundenindividueller Daten-Authentikationsschlüssel (DAK = Data Authen-
tication Key)15, sowie

. ein 16 Byte langer kartenindividueller Schlüssel KENC mit der Schlüsselnummer
'03' als kundenindividueller Chiffrierschlüssel.

Die Schlüssel KHBCI_Admin, KDAK und KENC sind nur der HBCI-Chipkarte und
dem für sie zuständigen Hintergrundsystem bekannt. Sie werden jeweils aus einem
KGK (Key Generating Key) unter Verwendung der Kartenidentifikationsdaten im
EF_ID des MF abgeleitet (vgl. Kapitel 8.4.1 von [DATKOM]). Das zuständige Hinter-
grundsystem kennt die jeweiligen KGK und leitet die kartenindividuellen Schlüssel
bei Bedarf ab.

Es können pro logischer Schlüsselnummer verschiedene KGK verwendet werden.
Ein KGK wird wie alle daraus abgeleiteten Schlüssel anhand der Schlüsselversion
identifiziert. Die Schlüsselversion zur jeweiligen logischen Schlüsselnummer im zu-
gehörigen EF_KEYD zeigt an, aus welchem KGK der jeweilige kartenindividuelle
Schlüssel abgeleitet ist.


##### . Format

Für das EF_KEY des DF_BANKING_20 sind die folgenden FCP festzulegen:


<table>
<tr>
<th>Tag</th>
<th>Länge</th>
<th>Wert</th>
<th>Erläuterung</th>
</tr>
<tr>
<td>'62'</td>
<td>'16'</td>
<td></td>
<td>Tag und Länge für FCP</td>
</tr>
<tr>
<td>'82'</td>
<td>'05'</td>
<td>'12 41 00 12 03'</td>
<td>Datei-Deskriptor für lineares EF mit fester Re- cordlänge (18 Byte), 3 Records</td>
</tr>
<tr>
<td>'83'</td>
<td>'02'</td>
<td>'00 10'</td>
<td>Datei-ID des EF_KEY</td>
</tr>
<tr>
<td>'88'</td>
<td>'01'</td>
<td>'10'</td>
<td>SFI '02' für das EF_KEY</td>
</tr>
<tr>
<td>'A1'</td>
<td>'06'</td>
<td>'8B 04 00 30 02 04'</td>
<td>Zugriffsregel-Referenzen</td>
</tr>
</table>


Auf das EF_KEY darf nur im SE #2 zugegriffen werden.

Die Kommandos APPEND RECORD und UPDATE RECORD dürfen nur ausgeführt
werden, wenn sie mit Secure Messaging durchgeführt werden, der Record-Inhalt
verschlüsselt (ENC) ist und die Kommandonachricht mit einem MAC abgesichert ist.
Verschlüsselung und MAC-Bildung erfolgen mit dem KHBCI_Admin. Der Returncode
eines APPEND RECORD oder UPDATE RECORD wird mit dem KHBCI_Admin MAC-
gesichert. Das Kommando READ RECORD darf nie ausgeführt werden. (Zugriffsre-
gel im Record 4 des EF_RULE)

<!-- PageFooter: 15 Um den Begriff ,Signierschlüssel" für Anwendungen nach SigG bzw. EU-Richtlinie freizuhalten, wurde hier der Begriff ,,Daten-Authentikationsschlüssel“ gewählt. Im weiteren Text wird jedoch zur besseren Lesbarkeit weiterhin davon gesprochen, dass eine Nachricht mit diesem Schlüssel sig- niert wird. -->
<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: C</td>
<td>Version: 3.0 - Final Version</td>
<td>Financial Transaction Services (FinTS) Dokument: Security - Sicherheitsverfahren HBCI</td>
</tr>
<tr>
<td>Seite: 114</td>
<td>Stand: 18.07.2013</td>
<td>Kapitel: Chipapplikationen<br>Abschnitt: Chipapplikation für DDV</td>
</tr>
</table>


##### . Daten

Das EF_KEY im DF_BANKING_20 enthält 3 Records mit den DF-spezifischen
Schlüsseln des DF_BANKING_20.


<table>
<tr>
<th>Logische Schlüs- selnummer</th>
<th>Schlüssel-Version</th>
<th>Schlüssel</th>
</tr>
<tr>
<td>'01'</td>
<td>'XX'</td>
<td>16 Byte langer KHBCI_Admin</td>
</tr>
<tr>
<td>'02'</td>
<td>'XX'</td>
<td>16 Byte langer KDAK</td>
</tr>
<tr>
<td>'03'</td>
<td>'XX'</td>
<td>16 Byte langer KENC</td>
</tr>
</table>


Es werden die Schlüsselversionen 1 bis 127 verwendet.

<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th>Version:</th>
<th rowspan="2">Kapitel: C</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Security - Sicherheitsverfahren HBCI</td>
<td>3.0 - Final Version</td>
</tr>
<tr>
<td>Kapitel:</td>
<td>Chipapplikationen</td>
<td>Stand:</td>
<td>Seite:</td>
</tr>
<tr>
<td>Abschnitt:</td>
<td>Chipapplikation für DDV</td>
<td>18.07.2013</td>
<td>115</td>
</tr>
</table>


#### C.2.1.4 EF_KEYD


##### . Beschreibung

Das EF_KEYD im DF_BANKING_20 enthält die Zusatzinformationen zu den DF-
spezifischen Schlüsseln des DF_BANKING_20.


##### . Format

Für das EF_KEYD sind die folgenden FCP festzulegen:


<table>
<tr>
<th>Tag</th>
<th>Länge</th>
<th>Wert</th>
<th>Erläuterung</th>
</tr>
<tr>
<td>'62'</td>
<td>'1C'</td>
<td></td>
<td>Tag und Länge für FCP</td>
</tr>
<tr>
<td>'82'</td>
<td>'05'</td>
<td>'14 41 00 1C 03'</td>
<td>Datei-Deskriptor für lineares EF mit variab- ler Recordlänge (max. 28 Byte) und 3 Re- cords</td>
</tr>
<tr>
<td>'83'</td>
<td>'02'</td>
<td>'00 13'</td>
<td>Datei-ID des EF_KEYD</td>
</tr>
<tr>
<td>'85'</td>
<td>'02'</td>
<td>'00 48'</td>
<td>für Nutzdaten allokierter Speicherplatz in Byte</td>
</tr>
<tr>
<td>'88'</td>
<td>'01'</td>
<td>'F0'</td>
<td>SFI '1E' für das EF_KEYD</td>
</tr>
<tr>
<td>'A1'</td>
<td>'08'</td>
<td>'8B 06 00 30 01 02 02 05'</td>
<td>Zugriffsregel-Referenzen</td>
</tr>
</table>


Im SE #1 dürfen nur die Kommandos READ / SEARCH RECORD mit ungesicherter
Kommando und Antwortnachricht ausgeführt werden (Zugriffsregel im Record 2 des
EF_RULE).

Im SE #2 dürfen die Kommandos APPEND RECORD und UPDATE RECORD nur
ausgeführt werden, wenn sie mit Secure Messaging durchgeführt werden. Die MAC-
Bildung erfolgt für Kommando- und Antwortnachricht mit dem KHBCI_Admin (Zugriffs-
regel im Record 5 des EF_RULE).


##### ◆ Daten

Das EF_KEYD enthält 3 Records, die die Zusatzinformation zu den DF-spezifischen
Schlüsseln des DF_BANKING_20 enthalten.

Das Datenobjekt mit Tag '93' enthält im Wertfeld als zweites Byte die Version des
entsprechenden Schlüssels.

Im folgenden wird der Aufbau der Schlüsselzusatzinformation dargestellt:

Eintrag 1 (KHBCI_Admin):


<table>
<tr>
<th>Tag</th>
<th>Länge</th>
<th>Wert</th>
<th>Erläuterung</th>
</tr>
<tr>
<td>'93'</td>
<td>'02'</td>
<td>'01 XX'</td>
<td>Schlüsselnummer und Schlüssel-Version</td>
</tr>
<tr>
<td>'C0'</td>
<td>'02'</td>
<td>'81 10'</td>
<td>Symmetrischer Schlüssel der Länge 16 Byte</td>
</tr>
<tr>
<td>'90'</td>
<td>'01'</td>
<td>'FF'</td>
<td>Fehlbedienungszähler</td>
</tr>
<tr>
<td>'7B'</td>
<td>'0F'</td>
<td></td>
<td>SE-Datenobjekt</td>
</tr>
<tr>
<td>'80'</td>
<td>'01'</td>
<td>'02'</td>
<td>Festlegung für SE #2</td>
</tr>
<tr>
<td>'B4'</td>
<td>'04'</td>
<td></td>
<td>CCT - Tag und Länge (Usage Qualifier '30' ist Default- wert)</td>
</tr>
<tr>
<td>'89'</td>
<td>'02'</td>
<td>'12 22'</td>
<td>Algorithmus-ID: Schlüssel darf zur Bildung eines Retail-MAC im CFB-Mode verwendet werden</td>
</tr>
<tr>
<td>'B8'</td>
<td>'04'</td>
<td></td>
<td>CT - Tag und Länge (Usage Qualifier '10' ist Default- wert)</td>
</tr>
<tr>
<td>'89'</td>
<td>'02'</td>
<td>'11 23'</td>
<td>Algorithmus-ID: Schlüssel darf zur Verschlüsselung als Triple-DES Schlüssel im CBC-Mode mit ICV ≠ 0 und ICV-Variante verwendet werden</td>
</tr>
</table>


<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: C</td>
<td>Version: 3.0 - Final Version</td>
<td>Financial Transaction Services (FinTS) Dokument: Security - Sicherheitsverfahren HBCI</td>
</tr>
<tr>
<td>Seite:</td>
<td rowspan="2">Stand: 18.07.2013</td>
<td>Kapitel: Chipapplikationen</td>
</tr>
<tr>
<td>116</td>
<td>Abschnitt: Chipapplikation für DDV</td>
</tr>
</table>


#### Eintrag 2 (KDAK):


<table>
<caption>Eintrag 3 (KENC):</caption>
<tr>
<th>Tag</th>
<th>Länge</th>
<th>Wert</th>
<th>Erläuterung</th>
</tr>
<tr>
<td>'93'</td>
<td>'02'</td>
<td>'02 XX'</td>
<td>Schlüsselnummer und Schlüssel-Version</td>
</tr>
<tr>
<td>'C0'</td>
<td>'02'</td>
<td>'81 10'</td>
<td>Symmetrischer Schlüssel der Länge 16 Byte</td>
</tr>
<tr>
<td>'7B'</td>
<td>'0C'</td>
<td></td>
<td>SE-Datenobjekt</td>
</tr>
<tr>
<td>'80'</td>
<td>'01'</td>
<td>'01'</td>
<td>Festlegung für SE #1</td>
</tr>
<tr>
<td>'B4'</td>
<td>'07'</td>
<td></td>
<td>CCT - Tag und Länge</td>
</tr>
<tr>
<td>'95'</td>
<td>'01'</td>
<td>'20'</td>
<td>Usage Qualifier: Nur SM-Antwortnachricht</td>
</tr>
<tr>
<td>'89'</td>
<td>'02'</td>
<td>'12 22'</td>
<td>Algorithmus-ID: Schlüssel darf zur Bildung eines Retail-MAC im CFB-Mode verwendet werden</td>
</tr>
</table>


<table>
<tr>
<th>Tag</th>
<th>Länge</th>
<th>Wert</th>
<th>Erläuterung</th>
</tr>
<tr>
<td>'93'</td>
<td>'02'</td>
<td>'03 XX'</td>
<td>Schlüsselnummer und Schlüssel-Version</td>
</tr>
<tr>
<td>'C0'</td>
<td>'02'</td>
<td>'81 10'</td>
<td>Symmetrischer Schlüssel der Länge 16 Byte</td>
</tr>
<tr>
<td>'7B'</td>
<td>'0C'</td>
<td></td>
<td>SE-Datenobjekt</td>
</tr>
<tr>
<td>'80'</td>
<td>'01'</td>
<td>'01'</td>
<td>Festlegung für SE #1</td>
</tr>
<tr>
<td>'A4'</td>
<td>'07'</td>
<td></td>
<td>AT - Tag und Länge</td>
</tr>
<tr>
<td>'95'</td>
<td>'01'</td>
<td>'40'</td>
<td>Usage Qualifier: Nur interne Authentikation</td>
</tr>
<tr>
<td>'89'</td>
<td>'02'</td>
<td>'21 12'</td>
<td>Algorithmus-ID: Schlüssel darf zur Authentikation der Chipkarte mit Triple-DES verwendet werden</td>
</tr>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th>Version:</th>
<th>Kapitel:</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Security - Sicherheitsverfahren HBCI</td>
<td>3.0 - Final Version</td>
<td>C</td>
</tr>
<tr>
<td>Kapitel:</td>
<td>Chipapplikationen</td>
<td>Stand:</td>
<td>Seite:</td>
</tr>
<tr>
<td>Abschnitt:</td>
<td>Chipapplikation für DDV</td>
<td>18.07.2013</td>
<td>117</td>
</tr>
</table>


#### C.2.1.5 EF_PWD


##### . Beschreibung

Das lokale EF_PWD im DF_BANKING_20 enthält in dem 9 Byte langen Record '01'
die Länge der HBCI-PIN und einen Referenzwert der HBCI-PIN der ZKA-Chipkarte.
Die HBCI-PIN hat eine Mindestlänge von 5 Ziffern und darf maximal 12 Ziffern lang
sein.


##### . Format

Für das EF_PWD des DF_BANKING_20 sind die folgenden FCP festzulegen:


<table>
<tr>
<th>Tag</th>
<th>Länge</th>
<th>Wert</th>
<th>Erläuterung</th>
</tr>
<tr>
<td>'62'</td>
<td>'16'</td>
<td></td>
<td></td>
</tr>
<tr>
<td>'82'</td>
<td>'05'</td>
<td>'12 41 00 09 01'</td>
<td>Datei-Deskriptor für lineares EF mit fester Recordlän- ge von 9 Byte</td>
</tr>
<tr>
<td>'83'</td>
<td>'02'</td>
<td>'00 12'</td>
<td>Datei-ID des EF_PWD</td>
</tr>
<tr>
<td>'88'</td>
<td>'01'</td>
<td>'18'</td>
<td>SFI '03' für das EF_PWD</td>
</tr>
<tr>
<td>'A1'</td>
<td>'06'</td>
<td>'8B 04 00 30 02 04'</td>
<td>Zugriffsregel-Referenz</td>
</tr>
</table>


Auf das EF_PWD darf nur im SE #2 zugegriffen werden: Die Kommandos APPEND
RECORD und UPDATE RECORD dürfen nur ausgeführt werden, wenn sie mit
Secure Messaging durchgeführt werden, der Recordinhalt verschlüsselt (ENC) ist
und die Kommandonachricht mit einem MAC abgesichert ist. Verschlüsselung und
MAC-Bildung erfolgen dabei mit dem KHBCI_Admin. Der Returncode eines APPEND
RECORD oder UPDATE RECORD wird MAC-gesichert. Die MAC-Bildung erfolgt für
die Antwortnachricht mit dem KHBCI_Admin. Das Kommando READ RECORD darf
nie ausgeführt werden (Zugriffsregel im Record 4 des EF_RULE).


##### ◆ Daten

Der Record '01' des EF_PWD enthält einen Referenzwert der HBCI-PIN.


<table>
<tr>
<th>Byte</th>
<th>Inhalt</th>
<th>Beschreibung</th>
</tr>
<tr>
<td>1</td>
<td>'05'</td>
<td>Länge der PIN</td>
</tr>
<tr>
<td>2-9</td>
<td>'XX..XX'</td>
<td>Referenzwert der PIN</td>
</tr>
</table>


Zur Erzeugung des Referenzwertes wird aus der HBCI-PIN zunächst der 8 Byte
lange 'Format 2 PIN Block' gemäß [ISO PIN1] wie folgt gebildet:


<table>
<tr>
<td>CLPPPPP</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>P/F</td>
<td>P/F</td>
<td>P/F</td>
<td>P/F</td>
<td>P/F</td>
<td>P/F</td>
<td>P/F</td>
<td>F</td>
<td>F</td>
</tr>
</table>


#### Erläuterung:

Jedes Feld repräsentiert ein Halbbyte.

C: Kontroll-Feld, binär kodiert

hat immer den Wert '2'

L: PIN-Länge, binär kodiert

mögliche Werte von '5' bis 'C'

P: PIN-Ziffer, BCD-kodiert

F: Filler, binär kodiert

hat immer den Wert 'F'

P/F: PIN-Ziffer/Filler

Belegung abhängig von der PIN-Länge

<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: C</td>
<td>Version: 3.0 - Final Version</td>
<td>Financial Transaction Services (FinTS) Dokument: Security - Sicherheitsverfahren HBCI</td>
</tr>
<tr>
<td>Seite:<br>118</td>
<td>Stand: 18.07.2013</td>
<td>Kapitel: Chipapplikationen<br>Abschnitt: Chipapplikation für DDV</td>
</tr>
</table>


Der erzeugte Format 2 PIN Block wird mit PB bezeichnet. Aus diesem PIN Block
wird der zu speichernde Referenzwert durch DES-Verschlüsselung mit sich selbst
erzeugt:

PIN-Referenzwert: ePB(PB)

Falls erforderlich, wird vor der Verwendung von PB als DES-Schlüssel ein Parity Ad-
justment vorgenommen. PB wird als Klartext unverändert verwendet.

<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th>Version:</th>
<th rowspan="2">Kapitel: C</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Security - Sicherheitsverfahren HBCI</td>
<td>3.0 - Final Version</td>
</tr>
<tr>
<td>Kapitel:</td>
<td>Chipapplikationen</td>
<td>Stand:</td>
<td>Seite:</td>
</tr>
<tr>
<td>Abschnitt:</td>
<td>Chipapplikation für DDV</td>
<td>18.07.2013</td>
<td>119</td>
</tr>
</table>


#### C.2.1.6 EF_PWDD


##### . Beschreibung

Das EF_PWDD im DF_BANKING_20 enthält in Record '01' die Zusatzinformationen
zu der im EF_PWD des DF_BANKING_20 abgelegten HBCI-PIN.


##### . Format

Für das EF_PWDD sind die folgenden FCP festzulegen:


<table>
<tr>
<th>Tag</th>
<th>Länge</th>
<th>Wert</th>
<th>Erläuterung</th>
</tr>
<tr>
<td>'62'</td>
<td>'1C'</td>
<td></td>
<td></td>
</tr>
<tr>
<td>'82'</td>
<td>'05'</td>
<td>'14 41 00 15 01'</td>
<td>Datei-Deskriptor für lineares EF mit variabler Recordlänge (max. 21 Byte) und 1 Record</td>
</tr>
<tr>
<td>'83'</td>
<td>'02'</td>
<td>'00 15'</td>
<td>Datei-ID des EF_PWDD</td>
</tr>
<tr>
<td>'85'</td>
<td>'02'</td>
<td>'00 15'</td>
<td>Für Nutzdaten allokierter Speicherplatz in Byte</td>
</tr>
<tr>
<td>'88'</td>
<td>'01'</td>
<td>'20'</td>
<td>SFI '04' für das EF_PWDD</td>
</tr>
<tr>
<td>'A1'</td>
<td>'08'</td>
<td>'8B 06 00 30 01 02 02 05'</td>
<td>Zugriffsregel-Referenzen</td>
</tr>
</table>


Im SE #1 dürfen nur die Kommandos READ / SEARCH RECORD mit ungesicherter
Kommando und Antwortnachricht ausgeführt werden (Zugriffsregel im Record 2 des
EF_RULE).

Im SE #2 durfen APPEND RECORD und UPDATE RECORD nur ausgeführt wer-
den, wenn sie mit Secure Messaging durchgeführt werden und die Kommandonach-
richt mit einem MAC abgesichert ist. Der Returncode wird MAC-gesichert. Die MAC-
Bildung erfolgt für Kommando- und Antwortnachricht mit dem KHBCI_Admin (Zugriffs-
regel im Record 5 des EF_RULE).


##### ◆ Daten

Das lokale EF_PWDD enthält in Record '01' einen 21 Byte langen Record, der die
Zusatzinformationen zu der HBCI-PIN enthält.


<table>
<tr>
<th>Tag</th>
<th>Länge</th>
<th>Wert</th>
<th>Beschreibung</th>
</tr>
<tr>
<td>'93'</td>
<td>'02'</td>
<td>'01 01'</td>
<td>Passwortreferenz: Passwort '01' im Record '01' des EF_PWD</td>
</tr>
<tr>
<td>'89'</td>
<td>'02'</td>
<td>'11 50'</td>
<td>Speicherformat des Passwortes (minimal 5 Ziffern)</td>
</tr>
<tr>
<td>'7B'</td>
<td>'0B'</td>
<td></td>
<td>SE-DO, Tag und Länge</td>
</tr>
<tr>
<td>'80'</td>
<td>'01'</td>
<td>'00'</td>
<td>SE Referenz-DO: Für alle SEs</td>
</tr>
<tr>
<td>'A1'</td>
<td>'03'</td>
<td>'8B 01 08'</td>
<td>Zugriffsregel-Referenz</td>
</tr>
<tr>
<td>'89'</td>
<td>'01'</td>
<td>'12'</td>
<td>Übertragungsformat der Authentikationsda- ten: PIN Format 2 Block</td>
</tr>
</table>


<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: C</td>
<td>Version: 3.0 - Final Version</td>
<td>Financial Transaction Services (FinTS) Dokument: Security - Sicherheitsverfahren HBCI</td>
</tr>
<tr>
<td>Seite:</td>
<td rowspan="2">Stand: 18.07.2013</td>
<td>Kapitel: Chipapplikationen</td>
</tr>
<tr>
<td>120</td>
<td>Abschnitt: Chipapplikation für DDV</td>
</tr>
</table>


#### C.2.1.7 EF_FBZ


##### . Beschreibung

EF_FBZ bezeichnet das lineare EF, das in Record '01' den Fehlbedienungszähler
und den zugehörigen Initialwert für die im DF-spezifischen EF_PWD abgelegte
HBCI-PIN enthält.


##### . Format

Für das EF_FBZ im DF_BANKING_20 sind die folgenden FCP festzulegen:


<table>
<tr>
<th>Tag</th>
<th>Länge</th>
<th>Wert</th>
<th>Erläuterung</th>
</tr>
<tr>
<td>'62'</td>
<td>'18'</td>
<td></td>
<td>Tag und Länge für FCP</td>
</tr>
<tr>
<td>'82'</td>
<td>'05'</td>
<td>'12 41 00 02 01'</td>
<td>Datei-Deskriptor für lineares EF fester Re- cordlänge</td>
</tr>
<tr>
<td>'83'</td>
<td>'02'</td>
<td>'00 16'</td>
<td>Datei-ID des EF_FBZ</td>
</tr>
<tr>
<td>'88'</td>
<td>'01'</td>
<td>'28'</td>
<td>SFI '05' für das EF_FBZ</td>
</tr>
<tr>
<td>'A1'</td>
<td>'08'</td>
<td>'8B 06 00 30 01 02 02 05'</td>
<td>Zugriffsregel-Referenzen</td>
</tr>
</table>


Im SE # 1 dürfen nur die Kommandos READ / SEARCH RECORD mit ungesicherter
Kommando und Antwortnachricht ausgeführt werden (Zugriffsregel im Record 2 des
EF_RULE).

Im SE #2 dürfen die Kommandos APPEND RECORD und UPDATE RECORD nur
ausgeführt werden, wenn sie mit Secure Messaging durchgeführt werden und die
Kommandonachricht mit einem MAC abgesichert ist. Der Returncode wird MAC-
gesichert. Die MAC-Bildung erfolgt für Kommando- und Antwortnachricht mit dem
KHBCI_Admin (Zugriffsregel im Record 5 des EF_RULE).


##### . Daten

Das EF_FBZ enthält in Record '01' einen 2 Byte langen Record, der den Fehlbedie-
nungszähler und den zugehörigen Initialwert '03' für die HBCI-PIN enthält.


<table>
<tr>
<td>Initialwert des FBZ</td>
<td>FBZ</td>
</tr>
<tr>
<td>'03'</td>
<td>'03'</td>
</tr>
</table>


<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th>Version:</th>
<th>Kapitel:</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Security - Sicherheitsverfahren HBCI</td>
<td>3.0 - Final Version</td>
<td>C</td>
</tr>
<tr>
<td>Kapitel:</td>
<td>Chipapplikationen</td>
<td>Stand:</td>
<td>Seite:</td>
</tr>
<tr>
<td>Abschnitt:</td>
<td>Chipapplikation für DDV</td>
<td>18.07.2013</td>
<td>121</td>
</tr>
</table>


#### C.2.1.8 EF_BNK


##### . Beschreibung

Bei dem EF_BNK handelt es sich um ein lineares EF mit 5 Records in dem Bank-
verbindungen abgelegt sind.


##### . Format

Für das EF_BNK in einer HBCI-Chipkarte sind die folgenden FCP festzulegen:


<table>
<tr>
<th>Tag</th>
<th>Länge</th>
<th>Wert</th>
<th>Erläuterung</th>
</tr>
<tr>
<td>'62'</td>
<td>'18'</td>
<td></td>
<td>Tag und Länge für FCP</td>
</tr>
<tr>
<td>'82'</td>
<td>'05'</td>
<td>'12 41 00 58 05'</td>
<td>Datei-Deskriptor für lineares EF mit fester Recordlänge 88 Byte und 5 Records</td>
</tr>
<tr>
<td>'83'</td>
<td>'02'</td>
<td>'03 01'</td>
<td>Datei-ID des EF_BNK</td>
</tr>
<tr>
<td>'88'</td>
<td>'01'</td>
<td>'D0'</td>
<td>SFI '1A' für das EF_BNK</td>
</tr>
<tr>
<td>'A1'</td>
<td>'08'</td>
<td>'8B 06 00 30 01 06 02 03'</td>
<td>Zugriffsregel-Referenzen</td>
</tr>
</table>


Im SE #1 dürfen READ / SEARCH RECORD immer ausgeführt werden, die Ant-
wortnachricht wird nicht abgesichert. UPDATE RECORD darf nur ausgeführt wer-
den, wenn zuvor eine Karteninhaber-Authentikation mit dem lokalen Passwort 1
(HBCI-PIN) erfolgt ist. Der Returncode wird nicht MAC-gesichert (Zugriffsregeln im
Record 6 des EF_RULE).

Im SE #2 darf das Kommando APPEND RECORD nur ausgeführt werden, wenn es
mit Secure Messaging durchgeführt wird. Die MAC-Bildung erfolgt für Kommando-
und Antwortnachricht mit dem KHBCI_Admin (Zugriffsregel im Record 3 des EF_RULE).


##### . Daten

Die Records setzen sich aus einer Bankkurzbezeichnung, der Bankleitzahl, dem
Kommunikationsdienst, der Adresse und dem Adresszusatz für den Kommunikati-
onszugang, dem Länderkennzeichen und der Benutzerkennung zusammen.


<table>
<tr>
<th>Byte</th>
<th>Länge</th>
<th>Wert</th>
<th>Erläuterung</th>
</tr>
<tr>
<td>1-20</td>
<td>20</td>
<td>'aa .. aa'</td>
<td>Kurzbezeichner des Kreditinstituts</td>
</tr>
<tr>
<td>21-24</td>
<td>4</td>
<td>'nn nn nn nn'</td>
<td>Kreditinstitutscode des kontoführenden Instituts</td>
</tr>
<tr>
<td>25-25</td>
<td>1</td>
<td>'n'</td>
<td>Kommunikationsdienst</td>
</tr>
<tr>
<td>26-53</td>
<td>28</td>
<td>'aa .. aa'</td>
<td>Kommunikationsadresse</td>
</tr>
<tr>
<td>54-55</td>
<td>2</td>
<td>'aa aa'</td>
<td>Kommunikationsadressenzusatz</td>
</tr>
<tr>
<td>56-58</td>
<td>3</td>
<td>'aa aa aa'</td>
<td>Länderkennzeichen des kontoführenden Instituts</td>
</tr>
<tr>
<td>59-88</td>
<td>30</td>
<td>'aa .. aa'</td>
<td>Benutzerkennung</td>
</tr>
</table>


Alphanumerische Feldinhalte ('a') werden ASCII-kodiert, linksbündig eingestellt und
mit Leerzeichen (X'20') auf die vorgegebene Länge aufgefüllt. Numerische Feldin-
halte ('n') werden BCD-kodiert.

<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: C</td>
<td>Version: 3.0 - Final Version</td>
<td>Financial Transaction Services (FinTS) Dokument: Security - Sicherheitsverfahren HBCI</td>
</tr>
<tr>
<td>Seite:</td>
<td rowspan="2">Stand: 18.07.2013</td>
<td>Kapitel: Chipapplikationen</td>
</tr>
<tr>
<td>122</td>
<td>Abschnitt: Chipapplikation für DDV</td>
</tr>
</table>


#### C.2.1.9 EF_MAC


##### . Beschreibung

Das EF_MAC wird für die MAC-Bildung über den Hashwert einer Nachricht benötigt.
Es besteht aus einem 12 Byte langem Record deren Zugriffsregeln so gesetzt wer-
den müssen, dass beim Lesen des Records der MAC produziert wird.


##### . Format

Für das EF_MAC sind die folgenden FCP festzulegen:


<table>
<tr>
<th>Tag</th>
<th>Länge</th>
<th>Wert</th>
<th>Erläuterung</th>
</tr>
<tr>
<td>'62'</td>
<td>'18'</td>
<td></td>
<td>Tag und Länge für FCP</td>
</tr>
<tr>
<td>'82'</td>
<td>'05'</td>
<td>'12 41 00 0C 01'</td>
<td>Datei-Deskriptor für lineares EF mit einem Record der Länge 12 Byte</td>
</tr>
<tr>
<td>'83'</td>
<td>'02'</td>
<td>'03 02'</td>
<td>Datei-ID des EF_MAC</td>
</tr>
<tr>
<td>'88'</td>
<td>'01'</td>
<td>'D8'</td>
<td>SFI '1B' für das EF_MAC</td>
</tr>
<tr>
<td>'A1'</td>
<td>'08'</td>
<td>'8B 06 00 30 01 07 02 03'</td>
<td>Zugriffsregel-Referenzen</td>
</tr>
</table>


Im SE #1 dürfen READ / SEARCH RECORD nach Karteninhaber-Authentikation
ausgeführt werden, die Antwortnachricht wird mit einem KDAK-MAC versehen.
UPDATE RECORD darf nur ausgeführt werden, wenn zuvor eine Karteninhaber-
Authentikation mit dem lokalen Passwort 1 (HBCI-PIN) erfolgt ist. Der Returncode
eines UPDATE RECORD wird nicht MAC-gesichert (Zugriffsregeln im Record 7 des
EF_RULE).

Im SE #2 darf das Kommando APPEND RECORD nur ausgeführt werden, wenn es
mit Secure Messaging durchgeführt wird. Die MAC-Bildung erfolgt für Kommando-
und Antwortnachricht mit dem KHBCI_Admin (Zugriffsregel im Record 3 des EF_RULE).


##### . Daten

Das EF_MAC enthält einen Record, der den folgenden Aufbau hat:


<table>
<tr>
<th>Byte</th>
<th>Wert</th>
<th>Erläuterung</th>
</tr>
<tr>
<td>1-12</td>
<td>'XX..XX'</td>
<td>Hashwert</td>
</tr>
</table>


<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th>Version:</th>
<th>Kapitel:</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Security - Sicherheitsverfahren HBCI</td>
<td>3.0 - Final Version</td>
<td>C</td>
</tr>
<tr>
<td>Kapitel:</td>
<td>Chipapplikationen</td>
<td>Stand:</td>
<td>Seite:</td>
</tr>
<tr>
<td>Abschnitt:</td>
<td>Chipapplikation für DDV</td>
<td>18.07.2013</td>
<td>123</td>
</tr>
</table>


#### C.2.1.10 EF_SEQ


##### . Beschreibung

Bei dem EF_SEQ handelt es sich um ein lineares EF, dessen Record ein 2 Byte
langes binär definiertes Element enthält. Dieser binäre aufsteigende Zähler fließt als
Sicherheitsreferenznummer (Signatur-ID) zur Absicherung der Daten gegen Doppe-
leinreichung ein. Der Startwert des Zählers ist 1. Ein Rücksetzen bei Überlauf findet
nicht statt.


##### . Format

Für das EF_SEQ sind die folgenden FCP festzulegen:


<table>
<tr>
<th>Tag</th>
<th>Länge</th>
<th>Wert</th>
<th>Erläuterung</th>
</tr>
<tr>
<td>'62'</td>
<td>'18'</td>
<td></td>
<td>Tag und Länge für FCP</td>
</tr>
<tr>
<td>'82'</td>
<td>'05'</td>
<td>'12 41 00 02 01'</td>
<td>Datei-Deskriptor für lineares EF mit 1 Record der Länge 2 Byte</td>
</tr>
<tr>
<td>'83'</td>
<td>'02'</td>
<td>'03 03'</td>
<td>Datei-ID des EF_SEQ</td>
</tr>
<tr>
<td>'88'</td>
<td>'01'</td>
<td>'E0'</td>
<td>SFI '1C' für das EF_SEQ</td>
</tr>
<tr>
<td>'A1'</td>
<td>'08'</td>
<td>'8B 06 00 30 01 06 02 05'</td>
<td>Zugriffsregel-Referenzen</td>
</tr>
</table>


Im SE #1 dürfen READ / SEARCH RECORD immer ausgeführt werden, die Ant-
wortnachricht wird nicht abgesichert. UPDATE RECORD darf nur ausgeführt wer-
den, wenn zuvor eine Karteninhaber-Authentikation mit dem lokalen Passwort 1
(HBCI-PIN) erfolgt ist. Der Returncode wird nicht MAC-gesichert (Zugriffsregeln im
Record 6 des EF_RULE).

Im SE #2 dürfen die Kommandos APPEND RECORD und UPDATE RECORD nur
ausgeführt werden, wenn sie mit Secure Messaging durchgeführt werden. Die MAC-
Bildung erfolgt für Kommando- und Antwortnachrichten jeweils mit dem KHBCI_Admin
(Zugriffsregel im Record 5 des EF_RULE).


##### . Daten

Das EF_SEQ enthält 1 Record, der den folgenden Aufbau hat:


<table>
<tr>
<th>Byte</th>
<th>Wert</th>
<th>Erläuterung</th>
</tr>
<tr>
<td>1-2</td>
<td>'XX XX'</td>
<td>Sequenznummer</td>
</tr>
<tr>
<td>Kapitel: C</td>
<td>Version: 3.0 - Final Version</td>
<td>Financial Transaction Services (FinTS) Dokument: Security - Sicherheitsverfahren HBCI</td>
</tr>
<tr>
<td rowspan="2">Seite:<br>124</td>
<td rowspan="2">Stand: 18.07.2013</td>
<td>Kapitel: Chipapplikationen</td>
</tr>
<tr>
<td>Abschnitt: Chipapplikation für DDV</td>
</tr>
</table>


#### C.2.2 Daten der Applikation HBCI-Banking für SECCOS 6

Die folgende Grafik gibt eine Übersicht über die Dateien einer HBCI-Karte mit der
Applikation HBCI-Banking für Seccos 6.


Abbildung 21: Datenelemente der Applikation "HBCI", Bankensignaturkarte mit Zerti-
fikat

![MF EF_KEY EF_KEYD EF_PWD EF_PWDD EF_FBZ EF_ID EF_INFO EF_RULE EF_SIG EF_SIGD DF_BANKING_20 EF_KEY EF_KEYD EF_RULE EF_BNK EF_MAC EF_SEQ EF_PWD EF_PWDD EF_FBZ](figures/138.1)


<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th>Version:</th>
<th>Kapitel:</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Security - Sicherheitsverfahren HBCI</td>
<td>3.0 - Final Version</td>
<td>C</td>
</tr>
<tr>
<td>Kapitel:</td>
<td>Chipapplikationen</td>
<td>Stand:</td>
<td>Seite:</td>
</tr>
<tr>
<td>Abschnitt:</td>
<td>Chipapplikation für DDV</td>
<td>18.07.2013</td>
<td>125</td>
</tr>
</table>


Abbildung 22: Datenelemente der Applikation "HBCI", Bankensignaturkarte ohne
Zertifikat

![MF EF_KEY EF_KEYD EF_ID EF_RULE EF_SIG EF_SIGD DF_BANKING_20 EF_KEY EF_KEYD EF_RULE EF_BNK EF_MAC EF_SEQ EF_PWD EF_PWDD EF_FBZ](figures/139.1)


<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: C</td>
<td>Version: 3.0 - Final Version</td>
<td>Financial Transaction Services (FinTS) Dokument: Security - Sicherheitsverfahren HBCI</td>
</tr>
<tr>
<td>Seite:</td>
<td rowspan="2">Stand: 18.07.2013</td>
<td>Kapitel: Chipapplikationen</td>
</tr>
<tr>
<td>126</td>
<td>Abschnitt: Chipapplikation für DDV</td>
</tr>
</table>


#### C.2.2.1 ADF der Applikation HBCI-Banking

Für das ADF der Applikation HBCI-Banking (DF_BANKING_20) sind beim Anlegen
die folgenden FCP festzulegen:


<table>
<tr>
<th>Tag</th>
<th>Länge</th>
<th>Wert</th>
<th>Erläuterung</th>
</tr>
<tr>
<td>'62'</td>
<td>'1A'</td>
<td></td>
<td>Tag und Länge für FCP</td>
</tr>
<tr>
<td>'82'</td>
<td>'01'</td>
<td>'38'</td>
<td>Datei-Deskriptor für DF</td>
</tr>
<tr>
<td>'83'</td>
<td>'02'</td>
<td>'A6 00'</td>
<td>Datei-ID des DF_BANKING_20</td>
</tr>
<tr>
<td>'84'</td>
<td>'09'</td>
<td>'D2 76 00 00 25 48 42 02 00'</td>
<td>DF-Name (AID) des DF_BANKING_20</td>
</tr>
<tr>
<td>'A1'</td>
<td>'06'</td>
<td>'8B 04 00 30 02 01'</td>
<td>Zugriffsregel-Referenzen</td>
</tr>
<tr>
<td>'A2'</td>
<td>'09'</td>
<td>'88 01 C8 51 04 3F 00 00 03'</td>
<td>SFI-Template: SFI '19' für das EF_ID im MF (Datei-ID: 00 03')</td>
</tr>
</table>


Der DF-Name (die AID) des DF_BANKING_20 bestehend aus der nationalen RID
des ZKA ('D2 76 00 00 25'), der ASCII-kodierten Kennung "HB" ('48 42') sowie der
Version der Applikation 2.0 ('02 00').

Die Zugriffsregeln für das DF_BANKING_20 stehen in der zugeordneten Regeldatei
EF_RULE. Durch die Zugriffsregeln werden für die DF-spezifischen Kommandos die
folgenden Festlegungen getroffen:

Wenn das DF_BANKING_20 selektiert ist, darf ein CREATE FILE (EF) oder ein
DELETE FILE (self) nur ausgeführt werden, wenn die Kommandonachricht mit
Secure Messaging ausgeführt wird und mit einem korrekten MAC versehen ist, der
unter Verwendung des Schlüssels KHBCI_Admin aus dem EF_KEY des
DF_BANKING_20 gebildet ist. Der Returncode wird für jedes dieser Kommandos
durch die Karte mit einem MAC mit dem Schlüssel KHBCI_Admin versehen. Die
Kommandos CREATE FILE (DF), DELETE FILE (child DF), ACTIVATE,
DEACTIVATE und TERMINATE dürfen nie ausgeführt werden. Alle zulässigen Ad-
ministrationskommandos dürfen nur im SE #2 ausgeführt werden (Zugriffsregeln im
Record 1 des EF_RULE).

Der Applikation HBCI-Banking sind 10 Dateien als AEF zuzuordnen:

SFI '01':
EF_RULE im DF_BANKING_20

SFI '02':
EF_KEY im DF_BANKING_20,

SFI '03':
EF_PWD im DF_BANKING_20,

SFI '04':
EF_PWDD im DF_BANKING_20,

SFI '05':
EF_FBZ im DF_BANKING_20,

SFI '19':
EF_ID im MF,

SFI '1A':
EF_BNK im DF_BANKING_20,

SFI '1B':
EF_MAC im DF_BANKING_20,

SFI '1C':
EF_SEQ im DF_BANKING_20,

SFI '1E':
EF_KEYD im DF_BANKING_20.

Wenn das DF_BANKING_20 mittels SELECT FILE selektiert wird und die entspre-
chende Option im Parameterbyte P2 des Kommandos gesetzt ist, wird die folgende
FCI ausgegeben:

<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th>Version:</th>
<th>Kapitel:</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Security - Sicherheitsverfahren HBCI</td>
<td>3.0 - Final Version</td>
<td>C</td>
</tr>
<tr>
<td>Kapitel:</td>
<td>Chipapplikationen</td>
<td>Stand:</td>
<td>Seite:</td>
</tr>
<tr>
<td>Abschnitt:</td>
<td>Chipapplikation für DDV</td>
<td>18.07.2013</td>
<td>127</td>
</tr>
</table>


<table>
<tr>
<th>Tag</th>
<th>Länge</th>
<th>Wert</th>
<th>Erläuterung</th>
</tr>
<tr>
<td>'6F'</td>
<td>'0D'</td>
<td></td>
<td>Tag und Länge für FCI</td>
</tr>
<tr>
<td>'84'</td>
<td>'09'</td>
<td>'D2 76 00 00 25 48 42 02 00'</td>
<td>DF-Name (AID) des DF_BANKING_20</td>
</tr>
<tr>
<td>'A5'</td>
<td>'00'</td>
<td></td>
<td>keine proprietären Informationen</td>
</tr>
</table>


Wird das DF_BANKING_20 mittels SELECT FILE selektiert und die entsprechende
Option im Parameterbyte P2 des Kommandos gesetzt, werden die folgenden FMD
mit den Pfaden der AEFs ausgegeben (vorausgesetzt, das DF_BANKING_20 befin-
det sich direkt im MF):


<table>
<tr>
<th>Tag</th>
<th>Länge</th>
<th>Wert</th>
<th>Erläuterung</th>
</tr>
<tr>
<td>'64'</td>
<td>'6E'</td>
<td></td>
<td>Tag und Länge für FMD</td>
</tr>
<tr>
<td>'A2'</td>
<td>'6C'</td>
<td></td>
<td>Tag und Länge SFI-Template</td>
</tr>
<tr>
<td>'88'</td>
<td>'01'</td>
<td>'08'</td>
<td>SFI '01' (EF_RULE im DF_BANKING_20)</td>
</tr>
<tr>
<td>'51'</td>
<td>'06'</td>
<td>'3F 00 A6 00 00 30'</td>
<td>Pfad für AEF mit SFI '01'</td>
</tr>
<tr>
<td>'88'</td>
<td>'01'</td>
<td>'10'</td>
<td>SFI '02' (EF_KEY im DF_BANKING_20)</td>
</tr>
<tr>
<td>'51'</td>
<td>'06'</td>
<td>'3F 00 A6 00 00 10'</td>
<td>Pfad für AEF mit SFI '02'</td>
</tr>
<tr>
<td>'85'</td>
<td>'01'</td>
<td>'18'</td>
<td>SFI '03' (EF_PWD im DF_BANKING_20)</td>
</tr>
<tr>
<td>'51'</td>
<td>'06'</td>
<td>'3F 00 A6 00 00 12'</td>
<td>Pfad für AEF mit SFI '03'</td>
</tr>
<tr>
<td>'85'</td>
<td>'01'</td>
<td>'20'</td>
<td>SFI '04' (EF_PWDD im DF_BANKING_20)</td>
</tr>
<tr>
<td>'51'</td>
<td>'06'</td>
<td>'3F 00 A6 00 00 15'</td>
<td>Pfad für AEF mit SFI '04'</td>
</tr>
<tr>
<td>'85'</td>
<td>'01'</td>
<td>'28'</td>
<td>SFI '05' (EF_FBZ im DF_BANKING_20)</td>
</tr>
<tr>
<td>'51'</td>
<td>'06'</td>
<td>'3F 00 A6 00 00 16'</td>
<td>Pfad für AEF mit SFI '05'</td>
</tr>
<tr>
<td>'88'</td>
<td>'01'</td>
<td>'C8'</td>
<td>SFI '19' (EF_ID im MF)</td>
</tr>
<tr>
<td>'51'</td>
<td>'04'</td>
<td>'3F 00 00 03'</td>
<td>Pfad für AEF mit SFI '19'</td>
</tr>
<tr>
<td>'85'</td>
<td>'01'</td>
<td>'D0'</td>
<td>SFI '1A' (EF_BNK im DF_BANKING_20)</td>
</tr>
<tr>
<td>'51'</td>
<td>'06'</td>
<td>'3F 00 A6 00 03 01'</td>
<td>Pfad für AEF mit SFI '1A'</td>
</tr>
<tr>
<td>'85'</td>
<td>'01'</td>
<td>'D8'</td>
<td>SFI '1B' (EF_MAC im DF_BANKING_20)</td>
</tr>
<tr>
<td>'51'</td>
<td>,90,</td>
<td>'3F 00 A6 00 03 02'</td>
<td>Pfad für AEF mit SFI '1B'</td>
</tr>
<tr>
<td>'85'</td>
<td>'01'</td>
<td>'E0'</td>
<td>SFI '1C' (EF_SEQ im DF_BANKING_20)</td>
</tr>
<tr>
<td>'51'</td>
<td>'06'</td>
<td>'3F 00 A6 00 03 03'</td>
<td>Pfad für AEF mit SFI '1C'</td>
</tr>
<tr>
<td>'85'</td>
<td>'01'</td>
<td>'F0'</td>
<td>SFI '1E' (EF_KEYD im DF_BANKING_20)</td>
</tr>
<tr>
<td>'51'</td>
<td>,90,</td>
<td>'3F 00 A6 00 00 13'</td>
<td>Pfad für AEF mit SFI '1E'</td>
</tr>
</table>


<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: C</td>
<td>Version: 3.0 - Final Version</td>
<td>Financial Transaction Services (FinTS) Dokument: Security - Sicherheitsverfahren HBCI</td>
</tr>
<tr>
<td>Seite: 128</td>
<td>Stand: 18.07.2013</td>
<td>Kapitel: Chipapplikationen<br>Abschnitt: Chipapplikation für DDV</td>
</tr>
</table>


#### C.2.2.2 EF_RULE


##### . Beschreibung

Die Datei EF_RULE enthält die Zugriffsregeln für die Applikation DF_BANKING_20.
In den FCP von Dateien und Verzeichnissen wird auf diese Zugriffsregeln referen-
ziert.


##### . Format

Für das EF_RULE des DF_BANKING_20 sind die folgenden FCP festzulegen:


<table>
<tr>
<th>Tag</th>
<th>Länge</th>
<th>Wert</th>
<th>Erläuterung</th>
</tr>
<tr>
<td>'62'</td>
<td>'1C'</td>
<td></td>
<td>Tag und Länge für FCP</td>
</tr>
<tr>
<td>'82'</td>
<td>'05'</td>
<td>'14 41 00 24 08'</td>
<td>Datei-Deskriptor für lineares EF mit variab- ler Recordlänge (max. 36 Byte), 8 Records</td>
</tr>
<tr>
<td>'83'</td>
<td>'02'</td>
<td>'00 30'</td>
<td>Datei-ID des EF_RULE</td>
</tr>
<tr>
<td>'85'</td>
<td>'02'</td>
<td>'00 7D'</td>
<td>für Nutzdaten allokierter Speicherplatz in Byte</td>
</tr>
<tr>
<td>'88'</td>
<td>'01'</td>
<td>'08'</td>
<td>SFI '01' für das EF_RULE</td>
</tr>
<tr>
<td>'A1'</td>
<td>'08'</td>
<td>'8B 06 00 30 01 02 02 03'</td>
<td>Zugriffsregel-Referenzen</td>
</tr>
</table>


Im SE #1 dürfen nur die Kommandos READ / SEARCH RECORD mit ungesicherter
Kommando und Antwortnachricht ausgeführt werden (Zugriffsregel im Record 2 des
EF_RULE).

Im SE #2 darf APPEND RECORD nur ausgeführt werden, wenn es mit Secure
Messaging ausgeführt wird. Die MAC-Bildung erfolgt für Kommando- und Antwort-
nachricht mit dem KHBCI_Admin. UPDATE RECORD darf nie ausgeführt werden (Zu-
griffsregel im Record 3 des EF_RULE).


##### . Daten

Das EF_RULE im DF_BANKING_20 enthält 8 Records mit den Zugriffsregeln für
das Verzeichnis und die Datenfelder des Verzeichnisses.

Die folgende Tabelle zeigt die Belegung dieser Records für eine HBCI-Chipkarte:


<table>
<tr>
<th>Rec.Nr.</th>
<th>Record-Inhalt</th>
<th>Byte</th>
</tr>
<tr>
<td>1</td>
<td>'80 01 42 B4 05 83 03 80 01 FF'</td>
<td>10</td>
</tr>
<tr>
<td>2</td>
<td>'80 01 01 90 00'</td>
<td>5</td>
</tr>
<tr>
<td>3</td>
<td>'80 01 04 B4 05 83 03 80 01 FF'</td>
<td>10</td>
</tr>
<tr>
<td>4</td>
<td>'80 01 06 AF 11 B4 05 83 03 80 01 FF B8 08 95 01 10 83 03 80 01 FF'</td>
<td>22</td>
</tr>
<tr>
<td>5</td>
<td>'80 01 06 B4 05 83 03 80 01 FF'</td>
<td>10</td>
</tr>
<tr>
<td>6</td>
<td>'80 01 02 A4 07 95 01 08 83 02 80 01 80 01 01 90 00'</td>
<td>17</td>
</tr>
<tr>
<td>7</td>
<td>'80 01 02 A4 07 95 01 08 83 02 80 01 80 01 01 AF 13 B4 08 95 01 20 83 03 80 02 FF A4 07 95 01 08 83 02 80 01'</td>
<td>36</td>
</tr>
<tr>
<td>8</td>
<td>'80 01 03 90 00 80 01 84 B4 05 83 03 80 01 FF'</td>
<td>15</td>
</tr>
</table>


Die Records 1 bis 5 enthalten jeweils eine, die Records 6 bis 8 jeweils zwei Zugriffs-
regeln.

Im folgenden werden die einzelnen Records des EF_RULE näher erläutert.

Record 1 wird referenziert als Zugriffsregel von DF_BANKING_20 in SE #2.

<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th>Version:</th>
<th>Kapitel:</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Security - Sicherheitsverfahren HBCI</td>
<td>3.0 - Final Version</td>
<td>C</td>
</tr>
<tr>
<td>Kapitel:</td>
<td>Chipapplikationen</td>
<td>Stand:</td>
<td>Seite:</td>
</tr>
<tr>
<td>Abschnitt:</td>
<td>Chipapplikation für DDV</td>
<td>18.07.2013</td>
<td>129</td>
</tr>
</table>


#### CREATE FILE (EF), DELETE FILE (self): MAC-SM-AC für Kommando- und Ant- wortnachricht mit KHBCI_Admin:


<table>
<tr>
<th>Tag</th>
<th>Länge</th>
<th>Wert</th>
<th>Erläuterung</th>
</tr>
<tr>
<td>'80'</td>
<td>'01'</td>
<td>'42'</td>
<td>Zugriffsart für CREATE FILE (EF), DELETE FILE (self)</td>
</tr>
<tr>
<td>'B4'</td>
<td>'05'</td>
<td></td>
<td>CCT - Tag und Länge</td>
</tr>
<tr>
<td>'83'</td>
<td>'03'</td>
<td>'80 01 FF'</td>
<td>Schlüsselreferenz für KHBCI_Admin</td>
</tr>
</table>


Record 2 wird referenziert als Zugriffsregel von EF_RULE, EF_KEYD, EF_PWDD
und EF_FBZ in SE #1.

READ / SEARCH RECORD: ALW


<table>
<tr>
<th>Tag</th>
<th>Länge</th>
<th>Wert</th>
<th>Erläuterung</th>
</tr>
<tr>
<td>'80'</td>
<td>'01'</td>
<td>'01'</td>
<td>Zugriffsart für READ / SEARCH RECORD</td>
</tr>
<tr>
<td>'90'</td>
<td>'00'</td>
<td></td>
<td>Zugriffsbedingung ALW</td>
</tr>
</table>


Record 3 wird referenziert als Zugriffsregel von EF_RULE, EF_BNK und EF_MAC
in SE #2.

APPEND RECORD: MAC-SM-AC für Kommando- und Antwortnachricht mit dem
Schlüssel KHBCI_Admin·


<table>
<tr>
<th>Tag</th>
<th>Länge</th>
<th>Wert</th>
<th>Erläuterung</th>
</tr>
<tr>
<td>'80'</td>
<td>'01'</td>
<td>'04'</td>
<td>Zugriffsart für APPEND RECORD</td>
</tr>
<tr>
<td>'B4'</td>
<td>'05'</td>
<td></td>
<td>CCT - Tag und Länge</td>
</tr>
<tr>
<td>'83'</td>
<td>'03'</td>
<td>'80 01 FF'</td>
<td>Schlüsselreferenz für KHBCI_Admin</td>
</tr>
</table>


Record 4 wird referenziert als Zugriffsregel von EF_KEY und EF_PWD in SE #2.

APPEND RECORD, UPDATE RECORD: MAC-ENC-SM-AC für Kommandonach-
richt und MAC-SM-AC für Antwortnachricht mit KHBCI_Admin.


<table>
<tr>
<th>Tag</th>
<th>Länge</th>
<th>Wert</th>
<th>Erläuterung</th>
</tr>
<tr>
<td>'80'</td>
<td>'01'</td>
<td>'06'</td>
<td>Zugriffsart für APPEND RECORD, UPDATE RECORD</td>
</tr>
<tr>
<td>'AF'</td>
<td>'11'</td>
<td></td>
<td>AND- Template, Tag und Länge</td>
</tr>
<tr>
<td>'B4'</td>
<td>'05'</td>
<td></td>
<td>CCT - Tag und Länge</td>
</tr>
<tr>
<td>'83'</td>
<td>'03'</td>
<td>'80 01 FF'</td>
<td>Schlüsselreferenz für KHBCI_Admin</td>
</tr>
<tr>
<td>'B8'</td>
<td>'08'</td>
<td></td>
<td>CT - Tag und Länge</td>
</tr>
<tr>
<td>'95'</td>
<td>'01'</td>
<td>'10'</td>
<td>Usage Qualifier: Nur für Kommandonachricht</td>
</tr>
<tr>
<td>'83'</td>
<td>'03'</td>
<td>'80 01 FF'</td>
<td>Schlüsselreferenz für KHBCI_Admin</td>
</tr>
</table>


Record 5 wird referenziert als Zugriffsregel von EF_KEYD, EF_SEQ, EF_PWDD
und EF_FBZ in SE #2.

APPEND RECORD, UPDATE RECORD: MAC-SM-AC für Kommando- und Ant-
wortnachricht mit dem Schlüssel KHBCI_Admin.


<table>
<tr>
<th>Tag</th>
<th>Länge</th>
<th>Wert</th>
<th>Erläuterung</th>
</tr>
<tr>
<td>'80'</td>
<td>'01'</td>
<td>'06'</td>
<td>Zugriffsart für APPEND RECORD, UPDATE RECORD</td>
</tr>
<tr>
<td>'B4'</td>
<td>'05'</td>
<td></td>
<td>CCT - Tag und Länge</td>
</tr>
<tr>
<td>'83'</td>
<td>'03'</td>
<td>'80 01 FF'</td>
<td>Schlüsselreferenz für KHBCI_Admin</td>
</tr>
</table>


<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: C</td>
<td>Version: 3.0 - Final Version</td>
<td>Financial Transaction Services (FinTS) Dokument: Security - Sicherheitsverfahren HBCI</td>
</tr>
<tr>
<td>Seite:</td>
<td rowspan="2">Stand: 18.07.2013</td>
<td>Kapitel: Chipapplikationen</td>
</tr>
<tr>
<td>130</td>
<td>Abschnitt: Chipapplikation für DDV</td>
</tr>
</table>


Record 6 wird referenziert als Zugriffsregel von EF_BNK und EF_SEQ in SE #1.

UPDATE RECORD: Karteninhaber-Authentikation (PWD) mit lokalem Passwort 1.
READ / SEARCH RECORD: ALW


<table>
<tr>
<th>Tag</th>
<th>Länge</th>
<th>Wert</th>
<th>Erläuterung</th>
</tr>
<tr>
<td>'80'</td>
<td>'01'</td>
<td>'02'</td>
<td>Zugriffsart für UPDATE RECORD</td>
</tr>
<tr>
<td>'A4'</td>
<td>'07'</td>
<td></td>
<td>AT - Tag und Länge</td>
</tr>
<tr>
<td>'95'</td>
<td>'01'</td>
<td>'08'</td>
<td>Usage Qualifier für Karteninhaber-Authentikation</td>
</tr>
<tr>
<td>'83'</td>
<td>'02'</td>
<td>'80 01'</td>
<td>Passwort-Referenz, lokales Passwort mit der Nummer 1</td>
</tr>
<tr>
<td>'80'</td>
<td>'01'</td>
<td>'01'</td>
<td>Zugriffsart für READ / SEARCH RECORD</td>
</tr>
<tr>
<td>'90'</td>
<td>'00'</td>
<td></td>
<td>ALW</td>
</tr>
</table>


Record 7 wird referenziert als Zugriffsregel von EF_MAC in SE #1.

UPDATE RECORD: Karteninhaber-Authentikation (PWD) mit lokalem Passwort 1.

READ / SEARCH RECORD: Karteninhaber-Authentikation (PWD) mit lokalem
Passwort 1 und MAC-SM-AC für die Antwortnachricht mit dem Schlüssel KDAK.


<table>
<tr>
<th>Tag</th>
<th>Länge</th>
<th>Wert</th>
<th>Erläuterung</th>
</tr>
<tr>
<td>'80'</td>
<td>'01'</td>
<td>'02'</td>
<td>Zugriffsart für UPDATE RECORD</td>
</tr>
<tr>
<td>'A4'</td>
<td>'07'</td>
<td></td>
<td>AT - Tag und Länge</td>
</tr>
<tr>
<td>'95'</td>
<td>'01'</td>
<td>'08'</td>
<td>Usage Qualifier für Karteninhaber-Authentikation</td>
</tr>
<tr>
<td>'83'</td>
<td>'02'</td>
<td>'80 01'</td>
<td>Passwort-Referenz, lokales Passwort mit der Nummer 1</td>
</tr>
<tr>
<td>'80'</td>
<td>'01'</td>
<td>'01'</td>
<td>Zugriffsart für READ / SEARCH RECORD</td>
</tr>
<tr>
<td>'AF'</td>
<td>'13'</td>
<td></td>
<td>AND - Template, Tag und Länge</td>
</tr>
<tr>
<td>'B4'</td>
<td>'08'</td>
<td></td>
<td>CCT - Tag und Länge</td>
</tr>
<tr>
<td>'95'</td>
<td>'01'</td>
<td>'20'</td>
<td>Usage Qualifier: Nur Antwortnachricht</td>
</tr>
<tr>
<td>'83'</td>
<td>'03'</td>
<td>'80 02 FF'</td>
<td>Schlüsselreferenz für KDAK</td>
</tr>
<tr>
<td>'A4'</td>
<td>'07'</td>
<td></td>
<td>AT - Tag und Länge</td>
</tr>
<tr>
<td>'95'</td>
<td>'01'</td>
<td>'08'</td>
<td>Usage Qualifier für Karteninhaber-Authentikation</td>
</tr>
<tr>
<td>'83'</td>
<td>'02'</td>
<td>'80 01'</td>
<td>Passwort-Referenz, lokales Passwort mit der Nummer 1</td>
</tr>
</table>


Record 8 wird referenziert als Zugriffsregel im EF_PWDD.

VERIFY, CHANGE REFERENCE DATA: ALW

RESET RETRY COUNTER: MAC-SM-AC für Kommando- und Antwortnachricht mit
KHBCI_Admin


<table>
<tr>
<th>Tag</th>
<th>Länge</th>
<th>Wert</th>
<th>Beschreibung</th>
</tr>
<tr>
<td>'80'</td>
<td>'01'</td>
<td>'03'</td>
<td>Zugriffsart für VERIFY, CHANGE REFERENCE DATA</td>
</tr>
<tr>
<td>'90'</td>
<td>'00'</td>
<td></td>
<td>ALW</td>
</tr>
<tr>
<td>'80'</td>
<td>'01'</td>
<td>'04'</td>
<td>Zugriffsart für Kommando: RESET RETRY COUNTER</td>
</tr>
<tr>
<td>'B4'</td>
<td>'05'</td>
<td></td>
<td>CCT - Tag und Länge</td>
</tr>
<tr>
<td>'83'</td>
<td>'03'</td>
<td>'80 01 FF'</td>
<td>Schlüsselreferenz für KHBCI_Admin</td>
</tr>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th>Version:</th>
<th>Kapitel:</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Security - Sicherheitsverfahren HBCI</td>
<td>3.0 - Final Version</td>
<td>C</td>
</tr>
<tr>
<td>Kapitel:</td>
<td>Chipapplikationen</td>
<td>Stand:</td>
<td>Seite:</td>
</tr>
<tr>
<td>Abschnitt:</td>
<td>Chipapplikation für DDV</td>
<td>18.07.2013</td>
<td>131</td>
</tr>
</table>


#### C.2.2.3 EF_KEY


##### . Beschreibung

Die applikationsspezifischen Schlüssel der Applikation HBCI-Banking sind im
EF_KEY des Applikationsverzeichnisses DF_BANKING_20 gespeichert. Dies sind

. ein 16 Byte langer kartenindividueller Schlüssel KHBCI_Admin mit der Schlüsselnum-
mer '01' zur Administration der Applikation DF_BANKING_20,

. ein 16 Byte langer kartenindividueller Schlüssel KDAK mit der Schlüsselnummer
'02' als kundenindividueller Daten-Authentikationsschlüssel (DAK = Data Authen-
tication Key)16, sowie

. ein 16 Byte langer kartenindividueller Schlüssel KENC mit der Schlüsselnummer
'03' als kundenindividueller Chiffrierschlüssel.

Die Schlüssel KHBCI_Admin, KDAK und KENC sind nur der HBCI-Chipkarte und
dem für sie zuständigen Hintergrundsystem bekannt. Sie werden jeweils aus einem
KGK (Key Generating Key) unter Verwendung der Kartenidentifikationsdaten im
EF_ID des MF abgeleitet (vgl. Kapitel 8.4.1 von [DATKOM]). Das zuständige Hinter-
grundsystem kennt die jeweiligen KGK und leitet die kartenindividuellen Schlüssel
bei Bedarf ab.

Es können pro logischer Schlüsselnummer verschiedene KGK verwendet werden.
Ein KGK wird wie alle daraus abgeleiteten Schlüssel anhand der Schlüsselversion
identifiziert. Die Schlüsselversion zur jeweiligen logischen Schlüsselnummer im zu-
gehörigen EF_KEYD zeigt an, aus welchem KGK der jeweilige kartenindividuelle
Schlüssel abgeleitet ist.


##### . Format

Für das EF_KEY des DF_BANKING_20 sind die folgenden FCP festzulegen:


<table>
<tr>
<th>Tag</th>
<th>Länge</th>
<th>Wert</th>
<th>Erläuterung</th>
</tr>
<tr>
<td>'62'</td>
<td>'16'</td>
<td></td>
<td>Tag und Länge für FCP</td>
</tr>
</table>


'82'

'05'

'32 41 00 12 03'

Datei-Deskriptor für sicherheitsrelevantes line-
ares EF mit fester Recordlänge (18 Byte), 3
Records


<table>
<tr>
<td>'83'</td>
<td>'02'</td>
<td>'00 10'</td>
<td>Datei-ID des EF_KEY</td>
</tr>
<tr>
<td>'88'</td>
<td>'01'</td>
<td>'10'</td>
<td>SFI '02' für das EF_KEY</td>
</tr>
<tr>
<td>'A1'</td>
<td>,90,</td>
<td>'8B 04 00 30 02 04'</td>
<td>Zugriffsregel-Referenzen</td>
</tr>
</table>


Auf das EF_KEY darf nur im SE #2 zugegriffen werden.

Die Kommandos APPEND RECORD und UPDATE RECORD dürfen nur ausgeführt
werden, wenn sie mit Secure Messaging durchgeführt werden, der Record-Inhalt
verschlüsselt (ENC) ist und die Kommandonachricht mit einem MAC abgesichert ist.
Verschlüsselung und MAC-Bildung erfolgen mit dem KHBCI_Admin. Der Returncode
eines APPEND RECORD oder UPDATE RECORD wird mit dem KHBCI Admin MAC-
gesichert. Das Kommando READ RECORD darf nie ausgeführt werden. (Zugriffsre-
gel im Record 4 des EF_RULE)

<!-- PageFooter: 16 Um den Begriff ,,Signierschlüssel“ für Anwendungen nach SigG bzw. EU-Richtlinie freizuhalten, wurde hier der Begriff ,,Daten-Authentikationsschlüssel“ gewählt. Im weiteren Text wird jedoch zur besseren Lesbarkeit weiterhin davon gesprochen, dass eine Nachricht mit diesem Schlüssel sig- niert wird. -->
<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: C</td>
<td>Version: 3.0 - Final Version</td>
<td>Financial Transaction Services (FinTS) Dokument: Security - Sicherheitsverfahren HBCI</td>
</tr>
<tr>
<td>Seite: 132</td>
<td>Stand: 18.07.2013</td>
<td>Kapitel: Chipapplikationen<br>Abschnitt: Chipapplikation für DDV</td>
</tr>
</table>


##### . Daten

Das EF_KEY im DF_BANKING_20 enthält 3 Records mit den DF-spezifischen
Schlüsseln des DF_BANKING_20.


<table>
<tr>
<th>Logische Schlüs- selnummer</th>
<th>Schlüssel-Version</th>
<th>Schlüssel</th>
</tr>
<tr>
<td>'01'</td>
<td>'XX'</td>
<td>16 Byte langer KHBCI_Admin</td>
</tr>
<tr>
<td>'02'</td>
<td>'XX'</td>
<td>16 Byte langer KDAK</td>
</tr>
<tr>
<td>'03'</td>
<td>'XX'</td>
<td>16 Byte langer KENC</td>
</tr>
</table>


Es werden die Schlüsselversionen 1 bis 127 verwendet.

<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th>Version:</th>
<th rowspan="2">Kapitel: C</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Security - Sicherheitsverfahren HBCI</td>
<td>3.0 - Final Version</td>
</tr>
<tr>
<td>Kapitel:</td>
<td>Chipapplikationen</td>
<td>Stand:</td>
<td>Seite:</td>
</tr>
<tr>
<td>Abschnitt:</td>
<td>Chipapplikation für DDV</td>
<td>18.07.2013</td>
<td>133</td>
</tr>
</table>


#### C.2.2.4 EF_KEYD


##### . Beschreibung

Das EF_KEYD im DF_BANKING_20 enthält die Zusatzinformationen zu den DF-
spezifischen Schlüsseln des DF_BANKING_20.


##### . Format

Für das EF_KEYD sind die folgenden FCP festzulegen:


<table>
<tr>
<th>Tag</th>
<th>Länge</th>
<th>Wert</th>
<th>Erläuterung</th>
</tr>
<tr>
<td>'62'</td>
<td>'1C'</td>
<td></td>
<td>Tag und Länge für FCP</td>
</tr>
<tr>
<td>'82'</td>
<td>'05'</td>
<td>'14 41 00 1C 03'</td>
<td>Datei-Deskriptor für lineares EF mit variab- ler Recordlänge (max. 28 Byte) und 3 Re- cords</td>
</tr>
<tr>
<td>'83'</td>
<td>'02'</td>
<td>'00 13'</td>
<td>Datei-ID des EF_KEYD</td>
</tr>
<tr>
<td>'85'</td>
<td>'02'</td>
<td>'00 48'</td>
<td>für Nutzdaten allokierter Speicherplatz in Byte</td>
</tr>
<tr>
<td>'88'</td>
<td>'01'</td>
<td>'F0'</td>
<td>SFI '1E' für das EF_KEYD</td>
</tr>
<tr>
<td>'A1'</td>
<td>'08'</td>
<td>'8B 06 00 30 01 02 02 05'</td>
<td>Zugriffsregel-Referenzen</td>
</tr>
</table>


Im SE #1 dürfen nur die Kommandos READ / SEARCH RECORD mit ungesicherter
Kommando und Antwortnachricht ausgeführt werden (Zugriffsregel im Record 2 des
EF_RULE).

Im SE #2 dürfen die Kommandos APPEND RECORD und UPDATE RECORD nur
ausgeführt werden, wenn sie mit Secure Messaging durchgeführt werden. Die MAC-
Bildung erfolgt für Kommando- und Antwortnachricht mit dem KHBCI_Admin (Zugriffs-
regel im Record 5 des EF_RULE).


##### ◆ Daten

Das EF_KEYD enthält 3 Records, die die Zusatzinformation zu den DF-spezifischen
Schlüsseln des DF_BANKING_20 enthalten.

Das Datenobjekt mit Tag '93' enthält im Wertfeld als zweites Byte die Version des
entsprechenden Schlüssels.

Im folgenden wird der Aufbau der Schlüsselzusatzinformation dargestellt:

Eintrag 1 (KHBCI_Admin):


<table>
<tr>
<th>Tag</th>
<th>Länge</th>
<th>Wert</th>
<th>Erläuterung</th>
</tr>
<tr>
<td>'93'</td>
<td>'02'</td>
<td>'01 XX'</td>
<td>Schlüsselnummer und Schlüssel-Version</td>
</tr>
<tr>
<td>'C0'</td>
<td>'02'</td>
<td>'81 10'</td>
<td>Symmetrischer Schlüssel der Länge 16 Byte</td>
</tr>
<tr>
<td>'90'</td>
<td>'01'</td>
<td>'FF'</td>
<td>Fehlbedienungszähler</td>
</tr>
<tr>
<td>'7B'</td>
<td>'0F'</td>
<td></td>
<td>SE-Datenobjekt</td>
</tr>
<tr>
<td>'80'</td>
<td>'01'</td>
<td>'02'</td>
<td>Festlegung für SE #2</td>
</tr>
<tr>
<td>'B4'</td>
<td>'04'</td>
<td></td>
<td>CCT - Tag und Länge (Usage Qualifier '30' ist Default- wert)</td>
</tr>
<tr>
<td>'89'</td>
<td>'02'</td>
<td>'12 22'</td>
<td>Algorithmus-ID: Schlüssel darf zur Bildung eines Retail-MAC im CFB-Mode verwendet werden</td>
</tr>
<tr>
<td>'B8'</td>
<td>'04'</td>
<td></td>
<td>CT - Tag und Länge (Usage Qualifier '10' ist Default- wert)</td>
</tr>
<tr>
<td>'89'</td>
<td>'02'</td>
<td>'11 23'</td>
<td>Algorithmus-ID: Schlüssel darf zur Verschlüsselung als Triple-DES Schlüssel im CBC-Mode mit ICV ≠ 0 und ICV-Variante verwendet werden</td>
</tr>
</table>


<!-- PageBreak -->


<table>
<caption>Eintrag 2 (KDAK):</caption>
<tr>
<td>Kapitel: C</td>
<td>Version: 3.0 - Final Version</td>
<td>Financial Transaction Services (FinTS) Dokument: Security - Sicherheitsverfahren HBCI</td>
</tr>
<tr>
<td>Seite:</td>
<td rowspan="2">Stand: 18.07.2013</td>
<td>Kapitel: Chipapplikationen</td>
</tr>
<tr>
<td>134</td>
<td>Abschnitt: Chipapplikation für DDV</td>
</tr>
</table>


<table>
<caption>Eintrag 3 (KENC):</caption>
<tr>
<th>Tag</th>
<th>Länge</th>
<th>Wert</th>
<th>Erläuterung</th>
</tr>
<tr>
<td>'93'</td>
<td>'02'</td>
<td>'02 XX'</td>
<td>Schlüsselnummer und Schlüssel-Version</td>
</tr>
<tr>
<td>'C0'</td>
<td>'02'</td>
<td>'81 10'</td>
<td>Symmetrischer Schlüssel der Länge 16 Byte</td>
</tr>
<tr>
<td>'7B'</td>
<td>'0C'</td>
<td></td>
<td>SE-Datenobjekt</td>
</tr>
<tr>
<td>'80'</td>
<td>'01'</td>
<td>'01'</td>
<td>Festlegung für SE #1</td>
</tr>
<tr>
<td>'B4'</td>
<td>'07'</td>
<td></td>
<td>CCT - Tag und Länge</td>
</tr>
<tr>
<td>'95'</td>
<td>'01'</td>
<td>'20'</td>
<td>Usage Qualifier: Nur SM-Antwortnachricht</td>
</tr>
<tr>
<td>'89'</td>
<td>'02'</td>
<td>'12 22'</td>
<td>Algorithmus-ID: Schlüssel darf zur Bildung eines Retail-MAC im CFB-Mode verwendet werden</td>
</tr>
</table>


<table>
<tr>
<th>Tag</th>
<th>Länge</th>
<th>Wert</th>
<th>Erläuterung</th>
</tr>
<tr>
<td>'93'</td>
<td>'02'</td>
<td>'03 XX'</td>
<td>Schlüsselnummer und Schlüssel-Version</td>
</tr>
<tr>
<td>'C0'</td>
<td>'02'</td>
<td>'81 10'</td>
<td>Symmetrischer Schlüssel der Länge 16 Byte</td>
</tr>
<tr>
<td>'7B'</td>
<td>'0C'</td>
<td></td>
<td>SE-Datenobjekt</td>
</tr>
<tr>
<td>'80'</td>
<td>'01'</td>
<td>'01'</td>
<td>Festlegung für SE #1</td>
</tr>
<tr>
<td>'A4'</td>
<td>'07'</td>
<td></td>
<td>AT - Tag und Länge</td>
</tr>
<tr>
<td>'95'</td>
<td>'01'</td>
<td>'40'</td>
<td>Usage Qualifier: Nur interne Authentikation</td>
</tr>
<tr>
<td>'89'</td>
<td>'02'</td>
<td>'21 12'</td>
<td>Algorithmus-ID: Schlüssel darf zur Authentikation der Chipkarte mit Triple-DES verwendet werden</td>
</tr>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th>Version:</th>
<th>Kapitel:</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Security - Sicherheitsverfahren HBCI</td>
<td>3.0 - Final Version</td>
<td>C</td>
</tr>
<tr>
<td>Kapitel:</td>
<td>Chipapplikationen</td>
<td>Stand:</td>
<td>Seite:</td>
</tr>
<tr>
<td>Abschnitt:</td>
<td>Chipapplikation für DDV</td>
<td>18.07.2013</td>
<td>135</td>
</tr>
</table>


#### C.2.2.5 EF_PWD


##### . Beschreibung

Das lokale EF_PWD im DF_BANKING_20 enthält in dem 9 Byte langen Record '01'
die Länge der HBCI-PIN und einen Referenzwert der HBCI-PIN der ZKA-Chipkarte.
Die HBCI-PIN hat eine Mindestlänge von 5 Ziffern und darf maximal 12 Ziffern lang
sein.


##### . Format

Für das EF_PWD des DF_BANKING_20 sind die folgenden FCP festzulegen:


<table>
<tr>
<th>Tag</th>
<th>Länge</th>
<th>Wert</th>
<th>Erläuterung</th>
</tr>
<tr>
<td>'62'</td>
<td>'16'</td>
<td></td>
<td></td>
</tr>
<tr>
<td>'82'</td>
<td>'05'</td>
<td>'32 41 00 09 01'</td>
<td>Datei-Deskriptor für sicherheitsrelvantes lineares EF mit fester Recordlänge von 9 Byte</td>
</tr>
<tr>
<td>'83'</td>
<td>'02'</td>
<td>'00 12'</td>
<td>Datei-ID des EF_PWD</td>
</tr>
<tr>
<td>'88'</td>
<td>'01'</td>
<td>'18'</td>
<td>SFI '03' für das EF_PWD</td>
</tr>
<tr>
<td>'A1'</td>
<td>'06'</td>
<td>'8B 04 00 30 02 04'</td>
<td>Zugriffsregel-Referenz</td>
</tr>
</table>


Auf das EF_PWD darf nur im SE #2 zugegriffen werden: Die Kommandos APPEND
RECORD und UPDATE RECORD dürfen nur ausgeführt werden, wenn sie mit
Secure Messaging durchgeführt werden, der Recordinhalt verschlüsselt (ENC) ist
und die Kommandonachricht mit einem MAC abgesichert ist. Verschlüsselung und
MAC-Bildung erfolgen dabei mit dem KHBCI_Admin. Der Returncode eines APPEND
RECORD oder UPDATE RECORD wird MAC-gesichert. Die MAC-Bildung erfolgt für
die Antwortnachricht mit dem KHBCI_Admin. Das Kommando READ RECORD darf
nie ausgeführt werden (Zugriffsregel im Record 4 des EF_RULE).


##### ◆ Daten

Der Record '01' des EF_PWD enthält einen Referenzwert der HBCI-PIN.


<table>
<tr>
<th>Byte</th>
<th>Inhalt</th>
<th>Beschreibung</th>
</tr>
<tr>
<td>1</td>
<td>'05'</td>
<td>Länge der PIN</td>
</tr>
<tr>
<td>2 - 9</td>
<td>'XX..XX'</td>
<td>Referenzwert der PIN</td>
</tr>
</table>


Zur Erzeugung des Referenzwertes wird aus der HBCI-PIN zunächst der 8 Byte
lange 'Format 2 PIN Block' gemäß [ISO PIN1] wie folgt gebildet:


<table>
<tr>
<td>CLPPPPP</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>P/F</td>
<td>P/F</td>
<td>P/F</td>
<td>P/F</td>
<td>P/F</td>
<td>P/F</td>
<td>P/F</td>
<td>F</td>
<td>F</td>
</tr>
</table>


#### Erläuterung:

Jedes Feld repräsentiert ein Halbbyte.

C: Kontroll-Feld, binär kodiert

hat immer den Wert '2'

L: PIN-Länge, binär kodiert

mögliche Werte von '5' bis 'C'

P: PIN-Ziffer, BCD-kodiert

F: Filler, binär kodiert

hat immer den Wert 'F'

P/F: PIN-Ziffer/Filler

Belegung abhängig von der PIN-Länge

<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: C</td>
<td>Version: 3.0 - Final Version</td>
<td>Financial Transaction Services (FinTS) Dokument: Security - Sicherheitsverfahren HBCI</td>
</tr>
<tr>
<td>Seite:<br>136</td>
<td>Stand: 18.07.2013</td>
<td>Kapitel: Chipapplikationen<br>Abschnitt: Chipapplikation für DDV</td>
</tr>
</table>


Der erzeugte Format 2 PIN Block wird mit PB bezeichnet. Aus diesem PIN Block
wird der zu speichernde Referenzwert durch DES-Verschlüsselung mit sich selbst
erzeugt:

PIN-Referenzwert: ePB(PB)

Falls erforderlich, wird vor der Verwendung von PB als DES-Schlüssel ein Parity Ad-
justment vorgenommen. PB wird als Klartext unverändert verwendet.

<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th>Version:</th>
<th rowspan="2">Kapitel: C</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Security - Sicherheitsverfahren HBCI</td>
<td>3.0 - Final Version</td>
</tr>
<tr>
<td>Kapitel:</td>
<td>Chipapplikationen</td>
<td>Stand:</td>
<td>Seite:</td>
</tr>
<tr>
<td>Abschnitt:</td>
<td>Chipapplikation für DDV</td>
<td>18.07.2013</td>
<td>137</td>
</tr>
</table>


#### C.2.2.6 EF_PWDD


##### . Beschreibung

Das EF_PWDD im DF_BANKING_20 enthält in Record '01' die Zusatzinformationen
zu der im EF_PWD des DF_BANKING_20 abgelegten HBCI-PIN.


##### . Format

Für das EF_PWDD sind die folgenden FCP festzulegen:


<table>
<tr>
<th>Tag</th>
<th>Länge</th>
<th>Wert</th>
<th>Erläuterung</th>
</tr>
<tr>
<td>'62'</td>
<td>'1C'</td>
<td></td>
<td></td>
</tr>
<tr>
<td>'82'</td>
<td>'05'</td>
<td>'14 41 00 15 01'</td>
<td>Datei-Deskriptor für lineares EF mit variabler Recordlänge (max. 21 Byte) und 1 Record</td>
</tr>
<tr>
<td>'83'</td>
<td>'02'</td>
<td>'00 15'</td>
<td>Datei-ID des EF_PWDD</td>
</tr>
<tr>
<td>'85'</td>
<td>'02'</td>
<td>'00 15'</td>
<td>Für Nutzdaten allokierter Speicherplatz in Byte</td>
</tr>
<tr>
<td>'88'</td>
<td>'01'</td>
<td>'20'</td>
<td>SFI '04' für das EF_PWDD</td>
</tr>
<tr>
<td>'A1'</td>
<td>'08'</td>
<td>'8B 06 00 30 01 02 02 05'</td>
<td>Zugriffsregel-Referenzen</td>
</tr>
</table>


Im SE #1 dürfen nur die Kommandos READ / SEARCH RECORD mit ungesicherter
Kommando und Antwortnachricht ausgeführt werden (Zugriffsregel im Record 2 des
EF_RULE).

Im SE #2 durfen APPEND RECORD und UPDATE RECORD nur ausgeführt wer-
den, wenn sie mit Secure Messaging durchgeführt werden und die Kommandonach-
richt mit einem MAC abgesichert ist. Der Returncode wird MAC-gesichert. Die MAC-
Bildung erfolgt für Kommando- und Antwortnachricht mit dem KHBCI_Admin (Zugriffs-
regel im Record 5 des EF_RULE).


##### ◆ Daten

Das lokale EF_PWDD enthält in Record '01' einen 21 Byte langen Record, der die
Zusatzinformationen zu der HBCI-PIN enthält.


<table>
<tr>
<th>Tag</th>
<th>Länge</th>
<th>Wert</th>
<th>Beschreibung</th>
</tr>
<tr>
<td>'93'</td>
<td>'02'</td>
<td>'01 01'</td>
<td>Passwortreferenz: Passwort '01' im Record '01' des EF_PWD</td>
</tr>
<tr>
<td>'89'</td>
<td>'02'</td>
<td>'11 50'</td>
<td>Speicherformat des Passwortes (minimal 5 Ziffern)</td>
</tr>
<tr>
<td>'A1'</td>
<td>'03'</td>
<td>'8B 01 08'</td>
<td>Zugriffsregel-Referenz</td>
</tr>
<tr>
<td>'7B'</td>
<td>,90,</td>
<td></td>
<td>SE-DO, Tag und Länge</td>
</tr>
<tr>
<td>'80'</td>
<td>'01'</td>
<td>'00'</td>
<td>SE Referenz-DO: Für alle SEs</td>
</tr>
<tr>
<td>'89'</td>
<td>'01'</td>
<td>'12'</td>
<td>Übertragungsformat der Authentikationsda- ten: PIN Format 2 Block</td>
</tr>
</table>


<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: C</td>
<td>Version: 3.0 - Final Version</td>
<td>Financial Transaction Services (FinTS) Dokument: Security - Sicherheitsverfahren HBCI</td>
</tr>
<tr>
<td rowspan="2">Seite: 138</td>
<td rowspan="2">Stand: 18.07.2013</td>
<td>Kapitel: Chipapplikationen</td>
</tr>
<tr>
<td>Abschnitt: Chipapplikation für DDV</td>
</tr>
</table>


#### C.2.2.7 EF_FBZ


##### . Beschreibung

EF_FBZ bezeichnet das lineare EF, das in Record '01' den Fehlbedienungszähler
und den zugehörigen Initialwert für die im DF-spezifischen EF_PWD abgelegte
HBCI-PIN enthält.


##### . Format

Für das EF_FBZ im DF_BANKING_20 sind die folgenden FCP festzulegen:


<table>
<tr>
<th>Tag</th>
<th>Länge</th>
<th>Wert</th>
<th>Erläuterung</th>
</tr>
<tr>
<td>'62'</td>
<td>'18'</td>
<td></td>
<td>Tag und Länge für FCP</td>
</tr>
<tr>
<td>'82'</td>
<td>'05'</td>
<td>'12 41 00 02 01'</td>
<td>Datei-Deskriptor für lineares EF fester Re- cordlänge</td>
</tr>
<tr>
<td>'83'</td>
<td>'02'</td>
<td>'00 16'</td>
<td>Datei-ID des EF_FBZ</td>
</tr>
<tr>
<td>'88'</td>
<td>'01'</td>
<td>'28'</td>
<td>SFI '05' für das EF_FBZ</td>
</tr>
<tr>
<td>'A1'</td>
<td>'08'</td>
<td>'8B 06 00 30 01 02 02 05'</td>
<td>Zugriffsregel-Referenzen</td>
</tr>
</table>


Im SE # 1 dürfen nur die Kommandos READ / SEARCH RECORD mit ungesicherter
Kommando und Antwortnachricht ausgeführt werden (Zugriffsregel im Record 2 des
EF_RULE).

Im SE #2 dürfen die Kommandos APPEND RECORD und UPDATE RECORD nur
ausgeführt werden, wenn sie mit Secure Messaging durchgeführt werden und die
Kommandonachricht mit einem MAC abgesichert ist. Der Returncode wird MAC-
gesichert. Die MAC-Bildung erfolgt für Kommando- und Antwortnachricht mit dem
KHBCI_Admin (Zugriffsregel im Record 5 des EF_RULE).


##### . Daten

Das EF_FBZ enthält in Record '01' einen 2 Byte langen Record, der den Fehlbedie-
nungszähler und den zugehörigen Initialwert '03' für die HBCI-PIN enthält.


<table>
<tr>
<td>Initialwert des FBZ</td>
<td>FBZ</td>
</tr>
<tr>
<td>'03'</td>
<td>'03'</td>
</tr>
</table>


<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th>Version:</th>
<th>Kapitel:</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Security - Sicherheitsverfahren HBCI</td>
<td>3.0 - Final Version</td>
<td>C</td>
</tr>
<tr>
<td>Kapitel:</td>
<td>Chipapplikationen</td>
<td>Stand:</td>
<td>Seite:</td>
</tr>
<tr>
<td>Abschnitt:</td>
<td>Chipapplikation für DDV</td>
<td>18.07.2013</td>
<td>139</td>
</tr>
</table>


#### C.2.2.8 EF_BNK


##### . Beschreibung

Bei dem EF_BNK handelt es sich um ein lineares EF mit 5 Records in dem Bank-
verbindungen abgelegt sind.


##### . Format

Für das EF_BNK in einer HBCI-Chipkarte sind die folgenden FCP festzulegen:


<table>
<tr>
<th>Tag</th>
<th>Länge</th>
<th>Wert</th>
<th>Erläuterung</th>
</tr>
<tr>
<td>'62'</td>
<td>'18'</td>
<td></td>
<td>Tag und Länge für FCP</td>
</tr>
<tr>
<td>'82'</td>
<td>'05'</td>
<td>'12 41 00 58 05'</td>
<td>Datei-Deskriptor für lineares EF mit fester Recordlänge 88 Byte und 5 Records</td>
</tr>
<tr>
<td>'83'</td>
<td>'02'</td>
<td>'03 01'</td>
<td>Datei-ID des EF_BNK</td>
</tr>
<tr>
<td>'88'</td>
<td>'01'</td>
<td>'D0'</td>
<td>SFI '1A' für das EF_BNK</td>
</tr>
<tr>
<td>'A1'</td>
<td>'08'</td>
<td>'8B 06 00 30 01 06 02 03'</td>
<td>Zugriffsregel-Referenzen</td>
</tr>
</table>


Im SE #1 dürfen READ / SEARCH RECORD immer ausgeführt werden, die Ant-
wortnachricht wird nicht abgesichert. UPDATE RECORD darf nur ausgeführt wer-
den, wenn zuvor eine Karteninhaber-Authentikation mit dem lokalen Passwort 1
(HBCI-PIN) erfolgt ist. Der Returncode wird nicht MAC-gesichert (Zugriffsregeln im
Record 6 des EF_RULE).

Im SE #2 darf das Kommando APPEND RECORD nur ausgeführt werden, wenn es
mit Secure Messaging durchgeführt wird. Die MAC-Bildung erfolgt für Kommando-
und Antwortnachricht mit dem KHBCI_Admin (Zugriffsregel im Record 3 des EF_RULE).


##### . Daten

Die Records setzen sich aus einer Bankkurzbezeichnung, der Bankleitzahl, dem
Kommunikationsdienst, der Adresse und dem Adresszusatz für den Kommunikati-
onszugang, dem Länderkennzeichen und der Benutzerkennung zusammen.


<table>
<tr>
<th>Byte</th>
<th>Länge</th>
<th>Wert</th>
<th>Erläuterung</th>
</tr>
<tr>
<td>1-20</td>
<td>20</td>
<td>'aa .. aa'</td>
<td>Kurzbezeichner des Kreditinstituts</td>
</tr>
<tr>
<td>21-24</td>
<td>4</td>
<td>'nn nn nn nn'</td>
<td>Kreditinstitutscode des kontoführenden Instituts</td>
</tr>
<tr>
<td>25-25</td>
<td>1</td>
<td>'n'</td>
<td>Kommunikationsdienst</td>
</tr>
<tr>
<td>26-53</td>
<td>28</td>
<td>'aa .. aa'</td>
<td>Kommunikationsadresse</td>
</tr>
<tr>
<td>54-55</td>
<td>2</td>
<td>'aa aa'</td>
<td>Kommunikationsadressenzusatz</td>
</tr>
<tr>
<td>56-58</td>
<td>3</td>
<td>'aa aa aa'</td>
<td>Länderkennzeichen des kontoführenden Instituts</td>
</tr>
<tr>
<td>59-88</td>
<td>30</td>
<td>'aa .. aa'</td>
<td>Benutzerkennung</td>
</tr>
</table>


Alphanumerische Feldinhalte ('a') werden ASCII-kodiert, linksbündig eingestellt und
mit Leerzeichen (X'20') auf die vorgegebene Länge aufgefüllt. Numerische Feldin-
halte ('n') werden BCD-kodiert.

<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: C</td>
<td>Version: 3.0 - Final Version</td>
<td>Financial Transaction Services (FinTS) Dokument: Security - Sicherheitsverfahren HBCI</td>
</tr>
<tr>
<td>Seite:</td>
<td rowspan="2">Stand: 18.07.2013</td>
<td>Kapitel: Chipapplikationen</td>
</tr>
<tr>
<td>140</td>
<td>Abschnitt: Chipapplikation für DDV</td>
</tr>
</table>


#### C.2.2.9 EF_MAC


##### . Beschreibung

Das EF_MAC wird für die MAC-Bildung über den Hashwert einer Nachricht benötigt.
Es besteht aus einem 12 Byte langem Record deren Zugriffsregeln so gesetzt wer-
den müssen, dass beim Lesen des Records der MAC produziert wird.


##### . Format

Für das EF_MAC sind die folgenden FCP festzulegen:


<table>
<tr>
<th>Tag</th>
<th>Länge</th>
<th>Wert</th>
<th>Erläuterung</th>
</tr>
<tr>
<td>'62'</td>
<td>'18'</td>
<td></td>
<td>Tag und Länge für FCP</td>
</tr>
<tr>
<td>'82'</td>
<td>'05'</td>
<td>'12 41 00 0C 01'</td>
<td>Datei-Deskriptor für lineares EF mit einem Record der Länge 12 Byte</td>
</tr>
<tr>
<td>'83'</td>
<td>'02'</td>
<td>'03 02'</td>
<td>Datei-ID des EF_MAC</td>
</tr>
<tr>
<td>'88'</td>
<td>'01'</td>
<td>'D8'</td>
<td>SFI '1B' für das EF_MAC</td>
</tr>
<tr>
<td>'A1'</td>
<td>'08'</td>
<td>'8B 06 00 30 01 07 02 03'</td>
<td>Zugriffsregel-Referenzen</td>
</tr>
</table>


Im SE #1 dürfen READ / SEARCH RECORD nach Karteninhaber-Authentikation
ausgeführt werden, die Antwortnachricht wird mit einem KDAK-MAC versehen.
UPDATE RECORD darf nur ausgeführt werden, wenn zuvor eine Karteninhaber-
Authentikation mit dem lokalen Passwort 1 (HBCI-PIN) erfolgt ist. Der Returncode
eines UPDATE RECORD wird nicht MAC-gesichert (Zugriffsregeln im Record 7 des
EF_RULE).

Im SE #2 darf das Kommando APPEND RECORD nur ausgeführt werden, wenn es
mit Secure Messaging durchgeführt wird. Die MAC-Bildung erfolgt für Kommando-
und Antwortnachricht mit dem KHBCI_Admin (Zugriffsregel im Record 3 des EF_RULE).


##### . Daten

Das EF_MAC enthält einen Record, der den folgenden Aufbau hat:


<table>
<tr>
<th>Byte</th>
<th>Wert</th>
<th>Erläuterung</th>
</tr>
<tr>
<td>1-12</td>
<td>'XX..XX'</td>
<td>Hashwert</td>
</tr>
</table>


<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th>Version:</th>
<th>Kapitel:</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Security - Sicherheitsverfahren HBCI</td>
<td>3.0 - Final Version</td>
<td>C</td>
</tr>
<tr>
<td>Kapitel:</td>
<td>Chipapplikationen</td>
<td>Stand:</td>
<td>Seite:</td>
</tr>
<tr>
<td>Abschnitt:</td>
<td>Chipapplikation für DDV</td>
<td>18.07.2013</td>
<td>141</td>
</tr>
</table>


#### C.2.2.10 EF_SEQ


##### . Beschreibung

Bei dem EF_SEQ handelt es sich um ein lineares EF, dessen Record ein 2 Byte
langes binär definiertes Element enthält. Dieser binäre aufsteigende Zähler fließt als
Sicherheitsreferenznummer (Signatur-ID) zur Absicherung der Daten gegen Doppe-
leinreichung ein. Der Startwert des Zählers ist 1. Ein Rücksetzen bei Überlauf findet
nicht statt.


##### . Format

Für das EF_SEQ sind die folgenden FCP festzulegen:


<table>
<tr>
<th>Tag</th>
<th>Länge</th>
<th>Wert</th>
<th>Erläuterung</th>
</tr>
<tr>
<td>'62'</td>
<td>'18'</td>
<td></td>
<td>Tag und Länge für FCP</td>
</tr>
<tr>
<td>'82'</td>
<td>'05'</td>
<td>'12 41 00 02 01'</td>
<td>Datei-Deskriptor für lineares EF mit 1 Record der Länge 2 Byte</td>
</tr>
<tr>
<td>'83'</td>
<td>'02'</td>
<td>'03 03'</td>
<td>Datei-ID des EF_SEQ</td>
</tr>
<tr>
<td>'88'</td>
<td>'01'</td>
<td>'E0'</td>
<td>SFI '1C' für das EF_SEQ</td>
</tr>
<tr>
<td>'A1'</td>
<td>'08'</td>
<td>'8B 06 00 30 01 06 02 05'</td>
<td>Zugriffsregel-Referenzen</td>
</tr>
</table>


Im SE #1 dürfen READ / SEARCH RECORD immer ausgeführt werden, die Ant-
wortnachricht wird nicht abgesichert. UPDATE RECORD darf nur ausgeführt wer-
den, wenn zuvor eine Karteninhaber-Authentikation mit dem lokalen Passwort 1
(HBCI-PIN) erfolgt ist. Der Returncode wird nicht MAC-gesichert (Zugriffsregeln im
Record 6 des EF_RULE).

Im SE #2 dürfen die Kommandos APPEND RECORD und UPDATE RECORD nur
ausgeführt werden, wenn sie mit Secure Messaging durchgeführt werden. Die MAC-
Bildung erfolgt für Kommando- und Antwortnachrichten jeweils mit dem KHBCI_Admin
(Zugriffsregel im Record 5 des EF_RULE).


##### . Daten

Das EF_SEQ enthält 1 Record, der den folgenden Aufbau hat:


<table>
<tr>
<th>Byte</th>
<th>Wert</th>
<th>Erläuterung</th>
</tr>
<tr>
<td>1-2</td>
<td>'XX XX'</td>
<td>Sequenznummer</td>
</tr>
<tr>
<td>Kapitel: C</td>
<td>Version: 3.0 - Final Version</td>
<td>Financial Transaction Services (FinTS) Dokument: Security - Sicherheitsverfahren HBCI</td>
</tr>
<tr>
<td>Seite: 142</td>
<td>Stand: 18.07.2013</td>
<td>Kapitel: Chipapplikationen<br>Abschnitt: Chipapplikation für DDV</td>
</tr>
</table>


#### C.2.3 Platzbedarf der Applikation im Chip

Die Platzbedarfsberechnung ist sehr stark von der Stärke der ROM-Maske abhän-
gig. Der notwendige Platz für die EF-Verwaltung z.B. Recordnummern- bzw.
Adressverwaltung steht im direkten Zusammenhang mit der Verwaltung des E2-
PROM. Diese Verwaltung ist Bestandteil der ROM-Maske. Der tatsächliche exakte
Platzbedarf kann nur von den ROM-Maskenentwicklern ermittelt werden. Er ist von
Chip zu Chip und ROM-Maske zu ROM-Maske unterschiedlich.


##### . Typ 0

Die nachfolgende Tabelle enthält daher nur die Nettodatengröße der "Banking"-
Applikation.


<table>
<tr>
<th>Dateiname</th>
<th>Headergröße17</th>
<th>Datengröße</th>
</tr>
<tr>
<td>DF_Banking</td>
<td>28</td>
<td>26</td>
</tr>
<tr>
<td>EF_KEY</td>
<td>23</td>
<td>17</td>
</tr>
<tr>
<td>EF_KEYD</td>
<td>23</td>
<td>5</td>
</tr>
<tr>
<td>EF_AUT</td>
<td>23</td>
<td>17</td>
</tr>
<tr>
<td>EF_AUTD</td>
<td>23</td>
<td>4</td>
</tr>
<tr>
<td>EF_PWD1</td>
<td>25</td>
<td>8</td>
</tr>
<tr>
<td>EF_PWDD1</td>
<td>23</td>
<td>5</td>
</tr>
<tr>
<td>EF_BNK</td>
<td>23</td>
<td>440</td>
</tr>
<tr>
<td>EF_MAC</td>
<td>23</td>
<td>12</td>
</tr>
<tr>
<td>EF_SEQ</td>
<td>23</td>
<td>2</td>
</tr>
<tr>
<td></td>
<td>237</td>
<td>536</td>
</tr>
</table>


Demnach hat die Applikation "Banking" einen Mindestplatzbedarf von 773 Byte.


###### ◆ Typ 1

Die nachfolgende Tabelle enthält daher nur eine grobe Abschätzung der Netto-
datengrößen (in Byte) der Applikation. Dabei wurde als Overhead die Größe des je-
weiligen FCP zugrundegelegt. Zusätzlich wurde das FMD des DF_BANKING_20
(enthält die vergebenen SFIs sowie deren Pfade) als "Nutzdaten" des DF interpre-
tiert.


<table>
<tr>
<th>Dateiname</th>
<th>Overhead</th>
<th>Nutzdaten</th>
</tr>
<tr>
<td>DF_BANKING_20</td>
<td>28</td>
<td>68</td>
</tr>
<tr>
<td>EF_KEY</td>
<td>24</td>
<td>54</td>
</tr>
<tr>
<td>EF_KEYD</td>
<td>30</td>
<td>72</td>
</tr>
<tr>
<td>EF_PWD</td>
<td>24</td>
<td>9</td>
</tr>
<tr>
<td>EF_PWDD</td>
<td>30</td>
<td>21</td>
</tr>
<tr>
<td>EF_FBZ</td>
<td>26</td>
<td>2</td>
</tr>
<tr>
<td>EF_RULE</td>
<td>30</td>
<td>125</td>
</tr>
<tr>
<td>EF_BNK</td>
<td>26</td>
<td>440</td>
</tr>
<tr>
<td>EF_MAC</td>
<td>26</td>
<td>12</td>
</tr>
<tr>
<td>EF_SEQ</td>
<td>26</td>
<td>2</td>
</tr>
<tr>
<td></td>
<td>270</td>
<td>805</td>
</tr>
</table>


Demnach hat die HBCI-Applikation einen Platzbedarf von ca. 1075 Byte.

<!-- PageFooter: 17 Größenangaben in Byte -->
<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th>Version:</th>
<th>Kapitel:</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Security - Sicherheitsverfahren HBCI</td>
<td>3.0 - Final Version</td>
<td>C</td>
</tr>
<tr>
<td>Kapitel:</td>
<td>Chipapplikationen</td>
<td>Stand:</td>
<td>Seite:</td>
</tr>
<tr>
<td>Abschnitt:</td>
<td>Chipapplikation für DDV</td>
<td>18.07.2013</td>
<td>143</td>
</tr>
</table>


#### C.2.4 Terminalabläufe (Typ 1 und SECCOS 6)

Nachfolgend werden die Anwendungsabläufe aus Endgerätesicht spezifiziert. Hier-
bei werden ausschließlich die chipkartenbezogenen Aspekte berücksichtigt. Anwen-
dungsbezogene Details sind nicht Bestandteil dieser Spezifikation.

Falls bei der Ausführung der Kommandos ein Fehler auftritt, bricht das Terminal den
Vorgang ab, es sei denn, es ist ein abweichendes Verhalten spezifiziert.


### C.2.4.1 Startdialog


<table>
<tr>
<td colspan="2">HBCI-Chipkarte</td>
</tr>
<tr>
<td>R1</td>
<td>ATR der HBCI-Chipkarte</td>
</tr>
<tr>
<td>R2</td>
<td>OK</td>
</tr>
<tr>
<td>R3</td>
<td>Kartenidentifikationsdaten (CID)</td>
</tr>
<tr>
<td>R4</td>
<td>OK</td>
</tr>
<tr>
<td>R4</td>
<td>Sequenznummer (SEQ)</td>
</tr>
<tr>
<td>R5</td>
<td>Bankverbindung</td>
</tr>
</table>


<table>
<tr>
<td rowspan="8">→ ← → ← →<br>← →<br>← →<br>← →</td>
<td colspan="2">Endgerät/Gateway</td>
</tr>
<tr>
<td>A1<br>C1</td>
<td>Anzeige: 'Bitte Karte einstecken'<br>Reset HBCI-Chipkarte</td>
</tr>
<tr>
<td>C2</td>
<td>SELECT FILE DF_BANKING(_20)</td>
</tr>
<tr>
<td>C3<br>A3</td>
<td>READ RECORD EF_ID<br>CID prüfen und speichern</td>
</tr>
<tr>
<td>A4<br>C4</td>
<td>HBCI-PIN-Eingabe und Formatie- rung<br>VERIFY HBCI-PIN</td>
</tr>
<tr>
<td>C5</td>
<td>READ RECORD EF_SEQ</td>
</tr>
<tr>
<td>A5</td>
<td>SEQ speichern</td>
</tr>
<tr>
<td>C6<br>A6</td>
<td>READ RECORD EF_BNK<br>Daten prüfen und speichern</td>
</tr>
</table>


#### ◆ Erläuterung

1\. Nachdem die HBCI-Chipkarte eingesteckt ist, wird ein Reset der Karte durchgeführt
(Kommunikationsprotokoll T = 1). Der korrekte ATR und seine Behandlung sind z.B.
in [LT] spezifiziert.

2\. Die Applikation HBCI-Banking wird geöffnet, indem das ADF der Applikation,
DF_BANKING_20 für HBCI-Karten von Typ 1 oder DF_BANKING für HBCI-Karten
von Typ 0, durch das Terminal mittels des Kommandos SELECT FILE ausgewählt
wird. Dabei wird zunächst versucht, die neue Applikation DF_BANKING_20 zu se-
lektieren. Bei einem Returncode '6A 82' ist die Applikation nicht vorhanden. Es wird
dann die "alte" Applikation DF_BANKING selektiert.

Command APDU:


<table>
<tr>
<th>Byte</th>
<th>Wert</th>
<th>Erläuterung</th>
</tr>
<tr>
<td>1-2</td>
<td>'00 A4'</td>
<td>CLA, INS</td>
</tr>
<tr>
<td>3</td>
<td>'04'</td>
<td>P1, Selektion mit DF-Name</td>
</tr>
<tr>
<td>4</td>
<td>'0C'</td>
<td>P2, Keine Antwortdaten</td>
</tr>
<tr>
<td>5</td>
<td>'09'</td>
<td>Lc</td>
</tr>
<tr>
<td>6-14</td>
<td>'D2 76 00 00 25 48 42 0X 00'</td>
<td>AID der HBCI-Applikation (X=1,2)</td>
</tr>
<tr>
<td>Kapitel: C</td>
<td>Version: 3.0 - Final Version</td>
<td>Financial Transaction Services (FinTS) Dokument: Security - Sicherheitsverfahren HBCI</td>
</tr>
<tr>
<td>Seite: 144</td>
<td>Stand: 18.07.2013</td>
<td>Kapitel: Chipapplikationen<br>Abschnitt: Chipapplikation für DDV</td>
</tr>
</table>


Nachdem der Applikationskontext geöffnet ist, können die AEFs der Applikation mit-
tels SFI referenziert werden. Das Terminal hält die Information vor, um welchen Kar-
tentyp es sich handelt

3\. Das Terminal liest mittels READ RECORD die Kartenidentifikationsdaten im Re-
cord '01' des EF_ID im MF der HBCI-Karte (SFI '19').

Command APDU:


<table>
<tr>
<th>Byte</th>
<th>Wert</th>
<th>Erläuterung</th>
</tr>
<tr>
<td>1-2</td>
<td>'00 B2'</td>
<td>CLA, INS</td>
</tr>
<tr>
<td>3</td>
<td>'01'</td>
<td>P1, Recordnummer</td>
</tr>
<tr>
<td>4</td>
<td>'CC'</td>
<td>P2, Reference Control Byte</td>
</tr>
<tr>
<td>5</td>
<td>'00'</td>
<td>Le</td>
</tr>
</table>


Wenn das READ RECORD erfolgreich ausgeführt wird, gibt die HBCI-Karte eine
Antwortnachricht mit der folgenden Struktur zurück.


<table>
<tr>
<th>Byte</th>
<th>Wert</th>
<th>Erläuterung</th>
</tr>
<tr>
<td>1</td>
<td>'67'</td>
<td>Branchenhauptschlüssel</td>
</tr>
<tr>
<td>2-4</td>
<td>'2n nn nn'</td>
<td>Kurz-BLZ kartenausgebendes Institut</td>
</tr>
<tr>
<td>5-9</td>
<td>'nn..nn'</td>
<td>individuelle Kartennummer</td>
</tr>
<tr>
<td>10</td>
<td>'nD'</td>
<td>Prüfziffer für Byte 1 - 9</td>
</tr>
<tr>
<td>11-12</td>
<td>'JJ MM'</td>
<td>Verfalldatum der Karte</td>
</tr>
<tr>
<td>13-15</td>
<td>'JJ MM TT'</td>
<td>Aktivierungsdatum der Karte</td>
</tr>
<tr>
<td>16-17</td>
<td>'0280'</td>
<td>Ländercode</td>
</tr>
<tr>
<td>18-20</td>
<td>'44 45 4D' oder '45 55 52'</td>
<td>Währungskennzeichen "DEM" oder "EUR"</td>
</tr>
<tr>
<td>21</td>
<td>'01'</td>
<td>Wertigkeit der Währung</td>
</tr>
<tr>
<td>22</td>
<td>'XX'</td>
<td>Chiptyp</td>
</tr>
<tr>
<td>23</td>
<td>'00'</td>
<td>Filler</td>
</tr>
<tr>
<td>24</td>
<td>'XX'</td>
<td>Betriebssystem-Version</td>
</tr>
<tr>
<td>23-24 oder 25-26</td>
<td>'XX XX'</td>
<td>Positiver Returncode SW1 SW2</td>
</tr>
</table>


Die Antwortdaten sind mindestens 22 Byte lang und können für Karten von Typ 1
länger als 24 Byte sein.

Die Kodierung der empfangenen Daten wird geprüft:

Wenn eine Karte von Typ 0 mehr als 22 Byte Antwortdaten ausgibt, oder wenn eine
Karte von Typ 1 weniger als 24 Byte Antwortdaten ausgibt, oder wenn Währungs-
kennzeichen in Byte 18-20 oder Wertigkeit der Währung in Byte 21 nicht korrekt ko-
diert sind, oder wenn eine Karte von Typ 0 das Währungskennzeichen "EUR" oder
eine Karte von Typ 1 das Währungskennzeichen "DEM" ausgibt, oder wenn Byte 24
einer Karte von Typ 1 den Wert '00' hat sowie bei jedem anderen Fehlerfall wird mit
einer Fehlermeldung abgebrochen.

4\. Das Terminal fordert den Karteninhaber auf, die PIN einzugeben und formatiert
dann die eingegebene PIN zum Format 2 PIN-Block FPIN2. Das Terminal baut eine
Kommandonachricht für das Kommando VERIFY auf.

<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th>Version:</th>
<th rowspan="2">Kapitel: C</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Security - Sicherheitsverfahren HBCI</td>
<td>3.0 - Final Version</td>
</tr>
<tr>
<td>Kapitel:</td>
<td>Chipapplikationen</td>
<td>Stand:</td>
<td>Seite:</td>
</tr>
<tr>
<td>Abschnitt:</td>
<td>Chipapplikation für DDV</td>
<td>18.07.2013</td>
<td>145</td>
</tr>
</table>


Command APDU:


<table>
<tr>
<th>Byte</th>
<th>Wert</th>
<th>Erläuterung</th>
</tr>
<tr>
<td>1</td>
<td>'00 20'</td>
<td>CLA, INS</td>
</tr>
<tr>
<td>3</td>
<td>'00'</td>
<td>P1, fester Wert</td>
</tr>
<tr>
<td>4</td>
<td>'81'</td>
<td>P2, PIN im EF_PWD1 des DF suchen (bzw. hat PWDID '01')</td>
</tr>
<tr>
<td>5</td>
<td>'08'</td>
<td>Lc</td>
</tr>
<tr>
<td>6-13</td>
<td>'XX..XX'</td>
<td>FPIN2</td>
</tr>
</table>


Die Chipkarte führt die PIN-Prüfung durch und setzt das Flag des entsprechenden
Sicherheitszustands, wenn die PIN-Prüfung erfolgreich war. Andernfalls wird der
PIN-Fehlbedienungszähler dekrementiert.

Durch den Returncode des Kommandos VERIFY teilt die Chipkarte dem Terminal
mit, ob die Prüfung erfolgreich war, bzw. wie viele Versuche noch möglich sind.

5\. Das Terminal liest mittels READ RECORD die Sequenznummer im Record '01' des
EF_SEQ (SFI '1C').

Command APDU:


<table>
<tr>
<th>Byte</th>
<th>Wert</th>
<th>Erläuterung</th>
</tr>
<tr>
<td>1-2</td>
<td>'00 B2'</td>
<td>CLA, INS</td>
</tr>
<tr>
<td>3</td>
<td>'01'</td>
<td>P1, Recordnummer</td>
</tr>
<tr>
<td>4</td>
<td>'E4'</td>
<td>P2, Reference Control Byte</td>
</tr>
<tr>
<td>5</td>
<td>'00'</td>
<td>Le</td>
</tr>
</table>


Wenn das READ RECORD erfolgreich ausgeführt wird, gibt die HBCI-Karte eine
Antwortnachricht mit der folgenden Struktur zurück.


<table>
<tr>
<th>Byte</th>
<th>Wert</th>
<th>Erläuterung</th>
</tr>
<tr>
<td>1-2</td>
<td>'XX XX'</td>
<td>Sequenzzähler</td>
</tr>
<tr>
<td>3-4</td>
<td>'XX XX'</td>
<td>Positiver Returncode SW1 SW2</td>
</tr>
</table>


Das Terminal speichert den Wert des Sequenzzählers.

6\. Das Terminal liest mittels READ RECORD sukzessive die Bankverbindungsdaten in
den Records des EF_BNK (SFI '1A'), bis der "passende" Eintrag gefunden wird.

Command APDU:


<table>
<tr>
<th>Byte</th>
<th>Wert</th>
<th>Erläuterung</th>
</tr>
<tr>
<td>1-2</td>
<td>'00 B2'</td>
<td>CLA, INS</td>
</tr>
<tr>
<td>3</td>
<td>'0Χ'</td>
<td>P1, Recordnummer X</td>
</tr>
<tr>
<td>4</td>
<td>'D4'</td>
<td>P2, Reference Control Byte</td>
</tr>
<tr>
<td>5</td>
<td>'00'</td>
<td>Le</td>
</tr>
</table>


Wenn das READ RECORD erfolgreich ausgeführt wird, gibt die HBCI-Karte eine
Antwortnachricht mit der folgenden Struktur zurück:

<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: C</td>
<td>Version: 3.0 - Final Version</td>
<td>Financial Transaction Services (FinTS) Dokument: Security - Sicherheitsverfahren HBCI</td>
</tr>
<tr>
<td>Seite:</td>
<td rowspan="2">Stand:<br>18.07.2013</td>
<td>Kapitel: Chipapplikationen</td>
</tr>
<tr>
<td>146</td>
<td>Abschnitt:<br>Chipapplikation für DDV</td>
</tr>
</table>


<table>
<tr>
<th>Byte</th>
<th>Länge</th>
<th>Wert</th>
<th>Erläuterung</th>
</tr>
<tr>
<td>1-20</td>
<td>20</td>
<td>'aa .. aa'</td>
<td>Kurzbezeichner des Kreditinstituts</td>
</tr>
<tr>
<td>21-24</td>
<td>4</td>
<td>'nn nn nn nn'</td>
<td>Bankleitzahl des kontoführenden Instituts</td>
</tr>
<tr>
<td>25-25</td>
<td>1</td>
<td>'n'</td>
<td>Kommunikationsdienst</td>
</tr>
<tr>
<td>26-53</td>
<td>28</td>
<td>'aa .. aa'</td>
<td>Kommunikationsadresse</td>
</tr>
<tr>
<td>54-55</td>
<td>2</td>
<td>'aa aa'</td>
<td>Kommunikationsadressenzusatz</td>
</tr>
<tr>
<td>56-58</td>
<td>3</td>
<td>'aa aa aa'</td>
<td>Länderkennzeichen des kontoführenden Instituts</td>
</tr>
<tr>
<td>59-88</td>
<td>30</td>
<td>'aa .. aa'</td>
<td>Benutzerkennung</td>
</tr>
<tr>
<td>89-90</td>
<td>2</td>
<td>'XX XX'</td>
<td>Positiver Returncode SW1 SW2</td>
</tr>
</table>


Alternativ kann für Chipkarten vom Typ 1 das Kommando SEARCH RECORD ver-
wendet werden, um mittels eines mit übergebenen Suchmusters den "passenden"
Eintrag in einem Schritt zu finden.

Beispiel: Es soll der erste Eintrag zu einer vorgegebenen Bankleitzahl des kontofüh-
renden Instituts (an Byteposition 21-24) gefunden werden:

Command APDU:


<table>
<tr>
<th>Byte</th>
<th>Wert</th>
<th>Erläuterung</th>
</tr>
<tr>
<td>1-2</td>
<td>'00 A2'</td>
<td>CLA, INS</td>
</tr>
<tr>
<td>3</td>
<td>'01'</td>
<td>P1, Recordnummer an der die Suche startet</td>
</tr>
<tr>
<td>4</td>
<td>'D7'</td>
<td>P2, Reference Control Byte (SFI + spezifische Su- che)</td>
</tr>
<tr>
<td>5</td>
<td>'07'</td>
<td>LC</td>
</tr>
<tr>
<td>6</td>
<td>'04'</td>
<td>Control Byte</td>
</tr>
<tr>
<td>7</td>
<td>'14'</td>
<td>Offset 20 = Byte 21</td>
</tr>
<tr>
<td>8</td>
<td>'0E'</td>
<td>Konfigurationsbyte: Suche an dieser Position bis zum ersten erfolgreichen Record mit Rückgabe des Inhalts</td>
</tr>
<tr>
<td>9-12</td>
<td>'nn nn nn nn'</td>
<td>Bankleitzahl-Suchmuster</td>
</tr>
<tr>
<td>13</td>
<td>'00'</td>
<td>Le</td>
</tr>
</table>


Das Kommando SEARCH RECORD gibt bei erfolgreicher Kommandoausführung
die folgende Antwortnachricht aus:


<table>
<tr>
<th>Byte</th>
<th>Wert</th>
<th>Erläuterung</th>
</tr>
<tr>
<td>1</td>
<td>'XX'</td>
<td>Recordnummer</td>
</tr>
<tr>
<td>2-89</td>
<td>'XX..XX'</td>
<td>Recordinhalt</td>
</tr>
<tr>
<td>90-91</td>
<td>'XX XX'</td>
<td>Statusbytes</td>
</tr>
</table>


Es sind auch weitere, umfangreichere Suchoptionen möglich (z.B. alle passenden
Einträge ermitteln oder Intervallsuche), siehe hierzu [LIT 1'].


### C.2.4.2Nachricht generieren

Dieser Teil des Gesamtablaufs ist nur insofern chipkartenrelevant, als Bankverbin-
dungsdaten, die für die Auftragsgenerierung benötigt werden, aus der Chipkarte
entnommen werden. Für die folgende Ablaufbeschreibung wird angenommen, dass
die Anwendung bereits HBCI-Nachrichten generiert hat. Diese Nachrichten müssen
jetzt ggf. noch kryptographisch gesichert werden, d.h. es werden Segmente für die
elektronische(n) Signatur(en) und für die Verschlüsselung entsprechend den HBCI-
Spezifikationen eingefügt.

<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th>Version:</th>
<th>Kapitel:</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Security - Sicherheitsverfahren HBCI</td>
<td>3.0 - Final Version</td>
<td>C</td>
</tr>
<tr>
<td>Kapitel:</td>
<td>Chipapplikationen</td>
<td>Stand:</td>
<td>Seite:</td>
</tr>
<tr>
<td>Abschnitt:</td>
<td>Chipapplikation für DDV</td>
<td>18.07.2013</td>
<td>147</td>
</tr>
</table>


### C.2.4.3 Nachricht signieren

Die folgenden Abläufe können offline, d.h. außerhalb des Übertragungsdialogs voll-
zogen werden. Dies gilt für alle Nachrichten mit Ausnahme der Dialoginitialisierung.
Der Grund besteht darin, dass für die Absicherung aller Kreditinstitutsnachrichten
der Schlüssel des Senders der Dialoginitialisierungsnachricht erforderlich ist. Daher
muss auch die Chipkarte des Senders während des gesamten Dialogs im Endgerät
stecken.

Die Abläufe für die Signatur der Dialoginitialisierungsnachricht sind grundsätzlich
identisch mit den im Folgenden beschriebenen Abläufen für die Signatur von Auf-
tragsnachrichten. Da aber für die Dialoginitialisierung anwendungsseitig noch wei-
tere Chipkartendaten (Benutzerkennung, Dialog-ID, Kommunikationszugang etc.)
benötigt werden, wird der komplette Ablauf einschlieBlich der Signatur der Dialogini-
tialisierung im Kapitel C.2.4.5 "Übertragungsdialog" noch einmal beschrieben.


<table>
<tr>
<td colspan="2">HBCI-Chipkarte</td>
</tr>
<tr>
<td>R1a</td>
<td>KV</td>
</tr>
<tr>
<td>R1b</td>
<td>OK</td>
</tr>
<tr>
<td>R1c</td>
<td>Datensatz</td>
</tr>
<tr>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
</tr>
<tr>
<td>R6</td>
<td>OK</td>
</tr>
<tr>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
</tr>
</table>


<table>
<tr>
<td colspan="2">Endgerät/Gateway</td>
</tr>
<tr>
<td>C1a<br>A1a</td>
<td>GET KEYINFO (nur Typ 1)<br>Schlüsselversion KV speichern</td>
</tr>
<tr>
<td>C1b<br>C1c</td>
<td>SELECT EF_KEYD (nur Typ 0)<br>READ RECORD EF_KEYD (nur Typ 0)</td>
</tr>
<tr>
<td>A1c</td>
<td>Schlüsselversion KV speichern</td>
</tr>
<tr>
<td>A2</td>
<td>Sequenzzähler (Signatur-ID) SEQ inkre- mentieren</td>
</tr>
<tr>
<td>A3</td>
<td>Signaturkopf aufbauen und in HBCI- Nachricht einfügen</td>
</tr>
<tr>
<td>A4</td>
<td>Daten (Signaturkopf, HBCI-Nutzdaten) für MAC-Berechnung bereitstellen</td>
</tr>
<tr>
<td>M5</td>
<td>MAC über Daten berechnen (siehe Kap. C.2.5.1)</td>
</tr>
<tr>
<td>C6</td>
<td>UPDATE RECORD EF_SEQ mit SEQ</td>
</tr>
<tr>
<td>A7</td>
<td>Signaturabschluss aufbauen und in HBCI- Nachricht einfügen</td>
</tr>
<tr>
<td>A8</td>
<td>ggf. A2 bis A7 für weitere Nachrichten wiederholen</td>
</tr>
<tr>
<td>A9</td>
<td>signierte HBCI-Nachrichten zur Weiter- verarbeitung speichern</td>
</tr>
<tr>
<td>A10</td>
<td>ggf. Startdialog und A1 bis A9 für Mehr- fachsignaturen wiederholen</td>
</tr>
</table>


#### ◆ Erläuterung

1\. In diesem Schritt stellt das Terminal fest, welcher Daten-Authentikationsschlüssel
KGKDAK bzw. KDAK zur Signatur der Nachricht verwendet werden muss. Dabei wird
Schritt 1a nur für Karten vom Typ 1, Schritt 1b und 1c nur für Karten vom Typ 0
durchgeführt.

1a. Falls es sich um eine HBCI-Karte von Typ 1 handelt, wird hierzu das Kommando
GET KEYINFO verwendet.

↓ ↑ ↓ ↑
←

←
→

←
→
←
→

<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: C</td>
<td>Version: 3.0 - Final Version</td>
<td>Financial Transaction Services (FinTS) Dokument: Security - Sicherheitsverfahren HBCI</td>
</tr>
<tr>
<td>Seite:</td>
<td rowspan="2">Stand: 18.07.2013</td>
<td>Kapitel: Chipapplikationen</td>
</tr>
<tr>
<td>148</td>
<td>Abschnitt: Chipapplikation für DDV</td>
</tr>
</table>


# Command APDU:


<table>
<tr>
<th>Byte</th>
<th>Wert</th>
<th>Erläuterung</th>
</tr>
<tr>
<td>1-2</td>
<td>'BO EE'</td>
<td>CLA,INS</td>
</tr>
<tr>
<td>3</td>
<td>'80'</td>
<td>P1 für "DF-spezifisch"</td>
</tr>
<tr>
<td>4</td>
<td>'02'</td>
<td>P2, Schlüsselnummer</td>
</tr>
<tr>
<td>5</td>
<td>,00،</td>
<td>Le</td>
</tr>
</table>


Bei der erfolgreichen Ausführung des GET KEYINFO gibt die HBCI-Karte eine Ant-
wortnachricht mit der folgenden Struktur zurück:


<table>
<tr>
<th>Byte</th>
<th>Wert</th>
<th>Erläuterung</th>
</tr>
<tr>
<td>1</td>
<td>'XX'</td>
<td>1 vorhandene Schlüssel-Version KV</td>
</tr>
<tr>
<td>2-3</td>
<td>'XX XX'</td>
<td>Positiver Returncode SW1 SW2</td>
</tr>
</table>


Die Schlüsselversion wird gespeichert.

1b. Falls es sich um eine HBCI-Karte von Typ 0 handelt, wird hierzu das EF_KEYD im
DF_BANKING mittels SELECT FILE EF_KEYD ausgewählt.

Command APDU:


<table>
<tr>
<th>Byte</th>
<th>Wert</th>
<th>Erläuterung</th>
</tr>
<tr>
<td>1-2</td>
<td>'00 A4'</td>
<td>CLA, INS</td>
</tr>
<tr>
<td>3</td>
<td>'02'</td>
<td>P1, Selektion eines EF im aktuellen DF</td>
</tr>
<tr>
<td>4</td>
<td>'0C'</td>
<td>P2, Keine Antwortdaten</td>
</tr>
<tr>
<td>5</td>
<td>'02'</td>
<td>Lc</td>
</tr>
<tr>
<td>6-7</td>
<td>'00 13'</td>
<td>Datei-ID von EF_KEYD</td>
</tr>
</table>


1c. Mittels READ RECORD liest das Terminal aus Record '02' die Zusatzinformationen
für den Schlüssel KDAK·

Command APDU:


<table>
<tr>
<th>Byte</th>
<th>Wert</th>
<th>Erläuterung</th>
</tr>
<tr>
<td>1-2</td>
<td>'00 B2'</td>
<td>CLA, INS</td>
</tr>
<tr>
<td>3</td>
<td>'02'</td>
<td>P1, Recordnummer für logische Schlüsselnr. '02'</td>
</tr>
<tr>
<td>4</td>
<td>'04'</td>
<td>P2, Reference Control Byte</td>
</tr>
<tr>
<td>5</td>
<td>'00'</td>
<td>Le</td>
</tr>
</table>


Wenn das READ RECORD erfolgreich ausgeführt wurde, gibt die HBCI-Karte die
folgende Antwortnachricht zurück:


<table>
<tr>
<th>Byte</th>
<th>Wert</th>
<th>Erläuterung</th>
</tr>
<tr>
<td>1</td>
<td>'02'</td>
<td>Logische Schlüsselnummer</td>
</tr>
<tr>
<td>2</td>
<td>'10'</td>
<td>Schlüssellänge</td>
</tr>
<tr>
<td>3</td>
<td>'07'</td>
<td>Algorithmus-ID</td>
</tr>
<tr>
<td>4</td>
<td>'XX'</td>
<td>Fehlbedienungszähler</td>
</tr>
<tr>
<td>5</td>
<td>'XX'</td>
<td>Schlüssel-Version</td>
</tr>
<tr>
<td>6-7</td>
<td>'XX XX'</td>
<td>Positiver Returncode SW1 SW2</td>
</tr>
</table>


Die Schlüsselversion wird gespeichert.

<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th>Version:</th>
<th rowspan="2">Kapitel: C</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Security - Sicherheitsverfahren HBCI</td>
<td>3.0 - Final Version</td>
</tr>
<tr>
<td>Kapitel:</td>
<td>Chipapplikationen</td>
<td>Stand:</td>
<td>Seite:</td>
</tr>
<tr>
<td>Abschnitt:</td>
<td>Chipapplikation für DDV</td>
<td>18.07.2013</td>
<td>149</td>
</tr>
</table>


2\. Der zuvor gelesene und gespeicherte Sequenzzähler SEQ wird inkrementiert.

3\. Der Signaturkopf wird aufgebaut und in die HBCI-Nachricht eingefügt.

4\. Die Daten (Signaturkopf, HBCI-Nutzdaten) für die MAC-Berechnung werden bereit-
gestellt.

5\. Der MAC über die Daten wird berechnet (siehe hierzu Kap. C.2.5.1).

6\. Das Terminal überschreibt den Sequenzzähler in EF_SEQ mit dem inkrementierten
Wert. Dies geschieht durch ein UPDATE RECORD EF_SEQ ohne Secure Mes-
saging. Aufgrund der Zugriffsbedingungen für das EF_SEQ kann das Kommando
nur ausgeführt werden, wenn zuvor die HBCI-PIN erfolgreich verifiziert wurde.

Command APDU:


<table>
<tr>
<th>Byte</th>
<th>Wert</th>
<th>Erläuterung</th>
</tr>
<tr>
<td>1-2</td>
<td>'00 DC'</td>
<td>CLA, INS</td>
</tr>
<tr>
<td>3</td>
<td>'01'</td>
<td>P1, Recordnummer</td>
</tr>
<tr>
<td>4</td>
<td>'E4'</td>
<td>P2, Reference Control Byte (SFI '1C')</td>
</tr>
<tr>
<td>5</td>
<td>'02'</td>
<td>Lc</td>
</tr>
<tr>
<td>6-7</td>
<td>'XX XX'</td>
<td>neuer Sequenzzähler SEQ</td>
</tr>
</table>


7\. Der Signaturabschluß wird aufgebaut und in die HBCI-Nachricht eingefügt.

8\. Ggf. können die Schritte 2 bis 7 für weitere Nachrichten wiederholt werden. Schritt 1
braucht nicht erneut durchgeführt zu werden, da die zu verwendende Schlüsselver-
sion bereits gespeichert ist..

9\. Die signierten HBCI-Nachrichten können zur Weiterverarbeitung gespeichert wer-
den.

10\. Ggf. werden Startdialog und die Schritte 1 bis 9 für Mehrfachsignaturen wiederholt.

<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: C</td>
<td>Version: 3.0 - Final Version</td>
<td>Financial Transaction Services (FinTS) Dokument: Security - Sicherheitsverfahren HBCI</td>
</tr>
<tr>
<td rowspan="2">Seite:<br>150</td>
<td rowspan="2">Stand:<br>18.07.2013</td>
<td>Kapitel: Chipapplikationen</td>
</tr>
<tr>
<td>Abschnitt:<br>Chipapplikation für DDV</td>
</tr>
</table>


# C.2.4.4Nachricht verschlüsseln


<table>
<tr>
<td colspan="2">HBCI-Chipkarte</td>
</tr>
<tr>
<td>R1a</td>
<td>KV</td>
</tr>
<tr>
<td>R1b<br>R1c</td>
<td>OK<br>Datensatz</td>
</tr>
<tr>
<td></td>
<td></td>
</tr>
<tr>
<td>R3</td>
<td>RND</td>
</tr>
<tr>
<td>R4</td>
<td>e* KENC(KSL)</td>
</tr>
<tr>
<td>R5</td>
<td>RND</td>
</tr>
<tr>
<td>R6</td>
<td>e* KENC(KSR)</td>
</tr>
<tr>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
</tr>
</table>


<table>
<tr>
<td></td>
<td colspan="2">Endgerät/Gateway</td>
</tr>
<tr>
<td rowspan="13">← →<br>→<br>← →<br>← →<br>← →<br>←<br>→<br>← →</td>
<td>C1a<br>A1a</td>
<td>GET KEYINFO (nur Typ 1)<br>Schlüsselversion KV speichern</td>
</tr>
<tr>
<td>C1b<br>C1c<br>A1c</td>
<td>SELECT EF_AUTD (nur Typ 0)<br>READ RECORD EF_AUTD (nur Typ 0)<br>Schlüsselversion KV speichern</td>
</tr>
<tr>
<td>A2</td>
<td>Daten (HBCI-Nutzdaten und ggf. Signa- turkopf/-abschluss) für die Verschlüsse- lung bereitstellen</td>
</tr>
<tr>
<td>C3<br>A3</td>
<td>GET CHALLENGE<br>RND als Nachrichtenschlüssel-Hälfte KSL speichern</td>
</tr>
<tr>
<td>C4<br>A4</td>
<td>INTERNAL AUTHENTICATE mit KSL<br>e* KENC(KSL) speichern</td>
</tr>
<tr>
<td>C5<br>A5</td>
<td>GET CHALLENGE<br>RND als Nachrichtenschlüssel-Hälfte KSR speichern</td>
</tr>
<tr>
<td>C6<br>A6</td>
<td>INTERNAL AUTHENTICATE mit KSR<br>e* KENC(KSR) speichern</td>
</tr>
<tr>
<td>A7</td>
<td>e* KENC(KSL) mit e* KENC(KSR) zu e* KENC(KS) konkatenieren und speichern</td>
</tr>
<tr>
<td>A8</td>
<td>KSL mit KSR zu KS konkatenieren und Da- ten mit KS verschlüsseln (Triple-DES CBC-Mode, IV=0, X9.23 Padding)</td>
</tr>
<tr>
<td>A9</td>
<td>Verschlüsselungskopf aufbauen und in HBCI-Nachricht einfügen</td>
</tr>
<tr>
<td>A10</td>
<td>Verschlüsselte Daten als Binärdaten in HBCI-Nachricht einfügen</td>
</tr>
<tr>
<td>A11</td>
<td>ggf. A2 bis A10 für weitere Nachrichten wiederholen</td>
</tr>
<tr>
<td>A12</td>
<td>Verschlüsselte und signierte HBCI-Mel- dungen zur weiteren Bearbeitung spei- chern</td>
</tr>
</table>


## ◆ Erläuterung

1\. In diesem Schritt stellt das Terminal fest, welche Version des Chiffrierschlüssels
KGKENC bzw. KENC zur Verschlüsselung der Nachricht verwendet werden muß.
Dabei wird Schritt 1a nur für Karten vom Typ 1, Schritt 1b und 1c nur für Karten vom
Typ 0 durchgeführt.

1a. Falls es sich um eine HBCI-Karte von Typ 1 handelt, wird hierzu das Kommando
GET KEYINFO verwendet.

<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th>Version:</th>
<th rowspan="2">Kapitel: C</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Security - Sicherheitsverfahren HBCI</td>
<td>3.0 - Final Version</td>
</tr>
<tr>
<td>Kapitel:</td>
<td>Chipapplikationen</td>
<td>Stand:</td>
<td>Seite:</td>
</tr>
<tr>
<td>Abschnitt:</td>
<td>Chipapplikation für DDV</td>
<td>18.07.2013</td>
<td>151</td>
</tr>
</table>


# Command APDU:


<table>
<tr>
<th>Byte</th>
<th>Wert</th>
<th>Erläuterung</th>
</tr>
<tr>
<td>1-2</td>
<td>'BO EE'</td>
<td>CLA,INS</td>
</tr>
<tr>
<td>3</td>
<td>'80'</td>
<td>P1 für "DF-spezifisch"</td>
</tr>
<tr>
<td>4</td>
<td>'03'</td>
<td>P2, Schlüsselnummer</td>
</tr>
<tr>
<td>5</td>
<td>,00،</td>
<td>Le</td>
</tr>
</table>


Bei der erfolgreichen Ausführung des GET KEYINFO gibt die HBCI-Karte eine Ant-
wortnachricht mit der folgenden Struktur zurück:


<table>
<tr>
<th>Byte</th>
<th>Wert</th>
<th>Erläuterung</th>
</tr>
<tr>
<td>1</td>
<td>'XX'</td>
<td>1 vorhandene Schlüssel-Version KV</td>
</tr>
<tr>
<td>2-3</td>
<td>'XX XX'</td>
<td>Positiver Returncode SW1 SW2</td>
</tr>
</table>


Die Schlüsselversion wird gespeichert.

1b. Falls es sich um eine HBCI-Karte von Typ 0 handelt, wird hierzu das EF_AUTD im
DF_BANKING mittels SELECT FILE EF_AUTD ausgewählt.

Command APDU:


<table>
<tr>
<th>Byte</th>
<th>Wert</th>
<th>Erläuterung</th>
</tr>
<tr>
<td>1-2</td>
<td>'00 A4'</td>
<td>CLA, INS</td>
</tr>
<tr>
<td>3</td>
<td>'02'</td>
<td>P1, Selektion eines EF im aktuellen DF</td>
</tr>
<tr>
<td>4</td>
<td>'0C'</td>
<td>P2, Keine Antwortdaten</td>
</tr>
<tr>
<td>5</td>
<td>'02'</td>
<td>Lc</td>
</tr>
<tr>
<td>6-7</td>
<td>'00 14'</td>
<td>Datei-ID von EF_AUTD</td>
</tr>
</table>


1c. Mittels READ RECORD liest das Terminal die Zusatzinformationen für den Schlüs-
sel KENC. Diese sind im Record '01' des selektierten EF_AUTD zu finden.

Command APDU:


<table>
<tr>
<th>Byte</th>
<th>Wert</th>
<th>Erläuterung</th>
</tr>
<tr>
<td>1-2</td>
<td>'00 B2'</td>
<td>CLA, INS</td>
</tr>
<tr>
<td>3</td>
<td>'01'</td>
<td>P1, Recordnummer für logische Schlüsselnr. '00'</td>
</tr>
<tr>
<td>4</td>
<td>'04'</td>
<td>P2, Reference Control Byte</td>
</tr>
<tr>
<td>5</td>
<td>'00'</td>
<td>Le</td>
</tr>
</table>


Wenn das READ RECORD erfolgreich ausgeführt wurde, gibt die HBCI-Karte die
folgende Antwortnachricht zurück:


<table>
<tr>
<th>Byte</th>
<th>Wert</th>
<th>Erläuterung</th>
</tr>
<tr>
<td>1</td>
<td>'03'</td>
<td>Logische Schlüsselnummer</td>
</tr>
<tr>
<td>2</td>
<td>'10'</td>
<td>Schlüssellänge</td>
</tr>
<tr>
<td>3</td>
<td>'07'</td>
<td>Algorithmus-ID</td>
</tr>
<tr>
<td>4</td>
<td>'XX'</td>
<td>Schlüssel-Version</td>
</tr>
<tr>
<td>5-6</td>
<td>'XX XX'</td>
<td>Positiver Returncode SW1 SW2</td>
</tr>
</table>


Die Schlüsselversion wird gespeichert.

2\. Die Daten (HBCI-Nutzdaten und ggf. Signaturkopf/-abschluss) für die Verschlüsse-
lung werden bereitgestellt.

<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: C</td>
<td>Version: 3.0 - Final Version</td>
<td>Financial Transaction Services (FinTS) Dokument: Security - Sicherheitsverfahren HBCI</td>
</tr>
<tr>
<td>Seite:</td>
<td rowspan="2">Stand: 18.07.2013</td>
<td>Kapitel: Chipapplikationen</td>
</tr>
<tr>
<td>152</td>
<td>Abschnitt: Chipapplikation für DDV</td>
</tr>
</table>


3\. Mit dem Kommando GET CHALLENGE lässt sich das Terminal eine Zufallszahl von
der HBCI-Karte geben.

Command APDU:


<table>
<tr>
<th>Byte</th>
<th>Wert</th>
<th>Erläuterung</th>
</tr>
<tr>
<td>1-2</td>
<td>'00 84'</td>
<td>CLA, INS</td>
</tr>
<tr>
<td>3</td>
<td>'00'</td>
<td>P1</td>
</tr>
<tr>
<td>4</td>
<td>'00'</td>
<td>P2</td>
</tr>
<tr>
<td>5</td>
<td>'00'</td>
<td>Le</td>
</tr>
</table>


Wenn das Kommando erfolgreich ausgeführt wurde, gibt die HBCI-Karte eine 8 Byte
lange Zufallszahl als Antwortdatum aus, die als Nachrichtenschlüssel-Hälfte KSL ge-
speichert wird.

4\. Mit dem Kommando INTERNAL AUTHENTICATE wird der Wert KSL von der HBCI-
Karte mit dem Schlüssel KENC verschlüsselt und in der Antwortnachricht als e*
KENC(KSL) übergeben.

Command APDU:


<table>
<tr>
<th>Byte</th>
<th>Wert</th>
<th>Erläuterung</th>
</tr>
<tr>
<td>1-2</td>
<td>'00 88'</td>
<td>CLA, INS</td>
</tr>
<tr>
<td>3</td>
<td>'00'</td>
<td>P1</td>
</tr>
<tr>
<td>4</td>
<td>'80' oder '83'</td>
<td>P2, Typ 0: '80' (log. Schlüsselnummer '00'), Typ 1: '83' (log. Schlüsselnummer '03')</td>
</tr>
<tr>
<td>5</td>
<td>'08'</td>
<td>Lc</td>
</tr>
<tr>
<td>6-13</td>
<td>'XX .. XX'</td>
<td>Zufallszahl KSL</td>
</tr>
<tr>
<td>14</td>
<td>'00'</td>
<td>Le</td>
</tr>
</table>


Das Kommando INTERNAL AUTHENTICATE gibt folgende Antwortnachricht zu-
rück:


<table>
<tr>
<th>Byte</th>
<th>Wert</th>
<th>Erläuterung</th>
</tr>
<tr>
<td>1-8</td>
<td>'XX .. XX'</td>
<td>Verschlüsselter Wert e* KENC(KSL)</td>
</tr>
<tr>
<td>9-10</td>
<td>'XX XX'</td>
<td>Positiver Returncode SW1 SW2</td>
</tr>
</table>


5\. Mit dem Kommando GET CHALLENGE lässt sich das Terminal eine weitere Zu-
fallszahl von der HBCI-Karte geben, die als Nachrichtenschlüssel-Hälfte KSR ge-
speichert wird.

6\. Analog zu Schritt 4 wird ein INTERNAL AUTHENTICATE mit KSR durchgeführt.

7\. e* KENC(KSL) wird mit e* KENC(KSR) zu e* KENC(KS) konkateniert und gespeichert.

8\. KSL wird mit KSR zu KS konkateniert und die Daten werden mit KS verschlüsselt
(Triple-DES CBC-Mode, IV=0, X9.23 Padding).

9\. Der Verschlüsselungskopf wird aufgebaut und in die HBCI-Nachricht eingefügt.

10\. Die verschlüsselten Daten als Binärdaten in die HBCI-Nachricht eingefügt.

11\. Ggf. werden die Schritte 2 bis 10 für weitere Nachrichten wiederholt (eine Wiederho-
lung von Schritt 1 ist nicht nötig).

12\. Die verschlüsselten und signierten HBCI-Meldungen werden zur weiteren Bearbei-
tung gespeichert.

<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th>Version:</th>
<th>Kapitel:</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Security - Sicherheitsverfahren HBCI</td>
<td>3.0 - Final Version</td>
<td>C</td>
</tr>
<tr>
<td>Kapitel:</td>
<td>Chipapplikationen</td>
<td>Stand:</td>
<td>Seite:</td>
</tr>
<tr>
<td>Abschnitt:</td>
<td>Chipapplikation für DDV</td>
<td>18.07.2013</td>
<td>153</td>
</tr>
</table>


# C.2.4.5Übertragungsdialog


<table>
<tr>
<th colspan="2">Endgerät/Gateway</th>
<th></th>
<th colspan="2">Kreditinstitut</th>
</tr>
<tr>
<td>A1</td>
<td>Sequenzzähler (Signatur-ID) SEQ inkrementieren</td>
<td rowspan="15">↑↓</td>
<td></td>
<td></td>
</tr>
<tr>
<td>A2</td>
<td>Benutzerkennung aus der bereits gelesenen Bankverbindung (EF_BNK) ermitteln</td>
<td></td>
<td></td>
</tr>
<tr>
<td>A3</td>
<td>Dialoginitialisierungsnachricht auf- bauen</td>
<td></td>
<td></td>
</tr>
<tr>
<td>A4</td>
<td>Signaturkopf aufbauen und in HBCI- Nachricht einfügen</td>
<td></td>
<td></td>
</tr>
<tr>
<td>A5</td>
<td>Daten (Signaturkopf, HBCI-Nutzda- ten) für MAC-Berechnung bereit- stellen</td>
<td></td>
<td></td>
</tr>
<tr>
<td>M6</td>
<td>MAC über Daten berechnen (siehe Kap. C.2.5.1)</td>
<td></td>
<td></td>
</tr>
<tr>
<td>C7</td>
<td>UPDATE RECORD EF_SEQ mit SEQ</td>
<td></td>
<td></td>
</tr>
<tr>
<td>A8</td>
<td>Signaturabschluss aufbauen und in HBCI-Nachricht einfügen</td>
<td></td>
<td></td>
</tr>
<tr>
<td>A9</td>
<td>Kommunikationszugang aus Bank- verbindung herstellen</td>
<td></td>
<td></td>
</tr>
<tr>
<td>C10</td>
<td>Nachricht (beginnend mit Dialog- initialisierungsnachricht) senden</td>
<td>R10</td>
<td>Antwortnach- richt senden</td>
</tr>
<tr>
<td>A11</td>
<td>falls Antwortnachricht verschlüsselt: Daten (Binärdaten nach dem Signa- turkopf) und d*KENC(KS) aus dem Signaturkopf für die Entschlüsselung bereitstellen</td>
<td></td>
<td></td>
</tr>
<tr>
<td>M12</td>
<td>Daten entschlüsseln (siehe Kap. C.2.5.2)</td>
<td></td>
<td></td>
</tr>
<tr>
<td>A13</td>
<td>falls Kreditinstitutsnachricht signiert: Daten (Signaturkopf, Nutzdaten) und Referenz-MAC für MAC-Prüfung be- reitstellen</td>
<td></td>
<td></td>
</tr>
<tr>
<td>M14</td>
<td>MAC über Daten und Referenz-MAC prüfen (siehe Kap. C.2.5.2)</td>
<td></td>
<td></td>
</tr>
<tr>
<td>A15</td>
<td>C10 bis M14 für alle weiteren HBCI- Nachrichten wiederholen</td>
<td></td>
<td></td>
</tr>
</table>


HBCI-Chipkarte

↓ ↑ ↓ ↑

R7

OK

↓↑

↓↑

<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: C</td>
<td>Version: 3.0 - Final Version</td>
<td>Financial Transaction Services (FinTS) Dokument: Security - Sicherheitsverfahren HBCI</td>
</tr>
<tr>
<td rowspan="2">Seite: 154</td>
<td rowspan="2">Stand: 18.07.2013</td>
<td>Kapitel: Chipapplikationen</td>
</tr>
<tr>
<td>Abschnitt: Chipapplikation für DDV</td>
</tr>
</table>


# C.2.5 Makros


## C.2.5.1 MAC-Berechnung / Prüfung


<table>
<tr>
<td colspan="2">HBCI-Chipkarte</td>
</tr>
<tr>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
</tr>
<tr>
<td>R3</td>
<td>OK</td>
</tr>
<tr>
<td>R4</td>
<td>OK</td>
</tr>
<tr>
<td>R5</td>
<td>Daten aus EF_MAC mit CFB-64 MAC über HASHR (iden- tisch mit CBC-MAC über HASH)</td>
</tr>
</table>


<table>
<tr>
<td colspan="2">Endgerät/Gateway</td>
</tr>
<tr>
<td>A1</td>
<td>Hashwert HASH über Daten berech- nen (RIPEMD160)</td>
</tr>
<tr>
<td>A2</td>
<td>HASH zerlegen in HASHL (die linken 8 Byte von HASH) und HASHR (die rest- lichen 12 Byte)</td>
</tr>
<tr>
<td>C3</td>
<td>UPDATE RECORD EF_MAC mit HASHR</td>
</tr>
<tr>
<td>C4</td>
<td>PUT DATA mit HASHL (nur Typ 0)</td>
</tr>
<tr>
<td>C5<br>A5</td>
<td>READ RECORD EF_MAC mit Secure Messaging (für Typ 1 wird hier HASHL mit über- geben)<br>Bei MAC-Berechnung: MAC zwischen- speichern<br>Bei MAC-Prüfung: MAC aus Kreditin- stitutsnachricht mit MAC der Chipkarte vergleichen</td>
</tr>
</table>


### ◆ Erläuterung

1\. Der Hashwert HASH wird über die Daten berechnet (RIPEMD160).

2\. Der Hashwert HASH wird zerlegt in HASHL (die linken 8 Byte von HASH) und
HASHR (die restlichen 12 Byte).

3\. HASHR wird in den ersten Record des EF_MAC eingetragen. Die Zugriffsbedingung
für das EF_MAC stellt sicher, daß das UPDATE-Kommando nur ausgeführt werden
kann, wenn zuvor die HBCI-PIN verifiziert wurde.

Command APDU:


<table>
<tr>
<th>Byte</th>
<th>Wert</th>
<th>Erläuterung</th>
</tr>
<tr>
<td>1-2</td>
<td>'00 DC'</td>
<td>CLA, INS</td>
</tr>
<tr>
<td>3</td>
<td>'01'</td>
<td>P1, Recordnummer</td>
</tr>
<tr>
<td>4</td>
<td>'DC'</td>
<td>P2, Reference Control Byte (SFI '1B')</td>
</tr>
<tr>
<td>5</td>
<td>'0C'</td>
<td>Lc</td>
</tr>
<tr>
<td>6-17</td>
<td>'XX .. XX'</td>
<td>Recordinhalt HASHR</td>
</tr>
</table>


4\. Das Terminal übergibt HASHL mittels PUT DATA an die HBCI-Karte. Dieser Schritt
wird nur für Karten vom Typ 0 durchgeführt, da für Karten vom Typ 1 der Zufallswert
als Bestandteil des Kommandos im nächsten Schritt übergeben wird.

↓ ↑ ↓ ↑ ↓

→

<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th>Version:</th>
<th rowspan="2">Kapitel: C</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Security - Sicherheitsverfahren HBCI</td>
<td>3.0 - Final Version</td>
</tr>
<tr>
<td>Kapitel:</td>
<td>Chipapplikationen</td>
<td>Stand:</td>
<td>Seite:</td>
</tr>
<tr>
<td>Abschnitt:</td>
<td>Chipapplikation für DDV</td>
<td>18.07.2013</td>
<td>155</td>
</tr>
</table>


Command APDU:


<table>
<tr>
<th>Byte</th>
<th>Wert</th>
<th>Erläuterung</th>
</tr>
<tr>
<td>1-2</td>
<td>'00 DA'</td>
<td>CLA, INS</td>
</tr>
<tr>
<td>3-4</td>
<td>'01 00'</td>
<td>P1, P2</td>
</tr>
<tr>
<td>5</td>
<td>'08'</td>
<td>Lc</td>
</tr>
<tr>
<td>6-13</td>
<td>'XX..XX'</td>
<td>HASHL</td>
</tr>
</table>


5\. Das Terminal liest mittels READ RECORD den soeben in EF_MAC eingetragenen
Hash-Wert mit Secure Messaging.

Command APDU für Chipkarten vom Typ 0:


<table>
<tr>
<th>Byte</th>
<th>Wert</th>
<th>Erläuterung</th>
</tr>
<tr>
<td>1-2</td>
<td>'04 B2'</td>
<td>CLA, INS</td>
</tr>
<tr>
<td>3</td>
<td>'01'</td>
<td>P1, Recordnummer</td>
</tr>
<tr>
<td>4</td>
<td>'DC'</td>
<td>P2, Reference Control Byte</td>
</tr>
<tr>
<td>5</td>
<td>'00'</td>
<td>Le</td>
</tr>
</table>


Wenn das READ RECORD erfolgreich ausgeführt wird, gibt die HBCI-Karte eine
Antwortnachricht mit der folgenden Struktur zurück:


<table>
<tr>
<th>Byte</th>
<th>Wert</th>
<th>Erläuterung</th>
</tr>
<tr>
<td>1-12</td>
<td>'XX … XX'</td>
<td>Recordinhalt HASHR</td>
</tr>
<tr>
<td>13-20</td>
<td>'XX … XX'</td>
<td>CFB-MAC mit KENC über die 16 Byte 1-12|'00 00 00 00' mit ICV= HASHL</td>
</tr>
<tr>
<td>21-22</td>
<td>'XX XX'</td>
<td>Positiver Returncode SW1 SW2</td>
</tr>
</table>


## Command APDU für Chipkarten vom Typ 1:18


<table>
<tr>
<th>Byte</th>
<th>Wert</th>
<th>Erläuterung</th>
</tr>
<tr>
<td>1-2</td>
<td>'08 B2'</td>
<td>CLA, INS mit Secure Messaging</td>
</tr>
<tr>
<td>3</td>
<td>'01'</td>
<td>P1, Recordnummer</td>
</tr>
<tr>
<td>4</td>
<td>'DC'</td>
<td>P2, Reference Control Byte</td>
</tr>
<tr>
<td>5</td>
<td>'11'</td>
<td>LC</td>
</tr>
<tr>
<td>6-7</td>
<td>'BA 0C'</td>
<td>Tag und Länge für Response Descriptor</td>
</tr>
<tr>
<td>8-9</td>
<td>'B4 0A'</td>
<td>Tag und Länge für CCT</td>
</tr>
<tr>
<td>10-11</td>
<td>'87 08'</td>
<td>Tag und Länge für Zufallszahl</td>
</tr>
<tr>
<td>12-19</td>
<td>'XX..XX'</td>
<td>Zufallszahl HASHL</td>
</tr>
<tr>
<td>20-22</td>
<td>'96 01 00'</td>
<td>Tag, Länge und Wert des Le-Datenobjekts</td>
</tr>
<tr>
<td>23</td>
<td>'00'</td>
<td>Le</td>
</tr>
</table>


Wenn das READ RECORD erfolgreich ausgeführt wird, gibt die HBCI-Karte eine
Antwortnachricht mit der folgenden Struktur zurück:

<!-- PageFooter: 18 Bezüglich der Übergabe von ICVs über Response Descriptors siehe Kapitel 8.6.1.1 von [DATKOM]. -->
<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: C</td>
<td>Version: 3.0 - Final Version</td>
<td>Financial Transaction Services (FinTS) Dokument: Security - Sicherheitsverfahren HBCI</td>
</tr>
<tr>
<td>Seite:</td>
<td rowspan="2">Stand: 18.07.2013</td>
<td>Kapitel: Chipapplikationen</td>
</tr>
<tr>
<td>156</td>
<td>Abschnitt: Chipapplikation für DDV</td>
</tr>
</table>


<table>
<tr>
<th>Byte</th>
<th>Wert</th>
<th>Erläuterung</th>
</tr>
<tr>
<td>1-2</td>
<td>'81 0C'</td>
<td>Tag und Länge des Klartext-Datenobjekts</td>
</tr>
<tr>
<td>3-14</td>
<td>'XX … XX'</td>
<td>Recordinhalt HASHR</td>
</tr>
<tr>
<td>15-16</td>
<td>'8E 08'</td>
<td>Tag und Länge des MAC-Datenobjekts</td>
</tr>
<tr>
<td>17-24</td>
<td>'XX … XX'</td>
<td>CFB-MAC mit KDAK über die 16 Byte 1-14|'80 00' mit ICV = HASHL</td>
</tr>
<tr>
<td>25-26</td>
<td>'XX XX'</td>
<td>Positiver Returncode SW1 SW2</td>
</tr>
</table>


Das Terminal speichert den Wert des MAC.

<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th>Version:</th>
<th>Kapitel:</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Security - Sicherheitsverfahren HBCI</td>
<td>3.0 - Final Version</td>
<td>C</td>
</tr>
<tr>
<td>Kapitel:</td>
<td>Chipapplikationen</td>
<td>Stand:</td>
<td>Seite:</td>
</tr>
<tr>
<td>Abschnitt:</td>
<td>Chipapplikation für DDV</td>
<td>18.07.2013</td>
<td>157</td>
</tr>
</table>


## C.2.5.2 Entschlüsselung


<table>
<tr>
<td colspan="2">HBCI-Chipkarte</td>
</tr>
<tr>
<td></td>
<td></td>
</tr>
<tr>
<td>R2</td>
<td>KSL</td>
</tr>
<tr>
<td>R3</td>
<td>KSR</td>
</tr>
<tr>
<td></td>
<td></td>
</tr>
</table>


↓↑ ↓↑


<table>
<tr>
<td colspan="2">Endgerät/Gateway</td>
</tr>
<tr>
<td>A1</td>
<td>d* KENC(KS) in die zwei Hälften d* KENC(KSL) und d* KENC(KSR) zerlegen</td>
</tr>
<tr>
<td>C2<br>A2</td>
<td>INTERNAL AUTHENTICATE mit d* KENC(KSL)<br>KSL zwischenspeichern</td>
</tr>
<tr>
<td>C3<br>A3</td>
<td>INTERNAL AUTHENTICATE mit d* KENC(KSR)<br>KSR zwischenspeichern</td>
</tr>
<tr>
<td>A4</td>
<td>KSL mit KSR zu KS konkatenieren und Daten mit KS entschlüsseln (Triple-DES CBC- Mode, IV=0, X9.23 Padding)</td>
</tr>
</table>


### ◆ Erläuterung

1\. $\mathrm { d } ^ { * } \mathrm { K } _ { \mathrm { E N C } } \left( \mathrm { K S } \right)$ wird in die zwei Hälften $\mathrm { d } ^ { * } \mathrm { K } _ { \mathrm { E N C } } \left( \mathrm { K S } _ { \mathrm { L } } \right)$ und $\mathrm { d } ^ { * } \mathrm { K } _ { \mathrm { E N C } } \left( \mathrm { K S } _ { \mathrm { R } } \right)$ zerlegt.

2\. Mit dem Kommando INTERNAL AUTHENTICATE wird der Wert $\mathrm { d } ^ { * } \mathrm { K } _ { \mathrm { E N C } } \left( \mathrm { K S } _ { \mathrm { L } } \right)$ von
der HBCI-Karte mit dem Schlüssel KENC entschlüsselt und in der Antwortnachricht
als KSL übergeben.

Command APDU:


<table>
<tr>
<th>Byte</th>
<th>Wert</th>
<th>Erläuterung</th>
</tr>
<tr>
<td>1-2</td>
<td>'00 88'</td>
<td>CLA, INS</td>
</tr>
<tr>
<td>3</td>
<td>'00'</td>
<td>P1</td>
</tr>
<tr>
<td>4</td>
<td>'80' oder '83'</td>
<td>P2, Typ 0: '80' (log. Schlüsselnummer '00'), Typ 1: '83' (log. Schlüsselnummer '03')</td>
</tr>
<tr>
<td>5</td>
<td>'08'</td>
<td>Lc</td>
</tr>
<tr>
<td>6-13</td>
<td>'XX .. XX'</td>
<td>Parameterwert d* $\mathrm { K } _ { \mathrm { E N C } } \left( \mathrm { K S } _ { \mathrm { L } } \right)$</td>
</tr>
<tr>
<td>14</td>
<td>'08'</td>
<td>Le</td>
</tr>
</table>


Das Kommando INTERNAL AUTHENTICATE gibt folgende Antwortnachricht zu-
rück:


<table>
<tr>
<th>Byte</th>
<th>Wert</th>
<th>Erläuterung</th>
</tr>
<tr>
<td>1-8</td>
<td>'XX .. XX'</td>
<td>Entschlüsselter Wert KSL</td>
</tr>
<tr>
<td>9-10</td>
<td>'XX XX'</td>
<td>Positiver Returncode SW1 SW2</td>
</tr>
</table>


KSL wird gespeichert.

3\. Analog zu Schritt 2 wird ein INTERNAL AUTHENTICATE mit d* $\mathrm { K } _ { \mathrm { E N C } } \left( \mathrm { K S } _ { \mathrm { R } } \right)$ durchge-
führt. Das Ergebnis wird als KSR gespeichert.

4\. KSL wird mit KSR zu KS konkateniert und die Daten werden mit KS entschlüsselt
(Triple-DES CBC-Mode, IV=0, X9.23 Padding).

<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: C</td>
<td>Version: 3.0 - Final Version</td>
<td>Financial Transaction Services (FinTS) Dokument: Security - Sicherheitsverfahren HBCI</td>
</tr>
<tr>
<td>Seite:</td>
<td rowspan="2">Stand: 18.07.2013</td>
<td>Kapitel: Chipapplikationen</td>
</tr>
<tr>
<td>158</td>
<td>Abschnitt: Chipapplikation für DDV</td>
</tr>
</table>


## C.2.6 Übersicht der Chip-Applikations-Parameter


### . Dateistruktur


<table>
<tr>
<th>Lage</th>
<th>Datei- ID</th>
<th>Name</th>
<th>SFI</th>
<th>Zugriffsregel SE #1 (Standard)</th>
<th>Zugriffsregel SE #2 (Admin)</th>
</tr>
<tr>
<td rowspan="2">MF</td>
<td>'00 03'</td>
<td>EF_ID</td>
<td>'19'</td>
<td></td>
<td></td>
</tr>
<tr>
<td>'A6 00'</td>
<td>DF_BANKING_20</td>
<td></td>
<td></td>
<td>1</td>
</tr>
<tr>
<td rowspan="9">DF_BANKING_20</td>
<td>'00 30'</td>
<td>EF_RULE</td>
<td>'01'</td>
<td>2</td>
<td>3</td>
</tr>
<tr>
<td>'00 10'</td>
<td>EF_KEY</td>
<td>'02'</td>
<td>--</td>
<td>4</td>
</tr>
<tr>
<td>'00 12'</td>
<td>EF_PWD</td>
<td>'03'</td>
<td>--</td>
<td>4</td>
</tr>
<tr>
<td>'00 13'</td>
<td>EF_KEYD</td>
<td>'1E'</td>
<td>2</td>
<td>5</td>
</tr>
<tr>
<td>'00 15'</td>
<td>EF_PWDD</td>
<td>'04'</td>
<td>2</td>
<td>5</td>
</tr>
<tr>
<td>'00 16'</td>
<td>EF_FBZ</td>
<td>'05'</td>
<td>2</td>
<td>5</td>
</tr>
<tr>
<td>'03 01'</td>
<td>EF_BNK</td>
<td>'1A'</td>
<td>6</td>
<td>3</td>
</tr>
<tr>
<td>'03 02'</td>
<td>EF_MAC</td>
<td>'1B'</td>
<td>7</td>
<td>3</td>
</tr>
<tr>
<td>'03 03'</td>
<td>EF_SEQ</td>
<td>'1C'</td>
<td>6</td>
<td>5</td>
</tr>
</table>


### . Zugriffsregeln


<table>
<tr>
<th>#</th>
<th>READ / SEARCH RECORD</th>
<th>APPEND RECORD</th>
<th>UPDATE RECORD</th>
<th>IN-/EXCLUDE CREATE EF DELETE self</th>
<th>VERIFY CHANGE REF DATA</th>
<th>RESET RETRY COUNTER</th>
</tr>
<tr>
<td>1</td>
<td></td>
<td></td>
<td></td>
<td colspan="2">KHBCI_Admin-MAC</td>
<td></td>
</tr>
<tr>
<td>2</td>
<td>ALW</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>3</td>
<td></td>
<td>KHBCI_Admin“ MAC</td>
<td>NEV</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>4</td>
<td></td>
<td colspan="2">KHBCI_Admin-ENC-MAC (K) KHBCI_Admin-MAC (A)</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>5</td>
<td></td>
<td colspan="2">KHBCI_Admin-MAC</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>6</td>
<td>ALW</td>
<td></td>
<td>HBCI-PIN</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>7</td>
<td>HBCI-PIN KDAK-MAC (A)</td>
<td></td>
<td>HBCI-PIN</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>8</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>ALW</td>
<td>KHBCI_Admin“ MAC</td>
</tr>
</table>


Die angegebenen Access Conditions gelten sowohl für Kommando- (K) als auch
Antwortnachrichten (A), sonst in Klammern eingeschränkt.


### ◆ Schlüssel der Applikation


<table>
<tr>
<th>Logische Schlüsselnr.</th>
<th>Erlaubte SE #</th>
<th>Schlüssel</th>
<th>Wer kennt den Masterschlüssel</th>
</tr>
<tr>
<td>'01'</td>
<td>2</td>
<td>KHBCI_Admin</td>
<td>zuständiges Hintergrundsystem</td>
</tr>
<tr>
<td>'02'</td>
<td>1</td>
<td>KDAK</td>
<td>zuständiges Hintergrundsystem</td>
</tr>
<tr>
<td>'03'</td>
<td>1</td>
<td>KENC</td>
<td>zuständiges Hintergrundsystem</td>
</tr>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th>Version:</th>
<th>Kapitel:</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Security - Sicherheitsverfahren HBCI</td>
<td>3.0 - Final Version</td>
<td>D</td>
</tr>
<tr>
<td>Kapitel:</td>
<td>Data Dictionary</td>
<td>Stand:</td>
<td>Seite:</td>
</tr>
<tr>
<td>Abschnitt:</td>
<td>Buchstabe A</td>
<td>18.07.2013</td>
<td>159</td>
</tr>
</table>


# D. DATA DICTIONARY

A


## Austauschkontrollreferenz

Dialog-ID der korrespondierenden Nachricht des Kunden (vgl. [HBCI], Kapi-
tel II.6.2).


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


B


## Benutzerdefinierte Signatur

Bei nicht-schlüsselbasierten Sicherheitsverfahren kann der Benutzer hier
Angaben zur Authentisierung machen. Ob das Feld verpflichtend ist, ist vom
jeweiligen Sicherheitsverfahren abhängig.

Format: s. Spezifikation „Sicherheitsverfahren PIN/TAN“

Typ:
DEG

Format:

Länge:

Version:
1


## Benutzerkennung

Eindeutig vergebene Kennung, anhand deren die Identifizierung des Benut-
zers erfolgt. Die Vergabe obliegt dem Kreditinstitut. Das Kreditinstitut hat zu
gewährleisten, dass die Benutzerkennung institutsweit eindeutig ist. Sie kann
beliebige Informationen enthalten, darf aber bei Verwendung des RAH- bzw.
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


## Bereich der Sicherheitsapplikation, kodiert

Information darüber, welche Daten vom kryptographischen Prozess verarbei-
tet werden. Diese Information wird benötigt um z.B. zwischen relevanter und
belangloser Reihenfolge von Signaturen zu unterscheiden (vgl. [HBCI], Kapi-
tel VI.4).

Wenn SHM gewählt wird, so bedeutet dies, dass nur über den eigenen Sig-
naturkopf sowie die HBCI-Nutzdaten ein Hashwert gebildet wird, der in die
Signatur eingeht. Dies entspricht bei Mehrfachsignaturen einer bedeutungs-
losen Reihenfolge.

<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: D</td>
<td>Version: 3.0 - Final Version</td>
<td>Financial Transaction Services (FinTS) Dokument: Security - Sicherheitsverfahren HBCI</td>
</tr>
<tr>
<td>Seite:<br>160</td>
<td>Stand:<br>18.07.2013</td>
<td>Kapitel: Data Dictionary<br>Abschnitt:<br>Buchstabe B</td>
</tr>
</table>


Wenn SHT gewählt wird, dann werden auch alle schon vorhandenen Signa-
turköpfe und -abschlüsse mitsigniert. Das heißt, dass die Reihenfolge der
Signaturen relevant ist.

Codierung:

1: Signaturkopf und HBCI-Nutzdaten (SHM)

2: Von Signaturkopf bis Signaturabschluss (SHT)


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


## Bezeichner für Algorithmusparameter, IV

Eigenschaft betreffend den Initialisierungswert für die Verfahren DDV, RAH
und RDH (Die Steuerung erfolgt in den BPD, vgl. [HBCI], Kapitel IV.4).

Codierung:

1: Initialization value, clear text (IVC)


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


## Bezeichner für Algorithmusparameter, Schlüssel

Eigenschaft des Schlüssels für die Verfahren DDV, RAH und RDH (Die
Steuerung erfolgt in den BPD, vgl. [HBCI], Kapitel IV.4).


### Codierung:

5: Symmetrischer Schlüssel, ver- bzw. entschlüsselt mit einem symmetri-
schen Schlüssel bei DDV (KYE) (vgl. [HBCI], Kapitel VI.2.2.1).

6: Symmetrischer Schlüssel, verschlüsselt mit einem öffentlichen Schlüssel
bei RAH und RDH (KYP).


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


### Bezeichner für Exponent

Enthält den Bezeichner für den Exponent des öffentlichen Schlüssels.

Codierung:

13: Exponent (EXP)


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


<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th>Version:</th>
<th>Kapitel:</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Security - Sicherheitsverfahren HBCI</td>
<td>3.0 - Final Version</td>
<td>D</td>
</tr>
<tr>
<td>Kapitel:</td>
<td>Data Dictionary</td>
<td>Stand:</td>
<td>Seite:</td>
</tr>
<tr>
<td>Abschnitt:</td>
<td>Buchstabe B</td>
<td>18.07.2013</td>
<td>161</td>
</tr>
</table>


## Bezeichner für Funktionstyp

Enthält den Bezeichner für den Funktionstyp des Key-Management.

Codierung:

112: 'Certificate Replacement' (Ersatz des Zertifikats) im Zusammenhang
mit der Schlüsseländerung

124: 'Certificate Status Request' im Zusammenhang mit der Anfrage für ei-
nen öffentlichen Schlüssel

224: 'Certificate Status Notice' im Zusammenhang mit der Übermittlung ei-
nes öffentlichen Schlüssels

130 : 'Certificate Revocation' (Zertifikatswiderruf) im Zusammenhang mit der
Schlüsselsperrung

231: 'Revocation Confirmation' (Bestätigung des Zertifikatswiderrufs) im Zu-
sammenhang mit der Bestätigung der Schlüsselsperrung


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


## Bezeichner für Hashalgorithmusparameter

Bezeichner für den Hashalgorithmusparameter.

Codierung:

1: IVC (Initialization value, clear text)


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


## Bezeichner für Modulus

Bezeichner für den Modulus des öffentlichen Schlüssels.

Codierung:

12: Modulus (MOD)


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


## Bezeichner für Sicherheitspartei

Identifikation der Funktion der beschriebenen Partei, in diesem Falle des
Kunden.


### Codierung:

1: Message Sender (MS), wenn ein Kunde etwas an sein Kreditinstitut sen-
det.

2: Message Receiver (MR), wenn das Kreditinstitut etwas an seinen Kunden
sendet.

<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: D</td>
<td>Version: 3.0 - Final Version</td>
<td>Financial Transaction Services (FinTS) Dokument: Security - Sicherheitsverfahren HBCI</td>
</tr>
<tr>
<td rowspan="2">Seite:<br>162</td>
<td rowspan="2">Stand:<br>18.07.2013</td>
<td>Kapitel: Data Dictionary</td>
</tr>
<tr>
<td>Abschnitt:<br>Buchstabe C</td>
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


#### Bezugssegment

Sofern sich ein Kreditinstitutssegment auf ein bestimmtes Kundensegment
bezieht (z.B. Antwortrückmeldung auf einen Kundenauftrag) hat das Kredit-
institut die Segmentnummer des Segments der Kundennachricht einzustel-
len, auf das sich das aktuelle Segment bezieht (s. DE „Segmentnummer“). In
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


C


##### CID

(Cardholder Identification) Identifikation der verwendeten Chipkarte. Die CID
steht sowohl bei DDV-Chipkarten als auch bei Signaturkarten im EF_ID der
Karte. Im DDV-Verfahren dient die CID dem Kreditinstitut zur Herleitung des
kartenindividuellen Schlüssels.


<table>
<tr>
<td>Typ:</td>
<td>DE</td>
</tr>
<tr>
<td>Format:</td>
<td>bin</td>
</tr>
<tr>
<td>Länge:</td>
<td>.256</td>
</tr>
<tr>
<td>Version:</td>
<td>1</td>
</tr>
</table>


D


###### Daten, verschlüsselt

Enthält die verschlüsselten (und komprimierten) Daten.


<table>
<tr>
<td>Typ:</td>
<td>DE</td>
</tr>
<tr>
<td>Format:</td>
<td>bin</td>
</tr>
<tr>
<td>Länge:</td>
<td>..</td>
</tr>
<tr>
<td>Version:</td>
<td>1</td>
</tr>
</table>


###### Datum

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


<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th>Version:</th>
<th>Kapitel:</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Security - Sicherheitsverfahren HBCI</td>
<td>3.0 - Final Version</td>
<td>D</td>
</tr>
<tr>
<td>Kapitel:</td>
<td>Data Dictionary</td>
<td>Stand:</td>
<td>Seite:</td>
</tr>
<tr>
<td>Abschnitt:</td>
<td>Buchstabe F</td>
<td>18.07.2013</td>
<td>163</td>
</tr>
</table>


## Datum- und Zeitbezeichner, kodiert

Enthält die Bedeutung des Zeitstempels.

Codierung:

1: Sicherheitszeitstempel (STS)

6: Certificate Revocation Time (CRT)


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


F


## Filterfunktion

Falls das Übertragungsverfahren eine Umwandlung der Nachricht in eine
7 Bit-Zeichendarstellung erfordert (z.B. Internet), so ist hier das anzuwen-
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


H


## Hashalgorithmus

Angaben zu einem kryptographischen Algorithmus, seinen Operations-
modus, sowie dessen Einsatz.


<table>
<tr>
<th>Nr.</th>
<th>Name</th>
<th>Typ</th>
<th>For- mat</th>
<th>Län- ge</th>
<th>Sta- tus</th>
<th>An- zahl</th>
<th>Restriktionen</th>
</tr>
<tr>
<td>1</td>
<td>Verwendung des Hashalgorithmus, kodiert</td>
<td>DE</td>
<td>code</td>
<td>.3</td>
<td>M</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td>2</td>
<td>Hashalgorithmus, kodiert</td>
<td>DE</td>
<td>code</td>
<td>..3</td>
<td>M</td>
<td>1</td>
<td>1, 3, 4, 5, 6, 999</td>
</tr>
<tr>
<td>3</td>
<td>Bezeichner für Hash- algorithmusparame- ter</td>
<td>DE</td>
<td>code</td>
<td>..3</td>
<td>M</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td>4</td>
<td>Wert des Hashalgo- rithmusparameters</td>
<td>DE</td>
<td>bin</td>
<td>..512</td>
<td>O</td>
<td>1</td>
<td></td>
</tr>
</table>


<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: D</td>
<td>Version: 3.0 - Final Version</td>
<td>Financial Transaction Services (FinTS) Dokument: Security - Sicherheitsverfahren HBCI</td>
</tr>
<tr>
<td>Seite:<br>164</td>
<td>Stand:<br>18.07.2013</td>
<td>Kapitel: Data Dictionary<br>Abschnitt:<br>Buchstabe I</td>
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


## Hashalgorithmus, kodiert

Code des verwendeten Hash-Algorithmus.

Codierung:

1: SHA-1

2: belegt

3: SHA-256

4: SHA-384

5: SHA-512

6: SHA-256 / SHA-256

999: Gegenseitig vereinbart (ZZZ); hier: RIPEMD-160


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


![](figures/178.1)


Wird als ,,Hashalgorithmus, kodiert“ die Option „6: SHA-256 /
SHA256“ gewählt, so findet ein Hashing sowohl in Software
als auch in der Bankensignaturkarte statt.

Die Anwendung muss dafür Sorge tragen, dass in der Karte
das gewünschte Hashverfahren - hier SHA-256 - selektiert
wird; ansonsten würde in dort das Default-Hashverfahren
angewendet, was nicht zulässig ist.

I


# Identifizierung der Partei

Code, welcher die (Kommunikations-)Partei identifiziert. Bei Verwendung des
RDH-Verfahrens ist die Kundensystem-ID einzustellen.


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
<th>Version:</th>
<th>Kapitel:</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Security - Sicherheitsverfahren HBCI</td>
<td>3.0 - Final Version</td>
<td>D</td>
</tr>
<tr>
<td>Kapitel:</td>
<td>Data Dictionary</td>
<td>Stand:</td>
<td>Seite:</td>
</tr>
<tr>
<td>Abschnitt:</td>
<td>Buchstabe K</td>
<td>18.07.2013</td>
<td>165</td>
</tr>
</table>


# K


## Kommunikationsadresse

Beim Zugang über TCP/IP ist die IP-Adresse als alphanumerischer Wert
(z.B. '123.123.123.123') einzustellen.

Beim Zugang über https ist die Adresse des Servlets als alphanumerischer
Wert (z.B. [,,https://www.xyz.de:7000/Servlet"](https://www.xyz.de:7000/Servlet)) einzustellen.


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
<td>.512</td>
</tr>
<tr>
<td>Version:</td>
<td>1</td>
</tr>
</table>


### Kommunikationsadressenzusatz

Beim Zugang über TCP/IP und https wird das Feld nicht belegt.


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


### Kommunikationsdienst

Unterstütztes Kommunikationsverfahren (Protokollstack).

Zur Zeit unterstützte Kommunikationsverfahren:

1: nicht belegt

2: TCP/IP (Protokollstack SLIP/PPP)

3: https


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
<td>3</td>
</tr>
</table>


### Kommunikationsparameter

Die Kommunikationsparameter enthalten Informationen für den Aufbau der
Transportverbindung.


<table>
<tr>
<th>Nr.</th>
<th>Name</th>
<th>Typ</th>
<th>For- mat</th>
<th>Län- ge</th>
<th>Sta- tus</th>
<th>An- zahl</th>
<th>Restriktionen</th>
</tr>
<tr>
<td>1</td>
<td>Kommunikationsdienst</td>
<td>DE</td>
<td>num</td>
<td>..2</td>
<td>M</td>
<td>1</td>
<td>1,2,3</td>
</tr>
<tr>
<td>2</td>
<td>Kommunikationsadres- se</td>
<td>DE</td>
<td>an</td>
<td>..512</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>3</td>
<td>Kommunikationsadres- senzusatz</td>
<td>DE</td>
<td>an</td>
<td>..512</td>
<td>C</td>
<td>1</td>
<td>M: ,Kommunikations- dienst' = 1 N: sonst</td>
</tr>
<tr>
<td>4</td>
<td>Filterfunktion</td>
<td>DE</td>
<td>an</td>
<td>3</td>
<td>C</td>
<td>1</td>
<td>MIM, UUE M: ,Kommunikations- dienst' = 2 N: sonst</td>
</tr>
<tr>
<td>5</td>
<td>Version der Filterfunk- tion</td>
<td>DE</td>
<td>num</td>
<td>..3</td>
<td>C</td>
<td>1</td>
<td>O: ,Filterfunktion' belegt N: sonst</td>
</tr>
</table>


<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: D</td>
<td>Version: 3.0 - Final Version</td>
<td>Financial Transaction Services (FinTS) Dokument: Security - Sicherheitsverfahren HBCI</td>
</tr>
<tr>
<td>Seite:<br>166</td>
<td>Stand:<br>18.07.2013</td>
<td>Kapitel: Data Dictionary<br>Abschnitt:<br>Buchstabe K</td>
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


## Komprimierungsfunktion

Code der unterstützten Komprimierungsfunktion.

Codierung:

0: Keine Kompression (NULL)

1: Lempel, Ziv, Welch (LZW)

2: Optimized LZW (COM)

3: Lempel, Ziv (LZSS)

4: LZ + Huffman Coding (LZHuf)

5: PKZIP (ZIP)

6: deflate (GZIP) [(http://www.gzip.org/zlib)](http://www.gzip.org/zlib)

7: bzip2 [(http://sourceware.cygnus.com/bzip2/)](http://sourceware.cygnus.com/bzip2/)

999: Gegenseitig vereinbart (ZZZ)


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


## Komprimierungsversion

Version der unterstützten Komprimierungsfunktion.

Momentan werden alle zulässigen Komprimierungsfunktionen mit Version 1
verwendet. Falls keine Komprimierung verwendet wird (Komprimierungs-
funktion 0), wird Version 0 angegeben.


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


## Kreditinstitutscode

Landesspezifische Kennung, die das Kreditinstitut eindeutig identifiziert. In
Deutschland wird die Bankleitzahl eingestellt. Bei Kreditinstituten, die in Län-
dern ohne Institutskennungssystem beheimatet sind, kann die Belegung ent-
fallen.


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


<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th>Version:</th>
<th>Kapitel:</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Security - Sicherheitsverfahren HBCI</td>
<td>3.0 - Final Version</td>
<td>D</td>
</tr>
<tr>
<td>Kapitel:</td>
<td>Data Dictionary</td>
<td>Stand:</td>
<td>Seite:</td>
</tr>
<tr>
<td>Abschnitt:</td>
<td>Buchstabe L</td>
<td>18.07.2013</td>
<td>167</td>
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


## Kunden-ID

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


L


## Länderkennzeichen

Länderkennzeichen gemäß ISO 3166-1 (numerischer Code) (s. [Formals],
Kap. „Anlagen“). Für Deutschland wird der Code 280 verwendet da dieser im
Kreditgewerbe gebräuchlicher als der neue Code 276 ist.


<table>
<tr>
<td>Typ:</td>
<td>DE</td>
</tr>
<tr>
<td>Format:</td>
<td>ctr</td>
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


N


## Nachrichtenbeziehung, kodiert

Code der Nachrichtenbeziehung. Im Zusammenhang mit der Übermittlung
eines öffentlichen Schlüssels oder mit der Bestätigung der Schlüssel-
sperrung ist der Wert ,1" vorgesehen. Im Zusammenhang mit der Schlüssel-
änderung, mit der Anfrage nach einem öffentlichen Schlüssel oder mit der
Schlüsselsperrung ist der Wert „2“ vorgesehen.


### Codierung:

1: Key-Management-Nachricht ist Antwort

2: Key-Management-Nachricht erwartet Antwort


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


<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: D</td>
<td>Version: 3.0 - Final Version</td>
<td>Financial Transaction Services (FinTS) Dokument: Security - Sicherheitsverfahren HBCI</td>
</tr>
<tr>
<td rowspan="2">Seite:<br>168</td>
<td rowspan="2">Stand:<br>18.07.2013</td>
<td>Kapitel: Data Dictionary</td>
</tr>
<tr>
<td>Abschnitt:<br>Buchstabe O</td>
</tr>
</table>


## Nachrichtenreferenznummer

Nachrichtennummer der korrespondierenden Nachricht des Kunden.


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


O


## Öffentlicher Schlüssel

Information, die beim RAH-/RDH-Key-Management zum Transport des öf-
fentlichen Schlüssels zwischen Kunde und Kreditinstitut bzw. umgekehrt
dient.


<table>
<tr>
<th>Nr.</th>
<th>Name</th>
<th>Typ</th>
<th>For- mat</th>
<th>Län- ge</th>
<th>Sta- tus</th>
<th>An- zahl</th>
<th>Restriktionen</th>
</tr>
<tr>
<td>1</td>
<td>Verwendungszweck für öffentlichen Schlüssel</td>
<td>DE</td>
<td>code</td>
<td>..3</td>
<td>M</td>
<td>1</td>
<td>5,6</td>
</tr>
<tr>
<td>2</td>
<td>Operationsmodus, kodiert</td>
<td>DE</td>
<td>code</td>
<td>..3</td>
<td>M</td>
<td>1</td>
<td>2, 16, 17, 18, 19</td>
</tr>
<tr>
<td>3</td>
<td>Verfahren Benutzer</td>
<td>DE</td>
<td>code</td>
<td>..3</td>
<td>M</td>
<td>1</td>
<td>10</td>
</tr>
<tr>
<td>4</td>
<td>Wert für Modulus</td>
<td>DE</td>
<td>bin</td>
<td>.512</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>5</td>
<td>Bezeichner für Modu- lus</td>
<td>DE</td>
<td>code</td>
<td>..3</td>
<td>M</td>
<td>1</td>
<td>12</td>
</tr>
<tr>
<td>6</td>
<td>Wert für Exponent</td>
<td>DE</td>
<td>bin</td>
<td>.512</td>
<td>M</td>
<td>1</td>
<td>65537</td>
</tr>
<tr>
<td>7</td>
<td>Bezeichner für Expo- nent</td>
<td>DE</td>
<td>code</td>
<td>..3</td>
<td>M</td>
<td>1</td>
<td>13</td>
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


## Operationsmodus, kodiert

Information über den Operationsmodus für den jeweils verwendeten Kryp-
toalgorithmus (zur Signaturbildung oder zur Verschlüsselung).

Codierung:


<table>
<tr>
<th>Code</th>
<th>Operationsmodus</th>
<th>Verwendung</th>
</tr>
<tr>
<td>2:</td>
<td>Cipher Block Chaining (CBC)</td>
<td>Nur für Verschlüsselung erlaubt (vgl. [HBCI], Kapitel VI.2.2)</td>
</tr>
<tr>
<td>16:</td>
<td>ISO 9796-1 (bei RDH),</td>
<td>Nur für Signatur erlaubt</td>
</tr>
<tr>
<td>17:</td>
<td>ISO 9796-2 mit Zufallszahl (bei RDH)</td>
<td>Nur für Signatur erlaubt</td>
</tr>
<tr>
<td>18:</td>
<td>RSASSA-PKCS#1 V1.5 (bei RDH) bzw. RSAES-PKCS#1 V1.5 (bei RAH, RDH)</td>
<td>Nur für Signatur erlaubt<br>Nur für Verschlüsselung erlaubt</td>
</tr>
<tr>
<td>19:</td>
<td>RSASSA-PSS (bei RAH, RDH)</td>
<td>Nur für Signatur erlaubt</td>
</tr>
<tr>
<td>999:</td>
<td>Gegenseitig vereinbart (ZZZ); bei DDV bedeutet dies die Bildung eines Retail- MAC für die Berechnung der Signatur</td>
<td>Nur für Signatur erlaubt (vgl. [HBCI], Kap. VI.2.1)</td>
</tr>
</table>


<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th>Version:</th>
<th>Kapitel:</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Security - Sicherheitsverfahren HBCI</td>
<td>3.0 - Final Version</td>
<td>D</td>
</tr>
<tr>
<td>Kapitel:</td>
<td>Data Dictionary</td>
<td>Stand:</td>
<td>Seite:</td>
</tr>
<tr>
<td>Abschnitt:</td>
<td>Buchstabe R</td>
<td>18.07.2013</td>
<td>169</td>
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


R


# Rolle des Sicherheitslieferanten, kodiert

Kodierte Information über das Verhältnis desjenigen, der bezüglich der zu si-
chernden Nachricht die Sicherheit gewährleistet.

Die Wahl ist von der bankfachlichen Auslegung der Signatur, respektive vom
vertraglichen Zustand zwischen Kunde und Kreditinstitut abhängig.

Codierung:

1: Der Unterzeichner ist Herausgeber der signierten Nachricht, z.B. Erfasser
oder Erstsignatur (ISS)

3: Der Unterzeichner unterstützt den Inhalt der Nachricht, z.B. bei Zweitsig-
natur (CON)

4: Der Unterzeichner ist Zeuge, aber für den Inhalt der Nachricht nicht ver-
antwortlich, z.B. Übermittler, welcher nicht Erfasser ist (WIT)


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


S


## Schlüsselart

Information über die Art des Schlüssels.

Bei den Sicherheitsverfahren RAH und RDH steht die Schlüsselart in engem
Zusammenhang mit dem Datenelement "Verwendungszweck für öffentlichen
Schlüssel". Die Inhalte beider Datenelemente sind konsistent zu halten.

Codierung:

D: Schlüssel zur Erzeugung digitaler Signaturen (DS-Schlüssel)

S: Signierschlüssel

V: Chiffrierschlüssel

Der DS-Schlüssel steht nur im Zusammenhang mit einer Bankensignatur-
karte zur Verfügung.

Im Falle der Bankensignaturkarte ergibt sich folgende Zuordnung zu den
Kartenschlüsseln:

\- DS-Schlüssel:
SK.CH.DS

\- Signierschlüssel: SK.CH.AUT

\- Chiffrierschlüssel: SK.CH.KE

<!-- PageBreak -->


<table>
<tr>
<td>Kapitel:</td>
<td>Version:</td>
<td>Financial Transaction Services (FinTS)</td>
</tr>
<tr>
<td>D</td>
<td>3.0 - Final Version</td>
<td>Dokument: Security - Sicherheitsverfahren HBCI</td>
</tr>
<tr>
<td>Seite:</td>
<td>Stand:</td>
<td>Kapitel: Data Dictionary</td>
</tr>
<tr>
<td>170</td>
<td>18.07.2013</td>
<td>Abschnitt: Buchstabe S</td>
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


# Schlüsselname

Verwendeter Schlüsselnamen beim RAH- und RDH-Verfahren respektive die
Referenz auf den Chiffrierschlüssel beim DDV-Verfahren in strukturierter
Form. Mit dieser Information kann die Referenz auf einen Schlüssel herge-
stellt werden.

Dabei enthält das DE „Benutzerkennung“ bei Schlüsseln des Kunden die
Benutzerkennung, mit der der Kunde eindeutig identifiziert wird. Bei Schlüs-
seln des Kreditinstituts ist dagegen eine beliebige Kennung einzustellen, die
dazu dient, den Kreditinstitutsschlüssel eindeutig zu identifizieren. Diese
Kennung darf weder einer anderen gültigen Benutzerkennung des Kreditin-
stituts noch der Benutzerkennung für den anonymen Zugang entsprechen.


<table>
<tr>
<th>Nr.</th>
<th>Name</th>
<th>Typ</th>
<th>For- mat</th>
<th>Län- ge</th>
<th>Sta- tus</th>
<th>An- zahl</th>
<th>Restriktionen</th>
</tr>
<tr>
<td>1</td>
<td>Kreditinstitutsken- nung</td>
<td>DEG</td>
<td>kik</td>
<td>#</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>2</td>
<td>Benutzerkennung</td>
<td>DE</td>
<td>id</td>
<td>#</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>3</td>
<td>Schlüsselart</td>
<td>DE</td>
<td>code</td>
<td>1</td>
<td>M</td>
<td>1</td>
<td>D, S, V</td>
</tr>
<tr>
<td>4</td>
<td>Schlüsselnummer</td>
<td>DE</td>
<td>num</td>
<td>..3</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>5</td>
<td>Schlüsselversion</td>
<td>DE</td>
<td>num</td>
<td>..3</td>
<td>M</td>
<td>1</td>
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
<td>3</td>
</tr>
</table>


## Schlüsselnummer

Schlüsselnummer des entsprechenden Schlüssels.


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


## Schlüsselversion

Versionsnummer des entsprechenden Schlüssels.


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
<th>Version:</th>
<th>Kapitel:</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Security - Sicherheitsverfahren HBCI</td>
<td>3.0 - Final Version</td>
<td>D</td>
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
<td>18.07.2013</td>
<td>171</td>
</tr>
</table>


# Segmentkennung

Segmentspezifische Kennung, die jedem Segment bzw. Auftrag zugeordnet
ist (z.B. "HKUEB" für "Einzelüberweisung"). Die Angabe hat in Großschrei-
bung zu erfolgen.


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


![](figures/185.1)


Falls der Kunde ein Segment mit einer veralteten Versions-
nummer einreicht, sollte ihm in einer entsprechenden War-
nung rückgemeldet werden, dass sein Kundenprodukt aktua-
lisiert werden sollte.


# Segmentkopf

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
<th>Typ</th>
<th>For- mat</th>
<th>Län- ge</th>
<th>Sta- tus</th>
<th>An- zahl</th>
<th>Restriktionen</th>
</tr>
<tr>
<td>1</td>
<td>Segmentkennung</td>
<td>DE</td>
<td>an</td>
<td>..6</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>2</td>
<td>Segmentnummer</td>
<td>DE</td>
<td>num</td>
<td>..3</td>
<td>M</td>
<td>1</td>
<td>&gt;=1</td>
</tr>
<tr>
<td>3</td>
<td>Segmentversion</td>
<td>DE</td>
<td>num</td>
<td>..3</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>4</td>
<td>Bezugssegment</td>
<td>DE</td>
<td>num</td>
<td>..3</td>
<td>C</td>
<td>1</td>
<td>&gt;=1<br>O: Verwendung in Kre- ditinstitutsnachricht N: Verwendung in Kun- dennachricht</td>
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


# Segmentnummer

Information zur eindeutigen Identifizierung eines Segments innerhalb einer
Nachricht. Die Segmente einer Nachricht werden in Einerschritten streng
monoton aufsteigend nummeriert. Die Nummerierung beginnt mit 1 im ersten
Segment der Nachricht (Nachrichtenkopf).

<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: D</td>
<td>Version: 3.0 - Final Version</td>
<td>Financial Transaction Services (FinTS) Dokument: Security - Sicherheitsverfahren HBCI</td>
</tr>
<tr>
<td>Seite:<br>172</td>
<td>Stand:<br>18.07.2013</td>
<td>Kapitel: Data Dictionary<br>Abschnitt:<br>Buchstabe S</td>
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


# Segmentversion

Versionsnummer zur Dokumentation von Änderungen eines Segmentfor-
mats.

Die Segmentversion von administrativen Segmenten (die Segmentart 'Admi-
nistration' bzw. 'Geschäftsvorfall' ist bei jeder Segmentbeschreibung ange-
geben) wird bei jeder Änderung des Segmentformats inkrementiert.

Bei Geschäftsvorfallssegmenten wird die Segmentversion auf logischer Ebe-
ne verwaltet, d.h. sie ist für das Auftrags-, das Antwort- und das Parame-
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


# Sicherheitsdatum und -uhrzeit

Zeitstempel, beispielsweise Datum und Uhrzeit des lokalen Rechners, an
dem die elektronische Unterschrift geleistet wurde, sowie die Bedeutung des
Zeitstempels.


<table>
<tr>
<th>Nr.</th>
<th>Name</th>
<th>Typ</th>
<th>For- mat</th>
<th>Län- ge</th>
<th>Sta- tus</th>
<th>An- zahl</th>
<th>Restriktionen</th>
</tr>
<tr>
<td>1</td>
<td>Datum- und Zeitbe- zeichner, kodiert</td>
<td>DE</td>
<td>code</td>
<td>..3</td>
<td>M</td>
<td>1</td>
<td>1,6</td>
</tr>
<tr>
<td>2</td>
<td>Datum</td>
<td>DE</td>
<td>dat</td>
<td>#</td>
<td>O</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>3</td>
<td>Uhrzeit</td>
<td>DE</td>
<td>tim</td>
<td>#</td>
<td>C</td>
<td>1</td>
<td>O: ,Datum' belegt N: sonst</td>
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


<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th>Version:</th>
<th>Kapitel:</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Security - Sicherheitsverfahren HBCI</td>
<td>3.0 - Final Version</td>
<td>D</td>
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
<td>18.07.2013</td>
<td>173</td>
</tr>
</table>


## Sicherheitsfunktion, kodiert

Bis HBCI 2.2 war die Sicherheitsfunktion die Unterscheidung zwischen DDV
und RDH, wobei die 1 nur das RDH-Verfahren kennzeichnete und 2 das
DDV-Verfahren. Ab FinTS 3.0 existieren beim RDH-Verfahren drei Schlüssel
(DS-Schlüssel für Non-Repudiation, Signierschlüssel für Authentication und
Chiffrierschlüssel für Verschlüsselung) und somit auch drei Sicherheitsfunk-
tionen (Sicherheitsfunktion 1 bei Verwendung des DS-Schlüssels, Sicher-
heitsfunktion 2 bei Verwendung des Signierschlüssel und Sicherheitsfunktion
4 bei Verwendung des Chiffrierschlüssels) beim RAH- und RDH-Verfahren.

Die Sicherheitsfunktion hat ab FinTS 3.0 lediglich informatorischen Wert, da
die eigentliche Steuerung über die Sicherheitsprofile und -Klassen erfolgt.

Kodierte Information über die Sicherheitsfunktion, die auf die Nachricht an-
gewendet wird.

Codierung:

1: Non-Repudiation of Origin, für RAH, RDH (NRO)

2: Message Origin Authentication, für RAH, RDH und DDV (AUT)

4: Encryption, Verschlüsselung und evtl. Komprimierung (ENC)


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


## Sicherheitsidentifikation, Details

Identifikation der im Sicherheitsprozess involvierten Parteien. Dient zur
Übermittlung der CID bei kartenbasierten Sicherheitsverfahren bzw. der
Kundensystem-ID bei softwarebasierten Verfahren (z.B. Speicherung der
Schlüssel in einer Schlüsseldatei).


<table>
<tr>
<th>Nr.</th>
<th>Name</th>
<th>Typ</th>
<th>For- mat</th>
<th>Län- ge</th>
<th>Sta- tus</th>
<th>An- zahl</th>
<th>Restriktionen</th>
</tr>
<tr>
<td>1</td>
<td>Bezeichner für Si- cherheitspartei</td>
<td>DE</td>
<td>code</td>
<td>..3</td>
<td>M</td>
<td>1</td>
<td>1, 2</td>
</tr>
<tr>
<td>2</td>
<td>CID</td>
<td>DE</td>
<td>bin</td>
<td>.256</td>
<td>C</td>
<td>1</td>
<td>M: Sicherheitsmedium = Chipkarte N: sonst</td>
</tr>
<tr>
<td>3</td>
<td>Identifizierung der Partei</td>
<td>DE</td>
<td>id</td>
<td>#</td>
<td>C</td>
<td>1</td>
<td>M: Sicherheitsmedium = Software N: sonst</td>
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


### Sicherheitskontrollreferenz

Referenzinformation, mit der die Verbindung zwischen Signaturkopf und da-
zu gehörigem Signaturabschluss hergestellt werden kann. Die Sicherheits-
kontrollreferenz im Signaturkopf muss mit der entsprechenden Information
im Signaturabschluss übereinstimmen.

<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: D</td>
<td>Version: 3.0 - Final Version</td>
<td>Financial Transaction Services (FinTS) Dokument: Security - Sicherheitsverfahren HBCI</td>
</tr>
<tr>
<td>Seite:<br>174</td>
<td>Stand:<br>18.07.2013</td>
<td>Kapitel: Data Dictionary<br>Abschnitt:<br>Buchstabe S</td>
</tr>
</table>


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
<td>. . 14</td>
</tr>
<tr>
<td>Version:</td>
<td>1</td>
</tr>
</table>


#### Sicherheitsprofil

Verfahren zur Absicherung der Transaktionen, das zwischen Kunde und
Kreditinstitut vereinbar wurde. Das Sicherheitsprofil wird anhand der Kombi-
nation der beiden Elemente ,,Sicherheitsverfahren“ und ,,Version" bestimmt
(z._B. RDH-3, DDV-1). Für das Sicherheitsverfahren PINTAN ist als Code der
Wert PIN und als Version der Wert 1 einzustellen.


<table>
<tr>
<th>Nr.</th>
<th>Name</th>
<th>Typ</th>
<th>For- mat</th>
<th>Län- ge</th>
<th>Sta- tus</th>
<th>An- zahl</th>
<th>Restriktionen</th>
</tr>
<tr>
<td>1</td>
<td>Sicherheitsverfahren, Code</td>
<td>DE</td>
<td>code</td>
<td>3</td>
<td>M</td>
<td>1</td>
<td>DDV, RAH, RDH, PIN</td>
</tr>
<tr>
<td>2</td>
<td>Version des Sicher- heitsverfahrens</td>
<td>DE</td>
<td>num</td>
<td>..3</td>
<td>M</td>
<td>1</td>
<td>1, 2, 3, 4, 5, 6, 7, 8, 9, 10</td>
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


#### Sicherheitsreferenznummer

Sicherheitsrelevante Nachrichtenidentifikation (Signatur-ID), welche zur Ver-
hinderung der Doppeleinreichung, respektive Garantie der Nachrichtense-
quenzintegrität eingesetzt werden kann.

Bei chipkartenbasierten Verfahren ist der Sequenzzähler der Chipkarte ein-
zustellen. Dies ist bei Typ-1 Karten der Wert ,,EF_SEQ" in der Application
DF_BANKING und bei SECCOS Bankensignaturkarten der Wert „usage
counter“ der beiden Signierschlüssel SK.CH.DS und SK.CH.AUT.

Bei softwarebasierten Verfahren wird die Sicherheitsreferenznummer auf
Basis des DE Kundensystem-ID und des DE Benutzerkennung der DEG
Schlüsselnamen verwaltet.


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


##### Sicherheitsverfahren, Code

Code des unterstützten Signatur- bzw. Verschlüsselungsalgorithmus.

Weitere Informationen zu den Verfahren sind Kapitel B.1 zu entnehmen.

Codierung:

DDV: DES-DES-Verfahren

RAH: RSA-AES-Hybridverfahren

RDH: RSA-DES-Hybridverfahren

PIN: PIN/TAN-Verfahren

EMV: EMV-AC-Variante (S-Fkt=820, 821) bei AZS-Verfahren

<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th>Version:</th>
<th>Kapitel:</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Security - Sicherheitsverfahren HBCI</td>
<td>3.0 - Final Version</td>
<td>D</td>
</tr>
<tr>
<td>Kapitel:</td>
<td>Data Dictionary</td>
<td>Stand:</td>
<td>Seite:</td>
</tr>
<tr>
<td>Abschnitt:</td>
<td>Buchstabe U</td>
<td>18.07.2013</td>
<td>175</td>
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
<td>3</td>
</tr>
<tr>
<td>Version:</td>
<td>3</td>
</tr>
</table>


###### Signaturalgorithmus

Angaben zum kryptographischen Algorithmus, zu seinem Operationsmodus,
so wie zu dessen Einsatz, in diesem Fall für die Signaturbildung über DDV
bzw. RAH / RDH.


<table>
<tr>
<th>Nr.</th>
<th>Name</th>
<th>Typ</th>
<th>For- mat</th>
<th>Län- ge</th>
<th>Sta- tus</th>
<th>An- zahl</th>
<th>Restriktionen</th>
</tr>
<tr>
<td>1</td>
<td>Verwendung des Signaturalgorithmus, kodiert</td>
<td>DE</td>
<td>code</td>
<td>..3</td>
<td>M</td>
<td>1</td>
<td>6</td>
</tr>
<tr>
<td>2</td>
<td>Signaturalgorithmus, kodiert</td>
<td>DE</td>
<td>code</td>
<td>..3</td>
<td>M</td>
<td>1</td>
<td>1,10</td>
</tr>
<tr>
<td>3</td>
<td>Operationsmodus, kodiert</td>
<td>DE</td>
<td>code</td>
<td>..3</td>
<td>M</td>
<td>1</td>
<td>16, 17, 18, 19, 999</td>
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


####### Signaturalgorithmus, kodiert

Kodierte Information über den Signaturalgorithmus.

Codierung:

1: DES-Algorithmus (bei DDV)

10: RSA-Algorithmus (bei RAH und RDH)

Typ:

DE

Format:

code

Länge:

..3

Version:

2


####### Sperrenkennzeichen

Information zur Begründung der Sperrung.

Codierung:

1:
Schlüssel des Zertifikatseigentümers kompromittiert

501: Zertifikat ungültig wegen Verdacht auf Kompromittierung

999: gesperrt aus sonstigen Gründen

<!-- PageBreak -->


<table>
<tr>
<td>Kapitel:</td>
<td>Version:</td>
<td>Financial Transaction Services (FinTS)</td>
</tr>
<tr>
<td>D</td>
<td>3.0 - Final Version</td>
<td>Dokument: Security - Sicherheitsverfahren HBCI</td>
</tr>
<tr>
<td>Seite:</td>
<td>Stand:</td>
<td>Kapitel: Data Dictionary</td>
</tr>
<tr>
<td>176</td>
<td>18.07.2013</td>
<td>Abschnitt:<br>Buchstabe U</td>
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


U


######## Uhrzeit

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


V


######### Validierungsresultat

Elektronische Signatur, die zur Validierung berechnet wurde.


<table>
<tr>
<td>Typ:</td>
<td>DE</td>
</tr>
<tr>
<td>Format:</td>
<td>bin</td>
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


######### Verfahren Benutzer

Information über das Benutzer-Verfahren, die beim öffentlichen Schlüssel
angegeben wird.

Es ist nur der folgende Wert zugelassen:

10: RSA-Verfahren


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


######### Verschlüsselungsalgorithmus

Angaben zum kryptographischen Algorithmus, zu seinem Operationsmodus,
so wie zu dessen Einsatz, in diesem Fall für die Nachrichtenverschlüsselung.

<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th>Version:</th>
<th>Kapitel:</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Security - Sicherheitsverfahren HBCI</td>
<td>3.0 - Final Version</td>
<td>D</td>
</tr>
<tr>
<td>Kapitel:</td>
<td>Data Dictionary</td>
<td>Stand:</td>
<td>Seite:</td>
</tr>
<tr>
<td>Abschnitt:</td>
<td>Buchstabe V</td>
<td>18.07.2013</td>
<td>177</td>
</tr>
</table>


<table>
<tr>
<th>Nr.</th>
<th>Name</th>
<th>Typ</th>
<th>For- mat</th>
<th>Län- ge</th>
<th>Sta- tus</th>
<th>An- zahl</th>
<th>Restriktionen</th>
</tr>
<tr>
<td>1</td>
<td>Verwendung des Verschlüsselungs- algorithmus, kodiert</td>
<td>DE</td>
<td>code</td>
<td>..3</td>
<td>M</td>
<td>1</td>
<td>2</td>
</tr>
<tr>
<td>2</td>
<td>Operationsmodus, kodiert</td>
<td>DE</td>
<td>code</td>
<td>..3</td>
<td>M</td>
<td>1</td>
<td>2, 16, 17, 18, 19</td>
</tr>
<tr>
<td>3</td>
<td>Verschlüsselungs- algorithmus, kodiert</td>
<td>DE</td>
<td>code</td>
<td>..3</td>
<td>M</td>
<td>1</td>
<td>13</td>
</tr>
<tr>
<td>4</td>
<td>Wert des Algorith- musparameters, Schlüssel</td>
<td>DE</td>
<td>bin</td>
<td>..512</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>5</td>
<td>Bezeichner für Algo- rithmusparameter, Schlüssel</td>
<td>DE</td>
<td>code</td>
<td>..3</td>
<td>M</td>
<td>1</td>
<td>5,6</td>
</tr>
<tr>
<td>6</td>
<td>Bezeichner für Algo- rithmusparameter, IV</td>
<td>DE</td>
<td>code</td>
<td>..3</td>
<td>M</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td>7</td>
<td>Wert des Algorith- musparameters, IV</td>
<td>DE</td>
<td>bin</td>
<td>..512</td>
<td>O</td>
<td>1</td>
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


######## Verschlüsselungsalgorithmus, kodiert

Kodierte Information über den verwendeten Verschlüsselungsalgorithmus.

Codierung:

13: 2-Key-Triple-DES

14: AES-256 [AES]


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
<td>3</td>
</tr>
</table>


######### Version der Filterfunktion

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


######### Version des Sicherheitsverfahrens

Version des unterstützten Sicherheitsverfahrens (s. „Sicherheitsverfahren,
Code“).

In Kombination mit dem Sicherheitsverfahren RAH sind die folgenden Versi-
onen gültig:

<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: D</td>
<td>Version: 3.0 - Final Version</td>
<td>Financial Transaction Services (FinTS) Dokument: Security - Sicherheitsverfahren HBCI</td>
</tr>
<tr>
<td>Seite:</td>
<td rowspan="2">Stand:<br>18.07.2013</td>
<td>Kapitel: Data Dictionary</td>
</tr>
<tr>
<td>178</td>
<td>Abschnitt:<br>Buchstabe V</td>
</tr>
</table>


<table>
<tr>
<th>Ver- sion</th>
<th>Signatur- verfahren</th>
<th>Schlüssellänge<br>(bit)</th>
<th>Hashverfahren</th>
<th>Schlüsselart*</th>
</tr>
<tr>
<td>7</td>
<td>PKCS#1 PSS</td>
<td>gemäß [DK Krypto]</td>
<td>SHA-256</td>
<td>D, S, V</td>
</tr>
<tr>
<td>9</td>
<td>PKCS#1 PSS</td>
<td>gemäß [DK Krypto]</td>
<td>SHA-256</td>
<td>S, V</td>
</tr>
<tr>
<td>10</td>
<td>PKCS#1 PSS</td>
<td>gemäß [DK Krypto]</td>
<td>SHA-256</td>
<td>S, V</td>
</tr>
</table>


In Kombination mit dem Sicherheitsverfahren RDH sind die folgenden Versi-
onen gültig:


<table>
<tr>
<th>Ver- sion</th>
<th>Signatur- verfahren</th>
<th>Schlüssellänge (bit)</th>
<th>Hashverfahren</th>
<th>Schlüsselart*</th>
</tr>
<tr>
<td>1</td>
<td>ISO 9796-1</td>
<td>708-768</td>
<td>RIPEMD-160</td>
<td>S, V</td>
</tr>
<tr>
<td>2</td>
<td>DIN, ISO 9796-2</td>
<td>1024-2048</td>
<td>RIPEMD-160</td>
<td>S, V</td>
</tr>
<tr>
<td>3</td>
<td>DIN, ISO 9796-2 PKCS#1 V1.5</td>
<td>1024-2048</td>
<td>RIPEMD-160 SHA-1</td>
<td>D, S, V</td>
</tr>
<tr>
<td>4</td>
<td>PKCS#1 V1.5</td>
<td>1024-2048</td>
<td>SHA-1</td>
<td>D, S, V</td>
</tr>
<tr>
<td>5</td>
<td>PKCS#1 V1.5</td>
<td>1024-2048</td>
<td>SHA-1</td>
<td>S,V</td>
</tr>
<tr>
<td>6</td>
<td>PKCS#1 V1.5</td>
<td>gemäß [DK Krypto]</td>
<td>SHA-256</td>
<td>D, S, V</td>
</tr>
<tr>
<td>7</td>
<td>PKCS#1 PSS</td>
<td>gemäß [DK Krypto]</td>
<td>SHA-256</td>
<td>D, S, V</td>
</tr>
<tr>
<td>8</td>
<td>PKCS#1 V1.5</td>
<td>gemäß [DK Krypto]</td>
<td>SHA-256</td>
<td>S, V</td>
</tr>
<tr>
<td>9</td>
<td>PKCS#1 PSS</td>
<td>gemäß [DK Krypto]</td>
<td>SHA-256</td>
<td>S, V</td>
</tr>
<tr>
<td>10</td>
<td>PKCS#1 PSS</td>
<td>gemäß [DK Krypto]</td>
<td>SHA-256</td>
<td>S, V</td>
</tr>
</table>


In Kombination mit dem Sicherheitsverfahren DDV sind die folgenden Versi-
onen gültig:


<table>
<tr>
<th>Ver- sion</th>
<th>Signatur- verfahren</th>
<th>Schlüssellänge (bit)</th>
<th>Hashverfahren</th>
<th>Schlüsselart*</th>
</tr>
<tr>
<td>1</td>
<td>MAC</td>
<td>128</td>
<td>RIPEMD-160</td>
<td>S, V</td>
</tr>
<tr>
<td>2</td>
<td>MAC</td>
<td>128</td>
<td>SHA-256</td>
<td>S, V</td>
</tr>
</table>


\* s. Element „Schlüsselart“

Andere als die genannten Profile sind nicht zulässig.


![](figures/192.1)


Um Multibankfähigkeit zu gewährleisten, ist die Unterstüt-
zung eines der Verfahren RAH-9 bzw. übergangsweise
RDH-9 kunden- und kreditinstitutsseitig verpflichtend.


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


###### Verwendung des Hashalgorithmus, kodiert

Kodierte Information über die Verwendung des Hashalgorithmus.

Im Zusammenhang mit Hash-Funktionen ist derzeit nur folgender Wert mög-
lich:

<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th>Version:</th>
<th>Kapitel:</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Security - Sicherheitsverfahren HBCI</td>
<td>3.0 - Final Version</td>
<td>D</td>
</tr>
<tr>
<td>Kapitel:</td>
<td>Data Dictionary</td>
<td>Stand:</td>
<td>Seite:</td>
</tr>
<tr>
<td>Abschnitt:</td>
<td>Buchstabe V</td>
<td>18.07.2013</td>
<td>179</td>
</tr>
</table>


###### Codierung:

1: Owner Hashing (OHA)


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


####### Verwendung des Signaturalgorithmus, kodiert

Kodierte Information über die Verwendung des Signaturalgorithmus.

Im Zusammenhang mit Signaturbildung ist derzeit nur folgender Wert mög-
lich:

Codierung:

6: Owner Signing (OSG)


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


####### Verwendung des Verschlüsselungsalgorithmus, kodiert

Kodierte Information über die Verwendung des Verschlüsselungs-
algorithmus.

Im Zusammenhang mit der Verschlüsselung sind derzeit folgende Werte
möglich:

Codierung:

2: Owner Symmetric (OSY)


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


<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: D</td>
<td>Version: 3.0 - Final Version</td>
<td>Financial Transaction Services (FinTS) Dokument: Security - Sicherheitsverfahren HBCI</td>
</tr>
<tr>
<td>Seite:<br>180</td>
<td>Stand:<br>18.07.2013</td>
<td>Kapitel: Data Dictionary<br>Abschnitt: Buchstabe W</td>
</tr>
</table>


# Verwendungszweck für öffentlichen Schlüssel

Kodierte Information über die Verwendung des öffentlichen Schlüssels. Die-
se Information muss konsistent zur Schlüsselart gehalten werden.

Codierung:

5: Owner Ciphering (Chiffrierschlüssel)

6: Owner Signing (Signierschlüssel)


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


W


# Wert des Algorithmusparameters, IV

Initialisierungswert für den kryptographischen Algorithmusparameter. Zur
Zeit ist die Angabe eines Wertes nicht zulässig; es wird dafür folgender Initia-
lisierungswert als Default verwendet: X'00 00 00 00 00 00 00 00'

In einer zukünftigen Version kann ein abweichender Initialisierungswert defi-
niert werden.


<table>
<tr>
<td>Typ:</td>
<td>DE</td>
</tr>
<tr>
<td>Format:</td>
<td>bin</td>
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


# Wert des Algorithmusparameters, Schlüssel

Verschlüsselter Nachrichtenschlüssel für den kryptographischen Algorith-
musparameter.


<table>
<tr>
<td>Typ:</td>
<td>DE</td>
</tr>
<tr>
<td>Format:</td>
<td>bin</td>
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


# Wert des Hashalgorithmusparameters

Initialisierungswert für den Hashalgorithmusparameter. Zur Zeit ist die Anga-
be eines Wertes nicht zulässig; es wird für RIPEMD-160 folgender Initialisie-
rungswert als Default verwendet:

X'01 23 45 67 89 AB CD EF FE DC BA 98 76 54 32 10 F0 E1 D2 C3' (Little-
Endian-Notation)

In einer zukünftigen Version kann ein abweichender Initialisierungswert defi-
niert werden.


<table>
<tr>
<td>Typ:</td>
<td>DE</td>
</tr>
<tr>
<td>Format:</td>
<td>bin</td>
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


# Wert für Exponent

Exponent des öffentlichen Schlüssels (z.Zt. 65537). Die Kürzung um führen-
de 0-Bytes ist empfehlenswert, aber nicht verbindlich.

<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th>Version:</th>
<th>Kapitel:</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Security - Sicherheitsverfahren HBCI</td>
<td>3.0 - Final Version</td>
<td>D</td>
</tr>
<tr>
<td>Kapitel:</td>
<td>Data Dictionary</td>
<td>Stand:</td>
<td>Seite:</td>
</tr>
<tr>
<td>Abschnitt:</td>
<td>Buchstabe Z</td>
<td>18.07.2013</td>
<td>181</td>
</tr>
</table>


<table>
<tr>
<td>Typ:</td>
<td>DE</td>
</tr>
<tr>
<td>Format:</td>
<td>bin</td>
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


## Wert für Modulus

Modulus des öffentlichen Schlüssels. Die Kürzung um führende 0-Bytes ist
empfehlenswert, aber nicht verbindlich.


<table>
<tr>
<td>Typ:</td>
<td>DE</td>
</tr>
<tr>
<td>Format:</td>
<td>bin</td>
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


Z


## Zertifikat

Zertifikat eines öffentlichen Schlüssels.

Da Zertifikate Informationen beinhalten, die auch in den HBCI-Formaten ent-
halten sind (z.B. Zertifikatsreferenz respektive Schlüsselnamen), können Da-
ten redundant vorkommen. Diese müssen dann auf Konsistenz überprüft
werden. Bei Unstimmigkeiten hat das Zertifikat Vorrang.


<table>
<tr>
<th>Nr.</th>
<th>Name</th>
<th>Typ</th>
<th>For- mat</th>
<th>Län- ge</th>
<th>Sta- tus</th>
<th>An- zahl</th>
<th>Restriktionen</th>
</tr>
<tr>
<td>1</td>
<td>Zertifikatstyp</td>
<td>DE</td>
<td>code</td>
<td>1</td>
<td>M</td>
<td>1</td>
<td>1, 2, 3</td>
</tr>
<tr>
<td>2</td>
<td>Zertifikatsinhalt</td>
<td>DE</td>
<td>bin</td>
<td>٠٠<br>4096</td>
<td>M</td>
<td>1</td>
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


### Zertifikatsinhalt

Transparenter Inhalt eines Zertifikats.

Bei der Bankensignaturkarte handelt es sich hier um

\- das Signaturzertifikat C_X509.CH.DS,

\- das CSA-(KE-)Zertifikat C_X509.CH.AUTC/S[&KE]

\- und das KE-Zertifikat C_X509.CH.KE


<table>
<tr>
<td>Typ:</td>
<td>DE</td>
</tr>
<tr>
<td>Format:</td>
<td>bin</td>
</tr>
<tr>
<td>Länge:</td>
<td>..4096</td>
</tr>
<tr>
<td>Version:</td>
<td>1</td>
</tr>
</table>


<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: D</td>
<td>Version: 3.0 - Final Version</td>
<td>Financial Transaction Services (FinTS) Dokument: Security - Sicherheitsverfahren HBCI</td>
</tr>
<tr>
<td>Seite:<br>182</td>
<td>Stand: 18.07.2013</td>
<td>Kapitel: Data Dictionary<br>Abschnitt:<br>Buchstabe Z</td>
</tr>
</table>


## Zertifikatstyp

Information über Aufbau und Inhalt eines Zertifikats.

Codierung:

1: ZKA

2: UN/EDIFACT

3: X.509 v3 (gemäß [ISIS/MTT])


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


<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th>Version:</th>
<th>Kapitel:</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Security - Sicherheitsverfahren HBCI</td>
<td>3.0 - Final Version</td>
<td>E</td>
</tr>
<tr>
<td>Kapitel:</td>
<td>Anlagen</td>
<td>Stand:</td>
<td>Seite:</td>
</tr>
<tr>
<td>Abschnitt:</td>
<td>Übersicht der Segmente</td>
<td>18.07.2013</td>
<td>183</td>
</tr>
</table>


### E. ANLAGEN


#### E.1 Übersicht der Segmente


<table>
<tr>
<th>Nr.</th>
<th>Segmentname</th>
<th>Kennung</th>
<th>Sen- der1</th>
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
<td>Bestätigung der Schlüsselsperrung</td>
<td>HISSP</td>
<td>I</td>
<td>3</td>
</tr>
<tr>
<td>3</td>
<td>Schlüsseländerung</td>
<td>HKSAK</td>
<td>K</td>
<td>3</td>
</tr>
<tr>
<td>4</td>
<td>Schlüsselsperrung</td>
<td>HKSSP</td>
<td>K</td>
<td>3</td>
</tr>
<tr>
<td>5</td>
<td>Signaturkopf</td>
<td>HNSHK</td>
<td>K/I</td>
<td>4</td>
</tr>
<tr>
<td>6</td>
<td>Übermittlung eines öffentlichen Schlüssels</td>
<td>HIISA</td>
<td>I</td>
<td>3</td>
</tr>
<tr>
<td>7</td>
<td>Verschlüsselte Daten</td>
<td>HNVSD</td>
<td>K/I</td>
<td>1</td>
</tr>
<tr>
<td>8</td>
<td>Verschlüsselungskopf</td>
<td>HNVSK</td>
<td>K/I</td>
<td>3</td>
</tr>
</table>


<!-- PageFooter: 1 K: Kunde, I: Kreditinstitut -->
