<!-- PageHeader: Bundesverband der Deutschen Volksbanken und Raiffeisenbanken e. V. Bundesverband deutscher Banken e. V. Bundesverband Öffentlicher Banken Deutschlands e. V. Deutscher Sparkassen- und Giroverband e. V. Verband deutscher Pfandbriefbanken e. V. -->
<!-- PageHeader: Die Deutsche Kreditwirtschaft -->


# FinTS Financial Transaction Services

Schnittstellenspezifikation

Sicherheitsverfahren PIN/TAN

Herausgeber:

Bundesverband deutscher Banken e.V., Berlin

Deutscher Sparkassen- und Giroverband e.V., Bonn/Berlin

Bundesverband der Deutschen Volksbanken und Raiffeisenbanken e.V., Berlin

Bundesverband Öffentlicher Banken Deutschlands e.V., Berlin

<!-- PageFooter: Version: 3.0-FV -->
<!-- PageFooter: Stand: 23.02.2018 -->
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

Dieses Dokument kann im Internet abgerufen werden unter https://www.fints.org.

<!-- PageBreak -->

<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th rowspan="2">Version: 3.0-FV</th>
<th rowspan="2">Kapitel: A</th>
</tr>
<tr>
<th>Dokument:</th>
<th>Security - Sicherheitsverfahren PIN/TAN</th>
</tr>
<tr>
<td>Kapitel:</td>
<td>Einleitung</td>
<td>Stand: 23.02.2018</td>
<td>Seite: 5</td>
</tr>
</table>


## Versionsführung

Das vorliegende Dokument wurde von folgenden Personen erstellt bzw. geändert:


<table>
<tr>
<th>Name</th>
<th>Organi- sation</th>
<th>Datum</th>
<th>Version</th>
<th>Dokumente</th>
<th>Anmerkungen</th>
</tr>
<tr>
<td></td>
<td>SIZ</td>
<td>22.06.2004</td>
<td>3.0 Final Version</td>
<td>FinTS_3.0_PINTAN.doc</td>
<td></td>
</tr>
<tr>
<td>Haubner</td>
<td>für SIZ</td>
<td>27.10.2010</td>
<td>3.0 Final Version</td>
<td>FinTS_3.0_PINTAN_20 10-10-27_FV.docx</td>
<td></td>
</tr>
<tr>
<td>Haubner</td>
<td>für SIZ</td>
<td>06.10.2017</td>
<td>3.0 Final Version</td>
<td>FinTS_3.0_PINTAN_20 17-10- 06_final_version.docx</td>
<td></td>
</tr>
<tr>
<td>Haubner</td>
<td>für SIZ</td>
<td>23.02.2018</td>
<td>3.0 Final Version</td>
<td>FinTS_3.0_PINTAN_20 18-02- 23_final_version.docx</td>
<td></td>
</tr>
</table>


Grau dargestellte Spezifikationsteile sind aus Sicht der Spezifikation obsolet, kön-
nen aber aus Migrationsgründen noch verwendet werden. Die Entscheidung hier-
über ist institutsspezifisch.


## Änderungen gegenüber der Vorversion

Änderungen zur Vorversion sind im Dokument durch einen Randbalken markiert.
Falls sich die Kapitelnummerierung geändert hat, bezieht sich die Kapitelangabe auf
die neue Nummerierung.


### Releasedatum 27.10.2010


<table>
<tr>
<th>lfd. Nr.</th>
<th>Kapitel</th>
<th>Kapitel- nummer</th>
<th>Ken- nung 1</th>
<th>Art2</th>
<th>Beschreibung</th>
</tr>
<tr>
<td>1</td>
<td>GV HKTAN</td>
<td>B.4</td>
<td></td>
<td>E</td>
<td>Segmentversionen #3 und #5</td>
</tr>
<tr>
<td>2</td>
<td>Management chip- TAN und mobi- leTAN</td>
<td>C.3</td>
<td></td>
<td>E</td>
<td>Erweiterungen im Management von chipTAN und mobileTAN</td>
</tr>
</table>


### Releasedatum 11.05.2017


<table>
<tr>
<td>lfd. Nr.</td>
<td>Kapitel</td>
<td>Kapitel- nummer</td>
<td>Ken- nung</td>
<td>Art</td>
<td>Beschreibung</td>
</tr>
</table>


<!-- PageFooter: 1 nur zur internen Zuordnung -->
<!-- PageFooter: 2 F = Fehler; Ä = Änderung; K = Klarstellung; E = Erweiterung -->
<!-- PageBreak -->


<table>
<tr>
<th>Kapitel:</th>
<th>Version: 3.0-FV</th>
<th>Financial Transaction Services (FinTS) Dokument: Security - Sicherheitsverfahren PIN/TAN</th>
</tr>
<tr>
<td>Seite: 6</td>
<td>Stand: 23.02.2018</td>
<td>Kapitel: Einleitung</td>
</tr>
</table>


<table>
<tr>
<th>lfd. Nr.</th>
<th>Kapitel</th>
<th>Kapitel- nummer</th>
<th>Ken- nung</th>
<th>Art</th>
<th>Beschreibung</th>
</tr>
<tr>
<td>1</td>
<td>Management TAN- Medien</td>
<td>C.3</td>
<td>0475</td>
<td>E</td>
<td>Erweiterungen bei den folgenden GVs für bilateral vereinbarte Sicherheitsver- fahren im Element ,,TAN-Medium- Klasse“:<br>- HKTAB #5<br>- HKTAU #3<br>- HKMTR #3<br>- HKMTF #3<br>- HKMTA #3<br>- HKTML #2</td>
</tr>
<tr>
<td>2</td>
<td>Starke Authentifi- zierung</td>
<td>B.3.3</td>
<td>0480</td>
<td>E</td>
<td>Abläufe zur starken Authentifizierung während der Dialoginitialisierung</td>
</tr>
<tr>
<td>3</td>
<td>Geschäftsvorfall HKTAN#6</td>
<td>B.4.1</td>
<td>0480</td>
<td>E</td>
<td>Neue HKTAN-Segmentversion #6 zur Unterstützung der starken Kun- denauthentifizierung während der Dialo- ginitialisierung und der Unterstützung der HHD_UC-Antwort bei bidirektionalen chipTAN-Lesern.</td>
</tr>
<tr>
<td>4</td>
<td>Bankensignatur</td>
<td>Diverse</td>
<td>0480</td>
<td>Ä</td>
<td>Die optionale Bankensignatur wird von keinem Kreditinstitut mehr verwendet und wurde daher komplett aus der Spe- zifikation entfernt. Dies bedeutet syntak- tisch, dass die Segmente ,,Signaturkopf“ und ,,Signaturabschluss" erhalten blei- ben, aber nicht mehr mit einer Banken- signatur belegt werden dürfen.</td>
</tr>
<tr>
<td>5</td>
<td>TAN- Listenverfahren</td>
<td>Diverse</td>
<td>0480</td>
<td>Ä</td>
<td>TAN-Listenverfahren (TAN-/iTAN-Liste) wurden aus der Spezifikation entfernt. Dies betrifft die aktuellen Segmentversi- onen. In den älteren Segmentversionen sind die Elemente zu TAN-Listen aus Kompatibilitätsgründen noch enthalten. Betroffen Elemente wurden farblich ge- kennzeichnet.</td>
</tr>
<tr>
<td>6</td>
<td>Archiv in Abschnitt E</td>
<td>Diverse</td>
<td>0480</td>
<td>Ä</td>
<td>Ältere Segmentversionen wurden in den Abschnitt E „Archiv: Ältere Segmentver- sionen" verlagert.</td>
</tr>
</table>


### Releasedatum 06.10.2017


<table>
<tr>
<th>lfd. Nr.</th>
<th>Kapitel</th>
<th>Kapitel- nummer</th>
<th>Ken- nung</th>
<th>Art</th>
<th>Beschreibung</th>
</tr>
<tr>
<td>1</td>
<td>Starke Kun- denauthentifizie- rung</td>
<td>B.3</td>
<td>0496</td>
<td>E</td>
<td>Neues Einleitungskapitel zur SCA</td>
</tr>
<tr>
<td>2</td>
<td>Rahmenbedingun- gen SCA</td>
<td>B.4.3.1</td>
<td>0496</td>
<td>Ä</td>
<td>Diverse Konkretisierungen und Fehler- behebungen bei den Rahmenbedingun- gen zur starken Kundenauthentifizierung</td>
</tr>
<tr>
<td>3</td>
<td>HITAN</td>
<td>B.5.1b</td>
<td>0496</td>
<td></td>
<td>Ergänzen FinTS-Füllwert bei Auftragsre- ferenz und Challenge für Dummy-HITAN</td>
</tr>
<tr>
<td>4</td>
<td>PIN/TAN- Management</td>
<td>C</td>
<td>0496</td>
<td>Ä</td>
<td>Klarstellung zur Isolation von PIN/TAN- Management-Geschäftsvorfällen</td>
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
<th>Security - Sicherheitsverfahren PIN/TAN</th>
</tr>
<tr>
<td>Kapitel:</td>
<td>Einleitung</td>
<td>Stand: 23.02.2018</td>
<td>Seite: 7</td>
</tr>
</table>


<table>
<tr>
<th>lfd. Nr.</th>
<th>Kapitel</th>
<th>Kapitel- nummer</th>
<th>Ken- nung</th>
<th>Art</th>
<th>Beschreibung</th>
</tr>
<tr>
<td>5</td>
<td>PIN-Änderung</td>
<td>C.1.1</td>
<td>0496</td>
<td>Ä</td>
<td>Anpassung an die starke Kundenauthen- tifizierung bzgl. des obligatorischen Ver- wendens einer TAN bei SCA.</td>
</tr>
</table>


### Releasedatum 23.02.2018


<table>
<tr>
<th>lfd. Nr.</th>
<th>Kapitel</th>
<th>Kapitel- nummer</th>
<th>Ken- nung</th>
<th>Art</th>
<th>Beschreibung</th>
</tr>
<tr>
<td>1</td>
<td>Starke Authentifi- zierung</td>
<td>B.4.3</td>
<td>0496</td>
<td>Ä</td>
<td>Allgemeine Anpassungen und Fehlerkor- rekturen in den Abläufen zu Prozessva- riante 1 und 2.<br>Speziell:<br>- Festlegung von fest definierten FinTS- Füllwerten<br>- Entfernen der festgelegten Bezugs- segmente in den Abläufen</td>
</tr>
<tr>
<td>2</td>
<td>Starke Kun- denauthentifizie- rung</td>
<td>B.3</td>
<td>0496</td>
<td>E</td>
<td>Verständlichere Darstellung der Auth- Klasse 2</td>
</tr>
<tr>
<td>3</td>
<td>Rahmenbedingun- gen</td>
<td>B.4.3.1</td>
<td>0496</td>
<td>E</td>
<td>Klarstellung, dass die Verwendung von 2 BPDs bei anonymen Dialogen nicht ver- pflichtend ist.</td>
</tr>
<tr>
<td>4</td>
<td>Data Dicitionary</td>
<td>D - M</td>
<td>0496</td>
<td>E</td>
<td>Klarstellung, dass der Parameter „Mehr als ein TAN-pflichtiger Auftrag pro Nach- richt erlaubt" = ,J" mit PSD2 nicht mehr zulässig ist.</td>
</tr>
</table>


<!-- PageBreak -->


<table>
<tr>
<th>Kapitel:</th>
<th>Version: 3.0-FV</th>
<th>Financial Transaction Services (FinTS) Dokument: Security - Sicherheitsverfahren PIN/TAN</th>
</tr>
<tr>
<td>Seite:<br>8</td>
<td>Stand: 23.02.2018</td>
<td>Kapitel: Einleitung</td>
</tr>
</table>


## Dokumentenstruktur

Das vorliegende Dokument steht in folgendem Bezug zu den anderen Bänden der
FinTS V3.0 Spezifikation:


![Hauptdokument Formals Rückmeldungen SEPA Messages Geschäftsvorfälle Messages Finanzdatenformate Security HBCI Security PIN/TAN Security Secoder 1 5 2 3 4 6 0 8 9 7 DK- Signaturkarte C Secoder R chipTAN mobile TAN Secoder](figures/8.1)


<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th rowspan="2">Version: 3.0-FV</th>
<th rowspan="2">Kapitel: A</th>
</tr>
<tr>
<th>Dokument:</th>
<th>Security - Sicherheitsverfahren PIN/TAN</th>
</tr>
<tr>
<td>Kapitel:</td>
<td>Einleitung</td>
<td>Stand: 23.02.2018</td>
<td>Seite: 9</td>
</tr>
</table>


## Inhaltsverzeichnis


<table>
<tr>
<td>Versionsführung</td>
<td>5</td>
</tr>
<tr>
<td>Änderungen gegenüber der Vorversion</td>
<td>5</td>
</tr>
<tr>
<td>Dokumentenstruktur</td>
<td>8</td>
</tr>
<tr>
<td>Inhaltsverzeichnis</td>
<td>9</td>
</tr>
<tr>
<td>Abbildungsverzeichnis</td>
<td>13</td>
</tr>
<tr>
<td>A. Einleitung</td>
<td>14</td>
</tr>
<tr>
<td>B. Verfahrensbeschreibung</td>
<td>17</td>
</tr>
<tr>
<td>B.1 Allgemeines</td>
<td>17</td>
</tr>
<tr>
<td>B.2 Zwei-Schritt-TAN-Verfahren</td>
<td>18</td>
</tr>
<tr>
<td>B.3 Starke Kundenauthentifizierung</td>
<td>20</td>
</tr>
<tr>
<td>B.4 Abläufe beim Zwei-Schritt-Verfahren</td>
<td>22</td>
</tr>
<tr>
<td>B.4.1 Abläufe bei Prozessvariante 1</td>
<td>23</td>
</tr>
<tr>
<td>B.4.1.1 Einfach-TAN bei Prozessvariante 1</td>
<td>23</td>
</tr>
<tr>
<td>B.4.1.2 Synchrone Eingabe von Mehrfach-TANs bei Prozessvariante 1</td>
<td>25</td>
</tr>
<tr>
<td>B.4.2 Abläufe bei Prozessvariante 2</td>
<td>26</td>
</tr>
<tr>
<td>B.4.2.1 Einfach-TAN bei Prozessvariante 2</td>
<td>27</td>
</tr>
<tr>
<td>B.4.2.2 Synchrone Eingabe von Mehrfach-TANs in einem Dialog bei Prozessvariante 2</td>
<td>29</td>
</tr>
<tr>
<td>B.4.2.3 Zeitversetzte, dialogübergreifende Eingabe von Mehrfach-TANs bei Prozessvariante 2</td>
<td>31</td>
</tr>
<tr>
<td>B.4.3 Abläufe bei der Initialisierung mit starker Kundenauthentifizierung</td>
<td>33</td>
</tr>
<tr>
<td>B.4.3.1 Rahmenbedingungen für den Einsatz der starken Kundenauthentifizierung</td>
<td>34</td>
</tr>
<tr>
<td>B.4.3.2 Initialisierung bei Prozessvariante 1</td>
<td>38</td>
</tr>
<tr>
<td>B.4.3.3 Initialisierung bei Prozessvariante 2</td>
<td>40</td>
</tr>
<tr>
<td>B.4.4 Allgemeine Festlegungen zum Zeitverhalten beim Zwei- Schritt-Verfahren</td>
<td>42</td>
</tr>
<tr>
<td>B.4.4.1 Verteilung von Aufträgen auf FinTS-Nachrichten</td>
<td>42</td>
</tr>
<tr>
<td>B.4.4.2 Zeitüberwachung beim Zwei-Schritt-Verfahren bei Einfach-TANs</td>
<td>43</td>
</tr>
<tr>
<td>B.5 Geschäftsvorfall HKTAN für Zwei-Schritt-TAN-Einreichung</td>
<td>43</td>
</tr>
<tr>
<td>B.5.1 Geschäftsvorfall HKTAN in Segmentversion #6</td>
<td>44</td>
</tr>
<tr>
<td>B.6 Erweiterung der Rückmeldungscodes</td>
<td>51</td>
</tr>
<tr>
<td>B.6.1 Beschreibung spezieller Rückmeldungen im Zwei-Schritt- Verfahren</td>
<td>52</td>
</tr>
<tr>
<td>B.7 Bankfachliche Anforderungen</td>
<td>54</td>
</tr>
</table>


<!-- PageBreak -->


<table>
<tr>
<th>Kapitel:</th>
<th>Version: 3.0-FV</th>
<th>Financial Transaction Services (FinTS) Dokument: Security - Sicherheitsverfahren PIN/TAN</th>
</tr>
<tr>
<td>Seite:<br>10</td>
<td>Stand: 23.02.2018</td>
<td>Kapitel: Einleitung</td>
</tr>
</table>


<table>
<tr>
<td>B.8 Erweiterung der Bank- und Userparameterdaten (BPD / UPD)</td>
<td>54</td>
</tr>
<tr>
<td>B.8.1 PIN/TAN-spezifische Informationen (HIPINS)</td>
<td>55</td>
</tr>
<tr>
<td>B.8.2 Spezielle Festlegungen für die Dialoginitialisierung beim Zwei-Schritt-Verfahren</td>
<td>56</td>
</tr>
<tr>
<td>B.9 Besondere Belegungsrichtlinien</td>
<td>57</td>
</tr>
<tr>
<td>B.9.1 DEG ,,Sicherheitsprofil"</td>
<td>58</td>
</tr>
<tr>
<td>B.9.2 DEG ,,Schlüsselname“</td>
<td>58</td>
</tr>
<tr>
<td>B.9.3 DEG ,,Sicherheitsidentifikation, Details"</td>
<td>58</td>
</tr>
<tr>
<td>B.9.4 Segment ,,Signaturkopf"</td>
<td>58</td>
</tr>
<tr>
<td>B.9.5 DEG ,,Hashalgorithmus"</td>
<td>58</td>
</tr>
<tr>
<td>B.9.6 DEG ,,Signaturalgorithmus"</td>
<td>58</td>
</tr>
<tr>
<td>B.9.7 Segment ,,Signaturabschluss“</td>
<td>59</td>
</tr>
<tr>
<td>B.9.8 Segment „Verschlüsselungskopf“</td>
<td>59</td>
</tr>
<tr>
<td>B.9.9 DEG „Verschlüsselungsalgorithmus“</td>
<td>59</td>
</tr>
<tr>
<td>B.9.10 Segment „Verschlüsselte Daten“</td>
<td>59</td>
</tr>
<tr>
<td>B.9.11 Parametersegmente zu Geschäftsvorfällen</td>
<td>59</td>
</tr>
<tr>
<td>C. PIN/TAN-Management</td>
<td>60</td>
</tr>
<tr>
<td>C.1 Verwalten der Online-Banking-PIN</td>
<td>61</td>
</tr>
<tr>
<td>C.1.1 PIN-Änderung</td>
<td>61</td>
</tr>
<tr>
<td>C.2 Sperren der Online-Banking-PIN</td>
<td>63</td>
</tr>
<tr>
<td>C.2.1 Sperre bei mehrmaliger Falscheingabe</td>
<td>63</td>
</tr>
<tr>
<td>C.2.2 PIN-Sperre</td>
<td>64</td>
</tr>
<tr>
<td>C.2.3 PIN-Sperre aufheben</td>
<td>65</td>
</tr>
<tr>
<td>C.3 Management chipTAN, mobileTAN und bilaterale Verfahren</td>
<td>67</td>
</tr>
<tr>
<td>C.3.1 Anzeige der verfügbaren TAN-Medien</td>
<td>67</td>
</tr>
<tr>
<td>C.3.1.1 Anzeigen der verfügbaren TAN-Medien, Segmentversion #5</td>
<td>67</td>
</tr>
<tr>
<td>C.3.1.2 Übermitteln / Anzeigen von TAN-Generator (HHD)- und Secoder-Informationen</td>
<td>70</td>
</tr>
<tr>
<td>C.3.2 TAN-Medium an- bzw. ummelden in Segmentversion #3</td>
<td>73</td>
</tr>
<tr>
<td>C.3.3 TAN-Generator Synchronisierung</td>
<td>76</td>
</tr>
<tr>
<td>C.3.4 Verwalten von Mobilfunkverbindungen</td>
<td>79</td>
</tr>
<tr>
<td>C.3.4.1 Mobilfunkverbindung registrieren</td>
<td>79</td>
</tr>
<tr>
<td>C.3.4.2 Mobilfunkverbindung freischalten</td>
<td>81</td>
</tr>
<tr>
<td>C.3.4.3 Mobilfunkverbindung ändern</td>
<td>82</td>
</tr>
<tr>
<td>C.3.4.4 Deaktivieren / Löschen von TAN-Medien</td>
<td>84</td>
</tr>
<tr>
<td>C.4 Sonstige</td>
<td>87</td>
</tr>
<tr>
<td>C.4.1 TAN-Verbrauchsinformationen anzeigen</td>
<td>87</td>
</tr>
</table>


<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th rowspan="2">Version: 3.0-FV</th>
<th rowspan="2">Kapitel:<br>A</th>
</tr>
<tr>
<th>Dokument:</th>
<th>Security - Sicherheitsverfahren PIN/TAN</th>
</tr>
<tr>
<td>Kapitel:</td>
<td>Einleitung</td>
<td>Stand: 23.02.2018</td>
<td>Seite: 11</td>
</tr>
</table>


<table>
<tr>
<td>C.4.1.1 TAN-Verbrauchsinformationen anzeigen, Segmentversion #2</td>
<td>87</td>
</tr>
<tr>
<td>C.4.2 TAN prüfen und „verbrennen“</td>
<td>89</td>
</tr>
<tr>
<td>C.4.3 PIN prüfen</td>
<td>89</td>
</tr>
<tr>
<td>D. Data-Dictionary</td>
<td>91</td>
</tr>
<tr>
<td>E. Archiv: Ältere Segmentversionen</td>
<td>150</td>
</tr>
<tr>
<td>E.1 HKTAN für Zwei-Schritt-TAN-Einreichung</td>
<td>150</td>
</tr>
<tr>
<td>E.1.1 Geschäftsvorfall HKTAN in Segmentversion #1</td>
<td>150</td>
</tr>
<tr>
<td>E.1.2 Geschäftsvorfall HKTAN in Segmentversion #2</td>
<td>153</td>
</tr>
<tr>
<td>E.1.3 Geschäftsvorfall HKTAN in Segmentversion #3</td>
<td>158</td>
</tr>
<tr>
<td>E.1.4 Geschäftsvorfall HKTAN in Segmentversion #4</td>
<td>164</td>
</tr>
<tr>
<td>E.1.5 Geschäftsvorfall HKTAN in Segmentversion #5</td>
<td>169</td>
</tr>
<tr>
<td>E.2 Management chipTAN, mobileTAN und bilaterale Verfahren</td>
<td>176</td>
</tr>
<tr>
<td>E.2.1 Anzeige der verfügbaren TAN-Medien</td>
<td>176</td>
</tr>
<tr>
<td>E.2.1.1 Anzeigen der verfügbaren TAN-Medien, Segmentversion #1</td>
<td>176</td>
</tr>
<tr>
<td>E.2.1.2 Anzeigen der verfügbaren TAN-Medien, Segmentversion #2</td>
<td>177</td>
</tr>
<tr>
<td>E.2.1.3 Anzeigen der verfügbaren TAN-Medien, Segmentversion #3</td>
<td>179</td>
</tr>
<tr>
<td>E.2.1.4 Anzeigen der verfügbaren TAN-Medien, Segmentversion #4</td>
<td>181</td>
</tr>
<tr>
<td>E.2.2 TAN-Generator / TAN-Liste an- bzw. ummelden</td>
<td>184</td>
</tr>
<tr>
<td>E.2.2.1 TAN-Generator / TAN-Liste an- bzw. ummelden in Segmentversion #1</td>
<td>184</td>
</tr>
<tr>
<td>E.2.2.2 TAN-Generator / TAN-Liste an- bzw. ummelden in Segmentversion #2</td>
<td>186</td>
</tr>
<tr>
<td>E.2.3 Verwalten von Mobilfunkverbindungen</td>
<td>188</td>
</tr>
<tr>
<td>E.2.3.1 Mobilfunkverbindung registrieren</td>
<td>188</td>
</tr>
<tr>
<td>E.2.3.2 Mobilfunkverbindung freischalten</td>
<td>193</td>
</tr>
<tr>
<td>E.2.3.3 Mobilfunkverbindung ändern</td>
<td>195</td>
</tr>
<tr>
<td>E.2.3.4 Deaktivieren / Löschen von TAN-Medien</td>
<td>199</td>
</tr>
<tr>
<td>E.2.4 TAN-Verbrauchsinformationen anzeigen<br>E.2.4.1 TAN-Verbrauchsinformationen anzeigen, Segmentversion #1</td>
<td>201<br>201</td>
</tr>
<tr>
<td>F. Anlagen</td>
<td>204</td>
</tr>
<tr>
<td>F.1 Übersicht der Segmente</td>
<td>204</td>
</tr>
<tr>
<td>F.2 Übersicht Nachrichtenaufbau</td>
<td>206</td>
</tr>
<tr>
<td>F.2.1 Beispieldialog im Ein-Schritt-Verfahren</td>
<td>207</td>
</tr>
<tr>
<td>F.2.2 Nachricht ,,Dialoginitialisierung"</td>
<td>207</td>
</tr>
<tr>
<td>F.2.3 Nachricht „SEPA Einzelüberweisung“</td>
<td>209</td>
</tr>
</table>


<!-- PageBreak -->


<table>
<tr>
<th>Kapitel:</th>
<th>Version: 3.0-FV</th>
<th>Financial Transaction Services (FinTS) Dokument: Security - Sicherheitsverfahren PIN/TAN</th>
</tr>
<tr>
<td>Seite: 12</td>
<td>Stand: 23.02.2018</td>
<td>Kapitel: Einleitung</td>
</tr>
</table>


<table>
<tr>
<td>F.2.4<br>Nachricht ,,Saldenabfrage"</td>
<td>210</td>
</tr>
<tr>
<td>F.2.5<br>Nachricht ,,Dialogbeendigung"</td>
<td>210</td>
</tr>
</table>


<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th rowspan="2">Version: 3.0-FV</th>
<th rowspan="2">Kapitel:<br>A</th>
</tr>
<tr>
<th>Dokument:</th>
<th>Security - Sicherheitsverfahren PIN/TAN</th>
</tr>
<tr>
<td>Kapitel:</td>
<td>Einleitung</td>
<td>Stand: 23.02.2018</td>
<td>Seite: 13</td>
</tr>
</table>


Abbildungsverzeichnis


<table>
<tr>
<td>Abbildung 1: Online-Banking mit PIN/TAN und HBCI</td>
<td>14</td>
</tr>
<tr>
<td>Abbildung 2: Präsentationsbeispiel für ein konkretes Zwei-Schritt-Verfahren</td>
<td>20</td>
</tr>
<tr>
<td>Abbildung 3: Wirkung der PSD2 Ausnahmen auf den Ablauf</td>
<td>22</td>
</tr>
</table>


<!-- PageBreak -->


<table>
<tr>
<th>Kapitel:</th>
<th>Version: 3.0-FV</th>
<th>Financial Transaction Services (FinTS) Dokument: Security - Sicherheitsverfahren PIN/TAN</th>
</tr>
<tr>
<td>Seite:<br>14</td>
<td>Stand: 23.02.2018</td>
<td>Kapitel: Einleitung</td>
</tr>
</table>


### A. EINLEITUNG

In dieser Spezifikation wird ein multibankfähiges FinTS-Protokoll für das Sicher-
heitsverfahren PIN/TAN beschrieben. Dieses Sicherheitsverfahren kann in mul-
tibankfähigen Online-Banking-Verfahren der deutschen Kreditwirtschaft eingesetzt
werden. Informationen bzgl. Nachrichtenaufbau und Dialogablauf sind dem Doku-
ment [Formals] zu entnehmen.

Um ein möglichst hohes Maß an Synergie nutzen zu können, wird für die Kommuni-
kation zwischen Kundenprogramm und Kreditinstitut weitestgehend auf der FinTS-
Spezifikation V3.0 (Sicherheitsverfahren HBCI) [HBCI] aufgesetzt, insbesondere
bzgl. Syntax, Datenformaten und Abläufen. Sofern nicht anders vermerkt gelten für
den Nachrichtenaufbau, Dialogablauf etc. die dort getroffenen Regelungen. Dieses
Dokument beschreibt daher nur die für das PIN/TAN-Verfahren abweichenden Fest-
legungen.

Die Einführung eines PIN/TAN-Protokolls auf Basis der FinTS-Syntax bietet die
Möglichkeit, sämtliche Online-Banking-Verfahren über eine einheitliche Plattform
abzuwickeln.


Abbildung 1: Online-Banking mit PIN/TAN und HBCI

![Finanz- Software für FinTS -PIN/TAN- FinTS- Komponenten PIN/TAN PIN/TAN- Verwaltung PIN/TAN- Interface Internet- Protokolle FinTS- Server Finanz- Software für FinTS -HBCI- Bank- anwen- dungen FinTS- Componenten HBCI HBCI Schlüssel- verwaltung](figures/14.1)


FinTS mit dem Sicherheitsverfahren PIN/TAN verfolgt als primären Zweck das Onli-
ne-Banking mit Offline-Finanzsoftwareprodukten. Um eine möglichst einfache In-
tegration in bestehende FinTS-Systeme zu erlauben, sollen die in der FinTS-

<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th rowspan="2">Version: 3.0-FV</th>
<th rowspan="2">Kapitel:<br>A</th>
</tr>
<tr>
<th>Dokument:</th>
<th>Security - Sicherheitsverfahren PIN/TAN</th>
</tr>
<tr>
<td>Kapitel:</td>
<td>Einleitung</td>
<td>Stand: 23.02.2018</td>
<td>Seite: 15</td>
</tr>
</table>


Spezifikation beschriebene Syntax und die Datenformate möglichst unverändert als
Grundlage verwendet werden. Somit gelten auch die für den Transport von Signa-
tur- und Verschlüsselungsinformationen erforderlichen Datenstrukturen weiterhin,
obwohl sie teilweise für das PIN/TAN-Verfahren nicht benötigt werden. Es wird le-
diglich eine neue DEG, die so genannte „Benutzerspezifische Signatur“ für die Auf-
nahme von PIN und TAN definiert, die anstatt der elektronischen HBCI-Signatur in
den Signaturabschluss eingestellt wird. Die nicht verwendeten Datenelemente der
Sicherheitssegmente werden, falls notwendig, mit Defaultwerten belegt.

Ob ein Kreditinstitut das Sicherheitsverfahren PIN/TAN anbietet, erkennt das Kun-
denprodukt in den Bankparameterdaten am Vorhandensein des Geschäftsvorfallpa-
rametersegments HIPINS (,,PIN/TAN-spezifische Informationen", vgl. Kapitel B.8.1)
bzw. des Kommunikationsdienstes 3 (https) im HIKOM-Segment.

Grundsätzlich können mit dem Sicherheitsverfahren PIN/TAN alle im Dokument
[Messages] aufgeführten Geschäftsvorfälle verwendet werden. Dies gilt auch für
verbandsindividuelle Erweiterungen. Welche Geschäftsvorfälle konkret zulässig
sind, teilt das Kreditinstitut im Segment HIPINS (s. Kap. B.8.1) mit.

Da bei PIN/TAN aufgrund der nicht vorhandenen kryptographischen Verfahren auf
Protokollebene keine Verschlüsselung zum Einsatz kommen kann, muss https
(TLS) auf Transportebene verwendet werden. Das FinTS Sicherheitsverfahren
PIN/TAN verbindet damit die Sicherheit eines Einmalpassworts (TAN) mit der in TLS
bewährten Transportverschlüsselung.

Das Sicherheitsverfahren PIN/TAN tritt in FinTS bezüglich der Einreichung von
TAN-pflichtigen Geschäftsvorfällen in zwei unterschiedlichen Ausprägungen auf, die
sich vom Prozessablauf her unterscheiden:


#### Ein-Schritt-TAN-Verfahren

Beim Ein-Schritt-TAN-Verfahren wird der Geschäftsvorfall in einem Prozess-Schritt
zusammen mit der TAN eingereicht, d. h. in einem Dialogschritt bestehend aus Auf-
trag und Antwort wird ein TAN-pflichtiger Geschäftsvorfall komplett abgewickelt.
Diese Verfahrensweise entspricht dem Vorgehen bei signaturbasierten Verfahren
und war bis zur Einführung des Zwei-Schritt-Verfahrens die einzige Möglichkeit,
TAN-pflichtige Aufträge über das FinTS-Protokoll einzureichen. Mit dem Ein-Schritt-
Verfahren kann keine starke Authentifizierung (vgl. [PSD2]) durchgeführt werden. Es
wird jedoch benötigt, um PIN/TAN-Management-Geschäftsvorfälle wie z. B. eine ini-
tiale PIN-Änderung durchführen zu können.

<!-- PageBreak -->


<table>
<tr>
<th>Kapitel:</th>
<th>Version: 3.0-FV</th>
<th>Financial Transaction Services (FinTS) Dokument: Security - Sicherheitsverfahren PIN/TAN</th>
</tr>
<tr>
<td>Seite:<br>16</td>
<td>Stand: 23.02.2018</td>
<td>Kapitel: Einleitung</td>
</tr>
</table>


## Zwei-Schritt-TAN-Verfahren

Beim Zwei-Schritt-Verfahren werden die Auftragseinreichung und die TAN-
Übermittlung in zwei Teilschritte zerlegt. Dadurch hat das Kreditinstitut auch die
Möglichkeit, als Antwort auf die erste Nachricht eine so genannte ,,Challenge" zu
übermitteln, aus der der Kunde dann die zu verwendende TAN herleiten muss.
Dadurch wird auch eine logische Bindung (auch als ,Dynamic Linking" bezeichnet)
der TAN an den Auftrag erreicht. Ein Zwei-Schritt-Verfahren ist die Voraussetzung
für die Durchführung einer starken Authentifizierung (vgl. [PSD2]).

Das Zwei-Schritt-Verfahren in FinTS beschreibt ausschlieBlich die Protokollabläufe
und dient als abstrakte Beschreibung, die in konkreten Ausprägungen wie z. B.
chipTAN verwendet werden kann. Die konkreten Ausprägungen selbst sind nicht
Bestandteil dieser Spezifikation.

Die Vorteile des FinTS Sicherheitsverfahrens PIN/TAN:

. Abwicklung aller Online-Banking-Verfahren (Kommunikationszugänge, Sicher-
heitsverfahren PIN/TAN und HBCI) über eine einheitliche Plattform

· Verfügbarkeit aller FinTS-Geschäftsvorfälle auch für PIN/TAN-Kunden

. Die Anpassung bestehender HBCI-Kundenprodukte ist mit Hilfe eines durch das
PIN/TAN-Verfahren erweiterten FinTS-Protokollbausteins möglich.

· einheitliche Stammdatenhaltung für alle Online-Banking-Verfahren

· einheitliche Anbindung der Banken-Fachanwendungen

. Kundenauthentisierung und -autorisierung an einer zentralen Stelle

· Standardisierung der Geschäftsvorfälle für das PIN/TAN-Management (z. B. PIN
ändern, TAN-Medien-Management u. ä.)

Im Folgenden gilt die Definition:


## FinTS-Füllwert

Als FinTS-Füllwert wird eine Belegung des entsprechenden Datenelementes be-
trachtet, welche den getroffenen Festlegungen (Formatvorgaben, Restriktionen, Be-
legungshinweise) nicht widerspricht. Ein FinTS-Füllwert ist somit ein gültiger Wert im
Sinne der Definition des Datenelementes. Trotzdem ist dieser FinTS-Füllwert des
betroffenen Datenelements für die Verarbeitung nicht relevant und wird daher von
den verarbeitenden Systemen auf Kreditinstitutsseite ignoriert.

Handelt es sich um Datenelemente mit Status ,O", sollten diese leer gelassen wer-
den. Auch hier gilt, dass Vorhandensein und Inhalt kreditinstitutsseitig nicht geprüft
werden.

<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th rowspan="2">Version: 3.0-FV</th>
<th rowspan="2">Kapitel: B</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Security - Sicherheitsverfahren PIN/TAN</td>
</tr>
<tr>
<td>Kapitel:<br>Abschnitt:</td>
<td>Allgemeines<br>Verfahrensbeschreibung</td>
<td>Stand: 23.02.2018</td>
<td>Seite: 17</td>
</tr>
</table>


# B. VERFAHRENSBESCHREIBUNG


## B.1 Allgemeines

Es gelten die in [Formals] und [HBCI] aufgeführten Formate und Belegungsrichtli-
nien.

Ergänzend bzw. abweichend hierzu gilt:

· Datenelemente in den Sicherheitssegmenten werden teilweise abweichend be-
legt (s. Kap. B.8). Die korrekte Segmentabfolge ist in Kap. F.1 beschrieben.

. PIN und TAN werden in die DEG ,,Benutzerdefinierte Signatur" des Segments
HNSHA ab der Version #2 eingestellt.

· Für die Rückmeldungen wurden neue Codes definiert (s. Kap. B.5.1).

. Beim HBCI DDV-Verfahren und TAN-Verfahren unter Verwendung von HKTAN >
Segmentversion #4 dürfen in der Dialoginitialisierung keine Schlüssel ausge-
tauscht werden (Segmente HKISA und HIISA).

. Die Bankparameterdaten werden um das Segment HIPINS erweitert, das die
PIN/TAN-spezifischen Informationen des Kreditinstituts enthält. Zusätzlich
kommt bei Einsatz des Zwei-Schritt-TAN-Verfahrens der neue Geschäftsvorfall
HKTAN für die Abwicklung und das Parametersegment HITANS für die Festle-
gungen hinzu.

• Der für den Kunden zugelassene Geschäftsvorfall HKTAN und die Geschäftsvor-
fälle für das PIN/TAN-Management sind im Segment HIUPD mitzuteilen.

· Die Verschlüsselungssegmente werden auch beim PIN/TAN-Verfahren benötigt,
obwohl dort auf Protokollebene keine Verschlüsselung stattfindet. Dies ist erfor-
derlich, damit der Aufbau personalisierter Nachrichten bei den Sicherheitsverfah-
ren HBCI und PIN/TAN identisch ist.

. Als Kommunikationsdienst ist https ab der Version #4 des Segmentes HIKOM zu
verwenden [Formals].

Für den Einsatz von Zwei-Schritt-Verfahren gelten zusätzlich die folgenden allge-
meinen Festlegungen:

· 1 bis 98 unterschiedliche Zwei-Schritt-Verfahren pro Institut
1 bis 9 unterschiedliche Zwei-Schritt-Verfahren pro Benutzer
(+ ggf. Ein-Schritt-Verfahren)

· Zur eindeutigen Bezeichnung des Ein- oder Zwei-Schritt-Verfahrens wird das
Element ,,Sicherheitsfunktion, kodiert" verwendet:

999: Ein-Schritt-Verfahren;

900 ... 997: Zwei-Schritt-Verfahren

Die Verknüpfung von Code und Verfahren ist institutsspezifisch und wird in der
BPD festgelegt (vgl. hierzu Kapitel B.8.2 und D).

• Alle unterstützten TAN-Verfahren (das Ein-Schritt-Verfahren und bis zu 98 in der
BPD definierte konkrete Zwei-Schritt-Verfahren) gelten als gleichberechtigte
PIN/TAN-Sicherheitsverfahren, die in HIPINS nicht dediziert angesprochen wer-
den können.

<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: B</td>
<td>Version: 3.0-FV</td>
<td>Financial Transaction Services (FinTS) Dokument: Security - Sicherheitsverfahren PIN/TAN</td>
</tr>
<tr>
<td>Seite:<br>18</td>
<td>Stand: 23.02.2018</td>
<td>Kapitel: Verfahrensbeschreibung<br>Abschnitt: Zwei-Schritt-TAN-Verfahren</td>
</tr>
</table>


Daher muss ein in HIPINS definierter TAN-pflichtiger Auftrag über irgendeines
aber kein spezielles der unterstützten TAN-Verfahren autorisiert werden.

· Mit dem Rückmeldungscode 3920 und Rückmeldeparametern werden dem Kun-
den in der Dialoginitialisierungsantwort die für ihn zugelassenen PIN/TAN-
Sicherheitsverfahren (ein Einschritt-Verfahren und bis zu 9 unterschiedliche
Zwei-Schritt-Verfahren) mitgeteilt. Als Bezugssegment für das Rückmeldungs-
segment HIRMS wird HKVVB (Verarbeitungsvorbereitung) verwendet.

• Der Kunde übermittelt im Signaturkopf der Dialoginitialisierungsnachricht, mit
welchem konkreten TAN-Verfahren er den Dialog führen will. Das konkrete TAN-
Verfahren darf während des Dialogs nicht gewechselt werden.

• Die beiden Teilschritte des Zwei-Schritt-Verfahrens müssen nicht zwingend in ei-
nem einzigen Dialog abgewickelt werden, außer es handelt sich um eine Dialogi-
nitialisierung. Über den Auftrags-Hashwert bzw. die Auftragsreferenz ist eine ent-
sprechende Verkettung über mehrere Dialoge hinweg möglich. Über einen BPD-
Parameter wird gesteuert, ob zeitversetztes / dialogübergreifendes Arbeiten er-
laubt ist.

. Beim Einsatz von Mehrfach-TANs gilt ein konkretes Zwei-Schritt-Verfahren für
den gesamten Dialog des jeweiligen Benutzers. Jeder Benutzer kann ein eigenes
konkretes Zwei-Schritt-Verfahren verwenden, die Prozessvariante (vgl. Kapitel
B.2) darf im Kontext einer Mehrfach-TAN-Einreichung jedoch nicht gewechselt
werden. Im Falle eines nicht zugelassenen Wechsels der Prozessvariante muss
das Kreditinstitut den Dialog mit Rückmeldungscode 9957 ,,Wechsel der TAN
Prozessvariante bei Mehrfach-TANs nicht erlaubt“ beenden. Für die Anmeldung
mit starker Authentifizierung (vgl. Kapitel B.4.3) sind Mehrfach-TANs nicht zuge-
lassen. Innerhalb eines Dialoges, der vom dialogführenden Benutzer mittels star-
ker Authentifizierung eröffnet wurde, können jedoch Aufträge mit Mehrfach-TANs
eingereicht werden.

. Eine im Rahmen der Dialoginitialisierung für die starke Kundenauthentifizierung
verwendete TAN gilt nicht für weitere in diesem Dialog eingereichte TAN-
pflichtige Aufträge (dies ist keine Session-TAN).


![](figures/18.1)


Gemäß §7 der „Bedingungen für die konto-/depotbezogene Nutzung
des Online-Banking mit PIN und TAN" dürfen sowohl die PIN als
auch TANs nicht elektronisch im Kundenprodukt gespeichert wer-
den.


## B.2 Zwei-Schritt-TAN-Verfahren

Das einschrittige PIN/TAN-Verfahren orientiert sich an der Arbeitsweise des HBCI-
Sicherheitsverfahrens und verwendet PIN und TAN im Sinne einer „Signatur“ einer
FinTS-Nachricht. Die Verwendung des Ein-Schritt-Verfahrens ist jedoch nur noch in
bestimmten Situationen, z. B. zur Ermittlung der zugelassenen Sicherheitsverfahren,
zugelassen. Die Arbeitsweise aller gängigen PIN/TAN-basierten Verfahren erfordert
jedoch bei TAN-pflichtigen Aufträgen eine Aufteilung zwischen Auftragseinreichung
und Authentisierung / Autorisierung in zwei Prozess-Schritte, um dem Kunden zum
Zweck der Transparenz über die relevanten Inhalte des Auftrags wie z. B. Betrag
und Empfänger eine Sicherheitsfrage, die so genannte ,,Challenge" mitzuteilen, die
er für die Ermittlung / Erzeugung der TAN benötigt. Damit wird die TAN über einen

<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th rowspan="2">Version: 3.0-FV</th>
<th rowspan="2">Kapitel: B</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Security - Sicherheitsverfahren PIN/TAN</td>
</tr>
<tr>
<td>Kapitel:<br>Abschnitt:</td>
<td>Verfahrensbeschreibung<br>Zwei-Schritt-TAN-Verfahren</td>
<td>Stand: 23.02.2018</td>
<td>Seite: 19</td>
</tr>
</table>


verfahrensabhängigen Algorithmus logisch an den Auftrag gebunden („Dynamic
Linking"). Dabei gibt es in FinTS grundsätzlich zwei unterschiedliche Prozessvarian-
ten, die mit insgesamt vier TAN-Prozessen abgebildet werden:


### Prozessvariante 1

. TAN-Prozess=1:

Im ersten Schritt wird ein Auftrags-Hashwert zum Institut übermittelt, der zur Her-
leitung der Challenge dient, die vom Institut zum Kundenprodukt gesendet wird.
Im zweiten Schritt werden die Auftragsdaten inklusive TAN eingereicht und bestä-
tigt.


### Prozessvariante 2

Bei der Prozessvariante 2 werden die TAN-Prozesse=2 bis 4 verwendet. Die
TAN-Prozesse 3 und 4 sind nur Unterprozesse von TAN-Prozess=2 und können
nicht isoliert auftreten.

. TAN-Prozess=2:

Zuerst wird der Auftrag eingereicht (siehe TAN-Prozess=4), aus dem eine Chal-
lenge errechnet wird. Anschließend wird mit TAN-Prozess=2 die TAN zum Institut
übertragen.

. TAN-Prozess=3:

Bei Verwendung von Mehrfach-TANs kann mit diesem Prozess die Einreichung
einer TAN eines weiteren Benutzers eingeleitet werden.

. TAN-Prozess=4:

Dient der Einleitung des Zwei-Schritt-Verfahrens für die erste TAN und wird bei
der Auftragseinreichung (Schritt 1) verwendet. TAN-Prozess=4 wird weiterhin in
Verbindung mit dem Geschäftsvorfall „TAN Prüfen und Verbrennen“ benutzt.

Beispiele für solche Zwei-Schritt-Verfahren sind Lösungen wie z. B. chipTAN- oder
mobile TAN-Verfahren.

Mit dem FinTS Zwei-Schritt-TAN-Verfahren wird keines dieser genannten Verfahren
konkret spezifiziert - es erfolgt nur eine abstrakte Definition des Ablaufs, der über
Parameter gesteuert wird. Der Ablauf selbst ist für alle Zwei-Schritt-Verfahren iden-
tisch. Die Parametrisierung eines konkreten Zwei-Schritt-Verfahrens erfolgt über das
Parametersegment HITANS (Geschäftsvorfallparameter zu „Zwei-Schritt-TAN-
Einreichung“ HKTAN).

Bei Verwendung von Mehrfach-TANs wird innerhalb eines Ablaufs die Prozessvari-
ante durch den Dialogführer des ersten (und ggf. einzigen) Dialogs für alle beteilig-
ten Benutzer festgelegt.

Durch Verwendung des Parametersegmentes HITANS ist die abstrakte Beschrei-
bung von maximal 98 konkreten Zwei-Schritt-Verfahren in der BPD möglich, die
über das Datenelement „Sicherheitsfunktion, kodiert“ referenziert werden.

<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: B</td>
<td>Version: 3.0-FV</td>
<td>Financial Transaction Services (FinTS) Dokument: Security - Sicherheitsverfahren PIN/TAN</td>
</tr>
<tr>
<td>Seite:<br>20</td>
<td>Stand: 23.02.2018</td>
<td>Kapitel: Verfahrensbeschreibung<br>Abschnitt: Starke Kundenauthentifizierung</td>
</tr>
</table>


Einem Benutzer können maximal 9 konkrete Zwei-Schritt-Verfahren zugeordnet
werden. Bei der Verwendung von Mehrfach-TANs kann jeder beteiligte Benutzer ein
eigenes konkretes Zwei-Schritt-Verfahren verwenden - die Verfahren können also
innerhalb einer Nachricht unterschiedlich sein1.


Abbildung 2: Präsentationsbeispiel für ein konkretes Zwei-Schritt-Verfahren

![1 X Überweisungsformular Empfangername Kontonummer Bankleitzahl Zwei-Schritt-Verfahren Nr. 1: Sicherheitsfkt, kodiert: 995 Techn. Identifikation: „chipTAN“ Name TAN-Verfahren: ,,chipTAN-Verfahren" Länge TAN-Eingabe: 6 Format TAN-Eingabe: 1 Text Rückgabewert: ,Start-Code" Länge Rückgabewert: 10 chipTAN-Verfahren Start-Code 2045201998 TAN:](figures/20.1)


Das Präsentationsbeispiel in Abbildung 2 soll zeigen, wie auf Basis der übermittel-
ten Parameter eine Gestaltung eines konkreten Zwei-Schritt-Verfahrens aussehen
kann.


## B.3 Starke Kundenauthentifizierung

Durch [MaSI] und [PSD2] besteht die Forderung nach einer starken Kundenauthen-
tifizierung (Strong Customer Authentication – SCA) bei Zugriff auf Kontodaten (Dia-
loginitialisierung) und Geschäftsvorfällen, die aufgrund ihres Missbrauchsrisikos
entsprechend geschützt werden müssen (TAN-pflichtige Geschäftsvorfälle).

Zusätzlich enthält [PSD2] aber auch Ausnahmen von dieser starken Kundenauthen-
tifizierung, d. h. unter bestimmten Rahmenbedingungen einen Verzicht auf die star-
ke Kundenauthentifizierung, was ebenfalls durch entsprechende FinTS-Prozesse
abzubilden ist. Da die Prüfung auf diese SCA-Ausnahmen zur Laufzeit erfolgen
muss, wird die Entscheidung, ob eine TAN erforderlich ist dynamisch gefällt. Wäh-
rend die Rahmenbedingungen zur Durchführung einer starken Kundenauthentifizie-
rung im Rahmen der Dialoginitialisierung in Abschnitt B.4.3 vollständig beschrieben
sind, folgen an dieser Stelle noch einige allgemeine Festlegungen zu den Ge-
schäftsvorfällen.

<!-- PageFooter: 1 1 Da es im aktuellen Dialog nur einen Dialogführer geben kann, müssen die zulässigen konkreten Zwei-Schritt-Verfahren der weiteren Benutzer bereits vorab über separate Dialoge (und entspre- chende Rückmeldecodes 3920) festgelegt worden sein. -->
<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th>Version:</th>
<th rowspan="2">Kapitel: B</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Security - Sicherheitsverfahren PIN/TAN</td>
<td>3.0-FV</td>
</tr>
<tr>
<td>Kapitel:</td>
<td>Verfahrensbeschreibung</td>
<td>Stand:</td>
<td>Seite:</td>
</tr>
<tr>
<td>Abschnitt:</td>
<td>Starke Kundenauthentifizierung</td>
<td>23.02.2018</td>
<td>21</td>
</tr>
</table>


Da sich die PSD2-Vorgaben nur auf den Zahlungsverkehr beziehen, gibt es in
FinTS weiterhin Geschäftsvorfälle, bei denen abhängig von der Deklaration in
HIPINS in keinem Fall oder immer eine TAN verwendet werden muss.

Durch die Einführung der Ausnahmen zur TAN-Pflicht ergeben sich für die FinTS-
Verarbeitung daher vier unterschiedliche Authentifizierungsklassen, die auch Aus-
wirkungen auf die Belegung des Elements TAN erforderlich im Parameterseg-
ment PIN/TAN-Spezifische Informationen (HIPINS) haben:


<table>
<tr>
<th>Auth- Klas- se</th>
<th>Beschreibung</th>
<th>TAN erforder- lich in HIPINS</th>
</tr>
<tr>
<td>1</td>
<td>Nicht-Zahlungsverkehrs-Geschäftsvorfälle, für die grundsätz- lich keine TAN erforderlich ist. Dies betrifft z. B. den Bereich Wertpapier.</td>
<td>N</td>
</tr>
<tr>
<td>2</td>
<td>Zahlungsverkehrs-Geschäftsvorfälle im Sinne der PSD2 wie z. B. SEPA-Überweisungen, aber auch Salden- und Umsatzab- fragen, für die die starke Kundenauthentifizierung inkl. ihrer Ausnahmen gilt. Diese werden zwar abweichend von der ur- sprünglichen Bedeutung in HIPINS nun grundsätzlich als TAN- pflichtig definiert, es wird jedoch erst zum Ausführungszeit- punkt durch das Kreditinstitut festgelegt, ob wirklich eine SCA (=TAN-Eingabe) notwendig ist, oder es sich um eine SCA-<br>Ausnahme handelt. Dabei kann dann die Definition in HIPINS dergestalt übersteuert werden, dass für einen als TAN-pflichtig gekennzeichneten Geschäftsvorfall aufgrund einer SCA Aus- nahme doch keine TAN benötigt wird.</td>
<td>✓</td>
</tr>
<tr>
<td>3</td>
<td>Nicht-Zahlungsverkehrs-Geschäftsvorfälle, für die grundsätz- lich eine TAN erforderlich ist. Dies betrifft z. B. den Bereich Wertpapier.</td>
<td>✓</td>
</tr>
<tr>
<td>4</td>
<td>PIN/TAN-Management-Geschäftsvorfälle, für die situationsbe- dingt eine starke Kundenauthentifizierung bis zum Abschluss des gesamten Prozesses ausgesetzt werden kann, z. B. im Rahmen einer initialen PIN-Änderung.</td>
<td>✓<br>J</td>
</tr>
</table>


Die Authentifizierungsklassen 1 und 3 entsprechen den heutigen statischen TAN-
Festlegungen auf Basis der Definitionen in HIPINS.

Bei der Durchführung von Geschäftsvorfällen der Authentifizierungsklasse 2 - hier-
zu gehört auch die Dialoginitialisierung – fällt die Entscheidung, ob eine TAN erfor-
derlich ist, erst nach dem Einreichen der Kundennachricht. Diese enthält bei Au-
thentifizierungsklasse 2 grundsätzlich eine TAN-Anforderung in Form eines HKTAN
ab Segmentversion #6. Institutsseitig wird nun gegen die in [PSD2] definierten Aus-
nahmen geprüft, wodurch zwei Möglichkeiten für die weitere Verarbeitung entste-
hen:

1\. Fortführen des Zwei-Schritt-TAN-Verfahrens. Dies wird vom Kreditinstitut gene-
rell durch den neuen Rückmeldungscode 0030 Auftrag empfangen - Si-
cherheitsfreigabe erforderlich signalisiert.

2\. Keine starke Kundenauthentifizierung erforderlich. Dies wird durch den Rück-
meldungscode 3076 Keine starke Authentifizierung erforderlich

<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: B</td>
<td>Version: 3.0-FV</td>
<td>Financial Transaction Services (FinTS) Dokument: Security - Sicherheitsverfahren PIN/TAN</td>
</tr>
<tr>
<td>Seite:<br>22</td>
<td>Stand: 23.02.2018</td>
<td>Kapitel: Verfahrensbeschreibung<br>Abschnitt: Abläufe beim Zwei-Schritt-Verfahren</td>
</tr>
</table>


angezeigt, zusätzlich zu fachlichen Rückmeldungen zum eingereichten Auftrag
wie z. B. 0010 Auftrag entgegengenommen.


Abbildung 3: Wirkung der PSD2 Ausnahmen auf den Ablauf

![Benutzer Institut Schritt 1a: Auftrag einreichen und TAN anfordern Prüfung auf PSD2 Ausnahmen und Entscheidung, ob Schritte 1b & 2a nötig sind Schritt 1b: Challenge Schritt 2a: TAN Nur, wenn Schritt 1b/2a nötig Schritt 2b: Antwort](figures/22.1)


Ein Kundensystem, das HKTAN ab #6 anbietet, muss auf diese beiden Möglichkei-
ten der Auftragseinreichung entsprechend reagieren können.

Details zu den genauen Abläufen sind in Kapitel B.4.3 für die Dialoginitialisierung
beschrieben. Das Verhalten beim Einreichen von Zahlungsverkehrsaufträgen ist
bzgl. der Ausnahmen analog dazu zu sehen.


![](figures/22.2)


Während der Migrationsphase: Da die Dialoginitialisierungsnach-
richt durch die Existenz des HKTAN ab Segmentversion #6 signali-
siert, ob das Kundenprodukt die starke Kundenauthentifizierung un-
terstützt, sollte das Kreditinstitut in der Antwort passende BPD
übermitteln, in denen das Segment HIPINS die für das Kundenpro-
dukt passenden Belegungen enthält. Somit sollten Geschäftsvorfälle
der Authentifizierungsklasse 2 nur bei SCA-fähigen Kundenproduk-
ten den Wert J besitzen, ansonsten den Wert N. Anderenfalls müss-
te ein Benutzer für Geschäftsvorfälle wie z. B. eine Saldenabfrage
bei nicht SCA-fähigen Kundenprodukten immer eine TAN eingeben.


## B.4 Abläufe beim Zwei-Schritt-Verfahren

Die Abläufe zur Abwicklung des Zwei-Schritt-Verfahrens unterscheiden sich je nach
gewählter Variante und der Behandlung von Mehrfach-TANs. Konkret werden fol-
gende in der Praxis vorkommenden Abläufe beschrieben:

Ablauf 1:
Prozessvariante 1 mit Einfach-TAN

<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th>Version:</th>
<th rowspan="2">Kapitel: B</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Security - Sicherheitsverfahren PIN/TAN</td>
<td>3.0-FV</td>
</tr>
<tr>
<td>Kapitel:</td>
<td>Verfahrensbeschreibung</td>
<td>Stand:</td>
<td>Seite:</td>
</tr>
<tr>
<td>Abschnitt:</td>
<td>Abläufe beim Zwei-Schritt-Verfahren</td>
<td>23.02.2018</td>
<td>23</td>
</tr>
</table>


Ablauf 2:
Prozessvariante 1 mit synchroner Eingabe von Mehrfach-TANs

Ablauf 3:
Prozessvariante 2 mit Einfach-TAN

Ablauf 4:
Prozessvariante 2 mit synchroner Eingabe von Mehrfach-TANs in ei-
nem Dialog

Ablauf 5:
Prozessvariante 2 mit zeitversetzter Eingabe von Mehrfach-TANs,
dialogübergreifend

Hinzu kommen folgende Abläufe für die Initialisierung mit starker Authentifizierung:

Ablauf 6:
Initialisierung bei Prozessvariante 1

Ablauf 7:
Initialisierung bei Prozessvariante 2

Alle Abläufe sind bezogen auf die einzelnen Prozessschritte exakt in der beschrie-
benen Form umzusetzen; die Bildung von anderen Derivaten ist nicht zugelassen.
Die Dialogendenachricht und die darauf folgende allgemeine Kreditinstitutsnachricht
werden aus Gründen der Übersichtlichkeit in den Prozessen nicht dargestellt.

Bei den Abläufen 1, 3 und 4 wird davon ausgegangen, dass alle enthaltenen Schrit-
te zwingend in einem einzigen Dialog abgewickelt werden.

In einem Dialog ist es grundsätzlich möglich aber nicht verpflichtend, dass mehrere
in sich abgeschlossene Abläufe hintereinander durchgeführt werden. Es gelten hier-
bei als Rahmenbedingungen die für den gesamten Dialog getroffenen Festlegun-
gen, z. B., dass die Prozessvariante innerhalb eines Dialoges nicht gewechselt wer-
den darf.

In den Prozessen mit Einfach-TAN sind die starke Kundenauthentifizierung und de-
ren Ausnahmen, wie in Kapitel B.3 beschrieben, berücksichtigt.


## B.4.1 Abläufe bei Prozessvariante 1

Um einen TAN-pflichtigen Auftrag im Zwei-Schritt-Verfahren über Prozessvariante 1
einzureichen, müssen die im Folgenden beschriebenen Schritte durchgeführt wer-
den. Dabei gilt grundlegende Abfolge der Segmente am Beispiel einer SEPA-
Einzelüberweisung:

1\. Schritt: HKTAN <> HITAN

2\. Schritt: HKCCS <> HIRMS zu HKCCS


## B.4.1.1Einfach-TAN bei Prozessvariante 1

Der vollständige Ablauf sieht bei einem Auftrag mit nur einer benötigten TAN („Ein-
fach-TAN") folgendermaßen aus:

Einfach-TAN bei Prozessvariante 1

Ausgangszustand:

• Es wurde ein Auftrags-Hashwertverfahren ungleich „0“ gewählt.

. Die Dialoginitialisierung ist erfolgt; der Kunde hat dort durch entsprechende
Belegung des DE ,,Sicherheitsfunktion, kodiert“ ein konkretes Zwei-Schritt-
Verfahren für den gesamten Dialog gewählt. Im Rahmen der Dialoginitialisie-
rung wurde ggf. bereits eine starke Kundenauthentifizierung durchgeführt (vgl.

<!-- PageBreak -->


<table>
<tr>
<th>Kapitel: B</th>
<th>Version: 3.0-FV</th>
<th>Financial Transaction Services (FinTS) Dokument: Security - Sicherheitsverfahren PIN/TAN</th>
</tr>
<tr>
<td>Seite:<br>24</td>
<td>Stand: 23.02.2018</td>
<td>Kapitel: Verfahrensbeschreibung<br>Abschnitt: Abläufe beim Zwei-Schritt-Verfahren</td>
</tr>
</table>


<table>
<tr>
<td colspan="3">Kapitel B.4.3).</td>
</tr>
<tr>
<td>Schritt 1a HKTAN</td>
<td>→</td>
<td>Auftrags-Hashwert einreichen<br>Durch Einreichung des Geschäftsvorfalls HKTAN mit der Bele- gung gemäß TAN-Prozess=1 wird der Auftrags-Hashwert zum Institut übertragen. Über die Belegung ,,Weitere TAN folgt" = ,N“ wird signalisiert, dass dies die letzte und einzige TAN zu dem eingereichten Auftrag ist.<br>Durch eine Prüfung der eingereichten Daten, im Speziellen der Benutzerkennung und der PIN, gegen die PSD2 Ausnahmen legt das Kreditinstitut fest, wie weiter vorgegangen werden soll:<br>. starke Kundenauthentifizierung erforderlich, angezeigt durch den Rückmeldungscode 0030 Auftrag emp- fangen - Sicherheitsfreigabe erforderlich (→weiter mit Schritt 1b(B))<br>. der Faktor Wissen ist ausreichend, angezeigt durch den Rückmeldungscode 3076 Keine starke Authen- tifizierung erforderlich (→weiter mit Schritt 1b, Fall (A)).</td>
</tr>
<tr>
<td>Schritt 1b HITAN</td>
<td>←</td>
<td>Challenge senden (A) Ohne starke Kundenauthentifizierung:<br>Durch RM-Code 3076 wird signalisiert, dass keine Challenge benötigt wird. Die Antwortnachricht enthält einen syntaktisch korrekten HITAN, d. h. für die Elemente Auftragsreferenz und Challenge sind vom Kreditinstitut die festen FinTS- Füllwerte ,,noref" und ,nochallenge" einzustellen. Diese sind vom Kundenprodukt zu ignorieren.<br>(B) Bei starker Kundenauthentifizierung:<br>Der Auftrag-Hashwert wird auf Institutsseite zwischengespei- chert und anschließend eine verfahrensspezifische Challenge ermittelt, die dem Kundenprodukt in HITAN mitgeteilt wird. Durch RM-Code 0030 zusammen mit den Elementen ,,Auf- trags-Hashwert" und ,Challenge" aus HITAN erhält das Kun- denprodukt in der Kreditinstitutsantwort die Information, dass der Kunde nun auf Basis der Challenge in vereinbarter Form ei- ne TAN ermitteln muss.</td>
</tr>
<tr>
<td>Schritt 2a z.B. HKCCS</td>
<td>→</td>
<td>1. TAN einreichen<br>(A) Ohne starke Kundenauthentifizierung:<br>Einreichen des eigentlichen Geschäftsvorfalls ohne TAN.<br>(B) Bei starker Kundenauthentifizierung:<br>Zusammen mit dem eigentlichen Geschäftsvorfall, z. B. HKCCS wird die ermittelte TAN zum Kreditinstitut übertragen. Nach er- folgreicher TAN-Verifikation kann der Auftrag verarbeitet wer- den.</td>
</tr>
<tr>
<td>Schritt 2b z. B.</td>
<td>←</td>
<td>Rückmeldungen senden</td>
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
<td>Security - Sicherheitsverfahren PIN/TAN</td>
<td>3.0-FV</td>
</tr>
<tr>
<td>Kapitel:</td>
<td>Verfahrensbeschreibung</td>
<td>Stand:</td>
<td>Seite:</td>
</tr>
<tr>
<td>Abschnitt:</td>
<td>Abläufe beim Zwei-Schritt-Verfahren</td>
<td>23.02.2018</td>
<td>25</td>
</tr>
</table>


<table>
<tr>
<td>HIRMS zu HKCCS</td>
<td></td>
<td>(A) Ohne starke Kundenauthentifizierung:<br>Mit der Kreditinstitutsantwort werden ggf. erzeugte Antwortseg- mente sowie die Rückmeldungen zum Auftrag selbst zum Kun- denprodukt gesendet.<br>(B) Bei starker Kundenauthentifizierung:<br>Mit der Kreditinstitutsantwort werden ggf. erzeugte Antwortseg- mente sowie die Rückmeldungen zur TAN-Verifikation und zum Auftrag selbst zum Kundenprodukt gesendet.</td>
</tr>
</table>


## B.4.1.2Synchrone Eingabe von Mehrfach-TANs bei Prozessvariante 1

Bereits beim etablierten Ein-Schritt-TAN-Verfahren ist die Verwendung von Mehr-
fach-TANs möglich. Diese müssen dort in einem Schritt zusammen mit dem Auftrag
eingereicht werden.

Beim Zwei-Schritt-TAN-Verfahren wird die Verwendung von Mehrfach-TANs optio-
nal in gleicher Weise unterstützt. Bei Prozessvariante 1 wird nur die synchrone Ein-
gabe von Mehrfach-TANs unterstützt. Der Parameter ,,TAN zeitversetzt / dialog-
übergreifend erlaubt“ in HITANS muss mit ,,N“ belegt werden.

Bei Verwendung von Mehrfach-TANs gemäß Prozessvariante 1 wird grundsätzlich
eine starke Kundenauthentifizierung gefordert; SCA-Ausnahmen werden nicht un-
terstützt.

Der erweiterte Ablauf für die synchrone Einreichung eines Auftrages mit Mehrfach-
TAN mit Prozessvariante 1 sieht folgendermaßen aus:


### Synchrone Eingabe von Mehrfach-TANs bei Prozessvariante 1

Ausgangszustand:

. Der Parameter ,,Mehrfach-TAN erlaubt" in HITANS ist mit ,,J" belegt.

. Der Parameter ,,TAN zeitversetzt / dialogübergreifend erlaubt" in HITANS ist
mit ,,N“ belegt.

. Es wurde ein Auftrags-Hashwertverfahren ungleich „0“ gewählt.

. Die Dialoginitialisierung ist erfolgt; der erste Benutzer hat dort durch Belegung
des DE ,,Sicherheitsfunktion, kodiert" ein konkretes Zwei-Schritt-Verfahren für
sich gewählt und dadurch die Prozessvariante 1 für den gesamten Ablauf fest-
gelegt. Im Rahmen der Dialoginitialisierung wurde ggf. bereits eine starke
Kundenauthentifizierung durchgeführt (vgl. Kapitel B.4.3).


<table>
<tr>
<td>Schritt 1a HKTAN</td>
<td>→</td>
<td>Auftrags-Hashwert einreichen<br>wie bei Einfach-TAN nach Prozessvariante 1. Über die Bele- gung ,,Weitere TAN folgt" = ,J" wird signalisiert, dass vor Einrei- chung des Auftrags mindestens eine weitere Challenge ange- fordert wird.</td>
</tr>
<tr>
<td>Schritt 1b HITAN</td>
<td>←</td>
<td>Challenge 1 senden (wie bei Einfach-TAN).</td>
</tr>
<tr>
<th>Kapitel: B</th>
<th>Version: 3.0-FV</th>
<th>Financial Transaction Services (FinTS) Dokument: Security - Sicherheitsverfahren PIN/TAN</th>
</tr>
<tr>
<td>Seite:<br>26</td>
<td>Stand: 23.02.2018</td>
<td>Kapitel: Verfahrensbeschreibung Abschnitt: Abläufe beim Zwei-Schritt-Verfahren</td>
</tr>
</table>


Neuer Dialog mit zweitem Benutzer und ggf. anderem konkreten Zwei-Schritt-
Verfahren („Sicherheitsfunktion, kodiert“)


<table>
<tr>
<td>Schritt 2a HKTAN</td>
<td>→</td>
<td>Auftrags-Hashwert einreichen<br>wie bei Einfach-TAN nach Prozessvariante 1. Über die Bele- gung ,,Weitere TAN folgt" = ,J" wird signalisiert, dass vor Einrei- chung des Auftrags noch eine weitere Challenge angefordert wird.</td>
</tr>
<tr>
<td>Schritt 2b HITAN</td>
<td>←</td>
<td>Challenge 2 senden wie bei Einfach-TAN</td>
</tr>
<tr>
<td colspan="3">Neuer Dialog mit drittem Benutzer und ggf. anderem konkreten Zwei-Schritt- Verfahren („Sicherheitsfunktion, kodiert“)</td>
</tr>
<tr>
<td>Schritt 3a HKTAN</td>
<td>→</td>
<td>Auftrags-Hashwert einreichen<br>wie bei Einfach-TAN nach Prozessvariante 1. Über die Bele- gung ,,Weitere TAN folgt" = ,N“ wird signalisiert, dass dies die letzte TAN zu dem eingereichten Auftrag ist.</td>
</tr>
<tr>
<td>Schritt 3b HITAN</td>
<td>←</td>
<td>Challenge 3 senden wie bei Einfach-TAN nach Prozessvariante 1</td>
</tr>
<tr>
<td>Schritt 4a z.B. HKCCS</td>
<td>→</td>
<td>Auftrag einreichen<br>Zusammen mit dem eigentlichen Geschäftsvorfall, z. B. HKCCS werden die ermittelten PINs und TANs in mehreren Signaturab- schlüssen zum Kreditinstitut übertragen. Nach erfolgreichen TAN-Verifikationen kann der Auftrag verarbeitet werden."</td>
</tr>
<tr>
<td>Schritt 4b z. B. HIRMS zu HKCCS</td>
<td>←</td>
<td>Rückmeldungen senden<br>Mit der Kreditinstitutsantwort zum Geschäftsvorfall werden die Rückmeldungen zum Auftrag selbst und zur TAN-Verifikation zum Kundenprodukt gesendet.<br>Über den Rückmeldecode 9910 - „Auftrag abgelehnt - Kompe- tenz nicht ausreichend" wird ggf. signalisiert, dass die für die Ausführung des Auftrags benötigten Berechtigungen nicht aus- reichend sind.</td>
</tr>
</table>


## B.4.2 Abläufe bei Prozessvariante 2

Um einen TAN-pflichtigen Auftrag im Zwei-Schritt-Verfahren über Prozessvariante 2
einzureichen, müssen die im Folgenden beschriebenen Schritte durchgeführt wer-
den. Dabei gilt die grundlegende Abfolge der Segmente am Beispiel einer Einzel-
überweisung:

Schritt 1: HKCCS und HKTAN <> HITAN

Schritt 2: HKTAN <> HITAN und HIRMS zu HKCCS

Durch die Verschachtelung der beiden Prozessschritte ergibt sich eine Sondersitua-
tion für die Verarbeitung der Rückmeldungen. Hierbei gelten folgende Regelungen:

<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th rowspan="2">Version: 3.0-FV</th>
<th rowspan="2">Kapitel: B</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Security - Sicherheitsverfahren PIN/TAN</td>
</tr>
<tr>
<td>Kapitel: Abschnitt:</td>
<td>Verfahrensbeschreibung Abläufe beim Zwei-Schritt-Verfahren</td>
<td>Stand: 23.02.2018</td>
<td>Seite: 27</td>
</tr>
</table>


• Alle Rückmeldungen in der letzten Antwort beziehen sich auf den Auftrag selbst,
auch die Rückmeldungen auf die ggf. erfolgte TAN-Einreichung mit HKTAN. In
der Antwort können auch explizite Kreditinstitutsantworten, z. B. ,SEPA Dauer-
auftragsbestand rückmelden (HICDB)" enthalten sein.

· Bei dialogübergreifender Verarbeitung kann nicht auf Bezugssegmente referen-
ziert werden. Daher muss auf Basis der DE ,,Auftragsreferenz“ eine Referenz auf
den eigentlichen Auftrag hergestellt werden.


![](figures/27.1)


Tritt in Prozessvariante 2 bei der Prüfung im ersten Schritt des ein-
gereichten Auftrags eine ggf. behebbare Fehlersituation auf, so be-
stehen für das Kreditinstitut folgende Reaktionsmöglichkeiten:

. Falls eine starke Kundenauthentifizierung erforderlich ist: Übermit-
teln einer Warnung (Rückmeldungscode 3xxx) zusammen mit ei-
nem Segment HITAN inklusive einer Challenge. Unterstützt das
Kreditinstitut das Stornieren von Aufträgen (BPD-Parameter „Auf-
tragsstorno erlaubt“=J) kann der Kunde im 2. Schritt den Auftrag
stornieren bzw. trotz der Warnung per TAN freigeben.

Falls das Kreditinstitut ein Auftragsstorno nicht unterstützt (BPD-
Parameter ,,Auftragsstorno erlaubt“=N) und der Kunde die TAN für
den Auftrag aufgrund der Warnung nicht einreicht, wird vom Kre-
ditinstitut die TAN für diesen Auftrag entwertet.

· Übermitteln eines Rückmeldungscode 9xxx ohne ein Segment
HITAN. Das Kundenprodukt muss dann den Auftrag verwerfen.
Andere Aufträge derselben Nachricht können jedoch ausgeführt
werden.

· Beenden des Dialogs mit Rückmeldungscode 9800 ohne Übermitt-
lung eines Segmentes HITAN. Keiner der in der Nachricht enthal-
tenen Aufträge wird ausgeführt.


## B.4.2.1Einfach-TAN bei Prozessvariante 2

Der vollständige Ablauf sieht bei einem Auftrag mit nur einer benötigten TAN („Ein-
fach-TAN") folgendermaßen aus:


### Einfach-TAN bei Prozessvariante 2

Ausgangszustand:

• Die Dialoginitialisierung ist erfolgt; der Benutzer hat dort durch Belegung des
DE ,,Sicherheitsfunktion, kodiert" ein konkretes Zwei-Schritt-Verfahren für sich
gewählt und dadurch die Prozessvariante 2 für den gesamten Ablauf festgelegt.
Im Rahmen der Dialoginitialisierung wurde ggf. bereits eine starke Kun-
denauthentifizierung durchgeführt (vgl. Kapitel B.4.3).


<table>
<tr>
<td>Schritt 1a z.B. HKCCS,</td>
<td>→</td>
<td>Auftrag einreichen<br>Es wird ein TAN-pflichtiger Auftrag in einer FinTS-Nachricht eingereicht. Die Nachricht enthält zusätzlich das Segment HKTAN mit der Belegung gemäß TAN-Prozess=4. Der Sig-</td>
</tr>
<tr>
<td>Kapitel: B</td>
<td>Version: 3.0-FV</td>
<td>Financial Transaction Services (FinTS) Dokument: Security - Sicherheitsverfahren PIN/TAN</td>
</tr>
<tr>
<td>Seite:<br>28</td>
<td>Stand: 23.02.2018</td>
<td>Kapitel: Verfahrensbeschreibung<br>Abschnitt: Abläufe beim Zwei-Schritt-Verfahren</td>
</tr>
</table>


<table>
<tr>
<td>HKTAN</td>
<td></td>
<td>naturabschluss enthält die PIN des Benutzers aber keine TAN. Als ,,Rolle des Sicherheitslieferanten, kodiert" wird ,,1" für Herausgeber (ISS) verwendet.<br>Durch eine Prüfung der eingereichten Daten, im Speziellen der Benutzerkennung und der PIN, gegen die PSD2 Aus- nahmen legt das Kreditinstitut fest, wie weiter vorgegangen werden soll:<br>. starke Kundenauthentifizierung erforderlich, ange- zeigt durch den Rückmeldungscode 0030 Auf- trag empfangen - Sicherheitsfreigabe erforderlich (→weiter mit Schritt 1b)<br>. der Faktor Wissen ist ausreichend, angezeigt durch den Rückmeldungscode 3076 Keine starke Authentifizierung erforderlich (→weiter mit Schritt 2b, Fall (A)).</td>
</tr>
<tr>
<td>Schritt 1b HITAN</td>
<td>←</td>
<td>Challenge senden<br>Da die Eingabe einer TAN erforderlich ist, erfolgt eine Zwi- schenspeicherung des Auftrags. Anschließend wird auf In- stitutsseite eine verfahrensspezifische Challenge ermittelt und dem Kundenprodukt im Segment HITAN mitgeteilt. In HITAN erfolgt die Belegung ebenfalls gemäß TAN- Prozess=4. Durch RM-Code 0030 zusammen mit den In- formationen ,,Auftragsreferenz“ und ,,Challenge" aus HITAN erhält das Kundenprodukt in der Kreditinstitutsantwort die Information, dass der Kunde nun auf Basis der Challenge in vereinbarter Form eine TAN ermitteln muss.</td>
</tr>
<tr>
<td>Schritt 2a HKTAN</td>
<td>→</td>
<td>TAN einreichen<br>Mit dem Geschäftsvorfall HKTAN mit der Belegung gemäß TAN-Prozess=2 wird die ermittelte TAN zusammen mit der Auftragsreferenz zum Kreditinstitut übermittelt. Wie beim Ein-Schritt-Verfahren enthält der Signaturkopf die Benut- zerkennung und der Signaturabschluss PIN und TAN des aktiven Benutzers für diesen Auftrag. Als ,Rolle des Sicher- heitslieferanten, kodiert" wird „1“ für Herausgeber (ISS) verwendet. Über die Belegung ,,Weitere TAN folgt" = ,N" wird signalisiert, dass dies die letzte und einzige TAN zu dem eingereichten Auftrag ist. Nach erfolgreicher TAN- Verifikation kann der Auftrag verarbeitet werden.</td>
</tr>
<tr>
<td>Schritt 2b z. B. HIRMS zu HKCCS, HITAN</td>
<td>←</td>
<td>Rückmeldungen senden<br>Die Nachricht enthält auch ein Segment HITAN mit TAN- Prozess=2 als Beantwortung des HKTAN. Bei Anwendung einer SCA-Ausnahme ist das Segment HITAN mit FinTS- Füllwerten belegt.<br>(A) Ohne starke Kundenauthentifizierung:<br>Mit der Kreditinstitutsantwort werden ggf. erzeugte Antwort- segmente sowie die Rückmeldungen zum Auftrag selbst zum Kundenprodukt gesendet. Die Nachricht enthält auch ein Segment HITAN mit TAN-Prozess=4 als Beantwortung</td>
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
<td>Dokument:</td>
<td>Security - Sicherheitsverfahren PIN/TAN</td>
</tr>
<tr>
<td>Kapitel:</td>
<td>Verfahrensbeschreibung</td>
<td>Stand:</td>
<td>Seite:</td>
</tr>
<tr>
<td>Abschnitt:</td>
<td>Abläufe beim Zwei-Schritt-Verfahren</td>
<td>23.02.2018</td>
<td>29</td>
</tr>
</table>


<table>
<tr>
<td></td>
<td></td>
<td>des HKTAN aus Schritt 1a.<br>Für die Elemente Auftragsreferenz und Challenge sind vom Kreditinstitut die festen FinTS-Füllwerte „noref“ und ,,nochallenge") einzustellen. Diese sind vom Kunden- produkt zu ignorieren.<br>(B) Bei starker Kundenauthentifizierung:<br>Mit der Kreditinstitutsantwort werden ggf. erzeugte Antwort- segmente sowie die Rückmeldungen zur TAN-Verifikation und zum Auftrag selbst zum Kundenprodukt gesendet. Die Nachricht enthält auch ein Segment HITAN mit TAN- Prozess=2 als Beantwortung des HKTAN aus Schritt 2a.</td>
</tr>
</table>


## B.4.2.2Synchrone Eingabe von Mehrfach-TANs in einem Dialog bei Prozessvariante 2

Bei Prozessvariante 2 wird die synchrone und zeitversetzte / dialogübergreifende
Eingabe von Mehrfach-TANs unterstützt. Dies wird über den Parameter ,TAN zeit-
versetzt / dialogübergreifend erlaubt" in HITANS gesteuert.

Bei der synchronen Eingabe von Mehrfach-TANs muss die Eingabe aller TANs zum
Auftrag innerhalb eines FinTS Dialoges erfolgen.

Bei Verwendung von Mehrfach-TANs gemäß Prozessvariante 2 wird grundsätzlich
eine starke Kundenauthentifizierung gefordert; SCA-Ausnahmen werden nicht un-
terstützt.

Der entsprechende Ablauf sieht folgendermaßen aus:

Synchrone Eingabe von Mehrfach-TANs in einem Dialog bei Prozessvarian-
te 2

Ausgangszustand:

. Der Parameter ,,Mehrfach-TAN erlaubt" in HITANS ist mit ,J“ belegt.

. Der Parameter ,,TAN zeitversetzt / dialogübergreifend erlaubt" in HITANS ist
mit ,,N" belegt.

• Der Kunde hat die Schritte 1a und 1b wie bei Einfach-TAN bei Prozessvariante
2 durchgeführt


<table>
<tr>
<td>Schritt 2a HKTAN</td>
<td>→</td>
<td>1. TAN einreichen wie bei Einfach-TAN mit Prozessvariante 2<br>Über die Belegung „Weitere TAN folgt" = ,J" wird signalisiert, dass dies nicht die letzte TAN zu dem eingereichten Auftrag war und noch mindestens eine weitere TAN nachgereicht wird. Als ,Rolle des Sicherheitslieferanten, kodiert“ wird ,1“ für Heraus- geber (ISS) verwendet.</td>
</tr>
<tr>
<td>Schritt 2b HITAN</td>
<td>←</td>
<td>Rückmeldungen zur 1. TAN senden<br>Zusammen mit dem Segment HITAN mit der Belegung gemäß TAN-Prozess=2 werden in der Kreditinstitutsantwort die Rück- meldungen zur TAN-Verifikation, nicht aber zum Auftrag selbst zum Kundenprodukt gesendet.</td>
</tr>
<tr>
<th>Kapitel: B</th>
<th>Version: 3.0-FV</th>
<th>Financial Transaction Services (FinTS) Dokument: Security - Sicherheitsverfahren PIN/TAN</th>
</tr>
<tr>
<td>Seite:<br>30</td>
<td>Stand: 23.02.2018</td>
<td>Kapitel: Verfahrensbeschreibung<br>Abschnitt: Abläufe beim Zwei-Schritt-Verfahren</td>
</tr>
</table>


<table>
<tr>
<td colspan="3">Weiterer Benutzer innerhalb des gleichen Dialogs mit ggf. anderem konkreten Zwei-Schritt-Verfahren („Sicherheitsfunktion, kodiert“)</td>
</tr>
<tr>
<td>Schritt 3a HKTAN</td>
<td>→</td>
<td>Challenge anfordern für TAN durch weiteren Benutzer<br>Mit dem Geschäftsvorfall HKTAN mit der Belegung gemäß TAN-Prozess=3 wird signalisiert, dass das Kundenprodukt eine weitere TAN zu einem bereits eingereichten Auftrag übermitteln möchte.<br>Dabei enthält ein 1. Signaturkopf die Benutzerkennung des dia- logführenden Benutzers. Als ,Rolle des Sicherheitslieferanten, kodiert“ wird „4“ für Zeuge (WIT) verwendet. Der korrespondie- rende Signaturabschluss enthält die zugehörige PIN des Dialog- führers.<br>Ein 2. Signaturkopf enthält die Benutzerkennung des weiteren Benutzers, für den die Challenge angefordert werden soll. Als ,Rolle des Sicherheitslieferanten, kodiert“ wird „1“ für Heraus- geber (ISS) verwendet. Der korrespondierende Signaturab- schluss enthält die zugehörige PIN des weiteren Benutzers.<br>Über die mitgeschickte Auftragsreferenz erfolgt die Zuordnung zu einem im Institut zuvor gespeicherten Auftrag.</td>
</tr>
</table>


<table>
<tr>
<td>Schritt 3b HITAN</td>
<td>←</td>
<td>Challenge senden für weitere TAN<br>Nach Überprüfung der PIN des weiteren Benutzers und Identifi- zieren des zwischengespeicherten Auftrags auf Institutsseite wird eine verfahrensspezifische Challenge ermittelt und dem Kundenprodukt mitgeteilt. Durch Verwenden des Rückmel- dungscode 0030 - „Auftrag empfangen - Sicherheitsfreigabe er- forderlich" zusammen mit den Informationen „Auftragsreferenz“ und ,,Challenge" aus HITAN erhält das Kundenprodukt in der Kreditinstitutsantwort die Information, dass der weitere Benutzer nun auf Basis der Challenge in vereinbarter Form eine TAN er- mitteln muss.</td>
</tr>
<tr>
<td>Schritt 4a HKTAN</td>
<td>→</td>
<td>TAN eines weiteren Benutzers einreichen<br>Mit dem Geschäftsvorfall HKTAN mit der Belegung gemäß TAN- Prozess=2 wird die ermittelte TAN eines weiteren Benutzers zum Kreditinstitut übertragen.<br>Dabei enthält ein 1. Signaturkopf wieder die Benutzerkennung des dialogführenden Benutzers. Als ,Rolle des Sicherheitsliefe- ranten, kodiert“ wird „4“ für Zeuge (WIT) verwendet. Der korres- pondierende Signaturabschluss enthält die zugehörige PIN des Dialogführers.<br>Ein 2. Signaturkopf enthält die Benutzerkennung des weiteren Benutzers, der die TAN einreichen möchte. Als „Rolle des Si- cherheitslieferanten, kodiert" wird ,1" für Herausgeber (ISS) ver- wendet. Der korrespondierende Signaturabschluss enthält die zugehörige PIN und TAN des weiteren Benutzers.<br>Über die Belegung „Weitere TAN folgt" = ,N" wird signalisiert, dass dies die letzte TAN zu dem eingereichten Auftrag war. An-</td>
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
<td>Dokument:</td>
<td>Security - Sicherheitsverfahren PIN/TAN</td>
</tr>
<tr>
<td>Kapitel:</td>
<td>Verfahrensbeschreibung</td>
<td>Stand:</td>
<td>Seite:</td>
</tr>
<tr>
<td>Abschnitt:</td>
<td>Abläufe beim Zwei-Schritt-Verfahren</td>
<td>23.02.2018</td>
<td>31</td>
</tr>
</table>


<table>
<tr>
<td></td>
<td></td>
<td>derenfalls werden innerhalb des gleichen Dialogs von einem wei- teren Benutzer die Schritte 3 und 4 in gleicher Weise nochmals durchgeführt.</td>
</tr>
<tr>
<td>Schritt 4b z. B. HIRMS zu HKCCS, HITAN</td>
<td>←</td>
<td>Rückmeldungen senden<br>Falls keine weitere TAN mehr folgt, werden mit der Kreditinstitut- santwort zum eigentlichen Auftrag ggf. erzeugte Antwortsegmen- te, sowie die Rückmeldungen zum Auftrag selbst und zur TAN- Verifikation zum Kundenprodukt gesendet. Die Nachricht enthält auch ein Segment HITAN mit der Belegung gemäß TAN- Prozess=2 als Beantwortung des HKTAN.</td>
</tr>
</table>


## B.4.2.3Zeitversetzte, dialogübergreifende Eingabe von Mehrfach-TANs bei Prozessva- riante 2

Bereits beim etablierten Ein-Schritt-TAN-Verfahren ist die Verwendung von Mehr-
fach-TANs möglich. Diese müssen dort in einem Schritt zusammen mit dem Auftrag
eingereicht werden.

<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: B</td>
<td>Version: 3.0-FV</td>
<td>Financial Transaction Services (FinTS) Dokument: Security - Sicherheitsverfahren PIN/TAN</td>
</tr>
<tr>
<td>Seite:<br>32</td>
<td>Stand: 23.02.2018</td>
<td>Kapitel: Verfahrensbeschreibung<br>Abschnitt: Abläufe beim Zwei-Schritt-Verfahren</td>
</tr>
</table>


Beim Zwei-Schritt-TAN-Verfahren wird die Verwendung von Mehrfach-TANs optio-
nal in gleicher Weise unterstützt. Bei Prozessvariante 2 wird zusätzlich zur synchro-
nen Eingabe innerhalb eines Dialoges auch die asynchrone Eingabe von Mehrfach-
TANs unterstützt. Der Parameter ,TAN zeitversetzt / dialogübergreifend erlaubt" in
HITANS muss hierfür mit „J“ belegt werden.

Dabei besteht aufgrund des komplexen Zeitverhaltens (vgl. Kapitel B.4.4.1 und
B.4.4.2.1) die Möglichkeit, die Auftrags-Einreichung mit der Eingabe der ersten TAN
von der Eingabe weiterer TANs zeitlich zu trennen. Mit dieser optionalen Möglichkeit
kann ein Einreicher einen Auftrag zusammen mit seiner PIN und TAN übermitteln –
weitere TANs anderer Berechtigter werden in separaten Prozessen in eigenen
FinTS-Dialogen nachgereicht.

Bei Verwendung von Mehrfach-TANs gemäß Prozessvariante 2 wird grundsätzlich
eine starke Kundenauthentifizierung gefordert; SCA-Ausnahmen werden nicht un-
terstützt.

Der entsprechend erweiterte Ablauf sieht folgendermaßen aus:


### Zeitversetzte, dialogübergreifende Eingabe von Mehrfach-TANs bei Pro- zessvariante 2

Ausgangszustand:

. Der Parameter ,,Mehrfach-TAN erlaubt" in HITANS ist mit ,,J" belegt.

. Der Parameter ,TAN zeitversetzt / dialogübergreifend erlaubt" in HITANS ist
mit ,,J“ belegt.

· Der Kunde hat die Schritte 1a und 1b wie bei Einfach-TAN mit Prozessvariante
2 durchgeführt


<table>
<tr>
<td>Schritt 2a HKTAN</td>
<td>→</td>
<td>1. TAN einreichen wie bei Einfach-TAN mit Prozessvariante 2<br>Über die Belegung „Weitere TAN folgt" = ,J" wird signalisiert, dass dies nicht die letzte TAN zu dem eingereichten Auftrag war und noch mindestens eine weitere TAN nachgereicht wird.</td>
</tr>
<tr>
<td>Schritt 2b HITAN</td>
<td>←</td>
<td>Rückmeldungen zur 1. TAN senden<br>Zusammen mit dem Segment HITAN mit der Belegung gemäß TAN-Prozess=2 werden in der Kreditinstitutsantwort die Rück- meldungen zur TAN-Verifikation, nicht aber zum Auftrag selbst zum Kundenprodukt gesendet.</td>
</tr>
</table>


Neuer Dialog mit weiterem Benutzer, zeitversetzt und ggf. anderem konkreten
Zwei-Schritt-Verfahren (,Sicherheitsfunktion, kodiert") aber gleicher Prozessvari-
ante


<table>
<tr>
<td>Schritt 3a HKTAN</td>
<td>→</td>
<td>Challenge anfordern für weitere TAN<br>Mit dem Geschäftsvorfall HKTAN mit Belegung gemäß TAN- Prozess=3 wird signalisiert, dass das Kundenprodukt eine wei- tere TAN zu einem bereits eingereichten Auftrag übermitteln möchte. Dabei enthält der Signaturkopf die Benutzerkennung und der Signaturabschluss die PIN des weiteren Benutzers. Über die mitgeschickte Auftragsreferenz erfolgt die Zuordnung zu einem im Institut zuvor gespeicherten Auftrag.</td>
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
<td>Dokument:</td>
<td>Security - Sicherheitsverfahren PIN/TAN</td>
</tr>
<tr>
<td>Kapitel:</td>
<td>Verfahrensbeschreibung</td>
<td>Stand:</td>
<td>Seite:</td>
</tr>
<tr>
<td>Abschnitt:</td>
<td>Abläufe beim Zwei-Schritt-Verfahren</td>
<td>23.02.2018</td>
<td>33</td>
</tr>
</table>


<table>
<tr>
<td>Schritt 3b HITAN</td>
<td>←</td>
<td>Challenge senden für weitere TAN<br>Nach Überprüfung der PIN des neuen Benutzers und Identifizie- ren des zwischengespeicherten Auftrags auf Institutsseite wird eine verfahrensspezifische Challenge ermittelt und dem Kun- denprodukt mitgeteilt. Durch Verwenden des Rückmeldungs- code 0030 - ,,Auftrag empfangen - Sicherheitsfreigabe erforder- lich" zusammen mit den Informationen „Auftragsreferenz“ und „Challenge“ aus HITAN erhält das Kundenprodukt in der Kredit- institutsantwort die Information, dass der Kunde nun auf Basis der Challenge in vereinbarter Form eine TAN ermitteln muss.</td>
</tr>
<tr>
<td>Schritt 4a HKTAN</td>
<td>→</td>
<td>weitere TAN einreichen<br>Mit dem Geschäftsvorfall HKTAN in der Belegung gemäß TAN- Prozess=2 wird die ermittelte weitere TAN zum Kreditinstitut übertragen.<br>Über die Belegung „Weitere TAN folgt" = ,N" wird signalisiert, dass dies die letzte TAN zu dem eingereichten Auftrag war. An- derenfalls werden zu einem späteren Zeitpunkt von einem wei- teren Benutzer die Schritte 3 und 4 in gleicher Weise nochmals durchgeführt.</td>
</tr>
<tr>
<td>Schritt 4b z. B. HIRMS zu HKCCS, HITAN</td>
<td>←</td>
<td>Rückmeldungen senden<br>Falls keine weitere TAN mehr folgt, werden mit der Kreditinsti- tutsantwort zum eigentlichen Auftrag ggf. erzeugte Antwortseg- mente, sowie die Rückmeldungen zum Auftrag selbst und zur TAN-Verifikation zum Kundenprodukt gesendet. Die Nachricht enthält auch ein Segment HITAN in der Belegung gemäß TAN- Prozess=2 als Beantwortung des HKTAN.</td>
</tr>
</table>


## B.4.3 Abläufe bei der Initialisierung mit starker Kundenauthentifizierung

Durch [MaSI] und [PSD2] besteht die Forderung nach einer starken Kundenauthen-
tifizierung u. a. beim Zugriff auf Kontendaten, also auch zum Zeitpunkt der FinTS-
Dialoginitialisierung. Hierfür wurden Abläufe geschaffen, die eine Umsetzung der
starken Kundenauthentifizierung bei TAN-Verfahren ermöglichen.

Hierzu wird in die Segmentfolge der Dialoginitialisierung durch das Kundenprodukt
unmittelbar nach dem Segment Verarbeitungsvorbereitung (HKVVB) ein
HKTAN-Segment mindestens der Segmentversion #6 eingestellt.


Damit ergibt sich für die Dialoginitialisierung bei starker Authentifizierung folgende
Segmentfolge:

![HNHBK Nachrichtenkopf / -abschluss HNHBS HNSHK Signaturkopf / -abschluss HNSHA PIN HKIDN HKVVB HKTAN TP=4](figures/33.1)


<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: B</td>
<td>Version: 3.0-FV</td>
<td>Financial Transaction Services (FinTS) Dokument: Security - Sicherheitsverfahren PIN/TAN</td>
</tr>
<tr>
<td>Seite:<br>34</td>
<td>Stand: 23.02.2018</td>
<td>Kapitel: Verfahrensbeschreibung<br>Abschnitt: Abläufe beim Zwei-Schritt-Verfahren</td>
</tr>
</table>


## B.4.3.1Rahmenbedingungen für den Einsatz der starken Kundenauthentifizierung

· Voraussetzung für die Verwendung der starken Kundenauthentifizierung ist,
dass ein Kundenprodukt bereits vor der Dialoginitialisierung die Sicherheits-
verfahren und Parameter kennt. Daher muss ein Kreditinstitut das Abholen
der BPD über einen anonymen Dialog zulassen, wenn es starke Authentifi-
zierung verwenden möchte.

· Sind dem Kundenprodukt die konkreten, für den Benutzer zugelassenen Si-
cherheitsverfahren nicht bekannt, so können diese über eine Dialoginitialisie-
rung mit Sicherheitsfunktion=999 angefordert werden. Die konkreten
Verfahren werden dann über den Rückmeldungscode=3920 zurückgemel-
det. Im Rahmen dieses Prozesses darf keine UPD zurückgeliefert werden
und die Durchführung anderer Geschäftsvorfälle ist in einem solchen Dialog
nicht erlaubt.

· Bei Einsatz der Prozessvariante 1 wird auf die Verwendung des Elements
Auftrags-Hashwert verzichtet, da die relevanten Daten sich bereits in der
Dialoginitialisierungsnachricht befinden. Da der Auftrags-Hashwert bei Pro-
zessvariante 1 belegt werden muss, wird ein FinTS-Füllwert verwendet, der
von der Gegenseite nicht geprüft wird. Dies gilt auch bei Verwendung von
PIN/TAN-Management-Geschäftsvorfällen.

· Basis für eine starke Authentifizierung ist die Verwendung des HKTAN ab der
Segmentversion #6. Ab dieser Segmentversion ist es möglich, ein HKTAN-
Segment in die Segmentfolge der Dialoginitialisierung zu integrieren.

. Bei Verwendung von chipTAN ist bei HHD V1.3.2 die Challenge-Klasse 02
(Anmelde-TAN) zu verwenden. Bei HHD V1.4 gilt die Schablone 01 bzw. 02
(Legitimation Kunde mit einem Authentifizierungsmerkmal). Die Aus-
wahl der Schablone 01 bzw. 02 wird durch das Kreditinstitut getroffen und ist
Inhalt des Start-Code im Schritt 2a in den Abläufen. Das Authentifizie-
rungsmerkmal wird durch das Kreditinstitut festgelegt und mit dem Benut-
zer vereinbart. Bei Prozessvariante 1 ist das Element Challengeklasse
des HKTAN mit dem festen FinTS-Füllwert 99 zu belegen, der im Kreditinsti-
tut ignoriert wird. Das Element Challenge-Parameter bleibt leer.

· Nach Bestätigung der eingereichten TAN mit HITAN ab #6 findet ein stan-
dardmäßiger FinTS-Dialog statt, in dem TAN-pflichtige und nicht-TAN-
pflichtige Aufträge ausgeführt werden können. Der Dialog muss durch das
Kundenprodukt mit einer Dialogendenachricht (HKEND) geschlossen werden.

• Migration: Durch die Unterstützung des HKTAN ab Segmentversion #6 in den
BPD signalisiert das Kreditinstitut die Fähigkeit zur Durchführung einer star-
ken Kundenauthentifizierung. Enthält die Segmentfolge der Dialoginitialisie-
rung kein HKTAN-Segment, so handelt es sich um eine schwache Authenti-
fizierung. Diese kann - solange zulässig - parallel zur starken Kun-
denauthentifizierung unterstützt werden. Durch Verwendung des Rückmel-
dungscode 3075 ,,Starke Authentifizierung ab dem ... erfor-
derlich" kann ein Benutzer auf den Wegfall der schwachen Authentifizie-
rung hingewiesen werden. Nach Ablauf dieser Frist kann eine Dialoginitiali-
sierung ohne starke Kundenauthentifizierung durch den Rückmeldungscode
9075 „Starke Authentifizierung erforderlich" abgewiesen
werden.

<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th rowspan="2">Version: 3.0-FV</th>
<th rowspan="2">Kapitel: B</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Security - Sicherheitsverfahren PIN/TAN</td>
</tr>
<tr>
<td>Kapitel: Abschnitt:</td>
<td>Verfahrensbeschreibung Abläufe beim Zwei-Schritt-Verfahren</td>
<td>Stand: 23.02.2018</td>
<td>Seite: 35</td>
</tr>
</table>


. Auch im Rahmen einer Eroffnung eines anonymen Dialogs muss ein Kun-
denprodukt, das die starke Kundenauthentifizierung unterstützt, in die Dia-
loginitialisierungsnachricht ein Segment HKTAN ab Segmentversion #6 ein-
stellen. Auf diese Weise ist eine Signalisierung der SCA-Fähigkeit möglich
und dem Kundensystem können in der Antwort bei Bedarf geeignete BPD
übermittelt werden, wenn das Kreditinstitut dies unterstützt.


![](figures/35.1)


![](figures/35.2)


Unterstützt ein Kreditinstitut die starke Kundenauthentifizierung
mithilfe von HKTAN ab #6, so sollte ein Kundenprodukt in die
Segmentfolge der Dialoginitialisierung grundlegend ein HKTAN-
Segment ab #6 einstellen, um ggf. einen Rückmeldungscode 3075
bzw. 9075 zu vermeiden.

Das Kreditinstitut muss anhand der in den PSD2 Regularien be-
schriebenen Ausnahmen festlegen, ob eine starke Kundenauthen-
tifizierung nötig ist (nur dann erfolgt der nächste Schritt des Zwei-
Schritt-Verfahrens) oder ob die Dialoginitialisierung in der Antwort-
nachricht unmittelbar beantwortet werden kann.

Das Kundenprodukt steuert also nicht, ob es sich um eine starke
oder schwache Authentifizierung handelt.

Im Rahmen der PIN/TAN-Management-Geschäftsvorfälle (vgl. Kapitel C.3) ist in be-
stimmten Situationen eine Einreichung ohne starke Kundenauthentifizierung erfor-
derlich (Authentifizierungsklasse 4, vgl. Kapitel B.3). Daher wird in einem solchen
Fall das Element Segmentkennung in HKTAN ab #6 mit der Segmentkennung des
jeweiligen Geschäftsvorfalls belegt, der dann isoliert in diesem Dialog eingereicht
wird.


<table>
<tr>
<td>Bezeichnung</td>
<td>Segmentkennung</td>
</tr>
<tr>
<td>PIN-Änderung</td>
<td>HKPAE</td>
</tr>
<tr>
<td>PIN-Sperre aufheben</td>
<td>HKPSA</td>
</tr>
<tr>
<td>PIN Sperren</td>
<td>HKPSP</td>
</tr>
<tr>
<td>Anzeige der verfügbaren TAN-Medien</td>
<td>HKTAB</td>
</tr>
<tr>
<td>TAN-Generator an- bzw. ummelden</td>
<td>HKTAU</td>
</tr>
<tr>
<td>TAN-Generator Synchronisierung</td>
<td>HKTSY</td>
</tr>
<tr>
<td>Mobilfunkverbindung registrieren</td>
<td>HKMTR / HKMTS</td>
</tr>
<tr>
<td>Mobilfunkverbindung freischalten</td>
<td>HKMTF</td>
</tr>
<tr>
<td>Mobilfunkverbindung ändern</td>
<td>HKMTA</td>
</tr>
<tr>
<td>Deaktivieren / Löschen von TAN-Medien</td>
<td>HKTML</td>
</tr>
</table>


In den nächsten Abschnitten sind die Rahmenbedingungen für repräsentative Pro-
zesse solcher PIN/TAN-Management Geschäftsvorfälle beschrieben.


## B.4.3.1.1 Rahmenbedingungen bei Erst-PIN-Änderung (HKPAE)

Die folgenden Schritte gelten für die Einreichung einer Erst-PIN-Änderung, die
ohne starke Kundenauthentifizierung erfolgt. Ggf. wurde ein zuvor durchgeführ-
ter Anmeldeversuch durch einen Rückmeldungscode 3916 (z. B. ,PIN muss
wegen erstmaliger Anmeldung zwangsweise geändert werden“) beantwortet.

<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: B</td>
<td>Version: 3.0-FV</td>
<td>Financial Transaction Services (FinTS) Dokument: Security - Sicherheitsverfahren PIN/TAN</td>
</tr>
<tr>
<td>Seite:<br>36</td>
<td>Stand: 23.02.2018</td>
<td>Kapitel: Verfahrensbeschreibung<br>Abschnitt: Abläufe beim Zwei-Schritt-Verfahren</td>
</tr>
</table>


. Erster Dialog - Ermitteln TAN-Verfahren

○ Zunächst wird ein Dialog mit der Signaturfunktion=999 (Ein-
Schritt-Verfahren) ohne integriertes HKTAN-Segment eröffnet.

○ Die Dialoginitialisierungsantwort enthält über den Rückmeldungscode
3920 die für den Benutzer zugelassenen TAN-Verfahren. Die Ant-
wort darf keine UPD enthalten, da noch keine starke Kundenauthenti-
fizierung vorliegt.

o Anschließend hat das Kundensystem den Dialog durch Senden einer
Dialogendenachricht (HKEND) zu beenden.

• Zweiter Dialog – PIN-Einreichung und Authentifizierung durch eine TAN2

o Anschließend wird in Prozessvariante 1 bzw. 2 (vgl. hierzu die Abläu-
fe in Kapitel B.4.3.2 bzw. B.4.3.3) unter Verwendung eines zugelas-
senen TAN-Verfahrens (diese wurden im ersten Dialog mit Rückmel-
dungscode 3920 zurück gemeldet) ein zweiter Dialog mit integrier-
tem HKTAN-Segment eröffnet, um die PIN-Änderung durchzuführen.
Das Datenelement Segmentkennung in HKTAN wird mit dem Wert
HKPAE belegt, um zu signalisieren, dass es sich um eine PIN-
Änderung handelt.

○ Hinweis: Ist die zur Durchführung des TAN-Prozesses benötigte Be-
zeichnung des TAN-Mediums noch nicht bekannt, so muss zuvor
der hierfür vorgesehene Ablauf (vgl. Abschnitt B.4.3.1.3) in einem
separaten Dialog durchgeführt werden. Erst dann kann der Dialog mit
der PIN-Änderung erfolgen.

o Nach erfolgter Dialoginitialisierungsantwort wird in einem nächsten
Schritt durch das Kundensystem der Geschäftsvorfall PIN Ändern
(HKPAE) eingereicht.

o Das Institut muss in der Antwort durch den Rückmeldungscode 0030
eine TAN zur Authentifizierung anfordern. Nach Eingabe der TAN
durch den Benutzer wird diese durch das Kundensystem eingereicht.

○ Unmittelbar nach Bestätigung der eingereichten TAN muss der Dia-
log durch das Kundensystem mit einer Dialogendenachricht (HKEND)
geschlossen werden. Um Auftragsnachrichten zu schicken, kann das
Kundenprodukt anschließend eine neue Dialoginitialisierung mit inte-
griertem HKTAN-Segment für diesen Benutzer senden.


### B.4.3.1.2 Rahmenbedingungen bei Zwangs-PIN-Änderung (HKPAE)

Die folgenden Schritte gelten für die Einreichung einer Zwangs-PIN-Änderung.

· Erster Dialog – Auslöser: Dialog mit fehlerhafter PIN

○ Auslöser ist ein Dialog mit wiederholt eingegebener fehlerhafter PIN.
Das verwendete Sicherheitsverfahren ist dafür unerheblich.

<!-- PageFooter: 2 Das Senden einer TAN mit dem Geschäftsvorfall HKPAE ist mit Einführung der starken Kun- denauthentifizierung obligatorisch, da durch die PSD2 für das Ändern des Wissenselementes eine starke Kundenauthentifizierung erforderlich ist. -->
<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th rowspan="2">Version: 3.0-FV</th>
<th rowspan="2">Kapitel: B</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Security - Sicherheitsverfahren PIN/TAN</td>
</tr>
<tr>
<td>Kapitel:<br>Abschnitt:</td>
<td>Verfahrensbeschreibung Abläufe beim Zwei-Schritt-Verfahren</td>
<td>Stand: 23.02.2018</td>
<td>Seite: 37</td>
</tr>
</table>


o Das Institut antwortet in diesem Fall mit einem Rückmeldungscode
3916 (z. B. ,PIN muss wegen zu vieler Fehlversuche zwangsweise
geändert werden“). Es wird davon ausgegangen, dass dem Kunden-
system die für den Benutzer zugelassenen TAN-Verfahren bekannt
sind bzw. diese der Kreditinstitutsantwort (Rückmeldungscode 3920)
entnommen werden. Die Antwort darf keine UPD enthalten, da durch
Fehlen des Wissenselementes keine starke Kundenauthentifizierung
vorliegt.

o Anschließend hat das Kundensystem den Dialog durch Senden einer
Dialogendenachricht (HKEND) zu beenden.

· Zweiter Dialog – PIN-Änderung und Authentifizierung durch eine TAN3

o Anschließend wird in Prozessvariante 1 bzw. 2 (vgl. hierzu die Abläu-
fe in Kapitel B.4.3.2 bzw. B.4.3.3) unter Verwendung eines zugelas-
senen TAN-Verfahrens ein zweiter Dialog mit integriertem HKTAN-
Segment eröffnet, um die PIN-Änderung durchzuführen. Das Daten-
element Segmentkennung in HKTAN wird mit dem Wert HKPAE be-
legt, um zu signalisieren, dass es sich um eine PIN-Änderung han-
delt.

○ Hinweis: Ist die zur Durchführung des TAN-Prozesses benötigte Be-
zeichnung des TAN-Mediums noch nicht bekannt, so muss zuvor
der hierfür vorgesehene Ablauf (vgl. Abschnitt B.4.3.1.3) in einem
separaten Dialog durchgeführt werden. Erst dann kann der Dialog mit
der PIN-Änderung durchgeführt werden.

o Nach erfolgter Dialoginitialisierungsantwort wird in einem nächsten
Schritt durch das Kundensystem der Geschäftsvorfall PIN Ändern
(HKPAE) eingereicht.

o Das Institut muss in der Antwort durch den Rückmeldungscode 0030
eine TAN zur Authentifizierung anfordern. Nach Eingabe der TAN
durch den Benutzer wird diese durch das Kundensystem eingereicht.

○ Unmittelbar nach Bestätigung der eingereichten TAN muss der Dia-
log durch das Kundensystem mit einer Dialogendenachricht (HKEND)
geschlossen werden. Um Auftragsnachrichten zu schicken, kann das
Kundenprodukt anschließend eine neue Dialoginitialisierung mit inte-
griertem HKTAN-Segment für diesen Benutzer senden.


## B.4.3.1.3 Rahmenbedingungen zur Ermittlung möglicher TAN-Medien-Kennungen (HKTAB)

Beim Erstzugang mit einem neuen TAN-Verfahren liegt einem Kundenprodukt
ggf. noch keine TAN-Medien-Bezeichnung für dieses Verfahren vor. In diesem
Fall muss der Geschäftsvorfall Anzeige der verfügbaren TAN-Medien
(HKTAB) ohne starke Kundenauthentifizierung durchführbar sein. Dies ist bei
der Prüfung der Kriterien im Kreditinstitut zu berücksichtigen.

. Erster Dialog - Ermitteln der TAN-Medien-Bezeichnung

<!-- PageFooter: 3 3 Das Senden einer TAN mit dem Geschäftsvorfall HKPAE ist mit Einführung der starken Kun- denauthentifizierung obligatorisch, da durch die PSD2 für das Ändern des Wissenselementes eine starke Kundenauthentifizierung erforderlich ist. -->
<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: B</td>
<td>Version: 3.0-FV</td>
<td>Financial Transaction Services (FinTS) Dokument: Security - Sicherheitsverfahren PIN/TAN</td>
</tr>
<tr>
<td>Seite:<br>38</td>
<td>Stand: 23.02.2018</td>
<td>Kapitel: Verfahrensbeschreibung<br>Abschnitt: Abläufe beim Zwei-Schritt-Verfahren</td>
</tr>
</table>


o Es wird eine Dialoginitialisierung in Prozessvariante 1 bzw. 2 durch-
geführt (vgl. hierzu die Abläufe in Kapitel B.4.3.2 bzw. B.4.3.3). In das
DE Segmentkennung in HKTAN wird der Wert HKTAB eingestellt.
Der vom Kundenprodukt hier als Füllwert gelieferte Inhalt des
Elementes Bezeichnung des TAN-Mediums in HKTAN ist vom
Kreditinstitut in dieser Situation zu ignorieren.

o Das Kreditinstitut liefert nach erfolgreicher PIN-Prüfung in HITAB die
für den Benutzer eingereichten TAN-Medien und mit dem Rückmel-
dungscode 3920 die zugelassenen TAN-Verfahren für den Benutzer
zurück (falls diese dem Kundensystem noch nicht bekannt waren)

o Anschließend hat das Kundensystem den Dialog durch Senden einer
Dialogendenachricht (HKEND) zu beenden.

• Zweiter Dialog - Starke Kundenauthentifizierung

o Nun wird unter Verwendung eines zugelassenen TAN-Verfahrens
und TAN-Mediums ein zweiter Dialog zum Durchführen einer starken
Kundenauthentifizierung eröffnet. Die SCA ist obligatorisch, da es
sich um die erste Nutzung dieses TAN-Verfahrens inkl. des gewähl-
ten TAN-Mediums handelt.

o Im Rahmen dieses Dialoges können nach erfolgreicher Durchführung
der starken Kundenauthentifizierung beliebige Geschäftsvorfälle
durchgeführt werden.


## B.4.3.1.4 Rahmenbedingungen zur Synchronisation von TAN-Generatoren (HKTSY)

Bei mehrfacher Eingabe einer falschen TAN wird bei chipTAN zunächst davon
ausgegangen, dass der TAN-Generator nicht synchronisiert ist, bevor eine TAN-
Sperre gesetzt wird. In diesem Fall muss für den Benutzer der nicht-TAN-
pflichtige Geschäftsvorfall TAN-Generator synchronisieren (HKTSY)
ohne starke Kundenauthentifizierung durchführbar sein, um eine TAN mit dem
zugehörigen aktuellen ATC einzureichen. Dies ist bei der Prüfung der Kriterien
im Kreditinstitut zu berücksichtigen.

· Es wird eine Dialoginitialisierung in Prozessvariante 1 bzw. 2 durchgeführt
(vgl. hierzu die Abläufe in Kapitel B.4.3.2 bzw. B.4.3.3). Als Segmentken-
nung in HKTAN wird der Wert HKTSY eingestellt.

. Das Kreditinstitut fordert nach erfolgreicher PIN-Prüfung den Benutzer mit
dem Rückmeldungscode 3931 auf, den Geschäftsvorfall HKTSY für eine ex-
plizite Synchronisation des TAN-Generators auszuführen.

. Unmittelbar nach erfolgreicher Verifizierung von TAN und ATC muss der
Dialog durch das Kundenprodukt durch eine Dialogendenachricht (HKEND)
geschlossen werden.


## B.4.3.2Initialisierung bei Prozessvariante 1

Der vollständige Ablauf sieht bei einer Initialisierung nach Prozessvariante 1 fol-
gendermaßen aus:

<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th rowspan="2">Version: 3.0-FV</th>
<th rowspan="2">Kapitel: B</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Security - Sicherheitsverfahren PIN/TAN</td>
</tr>
<tr>
<td>Kapitel:</td>
<td>Verfahrensbeschreibung</td>
<td>Stand:</td>
<td>Seite:</td>
</tr>
<tr>
<td>Abschnitt:</td>
<td>Abläufe beim Zwei-Schritt-Verfahren</td>
<td>23.02.2018</td>
<td>39</td>
</tr>
</table>


## Initialisierung bei Prozessvariante 1

Ausgangszustand:

. Vor dem allerersten Dialog mit dem Kreditinstitut bzw. falls die Informationen
nicht vorliegen: Das Kundenprodukt hat über einen anonymen Dialog die aktu-
ellen BPD abgeholt und ist somit in Kenntnis aller vom Kreditinstitut unterstütz-
ten Sicherheitsverfahren und Parameter.

. Vor dem allerersten Dialog mit dem Kreditinstitut bzw. falls die Informationen
nicht vorliegen: Mit der Durchführung eines personalisierten Dialogs mit der
Sicherheitsfunktion 999 erhält das Kundenprodukt mit dem Rückmeldungs-
code 3920 alle für den Benutzer zugelassenen Ein- und Zwei-Schritt-
Verfahren mitgeteilt. Eine UPD liegt zu diesem Zeitpunkt noch nicht vor. Dieser
Dialog wird durch das Kundensystem mit einer Dialogendenachricht (HKEND)
beendet.

· Der Benutzer wählt durch entsprechende Belegung des DE Sicherheits-
funktion, kodiert ein konkretes Zwei-Schritt-Verfahren für den gesamten
zweiten Dialog.

. Der Benutzer hat das Auftrags-Hashwertverfahren=1 (RIPEMD-160)
gewählt. Dies gilt für nachfolgende TAN-pflichtige Auftragsnachrichten, nicht
für die Dialoginitialisierung.


<table>
<tr>
<td>Schritt 1a HKIDN, HKVVB, HKTAN</td>
<td>→</td>
<td>Initialisierung starten<br>Es wird die Segmentfolge der Dialoginitialisierung eingereicht. Es wird der Geschäftsvorfall ab HKTAN#6 unmittelbar nach HKVVB mit der Belegung gemäß TAN-Prozess=1eingestellt. Das Element Auftrags-Hashwert ist mit dem FinTS-Füllwert binär '00000000' zu belegen. Das Datenelement Segmentken- nung des HKTAN enthält den Wert HKIDN zur Kennzeichnung, dass es sich um eine starke Authentifizierung handelt. Ggf. kann das DE Segmentkennung des HKTAN auch die Segment- kennung eines PIN/TAN-Management-Geschäftsvorfalls enthal- ten. Über die Belegung Weitere TAN folgt = N wird signa- lisiert, dass dies die einzige TAN ist.<br>Durch eine Prüfung der eingereichten Daten, im Speziellen der Benutzerkennung und der PIN, gegen die PSD2 Ausnahmen legt das Kreditinstitut fest, wie weiter vorgegangen werden soll:<br>· starke Kundenauthentifizierung erforderlich, angezeigt durch den Rückmeldungscode 0030 Auftrag emp- fangen - Sicherheitsfreigabe erforderlich (→weiter mit Schritt 1b)<br>. der Faktor Wissen ist ausreichend, angezeigt durch den Rückmeldungscode 3076 Keine starke Authen- tifizierung erforderlich (→weiter mit Schritt 2b, Fall (A)).</td>
</tr>
<tr>
<td>Schritt 1b HITAN</td>
<td>←</td>
<td>Challenge senden<br>Es wird eine verfahrensspezifische Challenge ermittelt und dem Kundenprodukt in HITAN mitgeteilt. Durch den RM-Code 0030 zusammen mit den Elementen Auftrags-Hashwert (fester</td>
</tr>
<tr>
<td>Kapitel: B</td>
<td>Version: 3.0-FV</td>
<td>Financial Transaction Services (FinTS) Dokument: Security - Sicherheitsverfahren PIN/TAN</td>
</tr>
<tr>
<td>Seite: 40</td>
<td>Stand: 23.02.2018</td>
<td>Kapitel: Verfahrensbeschreibung<br>Abschnitt: Abläufe beim Zwei-Schritt-Verfahren</td>
</tr>
</table>


<table>
<tr>
<td></td>
<td></td>
<td>FinTS-Füllwert = binär '00000000') und Challenge aus HITAN erhält das Kundenprodukt in der Kreditinstitutsantwort die In- formation, dass der Kunde nun auf Basis der Challenge in ver- einbarter Form eine Anmelde-TAN ermitteln muss.</td>
</tr>
<tr>
<td>Schritt 2a HKTAN</td>
<td>→</td>
<td>Anmelde-TAN einreichen<br>Zusammen mit dem eigentlichen Geschäftsvorfall, in diesem Fall HKTAN mit Belegung gemäß TAN-Prozess=1, wird die er- mittelte TAN (im Signaturabschluss) zum Kreditinstitut übertra- gen. Nach erfolgreicher TAN-Verifikation kann die erfolgreiche Prüfung auf starke Kundenauthentifizierung bestätigt werden.</td>
</tr>
<tr>
<td>Schritt 2b HITAN, ggf. HIBPD, HIUPD, HIRMS</td>
<td>←</td>
<td>BPD, UPD und Rückmeldungen senden (A) Ohne starke Kundenauthentifizierung:<br>Mit der Kreditinstitutsantwort werden ggf. erzeugte BPD und UPD, sowie die Rückmeldungen zum Kundenprodukt gesendet. Die Nachricht enthält auch ein Segment HITAN mit TAN- Prozess=1 als Beantwortung des HKTAN.<br>(B) Bei starker Kundenauthentifizierung<br>Mit der Kreditinstitutsantwort werden ggf. erzeugte BPD und UPD, sowie die Rückmeldungen zur PIN-Prüfung und zur TAN- Verifikation zum Kundenprodukt gesendet. Die Nachricht enthält auch ein Segment HITAN mit TAN-Prozess=1 als Beantwortung des HKTAN.</td>
</tr>
</table>


## B.4.3.3Initialisierung bei Prozessvariante 2

Der vollständige Ablauf sieht bei einer Initialisierung nach Prozessvariante 2 folgen-
dermaßen aus:


### Initialisierung bei Prozessvariante 2

Ausgangszustand:

. Vor dem allerersten Dialog mit dem Kreditinstitut bzw. falls die Informationen
nicht vorliegen: Das Kundenprodukt hat über einen anonymen Dialog die aktu-
ellen BPD abgeholt und ist somit in Kenntnis aller vom Kreditinstitut unterstütz-
ten Sicherheitsverfahren und Parameter.

. Vor dem allerersten Dialog mit dem Kreditinstitut bzw. falls die Informationen
nicht vorliegen: Mit der Durchführung eines personalisierten Dialogs mit der
Sicherheitsfunktion 999 erhält das Kundenprodukt mit dem Rückmeldungs-
code 3920 alle für den Benutzer zugelassenen Ein- und Zwei-Schritt-
Verfahren mitgeteilt. Eine UPD liegt zu diesem Zeitpunkt noch nicht vor. Dieser
Dialog wird durch das Kundensystem mit einer Dialogendenachricht (HKEND)
beendet.

· Der Benutzer wählt durch entsprechende Belegung des DE Sicherheits-
funktion, kodiert ein konkretes Zwei-Schritt-Verfahren für den gesamten
zweiten Dialog und legt die Prozessvariante 2 für den gesamten Ablauf fest.


<table>
<tr>
<td>Schritt 1a HKIDN, HKVVB,</td>
<td>→</td>
<td>Initialisierung starten Es wird die Segmentfolge der Dialoginitialisierung eingereicht. Die Nachricht enthält unmittelbar nach HKVVB zusätzlich das</td>
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
<td>Dokument:</td>
<td>Security - Sicherheitsverfahren PIN/TAN</td>
</tr>
<tr>
<td>Kapitel:</td>
<td>Verfahrensbeschreibung</td>
<td>Stand:</td>
<td>Seite:</td>
</tr>
<tr>
<td>Abschnitt:</td>
<td>Abläufe beim Zwei-Schritt-Verfahren</td>
<td>23.02.2018</td>
<td>41</td>
</tr>
</table>


<table>
<tr>
<td>HKTAN</td>
<td></td>
<td>Segment ab HKTAN#6 mit der Belegung gemäß TAN- Prozess=4. Das Datenelement Segmentkennung in HKTAN enthält den Wert HKIDN zur Kennzeichnung, dass es sich um eine starke Kundenauthentifizierung handelt. Ggf. kann das DE Segmentkennung des HKTAN auch die Segmentkennung eines PIN/TAN-Management-Geschäftsvorfalls enthalten. Der Signa- turabschluss enthält die PIN des Benutzers aber keine TAN.<br>Durch eine Prüfung der eingereichten Daten, im Speziellen der Benutzerkennung und der PIN, gegen die PSD2 Ausnahmen legt das Kreditinstitut fest, wie weiter vorgegangen werden soll:<br>. starke Kundenauthentifizierung erforderlich, angezeigt durch den Rückmeldungscode 0030 Auftrag emp- fangen - Sicherheitsfreigabe erforderlich (→weiter mit Schritt 1b)<br>. der Faktor Wissen ist ausreichend, angezeigt durch den Rückmeldungscode 3076 Keine starke Authen- tifizierung erforderlich (→weiter mit Schritt 2b, Fall (A)).</td>
</tr>
<tr>
<td>Schritt 1b HITAN</td>
<td>←</td>
<td>Challenge senden<br>Es wird eine verfahrensspezifische Challenge für eine Anmelde- TAN ermittelt und dem Kundenprodukt im Segment HITAN mit- geteilt. In HITAN erfolgt die Belegung ebenfalls gemäß TAN- Prozess=4. Durch den RM-Code 0030 _zusammen mit den In- formationen Auftragsreferenz und Challenge aus HITAN erhält das Kundenprodukt in der Kreditinstitutsantwort die In- formation, dass der Kunde nun auf Basis der Challenge in ver- einbarter Form einer Anmelde-TAN ermitteln muss.</td>
</tr>
<tr>
<td>Schritt 2a HKTAN</td>
<td>→</td>
<td>TAN einreichen<br>Mit dem Geschäftsvorfall HKTAN mit der Belegung gemäß TAN- Prozess=2 wird die ermittelte TAN zusammen mit der Auf- tragsreferenz zum Kreditinstitut übermittelt. Wie beim Ein- Schritt-Verfahren enthält der Signaturkopf die Benutzerkennung und der Signaturabschluss PIN und TAN des aktiven Benutzers für diese Anmeldung. Als Rolle des Sicherheitsliefe- ranten, kodiert wird „1“ für Herausgeber (ISS) verwendet. Über die Belegung Weitere TAN folgt = N wird signali- siert, dass dies die einzige TAN zu dem eingereichten Auftrag ist. Nach erfolgreicher TAN-Verifikation kann die erfolgreiche Prüfung auf starke Kundenauthentifizierung bestätigt werden.</td>
</tr>
<tr>
<td>Schritt 2b z. B. HIRMS, HIBPD, HIUPD HITAN</td>
<td>←</td>
<td>BPD, UPD und Rückmeldungen senden<br>(A) Ohne starke Kundenauthentifizierung:<br>Mit der Kreditinstitutsantwort werden ggf. erzeugte BPD und UPD, sowie die Rückmeldungen zur Dialoginitialisierung _zum Kundenprodukt gesendet. Die Nachricht enthält auch ein Seg- ment HITAN mit TAN-Prozess=4 als Beantwortung des HKTAN aus Schritt 1a.<br>Für die Elemente Auftragsreferenz und Challenge sind</td>
</tr>
</table>


|

<!-- PageNumber: I -->
<!-- PageNumber: | -->
<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: B</td>
<td>Version: 3.0-FV</td>
<td>Financial Transaction Services (FinTS) Dokument: Security - Sicherheitsverfahren PIN/TAN</td>
</tr>
<tr>
<td>Seite:<br>42</td>
<td>Stand: 23.02.2018</td>
<td>Kapitel: Verfahrensbeschreibung<br>Abschnitt: Abläufe beim Zwei-Schritt-Verfahren</td>
</tr>
</table>


<table>
<tr>
<td></td>
<td></td>
<td>vom Kreditinstitut die festen FinTS-Füllwerte ,,noref“ und ,nochallenge“ einzustellen. Diese sind vom Kundenprodukt zu ignorieren.<br>(B) Bei starker Kundenauthentifizierung:<br>Mit der Kreditinstitutsantwort werden ggf. erzeugte BPD und UPD, sowie die Rückmeldungen zur TAN-Verifikation und zur Dialoginitialisierung selbst zum Kundenprodukt gesendet. Die Nachricht enthält auch ein Segment HITAN mit TAN-Prozess=2 als Beantwortung des HKTAN aus Schritt 2a.</td>
</tr>
</table>


## B.4.4 Allgemeine Festlegungen zum Zeitverhalten beim Zwei-Schritt-Verfahren

Bei Verwendung des Zwei-Schritt-Verfahrens wird auf Institutsseite das Zeitfenster
zwischen den beiden Prozess-Schritten überwacht, um nicht freigegebene Aufträge
nach Ablauf der Gültigkeit entsprechend kennzeichnen und die zugehörige TAN
entwerten zu können. Das Zeitfenster selbst hängt von der Implementierung auf In-
stitutsseite ab. Auch bei der Verarbeitung von synchronen bzw. zeitversetzten Mehr-
fach-TANs ergibt sich unterschiedliches Zeitverhalten, wie in den folgenden Ab-
schnitten beschrieben.


![](figures/42.1)


Das Zeitfenster für die Eingabe einer TAN im Zwei-Schritt-Verfahren
wird institutsindividuell geregelt, muss dem Kunden aber genügend
Zeit für die Eingabe der TAN lassen und sollte daher einen Wert von
8 Minuten nicht unterschreiten.

Ein oberes Limit wird nur durch die Aufbewahrungsdauer offener
Aufträge im Institut festgelegt.

Um dem Kundenprodukt eine übersichtliche Benutzerführung zu
ermöglichen kann die DEG „Gültigkeitsdatum und –uhrzeit für Chal-
lenge" belegt werden (vgl. Kapitel B.5)


## B.4.4.1Verteilung von Aufträgen auf FinTS-Nachrichten

Es können TAN-pflichtige und nicht-TAN-pflichtige Aufträge gemischt werden, wobei
über den BPD-Parameter ,,Mehr als ein TAN-pflichtiger Auftrag pro Nachricht er-
laubt“ die Anzahl der TAN-pflichtigen Aufträge geregelt wird.


![](figures/42.2)


Durch das Zeitverhalten bei TAN-pflichtigen Aufträgen im Zwei-
Schritt-Verfahren kann es zu Problemen in Kombination mit PIN-
pflichtigen Aufträgen kommen, die eine lange Verarbeitungszeit er-
fordern wie z. B. Umsatzabfragen. Dadurch kann es möglich sein,
dass die Antwortzeit der Umsatzabfrage das Zeitfenster für die Be-
reitstellung der TAN durch den Kunden so stark einschränkt, dass
ein Timeout auftritt.

Diese Situation kann vermieden werden, wenn in solchen Fällen
die Aufträge in separaten Nachrichten vorab übertragen werden
und auf die Mischung mit den TAN-pflichtigen Aufträgen verzichtet
wird.

<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th>Version:</th>
<th rowspan="2">Kapitel: B</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Security - Sicherheitsverfahren PIN/TAN</td>
<td>3.0-FV</td>
</tr>
<tr>
<td>Kapitel:<br>Abschnitt:</td>
<td>Verfahrensbeschreibung<br>Geschäftsvorfall HKTAN für Zwei-Schritt-TAN-Einreichung</td>
<td>Stand: 23.02.2018</td>
<td>Seite: 43</td>
</tr>
</table>


## B.4.4.2Zeitüberwachung beim Zwei-Schritt-Verfahren bei Einfach-TANs

Die Eingabe einer TAN im Zwei-Schritt-Verfahren wird auf Institutsseite durch Timer
überwacht, d. h. nach Übermittlung der Challenge bleibt dem Kunden nur ein be-
stimmtes Zeitfenster, um die TAN einzureichen. Ein Ausbleiben der TAN wird als
fehlerhafter Versuch gewertet und die TAN wird als ungültig markiert. Dies wird bei
der Auftragsantwort im jeweiligen TAN-Prozess-Schritt über den Rückmeldecode
9951 – ,Zeitüberschreitung im Zwei-Schritt-Verfahren – TAN ungültig“ signalisiert.

Diese Zeitüberwachung gilt bei jeder Einreichung einer TAN im Zwei-Schritt-
Verfahren, also auch, wenn - ggf. über HKTAN eingeleitet – nachträglich zusätzlich
benötigte TANs eingereicht werden.


## B.4.4.2.1 Zeitüberwachung beim Zwei-Schritt-Verfahren bei Mehrfach-TANs

Bei der Verwendung von Mehrfach-TANs gelten für synchrone und zeitversetzte
Einreichung unterschiedliche Festlegungen für die Zeitüberwachung.


## B.4.4.2.2 Zeitüberwachung bei synchroner Eingabe von Mehrfach-TANs

Die Überwachung bei synchroner Eingabe von Mehrfach-TANs entspricht der Be-
handlung von Einfach-TANs, wobei die Zeitüberwachung auf Institutsseite so ge-
staltet sein muss, dass den Benutzern ein genügend großes Zeitfenster für die Ein-
reichung der TANs bleibt.


## B.4.4.2.3 Zeitüberwachung bei zeitversetzter Eingabe von Mehrfach-TANs

Die maximale Dauer, die ein eingereichter Auftrag für die Übermittlung weiterer
TANs aufbewahrt wird, unterliegt bei zeitversetzter Einreichung einer separaten
Zeitüberwachung für jeden Benutzer. Wird dieses Zeitfenster überschritten und der
Auftrag wurde inzwischen auf Institutsseite gelöscht, so wird dies in der Auftragsan-
twort HITAN über die Rückmeldecodes 9210 ,Auftrag abgelehnt - Kein eingereich-
ter Auftrag gefunden" bzw. 9210 - ,Auftragsreferenz ist unbekannt" signalisiert (vgl.
Kapitel B.6.1).


![](figures/43.1)


Die Aufbewahrungsdauer von Aufträgen mit Mehrfach-TANs bei
zeitversetzter Eingabe entspricht den Regelungen bei FinTS Sta-
tusprotokollen (vgl. [Formals] Kapitel C.7), kann institutsindividuell
jedoch auch bis zu einem Jahr betragen.


## B.5 Geschäftsvorfall HKTAN für Zwei-Schritt-TAN-Einreichung

Dieser Geschäftsvorfall dient im Zwei-Schritt-Verfahren dazu, eine Challenge zur
TAN-Bildung anzufordern und eine TAN zu einem Auftrag zu übermitteln. Hierfür
existieren zwei Prozessvarianten, deren Funktion im Kapitel B.4 genau beschrieben
ist.


![](figures/43.2)


Der Geschäftsvorfall HKTAN nimmt in FinTS eine Sonderrolle ein:
HKTAN muss in BPD, UPD und HIPINS (Parameter ,,TAN erfor-
derlich“ = „n“) wie ein Geschäftsvorfall aufgeführt werden und be-
sitzt mit HITANS auch Geschäftsvorfallparameter. Als Sonderbe-
dingung wird HKTAN jedoch wie ein administratives Segment bei


![](figures/43.3)


<!-- PageBreak -->


<table>
<tr>
<th>Kapitel: B</th>
<th>Version: 3.0-FV</th>
<th>Financial Transaction Services (FinTS) Dokument: Security - Sicherheitsverfahren PIN/TAN</th>
</tr>
<tr>
<td>Seite:<br>44</td>
<td>Stand: 23.02.2018</td>
<td>Kapitel: Verfahrensbeschreibung<br>Abschnitt: Geschäftsvorfall HKTAN für Zwei-Schritt-TAN-Einreichung</td>
</tr>
</table>


der Zählung im DE „Maximale Anzahl Aufträge“ pro Nachricht (vgl.
[Formals], Kapitel D.6) nicht berücksichtigt.

Durch Existenz dieses Geschäftsvorfalls HKTAN in der BPD und UPD wird grund-
sätzlich festgelegt, ob das Kreditinstitut Zwei-Schritt-Verfahren unterstützt bzw. ob
dies für den Kunden zugelassen ist. Mit Einführung der starken Kundenauthentifizie-
rung [PSD2] ist dies obligatorisch. Der Geschäftsvorfall HKTAN wird in mehreren
Segmentversionen angeboten. Ein Institut, das Zwei-Schritt-Verfahren anbieten will
muss mindestens eine dieser Segmentversionen unterstützen. Für die Unterstüt-
zung der starken Kundenauthentifizierung gemäß PSD2 wird mindestens die Seg-
mentversion #6 benötigt.

Zusammen mit der Kreditinstitutsrückmeldung können abhängig vom verwendeten
fachlichen Geschäftsvorfall auch Antwortsegmente zu diesem Auftrag
übertragen werden.


### B.5.1 Geschäftsvorfall HKTAN in Segmentversion #6

Ab der Segmentversion #6 dieses Geschäftsvorfalls wird die starke Kundenauthenti-
fizierung bei der Dialoginitialisierung durch Eingabe einer TAN unterstützt.

Mit dieser Version können aber auch andere PIN/TAN Zwei-Schritt-Verfahren - au-
Ber TAN-Listenverfahren - unterstützt werden; wahlweise können Kreditinstitute zu-
sätzlich auch die älteren Segmentversionen von HKTAN anbieten.


![](figures/44.1)


In der BPD können sich mehrere Segmentversionen von HITANS-
Segmenten befinden, wobei den einzelnen HITANS-Segmenten
über das Element „Sicherheitsfunktion, kodiert“ unterschiedliche
Verfahren zugeordnet sein können. Ein Kundenprodukt sollte - be-
ginnend mit der höchsten Segmentversion - alle in der BPD enthal-
tenen HITANS-Segmente analysieren, um so dem Kunden alle vom
Kreditinstitut unterstützten Sicherheitsverfahren anbieten zu kön-
nen.

Beispiel: Die BPD enthält Definitionen für HITANS#6 und
HITANS#5. In HITANS#6 gilt für starke Kundenauthentifizierung
analog PSD2, mit HKTAN#5 ist übergangsweise auch noch eine
Dialoginitialisierung ohne starke Authentifizierung möglich.

Realisierung Bank: verpflichtend in mindestens einer Segmentversion, falls
Geschäftsvorfälle mit PIN/TAN-Absicherung im Zwei-Schritt-
Verfahren angeboten werden. Zur Unterstützung der starken
Kundenauthentifizierung gemäß PSD2 wird mindestens Seg-
mentversion #6 benötigt.

Realisierung Kunde: optional


# a) Kundenauftrag


# Format


<table>
<tr>
<td>Name:</td>
<td>Zwei-Schritt-TAN-Einreichung</td>
</tr>
<tr>
<td>Typ:</td>
<td>Segment</td>
</tr>
<tr>
<td>Segmentart:</td>
<td>Geschäftsvorfall</td>
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
<td>Dokument:</td>
<td>Security - Sicherheitsverfahren PIN/TAN</td>
</tr>
<tr>
<td>Kapitel:<br>Abschnitt:</td>
<td>Verfahrensbeschreibung<br>Geschäftsvorfall HKTAN für Zwei-Schritt-TAN-Einreichung</td>
<td>Stand: 23.02.2018</td>
<td>Seite: 45</td>
</tr>
</table>


<table>
<tr>
<td>Kennung:</td>
<td>HKTAN</td>
</tr>
<tr>
<td>Bezugssegment:</td>
<td>-</td>
</tr>
<tr>
<td>Segmentversion:</td>
<td>6</td>
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
<td>TAN-Prozess</td>
<td>1</td>
<td>DE</td>
<td>code</td>
<td>1</td>
<td>M</td>
<td>1</td>
<td>1, 2, 3, 4</td>
</tr>
<tr>
<td>3</td>
<td>Segmentkennung</td>
<td>1</td>
<td>DE</td>
<td>an</td>
<td>..6</td>
<td>C</td>
<td>1</td>
<td>M: bei TAN-Prozess=1 M: bei TAN-Prozess=4 und starker Authentifizierung N: sonst</td>
</tr>
<tr>
<td>4</td>
<td>Kontoverbindung international Auf- traggeber</td>
<td>1</td>
<td>DEG</td>
<td>kti</td>
<td>#</td>
<td>C</td>
<td>1</td>
<td>M: bei TAN-Prozess=1 und „Auftraggeberkonto erfor- derlich"=2 und Kontover- bindung im Auftrag enthal- ten N: sonst</td>
</tr>
<tr>
<td>5</td>
<td>Auftrags-Hashwert</td>
<td>1</td>
<td>DE</td>
<td>bin</td>
<td>.256</td>
<td>C</td>
<td>1</td>
<td>M: bei Auftrags- Hashwertverfahren&lt;&gt;0 und TAN-Prozess=1 N: sonst</td>
</tr>
<tr>
<td>6</td>
<td>Auftragsreferenz</td>
<td>1</td>
<td>DE</td>
<td>an</td>
<td>.35</td>
<td>C</td>
<td>1</td>
<td>M: bei TAN-Prozess=2, 3 O: TAN-Prozess=1, 4</td>
</tr>
</table>


<!-- PageBreak -->


<table>
<tr>
<th>Kapitel: B</th>
<th>Version: 3.0-FV</th>
<th>Financial Transaction Services (FinTS) Dokument: Security - Sicherheitsverfahren PIN/TAN</th>
</tr>
<tr>
<td>Seite: 46</td>
<td>Stand: 23.02.2018</td>
<td>Kapitel: Verfahrensbeschreibung<br>Abschnitt: Geschäftsvorfall HKTAN für Zwei-Schritt-TAN-Einreichung</td>
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
<td>7</td>
<td>Weitere TAN folgt</td>
<td>1</td>
<td>DE</td>
<td>jn</td>
<td>1</td>
<td>C</td>
<td>1</td>
<td>M: bei TAN-Prozess=1, 2 N: bei TAN-Prozess=3, 4</td>
</tr>
<tr>
<td>8</td>
<td>Auftrag stornieren</td>
<td>1</td>
<td>DE</td>
<td>jn</td>
<td>1</td>
<td>C</td>
<td>1</td>
<td>O: bei TAN-Prozess=2 und ,,Auftragsstorno erlaubt“=J N: sonst</td>
</tr>
<tr>
<td>9</td>
<td>SMS- Abbuchungskonto</td>
<td>1</td>
<td>DEG</td>
<td>kti</td>
<td>#</td>
<td>C</td>
<td>1</td>
<td>M: bei TAN-Prozess=1, 3, 4 und ,,SMS- Abbuchungskonto erforder- lich“=2<br>O: sonst</td>
</tr>
<tr>
<td>10</td>
<td>Challenge-Klasse</td>
<td>1</td>
<td>DE</td>
<td>num</td>
<td>..2</td>
<td>C</td>
<td>1</td>
<td>M: bei TAN-Prozess=1 und ,Challenge-Klasse erforder- lich“=J N: sonst</td>
</tr>
<tr>
<td>11</td>
<td>Parameter Challen- ge-Klasse</td>
<td>1</td>
<td>DEG</td>
<td></td>
<td></td>
<td>C</td>
<td>1</td>
<td>O: bei TAN-Prozess=1 und ,Challenge-Klasse erforder- lich“=J N: sonst</td>
</tr>
<tr>
<td>12</td>
<td>Bezeichnung des TAN-Mediums</td>
<td>1</td>
<td>DE</td>
<td>an</td>
<td>.32</td>
<td>C</td>
<td>1</td>
<td>M: bei TAN-Prozess=1, 3, 4 und „Anzahl unterstützter aktiver TAN-Medien“ &gt; 1 und ,,Bezeichnung des TAN-Mediums erforder- lich“=2<br>O: sonst</td>
</tr>
<tr>
<td>13</td>
<td>Antwort HHD_UC</td>
<td>1</td>
<td>DEG</td>
<td></td>
<td></td>
<td>C</td>
<td>1</td>
<td>M: bei TAN-Prozess=2 und "Antwort HHD_UC erfor- derlich“=“J“ O: sonst</td>
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
<td>Dokument:</td>
<td>Security - Sicherheitsverfahren PIN/TAN</td>
</tr>
<tr>
<td>Kapitel:<br>Abschnitt:</td>
<td>Verfahrensbeschreibung<br>Geschäftsvorfall HKTAN für Zwei-Schritt-TAN-Einreichung</td>
<td>Stand: 23.02.2018</td>
<td>Seite: 47</td>
</tr>
</table>


# ◆ Belegungsrichtlinien


## Segmentkennung

Es ist die Kennung des Segmentes einzustellen, auf das sich die Challenge
bzw. dann die resultierende TAN bezieht. Dabei sind folgende Fälle zu un-
terscheiden:


<table>
<tr>
<td>Bezeichnung</td>
<td>Segment- kennung</td>
</tr>
<tr>
<td>Identifikation</td>
<td>HKIDN</td>
</tr>
<tr>
<td colspan="2">TAN-Management-Geschäftsvorfälle (siehe Abschnitt C.3):</td>
</tr>
<tr>
<td>Anzeige der verfügbaren TAN-Medien</td>
<td>HKTAB</td>
</tr>
<tr>
<td>TAN-Generator an- bzw. ummelden</td>
<td>HKTAU</td>
</tr>
<tr>
<td>TAN-Generator Synchronisierung</td>
<td>HKTSY</td>
</tr>
<tr>
<td>Mobilfunkverbindung registrieren</td>
<td>HKMTR / HKMTS</td>
</tr>
<tr>
<td>Mobilfunkverbindung freischalten</td>
<td>HKMTF</td>
</tr>
<tr>
<td>Mobilfunkverbindung ändern</td>
<td>HKMTA</td>
</tr>
<tr>
<td>Deaktivieren / Löschen von TAN-Medien</td>
<td>HKTML</td>
</tr>
</table>


## Auftragsreferenz

Als Auftragsreferenz ist derjenige Wert einzustellen, der bei der Auftragsein-
reichung im Rahmen der Kreditinstitutsrückmeldung mitgeteilt wurde.


## Parameter Challenge-Klasse

Die Parameter zur Challenge-Klasse dienen zur Übermittlung von Daten, die
bei Prozessvariante 1 im ersten Verfahrensschritt für die weitere Steuerung
benötigt werden. Die konkrete Belegung der Parameter sind den Belegungs-
richtlinien des jeweiligen Verfahrens zu entnehmen. Für die DK-Verfahren
chipTAN und mobileTAN gelten die Festlegungen in [HHD Belegung].


## Bezeichnung des TAN-Mediums

Ist in der BPD als ,,Anzahl unterstützter aktiver TAN-Medien“ ein Wert > 1
angegeben und ist der BPD-Wert für „Bezeichnung des TAN-Mediums erfor-
derlich" = 2, so muss der Kunde z. B. im Falle des mobileTAN-Verfahrens
hier die Bezeichnung seines für diesen Auftrag zu verwendenden TAN-
Mediums angeben.


## SMS-Abbuchungskonto

Ist in der BPD das Element ,,SMS-Abbuchungskonto erforderlich" mit ,2" be-
legt, so muss der Kunde z. B. im Falle des mobileTAN-Verfahrens hier das
für diesen Auftrag zu belastende SMS-Abbuchungskonto einstellen. Dieses
kann unabhängig von der Kontoverbindung des Dialogführers gewählt wer-
den.


## Antwort HHD_UC

Bei Verwendung von chipTAN-Verfahren mit bidirektionaler Kopplung wer-
den auf dem Rückkanal relevante Informationen aus dem TAN-

<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: B</td>
<td>Version: 3.0-FV</td>
<td>Financial Transaction Services (FinTS) Dokument: Security - Sicherheitsverfahren PIN/TAN</td>
</tr>
<tr>
<td>Seite:<br>48</td>
<td>Stand: 23.02.2018</td>
<td>Kapitel: Verfahrensbeschreibung<br>Abschnitt: Geschäftsvorfall HKTAN für Zwei-Schritt-TAN-Einreichung</td>
</tr>
</table>


Generierungsprozess an das Zugangsgerät übertragen. Diese können bei
Prozessvariante 2 – abhängig vom Zustand des BPD-Parameters „Antwort
HHD_UC erforderlich" - bei der TAN-Einreichung im zweiten Schritt mit
TAN-Prozess=2 zum Kreditinstitut übertragen werden. Bei Verwendung von
Prozessvariante 1 ist die Übertragung der HHD_UC-Parameter aus dem
Rückkanal nicht möglich, da dort im 2. Schritt kein HKTAN übermittelt wird.


# b) Kreditinstitutsrückmeldung


## Format


<table>
<tr>
<td>Name:</td>
<td>Zwei-Schritt-TAN-Einreichung Rückmeldung</td>
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
<td>HITAN</td>
</tr>
<tr>
<td>Bezugssegment:</td>
<td>HKTAN</td>
</tr>
<tr>
<td>Segmentversion:</td>
<td>6</td>
</tr>
<tr>
<td>Anzahl:</td>
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
<td>TAN-Prozess</td>
<td>1</td>
<td>DE</td>
<td>code</td>
<td>1</td>
<td>M</td>
<td>1</td>
<td>1, 2, 3, 4</td>
</tr>
<tr>
<td>3</td>
<td>Auftrags-Hashwert</td>
<td>1</td>
<td>DE</td>
<td>bin</td>
<td>.256</td>
<td>C</td>
<td>1</td>
<td>M: bei Auftrags- Hashwertverfahren&lt;&gt;0 und TAN-Prozess=1, N: sonst</td>
</tr>
<tr>
<td>4</td>
<td>Auftragsreferenz</td>
<td>1</td>
<td>DE</td>
<td>an</td>
<td>..35</td>
<td>C</td>
<td>1</td>
<td>M: bei TAN-Prozess=2, 3, 4 O: bei TAN-Prozess=1</td>
</tr>
<tr>
<td>5</td>
<td>Challenge</td>
<td>3</td>
<td>DE</td>
<td>an</td>
<td>.204 8</td>
<td>C</td>
<td>1</td>
<td>M: bei TAN-Prozess=1, 3, 4 O: bei TAN-Prozess=2</td>
</tr>
<tr>
<td>6</td>
<td>Challenge HHD UC</td>
<td>1</td>
<td>DE</td>
<td>bin</td>
<td>..</td>
<td>O</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>7</td>
<td>Gültigkeitsdatum und -uhrzeit für Challenge</td>
<td>1</td>
<td>DEG</td>
<td></td>
<td></td>
<td>O</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>8</td>
<td>Bezeichnung des TAN-Mediums</td>
<td>1</td>
<td>DE</td>
<td>an</td>
<td>..32</td>
<td>C</td>
<td>1</td>
<td>M: bei TAN-Prozess=1, 3, 4 und „Anzahl unterstützter aktiver TAN-Medien" nicht vorhanden O: sonst</td>
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
<td>Dokument:</td>
<td>Security - Sicherheitsverfahren PIN/TAN</td>
</tr>
<tr>
<td>Kapitel:<br>Abschnitt:</td>
<td>Verfahrensbeschreibung<br>Geschäftsvorfall HKTAN für Zwei-Schritt-TAN-Einreichung</td>
<td>Stand: 23.02.2018</td>
<td>Seite: 49</td>
</tr>
</table>


# ◆ Belegungsrichtlinien


## Auftrags-Hashwert

Es ist der in der Kundennachricht in HKTAN übermittelte Auftrags-Hashwert
unverändert einzustellen.


## Auftragsreferenz

Bei TAN-Prozess=2, 3 und 4 muss die Auftragsreferenz vom Institut immer
eingestellt werden. Bei TAN-Prozess=1 muss die Auftragsreferenz einge-
stellt werden, wenn sie zuvor im Segment HKTAN vom Kunden gesendet
wurde. Wird im Rahmen der starken Kundenauthentifizierung keine TAN be-
nötigt und ein „Dummy-HITANS“ geschickt, enthält die Auftragsreferenz den
fest definierten FinTS-Füllwert ,,noref“.


## Challenge

Obwohl die Challenge bei Prozessvariante 2 im zweiten Schritt nicht zwin-
gend benötigt wird, sollte sie aus Integritätsgründen trotzdem übertragen
werden. Wird im Rahmen der starken Kundenauthentifizierung keine TAN
benötigt und ein „Dummy-HITANS“ geschickt, enthält die Challenge einen
FinTS-Füllwert, z. B. „nochallenge“.


![](figures/49.1)


Das Kundenprodukt muss den Inhalt der empfangenen Challenge
dem Kunden unverändert anzeigen. Ist der BPD-Parameter ,,Chal-
lenge strukturiert“ mit ,,J“ belegt, so können im DE Challenge For-
matsteuerzeichen enthalten sein, die dann entsprechend zu inter-
pretieren sind (Näheres hierzu im Data Dictionary unter dem DE
„Challenge“).

Erläuterung: Die Challenge kann institutsindividuell aufgebaut wer-
den (z. B. 1 oder 2 Eingabefelder für den chipTAN-Leser).


## Challenge HHD_UC

Das Datenelement enthält eine Datenstruktur, die entsprechend den Vorga-
ben aus [HHD-Erweiterung] aufgebaut sein muss. Die einzelnen Elemente
dieser Datenstruktur sind für FinTS transparent und werden nicht durch
Trennzeichen getrennt.


## Bezeichnung des TAN-Mediums

Ist in der BPD der Parameter „Anzahl unterstützter aktiver TAN-Medien"
nicht vorhanden, so muss das Institut dem Kunden hier mitteilen, welches
TAN-Medium er z. B. beim mobileTAN-Verfahren verwenden soll.

<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: B</td>
<td>Version: 3.0-FV</td>
<td>Financial Transaction Services (FinTS) Dokument: Security - Sicherheitsverfahren PIN/TAN</td>
</tr>
<tr>
<td>Seite: 50</td>
<td>Stand: 23.02.2018</td>
<td>Kapitel: Verfahrensbeschreibung<br>Abschnitt: Geschäftsvorfall HKTAN für Zwei-Schritt-TAN-Einreichung</td>
</tr>
</table>


## ◆ Ausgewählte Beispiele für Rückmeldungscodes


<table>
<tr>
<td>Code</td>
<td>Beispiel für Rückmeldungstext</td>
</tr>
<tr>
<td>0010</td>
<td>Auftrag entgegengenommen</td>
</tr>
<tr>
<td>3075</td>
<td>Starke Authentifizierung ab dem ... erforderlich</td>
</tr>
<tr>
<td>9075</td>
<td>Dialog abgebrochen - starke Authentifizierung erforderlich</td>
</tr>
<tr>
<td>9210</td>
<td>Auftrag abgelehnt - Auftragsdaten inkonsistent. Eingereichter Auftrag gelöscht</td>
</tr>
<tr>
<td>9210</td>
<td>Auftrag abgelehnt - Zwei-Schritt-TAN inkonsistent. Eingereichter Auftrag gelöscht</td>
</tr>
<tr>
<td>9210</td>
<td>Auftrag abgelehnt - Kein eingereichter Auftrag gefunden</td>
</tr>
<tr>
<td>9210</td>
<td>Auftrag abgelehnt - Auftragsreferenz ist unbekannt</td>
</tr>
<tr>
<td>9330</td>
<td>chipTAN-Leser gesperrt. Führen Sie ggf. eine chipTAN-Synchronisation durch</td>
</tr>
<tr>
<td>9380</td>
<td>Gewähltes Zwei-Schritt-TAN-Verfahren nicht zulässig</td>
</tr>
<tr>
<td>9931</td>
<td>Sperrung des Kontos nach x Fehlversuchen</td>
</tr>
<tr>
<td>9941</td>
<td>TAN ungültig</td>
</tr>
<tr>
<td>9951</td>
<td>Zeitüberschreitung im Zwei-Schritt-Verfahren – TAN ungültig</td>
</tr>
<tr>
<td>9953</td>
<td>Nur ein TAN-pflichtiger Auftrag pro Nachricht erlaubt</td>
</tr>
<tr>
<td>9954</td>
<td>Mehrfach-TANs nicht erlaubt</td>
</tr>
<tr>
<td>9955</td>
<td>Ein-Schritt-TAN-Verfahren nicht zugelassen</td>
</tr>
<tr>
<td>9956</td>
<td>Zeitversetzte Eingabe von Mehrfach-TANs nicht erlaubt</td>
</tr>
<tr>
<td>9991</td>
<td>TAN bereits verbraucht</td>
</tr>
</table>


## c) Bankparameterdaten


## Format


<table>
<tr>
<td>Name:</td>
<td>Zwei-Schritt-TAN-Einreichung, Parameter</td>
</tr>
<tr>
<td>Typ:</td>
<td>Segment</td>
</tr>
<tr>
<td>Segmentart:</td>
<td>Geschäftsvorfallparameter</td>
</tr>
<tr>
<td>Kennung:</td>
<td>HITANS</td>
</tr>
<tr>
<td>Bezugssegment:</td>
<td>HKVVB</td>
</tr>
<tr>
<td>Segmentversion:</td>
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
<td>Parameter Zwei- Schritt-TAN- Einreichung</td>
<td>6</td>
<td>DEG</td>
<td></td>
<td></td>
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
<th rowspan="2">Kapitel: B</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Security - Sicherheitsverfahren PIN/TAN</td>
</tr>
<tr>
<td>Kapitel:<br>Abschnitt:</td>
<td>Verfahrensbeschreibung Erweiterung der Rückmeldungscodes</td>
<td>Stand: 23.02.2018</td>
<td>Seite: 51</td>
</tr>
</table>


## ◆ Belegungsrichtlinien

Auftrags-Hashwertverfahren (Parameter Zwei-Schritt-TAN-Einreichung)
Bei Verwendung von TAN-Prozess=1.


## B.6 Erweiterung der Rückmeldungscodes

Bei Verwendung des PIN/TAN-Verfahrens können spezielle Rückmeldecodes vom
Kreditinstitut zurückgemeldet werden, die rein PIN/TAN-spezifisch sind und u. U.
nicht direkt mit dem zugehörigen Geschäftsvorfall in Verbindung stehen. Es handelt
sich hierbei um die folgenden Codes:


## Erfolgsmeldungen


<table>
<tr>
<td>Code</td>
<td>Beispiel für Rückmeldungstext</td>
</tr>
<tr>
<td>0010</td>
<td>Auftrag entgegengenommen</td>
</tr>
<tr>
<td>0020</td>
<td>PIN-Sperre erfolgreich</td>
</tr>
<tr>
<td>0020</td>
<td>PIN-Sperre aufgehoben</td>
</tr>
<tr>
<td>0020</td>
<td>PIN geändert</td>
</tr>
<tr>
<td>0030</td>
<td>Auftrag empfangen - Sicherheitsfreigabe erforderlich</td>
</tr>
<tr>
<td>0030</td>
<td>Auftrag empfangen - Sicherheitsfreigabe erforderlich und Auftragsstorno möglich</td>
</tr>
<tr>
<td>0031</td>
<td>Auftragsstorno durchgeführt</td>
</tr>
<tr>
<td>0900</td>
<td>TAN gültig</td>
</tr>
<tr>
<td>0901</td>
<td>PIN gültig</td>
</tr>
</table>


## Warnungen und Hinweise


<table>
<tr>
<td>Code</td>
<td>Beispiel für Rückmeldungstext</td>
</tr>
<tr>
<td>3075</td>
<td>Starke Authentifizierung ab dem ... erforderlich</td>
</tr>
<tr>
<td>3076</td>
<td>Keine starke Authentifizierung erforderlich</td>
</tr>
<tr>
<td>3910</td>
<td>TAN wurde nicht verbraucht</td>
</tr>
<tr>
<td>3913</td>
<td>TAN wurde verbraucht</td>
</tr>
<tr>
<td>3916</td>
<td>PIN muss wegen erstmaliger Anmeldung zwangsweise geändert werden</td>
</tr>
<tr>
<td>3918</td>
<td>Kompetenz nicht ausreichend - weitere TAN erforderlich</td>
</tr>
<tr>
<td>3920</td>
<td>Zugelassene Ein- und Zwei-Schritt-Verfahren für den Benutzer (+ Rückmeldungsparameter)</td>
</tr>
<tr>
<td>3931</td>
<td>PIN gesperrt. Entsperren mit GV ,,PIN-Sperre aufheben“ möglich</td>
</tr>
<tr>
<td>3931</td>
<td>chipTAN-Leser gesperrt. Führen Sie ggf. eine chipTAN-Synchronisation durch</td>
</tr>
<tr>
<td>3932</td>
<td>Bitte führen Sie zunächst eine PIN-Änderung durch</td>
</tr>
<tr>
<td>3933</td>
<td>chipTAN-Leser gesperrt, Synchronisierung erforderlich Kartennummer</td>
</tr>
<tr>
<td>3934</td>
<td>Bitte eine Karte für die Verwendung mit chipTAN zulassen</td>
</tr>
<tr>
<td>3935</td>
<td>Bitte eine Karte für die Verwendung mit chipTAN zulassen</td>
</tr>
<tr>
<td>3939</td>
<td>mobileTAN-Freischaltung erforderlich. SMS-Freischaltcode wurde versendet</td>
</tr>
<tr>
<td>3940</td>
<td>Zur PIN-Änderung stehen folgende TAN-Medien zur Verfügung:</td>
</tr>
<tr>
<td>3941</td>
<td>Zur PIN-Änderung stehen folgende Rufnummern zur Verfügung:</td>
</tr>
<tr>
<td>3950</td>
<td>Die Selbstumstellung auf ein anderes Sicherheitsverfahren ist möglich</td>
</tr>
<tr>
<td>3951</td>
<td>Die Selbstumstellung auf ein anderes Sicherheitsverfahren ist erforderlich</td>
</tr>
<tr>
<td>3952</td>
<td>&lt;Rückmeldung des erfolgten Prozessschrittes der Selbstumstellung&gt;</td>
</tr>
<tr>
<td>3960</td>
<td>Individuell</td>
</tr>
</table>


<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: B</td>
<td>Version: 3.0-FV</td>
<td>Financial Transaction Services (FinTS) Dokument: Security - Sicherheitsverfahren PIN/TAN</td>
</tr>
<tr>
<td>Seite:<br>52</td>
<td>Stand: 23.02.2018</td>
<td>Kapitel: Verfahrensbeschreibung<br>Abschnitt: Erweiterung der Rückmeldungscodes</td>
</tr>
</table>


<table>
<tr>
<td>Code</td>
<td>Beispiel für Rückmeldungstext</td>
</tr>
<tr>
<td>-<br>3999</td>
<td></td>
</tr>
</table>


## Fehlermeldungen


<table>
<tr>
<td>Code</td>
<td>Beispiel für Rückmeldungstext</td>
</tr>
<tr>
<td>9075</td>
<td>Dialog abgebrochen - starke Authentifizierung erforderlich</td>
</tr>
<tr>
<td>9210</td>
<td>Auftrag abgelehnt - Auftragsdaten inkonsistent. Eingereichter Auftrag gelöscht</td>
</tr>
<tr>
<td>9210</td>
<td>Auftrag abgelehnt - Zwei-Schritt-TAN inkonsistent. Eingereichter Auftrag gelöscht</td>
</tr>
<tr>
<td>9210</td>
<td>Auftrag abgelehnt - Kein eingereichter Auftrag gefunden</td>
</tr>
<tr>
<td>9210</td>
<td>Auftrag abgelehnt - Auftragsreferenz ist unbekannt</td>
</tr>
<tr>
<td>9210</td>
<td>Auftrag abgelehnt - Kompetenz nicht ausreichend</td>
</tr>
<tr>
<td>9330</td>
<td>ChipTAN-Leser gesperrt. Führen Sie ggf. eine TAN-Gen.-Synchronisation durch</td>
</tr>
<tr>
<td>9931</td>
<td>Teilnehmersperre durchgeführt</td>
</tr>
<tr>
<td>9939</td>
<td>Freischalten der Mobilfunknummer für mobileTAN nicht möglich</td>
</tr>
<tr>
<td>9941</td>
<td>TAN ungültig</td>
</tr>
<tr>
<td>9942</td>
<td>PIN ungültig</td>
</tr>
<tr>
<td>9942</td>
<td>neue PIN ungültig</td>
</tr>
<tr>
<td>9951</td>
<td>Zeitüberschreitung im Zwei-Schritt-Verfahren – TAN ungültig</td>
</tr>
<tr>
<td>9953</td>
<td>Nur ein TAN-pflichtiger Auftrag pro Nachricht erlaubt</td>
</tr>
<tr>
<td>9954</td>
<td>Mehrfach-TANs nicht erlaubt</td>
</tr>
<tr>
<td>9955</td>
<td>Ein-Schritt-TAN-Verfahren nicht zugelassen</td>
</tr>
<tr>
<td>9956</td>
<td>Zeitversetzte Eingabe von Mehrfach-TANs nicht erlaubt</td>
</tr>
<tr>
<td>9957</td>
<td>Wechsel des TAN-Prozesses bei Mehrfach-TANs nicht erlaubt</td>
</tr>
<tr>
<td>9991</td>
<td>TAN bereits verbraucht</td>
</tr>
</table>


### B.6.1 Beschreibung spezieller Rückmeldungen im Zwei-Schritt-Verfahren


#### Rückmeldungscode 0030: Auftrag empfangen - Sicherheitsfreigabe erforderlich

Mit dem Rückmeldungscode 0030 als Antwort auf HKTAN bei Prozessvariante 1
bzw. die Einreichung einer Auftragsnachricht bei Prozessvariante 2 wird ein Zwei-
Schritt-Verfahren eingeleitet. Als Folge auf diesen Rückmeldecode darf je nach
TAN-Prozess ausschlieBlich ein Geschäftsvorfall mit der zugehörigen TAN übermit-
telt und kein neuer TAN-Prozess eingeleitet werden. Unabhängig davon können
PIN-pflichtige Geschäftsvorfälle, die keine TAN erfordern zwischen den beiden Pro-
zess-Schritten bearbeitet werden.

Rückmeldungscode 3075 / 9075:

\- Starke Authentifizierung ab dem ... erforderlich bzw.

\- Dialog abgebrochen - starke Authentifizierung erforderlich

Diese Rückmeldungen werden verwendet, wenn ein Institut durch Vorhandensein
von HKTAN#6 in den BPD eine starke Kundenauthentifizierung fordert, das Kunden-
produkt diese jedoch nicht durchführt. Diese Möglichkeit einer schwachen Authenti-
fizierung kann – solange zulässig – parallel zur starken Authentifizierung unterstützt
werden. Durch Verwendung des Rückmeldungscode 3075 „Starke Authenti-
fizierung ab dem ... erforderlich" kann der Benutzer auf den Wegfall der
schwachen Authentifizierung hingewiesen werden. Nach Ablauf dieser Frist kann
eine Dialoginitialisierung mit schwacher Authentifizierung durch den Rückmeldungs-
code 9075 ,,Dialog abgebrochen - starke Authentifizerung erfor-
derlich" abgewiesen werden. Der Rückmeldungscode 9075 muss in Kombination
mit Code 9800 auftreten.

<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th rowspan="2">Version: 3.0-FV</th>
<th rowspan="2">Kapitel: B</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Security - Sicherheitsverfahren PIN/TAN</td>
</tr>
<tr>
<td>Kapitel:<br>Abschnitt:</td>
<td>Verfahrensbeschreibung<br>Erweiterung der Rückmeldungscodes</td>
<td>Stand: 23.02.2018</td>
<td>Seite: 53</td>
</tr>
</table>


##### Rückmeldungscode 3076: Keine starke Authentifizierung erforderlich

Der Rückmeldungscode 3076 wird verwendet, wenn ein Institut durch Vorhanden-
sein von HKTAN#6 in den BPD eine starke Kundenauthentifizierung unterstützt. Im
Rahmen des Zwei-Schritt-Verfahrens bei Initialisierung und Auftragseinreichung
dient dieser RM-Code dazu, das Kundenprodukt nach der Einreichung in Schritt 1a
zu informieren, dass die Eingabe der PIN als Wissensfaktor ausreichend ist und
aufgrund einer in PSD2 definierten Ausnahme keine starke Kundenauthentifizierung
erforderlich ist. Die Verarbeitung wird mit Schritt 2b (Bestätigung der Auftragseinrei-
chung) fortgesetzt. Somit wird der RM-Code 3076 situationsbezogen alternativ zu
RM-Code 0030 verwendet.


#### Rückmeldungscode 3920: Zugelassene Ein- und Zwei-Schritt-Verfahren für den Benutzer (+ Rückmeldungsparameter)

Der Rückmeldungscode 3920 dient dazu, dem Kundenprodukt im Rahmen der Dia-
loginitialisierungsantwort die für den Benutzer zugelassenen Ein- und Zwei-Schritt-
Verfahren mitzuteilen. Hierzu werden in den Rückmeldungsparametern P1 bis P10
entsprechend den zugelassenen Verfahren (,,900" bis ,997") aus HITANS maximal
zehn mögliche Zwei-Schritt-Verfahren bzw. neun Zwei-Schritt-Verfahren + das Ein-
Schritt-Verfahren (,999") transportiert.


![](figures/53.1)


Das Kundenprodukt muss – unabhängig vom gewählten Verfahren
in ,,Sicherheitsfunktion, kodiert“ - bei jeder Dialoginitialisierung die
vom Institut mit dem Rückmeldungscode 3920 übermittelten Werte
P1, … , P10 prüfen, gegen gespeicherte Informationen vergleichen
und diese ggf. aktualisieren.

Sollte das Kundenprodukt in der Dialoginitialisierungsnachricht ein
Verfahren wählen, das für den Benutzer nicht bzw. nicht mehr zu-
gelassen ist, so beendet das Kreditinstitut den Dialog mit Rück-
meldungscode 9800 in Kombination mit Code 3920 und meldet die
aktuell zugelassenen Verfahren in den Parametern P1 bis P10.


#### Rückmeldungscode 3934 bzw. 3935: Bitte eine Karte zur Verwendung mit chip- TAN zulassen (+ Rückmeldungsparameter)

Die Rückmeldungscodes 3934 und 3935 veranlassen das Kundenprodukt, auf Basis
des Geschäftsvorfalls „TAN-Medium an bzw. ummelden (HKTAU)“ eine gültige Kar-
te für das chipTAN-Verfahren im laufenden Dialog anzumelden. Die Rückmeldungs-
parameter P1 und P2 enthalten pro Rückmeldung verpflichtend eine „Kartennum-
mer“ (Format „id“) und die zugehörige „Bezeichnung des TAN-Mediums“ (..32).

Bei Verwendung des Rückmeldungscode 3934 ist das Anstoßen des Geschäftsvor-
falls HKTAU verpflichtend.

Beim Rückmeldungscode 3935 ist das Initiieren der Kombination ,Anzeigen der ver-
fügbaren TAN-Medien (HKTAB)" und HKTAU optional.


#### Rückmeldungscode 9210:

\- Auftragsreferenz ist unbekannt bzw.

\- Auftrag abgelehnt - kein eingereichter Auftrag gefunden

Diese Rückmeldung kann folgende Ursachen haben:

<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: B</td>
<td>Version: 3.0-FV</td>
<td>Financial Transaction Services (FinTS) Dokument: Security - Sicherheitsverfahren PIN/TAN</td>
</tr>
<tr>
<td>Seite:<br>54</td>
<td>Stand: 23.02.2018</td>
<td>Kapitel: Verfahrensbeschreibung<br>Abschnitt: Bankfachliche Anforderungen</td>
</tr>
</table>


• Die eingereichte Auftragsreferenz bzw. der Auftrags-Hashwert wird im Auftrags-
bestand nicht gefunden, da das Element auf dem Weg vom Kreditinstitut zum
Kunden und wieder zurück verfälscht wurde.

• Ein zugehöriger Auftrag, der mehrere TANs erfordert, hat den maximalen Aufbe-
wahrungszeitraum überschritten und wurde vom Institut gelöscht.

• Ein zugehöriger Auftrag, der mehrere TANs erfordert, wurde über einen anderen
Vertriebsweg (außerhalb FinTS) autorisiert und ist inzwischen verarbeitet.


![](figures/54.1)


Das Kreditinstitut sollte den wirklichen Grund für diese Rückmel-
dung in das Statusprotokoll einstellen, damit der Kunde sich später
dort informieren und den Auftrag kundenseitig entsprechend weiter
bearbeiten kann.


## B.7 Bankfachliche Anforderungen

Es gelten die in [HBCI] aufgeführten Regelungen. Abweichend hierzu gilt:


### Zu signierende Nachrichten

Wie auch beim Sicherheitsverfahren HBCI ist die Signatur von Kreditinstitutsnach-
richten optional. Da der Kunde in seiner Auftragsnachricht das anzuwendende Sig-
naturverfahren vorgibt, darf das Kreditinstitut jedoch nicht mit einem Sicherheitsver-
fahren aus HBCI (RAH, RDH bzw. DDV) antworten. Somit sendet das Kreditinstitut
entweder keinen Sicherheitskopf und -abschluss oder alternativ sendet es Signa-
turkopf und -abschluss, bei denen allerdings PIN und TAN nicht belegt werden.


### Doppeleinreichungskontrolle über Signatur-ID und Kundensystem-ID

Im PIN/TAN-Verfahren werden keine Signatur-IDs benötigt, da hier die TAN deren
Aufgabe übernimmt und durch sie eine Doppeleinreichung verhindert wird. Eine
Kundensystem-ID ist jedoch auch hier notwendig, da der gleiche Benutzer zeitgleich
mehrere Dialoge von verschiedenen Kundensystemen aus führen kann. Soll eine
neue Kundensystem-ID durch das Segment HKSYN angefordert werden, so ist un-
ter ,,Sicherheitsfunktion, kodiert“ ein für den Kunden gültiges Ein- oder Zwei-Schritt-
Verfahren zurückzugeben.


## B.8 Erweiterung der Bank- und Userparameterdaten (BPD / UPD)

Für die Verwendung des PIN/TAN-Verfahrens müssen dem Kundenprodukt weitere
Daten im Rahmen der BPD- bzw. UPD-Segmentfolge übermittelt werden. So ist bei-
spielsweise anzugeben, welche Geschäftsvorfälle über PIN/TAN abgesichert wer-
den dürfen und für welche davon eine TAN erforderlich ist. Weiterhin muss auch
kommuniziert werden können, ob ein oder mehrere Zwei-Schritt-Verfahren unter-
stützt sind. Hierfür existieren zusätzliche Geschäftsvorfälle, welche die folgende In-
formation transportieren:


<table>
<tr>
<td>HIPINS</td>
<td>PIN/TAN-Verfahren ist unterstützt<br>nur Parametersegment; enthält die Segmentkennungen aller Ge- schäftsvorfälle, die über PIN/TAN abgewickelt werden können und die Information, welche Geschäftsvorfälle davon TAN-pflichtig sind.</td>
</tr>
<tr>
<td>HITANS</td>
<td>Mindestens ein Zwei-Schritt-Verfahren ist unterstützt (vgl. Kapitel B.5)</td>
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
<td>Dokument:</td>
<td>Security - Sicherheitsverfahren PIN/TAN</td>
</tr>
<tr>
<td>Kapitel:<br>Abschnitt:</td>
<td>Verfahrensbeschreibung<br>Erweiterung der Bank- und Userparameterdaten (BPD /</td>
<td>Stand: 23.02.2018</td>
<td>Seite: 55</td>
</tr>
</table>


### B.8.1 PIN/TAN-spezifische Informationen (HIPINS)

Die für die Kennzeichnung des PIN/TAN-Verfahrens notwendige BPD-/UPD-
Ergänzung wird in Form eines speziellen Parametersegmentes realisiert, welches
sich auf keinen echten Geschäftsvorfall bezieht, sondern Daten zu allen unterstütz-
ten Geschäftsvorfällen aufnehmen kann.

Das Spezialsegment HIPINS wird verwendet, um in die BPD-Segmentfolge
PIN/TAN-spezifische Daten einzufügen. Aufgrund seines Aufbaus analog zu einem
Segmentparametersegment wird es von Kundenprodukten, die das PIN/TAN-
Verfahren nicht unterstützen, ignoriert, da es sich auf einen ihnen unbekannten Ge-
schäftsvorfall zu beziehen scheint.

Die in HIPINS aufgeführten Geschäftsvorfälle dürfen vom Kunden in über PIN/TAN
abgesicherte Nachrichten eingestellt werden, sofern sie in den BPD und UPD als
generell erlaubt hinterlegt sind. Alle übrigen Geschäftsvorfälle können mit dem
PIN/TAN-Verfahren nicht verwendet werden.

Einzelheiten zur Verwendung von HIPINS in Kombination mit der starken Kun-
denauthentifizierung gemäß [PSD2] befinden sich in Kapitel B.3.


![](figures/55.1)


Um die Kompatibilität zwischen den Sicherheitsverfahren PIN/TAN
und HBCI sicherzustellen, konnte der mögliche Wertebereich in-
nerhalb von HISHV-Segmenten nicht um einen weiteren Wert für
PIN/TAN erweitert werden. Clients können diesem Segment somit
nicht entnehmen, ob das PIN/TAN-Verfahren unterstützt wird oder
nicht. Dies muss am Vorkommen des HIPINS-Segments festge-
macht werden. Ist ein solches Segment vorhanden, wird das
PIN/TAN- Verfahren unterstützt, andernfalls nicht.

Realisierung Bank:
verpflichtend,
falls
Geschäftsvorfälle
mit PIN/TAN-
Absicherung angeboten werden

Realisierung Kunde:
optional


#### ◆ Format


<table>
<tr>
<td>Name:</td>
<td>PIN/TAN-spezifische Informationen</td>
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
<td>HIPINS</td>
</tr>
<tr>
<td>Bezugssegment:</td>
<td>HKVVB</td>
</tr>
<tr>
<td>Segmentversion:</td>
<td>1</td>
</tr>
<tr>
<td>Sender:</td>
<td>Kreditinstitut</td>
</tr>
<tr>
<td>Format:</td>
<td>Geschäftsvorfall mit Parametern</td>
</tr>
</table>


#### ◆ Erläuterungen


<table>
<tr>
<td>Name:</td>
<td>Parameter PIN/TAN-spezifische Informationen</td>
</tr>
<tr>
<td>Typ:</td>
<td>Datenelementgruppe</td>
</tr>
<tr>
<td>Status:</td>
<td>M</td>
</tr>
</table>


<!-- PageBreak -->


<table>
<tr>
<th>Kapitel: B</th>
<th>Version: 3.0-FV</th>
<th>Financial Transaction Services (FinTS) Dokument: Security - Sicherheitsverfahren PIN/TAN</th>
</tr>
<tr>
<td>Seite:<br>56</td>
<td>Stand: 23.02.2018</td>
<td>Kapitel: Verfahrensbeschreibung<br>Abschnitt:<br>Erweiterung der Bank- und Userparameterdaten (BPD / UPD)</td>
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
<td></td>
<td>Minimale PIN-Länge</td>
<td>DE</td>
<td>num</td>
<td>..2</td>
<td>O</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td></td>
<td>Maximale PIN-Länge</td>
<td>DE</td>
<td>num</td>
<td>..2</td>
<td>O</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>·</td>
<td>Maximale TAN-Länge</td>
<td>DE</td>
<td>num</td>
<td>..2</td>
<td>O</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>.</td>
<td>Text zur Belegung der Benutzerkennung</td>
<td>DE</td>
<td>an</td>
<td>.30</td>
<td>O</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>.</td>
<td>Text zur Belegung der Kunden-ID</td>
<td>DE</td>
<td>an</td>
<td>..30</td>
<td>O</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td></td>
<td>Geschäftsvorfallspezifi- sche PIN/TAN- Informationen</td>
<td>DEG</td>
<td></td>
<td></td>
<td>O</td>
<td>999</td>
<td></td>
</tr>
</table>


### Beispiel

HIPINS:4:1:5+1+1+0+5:6:6:Kunden-Nr aus dem TAN-B
rief : :HKCCS:J:HKKAN:N:HKSAL:J:HKPAE:J:HKTLA:J:HK
TLF : J'


### B.8.2 Spezielle Festlegungen für die Dialoginitialisierung beim Zwei-Schritt- Verfahren

Im Rahmen der Dialoginitialisierung werden folgende Informationen ausgetauscht:


#### Zugelassene Ein- und Zwei-Schritt-Verfahren für den Benutzer

In der Dialoginitialisierungsantwort wird dem Kunden im Rahmen der Rück-
meldungen zu Segmenten (HIRMS) über den Rückmeldungscode 3920 und
entsprechende Rückmeldungsparameter mitgeteilt, welche konkreten Zwei-
Schritt-Verfahren für ihn zugelassen sind. Dabei wird pro Rückmeldeparame-
ter (P1 bis P10) ein Verfahrenskennzeichen (maximal 10 bzw. 9 + ggf. Ein-
Schritt-Verfahren) übermittelt. Die Kodierung erfolgt analog der Belegung
des DE ,Sicherheitsfunktion, kodiert" im Parametersegment HITANS, also im
Wertebereich ,,900" bis ,,997" bzw. ,999“ für Ein-Schritt-Verfahren.

<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th rowspan="2">Version: 3.0-FV</th>
<th rowspan="2">Kapitel: B</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Security - Sicherheitsverfahren PIN/TAN</td>
</tr>
<tr>
<td>Kapitel:</td>
<td>Verfahrensbeschreibung</td>
<td>Stand:</td>
<td>Seite:</td>
</tr>
<tr>
<td>Abschnitt:</td>
<td>Besondere Belegungsrichtlinien</td>
<td>23.02.2018</td>
<td>57</td>
</tr>
</table>


![](figures/57.1)


Das Kreditinstitut muss organisatorisch sicherstellen, dass der Kun-
de über eine geeignete Version eines Kundenproduktes verfügt, das
die Rückmeldeparameter entsprechend interpretieren kann. In je-
dem Falle sollte der Kunde durch einen verständlichen Rückmelde-
text darauf hingewiesen werden, dass er ggf. ein aktualisiertes Kun-
denprodukt benötigt.

Sollte der Kunde vertraglich an die Nutzung des Zwei-Schritt-
Verfahrens gebunden sein und verwendet er ein Kundenprodukt,
welches das Zwei-Schritt-Verfahren nicht unterstützt, so ist der Dia-
log zu beenden. Über den Rückmeldungscode 9955 „Ein-Schritt-
TAN-Verfahren nicht zugelassen“ und einen geeigneten Rückmel-
dungstext muss der Kunde eindeutig über die Ursache dieser Dia-
logbeendigung informiert werden. Der Rückmeldungstext muss
auch berücksichtigen, dass die Anfrage des Kundenproduktes mit
DE ,,Sicherheitsfunktion, kodiert" = ,999" in diesem Fall nur erfolgt,
um die unterstützten konkreten Zwei-Schritt-Verfahren für den Be-
nutzer zu ermitteln. Diese müssen über den Rückmeldungscode
3920 ,,Zugelassene Ein- und Zwei-Schritt-Verfahren für den Benut-
zer“ (oder den entsprechenden Rückmeldungscode 3920 in Kombi-
nation mit Code 9800 im Fehlerfall) mitgeteilt werden.


![](figures/57.2)


Sollte das Kundenprodukt Zwei-Schritt-Verfahren unterstützen und
noch keine Verfahrensparameter mit Angabe der für den aktuellen
Benutzer unterstützten Verfahren verfügen, so muss es einen Dia-
log eröffnen, um über die Rückmeldeparameter in Kenntnis der er-
laubten Verfahren zu gelangen. Hierbei ist für das DE „Sicherheits-
funktion, kodiert" der Wert ,,999" für Ein-Schritt-Verfahren zu ver-
wenden.


#### Gewähltes Zwei-Schritt-Verfahren des Kunden

Ein Kunde kann aus den für Ihn zugelassenen konkreten Zwei-Schritt-
Verfahren eines für den aktiven Dialog auswählen. Das entsprechende Ver-
fahrenskennzeichen wird in das DE ,,Sicherheitsfunktion, kodiert" im Signa-
turkopf der Dialoginitialisierungsnachricht eingestellt. Die Kodierung erfolgt
analog der Belegung des DE ,,Sicherheitsfunktion, kodiert" im Parame-
tersegment HITANS, also im Wertebereich ,,900" bis ,997". Das gewählte
konkrete Zwei-Schritt-Verfahren muss für den Benutzer erlaubt sein (BPD,
Rückmeldung 3920 bei Dialoginitialisierung). Auch wenn im Dialog keine
TAN-pflichtigen Geschäftsvorfälle eingereicht werden, muss ein Verfahren
ausgewählt werden.


## B.9 Besondere Belegungsrichtlinien

Datenelemente mit Status „O“, sollten grundsätzlich leer gelassen werden.

Für einige Datenelemente gelten bei PIN/TAN besondere Belegungsrichtlinien, die
von den allgemeinen in [HBCI] aufgeführten Richtlinien abweichen. Diese sind nach-
folgend aufgeführt.

<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: B</td>
<td>Version: 3.0-FV</td>
<td>Financial Transaction Services (FinTS) Dokument: Security - Sicherheitsverfahren PIN/TAN</td>
</tr>
<tr>
<td>Seite:<br>58</td>
<td>Stand: 23.02.2018</td>
<td>Kapitel: Verfahrensbeschreibung<br>Abschnitt: Besondere Belegungsrichtlinien</td>
</tr>
</table>


### B.9.1 DEG ,,Sicherheitsprofil"

Sicherheitsverfahren, Code

„PIN“ : bei allen Nachrichten

Version des Sicherheitsverfahrens

„1“ : bei allen Nachrichten, wenn Dialog im Einschritt-Verfahren

„2“ : bei allen Nachrichten, wenn Dialog im Zwei-Schritt-Verfahren


### B.9.2 DEG „Schlüsselname“

Schlüsselnummer

FinTS-Füllwert, z. B. „0“

Schlüsselversion

FinTS-Füllwert, z. B. „0“


### B.9.3 DEG ,,Sicherheitsidentifikation, Details"

CID

Dieses Feld darf nicht belegt werden.

Identifizierung der Partei

Dieses Feld muss eine gültige, zuvor vom Banksystem angeforderte Kun-
densystem-ID enthalten (analog zu RAH-/RDH-Verfahren). Dies gilt auch für
Zweit- und Drittsignaturen.


### B.9.4 Segment ,,Signaturkopf"

Sicherheitsfunktion, kodiert

Beim Ein-Schritt-Verfahren ist der Wert ,,999" einzustellen, beim Zwei-Schritt-
Verfahren der entsprechende in der BPD mitgeteilte Wert für das konkrete
Verfahren ,900" bis ,,997" (vgl. Kapitel B.8.2).

Zertifikat

Dieses Feld darf nicht belegt werden.


### B.9.5 DEG ,,Hashalgorithmus"

Wert des Hashalgorithmusparameters

Dieses Feld darf nicht belegt werden.


### B.9.6 DEG ,,Signaturalgorithmus"

Signaturalgorithmus, kodiert
FinTS-Füllwert, z. B. „10“

Operationsmodus, kodiert
FinTS-Füllwert, z. B. „16“

<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th>Version:</th>
<th rowspan="2">Kapitel: B</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Security - Sicherheitsverfahren PIN/TAN</td>
<td>3.0-FV</td>
</tr>
<tr>
<td>Kapitel:</td>
<td>Verfahrensbeschreibung</td>
<td>Stand:</td>
<td>Seite:</td>
</tr>
<tr>
<td>Abschnitt:</td>
<td>Besondere Belegungsrichtlinien</td>
<td>23.02.2018</td>
<td>59</td>
</tr>
</table>


### B.9.7 Segment ,,Signaturabschluss"

Es ist der Signaturabschluss gemäß [HBCI] ab Segmentversion 2 zu verwenden.


#### Validierungsresultat

Dieses Feld darf nicht belegt werden.

Benutzerdefinierte Signatur

Hier werden bei Verwendung des PIN/TAN-Verfahrens PIN und TAN einge-
stellt. Bei Verwendung des Zwei-Schritt-Verfahrens mit Prozessvariante 2
darf eine TAN ausschließlich über den Geschäftsvorfall HKTAN eingereicht
werden, wobei pro HKTAN nur die Verarbeitung einer einzelnen TAN zuläs-
sig ist. Ansonsten darf die DE ,,TAN" im Signaturabschluss nicht belegt wer-
den; ihr Inhalt wird in diesem Fall ignoriert und die TAN vom Institut entwer-
tet. Gleiches gilt bei der nicht zulässigen Übermittlung von mehreren TANs
mit HKTAN. Bei der Verwendung im Rahmen des Sicherheitsverfahrens
HBCI darf die DEG nicht belegt werden. Ihr Inhalt wird in diesem Fall igno-
riert.


### B.9.8 Segment „Verschlüsselungskopf“

Sicherheitsfunktion, kodiert

Es wird der Wert ,,998" (Klartext) verwendet.

Zertifikat

Dieses Feld darf nicht belegt werden.


### B.9.9 DEG „Verschlüsselungsalgorithmus"

Wert des Algorithmusparameters, Schlüssel
FinTS-Füllwert, z.B. X'00 00 00 00 00 00 00 00'

Bezeichner für Algorithmusparameter, Schlüssel
FinTS-Füllwert, z.B. „5“

Wert des Algorithmusparameters, IV

Belegung nicht zulässig.


### B.9.10 Segment „Verschlüsselte Daten“

Daten, verschlüsselt

Enthält die unverschlüsselten Daten (die Verschlüsselung erfolgt via Trans-
portverschlüsselung des verwendeten Transportprotokolls HTTPS).


### B.9.11 Parametersegmente zu Geschäftsvorfällen


#### Sicherheitsklasse

Sicherheitsklassen werden nur in Verbindung mit dem Sicherheitsverfahren
HBCI benutzt. Unterstützt ein Kreditinstitut ausschließlich das PIN/TAN-
Verfahren, so ist in das DE ,Sicherheitsklasse' des jeweiligen Geschäftsvor-
fallparametersegmentes als Füllwert ,0' einzustellen. Die Sicherheitsklasse
hat bei PIN/TAN für die Verarbeitung keine Bedeutung und darf vom Kun-
denprodukt für PIN/TAN nicht ausgewertet werden.

<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: B</td>
<td>Version: 3.0-FV</td>
<td>Financial Transaction Services (FinTS) Dokument: Security - Sicherheitsverfahren PIN/TAN</td>
</tr>
<tr>
<td>Seite:<br>60</td>
<td>Stand: 23.02.2018</td>
<td>Kapitel: PIN/TAN-Management<br>Abschnitt: Besondere Belegungsrichtlinien</td>
</tr>
</table>


Stattdessen sind die Informationen aus HIPINS für die Festlegung benötigter
Sicherheitsmerkmale zu verwenden.


# C. PIN/TAN-MANAGEMENT

Alle Geschäftsvorfälle zum PIN/TAN-Management werden innerhalb eines persona-
lisierten Dialoges gesendet, also nach Eingabe der PIN. Falls zusätzlich eine TAN
erforderlich ist, ist dies in der Beschreibung des Geschäftsvorfalls vermerkt. PIN und
TAN werden in die entsprechenden Felder des Signaturabschlusses eingestellt (vgl.
Kapitel B.9.7) und sind in der Regel im Geschäftsvorfall selbst nicht vorhanden
(Ausnahmen sind z. B. die PIN-Änderung oder die TAN-Generator-
Synchronisierung).


![](figures/60.1)


![](figures/60.2)


Die Geschäftsvorfälle zum PIN/TAN-Management sollten vom
Kundenprodukt immer in einem geschlossenen Kontext, d. h. in
separaten Nachrichten in einem separaten Dialog geschickt wer-
den, da ansonsten eine gezielte Verarbeitung nicht gewährleistet
werden kann und somit ein exaktes Wissen, ab wann z.B. eine
PIN-Änderung gültig ist, nicht besteht.

Desweiteren ist vom Kundenprodukt sicherzustellen, dass eine
Nachricht entweder nur einen einzelnen Geschäftsvorfall enthält,
für den eine TAN erforderlich ist, oder nur solche Geschäftsvorfäl-
le, für die keine TAN erforderlich ist. Andernfalls ist die eindeutige
Zuordnung der übergebenen TAN zu den Geschäftsvorfällen nicht
sichergestellt.

Eine Mischung von Geschäftsvorfällen, die eine TAN erfordern, mit
solchen, die keine erfordern, ist generell nicht zulässig.

Grundsätzlich werden alle vom Kunden übermittelten TANs, wenn möglich, aus Si-
cherheitsgründen entwertet („verbrannt“).


![](figures/60.3)


Damit der Kunde Informationen darüber erhält, dass eine von ihm
verwendete TAN aufgrund des Abbruchs der Verarbeitung eines
Geschäftsvorfalles nicht verbraucht wurde, ist vom Kreditinstitut ei-
ne entsprechende Rückmeldung zu diesem Geschäftsvorfall zu er-
zeugen. Ist diese Rückmeldung eingestellt worden, kann vom Kun-
den die gleiche TAN noch einmal verwendet werden.


![](figures/60.4)


Wird vom Kreditinstitut nicht gemeldet, dass die übermittelte TAN
weiterhin gültig ist, muss die Kundenseite davon ausgehen, dass
die TAN verbraucht wurde. Dies gilt auch dann, wenn der zugehöri-
ge Geschäftsvorfall aufgrund von Fehlern nicht ausgeführt wurde.

Beim Einsatz des Zwei-Schritt-Verfahrens erfolgt die Verarbeitung wie in den Fest-
legungen in Kapitel B.2 beschrieben.

<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th rowspan="2">Version: 3.0-FV</th>
<th rowspan="2">Kapitel: B</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Security - Sicherheitsverfahren PIN/TAN</td>
</tr>
<tr>
<td>Kapitel:</td>
<td>PIN/TAN-Management</td>
<td>Stand:</td>
<td>Seite:</td>
</tr>
<tr>
<td>Abschnitt:</td>
<td>Verwalten der Online-Banking-PIN</td>
<td>23.02.2018</td>
<td>61</td>
</tr>
</table>


Wird also für die Ausführung eines PIN/TAN-Management-Geschäftsvorfalls eine
TAN benötigt, so wird diese analog Prozessvariante 1 oder 2 ermittelt.

PIN/TAN-Management-Geschäftsvorfälle zur Verwaltung von TAN-Listen wurden
aus der vorliegenden Spezifikation entfernt und können bei Bedarf in einem älteren
Release im Archiv unter [https://www.fints.org](http://www.fints.org/) gefunden werden.


## C.1 Verwalten der Online-Banking-PIN


### C.1.1 PIN-Änderung

Dieser Geschäftsvorfall bewirkt die Änderung der PIN. Zur Änderung der PIN ist im
Signaturabschluss die alte PIN; der Geschäftsvorfall selbst enthält die neue PIN.

Folgende Ereignisse können Auslöser zur Änderung der PIN sein:

. Erstzugang zum Online Banking - hier ist die vom Institut vergebene PIN durch
eine persönliche PIN zu ersetzen.

Dazu wird in der Dialoginitialisierung vom Kreditinstitut der Code 3916 (,PIN
muss wegen erstmaliger Anmeldung zwangsweise geändert werden“) zurück
gemeldet. Der Kunde muss in der folgenden Nachricht zwingend eine PIN-
Änderungsnachricht senden.

. Auf Wunsch des Kunden

· Zwangsänderung bei Verdacht auf Kompromittierung

Die Abläufe zur Durchführung einer PIN-Änderung im Kontext der starken Kun-
denauthentifizierung befinden sich in den Abschnitten B.4.3.1.1(Erstzugang) und
B.4.3.1.2 (Zwangsänderung).

Hinweis: mit Einführung der starken Kundenauthentifizierung muss eine PIN-
Änderung obligatorisch mit einer TAN authentifiziert werden. Hierzu muss der Ge-
schäftsvorfall „PIN-Änderung“ im Parametersegment HIPINS als TAN-pflichtig de-
klariert sein.

<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: B</td>
<td>Version: 3.0-FV</td>
<td>Financial Transaction Services (FinTS) Dokument: Security - Sicherheitsverfahren PIN/TAN</td>
</tr>
<tr>
<td>Seite:<br>62</td>
<td>Stand: 23.02.2018</td>
<td>Kapitel: PIN/TAN-Management<br>Abschnitt: Verwalten der Online-Banking-PIN</td>
</tr>
</table>


Realisierung Bank: optional

Realisierung Kunde: optional


#### a) Kundenauftrag


##### Format


<table>
<tr>
<td>Name:</td>
<td>PIN ändern</td>
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
<td>HKPAE</td>
</tr>
<tr>
<td>Bezugssegment:</td>
<td>-</td>
</tr>
<tr>
<td>Segmentversion:</td>
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
<td>PIN</td>
<td>1</td>
<td>DE</td>
<td>an</td>
<td>.99</td>
<td>O</td>
<td>1</td>
<td></td>
</tr>
</table>


##### ◆ Belegungsrichtlinien

PIN

Es ist die neue PIN anzugeben.


##### b) Kreditinstitutsrückmeldung


##### ◆ Erläuterungen

Es werden keine Datensegmente zurückgemeldet.


##### ◆ Ausgewählte Beispiele für Rückmeldungscodes


<table>
<tr>
<td>Code</td>
<td>Beispiel für Rückmeldungstext</td>
</tr>
<tr>
<td>0020</td>
<td>PIN geändert</td>
</tr>
<tr>
<td>9942</td>
<td>neue PIN ungültig</td>
</tr>
</table>


##### c) Bankparameterdaten


##### Beschreibung

Geschäftsvorfallspezifische Parameter existieren nicht.


##### ◆ Format


<table>
<tr>
<td>Name:</td>
<td>PIN ändern Parameter</td>
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
<td>HIPAES</td>
</tr>
<tr>
<td>Bezugssegment:</td>
<td>HKVVB</td>
</tr>
<tr>
<td>Segmentversion:</td>
<td>1</td>
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
<th rowspan="2">Kapitel: B</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Security - Sicherheitsverfahren PIN/TAN</td>
</tr>
<tr>
<td>Kapitel:</td>
<td>PIN/TAN-Management</td>
<td>Stand:</td>
<td>Seite:</td>
</tr>
<tr>
<td>Abschnitt:</td>
<td>Sperren der Online-Banking-PIN</td>
<td>23.02.2018</td>
<td>63</td>
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
<td>.3</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>3</td>
<td>Anzahl Signaturen minde- stens</td>
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


## C.2 Sperren der Online-Banking-PIN

Es ist zu unterscheiden zwischen Sperren, die vom Kreditinstitut automatisch durch
eine mehrfach falsche Benutzereingabe veranlasst werden, und Sperren, die be-
wusst vom Benutzer initiiert werden.


### C.2.1 Sperre bei mehrmaliger Falscheingabe

Bei jedem Erhalt einer falsch signierten Nachricht für einen noch nicht gesperrten
Benutzer (z. B. falsche PIN oder ungültige TAN) wird der jeweilige Fehlbedienungs-
zähler (PIN oder TAN) erhöht. Nach Überschreiten des vom Kreditinstitut vorgege-
benen Wertes wird eine Sperre vorgenommen. Eine erfolgte Sperre wird dem Be-
nutzer mittels eines Rückmeldungscodes (9931: Sperre durchgeführt) mitgeteilt.

Sofern das Kreditinstitut dies zulässt, ist eine Entsperrung mit Hilfe des Geschäfts-
vorfalls ,,PIN-Sperre aufheben" (Kap. C.2.3) möglich. Andernfalls kann die Sperre
nur vom Kreditinstitut aufgehoben werden.

Der Umfang der Sperre ist institutsabhängig und kann dem Kunden im Rahmen der
Rückmeldung detaillierter mitgeteilt werden.


#### Ausgewählte Beispiele für Rückmeldungscodes


<table>
<tr>
<td>Code</td>
<td>Beispiel für Rückmeldungstext</td>
</tr>
<tr>
<td>9931</td>
<td>PIN gesperrt</td>
</tr>
<tr>
<td>9931</td>
<td>Online-Zugang gesperrt</td>
</tr>
<tr>
<td>9931</td>
<td>SB-Zugang gesperrt</td>
</tr>
<tr>
<td>9931</td>
<td>Konto gesperrt</td>
</tr>
</table>


<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: B</td>
<td>Version: 3.0-FV</td>
<td>Financial Transaction Services (FinTS) Dokument: Security - Sicherheitsverfahren PIN/TAN</td>
</tr>
<tr>
<td>Seite:<br>64</td>
<td>Stand: 23.02.2018</td>
<td>Kapitel: PIN/TAN-Management<br>Abschnitt: Sperren der Online-Banking-PIN</td>
</tr>
</table>


### C.2.2 PIN-Sperre

Dieser Geschäftsvorfall bewirkt eine Sperre durch den Kunden. Der Umfang der
Sperre ist institutsabhängig und kann dem Kunden im Rahmen der Rückmeldung
detaillierter mitgeteilt werden.

Das Sperren des Online-Banking-Zugangs durch den Benutzer erfordert analog zu
den HBCI-Signaturverfahren DDV und RAH die Eingabe einer gültigen PIN, selbst
wenn diese kompromittiert sein sollte.

Realisierung Bank:
optional

Realisierung Kunde: optional


## a) Kundenauftrag


## Format


<table>
<tr>
<td>Name:</td>
<td>PIN sperren</td>
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
<td>HKPSP</td>
</tr>
<tr>
<td>Bezugssegment:</td>
<td>-</td>
</tr>
<tr>
<td>Segmentversion:</td>
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


## ◆ Belegungsrichtlinien

Der Signaturabschluss muss eine gültige PIN enthalten.


## b) Kreditinstitutsrückmeldung


## ◆ Erläuterungen

Es werden keine Datensegmente zurückgemeldet.


## ◆ Ausgewählte Beispiele für Rückmeldungscodes


<table>
<tr>
<td>Code</td>
<td>Beispiel für Rückmeldungstext</td>
</tr>
<tr>
<td>0020</td>
<td>PIN-Sperre erfolgreich</td>
</tr>
<tr>
<td>0020</td>
<td>Konto-Sperre erfolgreich</td>
</tr>
<tr>
<td>0020</td>
<td>Sperre erfolgreich. Zur Entsperrung wenden Sie sich bitte an Ihr Kreditinstitut</td>
</tr>
</table>


## c) Bankparameterdaten


## Beschreibung

Geschäftsvorfallspezifische Parameter existieren nicht.

<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th rowspan="2">Version: 3.0-FV</th>
<th rowspan="2">Kapitel: B</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Security - Sicherheitsverfahren PIN/TAN</td>
</tr>
<tr>
<td>Kapitel:</td>
<td>PIN/TAN-Management</td>
<td>Stand:</td>
<td>Seite:</td>
</tr>
<tr>
<td>Abschnitt:</td>
<td>Sperren der Online-Banking-PIN</td>
<td>23.02.2018</td>
<td>65</td>
</tr>
</table>


## ◆ Format


<table>
<tr>
<td>Name:</td>
<td>PIN sperren Parameter</td>
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
<td>HIPSPS</td>
</tr>
<tr>
<td>Bezugssegment:</td>
<td>HKVVB</td>
</tr>
<tr>
<td>Segmentversion:</td>
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
<td>Anzahl Signaturen minde- stens</td>
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


### C.2.3 PIN-Sperre aufheben

Dieses Segment bewirkt das Aufheben einer PIN-Sperre. Wurde eine Online-Sperre
auf ein Konto gelegt (i.d.R. durch mehrmalige Eingabe einer falschen PIN), kann
das Konto durch die Eingabe der richtigen PIN und einer gültigen TAN wieder ent-
sperrt werden (PIN und TAN befinden sich im Signaturabschluss).


![](figures/65.1)


Da bei gesperrter PIN im Regelfall kein weiterer Dialog möglich ist,
da bereits die Dialoginitialisierung abgelehnt wird, kann dieser Ge-
schäftsvorfall nur angeboten werden, wenn das Kreditinstitut nach
einer PIN-Sperre einen weiteren Dialog mit der gesperrten PIN zu-
lässt, sofern in diesem nur der Geschäftsvorfall „PIN-Sperre aufhe-
ben“ gesendet wird.


![](figures/65.2)


In der Regel wird kreditinstitutsseitig nur ein einziger Versuch zur
Aufhebung der PIN-Sperre zugelassen. Schlägt dieser fehl, kann
nur das Kreditinstitut entsperren.

Realisierung Bank: optional

Realisierung Kunde: optional

<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: B</td>
<td>Version: 3.0-FV</td>
<td>Financial Transaction Services (FinTS) Dokument: Security - Sicherheitsverfahren PIN/TAN</td>
</tr>
<tr>
<td>Seite: 66</td>
<td>Stand: 23.02.2018</td>
<td>Kapitel: PIN/TAN-Management<br>Abschnitt: Sperren der Online-Banking-PIN</td>
</tr>
</table>


## a) Kundenauftrag


### Format


<table>
<tr>
<td>Name:</td>
<td>PIN-Sperre aufheben</td>
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
<td>HKPSA</td>
</tr>
<tr>
<td>Bezugssegment:</td>
<td>-</td>
</tr>
<tr>
<td>Segmentversion:</td>
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


### b) Kreditinstitutsrückmeldung


## ◆ Erläuterungen

Es werden keine Datensegmente zurückgemeldet.


## ◆ Ausgewählte Beispiele für Rückmeldungscodes

Code
Beispiel für Rückmeldungstext

0020
PIN-Sperre aufgehoben


## c) Bankparameterdaten


## Beschreibung

Geschäftsvorfallspezifische Parameter existieren nicht.


## ◆ Format


<table>
<tr>
<td>Name:</td>
<td>PIN-Sperre aufheben Parameter</td>
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
<td>HIPSAS</td>
</tr>
<tr>
<td>Bezugssegment:</td>
<td>HKVVB</td>
</tr>
<tr>
<td>Segmentversion:</td>
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
<td>Anzahl Signaturen minde- stens</td>
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
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th>Version:</th>
<th rowspan="2">Kapitel: B</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Security - Sicherheitsverfahren PIN/TAN</td>
<td>3.0-FV</td>
</tr>
<tr>
<td>Kapitel:</td>
<td>PIN/TAN-Management</td>
<td>Stand:</td>
<td>Seite:</td>
</tr>
<tr>
<td>Abschnitt:</td>
<td>Management chipTAN, mobileTAN und bilaterale Verfahren</td>
<td>23.02.2018</td>
<td>67</td>
</tr>
</table>


# C.3 Management chipTAN, mobileTAN und bilaterale Verfahren


## C.3.1 Anzeige der verfügbaren TAN-Medien

Mit Hilfe dieses Geschäftsvorfalls wird dem Kunden eine Übersicht über seine ver-
fügbaren TAN-Medien (TAN-Generator) gegeben.

Der Kunde muss auch im Hinblick auf das TAN-Zwei-Schritt-Verfahren wissen, wel-
ches Medium er verwenden darf. Hierzu werden ihm seine verfügbaren Medien
(Kartennummern) mit ihrem aktuellen Status angezeigt. Es wird dahingehend unter-
schieden, ob das Medium „Verfügbar" oder ,,Aktiv" ist. Folgekarten werden separat
mit eigenen Kennzeichen versehen, da mit der ,Aktivierung“ der Folgekarte die ak-
tuelle Karte für die TAN-Generierung gesperrt wird.


<table>
<tr>
<td>Status</td>
<td>Erläuterungen</td>
</tr>
<tr>
<td>Verfügbar</td>
<td>Das Medium kann genutzt werden, muss aber zuvor mit "TAN-Generator an- bzw. ummelden (HKTAU)" aktiv ge- meldet werden.</td>
</tr>
<tr>
<td>Aktiv</td>
<td>Die Bank zeigt an, dass es eine TAN-Verifikation gegen dieses Medium vornimmt.</td>
</tr>
<tr>
<td>Verfügbare Folgekarte</td>
<td>Das Medium kann mit dem Geschäftsvorfall „TAN-Medium an- bzw. ummelden (HKTAU)" aktiv gemeldet werden. Die aktuelle Karte kann dann nicht mehr genutzt werden.</td>
</tr>
<tr>
<td>Aktiv Folgekarte</td>
<td>Mit der ersten Nutzung der Folgekarte wird die zur Zeit ak- tive Karte gesperrt.</td>
</tr>
</table>


Anmerkung: Wenn eine Bank mehrere Medien in dem Status ,,Aktiv“ verwalten kann,
dann muss beim Zwei-Schritt-Verfahren dem Institut zuvor mit dem Geschäftsvorfall
,TAN-Medium an- bzw. ummelden“ (HKTAU) mitgeteilt werden, welches Medium für
die Signatur des Geschäftsvorfalles verwendet werden soll.


## C.3.1.1Anzeigen der verfügbaren TAN-Medien, Segmentversion #5

Bei Segmentversion #5 wird gegenüber der Vorgängerversion in der Kundennach-
richt durch das Datenelement ,,TAN-Medium-Klasse #4" die Unterstützung von bila-
teral vereinbarten Verfahren möglich.

Realisierung Bank: optional

Realisierung Kunde: optional

<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: B</td>
<td>Version: 3.0-FV</td>
<td>Financial Transaction Services (FinTS) Dokument: Security - Sicherheitsverfahren PIN/TAN</td>
</tr>
<tr>
<td>Seite:<br>68</td>
<td>Stand: 23.02.2018</td>
<td>Kapitel: PIN/TAN-Management<br>Abschnitt: Management chipTAN, mobileTAN und bilaterale Verfahren</td>
</tr>
</table>


# a) Kundenauftrag


## Format


<table>
<tr>
<td>Name:</td>
<td>TAN-Generator/Liste anzeigen Bestand</td>
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
<td>HKTAB</td>
</tr>
<tr>
<td>Bezugssegment:</td>
<td>-</td>
</tr>
<tr>
<td>Segmentversion:</td>
<td>5</td>
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
<td>TAN-Medium-Art</td>
<td>2</td>
<td>DE</td>
<td>code</td>
<td>1</td>
<td>M</td>
<td>1</td>
<td>0, 1, 2</td>
</tr>
<tr>
<td>3</td>
<td>TAN-Medium- Klasse</td>
<td>4</td>
<td>DE</td>
<td>code</td>
<td>1</td>
<td>M</td>
<td>1</td>
<td>A, L, G, M, S, B</td>
</tr>
</table>


## b) Kreditinstitutsrückmeldung


# Erläuterungen

Es wird ein Datensegment zurückgemeldet.


## ◆ Format


<table>
<tr>
<td>Name:</td>
<td>TAN-Generator/Liste anzeigen Bestand Rückmeldung</td>
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
<td>HITAB</td>
</tr>
<tr>
<td>Bezugssegment:</td>
<td>HKTAB</td>
</tr>
<tr>
<td>Segmentversion:</td>
<td>5</td>
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
<td>TAN-Einsatzoption</td>
<td>1</td>
<td>DE</td>
<td>code</td>
<td>1</td>
<td>M</td>
<td>1</td>
<td>0, 1, 2</td>
</tr>
<tr>
<td>3</td>
<td>TAN-Medium-Liste</td>
<td>5</td>
<td>DEG</td>
<td></td>
<td></td>
<td>O</td>
<td>99</td>
<td></td>
</tr>
</table>


# ◆ Belegungsrichtlinien


## TAN-Medium-Liste

Darf nur belegt werden, wenn für den Kunden ein TAN-Medium verfügbar /
nutzbar ist.

Beim mobileTAN-Verfahren (TAN-Medium-Klasse="M") muss entweder das
Datenelement ,,Mobiltelefonnummer“ oder ,,Mobiltelefonnummer verschleiert“
angegeben werden.

Bei bilateral vereinbarten Verfahren (TAN-Medium-Klasse="B") muss das Da-
tenelement ,,Sicherheitsfunktion, kodiert" angegeben werden. Die ,,Sicherheits-
funktion, kodiert" beinhaltet den Wert für das bilateral vereinbarte Verfahren in
der DEG ,,Verfahrensparameter Zwei-Schritt-Verfahren“.

<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th>Version:</th>
<th rowspan="2">Kapitel: B</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Security - Sicherheitsverfahren PIN/TAN</td>
<td>3.0-FV</td>
</tr>
<tr>
<td>Kapitel:</td>
<td>PIN/TAN-Management</td>
<td>Stand:</td>
<td>Seite:</td>
</tr>
<tr>
<td>Abschnitt:</td>
<td>Management chipTAN, mobileTAN und bilaterale Verfahren</td>
<td>23.02.2018</td>
<td>69</td>
</tr>
</table>


# ◆ Ausgewählte Beispiele für Rückmeldungscodes


<table>
<tr>
<td>Code</td>
<td>Beispiel für Rückmeldungstext</td>
</tr>
<tr>
<td>0020</td>
<td>Auftrag verarbeitet</td>
</tr>
</table>


# c) Bankparameterdaten


## Beschreibung

Geschäftsvorfallspezifische Parameter existieren nicht.


# ◆ Format


<table>
<tr>
<td>Name:</td>
<td>TAN-Generator/Liste anzeigen Bestand Parameter</td>
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
<td>HITABS</td>
</tr>
<tr>
<td>Bezugssegment:</td>
<td>HKVVB</td>
</tr>
<tr>
<td>Segmentversion:</td>
<td>5</td>
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
<td>Kapitel: B</td>
<td>Version: 3.0-FV</td>
<td>Financial Transaction Services (FinTS) Dokument: Security - Sicherheitsverfahren PIN/TAN</td>
</tr>
<tr>
<td>Seite:<br>70</td>
<td>Stand: 23.02.2018</td>
<td>Kapitel: PIN/TAN-Management<br>Abschnitt: Management chipTAN, mobileTAN und bilaterale Verfahren</td>
</tr>
</table>


## C.3.1.2Übermitteln / Anzeigen von TAN-Generator (HHD)- und Secoder-Informationen

Dieser Geschäftsvorfall dient dazu, Informationen über die Eigenschaften eines
TAN-Generators (HHD) oder Secoders vom Kundenprodukt an das Kreditinstitut zu
senden. Das Kreditinstitut kann mit diesen Daten zum Einen seine eigene Be-
standsverwaltung pflegen, aber auch entsprechende Informationen, die sich aus
den übertragenen Daten ergeben, zurück melden.

So kann z. B. ein Kunde die eindeutige Reader-ID seines TAN-Generators ermitteln
(per HotKey oder durch die Challenge-Klasse 09 seines HHD - vgl. [HHD]) und die-
se an das Kreditinstitut übermitteln. Durch Interpretation der Reader-ID kann das
Institut z. B. Hersteller, Gerätetyp und Version der Firmware ermitteln und in der
Kreditinstitutsantwort an den Kunden übertragen.

Realisierung Bank: optional

Realisierung Kunde: optional


# a) Kundenauftrag


# Format


<table>
<tr>
<td>Name:</td>
<td>HHD/Secoder-Informationen übermitteln</td>
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
<td>HKHSI</td>
</tr>
<tr>
<td>Bezugssegment:</td>
<td>-</td>
</tr>
<tr>
<td>Segmentversion:</td>
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
<td>TAN-Medium- Klasse</td>
<td>2</td>
<td>DE</td>
<td>code</td>
<td>1</td>
<td>M</td>
<td>1</td>
<td>G, S</td>
</tr>
<tr>
<td>3</td>
<td>Reader-ID</td>
<td>1</td>
<td>DE</td>
<td>id</td>
<td>#</td>
<td>C</td>
<td>1</td>
<td>M: bei DE ,,TAN-Medium- Klasse" = ,G" und DE ,,Reader-ID erforderlich" = „J“<br>O: bei DE ,,TAN-Medium- Klasse" = ,G" und DE ,Reader-ID erforderlich" = „N“ N: sonst</td>
</tr>
<tr>
<td>4</td>
<td>Verfahrensbestäti- gung</td>
<td>1</td>
<td>DE</td>
<td>jn</td>
<td>#</td>
<td>C</td>
<td>1</td>
<td>M: bei DE ,,Verfahrensbe- stätigung erforderlich“ = „J“ (BPD)<br>O: sonst</td>
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
<td>Security - Sicherheitsverfahren PIN/TAN</td>
<td>3.0-FV</td>
</tr>
<tr>
<td>Kapitel:</td>
<td>PIN/TAN-Management</td>
<td>Stand:</td>
<td>Seite:</td>
</tr>
<tr>
<td>Abschnitt:</td>
<td>Management chipTAN, mobileTAN und bilaterale Verfahren</td>
<td>23.02.2018</td>
<td>71</td>
</tr>
</table>


# ◆ Belegungsrichtlinien


## TAN-Medium-Klasse

Als TAN-Medium-Klasse kann entweder ,,G“ für TAN-Generator bzw. HHD
oder „S“ für Secoder angegeben werden.


## Reader-ID

Bei der TAN-Medium-Klasse ,,G“ für HHD kann die Reader-ID belegt werden,
wenn diese institutsseitig nicht bekannt ist und abgeglichen bzw. erfasst wer-
den soll. Durch den BPD-Parameter ,,Reader-ID erforderlich" kann gesteuert
werden, ob die Angabe der Reader-ID zwingend für die Ausführung des Ge-
schäftsvorfalls erforderlich ist.

Bei der TAN-Medium-Klasse ,,S“ für Secoder darf die Reader-ID nicht übertra-
gen werden, da diese als Teil des Sicherheitskonzeptes im Rahmen der ,,Vi-
sualisation Authentication" des Secoders als gemeinsames Geheimnis zwi-
schen Secoder und Institutsseite verwendet wird.


## b) Kreditinstitutsrückmeldung


## Erläuterungen

Es wird ein Datensegment zurückgemeldet.


## ◆ Format


<table>
<tr>
<td>Name:</td>
<td>HHD/Secoder Informationen rückmelden</td>
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
<td>HIHSI</td>
</tr>
<tr>
<td>Bezugssegment:</td>
<td>HKHSI</td>
</tr>
<tr>
<td>Segmentversion:</td>
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
<td>Reader-ID</td>
<td>1</td>
<td>DE</td>
<td>id</td>
<td>#</td>
<td>C</td>
<td>1</td>
<td>O: bei DE ,,TAN-Medium- Klasse“ = „G“ N: sonst</td>
</tr>
<tr>
<td>3</td>
<td>Gerätehersteller</td>
<td>1</td>
<td>DE</td>
<td>an</td>
<td>..64</td>
<td>O</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>4</td>
<td>Geräteklasse</td>
<td>1</td>
<td>DE</td>
<td>an</td>
<td>.64</td>
<td>O</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>5</td>
<td>Gerätebezeichnung</td>
<td>1</td>
<td>DE</td>
<td>an</td>
<td>.64</td>
<td>O</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>6</td>
<td>Geräteversion</td>
<td>1</td>
<td>DE</td>
<td>an</td>
<td>..64</td>
<td>O</td>
<td>1</td>
<td></td>
</tr>
</table>


## ◆ Ausgewählte Beispiele für Rückmeldungscodes


<table>
<tr>
<td>Code</td>
<td>Beispiel für Rückmeldungstext</td>
</tr>
<tr>
<td>0020</td>
<td>Auftrag verarbeitet</td>
</tr>
</table>


<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: B</td>
<td>Version: 3.0-FV</td>
<td>Financial Transaction Services (FinTS) Dokument: Security - Sicherheitsverfahren PIN/TAN</td>
</tr>
<tr>
<td>Seite:<br>72</td>
<td>Stand: 23.02.2018</td>
<td>Kapitel: PIN/TAN-Management<br>Abschnitt: Management chipTAN, mobileTAN und bilaterale Verfahren</td>
</tr>
</table>


## c) Bankparameterdaten


### Format


<table>
<tr>
<td>Name:</td>
<td>HHD/Secoder Informationen Parameter</td>
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
<td>HIHSIS</td>
</tr>
<tr>
<td>Bezugssegment:</td>
<td>HKVVB</td>
</tr>
<tr>
<td>Segmentversion:</td>
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
<td>Parameter HHD/Secoder In- formationen</td>
<td>1</td>
<td>DEG</td>
<td></td>
<td></td>
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
<th rowspan="2">Kapitel: B</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Security - Sicherheitsverfahren PIN/TAN</td>
<td>3.0-FV</td>
</tr>
<tr>
<td>Kapitel:<br>Abschnitt:</td>
<td>PIN/TAN-Management<br>Management chipTAN, mobileTAN und bilaterale Verfahren</td>
<td>Stand: 23.02.2018</td>
<td>Seite: 73</td>
</tr>
</table>


#### C.3.2 TAN-Medium an- bzw. ummelden in Segmentversion #3

Mit Hilfe dieses Geschäftsvorfalls kann der Kunde seinem Institut mitteilen, welches
Medium (Chipkarte, TAN-Generator oder bilateral vereinbart) er für die Autorisierung
der Aufträge per TAN verwenden wird.

Welches Medium gerade aktiv ist, kann mit Hilfe des Geschäftsvorfalls „TAN-
Medium anzeigen Bestand (HKTAB)“ bzw. für Detailinformationen zur Karte auch
„Kartenanzeige anfordern (HKAZK)" durch den Kunden erfragt werden.

Der Kunde entscheidet selbst, welches seiner verfügbaren TAN-Medien er verwen-
den möchte.

chipTAN-Verfahren:

Steht beim chipTAN-Verfahren ein Kartenwechsel an, so kann der Kunde mit die-
sem Geschäftsvorfall seine Karte bzw. Folgekarte aktivieren. Kann der Kunde meh-
rere Karten verwenden, dann kann mit diesem GV die Ummeldung auf eine andere
Karte erfolgen. Das Kreditinstitut entscheidet selbst, ob dieser GV TAN-pflichtig ist
oder nicht.

Realisierung Bank:
optional

Realisierung Kunde: optional


## a) Kundenauftrag


## Format


<table>
<tr>
<td>Name:</td>
<td>TAN-Medium an- bzw. ummelden</td>
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
<td>HKTAU</td>
</tr>
<tr>
<td>Bezugssegment:</td>
<td>-</td>
</tr>
<tr>
<td>Segmentversion:</td>
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
<td>TAN-Medium- Klasse</td>
<td>4</td>
<td>DE</td>
<td>code</td>
<td>1</td>
<td>M</td>
<td>1</td>
<td>A, L, G, M, S, B</td>
</tr>
<tr>
<td>3</td>
<td>Kartennummer</td>
<td>1</td>
<td>DE</td>
<td>id</td>
<td>#</td>
<td>C</td>
<td>1</td>
<td>M: DE ,,TAN-Medium- Klasse“=“G“ N: sonst</td>
</tr>
<tr>
<td>4</td>
<td>Kartenfolgenummer</td>
<td>1</td>
<td>DE</td>
<td>id</td>
<td>#</td>
<td>C</td>
<td>1</td>
<td>M: DE ,,TAN-Medium- Klasse"="G" und DE ,,Ein- gabe Kartenfolgenummer J/N" (BPD)="J" N: sonst</td>
</tr>
<tr>
<td>5</td>
<td>Kartenart</td>
<td>1</td>
<td>DE</td>
<td>num</td>
<td>..2</td>
<td>C</td>
<td>1</td>
<td>O: DE ,,TAN-Medium- Klasse"="G" und DE ,,Ein- gabe Kartenart zulässig“ (BPD) = „J“ N: sonst</td>
</tr>
<tr>
<td>6</td>
<td>Kontoverbindung international Auf- traggeber</td>
<td>1</td>
<td>DE</td>
<td>kti</td>
<td>#</td>
<td>C</td>
<td>1</td>
<td>M: DE ,,TAN-Medium- Klasse"="G" und DE ,,Kon- toverbindung erforderlich" (BPD)="J"</td>
</tr>
</table>


<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: B</td>
<td>Version: 3.0-FV</td>
<td>Financial Transaction Services (FinTS) Dokument: Security - Sicherheitsverfahren PIN/TAN</td>
</tr>
<tr>
<td>Seite:<br>74</td>
<td>Stand: 23.02.2018</td>
<td>Kapitel: PIN/TAN-Management<br>Abschnitt: Management chipTAN, mobileTAN und bilaterale Verfahren</td>
</tr>
</table>


<table>
<tr>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>O: sonst</td>
</tr>
<tr>
<td>7</td>
<td>gültig ab</td>
<td>1</td>
<td>DE</td>
<td>dat</td>
<td>#</td>
<td>C</td>
<td>1</td>
<td>O: DE ,,TAN-Medium- Klasse“=“G“ N: sonst</td>
</tr>
<tr>
<td>8</td>
<td>gültig bis</td>
<td>1</td>
<td>DE</td>
<td>dat</td>
<td>#</td>
<td>C</td>
<td>1</td>
<td>O: DE ,,TAN-Medium- Klasse“=“G“ N: sonst</td>
</tr>
<tr>
<td>9</td>
<td>ICCSN</td>
<td>1</td>
<td>DE</td>
<td>num</td>
<td>.. 19</td>
<td>C</td>
<td>1</td>
<td>O: DE ,,TAN-Medium- Klasse“=“G“ N: sonst</td>
</tr>
<tr>
<td>10</td>
<td>TAN-Listennummer</td>
<td>1</td>
<td>DE</td>
<td>an</td>
<td>..20</td>
<td>C</td>
<td>1</td>
<td>M: DE ,,TAN-Medium- Klasse"="L" und DE ,,Ein- gabe TAN-Listennummer J/N" (BPD)="J" O: DE „TAN-Medium- Klasse"="L" und DE ,,Ein- gabe TAN-Listennummer J/N" (BPD)="N" N: sonst</td>
</tr>
<tr>
<td>11</td>
<td>ATC</td>
<td>1</td>
<td>DE</td>
<td>num</td>
<td>..5</td>
<td>C</td>
<td>1</td>
<td>M: DE ,,TAN-Medium- Klasse"="G" und DE ,,Ein- gabe von ATC und TAN er- forderlich" (BPD)="J" N: sonst</td>
</tr>
<tr>
<td>12</td>
<td>TAN</td>
<td>1</td>
<td>DE</td>
<td>an</td>
<td>.99</td>
<td>C</td>
<td>1</td>
<td>M: DE ,,TAN-Medium- Klasse"="G" und DE ,,Ein- gabe von ATC und TAN er- forderlich" (BPD)="J" N: sonst</td>
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
<td>Security - Sicherheitsverfahren PIN/TAN</td>
<td>3.0-FV</td>
</tr>
<tr>
<td>Kapitel:</td>
<td>PIN/TAN-Management</td>
<td>Stand:</td>
<td>Seite:</td>
</tr>
<tr>
<td>Abschnitt:</td>
<td>Management chipTAN, mobileTAN und bilaterale Verfahren</td>
<td>23.02.2018</td>
<td>75</td>
</tr>
</table>


# ◆ Belegungsrichtlinien

TAN-Listennummer

Wird keine TAN-Listennummer angegeben, so wird die aktuelle / freigeschal-
tete Liste verwendet.

Gültig ab, Gültig bis

Die übliche Angabe im Format JJMM muss in diesem Fall auf ein existieren-
des Datumsformat umgesetzt werden (z. B. Gültig bis „9912“ wird umgesetzt
in „19991231“).

Kartenart

Die Eingabe der Kartenart wird über den BPD-Parameter ,,Eingabe Kartenart
zulässig“ gesteuert. Ist dieser Parameter auf „J“ gesetzt, enthält das BPD-
Segment HITAUS auch die zulässigen Kartenarten.


# b) Kreditinstitutsrückmeldung


# ◆ Format

Allgemeine Kreditinstitutsnachricht ohne Datensegmente

Ausgewählte Beispiele für Rückmeldungscodes


<table>
<tr>
<td>Code</td>
<td>Beispiel für Rückmeldungstext</td>
</tr>
<tr>
<td>0020</td>
<td>An- bzw. Ummeldung erfolgreich</td>
</tr>
<tr>
<td>9935</td>
<td>An- bzw. Ummeldung fehlgeschlagen</td>
</tr>
<tr>
<td>9935</td>
<td>Kartennummer unbekannt</td>
</tr>
<tr>
<td>9935</td>
<td>Karte als TAN-Generator nicht zugelassen - bitte wenden Sie sich an Ihr Institut</td>
</tr>
</table>


# c) Bankparameterdaten


# Format


<table>
<tr>
<td>Name:</td>
<td>TAN-Medium an- bzw. ummelden Parameter</td>
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
<td>HITAUS</td>
</tr>
<tr>
<td>Bezugssegment:</td>
<td>HKVVB</td>
</tr>
<tr>
<td>Segmentversion:</td>
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
<td>Parameter TAN- Generator An- bzw. Ummelden</td>
<td>3</td>
<td>DEG</td>
<td></td>
<td></td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
</table>


<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: B</td>
<td>Version: 3.0-FV</td>
<td>Financial Transaction Services (FinTS) Dokument: Security - Sicherheitsverfahren PIN/TAN</td>
</tr>
<tr>
<td>Seite:<br>76</td>
<td>Stand: 23.02.2018</td>
<td>Kapitel: PIN/TAN-Management<br>Abschnitt: Management chipTAN, mobileTAN und bilaterale Verfahren</td>
</tr>
</table>


## C.3.3 TAN-Generator Synchronisierung

Mit Hilfe dieses Geschäftsvorfalls ist eine explizite Synchronisierung eines TAN-
Generators nach dem chipTAN-Verfahren möglich. Als „TAN-Generator" wird die
entsprechende TAN-Applikation (Debit oder Credit) auf der SECCOS-Chipkarte be-
zeichnet. Im Regelfall erfolgt die Synchronisierung implizit, d. h. das Kreditinstituts-
system führt aufgrund eines Vergleichs des in der TAN übermittelten Zählers (ATC)
und des im Institut geführten Zählers eine automatische Synchronisierung durch.
Falls aufgrund eines zu starken Divergierens dieser beiden Zähler eine implizite
Synchronisierung nicht mehr möglich ist, muss der Kunde durch diesen Geschäfts-
vorfall eine explizite Synchronisierung veranlassen.

Um die Synchronisierung durchführen zu können, muss der Kunde den aktuellen
ATC im chipTAN-Lesegerät zur Anzeige bringen und zusammen mit der zugehöri-
gen TAN an das Kreditinstitut übermitteln. Diese TAN wird zusammen mit der PIN
im Sicherheitskopf übertragen.


![](figures/76.1)


Da bei der vierten Falscheingabe der TAN-Generator kreditinsti-
tutsseitig gesperrt wird, sollte das Kundenprodukt den Kunden spä-
testens nach der dritten Ablehnung einer TAN zu einer expliziten
Synchronisierung auffordern, da in diesem Fall zu vermuten ist,
dass der Fehler nicht auf einer Falscheingabe des Kunden, sondern
auf einem Synchronisierungsproblem beruht.

Realisierung Bank: verpflichtend, wenn das chipTAN-Verfahren unterstützt wird
Realisierung Kunde: optional

<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th>Version:</th>
<th rowspan="2">Kapitel: B</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Security - Sicherheitsverfahren PIN/TAN</td>
<td>3.0-FV</td>
</tr>
<tr>
<td>Kapitel:</td>
<td>PIN/TAN-Management</td>
<td>Stand:</td>
<td>Seite:</td>
</tr>
<tr>
<td>Abschnitt:</td>
<td>Management chipTAN, mobileTAN und bilaterale Verfahren</td>
<td>23.02.2018</td>
<td>77</td>
</tr>
</table>


# a) Kundenauftrag


## Format


<table>
<tr>
<td>Name:</td>
<td>TAN-Generator Synchronisierung</td>
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
<td>HKTSY</td>
</tr>
<tr>
<td>Bezugssegment:</td>
<td>-</td>
</tr>
<tr>
<td>Segmentversion:</td>
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
<td>ATC</td>
<td>1</td>
<td>DE</td>
<td>num</td>
<td>..5</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>3</td>
<td>TAN</td>
<td>1</td>
<td>DE</td>
<td>an</td>
<td>.99</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>4</td>
<td>Kartennummer</td>
<td>1</td>
<td>DE</td>
<td>id</td>
<td>#</td>
<td>C</td>
<td>1</td>
<td>M: DE ,,Eingabe der Kar- tennummer J/N" (BPD)="J" N: sonst</td>
</tr>
<tr>
<td>5</td>
<td>Kartenfolgenummer</td>
<td>1</td>
<td>DE</td>
<td>id</td>
<td>#</td>
<td>C</td>
<td>1</td>
<td>M: DE ,,Eingabe der Karten- folgenummer J/N" (BPD)="J" N: sonst</td>
</tr>
</table>


## b) Kreditinstitutsrückmeldung


# ◆ Format

Allgemeine Kreditinstitutsnachricht ohne Datensegmente


# ◆ Ausgewählte Beispiele für Rückmeldungscodes


<table>
<tr>
<td>Code</td>
<td>Beispiel für Rückmeldungstext</td>
</tr>
<tr>
<td>0020</td>
<td>Synchronisierung erfolgreich</td>
</tr>
<tr>
<td>3931</td>
<td>TAN-Generator gesperrt, Synchronisierung erforderlich</td>
</tr>
<tr>
<td>3933</td>
<td>TAN-Generator gesperrt, Synchronisierung erforderlich Kartennummer ##########</td>
</tr>
<tr>
<td>9931</td>
<td>TAN-Generator gesperrt</td>
</tr>
<tr>
<td>9931</td>
<td>Online-Zugang gesperrt</td>
</tr>
</table>


# c) Bankparameterdaten


# Format


<table>
<tr>
<td>Name:</td>
<td>TAN-Generator Synchronisierung Parameter</td>
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
<td>HITSYS</td>
</tr>
<tr>
<td>Bezugssegment:</td>
<td>HKVVB</td>
</tr>
<tr>
<td>Segmentversion:</td>
<td>1</td>
</tr>
<tr>
<td>Sender:</td>
<td>Kreditinstitut</td>
</tr>
</table>


<!-- PageBreak -->


<table>
<tr>
<th>Kapitel: B</th>
<th>Version: 3.0-FV</th>
<th>Financial Transaction Services (FinTS) Dokument: Security - Sicherheitsverfahren PIN/TAN</th>
</tr>
<tr>
<td>Seite:<br>78</td>
<td>Stand: 23.02.2018</td>
<td>Kapitel: PIN/TAN-Management<br>Abschnitt: Management chipTAN, mobileTAN und bilaterale Verfahren</td>
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
<tr>
<td>5</td>
<td>Parameter TAN- Generator Syn- chronisierung</td>
<td>1</td>
<td>DEG</td>
<td></td>
<td></td>
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
<th rowspan="2">Kapitel: B</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Security - Sicherheitsverfahren PIN/TAN</td>
<td>3.0-FV</td>
</tr>
<tr>
<td>Kapitel:<br>Abschnitt:</td>
<td>PIN/TAN-Management<br>Management chipTAN, mobileTAN und bilaterale Verfahren</td>
<td>Stand: 23.02.2018</td>
<td>Seite: 79</td>
</tr>
</table>


# C.3.4 Verwalten von Mobilfunkverbindungen


## C.3.4.1Mobilfunkverbindung registrieren


### C.3.4.1.1 Mobilfunkverbindung registrieren in Segmentversion #3

Mit Hilfe dieses Geschäftsvorfalls kann ein Kunde sein Mobilfunkverbindung regist-
rieren.


![](figures/79.1)


![](figures/79.2)


Dieser Geschäftsvorfall kann auch mit der Segmentkennung
HKMTS verwendet werden. Damit ist es möglich, den Geschäftsvor-
fall mit unterschiedlicher Belegung des Parameters ,,Abbuchungs-
konto erforderlich" in der BPD zur Verfügung zu stellen und damit
über die UPD eine kundenspezifische Abrechnung der SMS-Kosten
zu erreichen.


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


#### a) Kundenauftrag


##### Format


<table>
<tr>
<td>Name:</td>
<td>Mobilfunkverbindung registrieren</td>
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
<td>HKMTR</td>
</tr>
<tr>
<td>Bezugssegment:</td>
<td>-</td>
</tr>
<tr>
<td>Segmentversion:</td>
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
<td>TAN-Medium- Klasse</td>
<td>4</td>
<td>DE</td>
<td>code</td>
<td>1</td>
<td>M</td>
<td>1</td>
<td>M, B</td>
</tr>
<tr>
<td>3</td>
<td>Mobiltelefonnum- mer</td>
<td>1</td>
<td>DE</td>
<td>an</td>
<td>..35</td>
<td>M</td>
<td>1</td>
<td>M: DE ,,TAN-Medium- Klasse=“M“ O: sonst</td>
</tr>
<tr>
<td>4</td>
<td>Bezeichnung des TAN-Mediums</td>
<td>1</td>
<td>DE</td>
<td>an</td>
<td>.32</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>5</td>
<td>SMS- Abbuchungskonto</td>
<td>1</td>
<td>DEG</td>
<td>kti</td>
<td>#</td>
<td>C</td>
<td>1</td>
<td>M: DE „SMS- Abbuchungskonto erforder- lich J/N" (BPD)="J" O: sonst</td>
</tr>
<tr>
<td>6</td>
<td>Kontaktaufnahme durch Kreditinstitut erlaubt</td>
<td>1</td>
<td>DE</td>
<td>jn</td>
<td>#</td>
<td>C</td>
<td>1</td>
<td>M: DE ,,Zustimmung zur Kontaktaufnahme unter- stützt“ (BPD)=“J“ O: sonst</td>
</tr>
</table>


<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: B</td>
<td>Version: 3.0-FV</td>
<td>Financial Transaction Services (FinTS) Dokument: Security - Sicherheitsverfahren PIN/TAN</td>
</tr>
<tr>
<td>Seite:<br>80</td>
<td>Stand: 23.02.2018</td>
<td>Kapitel: PIN/TAN-Management<br>Abschnitt: Management chipTAN, mobileTAN und bilaterale Verfahren</td>
</tr>
</table>


#### ◆ Belegungsrichtlinien


##### Mobiltelefonnummer

Es muss die Mobiltelefonnummer verwendet werden, die mit dem Institut für
die Nutzung von mobileTAN vereinbart ist. Es sind nur Ziffern inklusive füh-
render Nullen erlaubt und es gilt die nationale Schreibweise für Telefonnum-
mern, z. B. 0170/1234567 oder (0170) 1234567.


![](figures/80.1)


Das Kundensystem sollte den Kunden bei der Eingabe eines
korrekten Telefonnummern-Formates unterstützen.


![](figures/80.2)


Falls der Prozess vorsieht, dass die Registrierung der Mobilte-
lefonnummer zuvor auf alternativem Weg erfolgen muss, kön-
nen nur im Vorfeld vereinbarte Rufnummern verwendet wer-
den. Das Institut muss in diesem Fall die Existenz einer ent-
sprechenden Vereinbarung prüfen.


#### b) Kreditinstitutsrückmeldung


##### ◆ Erläuterungen

Es werden keine Datensegmente zurückgemeldet.


##### ◆ Ausgewählte Beispiele für Rückmeldungscodes


<table>
<tr>
<td>Code</td>
<td>Beispiel für Rückmeldungstext</td>
</tr>
<tr>
<td>0020</td>
<td>Auftrag verarbeitet</td>
</tr>
<tr>
<td>9939</td>
<td>MobileTAN-Mobilrufnummer nicht zur Registrierung zugelassen</td>
</tr>
<tr>
<td>9939</td>
<td>Format der mobileTAN-Mobilrufnummer nicht korrekt</td>
</tr>
<tr>
<td>9939</td>
<td>MobileTAN-Mobilrufnummer bereits registriert</td>
</tr>
</table>


##### c) Bankparameterdaten


##### ◆ Format


<table>
<tr>
<td>Name:</td>
<td>Mobilfunkverbindung registrieren Parameter</td>
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
<td>HIMTRS</td>
</tr>
<tr>
<td>Bezugssegment:</td>
<td>HKVVB</td>
</tr>
<tr>
<td>Segmentversion:</td>
<td>3</td>
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
<th>Version:</th>
<th rowspan="2">Kapitel: B</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Security - Sicherheitsverfahren PIN/TAN</td>
<td>3.0-FV</td>
</tr>
<tr>
<td>Kapitel:<br>Abschnitt:</td>
<td>PIN/TAN-Management<br>Management chipTAN, mobileTAN und bilaterale Verfahren</td>
<td>Stand: 23.02.2018</td>
<td>Seite: 81</td>
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
<td>Num</td>
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
<td>Parameter Mobil- funkverbindung re- gistrieren</td>
<td>2</td>
<td>DEG</td>
<td></td>
<td></td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
</table>


## C.3.4.2Mobilfunkverbindung freischalten


### C.3.4.2.1 Mobilfunkverbindung freischalten in Segmentversion #3

Mit Hilfe dieses Geschäftsvorfalls kann ein Kunde seine zuvor registrierte Mobil-
funkverbindung freischalten.

Realisierung Bank: optional

Realisierung Kunde: optional


## a) Kundenauftrag


## Format


<table>
<tr>
<td>Name:</td>
<td>Mobilfunkverbindung freischalten</td>
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
<td>HKMTF</td>
</tr>
<tr>
<td>Bezugssegment:</td>
<td>-</td>
</tr>
<tr>
<td>Segmentversion:</td>
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
<td>TAN-Medium- Klasse</td>
<td>4</td>
<td>DE</td>
<td>code</td>
<td>1</td>
<td>M</td>
<td>1</td>
<td>M, B</td>
</tr>
<tr>
<td>3</td>
<td>Bezeichnung des TAN-Mediums</td>
<td>1</td>
<td>DE</td>
<td>an</td>
<td>.32</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>4</td>
<td>Freischaltcode</td>
<td>2</td>
<td>DE</td>
<td>an</td>
<td>..64</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
</table>


## b) Kreditinstitutsrückmeldung


## Erläuterungen

Es werden keine Datensegmente zurückgemeldet.


## ◆ Ausgewählte Beispiele für Rückmeldungscodes


<table>
<tr>
<td>Code</td>
<td>Beispiel für Rückmeldungstext</td>
</tr>
<tr>
<td>0020</td>
<td>Mobiltelefon für mobileTAN freigeschaltet</td>
</tr>
<tr>
<td>9939</td>
<td>mobileTAN-Mobilrufnummer kann nicht freigeschaltet werden</td>
</tr>
</table>


<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: B</td>
<td>Version: 3.0-FV</td>
<td>Financial Transaction Services (FinTS) Dokument: Security - Sicherheitsverfahren PIN/TAN</td>
</tr>
<tr>
<td>Seite:<br>82</td>
<td>Stand: 23.02.2018</td>
<td>Kapitel: PIN/TAN-Management<br>Abschnitt: Management chipTAN, mobileTAN und bilaterale Verfahren</td>
</tr>
</table>


<table>
<tr>
<td>Code</td>
<td>Beispiel für Rückmeldungstext</td>
</tr>
<tr>
<td>3939</td>
<td>mobileTAN-Freischaltung erforderlich. SMS-Freischaltcode wurde versendet</td>
</tr>
</table>


## c) Bankparameterdaten


### . Beschreibung

Geschäftsvorfallspezifische Parameter existieren nicht.


## ◆ Format


<table>
<tr>
<td>Name:</td>
<td>Mobilfunkverbindung freischalten Parameter</td>
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
<td>HIMTFS</td>
</tr>
<tr>
<td>Bezugssegment:</td>
<td>HKVVB</td>
</tr>
<tr>
<td>Segmentversion:</td>
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


# C.3.4.3Mobilfunkverbindung ändern


## C.3.4.3.1 Mobilfunkverbindung ändern in Segmentversion #3

Mit Hilfe dieses Geschäftsvorfalls kann ein Kunde seine Mobilfunkverbindung bzw.
die damit verbundenen Informationen ändern.


![](figures/82.1)


![](figures/82.2)


Dieser Geschäftsvorfall kann auch mit der Segmentkennung
HKMTB verwendet werden. Damit ist es möglich, den Geschäftsvor-
fall mit unterschiedlicher Belegung des Parameters ,,Abbuchungs-
konto erforderlich" in der BPD zur Verfügung zu stellen und damit
über die UPD eine kundenspezifische Abrechnung der SMS-Kosten
zu erreichen.

Realisierung Bank: optional

Realisierung Kunde: optional

<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th>Version:</th>
<th rowspan="2">Kapitel: B</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Security - Sicherheitsverfahren PIN/TAN</td>
<td>3.0-FV</td>
</tr>
<tr>
<td>Kapitel:<br>Abschnitt:</td>
<td>PIN/TAN-Management<br>Management chipTAN, mobileTAN und bilaterale Verfahren</td>
<td>Stand: 23.02.2018</td>
<td>Seite: 83</td>
</tr>
</table>


# a) Kundenauftrag


## Format


<table>
<tr>
<td>Name:</td>
<td>Mobilfunkverbindung ändern</td>
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
<td>HKMTA</td>
</tr>
<tr>
<td>Bezugssegment:</td>
<td>-</td>
</tr>
<tr>
<td>Segmentversion:</td>
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
<td>TAN-Medium- Klasse</td>
<td>4</td>
<td>DE</td>
<td>code</td>
<td>1</td>
<td>M</td>
<td>1</td>
<td>M, B</td>
</tr>
<tr>
<td>3</td>
<td>Mobiltelefonnum- mer</td>
<td>1</td>
<td>DE</td>
<td>an</td>
<td>..35</td>
<td>M</td>
<td>1</td>
<td>M: DE „TAN-Medium- Klasse=“M“ O: sonst</td>
</tr>
<tr>
<td>4</td>
<td>Bezeichnung des TAN-Mediums alt</td>
<td>1</td>
<td>DE</td>
<td>an</td>
<td>..32</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>5</td>
<td>Bezeichnung des TAN-Mediums neu</td>
<td>1</td>
<td>DE</td>
<td>an</td>
<td>..32</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>6</td>
<td>SMS- Abbuchungskonto</td>
<td>1</td>
<td>DEG</td>
<td>kti</td>
<td>#</td>
<td>O</td>
<td>1</td>
<td>M: DE „SMS- Abbuchungskonto erforder- lich J/N" (BPD)="J" O: sonst</td>
</tr>
<tr>
<td>7</td>
<td>Kontaktaufnahme durch Kreditinstitut erlaubt</td>
<td>1</td>
<td>DE</td>
<td>jn</td>
<td>#</td>
<td>C</td>
<td>1</td>
<td>M: DE ,,Zustimmung zur Kontaktaufnahme unter- stützt“ (BPD)=“J“ O: sonst</td>
</tr>
</table>


## ◆ Belegungsrichtlinien


### Bezeichnung des TAN-Mediums alt

Es muss die vereinbarte Bezeichnung einer bestehenden und frei geschalte-
ten Mobiltelefonnummer verwendet werden.


### b) Kreditinstitutsrückmeldung


## Erläuterungen

Es werden keine Datensegmente zurückgemeldet.


## ◆ Ausgewählte Beispiele für Rückmeldungscodes


<table>
<tr>
<td>Code</td>
<td>Beispiel für Rückmeldungstext</td>
</tr>
<tr>
<td>0020</td>
<td>Auftrag verarbeitet</td>
</tr>
<tr>
<td>9939</td>
<td>MobileTAN-Mobilrufnummer nicht zur Registrierung zugelassen</td>
</tr>
<tr>
<td>9939</td>
<td>Format der mobileTAN-Mobilrufnummer nicht korrekt</td>
</tr>
<tr>
<td>9939</td>
<td>MobileTAN-Mobilrufnummer bereits registriert</td>
</tr>
<tr>
<td>9939</td>
<td>alte mobileTAN-Mobilfunknummer existiert nicht oder ist nicht freigeschaltet</td>
</tr>
</table>


<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: B</td>
<td>Version: 3.0-FV</td>
<td>Financial Transaction Services (FinTS) Dokument: Security - Sicherheitsverfahren PIN/TAN</td>
</tr>
<tr>
<td>Seite:<br>84</td>
<td>Stand: 23.02.2018</td>
<td>Kapitel: PIN/TAN-Management<br>Abschnitt: Management chipTAN, mobileTAN und bilaterale Verfahren</td>
</tr>
</table>


## c) Bankparameterdaten


### Format


<table>
<tr>
<td>Name:</td>
<td>Mobilfunkverbindung registrieren Parameter</td>
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
<td>HIMTAS</td>
</tr>
<tr>
<td>Bezugssegment:</td>
<td>HKVVB</td>
</tr>
<tr>
<td>Segmentversion:</td>
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
<td>Parameter Mobil- funkverbindung än- dern</td>
<td>2</td>
<td>DEG</td>
<td></td>
<td></td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
</table>


#### C.3.4.4Deaktivieren / Löschen von TAN-Medien


##### C.3.4.4.1 Deaktivieren / Löschen von TAN-Medien, Segmentversion #2

Mit Hilfe dieses Geschäftsvorfalls kann ein Kunde ein aktives bzw. verfügbares
TAN-Medium deaktivieren oder löschen.

Deaktivieren, bewirkt eine Statusänderung von „aktiv“ nach „verfügbar“ für das ge-
wählte TAN-Medium.

Beim Löschvorgang wird das entsprechende TAN-Medium gänzlich von der Liste
der TAN-Medien genommen. Dieser Vorgang kann nicht mehr rückgängig gemacht
werden.

Realisierung Bank: optional

Realisierung Kunde: optional

<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th>Version:</th>
<th rowspan="2">Kapitel: B</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Security - Sicherheitsverfahren PIN/TAN</td>
<td>3.0-FV</td>
</tr>
<tr>
<td>Kapitel:</td>
<td>PIN/TAN-Management</td>
<td>Stand:</td>
<td>Seite:</td>
</tr>
<tr>
<td>Abschnitt:</td>
<td>Management chipTAN, mobileTAN und bilaterale Verfahren</td>
<td>23.02.2018</td>
<td>85</td>
</tr>
</table>


### a) Kundenauftrag


#### Format


<table>
<tr>
<td>Name:</td>
<td>TAN-Medium deaktivieren oder löschen</td>
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
<td>HKTML</td>
</tr>
<tr>
<td>Bezugssegment:</td>
<td>-</td>
</tr>
<tr>
<td>Segmentversion:</td>
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
<td>TAN-Medium- Klasse</td>
<td>4</td>
<td>DE</td>
<td>code</td>
<td>1</td>
<td>M</td>
<td>1</td>
<td>A, L, G, M, S, B</td>
</tr>
<tr>
<td>3</td>
<td>TAN-Listennummer</td>
<td>1</td>
<td>DE</td>
<td>an</td>
<td>..20</td>
<td>C</td>
<td>1</td>
<td>M: DE ,,TAN-Medium- Klasse“=“L“ N: sonst</td>
</tr>
<tr>
<td>4</td>
<td>Bezeichnung des TAN-Mediums</td>
<td>1</td>
<td>DE</td>
<td>an</td>
<td>.32</td>
<td>C</td>
<td>1</td>
<td>M: DE ,,TAN-Medium- Klasse"="M" oder „TAN- Medium-Klasse"="B" N: sonst</td>
</tr>
<tr>
<td>5</td>
<td>Deaktivie- ren/Löschen</td>
<td>1</td>
<td>DE</td>
<td>code</td>
<td>1</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
</table>


#### ◆ Belegungsrichtlinien


##### TAN-Medium-Klasse

Es muss die zu deaktivierende / zu löschende TAN-Medium-Klasse angege-
ben werden. Bei Angabe von TAN-Medium-Klasse"G" wird die als aktiv defi-
nierte Kombination aus TAN-Generator und Karte gelöscht bzw. deaktiviert.
Bei TAN-Medium-Klasse="L" oder ,,M" / ,B" muss die Angabe der TAN-
Listennummer bzw. der Bezeichnung des TAN-Mediums erfolgen.


![](figures/85.1)


Das Kundensystem sollte den Kunden darauf hinweisen,
wenn er versuchen will, das letzte im Bestand des Kunden-
systems bekannte TAN-Medium zu deaktivieren oder zu lö-
schen.


### b) Kreditinstitutsrückmeldung


## Erläuterungen

Es werden keine Datensegmente zurückgemeldet.

<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: B</td>
<td>Version: 3.0-FV</td>
<td>Financial Transaction Services (FinTS) Dokument: Security - Sicherheitsverfahren PIN/TAN</td>
</tr>
<tr>
<td>Seite:<br>86</td>
<td>Stand: 23.02.2018</td>
<td>Kapitel: PIN/TAN-Management<br>Abschnitt: Management chipTAN, mobileTAN und bilaterale Verfahren</td>
</tr>
</table>


## ◆ Ausgewählte Beispiele für Rückmeldungscodes


<table>
<tr>
<td>Code</td>
<td>Beispiel für Rückmeldungstext</td>
</tr>
<tr>
<td>0020</td>
<td>Auftrag verarbeitet</td>
</tr>
<tr>
<td>9958</td>
<td>Deaktivieren / Löschen für TAN-Medium nicht möglich</td>
</tr>
<tr>
<td>9958</td>
<td>TAN-Medium nicht bekannt</td>
</tr>
</table>


## c) Bankparameterdaten


## Beschreibung

Geschäftsvorfallspezifische Parameter existieren nicht.


## ◆ Format


<table>
<tr>
<td>Name:</td>
<td>TAN-Medium deaktivieren oder löschen Parameter</td>
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
<td>HITMLS</td>
</tr>
<tr>
<td>Bezugssegment:</td>
<td>HKVVB</td>
</tr>
<tr>
<td>Segmentversion:</td>
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
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th>Version:</th>
<th>Kapitel:</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Security - Sicherheitsverfahren PIN/TAN</td>
<td>3.0-FV</td>
<td>B</td>
</tr>
<tr>
<td>Kapitel:<br>Abschnitt:</td>
<td>Sonstige<br>PIN/TAN-Management</td>
<td>Stand: 23.02.2018</td>
<td>Seite: 87</td>
</tr>
</table>


# C.4 Sonstige


## C.4.1 TAN-Verbrauchsinformationen anzeigen

Dieses Segment bewirkt die Anzeige der verbrauchten TANs des Kunden.


## C.4.1.1TAN-Verbrauchsinformationen anzeigen, Segmentversion #2

Dieses Segment bewirkt die Anzeige der verbrauchten TANs des Kunden. In Seg-
mentversion #2 wurden in der DEG ,,TAN-Information" die Datenelementgruppen
,Entgelte-Abbuchungskonto" und „Transaktionskonto“ ergänzt, um beim z. B. mobi-
leTAN-Verfahren eine PSD-konforme Information für den Kunden zu ermöglichen,
auf welche Kontoverbindung die ggf. entstandenen SMS-Entgelte belastet wurden
und für welches Konto die Transaktion durchgeführt wurde. Das Transaktionskonto
kann insbesondere für eine Aufteilung der entstandenen Entgelte dienen, wenn ge-
nerell nur ein Entgelte-Abbuchungskonto für alle Konten gemeinsam verwendet
wird. Weiterhin wird in Segmentversion #2 die Möglichkeit geboten, durch die Anga-
be der Elemente ,,Von Datum" und ,,Bis Datum" in der Kundennachricht TAN-
Verbrauchsinformationen ein dadurch definiertes Zeitfenster auszugeben.

Realisierung Bank: optional

Realisierung Kunde: optional


# a) Kundenauftrag


## Beschreibung

Das Auftragssegment enthält neben dem Segmentkopf die Angaben ,,Von Datum“
und ,Bis Datum". Wenn diese beiden Felder in der Kundennachricht mitgeliefert
werden, enthält die Kreditinstitutsantwort TAN-Verbrauchsinformationen, die inner-
halb dieser Datumsgrenzen liegen.


## ◆ Format


<table>
<tr>
<td>Name:</td>
<td>TAN-Verbrauchsinformationen anfordern</td>
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
<td>HKTAZ</td>
</tr>
<tr>
<td>Bezugssegment:</td>
<td>-</td>
</tr>
<tr>
<td>Segmentversion:</td>
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
</table>


<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: B</td>
<td>Version: 3.0-FV</td>
<td>Financial Transaction Services (FinTS) Dokument: Security - Sicherheitsverfahren PIN/TAN</td>
</tr>
<tr>
<td>Seite:<br>88</td>
<td>Stand: 23.02.2018</td>
<td>Kapitel: PIN/TAN-Management<br>Abschnitt: Sonstige</td>
</tr>
</table>


## b) Kreditinstitutsrückmeldung


## Beschreibung

Je zurück zu meldender TAN-Liste ist ein Segment in die Antwortnachricht einzu-
stellen.


## ◆ Format


<table>
<tr>
<td>Name:</td>
<td>TAN-Verbrauchsinformationen rückmelden</td>
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
<td>HITAZ</td>
</tr>
<tr>
<td>Bezugssegment:</td>
<td>HKTAZ</td>
</tr>
<tr>
<td>Segmentversion:</td>
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
<td>TAN-Listenstatus</td>
<td>1</td>
<td>DE</td>
<td>code</td>
<td>1</td>
<td>O</td>
<td>1</td>
<td>A, N, S, V</td>
</tr>
<tr>
<td>3</td>
<td>TAN-Listennummer</td>
<td>1</td>
<td>DE</td>
<td>an</td>
<td>.20</td>
<td>O</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>4</td>
<td>Erstellungsdatum</td>
<td>1</td>
<td>DE</td>
<td>dat</td>
<td>#</td>
<td>O</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>5</td>
<td>Anzahl TANs pro Liste</td>
<td>1</td>
<td>DE</td>
<td>num</td>
<td>..4</td>
<td>O</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>6</td>
<td>Anzahl verbrauch- ter TANs pro Liste</td>
<td>1</td>
<td>DE</td>
<td>num</td>
<td>..4</td>
<td>O</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>7</td>
<td>TAN-Information</td>
<td>2</td>
<td>DEG</td>
<td></td>
<td></td>
<td>O</td>
<td>999</td>
<td></td>
</tr>
</table>


## . Belegungsrichtlinien

TAN-Listennummer

Kennung der TAN-Liste, die zurückgemeldet wird.


## ◆ Ausgewählte Beispiele für Rückmeldungscodes


<table>
<tr>
<td>Code</td>
<td>Beispiel für Rückmeldungstext</td>
</tr>
<tr>
<td>0020</td>
<td>Auftrag ausgeführt</td>
</tr>
</table>


## c) Bankparameterdaten


## Beschreibung

Geschäftsvorfallspezifische Parameter existieren nicht.


## ◆ Format


<table>
<tr>
<td>Name:</td>
<td>TAN-Verbrauchsinformationen Parameter</td>
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
<td>HITAZS</td>
</tr>
<tr>
<td>Bezugssegment:</td>
<td>HKVVB</td>
</tr>
<tr>
<td>Segmentversion:</td>
<td>2</td>
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
<th rowspan="2">Kapitel: B</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Security - Sicherheitsverfahren PIN/TAN</td>
</tr>
<tr>
<td>Kapitel:</td>
<td>PIN/TAN-Management</td>
<td>Stand:</td>
<td>Seite:</td>
</tr>
<tr>
<td>Abschnitt:</td>
<td>Sonstige</td>
<td>23.02.2018</td>
<td>89</td>
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


### C.4.2 TAN prüfen und ,,verbrennen"

Um eine TAN prüfen und verbrennen zu lassen, wird dem Benutzer beim Ein-
Schritt-TAN-Verfahren kein spezieller Geschäftsvorfall bereitgestellt. Vielmehr hat er
dort die Möglichkeit, in der Initialisierungsnachricht neben der PIN zusätzlich auch
eine TAN mitzuschicken.

Diese wird an die Bankanwendung übermittelt und kann dann von dieser geprüft
und entwertet werden. Die Ergebnisse der Prüfung und des Verbrennens werden
von der Bankanwendung als zusätzliche Returncodes innerhalb der Initialisierungs-
antwort zurückgemeldet.


#### Zwei-Schritt-Verfahren, Prozessvariante 1

Bei Einsatz eines Zwei-Schritt-Verfahrens bei Prozessvariante 1 wird das Prüfen
und ,,Verbrennen" von TANs nicht unterstützt.


#### Zwei-Schritt-Verfahren, Prozessvariante 2

Bei Einsatz eines Zwei-Schritt-Verfahrens darf die TAN bei Prozessvariante 2 nicht
in die Initialisierungsnachricht eingestellt werden. Die TAN-Eingabe muss über den
Geschäftsvorfall „Zwei-Schritt-TAN-Einreichung" (HKTAN, TAN-Prozess=4) einge-
leitet und über HKTAN, TAN-Prozess=2 abgewickelt werden.


![](figures/89.1)


Der Geschäftsvorfall „TAN prüfen und verbrennen“ unterscheidet
sich von einem Standardablauf dadurch, dass im ersten Schritt au-
ßer HKTAN kein Geschäftsvorfall übertragen wird.


## ◆ Beispiele für mögliche Rückmeldungscodes


<table>
<tr>
<td>Code</td>
<td>Beispiel für Rückmeldungstext</td>
</tr>
<tr>
<td>0900</td>
<td>TAN gültig</td>
</tr>
<tr>
<td>9941</td>
<td>TAN ungültig</td>
</tr>
<tr>
<td>3913</td>
<td>TAN wurde verbraucht</td>
</tr>
</table>


### C.4.3 PIN prüfen

Um eine PIN prüfen zu lassen, wird dem Benutzer kein spezieller Geschäftsvorfall
bereitgestellt. Vielmehr ist diese PIN-Prüfung innerhalb der Dialoginitialisierung im-
plizit von der Bankanwendung durchzuführen. Die PIN wird an die Bankanwendung
übermittelt und kann dort geprüft werden. Die Ergebnisse der Prüfung werden von
der Bankanwendung als zusätzliche Returncodes innerhalb der Initialisierungsant-
wort zurückgemeldet.

<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: B</td>
<td>Version: 3.0-FV</td>
<td>Financial Transaction Services (FinTS) Dokument: Security - Sicherheitsverfahren PIN/TAN</td>
</tr>
<tr>
<td>Seite: 90</td>
<td>Stand: 23.02.2018</td>
<td>Kapitel: PIN/TAN-Management<br>Abschnitt: Sonstige</td>
</tr>
</table>


#### ◆ mögliche Rückmeldungscodes


<table>
<tr>
<td>Code</td>
<td>Beispiel für Rückmeldungstext</td>
</tr>
<tr>
<td>0901</td>
<td>PIN gültig</td>
</tr>
<tr>
<td>9942</td>
<td>PIN ungültig</td>
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
<td>Security - Sicherheitsverfahren PIN/TAN</td>
<td>3.0-FV</td>
<td>D</td>
</tr>
<tr>
<td>Kapitel:</td>
<td>Data-Dictionary</td>
<td>Stand:</td>
<td>Seite:</td>
</tr>
<tr>
<td>Abschnitt:</td>
<td>Sonstige</td>
<td>23.02.2018</td>
<td>91</td>
</tr>
</table>


# D. DATA-DICTIONARY

A


## Antwort HHD_UC

Enthält im Falle eines bidirektionalen chipTAN-Verfahrens unter Secoder 3
die Antwortdaten des Secoder-Kommandos ,,SECODER TRANSMIT
HHDUC".


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
<td>ATC</td>
<td>1</td>
<td>DE</td>
<td>an</td>
<td>..5</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>2</td>
<td>Application Cryp- togram AC</td>
<td>1</td>
<td>DE</td>
<td>bin</td>
<td>.256</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>3</td>
<td>EF ID Data</td>
<td>1</td>
<td>DE</td>
<td>bin</td>
<td>.256</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>4</td>
<td>CVR</td>
<td>1</td>
<td>DE</td>
<td>bin</td>
<td>.256</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>5</td>
<td>Versionsinfo der chipTAN- Applikation</td>
<td>1</td>
<td>DE</td>
<td>bin</td>
<td>.256</td>
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
<td>1</td>
</tr>
</table>


## Antwort HHD_UC erforderlich

Nur bei bidirektionalen chipTAN-Verfahren: über diesen BPD-Parameter wird
festgelegt, ob die Inhalte der Datenelementgruppe „Antwort HHD_UC" zwin-
gend an das Kreditinstitut übertragen werden müssen oder ob dies optional
ist.


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

<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: D</td>
<td>Version: 3.0-FV</td>
<td>Financial Transaction Services (FinTS) Dokument: Security - Sicherheitsverfahren PIN/TAN</td>
</tr>
<tr>
<td>Seite:<br>92</td>
<td>Stand:<br>23.02.2018</td>
<td>Kapitel: Data-Dictionary<br>Abschnitt: Sonstige</td>
</tr>
</table>


gebenen Anzahl sein. Für Institute, die keine UPD unterstützen, bedeutet
dies, dass der Eintrag '0' in den BPD nur für Nichtkunden gilt und für Kunden
als 'mindestens 1' zu interpretieren ist.

Der Wert gilt für alle Signaturverfahren.


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


## Anzahl freie TANs

Anzahl der noch verfügbaren TANs einer TAN-Liste.


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


## Anzahl TANs pro Liste

Anzahl der TANs pro TAN-Liste. Sofern dies das Kreditinstitut anbietet, kann
der Kunde die Anzahl TANs pro Liste bei der Anforderung einer neuen TAN-
Liste wählen.


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


## Anzahl unterstützter aktiver TAN-Listen

Dieser Parameter wird z. B. bei Verwendung eines indizierten TAN-
Verfahrens eingesetzt. Unterstützt das Institut mehrere aktive TAN-Listen,
kann über diesen Parameter angegeben werden, dass die Eingabe der TAN-
Listennummer erforderlich ist.

Nicht gesetzt werden muss der Parameter, wenn das Institut mehrere Listen
unterstützt, jedoch der Kunde in der Rückantwort HITAN zusätzlich von der
Bank mitgeteilt bekommt, welche TAN auf welcher Liste zur Freischaltung
angegeben werden muss.


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


## Anzahl unterstützter aktiver TAN-Medien

Dieser Parameter wird z. B. bei Verwendung des mobileTAN-Verfahrens o-
der des dynamischen ZKA TAN-Generators eingesetzt. Unterstützt das Insti-
tut mehrere aktive TAN-Medien, kann über diesen Parameter angegeben
werden, dass die Eingabe der Bezeichnung des entsprechenden TAN-
Mediums erforderlich ist. Nicht gesetzt werden muss der Parameter, wenn
das Institut mehrere TAN-Medien unterstützt, jedoch der Kunde in der Rück-
antwort HITAN zusätzlich vom Institut mitgeteilt bekommt, mit welchem TAN-
Medium er die jeweilige TAN erzeugen muss.

<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th>Version:</th>
<th rowspan="2">Kapitel: D</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Security - Sicherheitsverfahren PIN/TAN</td>
<td>3.0-FV</td>
</tr>
<tr>
<td>Kapitel:</td>
<td>Data-Dictionary</td>
<td>Stand:</td>
<td>Seite:</td>
</tr>
<tr>
<td>Abschnitt:</td>
<td>Sonstige</td>
<td>23.02.2018</td>
<td>93</td>
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


# Anzahl verbrauchter TANs pro Liste

Anzahl der verbrauchten TANs pro TAN-Liste.


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


## Application Cryptogram AC

Nur bei bidirektionalen chipTAN-Verfahren mit Secoder 3: Bestandteil der
Antwort auf das Secoder-Kommando ,,SECODER TRANSMIT HHDUC".


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


### ATC

Der ATC (Application Transaction Counter) ist ein zentraler Bestandteil des
DK-TAN-Generators auf Basis der SECCOS-Chipkarte. Der ATC wird auf
der Chipkarte bei jedem TAN-Generierungsvorgang erhöht. Kreditinsti-
tutsseitig wird der aktuelle ATC jeweils gespeichert und geht auch in die
zentrale TAN-Berechnung mit ein. Sind die ATCs auf Kunden- und Insti-
tutsseite nicht mehr deckungsgleich (bzw. überschreitet die Differenz einen
maximal zulässigen Wert) müssen Synchronisationsverfahren durchgeführt
werden, z. B. eine explizite Synchronisierung über den Geschäftsvorfall
,TAN-Generator synchronisieren" (HKTSY).


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
<td>..5</td>
</tr>
<tr>
<td>Version:</td>
<td>1</td>
</tr>
</table>


### Auftraggeberkonto erforderlich

Parameter, der angibt, ob eine Zahlungsverkehrskontoverbindung explizit
angegeben werden muss, wenn diese im Geschäftsvorfall enthalten ist.

Diese Funktion ermöglicht das Sicherstellen einer gültigen Kontoverbindung
z. B. für die Abrechnung von SMS-Kosten bereits vor Erzeugen und Versen-
den einer (ggf. kostenpflichtigen!) TAN.

Codierung:

0: Auftraggeberkonto darf nicht angegeben werden

2: Auftraggeberkonto muss angegeben werden,
wenn im Geschäftsvorfall enthalten

<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: D</td>
<td>Version: 3.0-FV</td>
<td>Financial Transaction Services (FinTS) Dokument: Security - Sicherheitsverfahren PIN/TAN</td>
</tr>
<tr>
<td>Seite:<br>94</td>
<td>Stand:<br>23.02.2018</td>
<td>Kapitel: Data-Dictionary<br>Abschnitt: Sonstige</td>
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
<td>1</td>
</tr>
</table>


#### Auftrags-Hashwert

Er enthält im Falle des Zwei-Schritt-TAN-Verfahrens bei TAN-Prozess=1 den
Hashwert über die Daten eines Kundenauftrags (z. B. ,HKCCS"). Dieser wird
z. B. im Rahmen des Geschäftsvorfalls HKTAN vom Kunden übermittelt und
vom Kreditinstitut in der Antwortnachricht HITAN gespiegelt.

Das vom Institut verwendete Auftrags-Hashwertverfahren wird in der BPD
übermittelt. In der vorliegenden Version wird RIPEMD-160 verwendet.

In die Berechnung des Auftrags-Hashwerts geht der Bereich vom ersten bit
des Segmentkopfes bis zum letzten bit des Trennzeichens ein.

RIPEMD-160

Der Hash-Algorithmus RIPEMD-160 bildet Eingabe-Bitfolgen beliebiger Län-
ge auf einen als Bytefolge dargestellten Hash-Wert von 20 Byte (160 Bit)
Länge ab. Teil des Hash-Algorithmus ist das Padding von Eingabe-Bitfolgen
auf ein Vielfaches von 64 Byte. Das Padding erfolgt auch dann, wenn die
Eingabe-Bitfolge bereits eine Länge hat, die ein Vielfaches von 64 Byte ist.
RIPEMD-160 verarbeitet die Eingabe-Bitfolgen in Blöcken von 64 Byte Län-
ge.

Als Initialisierungsvektor dient die binäre Zeichenfolge X'01 23 45 67 89 AB
CD EF FE DC BA 98 76 54 32 10 F0 E1 D2 C3'.


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


#### Auftrags-Hashwertverfahren

Information, welches Verfahren für die Hashwertbildung über den Kunden-
auftrag verwendet werden soll. Es sind nur die in [HBCI] beschriebenen Ver-
fahren und deren Parametrisierung (Initialisierungsvektor, etc.) zulässig.

Codierung:

0: Auftrags-Hashwert nicht unterstützt

1: RIPEMD-160

2: SHA-1


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


##### Auftragsreferenz

Enthält im Falle des Zwei-Schritt-TAN-Verfahrens die Referenz auf einen
eingereichten Auftrag. Die Auftragsreferenz wird bei der späteren Einrei-

<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th>Version:</th>
<th>Kapitel:</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Security - Sicherheitsverfahren PIN/TAN</td>
<td>3.0-FV</td>
<td>D</td>
</tr>
<tr>
<td>Kapitel:</td>
<td>Data-Dictionary</td>
<td>Stand:</td>
<td>Seite:</td>
</tr>
<tr>
<td>Abschnitt:</td>
<td>Sonstige</td>
<td>23.02.2018</td>
<td>95</td>
</tr>
</table>


chung der zugehörigen TANs (mittels HKTAN bei TAN-Prozess=2 bzw. 3)
zur Referenzierung des Auftrags verwendet.


![](figures/95.1)


Da die Auftragsreferenz immer eindeutig ist, sollten Kun-
denprodukte diese als zentrale Referenzierung verwenden
und dem Kunden auch zusammen mit den Auftragsdaten
präsentieren bzw. für die Problemverfolgung leicht zugäng-
lich machen.


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


## Auftrag stornieren

Falls ein Kreditinstitut die Auftragseinreichung mit einer oder mehreren War-
nungen beantwortet, aber trotzdem in HITAN eine Challenge übermittelt,
kann das Kundenprodukt unter Verwendung der zugehörigen TAN den Auf-
trag stornieren. Für die Auftragsstornierung gelten folgende Rahmenbedin-
gungen:

1\.
Ein Auftragsstorno kann ausschließlich bei Prozessvariante 2 in
TAN-Prozess=2 erfolgen.

2\.
Der BPD-Parameter ,,Auftragsstorno erlaubt“ ist mit ,,J“ belegt.

3\.
Die Kreditinstitutsrückmeldung im ersten Schritt (Antwort auf Ein-
reichung von Auftrag und HITAN mit Belegung gemäß TAN-
Prozess=4) enthält:

• eine oder mehrere Rückmeldungen mit Bezug zum Auf-
tragssegment mit mindestens einer Warnung zu diesem
Auftrag (Rückmeldungscode=3xxx).

. ein Segment HITAN mit Belegung gemäß TAN-Prozess=4
und einer Challenge zum Auftrag.

4\.
Bei Mehrfach-TANs kann ein Storno nur in Verbindung mit der
Auftragseinreichung erfolgen, nicht bei der nachträglichen Über-
mittlung von zusätzlichen TANs.


![](figures/95.2)


Bietet ein Kreditinstitut die Möglichkeit eines Auftragsstorno
nicht an (BPD-Parameter ,,Auftragsstorno erlaubt"=N) und
übermittelt im Zusammenhang mit Warnungen als Antwort
auf die Auftragseinreichung trotzdem ein Segment HITAN in-
klusive einer Challenge, so bleibt dem Kunden nur die Mög-
lichkeit, die Challenge nicht zu beantworten und damit einen
TAN-Fehlversuch zu erzeugen, wenn er den Auftrag auf-
grund der Warnung stornieren möchte.

<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: D</td>
<td>Version: 3.0-FV</td>
<td>Financial Transaction Services (FinTS) Dokument: Security - Sicherheitsverfahren PIN/TAN</td>
</tr>
<tr>
<td>Seite:<br>96</td>
<td>Stand:<br>23.02.2018</td>
<td>Kapitel: Data-Dictionary<br>Abschnitt: Sonstige</td>
</tr>
</table>


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


### Auftragsstorno erlaubt

Über diesen Parameter wird bestimmt, ob ein Kreditinstitut unter exakt defi-
nierten Rahmenbedingungen eine Stornierung von Aufträgen zulässt oder
nicht.


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


B


#### BEN

Optional in der Antwort auf die TAN gesendete Bestätigungsnummer, die der
Kunde in diesem Fall mit der auf seiner TAN-Liste abgedruckten BEN ver-
gleichen muss.


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
<td>..99</td>
</tr>
<tr>
<td>Version:</td>
<td>1</td>
</tr>
</table>


#### Benutzerdefinierte Signatur

Enthält im Falle des PIN/TAN-Verfahrens die PIN und evtl. eine TAN. Die
PIN ist in jeder Nachricht zu senden. Ob eine TAN erforderlich ist, hängt von
den im HIPINS-Segment festgelegten Anforderungen der Geschäftsvorfälle
ab.


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
<td>6</td>
<td>PIN</td>
<td>1</td>
<td>DE</td>
<td>an</td>
<td>.99</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>7</td>
<td>TAN</td>
<td>1</td>
<td>DE</td>
<td>an</td>
<td>.99</td>
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
<td>1</td>
</tr>
</table>


### Bezeichnung des TAN-Mediums

Symbolischer Name für ein TAN-Medium wie z. B. TAN-Generator oder Mo-
biltelefon. Diese Bezeichnung kann in Verwaltungs-Geschäftsvorfällen be-
nutzt werden, wenn z. B. die Angabe der echten Handynummer aus Daten-
schutzgründen nicht möglich ist oder auch um die Benutzerfreundlichkeit zu
erhöhen.

<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th>Version:</th>
<th>Kapitel:</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Security - Sicherheitsverfahren PIN/TAN</td>
<td>3.0-FV</td>
<td>D</td>
</tr>
<tr>
<td>Kapitel:</td>
<td>Data-Dictionary</td>
<td>Stand:</td>
<td>Seite:</td>
</tr>
<tr>
<td>Abschnitt:</td>
<td>Sonstige</td>
<td>23.02.2018</td>
<td>97</td>
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
<td>..32</td>
</tr>
<tr>
<td>Version:</td>
<td>1</td>
</tr>
</table>


## Bezeichnung des TAN-Mediums alt

Symbolischer Name für ein TAN-Medium wie z. B. TAN-Generator oder Mobil-
telefon. Diese Bezeichnung kann in Verwaltungs-Geschäftsvorfällen benutzt
werden, wenn z. B. die Angabe der echten Handynummer aus Datenschutz-
gründen nicht möglich ist oder auch um die Benutzerfreundlichkeit zu erhö-
hen. In der Ausprägung mit Suffix „alt“ wird dieses Element zur Änderung der
Bezeichnung verwendet. Es muss die vereinbarte Bezeichnung einer beste-
henden und frei geschalteten Mobiltelefonnummer verwendet werden.


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
<td>..32</td>
</tr>
<tr>
<td>Version:</td>
<td>1</td>
</tr>
</table>


### Bezeichnung des TAN-Mediums neu

Symbolischer Name für ein TAN-Medium wie z. B. TAN-Generator oder Mo-
biltelefon. Diese Bezeichnung kann in Verwaltungs-Geschäftsvorfällen be-
nutzt werden, wenn z. B. die Angabe der echten Handynummer aus Daten-
schutzgründen nicht möglich ist oder auch um die Benutzerfreundlichkeit zu
erhöhen. In der Ausprägung mit Suffix ,,neu" wird dieses Element zur Ände-
rung der Bezeichnung verwendet.


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
<td>..32</td>
</tr>
<tr>
<td>Version:</td>
<td>1</td>
</tr>
</table>


### Bezeichnung des TAN-Mediums erforderlich

Abhängig vom Kreditinstitut und der Anzahl unterstützter TAN-Medien ist die
Angabe der Bezeichnung des TAN-Mediums erforderlich, damit der Kunde
dem Institut mitteilen kann, welches der TAN-Medien er verwenden möchte.

Codierung:

0: Bezeichnung des TAN-Mediums darf nicht angegeben werden

1: Bezeichnung des TAN-Mediums kann angegeben werden

2: Bezeichnung des TAN-Mediums muss angegeben werden


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


#### Bezugssegment

Sofern sich ein Kreditinstitutssegment auf ein bestimmtes Kundensegment
bezieht (z. B. Antwortrückmeldung auf einen Kundenauftrag) hat das Kredit-
institut die Segmentnummer des Segments der Kundennachricht einzustel-
len, auf das sich das aktuelle Segment bezieht (s. DE ,Segmentnummer“). In
Zusammenhang mit den Angaben zur Bezugsnachricht aus dem Nachrich-

<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: D</td>
<td>Version: 3.0-FV</td>
<td>Financial Transaction Services (FinTS) Dokument: Security - Sicherheitsverfahren PIN/TAN</td>
</tr>
<tr>
<td>Seite:<br>98</td>
<td>Stand: 23.02.2018</td>
<td>Kapitel: Data-Dictionary<br>Abschnitt: Sonstige</td>
</tr>
</table>


tenkopf ist hierdurch eine eindeutige Referenz auf das Segment einer Kun-
dennachricht möglich.

Falls die Angabe eines Bezugssegments erforderlich ist, ist dieses bei der
Formatbeschreibung eines Kreditinstitutssegments angegeben.


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


##### Bis Datum

Endedatum eines Zeitraums (s. [Formals], Kap. B.6.3 „Abholauftrag“).

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


C


##### Challenge #1

Dieses Datenelement enthält im Falle des Zwei-Schritt-TAN-Verfahrens die
Challenge zu einem eingereichten Auftrag. Aus der Challenge wird vom
Kunden die eigentliche TAN ermittelt. Die Challenge wird unabhängig von
Prozessvariante 1 oder 2 in der Kreditinstitutsantwort im Segment HITAN
übermittelt.


![](figures/98.1)


Bei der Challenge kann es sich, abhängig vom konkreten
Zwei-Schritt-Verfahren, um eine „Auftragsquersumme“, ei-
nen Hashwert, einen Index auf eine bestimmte TAN in ei-
ner Liste o. ä. handeln. Bei chipTAN-Lesern ist es auch
möglich, dass die Challenge eine textuelle Anweisung ent-
hält, beispielsweise in der Form „Tippen Sie bitte die ersten
sechs Stellen der Empfänger-IBAN und die letzten beiden
Stellen des Betrags in den chipTAN-Leser ein". Das Kun-
denprodukt braucht i. d. R. die Bildungsregel für die Chal-
lenge bzw. die Ableitung der TAN aus der Challenge nicht
zu kennen – dies ist nur zwischen Kunde und Kreditinstitut
vereinbart und Inhalt der Verfahrensanweisung des jeweili-
gen Instituts.


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
<td>.256</td>
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
<th rowspan="2">Kapitel:<br>D</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Security - Sicherheitsverfahren PIN/TAN</td>
</tr>
<tr>
<td>Kapitel:</td>
<td>Data-Dictionary</td>
<td>Stand:</td>
<td>Seite:</td>
</tr>
<tr>
<td>Abschnitt:</td>
<td>Sonstige</td>
<td>23.02.2018</td>
<td>99</td>
</tr>
</table>


##### Challenge #2

Dieses Datenelement enthält im Falle des Zwei-Schritt-TAN-Verfahrens die
Challenge zu einem eingereichten Auftrag. Aus der Challenge wird vom
Kunden die eigentliche TAN ermittelt. Die Challenge wird unabhängig von
Prozessvariante 1 oder 2 in der Kreditinstitutsantwort im Segment HITAN
übermittelt.


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
<td>.999</td>
</tr>
<tr>
<td>Version:</td>
<td>2</td>
</tr>
</table>


###### Challenge #3

Dieses Datenelement enthält im Falle des Zwei-Schritt-TAN-Verfahrens die
Challenge zu einem eingereichten Auftrag. Aus der Challenge wird vom
Kunden die eigentliche TAN ermittelt. Die Challenge wird unabhängig vom
Prozessvariante 1 oder 2 in der Kreditinstitutsantwort im Segment HITAN
übermittelt.

Ist der BPD-Parameter ,,Challenge strukturiert“ mit „J“ belegt, so können im
Text folgende Formatsteuerzeichen enthalten sein, die kundenseitig entspre-
chend zu interpretieren sind. Eine Kaskadierung von Steuerzeichen ist nicht
erlaubt.


<table>
<tr>
<td>&lt;br&gt;</td>
<td>Zeilenumbruch</td>
</tr>
<tr>
<td>&lt;p&gt;</td>
<td>Neuer Absatz</td>
</tr>
<tr>
<td>&lt;b&gt; ...</td>
<td>&lt;/b&gt; Fettdruck</td>
</tr>
<tr>
<td>&lt;i&gt; ...</td>
<td>&lt;/i&gt; Kursivdruck</td>
</tr>
<tr>
<td>&lt;u&gt; ...</td>
<td>&lt;/u&gt; Unterstreichen</td>
</tr>
<tr>
<td>&lt;ul&gt;</td>
<td>&lt;/ul&gt; Beginn / Ende Aufzählung</td>
</tr>
<tr>
<td>&lt;ol&gt;</td>
<td>&lt;/ol&gt; Beginn / Ende Nummerierte Liste</td>
</tr>
<tr>
<td>&lt;li&gt; ...</td>
<td>&lt;/li&gt;<br>Listenelement einer Aufzählung / Nummerierten Liste</td>
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
<td>..2048</td>
</tr>
<tr>
<td>Version:</td>
<td>3</td>
</tr>
</table>


<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: D</td>
<td>Version: 3.0-FV</td>
<td>Financial Transaction Services (FinTS) Dokument: Security - Sicherheitsverfahren PIN/TAN</td>
</tr>
<tr>
<td>Seite:<br>100</td>
<td>Stand: 23.02.2018</td>
<td>Kapitel: Data-Dictionary<br>Abschnitt: Sonstige</td>
</tr>
</table>


###### Challenge-Betrag erforderlich

Über diesen BPD-Parameter erhält die Kundenseite die Information, ob im
Rahmen der ,,Parameter Challenge-Klasse“ auch der Betrag übermittelt wer-
den soll oder ob dies nicht zugelassen ist.


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


###### Challenge-Betragswert

Monetärer Wert eines Auftrags ohne das zugehörige Währungskennzeichen.
Das Format des Challenge-Betragswerts entspricht dem abgeleiteten Format
,wrt" (vgl. [Formals], Kapitel B.4.2). Die genaue Belegung wird durch das
konkrete Zwei-Schritt-Verfahren vorgegeben und ist der dortigen Spezifikati-
on zu entnehmen.


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
<td>..999</td>
</tr>
<tr>
<td>Version:</td>
<td>1</td>
</tr>
</table>


###### Challenge-Betragswährung

Information über die Auftragswährung, die in Verbindung mit dem Challenge-
Betragswert zu verwenden ist. Das Format der Challenge-Betragswährung
entspricht dem abgeleiteten Format ,cur" (vgl. [Formals], Kapitel B.4.2). Die
genaue Belegung wird durch das konkrete Zwei-Schritt-Verfahren vorgege-
ben und ist der dortigen Spezifikation zu entnehmen.

Typ: DE


<table>
<tr>
<td>Format:</td>
<td>an</td>
</tr>
<tr>
<td>Länge:</td>
<td>..999</td>
</tr>
<tr>
<td>Version:</td>
<td>1</td>
</tr>
</table>


###### Challenge HHD_UC

Bei Verwendung von Zwei-Schritt-Verfahren mit unidirektionaler Kopplung
(vgl. hierzu [HHD_UC]) müssen zusätzlich zum Datenelement „Challenge"
die Daten für die Übertragung z. B. über eine optische Schnittstelle bereitge-
stellt werden. Die einzelnen Datenelemente der „Challenge HHD_UC" sind in
[HHD_UC] beschrieben und werden hier im FinTS Data Dictionary nicht nä-
her erläutert. Da HHD_UC einen anderen Basiszeichensatz verwendet (ISO
646) wird die HHD_UC-Struktur als binär definiert. Als maximale Länge kann
ein Wert von 128 angenommen werden.


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


<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th>Version:</th>
<th>Kapitel:</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Security - Sicherheitsverfahren PIN/TAN</td>
<td>3.0-FV</td>
<td>D</td>
</tr>
<tr>
<td>Kapitel:</td>
<td>Data-Dictionary</td>
<td>Stand:</td>
<td>Seite:</td>
</tr>
<tr>
<td>Abschnitt:</td>
<td>Sonstige</td>
<td>23.02.2018</td>
<td>101</td>
</tr>
</table>


###### Challenge-Klasse

Mit der Challenge-Klasse wird dem Kreditinstitut die Art des Geschäftsvor-
falls mitgeteilt, was bei Prozessvariante 1 und der Verwendung von kontext-
abhängigen konkreten Zwei-Schritt-Verfahren essentiell für die weitere Ver-
arbeitung ist. Auf Basis der durch die Challenge-Klasse festgelegten Infor-
mation kann das Kreditinstitut dem Kunden eine dazu passende Challenge
übermitteln. Welche Geschäftsvorfälle welchen Challenge-Klassen zugeord-
net werden, ist der Beschreibung des jeweiligen konkreten Zwei-Schritt-
Verfahrens zu entnehmen.


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
<td>.2</td>
</tr>
<tr>
<td>Version:</td>
<td>1</td>
</tr>
</table>


###### Challenge-Klasse erforderlich

Dieses DE kennzeichnet Zwei-Schritt-Verfahren (wie z. B. chipTAN-Leser),
bei denen für die Challenge-Ermittlung die Belegung des Elements „Challen-
ge-Klasse" in HKTAN erforderlich ist.


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


###### Challenge-Klasse Parameter

Zur jeweiligen Challenge-Klasse gehöriger Einzelparameter.


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
<td>..999</td>
</tr>
<tr>
<td>Version:</td>
<td>1</td>
</tr>
</table>


###### Challenge strukturiert

Über diesen BPD-Parameter erhält die Kundenseite die Information, dass im
Datenelement ,,Challenge" Formatsteuerzeichen enthalten sein können. Nä-
heres hierzu siehe unter DE ,,Challenge“.


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


###### CVR

Nur bei bidirektionalen chipTAN-Verfahren mit Secoder 3: Das ,,Card Valida-
tion Result (CVR)" ist Bestandteil der Antwort auf das Secoder-Kommando
"SECODER TRANSMIT HHDUC".


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


<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: D</td>
<td>Version: 3.0-FV</td>
<td>Financial Transaction Services (FinTS) Dokument: Security - Sicherheitsverfahren PIN/TAN</td>
</tr>
<tr>
<td>Seite:<br>102</td>
<td>Stand: 23.02.2018</td>
<td>Kapitel: Data-Dictionary<br>Abschnitt: Sonstige</td>
</tr>
</table>


D


####### Deaktivieren/Löschen

Mit diesem Element wird kodiert ob ein Element deaktiviert oder gelöscht
werden soll.

Codierung:

D: Deaktivieren

L: Löschen


<table>
<tr>
<td>Typ:</td>
<td>DE</td>
</tr>
<tr>
<td>Format:</td>
<td>1</td>
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


######## Dialog-ID

Die Dialog-ID dient der eindeutigen Zuordnung einer Nachricht zu einem
HBCI-Dialog. Die erste Kundennachricht (Dialoginitialisierung) enthält als Di-
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


E


######## EF_ID Data

Nur bei bidirektionalen chipTAN-Verfahren mit Secoder 3: Bestandteil der
Antwort auf das Secoder-Kommando ,,SECODER TRANSMIT HHDUC".


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


######## Eingabe Kartenart zulässig

Durch diesen Parameter wird festgelegt, ob bei Geschäftsvorfällen zum Ma-
nagement eines TAN-Generators (z. B. an-, ummelden) die Eingabe der Kar-
tenart erlaubt ist. Ist dies der Fall, so werden im zugehörigen BPD-Segment
(z. B. HITAUS) dem Kunden auch die zulässigen Kartenarten mitgeteilt.


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
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th>Version:</th>
<th>Kapitel:</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Security - Sicherheitsverfahren PIN/TAN</td>
<td>3.0-FV</td>
<td>D</td>
</tr>
<tr>
<td>Kapitel:</td>
<td>Data-Dictionary</td>
<td>Stand:</td>
<td>Seite:</td>
</tr>
<tr>
<td>Abschnitt:</td>
<td>Sonstige</td>
<td>23.02.2018</td>
<td>103</td>
</tr>
</table>


####### Eingabe Kartennummer J/N

Durch diesen Parameter wird festgelegt, ob bei Geschäftsvorfällen zum Ma-
nagement eines TAN-Generators (z. B. an-, ummelden, synchronisieren) die
Kartennummer mit angegeben werden muss.


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


####### Eingabe Kartenfolgenummer J/N

Durch diesen Parameter wird festgelegt, ob bei Geschäftsvorfällen zum Ma-
nagement eines TAN-Generators (z. B. an-, ummelden, synchronisieren) die
Kartenfolgenummer mit angegeben werden muss.


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


####### Eingabe TAN-Listennummer J/N

Durch diesen Parameter wird festgelegt, ob bei Anmeldung einer TAN-Liste
die TAN-Listennummer mit angegeben werden muss.


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


####### Eingabe von ATC und TAN erforderlich

Durch diesen Parameter wird festgelegt, ob bei Anmeldung eines TAN-
Generators zusätzlich zum ATC auch eine generierte TAN der neuen Karte
mit angegeben werden muss.


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


####### Ein-Schritt-Verfahren erlaubt

Angabe, ob Ein-Schritt-Verfahren erlaubt ist oder nicht. Darüber wird das
Kundenprodukt informiert, ob die Einreichung von Aufträgen im Ein-Schritt-
Verfahren zusätzlich zu den definierten Zwei-Schritt-Verfahren zugelassen
ist.


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


![](figures/103.1)


Wird das Ein-Schritt-TAN-Verfahren von einem Institut nicht
mehr unterstützt und reicht ein Kunde trotzdem einen Auf-
trag in diesem Verfahren ein, so sollte das Institut dies mit

<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: D</td>
<td>Version: 3.0-FV</td>
<td>Financial Transaction Services (FinTS) Dokument: Security - Sicherheitsverfahren PIN/TAN</td>
</tr>
<tr>
<td>Seite:<br>104</td>
<td>Stand: 23.02.2018</td>
<td>Kapitel: Data-Dictionary<br>Abschnitt: Sonstige</td>
</tr>
</table>


einer verständlichen Rückmeldung ablehnen, damit der
Kunde entsprechend reagieren kann. Der passende Rück-
meldecode lautet 9955 - „Ein-Schritt-TAN-Verfahren nicht
zugelassen“


##### Entgelte-Abbuchungskonto

Zahlungsverkehrskontoverbindung, die für die Abbuchung von Transaktions-
entgelten wie z. B. SMS-Kosten oder transaktionsabhängige Schutzgebüh-
ren für chipTAN-Lesegeräte herangezogen werden soll bzw. herangezogen
wurde. Inhaltlich ist SMS-Abbuchungskonto als Teilmenge gleichbedeutend
mit dem Entgelte-Abbuchungskonto.


<table>
<tr>
<td>Typ:</td>
<td>DEG</td>
</tr>
<tr>
<td>Format:</td>
<td>kti</td>
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


###### Erlaubtes Format im Zwei-Schritt-Verfahren

Angabe des erwarteten Formates der TAN im konkreten Zwei-Schritt-
Verfahren.

Codierung:

1: numerisch

2: alfanumerisch


![](figures/104.1)


Kundenprodukte sollten die Eingabe der TAN auf dieses
Format beschränken.


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


###### Erstellungsdatum

Datum der Erstellung (z. B. einer TAN-Liste)


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


F


##### Freigeschaltet am

Datum, zu dem ein TAN-Medium freigeschaltet wurde.

<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th>Version:</th>
<th rowspan="2">Kapitel: D</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Security - Sicherheitsverfahren PIN/TAN</td>
<td>3.0-FV</td>
</tr>
<tr>
<td>Kapitel:</td>
<td>Data-Dictionary</td>
<td>Stand:</td>
<td>Seite:</td>
</tr>
<tr>
<td>Abschnitt:</td>
<td>Sonstige</td>
<td>23.02.2018</td>
<td>105</td>
</tr>
</table>


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


## Freischaltcode #1

Ordnungsbegriff der zur Freischaltung eines TAN-Mediums verwendet wird.
Dieser Ordnungsbegriff wird vom Institut vorgegeben und ggf. auf alternati-
vem Weg (z. B. als SMS) an den Kunden übermittelt.


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
<td>..8</td>
</tr>
<tr>
<td>Version:</td>
<td>1</td>
</tr>
</table>


### Freischaltcode #2

Ordnungsbegriff der zur Freischaltung eines TAN-Mediums verwendet wird.
Dieser Ordnungsbegriff wird vom Institut vorgegeben und ggf. auf alternati-
vem Weg (z. B. als SMS oder per Briefpost) an den Kunden übermittelt.


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
<td>..64</td>
</tr>
<tr>
<td>Version:</td>
<td>2</td>
</tr>
</table>


G


#### Geräteklasse

Klasse, der ein HHD oder Secoder zugeordnet werden kann. Die Klasse ist
kein Bestandteil der Reader-ID und muss aus der Gerätebezeichnung abge-
leitet werden. Es handelt sich hierbei um Freitext, z. B. ,HHD manuell" bzw.
,HHD, optisch gekoppelt" oder ,Secoder I“.


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
<td>..64</td>
</tr>
<tr>
<td>Version:</td>
<td>1</td>
</tr>
</table>


##### Gerätehersteller

Herstellerbezeichnung für ein HHD oder einen Secoder, wie sie sich z. B.
aus der Reader-ID oder institutsseitigen Beständen ergibt.


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
<td>..64</td>
</tr>
<tr>
<td>Version:</td>
<td>1</td>
</tr>
</table>


### Gerätebezeichnung

Bezeichnung des HHD oder eines Secoders, wie sie sich z. B. aus der Rea-
der-ID oder institutsseitigen Beständen ergibt. Die Bezeichnung sollte ein-

<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: D</td>
<td>Version: 3.0-FV</td>
<td>Financial Transaction Services (FinTS) Dokument: Security - Sicherheitsverfahren PIN/TAN</td>
</tr>
<tr>
<td>Seite:<br>106</td>
<td>Stand:<br>23.02.2018</td>
<td>Kapitel: Data-Dictionary<br>Abschnitt:<br>Sonstige</td>
</tr>
</table>


deutig sein und möglichst viele Aufschlüsse über die exakte Art des Gerätes
geben.


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
<td>..64</td>
</tr>
<tr>
<td>Version:</td>
<td>1</td>
</tr>
</table>


## Geräteversion

Hierbei handelt es sich um die Firmware-Version des Gerätes und nicht um
die Version der HHD- oder Secoder-Spezifikation. Die Geräteversion ergibt
sich z. B. aus der Reader-ID oder institutsseitigen Beständen.


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
<td>..64</td>
</tr>
<tr>
<td>Version:</td>
<td>1</td>
</tr>
</table>


## Geschäftsvorfallspezifische PIN/TAN-Informationen

Eine DEG dieses Typs enthält für genau einen Geschäftsvorfall PIN/TAN-
relevante Informationen. Ist für einen Geschäftsvorfall eine zugehörige DEG
hinterlegt, kann das Kundenprodukt diesen Geschäftsvorfall über das
PIN/TAN-Verfahren absichern, andernfalls ist dies nicht erlaubt.

Hierdurch wird nicht festgelegt, ob und wie oft ein Geschäftsvorfall zu signie-
ren ist. Dies wird weiterhin über die BPD und UPD angegeben.

Werden mehr Signaturen eingestellt als in BPD und UPD gefordert, so sind
diese alle gemäß der Einstellungen im HIPINS-Segment zu bilden.

Werden in BPD und UPD keine Signaturen gefordert, können diese selbst
dann weggelassen werden, wenn für den betreffenden Geschäftsvorfall eine
TAN erforderlich ist.

Im Feld ,,Segmentkennung" ist die Kennung des Auftragssegments des Ge-
schäftsvorfalls anzugeben, auf den sich die PIN/TAN-Informationen bezie-
hen.


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
<td>Segmentkennung</td>
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
<td>TAN erforderlich</td>
<td>1</td>
<td>DE</td>
<td>jn</td>
<td>#</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
</table>


### Gültig ab

Datum, ab dem eine Vereinbarung oder Vertrag gilt (z.B. Gültigkeitsbeginn
einer an den Kunden ausgegebenen Karte).


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
<td>Security - Sicherheitsverfahren PIN/TAN</td>
<td>3.0-FV</td>
<td>D</td>
</tr>
<tr>
<td>Kapitel:</td>
<td>Data-Dictionary</td>
<td>Stand:</td>
<td>Seite:</td>
</tr>
<tr>
<td>Abschnitt:</td>
<td>Sonstige</td>
<td>23.02.2018</td>
<td>107</td>
</tr>
</table>


#### Gültig bis

Datum, bis zu dem eine Vereinbarung oder Vertrag gilt (z. B. Verfalldatum
einer an den Kunden ausgegebenen Karte).


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


##### Gültigkeitsdatum und -uhrzeit für Challenge

Datum und Uhrzeit, bis zu welchem Zeitpunkt eine TAN auf Basis der ge-
sendeten Challenge gültig ist. Nach Ablauf der Gültigkeitsdauer wird die ent-
sprechende TAN entwertet.


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
<td>Datum</td>
<td>DE</td>
<td>dat</td>
<td>#</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>2</td>
<td>Uhrzeit</td>
<td>DE</td>
<td>tim</td>
<td>#</td>
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
<td>1</td>
</tr>
</table>


I


#### ICCSN

= Integrated Circuit Card Serial Number. International eindeutige ID eines
Chip (z. B. eines Chip auf einer Banken-Chipkarte oder eines SIM). Die
ICCSN ist maximal 18 Stellen lang und verfügt optional an Stelle 19 über ei-
ne Prüfziffer.


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
<td>.. 19</td>
</tr>
<tr>
<td>Version:</td>
<td>1</td>
</tr>
</table>


##### Initialisierungsmodus

Bezeichnet das Verfahren, welches bei Verwendung von PIN/TAN während
der Dialoginitialisierung verwendet wird und bezieht sich dabei auf die in der
Spezifikation des HandHeldDevice [HHD] bzw. den Belegungsrichtlinien
[HHD-Belegung] definierten Schablonen 01 und 02.

Die Schablonen werden in [HHD] zwar begrifflich auch als ,,Challengeklas-
sen" bezeichnet, sind jedoch Bestandteil des dort definierten ,,Start-Code",
der in Ausgaberichtung im FinTS Datenelement „Challenge“ übertragen wird
und daher nicht zu verwechseln mit der ,,Challengeklasse" im Sinne einer
Geschäftsvorfallsklasse bei HKTAN in der Prozessvariante 1.

Codierung:

00: Initialisierungsverfahren mit Klartext-PIN ohne TAN

01: Verwendung analog der in [HHD] beschriebenen Schablone 01 - ver-
schlüsselte PIN und ohne TAN

<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: D</td>
<td>Version: 3.0-FV</td>
<td>Financial Transaction Services (FinTS) Dokument: Security - Sicherheitsverfahren PIN/TAN</td>
</tr>
<tr>
<td>Seite:<br>108</td>
<td>Stand: 23.02.2018</td>
<td>Kapitel: Data-Dictionary<br>Abschnitt: Sonstige</td>
</tr>
</table>


02: Verwendung analog der in [HHD] beschriebenen Schablone 02 - reser-
viert, bei FinTS derzeit nicht verwendet


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
<td>2</td>
</tr>
<tr>
<td>Version:</td>
<td>1</td>
</tr>
</table>


K


#### Kartenart

Angabe zur Kartenart der Karte, auf die der Kundenauftrag oder die Kreditin-
stituts-Rückmeldung bezieht.

Die je Kreditinstitut angebotenen Kartenarten sind in den BPD eingestellt.


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


##### Kartennummer

Kartennummer der SECCOS-Karte, die beim DK-TAN-Generator verwendet
wird.


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


##### Kartenfolgenummer

Kartenfolgenummer der SECCOS-Karte, die beim DK-TAN-Generator ver-
wendet wird.


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


##### Kontaktaufnahme durch Kreditinstitut erlaubt

Über dieses Datenelement wird festgelegt, ob der Kunde einer Kontaktauf-
nahme des Kreditinstituts über das registrierte TAN-Medium zustimmt. oder
nicht. Wird das Datenelement weggelassen, gilt entsprechend den FinTS-
Konventionen die Belegung ,,N".

<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th>Version:</th>
<th>Kapitel:</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Security - Sicherheitsverfahren PIN/TAN</td>
<td>3.0-FV</td>
<td>D</td>
</tr>
<tr>
<td>Kapitel:</td>
<td>Data-Dictionary</td>
<td>Stand:</td>
<td>Seite:</td>
</tr>
<tr>
<td>Abschnitt:</td>
<td>Sonstige</td>
<td>23.02.2018</td>
<td>109</td>
</tr>
</table>


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


##### Kontoverbindung Auftraggeber #3

Kontoverbindung des Auftraggebers, auf die sich der aktuelle Auftrag be-
zieht.


<table>
<tr>
<td>Typ:</td>
<td>DEG</td>
</tr>
<tr>
<td>Format:</td>
<td>ktv</td>
</tr>
<tr>
<td>Länge:</td>
<td>#</td>
</tr>
<tr>
<td>Version:</td>
<td>3</td>
</tr>
</table>


##### Kontoverbindung erforderlich

Über dieses Datenelement wird festgelegt, ob die Angabe der Kontoverbin-
dung erfolgen muss oder optional ist.


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


##### Kontoverbindung international Auftraggeber

Kontoverbindung des Auftraggebers (Konto / BLZ bzw. IBAN), auf die sich
der aktuelle Auftrag bezieht.


<table>
<tr>
<td>Typ:</td>
<td>DEG</td>
</tr>
<tr>
<td>Format:</td>
<td>kti</td>
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


#### Letzte Benutzung

Datum, an dem das TAN-Medium das letzte Mal benutzt wurde


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


M


#### Maximale Anzahl Aufträge

Höchstens zulässige Anzahl an Segmenten der jeweiligen Auftragsart je
Kundennachricht. Übersteigt die Anzahl der vom Kunden übermittelten Seg-
mente pro Auftragsart die zugelassene Maximalanzahl, so wird die gesamte
Nachricht abgelehnt.

<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: D</td>
<td>Version: 3.0-FV</td>
<td>Financial Transaction Services (FinTS) Dokument: Security - Sicherheitsverfahren PIN/TAN</td>
</tr>
<tr>
<td>Seite:<br>110</td>
<td>Stand: 23.02.2018</td>
<td>Kapitel: Data-Dictionary<br>Abschnitt: Sonstige</td>
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


##### Maximale Länge des Rückgabewertes im Zwei-Schritt-Verfahren #1

Angabe der Länge der vom Institut übermittelten maximalen Länge des
Rückgabewertes (maximal 256 Stellen) im konkreten Zwei-Schritt-Verfahren.


![](figures/110.1)


Kundenprodukte sollten für die Anzeige des Rückgabewer-
tes ein geeignetes Anzeigefenster, ggf. mit Scrollbar vorse-
hen.


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


###### Maximale Länge des Rückgabewertes im Zwei-Schritt-Verfahren #2

Angabe der Länge der vom Institut übermittelten maximalen Länge des
Rückgabewertes (maximal 999 Stellen) im konkreten Zwei-Schritt-Verfahren.


![](figures/110.2)


Kundenprodukte sollten für die Anzeige des Rückgabewer-
tes ein geeignetes Anzeigefenster, ggf. mit Scrollbar vorse-
hen.


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


###### Maximale Länge des Rückgabewertes im Zwei-Schritt-Verfahren #3

Angabe der Länge der vom Institut übermittelten maximalen Länge des
Rückgabewertes (maximal 2048 Stellen) im konkreten Zwei-Schritt-
Verfahren.


![](figures/110.3)


Kundenprodukte sollten für die Anzeige des Rückgabewer-
tes ein geeignetes Anzeigefenster, ggf. mit Scrollbar vorse-
hen.


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
<td>.4</td>
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
<th>Version:</th>
<th>Kapitel:</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Security - Sicherheitsverfahren PIN/TAN</td>
<td>3.0-FV</td>
<td>D</td>
</tr>
<tr>
<td>Kapitel:</td>
<td>Data-Dictionary</td>
<td>Stand:</td>
<td>Seite:</td>
</tr>
<tr>
<td>Abschnitt:</td>
<td>Sonstige</td>
<td>23.02.2018</td>
<td>111</td>
</tr>
</table>


##### Maximale Länge des TAN-Eingabewertes im Zwei-Schritt-Verfahren

Angabe der erwarteten maximalen Länge der TAN im konkreten Zwei-
Schritt-Verfahren.


![](figures/111.1)


Kundenprodukte sollten die Eingabe der TAN auf diesen
Wert (maximal 99 Stellen) beschränken.


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


###### Maximale PIN-Länge

Maximale Länge der PIN. Wenn das Kreditinstitut eine feste PIN-Länge er-
wartet, sind minimale und maximale PIN-Länge auf denselben Wert zu set-
zen.


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


###### Maximale TAN-Länge

Maximale Länge einer TAN.


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


###### Mehr als ein TAN-pflichtiger Auftrag pro Nachricht erlaubt

Angabe, ob in einer FinTS-Nachricht mehr als ein TAN-pflichtiger Auftrag
gesendet werden darf. Bei Angabe von ,,N" darf in einer FinTS-Nachricht nur
ein TAN-pflichtiger Auftrag enthalten sein. Bei Angabe von ,J" wird die ma-
ximale Anzahl der TAN-pflichtigen Aufträge analog dem Geschäftsvorfallpa-
rameter „Maximale Anzahl Aufträge“ in der BPD bestimmt (vgl. [Formals],
Kapitel D.6). Die Option bezieht sich auf die Anzahl der in der Nachricht ent-
haltenen Aufträge, nicht auf die Anzahl der TANs, d. h. es ist pro Signaturab-
schluss nur eine TAN erlaubt, die bei Angabe von ,,J" aber ggf. für mehrere
Aufträge gilt. Dieser Parameter gilt sowohl für das Einschritt- als auch das
Zwei-Schritt-Verfahren.


![](figures/111.2)


Mit Einführung der Zahlungsdienstrichtlinie PSD2 (verglei-
che [PSD2]) ist die Angabe von ,,J“ nicht mehr erlaubt, da
das dort geforderte dynamic linking sowie die Transparenz
bzgl. Empfänger-IBAN und Betrag gegenüber dem Kunden
auftragsbezogen gilt.

Um die Anzahl der FinTS-Nachrichten zu minimieren wird
empfohlen, die Option ,,Alle Konten“ = ,,J“ bei allen Ge-
schäftsvorfällen zu benutzen, die diese Option anbieten

<!-- PageBreak -->


<table>
<tr>
<th>Kapitel: D</th>
<th>Version: 3.0-FV</th>
<th>Financial Transaction Services (FinTS) Dokument: Security - Sicherheitsverfahren PIN/TAN</th>
</tr>
<tr>
<td>Seite: 112</td>
<td>Stand: 23.02.2018</td>
<td>Kapitel: Data-Dictionary<br>Abschnitt: Sonstige</td>
</tr>
</table>


###### und bei denen dies fachlich verarbeitbar ist.


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
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th>Version:</th>
<th>Kapitel:</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Security - Sicherheitsverfahren PIN/TAN</td>
<td>3.0-FV</td>
<td>D</td>
</tr>
<tr>
<td>Kapitel:</td>
<td>Data-Dictionary</td>
<td>Stand:</td>
<td>Seite:</td>
</tr>
<tr>
<td>Abschnitt:</td>
<td>Sonstige</td>
<td>23.02.2018</td>
<td>113</td>
</tr>
</table>


####### Mehrfach-TAN erlaubt

Angabe, ob beim Zwei-Schritt-Verfahren die Verwendung von Mehrfach-
TANs erlaubt ist.


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


####### Minimale PIN-Länge

Minimale Länge der PIN. Wenn das Kreditinstitut eine feste PIN-Länge er-
wartet, sind minimale und maximale PIN-Länge auf denselben Wert zu set-
zen.

Typ: DE


<table>
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


####### Mobiltelefonnummer

Reale Nummer des Mobiltelefons. Es sind nur Ziffern inklusive führender
Nullen erlaubt und es gilt die nationale Schreibweise für Telefonnummern,
z. B. 0170/1234567 oder (0170) 1234567.


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


####### Mobiltelefonnummer verschleiert

Darstellung der Mobiltelefonnummer in der Form „*****nnnn“, wobei die letz-
ten vier Stellen denen der realen Mobiltelefonnummer entsprechen. Die An-
zahl des Platzhalters ,\*" kann entweder fix sein oder der Anzahl der Zeichen
der realen Mobiltelefonnummer (mit oder ohne Sonderzeichen) entsprechen.
Ein anderes Zeichen als ,,\*" als Platzhalter ist nicht zugelassen.


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


N


####### Name des Zwei-Schritt-Verfahrens

Textliche Bezeichnung des konkreten Zwei-Schritt-Verfahrens, z. B. ,,chip-
TAN" oder ,,mobileTAN". Der Name soll vom Kundenprodukt zur Anzeige
verwendet werden.


![](figures/113.1)


Kundenprodukte sollten diesen Text als Beschreibung des
konkreten Zwei-Schritt-Verfahrens verwenden. Dies gilt für
die Anzeige bei der Eingabe zur TAN-Aufforderung. Bei
Verwaltungsfunktionen soll die ,,Technische Identifikation

<!-- PageBreak -->


<table>
<tr>
<th>Kapitel: D</th>
<th>Version: 3.0-FV</th>
<th>Financial Transaction Services (FinTS) Dokument: Security - Sicherheitsverfahren PIN/TAN</th>
</tr>
<tr>
<td>Seite:<br>114</td>
<td>Stand: 23.02.2018</td>
<td>Kapitel: Data-Dictionary<br>Abschnitt: Sonstige</td>
</tr>
</table>


###### TAN-Verfahren“ verwendet werden.


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


####### Name Karteninhaber #2

Name des Inhabers einer vom Kreditinstitut ausgestellten Karte. Dabei muss
der Karteninhaber nicht notwendigerweise der Kontoinhaber sein. Auch die
Schreibweise des Namens muss nicht notwendigerweise mit dem auf der
Karte aufzudruckenden Namen übereinstimmen.

Der Name des Karteninhabers und das Verfalldatum der Karte können bei
Kundenaufträgen als zusätzliche Identifizierungskriterien herangezogen wer-
den, wenn bspw. die Kartenfolgenummer nicht bekannt ist.


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
<td>2</td>
</tr>
</table>


P


####### Parameter Challenge-Klasse

Auftragsspezifische Daten, die entsprechend der Challenge-Klasse für die
Verarbeitung im Institut benötigt werden.


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
<td>Challenge-Klasse Parameter</td>
<td>DE</td>
<td>an</td>
<td>.999</td>
<td>O</td>
<td>9</td>
<td></td>
</tr>
</table>


Typ:

DEG

Format:

Länge:

Version:

1


####### Parameter HHD-/Secoder-Informationen

Auftragsspezifische Bankparameterdaten für den Geschäftsvorfall „HHD-
/Secoder-Informationen übermitteln“.


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
<td>Reader-ID erfor- derlich</td>
<td>DE</td>
<td>jn</td>
<td>#</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>2</td>
<td>Verfahrensbestä- tigung erforderlich</td>
<td>DE</td>
<td>jn</td>
<td>#</td>
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
<td>Security - Sicherheitsverfahren PIN/TAN</td>
<td>3.0-FV</td>
<td>D</td>
</tr>
<tr>
<td>Kapitel:</td>
<td>Data-Dictionary</td>
<td>Stand:</td>
<td>Seite:</td>
</tr>
<tr>
<td>Abschnitt:</td>
<td>Sonstige</td>
<td>23.02.2018</td>
<td>115</td>
</tr>
</table>


####### Parameter Mobilfunkverbindung ändern

Auftragsspezifische Bankparameterdaten für den Geschäftsvorfall „Mobil-
funkverbindung ändern“.


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
<td>SMS- Abbuchungskonto erforderlich</td>
<td>1</td>
<td>DE</td>
<td>jn</td>
<td>#</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
</table>


Typ:

DEG

Format:

Länge:

Version:

1


####### Parameter Mobilfunkverbindung ändern #2

Auftragsspezifische Bankparameterdaten für den Geschäftsvorfall „Mobil-
funkverbindung ändern“.


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
<td>SMS- Abbuchungskonto erforderlich</td>
<td>1</td>
<td>DE</td>
<td>jn</td>
<td>#</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>2</td>
<td>Zustimmung zur Kontaktaufnahme unterstützt</td>
<td>1</td>
<td>DE</td>
<td>jn</td>
<td>#</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
</table>


Typ:

DEG

Format:

Länge:

Version:

2


####### Parameter Mobilfunkverbindung registrieren

Auftragsspezifische Bankparameterdaten für den Geschäftsvorfall ,,Mobil-
funkverbindung registrieren“.


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
<td>SMS- Abbuchungskonto erforderlich</td>
<td>1</td>
<td>DE</td>
<td>jn</td>
<td>#</td>
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
<td>1</td>
</tr>
</table>


<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: D</td>
<td>Version: 3.0-FV</td>
<td>Financial Transaction Services (FinTS) Dokument: Security - Sicherheitsverfahren PIN/TAN</td>
</tr>
<tr>
<td>Seite: 116</td>
<td>Stand: 23.02.2018</td>
<td>Kapitel: Data-Dictionary<br>Abschnitt: Sonstige</td>
</tr>
</table>


####### Parameter Mobilfunkverbindung registrieren #2

Auftragsspezifische Bankparameterdaten für den Geschäftsvorfall ,,Mobil-
funkverbindung registrieren".


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
<td>SMS- Abbuchungskonto erforderlich</td>
<td>1</td>
<td>DE</td>
<td>jn</td>
<td>#</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>2</td>
<td>Zustimmung zur Kontaktaufnahme unterstützt</td>
<td>1</td>
<td>DE</td>
<td>jn</td>
<td>#</td>
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


####### Parameter TAN-Generator an- bzw. ummelden #1

Auftragsspezifische Bankparameterdaten für den Geschäftsvorfall „TAN-
Generator an- bzw. ummelden“.


<table>
<tr>
<th>Nr .</th>
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
<td>Eingabe TAN- Listennummer J/N</td>
<td>1</td>
<td>DE</td>
<td>jn</td>
<td>1</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>2</td>
<td>Eingabe Kartenfol- genummer J/N</td>
<td>1</td>
<td>DE</td>
<td>jn</td>
<td>1</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>3</td>
<td>Eingabe von ATC und TAN erforder- lich</td>
<td>1</td>
<td>DE</td>
<td>jn</td>
<td>1</td>
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
<td>1</td>
</tr>
</table>


####### Parameter TAN-Generator an- bzw. ummelden #2

Auftragsspezifische Bankparameterdaten für den Geschäftsvorfall ,,TAN-
Generator an- bzw. ummelden“.

<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th>Version:</th>
<th>Kapitel:</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Security - Sicherheitsverfahren PIN/TAN</td>
<td>3.0-FV</td>
<td>D</td>
</tr>
<tr>
<td>Kapitel:</td>
<td>Data-Dictionary</td>
<td>Stand:</td>
<td>Seite:</td>
</tr>
<tr>
<td>Abschnitt:</td>
<td>Sonstige</td>
<td>23.02.2018</td>
<td>117</td>
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
<td>Eingabe TAN- Listennummer J/N</td>
<td>1</td>
<td>DE</td>
<td>jn</td>
<td>1</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>2</td>
<td>Eingabe Karten- folgenummer J/N</td>
<td>1</td>
<td>DE</td>
<td>jn</td>
<td>1</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>3</td>
<td>Eingabe von ATC und TAN erforder- lich</td>
<td>1</td>
<td>DE</td>
<td>jn</td>
<td>1</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>4</td>
<td>Eingabe Kartenart zulässig</td>
<td>1</td>
<td>DE</td>
<td>jn</td>
<td>1</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>5</td>
<td>Zulässige Karten- art</td>
<td>1</td>
<td>DE</td>
<td>num</td>
<td>.2</td>
<td>C</td>
<td>0..99</td>
<td>M: wenn ,,Eingabe Kartenart zulässig = J“ N: sonst</td>
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


####### Parameter TAN-Generator an- bzw. ummelden #3

Auftragsspezifische Bankparameterdaten für den Geschäftsvorfall „TAN-
Generator an- bzw. ummelden“.


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
<td>Eingabe TAN- Listennummer J/N</td>
<td>1</td>
<td>DE</td>
<td>jn</td>
<td>1</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>2</td>
<td>Eingabe Karten- folgenummer J/N</td>
<td>1</td>
<td>DE</td>
<td>jn</td>
<td>1</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>3</td>
<td>Eingabe von ATC und TAN erforder- lich</td>
<td>1</td>
<td>DE</td>
<td>jn</td>
<td>1</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>4</td>
<td>Eingabe Kartenart zulässig</td>
<td>1</td>
<td>DE</td>
<td>jn</td>
<td>1</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>5</td>
<td>Kontoverbindung erforderlich</td>
<td>1</td>
<td>DE</td>
<td>jn</td>
<td>1</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>6</td>
<td>Zulässige Karten- art</td>
<td>1</td>
<td>DE</td>
<td>num</td>
<td>..2</td>
<td>C</td>
<td>0..99</td>
<td>M: wenn ,,Eingabe Kartenart zulässig = J“ N: sonst</td>
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


####### Parameter TAN-Generator Synchronisierung

Auftragsspezifische Bankparameterdaten für den Geschäftsvorfall „TAN-
Generator Synchronisierung".

<!-- PageBreak -->


<table>
<tr>
<th>Kapitel: D</th>
<th>Version: 3.0-FV</th>
<th>Financial Transaction Services (FinTS) Dokument: Security - Sicherheitsverfahren PIN/TAN</th>
</tr>
<tr>
<td>Seite: 118</td>
<td>Stand: 23.02.2018</td>
<td>Kapitel: Data-Dictionary<br>Abschnitt: Sonstige</td>
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
<td>Eingabe Karten- nummer J/N</td>
<td>1</td>
<td>DE</td>
<td>jn</td>
<td>1</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>2</td>
<td>Eingabe Karten- folgenummer J/N</td>
<td>1</td>
<td>DE</td>
<td>jn</td>
<td>1</td>
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
<td>1</td>
</tr>
</table>


####### Parameter Zwei-Schritt-TAN-Einreichung, Elementversion #1

Auftragsspezifische Bankparameterdaten für den Geschäftsvorfall „Zwei-
Schritt-TAN-Einreichung".


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
<td>Einschritt- Verfahren erlaubt</td>
<td>1</td>
<td>DE</td>
<td>jn</td>
<td>#</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>2</td>
<td>Mehr als ein TAN- pflichtiger Auftrag pro Nachricht er- laubt</td>
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
<td>Auftrags- Hashwertverfah- ren</td>
<td>1</td>
<td>DE</td>
<td>code</td>
<td>1</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>4</td>
<td>Sicherheitsprofil Banken-Signatur bei HITAN</td>
<td>1</td>
<td>DE</td>
<td>code</td>
<td>1</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>5</td>
<td>Verfahrenspara- meter Zwei- Schritt-Verfahren</td>
<td>1</td>
<td>DEG</td>
<td></td>
<td></td>
<td>M</td>
<td>1..98</td>
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
<td>1</td>
</tr>
</table>


####### Parameter Zwei-Schritt-TAN-Einreichung, Elementversion #2

Auftragsspezifische Bankparameterdaten für den Geschäftsvorfall ,Zwei-
Schritt-TAN-Einreichung“.

<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th>Version:</th>
<th rowspan="2">Kapitel: D</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Security - Sicherheitsverfahren PIN/TAN</td>
<td>3.0-FV</td>
</tr>
<tr>
<td>Kapitel:</td>
<td>Data-Dictionary</td>
<td>Stand:</td>
<td>Seite:</td>
</tr>
<tr>
<td>Abschnitt:</td>
<td>Sonstige</td>
<td>23.02.2018</td>
<td>119</td>
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
<td>Einschritt- Verfahren erlaubt</td>
<td>1</td>
<td>DE</td>
<td>jn</td>
<td>#</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>2</td>
<td>Mehr als ein TAN- pflichtiger Auftrag pro Nachricht er- laubt</td>
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
<td>Auftrags- Hashwertverfah- ren</td>
<td>1</td>
<td>DE</td>
<td>code</td>
<td>1</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>4</td>
<td>Verfahrenspara- meter Zwei- Schritt-Verfahren</td>
<td>2</td>
<td>DEG</td>
<td></td>
<td></td>
<td>M</td>
<td>1..98</td>
<td></td>
</tr>
</table>


Typ:

DEG

Format:

Länge:

Version:

2


####### Parameter Zwei-Schritt-TAN-Einreichung, Elementversion #3

Auftragsspezifische Bankparameterdaten für den Geschäftsvorfall „Zwei-
Schritt-TAN-Einreichung".


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
<td>Einschritt- Verfahren erlaubt</td>
<td>1</td>
<td>DE</td>
<td>jn</td>
<td>#</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>2</td>
<td>Mehr als ein TAN- pflichtiger Auftrag pro Nachricht er- laubt</td>
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
<td>Auftrags- Hashwertverfah- ren</td>
<td>1</td>
<td>DE</td>
<td>code</td>
<td>1</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>4</td>
<td>Verfahrenspara- meter Zwei- Schritt-Verfahren</td>
<td>3</td>
<td>DEG</td>
<td></td>
<td></td>
<td>M</td>
<td>1..98</td>
<td></td>
</tr>
</table>


Typ:

DEG

Format:

Länge:

Version:

3


####### Parameter Zwei-Schritt-TAN-Einreichung, Elementversion #4

Auftragsspezifische Bankparameterdaten für den Geschäftsvorfall „Zwei-
Schritt-TAN-Einreichung".

<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: D</td>
<td>Version: 3.0-FV</td>
<td>Financial Transaction Services (FinTS) Dokument: Security - Sicherheitsverfahren PIN/TAN</td>
</tr>
<tr>
<td>Seite: 120</td>
<td>Stand: 23.02.2018</td>
<td>Kapitel: Data-Dictionary<br>Abschnitt: Sonstige</td>
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
<td>Einschritt- Verfahren erlaubt</td>
<td>1</td>
<td>DE</td>
<td>jn</td>
<td>#</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>2</td>
<td>Mehr als ein TAN- pflichtiger Auftrag pro Nachricht er- laubt</td>
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
<td>Auftrags- Hashwertverfah- ren</td>
<td>1</td>
<td>DE</td>
<td>code</td>
<td>1</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>4</td>
<td>Verfahrenspara- meter Zwei- Schritt-Verfahren</td>
<td>4</td>
<td>DEG</td>
<td></td>
<td></td>
<td>M</td>
<td>1..98</td>
<td></td>
</tr>
</table>


Typ:

DEG

Format:

Länge:

Version:

4


####### Parameter Zwei-Schritt-TAN-Einreichung, Elementversion #5

Auftragsspezifische Bankparameterdaten für den Geschäftsvorfall „Zwei-
Schritt-TAN-Einreichung".


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
<td>Einschritt- Verfahren erlaubt</td>
<td>1</td>
<td>DE</td>
<td>jn</td>
<td>#</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>2</td>
<td>Mehr als ein TAN- pflichtiger Auftrag pro Nachricht er- laubt</td>
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
<td>Auftrags- Hashwertverfah- ren</td>
<td>1</td>
<td>DE</td>
<td>code</td>
<td>1</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>4</td>
<td>Verfahrenspara- meter Zwei- Schritt-Verfahren</td>
<td>5</td>
<td>DEG</td>
<td></td>
<td></td>
<td>M</td>
<td>1..98</td>
<td></td>
</tr>
</table>


Typ:

DEG

Format:

Länge:

Version:

5


####### Parameter Zwei-Schritt-TAN-Einreichung, Elementversion #6

Auftragsspezifische Bankparameterdaten für den Geschäftsvorfall ,Zwei-
Schritt-TAN-Einreichung“.

<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th>Version:</th>
<th>Kapitel:</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Security - Sicherheitsverfahren PIN/TAN</td>
<td>3.0-FV</td>
<td>D</td>
</tr>
<tr>
<td>Kapitel:</td>
<td>Data-Dictionary</td>
<td>Stand:</td>
<td>Seite:</td>
</tr>
<tr>
<td>Abschnitt:</td>
<td>Sonstige</td>
<td>23.02.2018</td>
<td>121</td>
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
<td>Einschritt- Verfahren erlaubt</td>
<td>1</td>
<td>DE</td>
<td>jn</td>
<td>#</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>2</td>
<td>Mehr als ein TAN- pflichtiger Auftrag pro Nachricht er- laubt</td>
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
<td>Auftrags- Hashwertverfah- ren</td>
<td>1</td>
<td>DE</td>
<td>code</td>
<td>1</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>4</td>
<td>Verfahrenspara- meter Zwei- Schritt-Verfahren</td>
<td>6</td>
<td>DEG</td>
<td></td>
<td></td>
<td>M</td>
<td>1..98</td>
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
<td>6</td>
</tr>
</table>


PIN

(Private Identifikationsnummer) Authentisierungsmerkmal des Kunden beim
PIN/TAN-Verfahren. Das Format einer PIN ist kreditinstitutsindividuell. Die
minimale und maximale Länge der PIN kann das Kreditinstitut im Segment
HIPINS angeben.


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
<td>..99</td>
</tr>
<tr>
<td>Version:</td>
<td>1</td>
</tr>
</table>


R


###### Reader-ID

Eindeutige Identifikationsnummer eines chipTAN-Lesers bzw. eines Seco-
ders.


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


###### Reader-ID erforderlich

Über diesen Parameter wird festgelegt, ob die Übertragung der Reader-ID
zwingend erforderlich ist oder optional erfolgen kann. So kann ein Kreditinsti-
tut die Übertragung der Reader-ID verlangen, wenn keine zentralen Bestän-
de zur Verfügung stehen oder die Reader-ID für eine zentrale Verwaltung er-
fasst werden soll.

<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: D</td>
<td>Version: 3.0-FV</td>
<td>Financial Transaction Services (FinTS) Dokument: Security - Sicherheitsverfahren PIN/TAN</td>
</tr>
<tr>
<td>Seite:<br>122</td>
<td>Stand: 23.02.2018</td>
<td>Kapitel: Data-Dictionary<br>Abschnitt: Sonstige</td>
</tr>
</table>


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


S


###### Segmentkennung

Segmentspezifische Kennung, die jedem Segment bzw. Auftrag zugeordnet
ist (z.B. "HKCCS" für "SEPA-Einzelüberweisung"). Die Angabe hat in Groß-
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


###### Segmentkopf

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
<td>&gt;=1<br>O: Verwendung in Kre- ditinstitutsnachricht<br>N: Verwendung in Kun- dennachricht</td>
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


###### Segmentnummer

Information zur eindeutigen Identifizierung eines Segments innerhalb einer
Nachricht. Die Segmente einer Nachricht werden in Einerschritten streng
monoton aufsteigend nummeriert. Die Nummerierung beginnt mit 1 im ersten
Segment der Nachricht (Nachrichtenkopf).

<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th>Version:</th>
<th rowspan="2">Kapitel: D</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Security - Sicherheitsverfahren PIN/TAN</td>
<td>3.0-FV</td>
</tr>
<tr>
<td>Kapitel:</td>
<td>Data-Dictionary</td>
<td>Stand:</td>
<td>Seite:</td>
</tr>
<tr>
<td>Abschnitt:</td>
<td>Sonstige</td>
<td>23.02.2018</td>
<td>123</td>
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


###### Segmentversion

Versionsnummer zur Dokumentation von Änderungen eines Segment-
formats.

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

Die für die jeweilige FinTS-Version gültige Segmentversion ist bei der jewei-
ligen Segmentbeschreibung vermerkt.

Falls der Kunde ein Segment mit einer veralteten Versionsnummer einreicht,
sollte ihm in einer entsprechenden Warnung rück gemeldet werden, dass
sein Kundenprodukt aktualisiert werden sollte.

Typ: DE


<table>
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


###### Sicherheitsfunktion, kodiert #2

Kodierte Information über die Sicherheitsfunktion, die auf die Nachricht angewendet
wird. Dieses Element wird gemeinsam in den Sicherheitsverfahren HBCI, PIN/TAN
und den AZS-Verfahren benutzt.

FinTS V3.0 - Sicherheitsverfahren HBCI:

Die Sicherheitsfunktion hat ab FinTS 3.0 lediglich informatorischen Wert, da die ei-
gentliche Steuerung über die Sicherheitsprofile und -klassen erfolgt.

FinTS V3.0 - Sicherheitsverfahren PIN/TAN:

Codierung der verwendeten Sicherheits- und Verschlüsselungsfunktionen

FinTS V3.0 - Alternative ZKA Sicherheitsverfahren:

Dient der Kennzeichnung des jeweiligen Verfahrens in Verbindung mit dem Ge-
schäftsvorfall HKAZS


####### Codierung:


<table>
<tr>
<td>Code</td>
<td>Segment</td>
<td>Bedeutung</td>
</tr>
<tr>
<td>Kapitel: D</td>
<td>Version: 3.0-FV</td>
<td>Financial Transaction Services (FinTS) Dokument: Security - Sicherheitsverfahren PIN/TAN</td>
</tr>
<tr>
<td>Seite: 124</td>
<td>Stand: 23.02.2018</td>
<td>Kapitel: Data-Dictionary<br>Abschnitt: Sonstige</td>
</tr>
</table>


<table>
<tr>
<td>1</td>
<td>Sicherheitsverfahren HBCI: - Signaturkopf</td>
<td>Non-Repudiation of Origin, für RAH (NRO)</td>
</tr>
<tr>
<td>2</td>
<td>Sicherheitsverfahren HBCI: - Signaturkopf</td>
<td>Message Origin Authen- tication, für RAH und DDV (AUT)</td>
</tr>
<tr>
<td>4</td>
<td>Sicherheitsverfahren HBCI: - Verschlüsselungskopf</td>
<td>Encryption, Verschlüsse- lung und evtl. Komprimie- rung (ENC)</td>
</tr>
<tr>
<td>811</td>
<td>Alternative ZKA Sicherheitsverfahren: - Signaturkopf bei HKAZS,<br>- HIAZSS Verfahrensparameter</td>
<td>Fortgeschrittene Elektro- nische Signatur (,,AUT- Signatur") mit Secoder ohne Institutssignatur</td>
</tr>
<tr>
<td>900</td>
<td>Sicherheitsverfahren PIN/TAN:<br>- Signaturkopf bei HKTAN,<br>- HITANS Verfahrensparameter Zwei-Schritt-Verfahren</td>
<td>1. konkretes Zwei-Schritt- TAN-Verfahren</td>
</tr>
<tr>
<td>901</td>
<td>Sicherheitsverfahren PIN/TAN:<br>- Signaturkopf bei HKTAN,<br>- HITANS Verfahrensparameter Zwei-Schritt-Verfahren</td>
<td>2. konkretes Zwei-Schritt- Verfahren</td>
</tr>
<tr>
<td>...</td>
<td></td>
<td></td>
</tr>
<tr>
<td>996</td>
<td>Sicherheitsverfahren PIN/TAN:<br>- Signaturkopf bei HKTAN,<br>- HITANS Verfahrensparameter Zwei-Schritt-Verfahren</td>
<td>97. konkretes Zwei- Schritt-Verfahren</td>
</tr>
<tr>
<td>997</td>
<td>Sicherheitsverfahren PIN/TAN:<br>- Signaturkopf bei HKTAN,<br>- HITANS Verfahrensparameter Zwei-Schritt-Verfahren</td>
<td>98. konkretes Zwei- Schritt-Verfahren</td>
</tr>
<tr>
<td>998</td>
<td>Sicherheitsverfahren PIN/TAN:<br>- Verschlüsselungskopf</td>
<td>Daten im Klartext (nur in Verbindung mit TLS er- laubt)</td>
</tr>
<tr>
<td>999</td>
<td>Signaturkopf</td>
<td>Klassisches Ein-Schritt- Verfahren</td>
</tr>
</table>


Die Werte 900 bis 997 und 999 werden auch im Rahmen der Rückmeldung
mit Code 3920 ,,Zugelassene Ein- und Zwei-Schritt-Verfahren für Benutzer“
als Rückmeldungsparameter P1 bis P10 verwendet.


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


####### Sicherheitsprofil Banken-Signatur bei HITAN

Information, ob das Kreditinstitut beim Zwei-Schritt-Verfahren die Absiche-
rung der Kreditinstitutsantwort HITAN mittels Banken-Signatur zulässt und

<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th>Version:</th>
<th>Kapitel:</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Security - Sicherheitsverfahren PIN/TAN</td>
<td>3.0-FV</td>
<td>D</td>
</tr>
<tr>
<td>Kapitel:</td>
<td>Data-Dictionary</td>
<td>Stand:</td>
<td>Seite:</td>
</tr>
<tr>
<td>Abschnitt:</td>
<td>Sonstige</td>
<td>23.02.2018</td>
<td>125</td>
</tr>
</table>


wenn ja, welches Sicherheitsprofil zugelassen ist. Dieser Parameter wird aus
Kompatibilitätsgründen ausschließlich bei HITAN in Segmentversion=1 ver-
wendet und entfällt ab Segmentversion=2 ersatzlos, da die Unterstützung
der Banken-Signatur durch ein Institut außerhalb des FinTS-Protokolls gere-
gelt wird.

Codierung:

0: Banken-Signatur von HITAN nicht erlaubt

1: RDH-1 (wird in FinTS V3.0 nicht verwendet)

2: RDH-2 (in FinTS V3.0)


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


###### SMS-Abbuchungskonto

Zahlungsverkehrskontoverbindung, die für die Abbuchung von SMS-Kosten
herangezogen werden soll.


<table>
<tr>
<td>Typ:</td>
<td>DEG</td>
</tr>
<tr>
<td>Format:</td>
<td>kti</td>
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


###### SMS-Abbuchungskonto erforderlich

Parameter, der angibt, ob eine Zahlungsverkehrskontoverbindung für die
Abbuchung von SMS-Kosten angegeben werden muss. Die Belastung von
SMS-Kosten durch das Institut wird unabhängig von dem Vorhandensein ei-
ner Kontoverbindung z. B. kundenindividuell geregelt.

Das Element wird in Basisfunktionen verwendet, die nur eine J/N Entschei-
dung benötigen.


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
<td>Version</td>
<td>1</td>
</tr>
</table>


###### SMS-Abbuchungskonto erforderlich

Parameter, der angibt, ob eine Zahlungsverkehrskontoverbindung für die
Abbuchung von SMS-Kosten angegeben werden kann oder muss. Die Be-
lastung von SMS-Kosten durch das Institut wird unabhängig von dem Vor-
handensein einer Kontoverbindung z. B. kundenindividuell geregelt.

Das Element in der Version #2 ermöglicht eine detailliertere Steuerung der
Belegung. Es wird z. B. in HKTAN ab Segmentversion #5 eingesetzt.

Codierung:

0: SMS-Abbuchungskonto darf nicht angegeben werden

1: SMS-Abbuchungskonto kann angegeben werden

<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: D</td>
<td>Version: 3.0-FV</td>
<td>Financial Transaction Services (FinTS) Dokument: Security - Sicherheitsverfahren PIN/TAN</td>
</tr>
<tr>
<td>Seite:<br>126</td>
<td>Stand:<br>23.02.2018</td>
<td>Kapitel: Data-Dictionary<br>Abschnitt:<br>Sonstige</td>
</tr>
</table>


###### 2: SMS-Abbuchungskonto muss angegeben werden


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


####### Status

Gibt an, in welchem Status sich ein TAN-Medium befindet.

Codierung:

1: Aktiv

2: Verfügbar

3: Aktiv Folgekarte

4: Verfügbar Folgekarte


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


T


####### TAN

(Transaktionsnummer) One-Time-Passwort zur Freigabe von Transaktionen
beim PIN/TAN-Verfahren. Das Format einer TAN ist kreditinstitutsindividuell.
Die maximale Länge der TAN kann das Kreditinstitut im Segment HIPINS
angeben. Das DE TAN darf beim Zwei-Schritt-Verfahren bei TAN-Prozess=2
ausschließlich in Verbindung mit dem Geschäftsvorfall HKTAN belegt wer-
den. Ansonsten wird der Inhalt ignoriert und die TAN vom Institut entwertet.


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
<td>..99</td>
</tr>
<tr>
<td>Version:</td>
<td>1</td>
</tr>
</table>


###### TAN erforderlich

Es wird angegeben, ob beim Einreichen des Geschäftsvorfalles je vorhande-
ner Signatur eine TAN angegeben werden muss oder nicht.


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


###### TAN-Einsatzoption

Es werden die Möglichkeiten festgelegt, die ein Kunde hat, wenn er für
PIN/TAN parallel mehrere TAN-Medien zur Verfügung hat.

Codierung:

<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th>Version:</th>
<th>Kapitel:</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Security - Sicherheitsverfahren PIN/TAN</td>
<td>3.0-FV</td>
<td>D</td>
</tr>
<tr>
<td>Kapitel:</td>
<td>Data-Dictionary</td>
<td>Stand:</td>
<td>Seite:</td>
</tr>
<tr>
<td>Abschnitt:</td>
<td>Sonstige</td>
<td>23.02.2018</td>
<td>127</td>
</tr>
</table>


0:
Kunde kann alle ,,aktiven" Medien parallel nutzen

1:
Kunde kann genau ein Medium (z. B. ein Mobiltelefon oder einen
TAN-Generator) zu einer Zeit nutzen

2:
Kunde kann ein Mobiltelefon und einen TAN-Generator parallel nutzen


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


###### TAN-Information, Segmentversion #1

Informationen zu einer TAN der TAN-Liste.


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
<td>TAN-Verbrauchs- kennzeichen</td>
<td>1</td>
<td>DE</td>
<td>code</td>
<td>..2</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>2</td>
<td>TAN-Verbrauchs- erläuterung</td>
<td>1</td>
<td>DE</td>
<td>an</td>
<td>..99</td>
<td>C</td>
<td>1</td>
<td>O: TAN- Verbrauchskenn- zeichen = 99 N: sonst</td>
</tr>
<tr>
<td>3</td>
<td>TAN</td>
<td>1</td>
<td>DE</td>
<td>an</td>
<td>.99</td>
<td>C</td>
<td>1</td>
<td>O: TAN wurde verbraucht N: sonst</td>
</tr>
<tr>
<td>4</td>
<td>TAN- Verbrauchsdatum</td>
<td>1</td>
<td>DE</td>
<td>dat</td>
<td>#</td>
<td>C</td>
<td>1</td>
<td>O: TAN wurde verbraucht N: sonst</td>
</tr>
<tr>
<td>5</td>
<td>TAN- Verbrauchsuhrzeit</td>
<td>1</td>
<td>DE</td>
<td>tim</td>
<td>#</td>
<td>C</td>
<td>1</td>
<td>O: TAN wurde verbraucht und Verbrauchsdatum angegeben N: sonst</td>
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


###### TAN-Information, Segmentversion #2 Informationen zu einer TAN.

<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: D</td>
<td>Version: 3.0-FV</td>
<td>Financial Transaction Services (FinTS) Dokument: Security - Sicherheitsverfahren PIN/TAN</td>
</tr>
<tr>
<td>Seite: 128</td>
<td>Stand: 23.02.2018</td>
<td>Kapitel: Data-Dictionary<br>Abschnitt:<br>Sonstige</td>
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
<td>TAN-Verbrauchs- kennzeichen</td>
<td>1</td>
<td>DE</td>
<td>code</td>
<td>..2</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>2</td>
<td>TAN-Verbrauchs- erläuterung</td>
<td>1</td>
<td>DE</td>
<td>an</td>
<td>..99</td>
<td>C</td>
<td>1</td>
<td>O: TAN- Verbrauchskenn- zeichen = 99 N: sonst</td>
</tr>
<tr>
<td>3</td>
<td>TAN</td>
<td>1</td>
<td>DE</td>
<td>an</td>
<td>.99</td>
<td>O</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>4</td>
<td>TAN- Verbrauchsdatum</td>
<td>1</td>
<td>DE</td>
<td>dat</td>
<td>#</td>
<td>O</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>5</td>
<td>TAN- Verbrauchsuhrzeit</td>
<td>1</td>
<td>DE</td>
<td>tim</td>
<td>#</td>
<td>C</td>
<td>1</td>
<td>O: Verbrauchs- datum angegeben N: sonst</td>
</tr>
<tr>
<td>6</td>
<td>Entgelte- Abbuchungskonto</td>
<td>1</td>
<td>DEG</td>
<td>kti</td>
<td>#</td>
<td>O</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>7</td>
<td>Transaktionskonto</td>
<td>1</td>
<td>DEG</td>
<td>kti</td>
<td>#</td>
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


###### TAN-Medium-Art, Elementversion #1

dient der Klassifizierung der gesamten dem Kunden zugeordneten TAN-
Medien. Bei Geschäftsvorfällen zum Management des TAN-Generators kann
aus diesen nach folgender Codierung selektiert werden.

Codierung:

0: Alle

2: Aktiv

3: Verfügbar


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


###### TAN-Medium-Art, Elementversion #2

dient der Klassifizierung der gesamten dem Kunden zugeordneten TAN-
Medien. Bei Geschäftsvorfällen zum Management des TAN-Generators kann
aus diesen nach folgender Codierung selektiert werden.

Codierung:

0: Alle

1: Aktiv

2: Verfügbar

Typ: DE

<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th rowspan="2">Version: 3.0-FV</th>
<th rowspan="2">Kapitel: D</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Security - Sicherheitsverfahren PIN/TAN</td>
</tr>
<tr>
<td>Kapitel:</td>
<td>Data-Dictionary</td>
<td>Stand:</td>
<td>Seite:</td>
</tr>
<tr>
<td>Abschnitt:</td>
<td>Sonstige</td>
<td>23.02.2018</td>
<td>129</td>
</tr>
</table>


<table>
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


###### TAN-Medium-Klasse, Elementversion #1

dient der Klassifizierung der möglichen TAN-Medien. Bei Geschäftsvorfällen
zum Management der TAN-Medien kann aus diesen nach folgender Codie-
rung selektiert werden.

Codierung:

L: Liste

G: TAN-Generator

M: Mobiltelefon mit mobile TAN


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


###### TAN-Medium-Klasse, Elementversion #2

dient der Klassifizierung der möglichen TAN-Medien. Bei Geschäftsvorfällen
zum Management der TAN-Medien kann aus diesen nach folgender Codie-
rung selektiert werden.

Codierung:

L: Liste

G: TAN-Generator

M: Mobiltelefon mit mobile TAN

S: Secoder


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


###### TAN-Medium-Klasse, Elementversion #3

dient der Klassifizierung der möglichen TAN-Medien. Bei Geschäftsvorfällen
zum Management der TAN-Medien kann aus diesen nach folgender Codie-
rung selektiert werden.

Codierung:

A: Alle Medien

L: Liste

G: TAN-Generator

M: Mobiltelefon mit mobile TAN

S: Secoder

Typ: DE

<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: D</td>
<td>Version: 3.0-FV</td>
<td>Financial Transaction Services (FinTS) Dokument: Security - Sicherheitsverfahren PIN/TAN</td>
</tr>
<tr>
<td>Seite: 130</td>
<td>Stand: 23.02.2018</td>
<td>Kapitel: Data-Dictionary<br>Abschnitt: Sonstige</td>
</tr>
</table>


<table>
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
<td>3</td>
</tr>
</table>


###### TAN-Medium-Klasse, Elementversion #4

dient der Klassifizierung der möglichen TAN-Medien. Bei Geschäftsvorfällen
zum Management der TAN-Medien kann aus diesen nach folgender Codie-
rung selektiert werden.

Codierung:

A: Alle Medien

L: Liste

G: TAN-Generator

M: Mobiltelefon mit mobile TAN

S: Secoder

B: Bilateral vereinbart

Typ: DE


<table>
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
<td>4</td>
</tr>
</table>


###### TAN-Medium-Liste, Elementversion #1

Informationen zu Art und Parametrisierung von TAN-Medien. Als TAN-Medien
werden sowohl TAN-Listen als auch ZKA-TAN-Generatoren / Karten be-
zeichnet.


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
<td>TAN-Generator / Liste</td>
<td>1</td>
<td>DE</td>
<td>an</td>
<td>1</td>
<td>M</td>
<td>1</td>
<td>G, L</td>
</tr>
<tr>
<td>2</td>
<td>Status</td>
<td>1</td>
<td>DE</td>
<td>code</td>
<td>1</td>
<td>M</td>
<td>1</td>
<td>1, 2, 3, 4</td>
</tr>
<tr>
<td>3</td>
<td>Kartennummer</td>
<td>1</td>
<td>DE</td>
<td>Id</td>
<td>#</td>
<td>C</td>
<td>1</td>
<td>M: DE „TAN- Generator / Lis- te“=“G“ N: sonst</td>
</tr>
<tr>
<td>4</td>
<td>Kartenfolgenum- mer</td>
<td>1</td>
<td>DE</td>
<td>Id</td>
<td>#</td>
<td>C</td>
<td>1</td>
<td>M: DE „TAN- Generator / Lis- te“=“G“ N: sonst</td>
</tr>
<tr>
<td>5</td>
<td>TAN- Listennummer</td>
<td>1</td>
<td>DE</td>
<td>an</td>
<td>..20</td>
<td>C</td>
<td>1</td>
<td>M: DE „TAN- Generator / Liste"="L" N: sonst</td>
</tr>
<tr>
<td>6</td>
<td>Anzahl freie TANs</td>
<td>1</td>
<td>DE</td>
<td>num</td>
<td>.3</td>
<td>O</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>7</td>
<td>Letzte Benutzung</td>
<td>1</td>
<td>DE</td>
<td>dat</td>
<td>8</td>
<td>O</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>8</td>
<td>Freigeschaltet am</td>
<td>1</td>
<td>DE</td>
<td>dat</td>
<td>8</td>
<td>O</td>
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
<td>Security - Sicherheitsverfahren PIN/TAN</td>
<td>3.0-FV</td>
<td>D</td>
</tr>
<tr>
<td>Kapitel:</td>
<td>Data-Dictionary</td>
<td>Stand:</td>
<td>Seite:</td>
</tr>
<tr>
<td>Abschnitt:</td>
<td>Sonstige</td>
<td>23.02.2018</td>
<td>131</td>
</tr>
</table>


Typ:
DEG

Format:

Länge:

Version:
1


###### TAN-Medium-Liste, Elementversion #2

Informationen zu Art und Parametrisierung von TAN-Medien. Als TAN-Medien
werden sowohl TAN-Listen als auch ZKA-TAN-Generatoren / Karten oder
Mobiltelefone bezeichnet.


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
<td>TAN-Medium- Klasse</td>
<td>1</td>
<td>DE</td>
<td>code</td>
<td>1</td>
<td>M</td>
<td>1</td>
<td>G, L, M</td>
</tr>
<tr>
<td>2</td>
<td>Status</td>
<td>1</td>
<td>DE</td>
<td>code</td>
<td>1</td>
<td>M</td>
<td>1</td>
<td>1, 2, 3, 4</td>
</tr>
<tr>
<td>3</td>
<td>Kartennummer</td>
<td>1</td>
<td>DE</td>
<td>id</td>
<td>#</td>
<td>C</td>
<td>1</td>
<td>M: DE ,,TAN-Medium- Klasse“=“G“ N: sonst</td>
</tr>
<tr>
<td>4</td>
<td>Kartenfolgenum- mer</td>
<td>1</td>
<td>DE</td>
<td>id</td>
<td>#</td>
<td>C</td>
<td>1</td>
<td>M: DE ,,TAN-Medium- Klasse“=“G“ N: sonst</td>
</tr>
<tr>
<td>5</td>
<td>Kartenart</td>
<td>1</td>
<td>DE</td>
<td>num</td>
<td>..2</td>
<td>C</td>
<td>1</td>
<td>O: DE ,,TAN- Generator/-Liste"="G" und DE ,,Eingabe Kartenart zulässig“ (BPD) = „J“ N: sonst</td>
</tr>
<tr>
<td>6</td>
<td>Kontoverbindung Auftraggeber</td>
<td>3</td>
<td>DEG</td>
<td>ktv</td>
<td>#</td>
<td>C</td>
<td>1</td>
<td>O: DE „TAN- Generator/-Liste"="G" N: sonst</td>
</tr>
<tr>
<td>7</td>
<td>gültig ab</td>
<td>1</td>
<td>DE</td>
<td>dat</td>
<td>#</td>
<td>C</td>
<td>1</td>
<td>O: DE ,,TAN- Generator/-Liste"="G" N: sonst</td>
</tr>
<tr>
<td>8</td>
<td>gültig bis</td>
<td>1</td>
<td>DE</td>
<td>dat</td>
<td>#</td>
<td>C</td>
<td>1</td>
<td>O: DE „TAN- Generator/-Liste"="G" N: sonst</td>
</tr>
<tr>
<td>9</td>
<td>TAN- Listennummer</td>
<td>1</td>
<td>DE</td>
<td>an</td>
<td>..20</td>
<td>C</td>
<td>1</td>
<td>M: DE ,,TAN-Medium- Klasse“=“L“ N: sonst</td>
</tr>
<tr>
<td>10</td>
<td>Bezeichnung des TAN-Mediums</td>
<td>1</td>
<td>DE</td>
<td>an</td>
<td>..32</td>
<td>C</td>
<td>1</td>
<td>M: DE ,,TAN-Medium- Klasse“=“M“ O: sonst</td>
</tr>
<tr>
<td>11</td>
<td>SMS- Abbuchungskonto</td>
<td>1</td>
<td>DEG</td>
<td>kti</td>
<td>#</td>
<td>C</td>
<td>1</td>
<td>O: DE ,,TAN-Medium- Klasse“=“M“ N: sonst</td>
</tr>
<tr>
<td>12</td>
<td>Anzahl freie TANs</td>
<td>1</td>
<td>DE</td>
<td>num</td>
<td>.3</td>
<td>O</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>13</td>
<td>Letzte Benutzung</td>
<td>1</td>
<td>DE</td>
<td>dat</td>
<td>8</td>
<td>O</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>14</td>
<td>Freigeschaltet am</td>
<td>1</td>
<td>DE</td>
<td>dat</td>
<td>8</td>
<td>O</td>
<td>1</td>
<td></td>
</tr>
</table>


<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: D</td>
<td>Version: 3.0-FV</td>
<td>Financial Transaction Services (FinTS) Dokument: Security - Sicherheitsverfahren PIN/TAN</td>
</tr>
<tr>
<td>Seite: 132</td>
<td>Stand: 23.02.2018</td>
<td>Kapitel: Data-Dictionary<br>Abschnitt: Sonstige</td>
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


###### TAN-Medium-Liste, Elementversion #3

Informationen zu Art und Parametrisierung von TAN-Medien. Als TAN-Medien
werden sowohl TAN-Listen als auch ZKA-TAN-Generatoren / Karten oder
Mobiltelefone bezeichnet.


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
<td>TAN-Medium- Klasse</td>
<td>2</td>
<td>DE</td>
<td>code</td>
<td>1</td>
<td>M</td>
<td>1</td>
<td>G, L, M, S</td>
</tr>
<tr>
<td>2</td>
<td>Status</td>
<td>1</td>
<td>DE</td>
<td>code</td>
<td>1</td>
<td>M</td>
<td>1</td>
<td>1, 2, 3, 4</td>
</tr>
<tr>
<td>3</td>
<td>Kartennummer</td>
<td>1</td>
<td>DE</td>
<td>Id</td>
<td>#</td>
<td>C</td>
<td>1</td>
<td>M: DE ,,TAN-Medium- Klasse“=“G“ N: sonst</td>
</tr>
<tr>
<td>4</td>
<td>Kartenfolgenum- mer</td>
<td>1</td>
<td>DE</td>
<td>Id</td>
<td>#</td>
<td>C</td>
<td>1</td>
<td>M: DE ,,TAN-Medium- Klasse"="G" N: sonst</td>
</tr>
<tr>
<td>5</td>
<td>Kartenart</td>
<td>1</td>
<td>DE</td>
<td>num</td>
<td>.2</td>
<td>C</td>
<td>1</td>
<td>O: DE „TAN- Generator/-Liste"="G" und DE ,,Eingabe Kartenart zulässig“ (BPD) = „J“ N: sonst</td>
</tr>
<tr>
<td>6</td>
<td>Kontoverbindung Auftraggeber</td>
<td>3</td>
<td>DEG</td>
<td>ktv</td>
<td>#</td>
<td>C</td>
<td>1</td>
<td>O: DE „TAN- Generator/-Liste"="G" N: sonst</td>
</tr>
<tr>
<td>7</td>
<td>gültig ab</td>
<td>1</td>
<td>DE</td>
<td>dat</td>
<td>#</td>
<td>C</td>
<td>1</td>
<td>O: DE „TAN- Generator/-Liste"="G" N: sonst</td>
</tr>
<tr>
<td>8</td>
<td>gültig bis</td>
<td>1</td>
<td>DE</td>
<td>dat</td>
<td>#</td>
<td>C</td>
<td>1</td>
<td>O: DE ,,TAN- Generator/-Liste"="G" N: sonst</td>
</tr>
<tr>
<td>9</td>
<td>TAN- Listennummer</td>
<td>1</td>
<td>DE</td>
<td>an</td>
<td>..20</td>
<td>C</td>
<td>1</td>
<td>M: DE ,,TAN-Medium- Klasse“=“L“ N: sonst</td>
</tr>
<tr>
<td>10</td>
<td>Bezeichnung des TAN-Mediums</td>
<td>1</td>
<td>DE</td>
<td>an</td>
<td>..32</td>
<td>C</td>
<td>1</td>
<td>M: DE ,,TAN-Medium- Klasse“=“M“ O: sonst</td>
</tr>
<tr>
<td>11</td>
<td>Mobiltelefonnum- mer verschleiert</td>
<td>1</td>
<td>DE</td>
<td>an</td>
<td>..35</td>
<td>C</td>
<td>1</td>
<td>M: DE ,,TAN-Medium- Klasse“=“M“ N: sonst</td>
</tr>
<tr>
<td>12</td>
<td>SMS- Abbuchungskonto</td>
<td>1</td>
<td>DEG</td>
<td>kti</td>
<td>#</td>
<td>C</td>
<td>1</td>
<td>O: DE ,,TAN-Medium- Klasse“=“M“ N: sonst</td>
</tr>
<tr>
<td>13</td>
<td>Anzahl freie TANs</td>
<td>1</td>
<td>DE</td>
<td>num</td>
<td>..3</td>
<td>O</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>14</td>
<td>Letzte Benutzung</td>
<td>1</td>
<td>DE</td>
<td>dat</td>
<td>8</td>
<td>O</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>15</td>
<td>Freigeschaltet am</td>
<td>1</td>
<td>DE</td>
<td>dat</td>
<td>8</td>
<td>O</td>
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
<td>Security - Sicherheitsverfahren PIN/TAN</td>
<td>3.0-FV</td>
<td>D</td>
</tr>
<tr>
<td>Kapitel:</td>
<td>Data-Dictionary</td>
<td>Stand:</td>
<td>Seite:</td>
</tr>
<tr>
<td>Abschnitt:</td>
<td>Sonstige</td>
<td>23.02.2018</td>
<td>133</td>
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


###### TAN-Medium-Liste, Elementversion #4

Informationen zu Art und Parametrisierung von TAN-Medien. Als TAN-Medien
werden sowohl TAN-Listen als auch ZKA-TAN-Generatoren / Karten oder
Mobiltelefone bezeichnet.


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
<td>TAN-Medium- Klasse</td>
<td>3</td>
<td>DE</td>
<td>code</td>
<td>1</td>
<td>M</td>
<td>1</td>
<td>A, G, L, M, S</td>
</tr>
<tr>
<td>2</td>
<td>Status</td>
<td>1</td>
<td>DE</td>
<td>code</td>
<td>1</td>
<td>M</td>
<td>1</td>
<td>1, 2, 3, 4</td>
</tr>
<tr>
<td>3</td>
<td>Kartennummer</td>
<td>1</td>
<td>DE</td>
<td>Id</td>
<td>#</td>
<td>C</td>
<td>1</td>
<td>M: DE ,,TAN-Medium- Klasse“=“G“ N: sonst</td>
</tr>
<tr>
<td>4</td>
<td>Kartenfolgenum- mer</td>
<td>1</td>
<td>DE</td>
<td>Id</td>
<td>#</td>
<td>C</td>
<td>1</td>
<td>M: DE ,,TAN-Medium- Klasse“=“G“ N: sonst</td>
</tr>
<tr>
<td>5</td>
<td>Kartenart</td>
<td>1</td>
<td>DE</td>
<td>num</td>
<td>..2</td>
<td>C</td>
<td>1</td>
<td>O: DE „TAN- Generator/-Liste"="G" und DE ,,Eingabe Kartenart zulässig“ (BPD) = „J“ N: sonst</td>
</tr>
<tr>
<td>6</td>
<td>Kontoverbindung Auftraggeber</td>
<td>3</td>
<td>DEG</td>
<td>ktv</td>
<td>#</td>
<td>C</td>
<td>1</td>
<td>O: DE „TAN- Generator/-Liste"="G" N: sonst</td>
</tr>
<tr>
<td>7</td>
<td>gültig ab</td>
<td>1</td>
<td>DE</td>
<td>dat</td>
<td>#</td>
<td>C</td>
<td>1</td>
<td>O: DE „TAN- Generator/-Liste"="G" N: sonst</td>
</tr>
<tr>
<td>8</td>
<td>gültig bis</td>
<td>1</td>
<td>DE</td>
<td>dat</td>
<td>#</td>
<td>C</td>
<td>1</td>
<td>O: DE „TAN- Generator/-Liste"="G" N: sonst</td>
</tr>
<tr>
<td>9</td>
<td>TAN- Listennummer</td>
<td>1</td>
<td>DE</td>
<td>an</td>
<td>..20</td>
<td>C</td>
<td>1</td>
<td>M: DE „TAN-Medium- Klasse“=“L“ N: sonst</td>
</tr>
<tr>
<td>10</td>
<td>Bezeichnung des TAN-Mediums</td>
<td>1</td>
<td>DE</td>
<td>an</td>
<td>..32</td>
<td>C</td>
<td>1</td>
<td>M: DE ,,TAN-Medium- Klasse“=“M“ O: sonst</td>
</tr>
<tr>
<td>11</td>
<td>Mobiltelefonnum- mer verschleiert</td>
<td>1</td>
<td>DE</td>
<td>an</td>
<td>..35</td>
<td>C</td>
<td>1</td>
<td>O: DE ,,TAN-Medium- Klasse"="M" N: sonst</td>
</tr>
<tr>
<td>12</td>
<td>Mobiltelefonnum- mer</td>
<td>1</td>
<td>DE</td>
<td>an</td>
<td>..35</td>
<td>C</td>
<td>1</td>
<td>O: DE ,,TAN-Medium- Klasse“=“M“ N: sonst</td>
</tr>
<tr>
<td>13</td>
<td>SMS- Abbuchungskonto</td>
<td>1</td>
<td>DEG</td>
<td>kti</td>
<td>#</td>
<td>C</td>
<td>1</td>
<td>O: DE ,,TAN-Medium- Klasse"="M"</td>
</tr>
</table>


<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: D</td>
<td>Version: 3.0-FV</td>
<td>Financial Transaction Services (FinTS) Dokument: Security - Sicherheitsverfahren PIN/TAN</td>
</tr>
<tr>
<td>Seite:<br>134</td>
<td>Stand: 23.02.2018</td>
<td>Kapitel: Data-Dictionary<br>Abschnitt: Sonstige</td>
</tr>
</table>


<table>
<tr>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>N: sonst</td>
</tr>
<tr>
<td>14</td>
<td>Anzahl freie TANs</td>
<td>1</td>
<td>DE</td>
<td>num</td>
<td>.3</td>
<td>O</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>15</td>
<td>Letzte Benutzung</td>
<td>1</td>
<td>DE</td>
<td>dat</td>
<td>8</td>
<td>O</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>16</td>
<td>Freigeschaltet am</td>
<td>1</td>
<td>DE</td>
<td>dat</td>
<td>8</td>
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
<td>4</td>
</tr>
</table>


###### TAN-Medium-Liste, Elementversion #5

Informationen zu Art und Parametrisierung von TAN-Medien. Als TAN-Medien
werden sowohl TAN-Listen als auch DK-TAN-Generatoren / Karten oder Mo-
biltelefone sowie bilateral vereinbarte Medien bezeichnet.

Wird das Datenelement ,,TAN-Medium-Klasse" mit ,B" (bilateral vereinbart)
belegt, so muss im Element ,,Sicherheitsfunktion, kodiert“ die entsprechende
Sicherheitsfunktion in der DEG ,,Verfahrensparameter Zwei-Schritt-Verfahren“
referenziert werden.


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
<td>TAN-Medium- Klasse</td>
<td>4</td>
<td>DE</td>
<td>code</td>
<td>1</td>
<td>M</td>
<td>1</td>
<td>A, G, L, M, S, B</td>
</tr>
<tr>
<td>2</td>
<td>Status</td>
<td>1</td>
<td>DE</td>
<td>code</td>
<td>1</td>
<td>M</td>
<td>1</td>
<td>1, 2, 3, 4</td>
</tr>
<tr>
<td>3</td>
<td>Sicherheitsfunkti- on, kodiert</td>
<td>2</td>
<td>DE</td>
<td>num</td>
<td>3</td>
<td>C</td>
<td>1</td>
<td>M: DE ,,TAN-Medium- Klasse“=“B“ N: sonst</td>
</tr>
<tr>
<td>4</td>
<td>Kartennummer</td>
<td>1</td>
<td>DE</td>
<td>Id</td>
<td>#</td>
<td>C</td>
<td>1</td>
<td>M: DE ,,TAN-Medium- Klasse“=“G“ N: sonst</td>
</tr>
<tr>
<td>5</td>
<td>Kartenfolgenum- mer</td>
<td>1</td>
<td>DE</td>
<td>Id</td>
<td>#</td>
<td>C</td>
<td>1</td>
<td>M: DE ,,TAN-Medium- Klasse“=“G“ N: sonst</td>
</tr>
<tr>
<td>6</td>
<td>Kartenart</td>
<td>1</td>
<td>DE</td>
<td>num</td>
<td>.2</td>
<td>C</td>
<td>1</td>
<td>O: DE ,,TAN- Generator/-Liste"="G" und DE ,,Eingabe Kartenart zulässig“ (BPD) = „J“ N: sonst</td>
</tr>
<tr>
<td>7</td>
<td>Kontoverbindung Auftraggeber</td>
<td>3</td>
<td>DEG</td>
<td>ktv</td>
<td>#</td>
<td>C</td>
<td>1</td>
<td>O: DE „TAN- Generator/-Liste"="G" N: sonst</td>
</tr>
<tr>
<td>8</td>
<td>gültig ab</td>
<td>1</td>
<td>DE</td>
<td>dat</td>
<td>#</td>
<td>C</td>
<td>1</td>
<td>O: DE „TAN- Generator/-Liste"="G" N: sonst</td>
</tr>
</table>


<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th>Version:</th>
<th rowspan="2">Kapitel: D</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Security - Sicherheitsverfahren PIN/TAN</td>
<td>3.0-FV</td>
</tr>
<tr>
<td>Kapitel:</td>
<td>Data-Dictionary</td>
<td>Stand:</td>
<td>Seite:</td>
</tr>
<tr>
<td>Abschnitt:</td>
<td>Sonstige</td>
<td>23.02.2018</td>
<td>135</td>
</tr>
</table>


<table>
<tr>
<td>9</td>
<td>gültig bis</td>
<td>1</td>
<td>DE</td>
<td>dat</td>
<td>#</td>
<td>C</td>
<td>1</td>
<td>O: DE „TAN- Generator/-Liste"="G" N: sonst</td>
</tr>
<tr>
<td>10</td>
<td>TAN- Listennummer</td>
<td>1</td>
<td>DE</td>
<td>an</td>
<td>..20</td>
<td>C</td>
<td>1</td>
<td>M: DE „TAN-Medium- Klasse“=“L“ N: sonst</td>
</tr>
<tr>
<td>11</td>
<td>Bezeichnung des TAN-Mediums</td>
<td>1</td>
<td>DE</td>
<td>an</td>
<td>..32</td>
<td>C</td>
<td>1</td>
<td>M: DE ,,TAN-Medium- Klasse“=“M“ O: sonst</td>
</tr>
<tr>
<td>12</td>
<td>Mobiltelefonnum- mer verschleiert</td>
<td>1</td>
<td>DE</td>
<td>an</td>
<td>..35</td>
<td>C</td>
<td>1</td>
<td>O: DE ,,TAN-Medium- Klasse“=“M“ N: sonst</td>
</tr>
<tr>
<td>13</td>
<td>Mobiltelefonnum- mer</td>
<td>1</td>
<td>DE</td>
<td>an</td>
<td>..35</td>
<td>C</td>
<td>1</td>
<td>O: DE ,,TAN-Medium- Klasse“=“M“ N: sonst</td>
</tr>
<tr>
<td>14</td>
<td>SMS- Abbuchungskonto</td>
<td>1</td>
<td>DEG</td>
<td>kti</td>
<td>#</td>
<td>C</td>
<td>1</td>
<td>O: DE ,,TAN-Medium- Klasse“=“M“ N: sonst</td>
</tr>
<tr>
<td>15</td>
<td>Anzahl freie TANs</td>
<td>1</td>
<td>DE</td>
<td>num</td>
<td>..3</td>
<td>O</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>16</td>
<td>Letzte Benutzung</td>
<td>1</td>
<td>DE</td>
<td>dat</td>
<td>8</td>
<td>O</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>17</td>
<td>Freigeschaltet am</td>
<td>1</td>
<td>DE</td>
<td>dat</td>
<td>8</td>
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
<td>5</td>
</tr>
</table>


###### TAN-Prozess

Beim Zwei-Schritt-Verfahren werden die notwendigen Prozess-Schritte mit-
tels des Geschäftsvorfalls HKTAN durchgeführt. Dieser unterstützt flexibel
vier unterschiedliche Ausprägungen für die beiden Prozessvarianten für
Zwei-Schritt-Verfahren, wobei die TAN-Prozesse 3 und 4 nicht isoliert und
nur in Verbindung mit TAN-Prozess=2 auftreten können. Der TAN-Prozess
wird wie folgt kodiert:

Codierung:

Prozessvariante 1:

TAN-Prozess=1:

Im ersten Schritt wird der Auftrags-Hashwert über den Geschäftsvorfall
HKTAN mitgeteilt, im zweiten Schritt erfolgt nach Ermittlung der TAN
aus der zurückgemeldeten Challenge die Einreichung des eigentlichen
Auftrags inklusive der TAN über das normale Auftragssegment.

Abfolge der Segmente am Beispiel HKCCS:

1\. Schritt: HKTAN <> HITAN

2\. Schritt: HKCCS <> HIRMS zu HKCCS

<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: D</td>
<td>Version: 3.0-FV</td>
<td>Financial Transaction Services (FinTS) Dokument: Security - Sicherheitsverfahren PIN/TAN</td>
</tr>
<tr>
<td>Seite:<br>136</td>
<td>Stand: 23.02.2018</td>
<td>Kapitel: Data-Dictionary<br>Abschnitt: Sonstige</td>
</tr>
</table>


###### Prozessvariante 2:

Im ersten Schritt wird der Auftrag komplett über das normale Auftrags-
segment eingereicht, jedoch ohne Übermittlung der TAN. Im zweiten
Schritt erfolgt nach Ermittlung der TAN aus der zurückgemeldeten Chal-
lenge die Einreichung der TAN über den Geschäftsvorfall HKTAN.

Abfolge der Segmente am Beispiel HKCCS:

Schritt 1: HKCCS und HKTAN <> HITAN

Schritt 2: HKTAN <> HITAN und HIRMS zu HICCS


####### TAN-Prozess=2:

kann nur im zweiten Schritt auftreten. Er dient zur Übermittlung der TAN
mittels HKTAN, nachdem der Auftrag selbst zuvor bereits mit TAN-
Prozess=3 oder 4 eingereicht wurde. Dieser Geschäftsvorfall wird mit
HITAN, TAN-Prozess=2 beantwortet.


####### TAN-Prozess=3:

kann nur im ersten Schritt bei Mehrfach-TANs für die zweite und ggf.
dritte TAN auftreten. Hierdurch wird die Einreichung eingeleitet, wenn
zeitversetzte Einreichung von Mehrfach-TANs erlaubt ist.


####### TAN-Prozess=4:

kann nur im ersten Schritt auftreten. Hiermit wird das Zwei-Schritt-
Verfahren nach Prozessvariante 2 für die erste TAN eingeleitet. HKTAN
wird zusammen mit dem Auftragssegment übertragen und durch HITAN
mit TAN-Prozess=4 beantwortet. TAN-Prozess=4 wird auch beim Ge-
schäftsvorfall „Prüfen / Verbrennen von TANs" eingesetzt.


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


###### TAN-Verbrauchsdatum

Datum, an dem die TAN verbraucht wurde.


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


###### TAN-Verbrauchserläuterung

Freitextliche Erläuterung zum Geschäftsvorfall, für den die TAN verbraucht
wurde.


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
<td>..99</td>
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
<td>Security - Sicherheitsverfahren PIN/TAN</td>
<td>3.0-FV</td>
<td>D</td>
</tr>
<tr>
<td>Kapitel:</td>
<td>Data-Dictionary</td>
<td>Stand:</td>
<td>Seite:</td>
</tr>
<tr>
<td>Abschnitt:</td>
<td>Sonstige</td>
<td>23.02.2018</td>
<td>137</td>
</tr>
</table>


###### TAN-Verbrauchskennzeichen

Kennzeichnet, für welchen Zweck eine TAN verbraucht wurde.

Folgende Codes sind gültig:

0
noch nicht verbraucht

1
nicht belegt

2
PIN-Änderung

3
Kontosperre aufheben

4
Aktivieren neuer TAN-Liste

5
Entwertete TAN (maschinell, z. B. bei TAN-Verbrennen)

6
Mitteilung mit TAN

7
Überweisung

8
Wertpapiertransaktion (Neuanlage/Änderung/Löschung)

9
Dauerauftrag (Neuanlage/Änderung/Löschung)

10
Entwertete TAN durch Überschreitung des Zeitlimits
im Zwei-Schritt-Verfahren

11
Entwertete TAN durch Überschreitung des Zeitlimits bei
Mehrfachsignaturen im Zwei-Schritt-Verfahren

12
Entwertete TAN (z. B. bei falsch beantworteter Challenge)

20
Lastschriften

21
Europa-Überweisung

22
Auslandsüberweisung

23
Terminüberweisung

24
Umbuchung

50 bis

98
institutsindividuell

99
Sonstige


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
<td>1</td>
</tr>
</table>


<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: D</td>
<td>Version: 3.0-FV</td>
<td>Financial Transaction Services (FinTS) Dokument: Security - Sicherheitsverfahren PIN/TAN</td>
</tr>
<tr>
<td>Seite:<br>138</td>
<td>Stand: 23.02.2018</td>
<td>Kapitel: Data-Dictionary<br>Abschnitt:<br>Sonstige</td>
</tr>
</table>


###### TAN-Verbrauchsuhrzeit

Transaktionsnummer in Klarschrift.


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


###### TAN zeitversetzt / dialogübergreifend erlaubt

Angabe, ob beim Zwei-Schritt-Verfahren die zeitversetzte Einreichung von
Mehrfach-TANs erlaubt ist. Dies bedeutet, dass ein Zweit-Signierer zu einem
späteren Zeitpunkt eine TAN zu einem zuvor eingereichten Auftrag einrei-
chen darf. Voraussetzung ist, dass grundsätzlich die Verwendung von Mehr-
fach-TANs beim Zwei-Schritt-Verfahren erlaubt ist (vgl. Parameter „Mehr-
fach-TAN erlaubt"). Der Parameter ist in der vorliegenden Version so zu in-
terpretieren, dass ein Institut je nach Parametrisierung entweder zeitversetz-
te Eingabe erlaubt, oder nicht - jedoch nicht beide Varianten.


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


###### TAN Zeit- und Dialogbezug

Beschreibung der protokolltechnischen Möglichkeiten, die dem Kunden im
Zusammenhang mit Mehrfach-TANs zur Verfügung stehen. Es wird festge-
legt, ob die Eingabe der einzelnen TANs zu einem Auftrag durch die unter-
schiedlichen Benutzer synchron in einem Dialog erfolgen muss oder zeitver-
setzt in mehreren Dialogen erfolgen kann. Es wird auch festgelegt, ob ein
Institut nur eines dieser Verfahren oder beide parallel anbietet. Vorausset-
zung ist, dass grundsätzlich die Verwendung von Mehrfach-TANs beim Zwei-
Schritt-Verfahren erlaubt ist (vgl. Parameter ,,Mehrfach-TAN erlaubt"). Bei
Prozessvariante 1 ist der Parameter immer mit „nicht zutreffend“ zu belegen,
da hier generell keine zeitversetzte Verarbeitung möglich ist. Dieser Parame-
ter erweitert den Parameter ,,TAN zeitversetzt / dialogübergreifend erlaubt".

Folgende Codes sind gültig:

1
TAN nicht zeitversetzt / dialogübergreifend erlaubt

2
TAN zeitversetzt / dialogübergreifend erlaubt

3
beide Verfahren unterstützt

4
nicht zutreffend


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


<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th>Version:</th>
<th>Kapitel:</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Security - Sicherheitsverfahren PIN/TAN</td>
<td>3.0-FV</td>
<td>D</td>
</tr>
<tr>
<td>Kapitel:</td>
<td>Data-Dictionary</td>
<td>Stand:</td>
<td>Seite:</td>
</tr>
<tr>
<td>Abschnitt:</td>
<td>Sonstige</td>
<td>23.02.2018</td>
<td>139</td>
</tr>
</table>


###### TAN-Zusatzinformationen

Bei Einsatz des Zwei-Schritt-Verfahrens und Prozessvariante 1 kann ein
Kunde bei Einreichung des Auftrags-Hashwerts mit HKTAN eine kundenspe-
zifische Kennung einstellen, um einen Auftrag bei Anforderung der Challen-
ge wieder erkennen zu können.


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
<td>..99</td>
</tr>
<tr>
<td>Version:</td>
<td>1</td>
</tr>
</table>


###### Technische Identifikation TAN-Verfahren

Da das Kundenprodukt die konkreten Zwei-Schritt-Verfahren i. d. R. nicht
kennt, stellt die technische Identifikation einen vom Institut zur Verfügung
gestellten Schlüsselbegriff dar, der vom Kundenprodukt zur internen Refe-
renzierung des konkreten Zwei-Schritt-Verfahrens verwendet werden kann.
Diese Information dient somit nur der internen Verarbeitung des Kundenpro-
duktes und wird dem Kunden nicht angezeigt.


![](figures/139.1)


Institute sollten die technische Identifikation eines konkre-
ten Zwei-Schritt-Verfahrens nicht wechseln, um dem Kun-
denprodukt eine eindeutige Referenzierung zu ermögli-
chen.

Die technische Identifikation sollte keine Leerzeichen oder
Umlaute enthalten. Als Trennzeichen ist nur ,," (Unter-
strich) zugelassen.


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


###### Text zur Belegung der Benutzerkennung

Da in heutigen PIN/TAN-Verfahren i. d. R. keine Benutzerkennungen ver-
wendet werden, kann dem Kunden mit Hilfe dieses Textes mitgeteilt werden,
welche Eingabe im Feld ,,Benutzerkennung“ des Kundenproduktes erwartet
wird (z. B. die Kundennummer).


![](figures/139.2)


Kundenprodukte sollten diesen Text z.B. als Vorbelegung
im Feld „Benutzerkennung“ anzeigen.


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
<td>Kapitel: D</td>
<td>Version: 3.0-FV</td>
<td>Financial Transaction Services (FinTS) Dokument: Security - Sicherheitsverfahren PIN/TAN</td>
</tr>
<tr>
<td>Seite:<br>140</td>
<td>Stand: 23.02.2018</td>
<td>Kapitel: Data-Dictionary<br>Abschnitt: Sonstige</td>
</tr>
</table>


###### Text zur Belegung der Kunden-ID

Da in heutigen PIN/TAN-Verfahren i.d.R. keine Kunden-IDs verwendet wer-
den, kann dem Kunden mit Hilfe dieses Textes mitgeteilt werden, welche
Eingabe im Feld ,,Kunden-ID" des Kundenproduktes erwartet wird (z. B. die
Kundennummer).


![](figures/140.1)


Kundenprodukte sollten diesen Text z.B. als Vorbelegung
im Feld ,,Kunden-ID“ anzeigen.


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


###### Text zur Belegung des Rückgabewertes im Zwei-Schritt-Verfahren

Es wird ein Textfeld übergeben, das die Art des geforderten Rückgabewertes
beschreibt, z. B. ,,Challenge“ oder ,Index“.


![](figures/140.2)


Kundenprodukte sollten diesen Text als Beschreibung vor
bzw. in dem Eingabefeld für den Rückgabewert anzeigen.


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


###### Transaktionskonto

Zahlungsverkehrskontoverbindung, für die eine mit Entgelten belegte Trans-
aktion durchgeführt wurde. Dies ist z. B. bei einer Überweisung die Auftrag-
geberkontoverbindung.


<table>
<tr>
<td>Typ:</td>
<td>DEG</td>
</tr>
<tr>
<td>Format:</td>
<td>kti</td>
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


###### Verfahrensbestätigung

Beim Wechsel zwischen unterschiedlichen Zwei-Schritt-Verfahren kann in
bestimmten Situationen eine explizite Bestätigung des Kunden erforderlich
sein, die als Willenserklärung auch an das Kreditinstitut übermittelt werden
muss, um dort mit in die Dokumentation einfließen zu können.

<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th>Version:</th>
<th>Kapitel:</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Security - Sicherheitsverfahren PIN/TAN</td>
<td>3.0-FV</td>
<td>D</td>
</tr>
<tr>
<td>Kapitel:</td>
<td>Data-Dictionary</td>
<td>Stand:</td>
<td>Seite:</td>
</tr>
<tr>
<td>Abschnitt:</td>
<td>Sonstige</td>
<td>23.02.2018</td>
<td>141</td>
</tr>
</table>


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


###### Verfahrensbestätigung erforderlich

Über diesen Parameter wird festgelegt, ob im Fall eines Wechsels zwischen
Zwei-Schritt-Verfahren eine explizite Verfahrensbestätigung des Kunden er-
forderlich ist oder nicht.


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


###### Verfahrensparameter Zwei-Schritt-Verfahren, Elementversion #1

Parametrisierung konkreter Zwei-Schritt-Verfahren.


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
<td>Sicherheitsfunktion, kodiert</td>
<td>1</td>
<td>DE</td>
<td>code</td>
<td>..3</td>
<td>M</td>
<td>1</td>
<td>900, ., 997</td>
</tr>
<tr>
<td>2</td>
<td>TAN-Prozess</td>
<td>1</td>
<td>DE</td>
<td>code</td>
<td>1</td>
<td>M</td>
<td>1</td>
<td>1,2</td>
</tr>
<tr>
<td>3</td>
<td>Technische Identifi- kation TAN- Verfahren</td>
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
<td>Name des Zwei- Schritt-Verfahrens</td>
<td>1</td>
<td>DE</td>
<td>an</td>
<td>..30</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>5</td>
<td>Maximale Länge des TAN-Eingabewertes im Zwei-Schritt- Verfahren</td>
<td>1</td>
<td>DE</td>
<td>num</td>
<td>..2</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>6</td>
<td>Erlaubtes Format im Zwei-Schritt- Verfahren</td>
<td>1</td>
<td>DE</td>
<td>code</td>
<td>1</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>7</td>
<td>Text zur Belegung des Rückgabewertes im Zwei-Schritt- Verfahren</td>
<td>1</td>
<td>DE</td>
<td>an</td>
<td>..30</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>8</td>
<td>Maximale Länge des Rückgabewertes im Zwei-Schritt- Verfahren</td>
<td>1</td>
<td>DE</td>
<td>num</td>
<td>..3</td>
<td>M</td>
<td>1</td>
<td>1..256</td>
</tr>
<tr>
<td>9</td>
<td>Anzahl unterstützter aktiver TAN-Listen</td>
<td>1</td>
<td>DE</td>
<td>num</td>
<td>1</td>
<td>O</td>
<td>1</td>
<td></td>
</tr>
</table>


<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: D</td>
<td>Version: 3.0-FV</td>
<td>Financial Transaction Services (FinTS) Dokument: Security - Sicherheitsverfahren PIN/TAN</td>
</tr>
<tr>
<td>Seite: 142</td>
<td>Stand: 23.02.2018</td>
<td>Kapitel: Data-Dictionary<br>Abschnitt: Sonstige</td>
</tr>
</table>


<table>
<tr>
<td>10</td>
<td>Mehrfach-TAN er- laubt</td>
<td>1</td>
<td>DE</td>
<td>jn</td>
<td>#</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>11</td>
<td>TAN zeitversetzt / di- alogübergreifend er- laubt</td>
<td>1</td>
<td>DE</td>
<td>jn</td>
<td>#</td>
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
<td>1</td>
</tr>
</table>


###### Verfahrensparameter Zwei-Schritt-Verfahren, Elementversion #2

Parametrisierung konkreter Zwei-Schritt-Verfahren.


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
<td>Sicherheitsfunktion, kodiert</td>
<td>1</td>
<td>DE</td>
<td>code</td>
<td>..3</td>
<td>M</td>
<td>1</td>
<td>900, ., 997</td>
</tr>
<tr>
<td>2</td>
<td>TAN-Prozess</td>
<td>1</td>
<td>DE</td>
<td>code</td>
<td>1</td>
<td>M</td>
<td>1</td>
<td>1,2</td>
</tr>
<tr>
<td>3</td>
<td>Technische Identifi- kation TAN- Verfahren</td>
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
<td>Name des Zwei- Schritt-Verfahrens</td>
<td>1</td>
<td>DE</td>
<td>an</td>
<td>..30</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>5</td>
<td>Maximale Länge des TAN-Eingabewertes im Zwei-Schritt- Verfahren</td>
<td>1</td>
<td>DE</td>
<td>num</td>
<td>..2</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>6</td>
<td>Erlaubtes Format im Zwei-Schritt- Verfahren</td>
<td>1</td>
<td>DE</td>
<td>code</td>
<td>1</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>7</td>
<td>Text zur Belegung des Rückgabewertes im Zwei-Schritt- Verfahren</td>
<td>1</td>
<td>DE</td>
<td>an</td>
<td>..30</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>8</td>
<td>Maximale Länge des Rückgabewertes im Zwei-Schritt- Verfahren</td>
<td>2</td>
<td>DE</td>
<td>num</td>
<td>..3</td>
<td>M</td>
<td>1</td>
<td>1..256</td>
</tr>
<tr>
<td>9</td>
<td>Anzahl unterstützter aktiver TAN-Listen</td>
<td>1</td>
<td>DE</td>
<td>num</td>
<td>1</td>
<td>O</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>10</td>
<td>Mehrfach-TAN er- laubt</td>
<td>1</td>
<td>DE</td>
<td>jn</td>
<td>#</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>11</td>
<td>TAN Zeit- und Dia- logbezug</td>
<td>1</td>
<td>DE</td>
<td>code</td>
<td>1</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>12</td>
<td>TAN-Listennummer erforderlich</td>
<td>1</td>
<td>DE</td>
<td>code</td>
<td>1</td>
<td>M</td>
<td>1</td>
<td>0,2</td>
</tr>
<tr>
<td>13</td>
<td>Auftragsstorno er- laubt</td>
<td>1</td>
<td>DE</td>
<td>jn</td>
<td>#</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>14</td>
<td>Challenge-Klasse er- forderlich</td>
<td>1</td>
<td>DE</td>
<td>jn</td>
<td>#</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>15</td>
<td>Challenge-Betrag er- forderlich</td>
<td>1</td>
<td>DE</td>
<td>jn</td>
<td>#</td>
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
<td>Security - Sicherheitsverfahren PIN/TAN</td>
<td>3.0-FV</td>
<td>D</td>
</tr>
<tr>
<td>Kapitel:</td>
<td>Data-Dictionary</td>
<td>Stand:</td>
<td>Seite:</td>
</tr>
<tr>
<td>Abschnitt:</td>
<td>Sonstige</td>
<td>23.02.2018</td>
<td>143</td>
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


###### Verfahrensparameter Zwei-Schritt-Verfahren, Elementversion #3

Parametrisierung konkreter Zwei-Schritt-Verfahren.


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
<td>Sicherheitsfunktion, kodiert</td>
<td>1</td>
<td>DE</td>
<td>code</td>
<td>..3</td>
<td>M</td>
<td>1</td>
<td>900,., 997</td>
</tr>
<tr>
<td>2</td>
<td>TAN-Prozess</td>
<td>1</td>
<td>DE</td>
<td>code</td>
<td>1</td>
<td>M</td>
<td>1</td>
<td>1,2</td>
</tr>
<tr>
<td>3</td>
<td>Technische Identifi- kation TAN- Verfahren</td>
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
<td>Name des Zwei- Schritt-Verfahrens</td>
<td>1</td>
<td>DE</td>
<td>an</td>
<td>..30</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>5</td>
<td>Maximale Länge des TAN-Eingabewertes im Zwei-Schritt- Verfahren</td>
<td>1</td>
<td>DE</td>
<td>num</td>
<td>..2</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>6</td>
<td>Erlaubtes Format im Zwei-Schritt- Verfahren</td>
<td>1</td>
<td>DE</td>
<td>code</td>
<td>1</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>7</td>
<td>Text zur Belegung des Rückgabewertes im Zwei-Schritt- Verfahren</td>
<td>1</td>
<td>DE</td>
<td>an</td>
<td>..30</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>8</td>
<td>Maximale Länge des Rückgabewertes im Zwei-Schritt- Verfahren</td>
<td>2</td>
<td>DE</td>
<td>num</td>
<td>..3</td>
<td>M</td>
<td>1</td>
<td>1..256</td>
</tr>
<tr>
<td>9</td>
<td>Anzahl unterstützter aktiver TAN-Listen</td>
<td>1</td>
<td>DE</td>
<td>num</td>
<td>1</td>
<td>O</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>10</td>
<td>Mehrfach-TAN er- laubt</td>
<td>1</td>
<td>DE</td>
<td>jn</td>
<td>#</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>11</td>
<td>TAN Zeit- und Dia- logbezug</td>
<td>1</td>
<td>DE</td>
<td>code</td>
<td>1</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>12</td>
<td>TAN-Listennummer erforderlich</td>
<td>1</td>
<td>DE</td>
<td>code</td>
<td>1</td>
<td>M</td>
<td>1</td>
<td>0,2</td>
</tr>
<tr>
<td>13</td>
<td>Auftragsstorno er- laubt</td>
<td>1</td>
<td>DE</td>
<td>jn</td>
<td>#</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>14</td>
<td>Challenge-Klasse er- forderlich</td>
<td>1</td>
<td>DE</td>
<td>jn</td>
<td>#</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>15</td>
<td>Challenge-Betrag er- forderlich</td>
<td>1</td>
<td>DE</td>
<td>jn</td>
<td>#</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>16</td>
<td>Initialisierungsmodus</td>
<td>1</td>
<td>DE</td>
<td>code</td>
<td>#</td>
<td>M</td>
<td>1</td>
<td>00,01,02</td>
</tr>
<tr>
<td>17</td>
<td>Bezeichnung des TAN-Mediums erfor- derlich</td>
<td>1</td>
<td>DE</td>
<td>code</td>
<td>1</td>
<td>M</td>
<td>1</td>
<td>0, 2</td>
</tr>
<tr>
<td>18</td>
<td>Anzahl unterstützter aktiver TAN-Medien</td>
<td>1</td>
<td>DE</td>
<td>num</td>
<td>1</td>
<td>O</td>
<td>1</td>
<td></td>
</tr>
</table>


<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: D</td>
<td>Version: 3.0-FV</td>
<td>Financial Transaction Services (FinTS) Dokument: Security - Sicherheitsverfahren PIN/TAN</td>
</tr>
<tr>
<td>Seite: 144</td>
<td>Stand: 23.02.2018</td>
<td>Kapitel: Data-Dictionary<br>Abschnitt: Sonstige</td>
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


###### Verfahrensparameter Zwei-Schritt-Verfahren, Elementversion #4

Parametrisierung konkreter Zwei-Schritt-Verfahren.


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
<td>Sicherheitsfunktion, kodiert</td>
<td>1</td>
<td>DE</td>
<td>code</td>
<td>..3</td>
<td>M</td>
<td>1</td>
<td>900, ., 997</td>
</tr>
<tr>
<td>2</td>
<td>TAN-Prozess</td>
<td>1</td>
<td>DE</td>
<td>code</td>
<td>1</td>
<td>M</td>
<td>1</td>
<td>1,2</td>
</tr>
<tr>
<td>3</td>
<td>Technische Identifi- kation TAN- Verfahren</td>
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
<td>ZKA TAN-Verfahren</td>
<td>1</td>
<td>DE</td>
<td>an</td>
<td>..32</td>
<td>O</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>5</td>
<td>Version ZKA TAN- Verfahren</td>
<td>1</td>
<td>DE</td>
<td>an</td>
<td>.. 10</td>
<td>O</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>6</td>
<td>Name des Zwei- Schritt-Verfahrens</td>
<td>1</td>
<td>DE</td>
<td>an</td>
<td>..30</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>7</td>
<td>Maximale Länge des TAN-Eingabewertes im Zwei-Schritt- Verfahren</td>
<td>1</td>
<td>DE</td>
<td>num</td>
<td>..2</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>8</td>
<td>Erlaubtes Format im Zwei-Schritt- Verfahren</td>
<td>1</td>
<td>DE</td>
<td>code</td>
<td>1</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>9</td>
<td>Text zur Belegung des Rückgabewertes im Zwei-Schritt- Verfahren</td>
<td>1</td>
<td>DE</td>
<td>an</td>
<td>..30</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>10</td>
<td>Maximale Länge des Rückgabewertes im Zwei-Schritt- Verfahren</td>
<td>2</td>
<td>DE</td>
<td>num</td>
<td>..3</td>
<td>M</td>
<td>1</td>
<td>1..256</td>
</tr>
<tr>
<td>11</td>
<td>Anzahl unterstützter aktiver TAN-Listen</td>
<td>1</td>
<td>DE</td>
<td>num</td>
<td>1</td>
<td>O</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>12</td>
<td>Mehrfach-TAN er- laubt</td>
<td>1</td>
<td>DE</td>
<td>jn</td>
<td>#</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>13</td>
<td>TAN Zeit- und Dia- logbezug</td>
<td>1</td>
<td>DE</td>
<td>code</td>
<td>1</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>14</td>
<td>TAN-Listennummer erforderlich</td>
<td>1</td>
<td>DE</td>
<td>code</td>
<td>1</td>
<td>M</td>
<td>1</td>
<td>0,2</td>
</tr>
<tr>
<td>15</td>
<td>Auftragsstorno er- laubt</td>
<td>1</td>
<td>DE</td>
<td>jn</td>
<td>#</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>16</td>
<td>SMS- Abbuchungskonto erforderlich</td>
<td>1</td>
<td>DE</td>
<td>jn</td>
<td>#</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>17</td>
<td>Challenge-Klasse er- forderlich</td>
<td>1</td>
<td>DE</td>
<td>jn</td>
<td>#</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>18</td>
<td>Challenge-Betrag er- forderlich</td>
<td>1</td>
<td>DE</td>
<td>jn</td>
<td>#</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>19</td>
<td>Challenge strukturiert</td>
<td>1</td>
<td>DE</td>
<td>jn</td>
<td>#</td>
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
<td>Security - Sicherheitsverfahren PIN/TAN</td>
<td>3.0-FV</td>
<td>D</td>
</tr>
<tr>
<td>Kapitel:</td>
<td>Data-Dictionary</td>
<td>Stand:</td>
<td>Seite:</td>
</tr>
<tr>
<td>Abschnitt:</td>
<td>Sonstige</td>
<td>23.02.2018</td>
<td>145</td>
</tr>
</table>


<table>
<tr>
<td>20</td>
<td>Initialisierungsmodus</td>
<td>1</td>
<td>DE</td>
<td>code</td>
<td>#</td>
<td>M</td>
<td>1</td>
<td>00,01,02</td>
</tr>
<tr>
<td>21</td>
<td>Bezeichnung des TAN-Mediums erfor- derlich</td>
<td>1</td>
<td>DE</td>
<td>code</td>
<td>1</td>
<td>M</td>
<td>1</td>
<td>0, 1, 2</td>
</tr>
<tr>
<td>22</td>
<td>Anzahl unterstützter aktiver TAN-Medien</td>
<td>1</td>
<td>DE</td>
<td>num</td>
<td>1</td>
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
<td>4</td>
</tr>
</table>


###### Verfahrensparameter Zwei-Schritt-Verfahren, Elementversion #5

Parametrisierung konkreter Zwei-Schritt-Verfahren.


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
<td>Sicherheitsfunktion, kodiert</td>
<td>1</td>
<td>DE</td>
<td>code</td>
<td>..3</td>
<td>M</td>
<td>1</td>
<td>900, ., 997</td>
</tr>
<tr>
<td>2</td>
<td>TAN-Prozess</td>
<td>1</td>
<td>DE</td>
<td>code</td>
<td>1</td>
<td>M</td>
<td>1</td>
<td>1,2</td>
</tr>
<tr>
<td>3</td>
<td>Technische Identifi- kation TAN- Verfahren</td>
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
<td>ZKA TAN-Verfahren</td>
<td>1</td>
<td>DE</td>
<td>an</td>
<td>.32</td>
<td>O</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>5</td>
<td>Version ZKA TAN- Verfahren</td>
<td>1</td>
<td>DE</td>
<td>an</td>
<td>.10</td>
<td>O</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>6</td>
<td>Name des Zwei- Schritt-Verfahrens</td>
<td>1</td>
<td>DE</td>
<td>an</td>
<td>..30</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>7</td>
<td>Maximale Länge des TAN-Eingabewertes im Zwei-Schritt- Verfahren</td>
<td>1</td>
<td>DE</td>
<td>num</td>
<td>..2</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>8</td>
<td>Erlaubtes Format im Zwei-Schritt- Verfahren</td>
<td>1</td>
<td>DE</td>
<td>code</td>
<td>1</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>9</td>
<td>Text zur Belegung des Rückgabewertes im Zwei-Schritt- Verfahren</td>
<td>1</td>
<td>DE</td>
<td>an</td>
<td>..30</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>10</td>
<td>Maximale Länge des Rückgabewertes im Zwei-Schritt- Verfahren</td>
<td>3</td>
<td>DE</td>
<td>num</td>
<td>..4</td>
<td>M</td>
<td>1</td>
<td>1..2048</td>
</tr>
<tr>
<td>11</td>
<td>Anzahl unterstützter aktiver TAN-Listen</td>
<td>1</td>
<td>DE</td>
<td>num</td>
<td>1</td>
<td>O</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>12</td>
<td>Mehrfach-TAN er- laubt</td>
<td>1</td>
<td>DE</td>
<td>jn</td>
<td>#</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>13</td>
<td>TAN Zeit- und Dia- logbezug</td>
<td>1</td>
<td>DE</td>
<td>code</td>
<td>1</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>14</td>
<td>TAN-Listennummer erforderlich</td>
<td>1</td>
<td>DE</td>
<td>code</td>
<td>1</td>
<td>M</td>
<td>1</td>
<td>0,2</td>
</tr>
</table>


<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: D</td>
<td>Version: 3.0-FV</td>
<td>Financial Transaction Services (FinTS) Dokument: Security - Sicherheitsverfahren PIN/TAN</td>
</tr>
<tr>
<td>Seite: 146</td>
<td>Stand: 23.02.2018</td>
<td>Kapitel: Data-Dictionary<br>Abschnitt: Sonstige</td>
</tr>
</table>


<table>
<tr>
<td>15</td>
<td>Auftragsstorno er- laubt</td>
<td>1</td>
<td>DE</td>
<td>jn</td>
<td>#</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>16</td>
<td>SMS- Abbuchungskonto erforderlich</td>
<td>2</td>
<td>DE</td>
<td>code</td>
<td>1</td>
<td>M</td>
<td>1</td>
<td>0, 1, 2</td>
</tr>
<tr>
<td>17</td>
<td>Auftraggeberkonto erforderlich</td>
<td>1</td>
<td>DE</td>
<td>code</td>
<td>1</td>
<td>M</td>
<td>1</td>
<td>0, 2</td>
</tr>
<tr>
<td>18</td>
<td>Challenge-Klasse er- forderlich</td>
<td>1</td>
<td>DE</td>
<td>jn</td>
<td>#</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>19</td>
<td>Challenge strukturiert</td>
<td>1</td>
<td>DE</td>
<td>jn</td>
<td>#</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>20</td>
<td>Initialisierungsmodus</td>
<td>1</td>
<td>DE</td>
<td>code</td>
<td>#</td>
<td>M</td>
<td>1</td>
<td>00,01,02</td>
</tr>
<tr>
<td>21</td>
<td>Bezeichnung des TAN-Mediums erfor- derlich</td>
<td>1</td>
<td>DE</td>
<td>code</td>
<td>1</td>
<td>M</td>
<td>1</td>
<td>0, 1, 2</td>
</tr>
<tr>
<td>22</td>
<td>Anzahl unterstützter aktiver TAN-Medien</td>
<td>1</td>
<td>DE</td>
<td>num</td>
<td>1</td>
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
<td>5</td>
</tr>
</table>


###### Verfahrensparameter Zwei-Schritt-Verfahren, Elementversion #6

Parametrisierung konkreter Zwei-Schritt-Verfahren.


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
<td>Sicherheitsfunktion, kodiert</td>
<td>1</td>
<td>DE</td>
<td>code</td>
<td>..3</td>
<td>M</td>
<td>1</td>
<td>900, ., 997</td>
</tr>
<tr>
<td>2</td>
<td>TAN-Prozess</td>
<td>1</td>
<td>DE</td>
<td>code</td>
<td>1</td>
<td>M</td>
<td>1</td>
<td>1,2</td>
</tr>
<tr>
<td>3</td>
<td>Technische Identifi- kation TAN- Verfahren</td>
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
<td>ZKA TAN-Verfahren</td>
<td>1</td>
<td>DE</td>
<td>an</td>
<td>.32</td>
<td>O</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>5</td>
<td>Version ZKA TAN- Verfahren</td>
<td>1</td>
<td>DE</td>
<td>an</td>
<td>..10</td>
<td>O</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>6</td>
<td>Name des Zwei- Schritt-Verfahrens</td>
<td>1</td>
<td>DE</td>
<td>an</td>
<td>..30</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>7</td>
<td>Maximale Länge des TAN-Eingabewertes im Zwei-Schritt- Verfahren</td>
<td>1</td>
<td>DE</td>
<td>num</td>
<td>..2</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>8</td>
<td>Erlaubtes Format im Zwei-Schritt- Verfahren</td>
<td>1</td>
<td>DE</td>
<td>code</td>
<td>1</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>9</td>
<td>Text zur Belegung des Rückgabewertes im Zwei-Schritt- Verfahren</td>
<td>1</td>
<td>DE</td>
<td>an</td>
<td>..30</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>10</td>
<td>Maximale Länge des Rückgabewertes im Zwei-Schritt- Verfahren</td>
<td>3</td>
<td>DE</td>
<td>num</td>
<td>..4</td>
<td>M</td>
<td>1</td>
<td>1..2048</td>
</tr>
<tr>
<td>11</td>
<td>Mehrfach-TAN er-</td>
<td>1</td>
<td>DE</td>
<td>jn</td>
<td>#</td>
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
<td>Security - Sicherheitsverfahren PIN/TAN</td>
<td>3.0-FV</td>
<td>D</td>
</tr>
<tr>
<td>Kapitel:</td>
<td>Data-Dictionary</td>
<td>Stand:</td>
<td>Seite:</td>
</tr>
<tr>
<td>Abschnitt:</td>
<td>Sonstige</td>
<td>23.02.2018</td>
<td>147</td>
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
<td></td>
<td>laubt</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>12</td>
<td>TAN Zeit- und Dia- logbezug</td>
<td>1</td>
<td>DE</td>
<td>code</td>
<td>1</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>13</td>
<td>Auftragsstorno er- laubt</td>
<td>1</td>
<td>DE</td>
<td>jn</td>
<td>#</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>14</td>
<td>SMS- Abbuchungskonto erforderlich</td>
<td>2</td>
<td>DE</td>
<td>code</td>
<td>1</td>
<td>M</td>
<td>1</td>
<td>0, 1, 2</td>
</tr>
<tr>
<td>15</td>
<td>Auftraggeberkonto erforderlich</td>
<td>1</td>
<td>DE</td>
<td>code</td>
<td>1</td>
<td>M</td>
<td>1</td>
<td>0, 2</td>
</tr>
<tr>
<td>16</td>
<td>Challenge-Klasse er- forderlich</td>
<td>1</td>
<td>DE</td>
<td>jn</td>
<td>#</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>17</td>
<td>Challenge strukturiert</td>
<td>1</td>
<td>DE</td>
<td>jn</td>
<td>#</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>18</td>
<td>Initialisierungsmodus</td>
<td>1</td>
<td>DE</td>
<td>code</td>
<td>#</td>
<td>M</td>
<td>1</td>
<td>00,01,02</td>
</tr>
<tr>
<td>19</td>
<td>Bezeichnung des TAN-Mediums erfor- derlich</td>
<td>1</td>
<td>DE</td>
<td>code</td>
<td>1</td>
<td>M</td>
<td>1</td>
<td>0, 1, 2</td>
</tr>
<tr>
<td>20</td>
<td>Antwort HHD UC er- forderlich</td>
<td>1</td>
<td>DE</td>
<td>jn</td>
<td>#</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>21</td>
<td>Anzahl unterstützter aktiver TAN-Medien</td>
<td>1</td>
<td>DE</td>
<td>num</td>
<td>1</td>
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
<td>6</td>
</tr>
</table>


###### Version ZKA-TAN-Verfahren

Bei Einsatz eines ZKA TAN Zwei-Schritt-Verfahrens ist hier optional die An-
gabe einer Versionsbezeichnung möglich.

Bei folgenden ZKA-Verfahren ist die Angabe der Version zwingend erforder-
lich; die verbindlichen Werte sind den jeweiligen Spezifikationen bzw. Bele-
gungsrichtlinien zu entnehmen:

HHD:
z. B. 1.3.1
(vgl. [HHD-Belegung])

HHDOPT1: z. B. 1.4

(vgl. [HHD-Belegung])


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
<td>.. 10</td>
</tr>
<tr>
<td>Version:</td>
<td>1</td>
</tr>
</table>


###### Versionsinfo der chipTAN-Applikation

Nur bei bidirektionalen chipTAN-Verfahren mit Secoder 3: Bestandteil der
Antwort auf das Secoder-Kommando ,,SECODER TRANSMIT HHDUC".

<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: D</td>
<td>Version: 3.0-FV</td>
<td>Financial Transaction Services (FinTS) Dokument: Security - Sicherheitsverfahren PIN/TAN</td>
</tr>
<tr>
<td>Seite:<br>148</td>
<td>Stand: 23.02.2018</td>
<td>Kapitel: Data-Dictionary<br>Abschnitt: Sonstige</td>
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
<td>256</td>
</tr>
<tr>
<td>Version:</td>
<td>1</td>
</tr>
</table>


###### Von Datum

Anfangsdatum eines Zeitraums (s. [Formals], Kap. B.6.3 „Abholauftrag“).

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


W


###### Weitere TAN folgt

Das Kundenprodukt teilt mit, ob dies die letzte / einzige benötigte TAN für
den bereits eingereichten Auftrag ist, oder ob noch mindestens eine weitere
TAN eingereicht wird.


![](figures/148.1)


Kundenprodukte können entweder aus der UPD („Anzahl
benötigter Signaturen“) oder aufgrund eigener Administrati-
onsfunktionen entscheiden, ob für einen Auftrag noch wei-
tere TANs benötigt werden.


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


Z


###### ZKA TAN-Verfahren

Es existieren FinTS Zwei-Schritt-Verfahren, die entweder im ZKA standardi-
siert sind oder deren Rahmenbedingungen für den Einsatz festgelegt sind.

Folgende Verfahrensbezeichnungen sind gültig:

HHD
[HHD], [HHD-Belegung]

HHDUC
[HHD], [HHD-Belegung]

HHDOPT1 [HHD], [HHD-Belegung], [HHD-Erweiterung]
mobileTAN [mobileTAN]

<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th>Version:</th>
<th>Kapitel:</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Security - Sicherheitsverfahren PIN/TAN</td>
<td>3.0-FV</td>
<td>D</td>
</tr>
<tr>
<td>Kapitel:</td>
<td>Data-Dictionary</td>
<td>Stand:</td>
<td>Seite:</td>
</tr>
<tr>
<td>Abschnitt:</td>
<td>Sonstige</td>
<td>23.02.2018</td>
<td>149</td>
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
<td>..32</td>
</tr>
<tr>
<td>Version:</td>
<td>1</td>
</tr>
</table>


###### Zulässige Kartenart

Informationen zu den zulässigen Kartenarten für das An- bzw. Ummelden
von TAN-Generatoren (HKTAU).


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


###### Zustimmung zur Kontaktaufnahme unterstützt

Über diesen Parameter wird festgelegt, ob das Kreditinstitut die Steuerung
der Zustimmung des Kunden zur Kontaktaufnahme unterstützt oder nicht.


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
<th>Kapitel: D</th>
<th>Version: 3.0-FV</th>
<th>Financial Transaction Services (FinTS) Dokument: Security - Sicherheitsverfahren PIN/TAN</th>
</tr>
<tr>
<td>Seite: 150</td>
<td>Stand: 23.02.2018</td>
<td>Kapitel: Archiv: Ältere Segmentversionen<br>Abschnitt: HKTAN für Zwei-Schritt-TAN-Einreichung</td>
</tr>
</table>


###### E. ARCHIV: ÄLTERE SEGMENTVERSIONEN

In diesem Abschnitt befinden sich ältere Segmentversionen von HKTAN bzw.
PIN/TAN-Managementgeschäftsvorfällen, die je nach Institut noch angeboten wer-
den.


####### E.1 HKTAN für Zwei-Schritt-TAN-Einreichung


######## E.1.1 Geschäftsvorfall HKTAN in Segmentversion #1

Die Segmentversion #1 dieses Geschäftsvorfalls wird von Kreditinstituten verwen-
det, die das Zwei-Schritt-Verfahren ohne die Erweiterungen zur Unterstützung der
Challenge-Klasse anbieten. Kreditinstitute können zusätzlich auch die Segmentver-
sion #2 oder höher anbieten.

Realisierung Bank:
verpflichtend in Segmentversion #1 oder höher, falls
Geschäftsvorfälle mit PIN/TAN-Absicherung im Zwei-Schritt-
Verfahren angeboten werden

Realisierung Kunde:
optional


######### a) Kundenauftrag


######### Format


<table>
<tr>
<td>Name:</td>
<td>Zwei-Schritt-TAN-Einreichung</td>
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
<td>HKTAN</td>
</tr>
<tr>
<td>Bezugssegment:</td>
<td>-</td>
</tr>
<tr>
<td>Segmentversion:</td>
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
<td>TAN-Prozess</td>
<td>1</td>
<td>DE</td>
<td>code</td>
<td>1</td>
<td>M</td>
<td>1</td>
<td>1, 2, 3, 4</td>
</tr>
<tr>
<td>3</td>
<td>Auftrags-Hashwert</td>
<td>1</td>
<td>DE</td>
<td>bin</td>
<td>.256</td>
<td>C</td>
<td>1</td>
<td>M: bei Auftrags- Hashwertverfahren&lt;&gt;0 und TAN-Prozess=1 N: sonst</td>
</tr>
<tr>
<td>4</td>
<td>Auftragsreferenz</td>
<td>1</td>
<td>DE</td>
<td>an</td>
<td>..35</td>
<td>C</td>
<td>1</td>
<td>M: bei TAN-Prozess=2, 3 N: TAN-Prozess=1, 4</td>
</tr>
<tr>
<td>5</td>
<td>TAN-Listennummer</td>
<td>1</td>
<td>DE</td>
<td>an</td>
<td>..20</td>
<td>C</td>
<td>1</td>
<td>M: bei TAN-Prozess=1, 3, 4 und „Anzahl unterstützter aktiver TAN-Listen“ &gt; 1 O: sonst</td>
</tr>
<tr>
<td>6</td>
<td>Weitere TAN folgt</td>
<td>1</td>
<td>DE</td>
<td>jn</td>
<td>1</td>
<td>C</td>
<td>1</td>
<td>M: bei TAN-Prozess=1, 2 N: bei TAN-Prozess=3, 4</td>
</tr>
<tr>
<td>7</td>
<td>TAN- Zusatzinformatio- nen</td>
<td>1</td>
<td>DE</td>
<td>an</td>
<td>.99</td>
<td>C</td>
<td>1</td>
<td>O: bei TAN-Prozess=1 N: bei TAN-Prozess=2, 3, 4</td>
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
<td>Dokument:</td>
<td>Security - Sicherheitsverfahren PIN/TAN</td>
</tr>
<tr>
<td>Kapitel:<br>Abschnitt:</td>
<td>Archiv: Ältere Segmentversionen HKTAN für Zwei-Schritt-TAN-Einreichung</td>
<td>Stand: 23.02.2018</td>
<td>Seite: 151</td>
</tr>
</table>


###### ◆ Belegungsrichtlinien


####### Auftragsreferenz

Als Auftragsreferenz ist derjenige Wert einzustellen, der bei der Auftragsein-
reichung im Rahmen der Kreditinstitutsrückmeldung mitgeteilt wurde.


####### TAN-Listennummer

Ist in der BPD als ,,Anzahl unterstützter aktiver TAN-Listen“ ein Wert > 1 an-
gegeben, so muss der Kunde z. B. im Falle eines indizierten TAN-Verfahrens
hier seine für diesen Auftrag zu verwendende TAN-Liste angeben.

<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: D</td>
<td>Version: 3.0-FV</td>
<td>Financial Transaction Services (FinTS) Dokument: Security - Sicherheitsverfahren PIN/TAN</td>
</tr>
<tr>
<td>Seite:<br>152</td>
<td>Stand: 23.02.2018</td>
<td>Kapitel: Archiv: Ältere Segmentversionen<br>Abschnitt: HKTAN für Zwei-Schritt-TAN-Einreichung</td>
</tr>
</table>


b)
Kreditinstitutsrückmeldung

Format


<table>
<tr>
<td>Name:</td>
<td>Zwei-Schritt-TAN-Einreichung Rückmeldung</td>
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
<td>HITAN</td>
</tr>
<tr>
<td>Bezugssegment:</td>
<td>HKTAN</td>
</tr>
<tr>
<td>Segmentversion:</td>
<td>1</td>
</tr>
<tr>
<td>Anzahl:</td>
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
<td>TAN-Prozess</td>
<td>1</td>
<td>DE</td>
<td>code</td>
<td>1</td>
<td>M</td>
<td>1</td>
<td>1, 2, 3, 4</td>
</tr>
<tr>
<td>3</td>
<td>Auftrags-Hashwert</td>
<td>1</td>
<td>DE</td>
<td>bin</td>
<td>.256</td>
<td>C</td>
<td>1</td>
<td>M: bei Auftrags- Hashwertverfahren&lt;&gt;0 und TAN-Prozess=1 N: sonst</td>
</tr>
<tr>
<td>4</td>
<td>Auftragsreferenz</td>
<td>1</td>
<td>DE</td>
<td>an</td>
<td>..35</td>
<td>C</td>
<td>1</td>
<td>M: bei TAN-Prozess=2, 3, 4 O: bei TAN-Prozess=1</td>
</tr>
<tr>
<td>5</td>
<td>Challenge</td>
<td>1</td>
<td>DE</td>
<td>an</td>
<td>.256</td>
<td>C</td>
<td>1</td>
<td>M: bei TAN-Prozess=1, 3, 4 O: bei TAN-Prozess=2</td>
</tr>
<tr>
<td>6</td>
<td>Gültigkeitsdatum und -uhrzeit für Challenge</td>
<td>1</td>
<td>DEG</td>
<td></td>
<td></td>
<td>O</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>7</td>
<td>TAN-Listennummer</td>
<td>1</td>
<td>DE</td>
<td>an</td>
<td>..20</td>
<td>C</td>
<td>1</td>
<td>M: bei TAN-Prozess=1, 3, 4 und „Anzahl unterstützter aktiver TAN-Listen" nicht vorhanden O: sonst</td>
</tr>
<tr>
<td>8</td>
<td>TAN- Zusatzinformatio- nen</td>
<td>1</td>
<td>DE</td>
<td>an</td>
<td>..99</td>
<td>C</td>
<td>1</td>
<td>O: bei TAN-Prozess=1 N: bei TAN-Prozess=2, 3, 4</td>
</tr>
</table>


###### ◆ Belegungsrichtlinien


####### Auftrags-Hashwert

Es ist der in der Kundennachricht in HKTAN übermittelte Auftrags-Hashwert
unverändert einzustellen.


####### Challenge

Obwohl die Challenge bei Prozessvariante 2 im zweiten Schritt nicht zwin-
gend benötigt wird, sollte sie aus Integritätsgründen trotzdem übertragen
werden.


####### TAN-Listennummer

Ist in der BPD der Parameter „Anzahl unterstützter aktiver TAN-Listen" nicht
vorhanden, so muss das Institut dem Kunden hier mitteilen, welche TAN-
Liste er z. B. bei Einsatz eines indizierten TAN-Verfahrens verwenden soll.

<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th rowspan="2">Version: 3.0-FV</th>
<th rowspan="2">Kapitel: D</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Security - Sicherheitsverfahren PIN/TAN</td>
</tr>
<tr>
<td>Kapitel:<br>Abschnitt:</td>
<td>Archiv: Ältere Segmentversionen HKTAN für Zwei-Schritt-TAN-Einreichung</td>
<td>Stand: 23.02.2018</td>
<td>Seite: 153</td>
</tr>
</table>


###### ◆ Ausgewählte Beispiele für Rückmeldungscodes


<table>
<tr>
<td>Code</td>
<td>Beispiel für Rückmeldungstext</td>
</tr>
<tr>
<td>0010</td>
<td>Auftrag entgegengenommen</td>
</tr>
<tr>
<td>9210</td>
<td>Auftrag abgelehnt – Auftragsdaten inkonsistent. Eingereichter Auftrag gelöscht</td>
</tr>
<tr>
<td>9210</td>
<td>Auftrag abgelehnt - Zwei-Schritt-TAN inkonsistent. Eingereichter Auftrag gelöscht</td>
</tr>
<tr>
<td>9210</td>
<td>Auftrag abgelehnt – Kein eingereichter Auftrag gefunden</td>
</tr>
<tr>
<td>9210</td>
<td>Auftrag abgelehnt – Auftragsreferenz ist unbekannt</td>
</tr>
<tr>
<td>9330</td>
<td>TAN-Generator gesperrt. Führen Sie ggf. eine TAN-Gen.-Synchronisation durch</td>
</tr>
<tr>
<td>9360</td>
<td>Sperrung der TAN-Liste nach weiteren x Fehlversuchen</td>
</tr>
<tr>
<td>9380</td>
<td>Gewähltes Zwei-Schritt-TAN-Verfahren nicht zulässig</td>
</tr>
<tr>
<td>9931</td>
<td>Sperrung des Kontos nach x Fehlversuchen</td>
</tr>
<tr>
<td>9941</td>
<td>TAN ungültig</td>
</tr>
<tr>
<td>9951</td>
<td>Zeitüberschreitung im Zwei-Schritt-Verfahren – TAN ungültig</td>
</tr>
<tr>
<td>9953</td>
<td>Nur ein TAN-pflichtiger Auftrag pro Nachricht erlaubt</td>
</tr>
<tr>
<td>9954</td>
<td>Mehrfach-TANs nicht erlaubt</td>
</tr>
<tr>
<td>9955</td>
<td>Ein-Schritt-TAN-Verfahren nicht zugelassen</td>
</tr>
<tr>
<td>9956</td>
<td>Zeitversetzte Eingabe von Mehrfach-TANs nicht erlaubt</td>
</tr>
<tr>
<td>9991</td>
<td>TAN bereits verbraucht</td>
</tr>
</table>


###### c) Bankparameterdaten


###### Format


<table>
<tr>
<td>Name:</td>
<td>Zwei-Schritt-TAN-Einreichung, Parameter</td>
</tr>
<tr>
<td>Typ:</td>
<td>Segment</td>
</tr>
<tr>
<td>Segmentart:</td>
<td>Geschäftsvorfallparameter</td>
</tr>
<tr>
<td>Kennung:</td>
<td>HITANS</td>
</tr>
<tr>
<td>Bezugssegment:</td>
<td>HKVVB</td>
</tr>
<tr>
<td>Segmentversion:</td>
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
<td>Parameter Zwei- Schritt-TAN- Einreichung</td>
<td>1</td>
<td>DEG</td>
<td></td>
<td></td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
</table>


##### E.1.2 Geschäftsvorfall HKTAN in Segmentversion #2

Die Segmentversion #2 dieses Geschäftsvorfalls wird von Kreditinstituten verwen-
det, die das Zwei-Schritt-Verfahren inklusive der Erweiterungen zur Unterstützung
der Challenge-Klasse anbieten.

<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: D</td>
<td>Version: 3.0-FV</td>
<td>Financial Transaction Services (FinTS) Dokument: Security - Sicherheitsverfahren PIN/TAN</td>
</tr>
<tr>
<td>Seite: 154</td>
<td>Stand: 23.02.2018</td>
<td>Kapitel: Archiv: Ältere Segmentversionen<br>Abschnitt: HKTAN für Zwei-Schritt-TAN-Einreichung</td>
</tr>
</table>


<table>
<tr>
<td>Realisierung Bank:</td>
<td>verpflichtend in mindestens einer Segmentversion, falls Geschäftsvorfälle mit PIN/TAN-Absicherung im Zwei-Schritt-Verfahren angeboten werden</td>
</tr>
<tr>
<td>Realisierung Kunde:</td>
<td>optional</td>
</tr>
</table>


# a) Kundenauftrag

Format


<table>
<tr>
<td>Name:</td>
<td>Zwei-Schritt-TAN-Einreichung</td>
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
<td>HKTAN</td>
</tr>
<tr>
<td>Bezugssegment:</td>
<td>-</td>
</tr>
<tr>
<td>Segmentversion:</td>
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
<td>TAN-Prozess</td>
<td>1</td>
<td>DE</td>
<td>code</td>
<td>1</td>
<td>M</td>
<td>1</td>
<td>1, 2, 3, 4</td>
</tr>
<tr>
<td>3</td>
<td>Auftrags-Hashwert</td>
<td>1</td>
<td>DE</td>
<td>bin</td>
<td>.256</td>
<td>C</td>
<td>1</td>
<td>M: bei Auftrags- Hashwertverfahren&lt;&gt;0 und TAN-Prozess=1 N: sonst</td>
</tr>
<tr>
<td>4</td>
<td>Auftragsreferenz</td>
<td>1</td>
<td>DE</td>
<td>an</td>
<td>..35</td>
<td>C</td>
<td>1</td>
<td>M: bei TAN-Prozess=2, 3 O: TAN-Prozess=1, 4</td>
</tr>
<tr>
<td>5</td>
<td>TAN-Listennummer</td>
<td>1</td>
<td>DE</td>
<td>an</td>
<td>..20</td>
<td>C</td>
<td>1</td>
<td>M: bei TAN-Prozess=1, 3, 4 und „Anzahl unterstützter aktiver TAN-Listen" &gt; 1 und ,TAN-Listennummer erfor- derlich“=2 O: sonst</td>
</tr>
<tr>
<td>6</td>
<td>Weitere TAN folgt</td>
<td>1</td>
<td>DE</td>
<td>jn</td>
<td>1</td>
<td>C</td>
<td>1</td>
<td>M: bei TAN-Prozess=1, 2 N: bei TAN-Prozess=3, 4</td>
</tr>
<tr>
<td>7</td>
<td>Auftrag stornieren</td>
<td>1</td>
<td>DE</td>
<td>jn</td>
<td>1</td>
<td>C</td>
<td>1</td>
<td>O: bei TAN-Prozess=2 und „Auftragsstorno erlaubt“=J N: sonst</td>
</tr>
<tr>
<td>8</td>
<td>Challenge-Klasse</td>
<td>1</td>
<td>DE</td>
<td>num</td>
<td>..2</td>
<td>C</td>
<td>1</td>
<td>M: bei TAN-Prozess=1 und ,Challenge-Klasse erforder- lich“=J N: sonst</td>
</tr>
<tr>
<td>9</td>
<td>Parameter Challen- ge-Klasse</td>
<td>1</td>
<td>DEG</td>
<td></td>
<td></td>
<td>C</td>
<td>1</td>
<td>O: bei TAN-Prozess=1 und ,,Challenge-Klasse erforder- lich“=J N: sonst</td>
</tr>
</table>


# ◆ Belegungsrichtlinien


# Auftragsreferenz

Als Auftragsreferenz ist derjenige Wert einzustellen, der bei der Auftragsein-
reichung im Rahmen der Kreditinstitutsrückmeldung mitgeteilt wurde.

<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th rowspan="2">Version: 3.0-FV</th>
<th rowspan="2">Kapitel: D</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Security - Sicherheitsverfahren PIN/TAN</td>
</tr>
<tr>
<td>Kapitel:<br>Abschnitt:</td>
<td>HKTAN für Zwei-Schritt-TAN-Einreichung<br>Archiv: Ältere Segmentversionen</td>
<td>Stand: 23.02.2018</td>
<td>Seite: 155</td>
</tr>
</table>


## Parameter Challenge-Klasse

Die Parameter zur Challenge-Klasse dienen zur Übermittlung von Daten, die
bei Prozessvariante 1 im ersten Verfahrensschritt für die weitere Steuerung
benötigt werden. Ist das Datenelement ,,Challenge-Klasse“ belegt, so müs-
sen die Parameter die zur jeweiligen Challenge-Klasse passenden Informati-
onen, z. B. Empfänger-IBAN oder eine Wertpapierkennnummer enthalten.

Ist das Datenelement ,,Challenge-Betrag erforderlich“ in den BPD mit „J“ be-
legt, muss bei Vorhandensein einer Betragsinformation im Auftrag dieser
Challenge-Betragswert direkt anschließend an die regulären Challenge-
Klasse-Parameter als zusätzliche(r) Challenge-Klasse Parameter übermittelt
werden. Je nach konkretem Zwei-Schritt-Verfahren muss ggf. auch eine zu-
gehörige Challenge-Betragswährung als weiterer Parameter eingestellt wer-
den.

Hierbei gilt folgende Belegungsvorschrift:


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
<td>Challenge- Betragswert</td>
<td>DE</td>
<td>an</td>
<td>..999</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>2</td>
<td>Challenge- Betragswährung</td>
<td>DE</td>
<td>an</td>
<td>..999</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
</table>


Das alfanumerische DE "Challenge-Betragswert" muss analog der Belegung
des abgeleiteten Formats ,,wrt“ (vgl. [Formals], Kapitel B.4.2) befüllt werden.

Das alfanumerische DE "Challenge-Betragswährung" muss analog der Bele-
gung des abgeleiteten Formats ,,cur" (vgl. [Formals], Kapitel B.4.2) befüllt
werden. Falls in den Auftragsdaten keine oder keine eindeutige Währung
existiert, ist es mit "000" zu befüllen. Weitere Belegungsrichtlinien für Chal-
lenge-Betragswert und Challenge-Betragswährung hängen vom verwende-
ten konkreten Zwei-Schritt-Verfahren ab und sind der dortigen Spezifikation
zu entnehmen.


## TAN-Listennummer

Ist in der BPD als „Anzahl unterstützter aktiver TAN-Listen“ ein Wert > 1 an-
gegeben und ist der BPD-Wert für „TAN-Listennummer erforderlich“ = 2, so
muss der Kunde z. B. im Falle eines indizierten TAN-Verfahrens hier seine
für diesen Auftrag zu verwendende TAN-Liste angeben.


### b) Kreditinstitutsrückmeldung

Format


<table>
<tr>
<td>Name:</td>
<td>Zwei-Schritt-TAN-Einreichung Rückmeldung</td>
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
<td>HITAN</td>
</tr>
<tr>
<td>Bezugssegment:</td>
<td>HKTAN</td>
</tr>
<tr>
<td>Segmentversion:</td>
<td>2</td>
</tr>
<tr>
<td>Anzahl:</td>
<td>1</td>
</tr>
<tr>
<td>Sender:</td>
<td>Kreditinstitut</td>
</tr>
</table>


<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: D</td>
<td>Version: 3.0-FV</td>
<td>Financial Transaction Services (FinTS) Dokument: Security - Sicherheitsverfahren PIN/TAN</td>
</tr>
<tr>
<td>Seite: 156</td>
<td>Stand: 23.02.2018</td>
<td>Kapitel: Archiv: Ältere Segmentversionen<br>Abschnitt: HKTAN für Zwei-Schritt-TAN-Einreichung</td>
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
<td>TAN-Prozess</td>
<td>1</td>
<td>DE</td>
<td>code</td>
<td>1</td>
<td>M</td>
<td>1</td>
<td>1, 2, 3, 4</td>
</tr>
<tr>
<td>3</td>
<td>Auftrags-Hashwert</td>
<td>1</td>
<td>DE</td>
<td>bin</td>
<td>.256</td>
<td>C</td>
<td>1</td>
<td>M: bei Auftrags- Hashwertverfahren&lt;&gt;0 und TAN-Prozess=1, N: sonst</td>
</tr>
<tr>
<td>4</td>
<td>Auftragsreferenz</td>
<td>1</td>
<td>DE</td>
<td>an</td>
<td>..35</td>
<td>C</td>
<td>1</td>
<td>M: bei TAN-Prozess=2, 3, 4 O: bei TAN-Prozess=1</td>
</tr>
<tr>
<td>5</td>
<td>Challenge</td>
<td>2</td>
<td>DE</td>
<td>an</td>
<td>.999</td>
<td>C</td>
<td>1</td>
<td>M: bei TAN-Prozess=1, 3, 4 O: bei TAN-Prozess=2</td>
</tr>
<tr>
<td>6</td>
<td>Gültigkeitsdatum und -uhrzeit für Challenge</td>
<td>1</td>
<td>DEG</td>
<td></td>
<td></td>
<td>O</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>7</td>
<td>TAN-Listennummer</td>
<td>1</td>
<td>DE</td>
<td>an</td>
<td>..20</td>
<td>C</td>
<td>1</td>
<td>M: bei TAN-Prozess=1, 3, 4 und „Anzahl unterstützter aktiver TAN-Listen" nicht vorhanden O: sonst</td>
</tr>
<tr>
<td>8</td>
<td>BEN</td>
<td>1</td>
<td>DE</td>
<td>an</td>
<td>..99</td>
<td>C</td>
<td>1</td>
<td>O: bei TAN-Prozess=2 N: sonst</td>
</tr>
<tr>
<td>Nr.</td>
<td>Name</td>
<td>Ver- sion</td>
<td>Typ</td>
<td>For- mat</td>
<td>Län- ge</td>
<td>Sta- tus</td>
<td>An- zahl</td>
<td>Restriktionen</td>
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
<td>TAN-Prozess</td>
<td>1</td>
<td>DE</td>
<td>code</td>
<td>1</td>
<td>M</td>
<td>1</td>
<td>1, 2, 3, 4</td>
</tr>
<tr>
<td>3</td>
<td>Auftrags-Hashwert</td>
<td>1</td>
<td>DE</td>
<td>bin</td>
<td>.256</td>
<td>C</td>
<td>1</td>
<td>M: bei Auftrags- Hashwertverfahren&lt;&gt;0 und TAN-Prozess=1, N: sonst</td>
</tr>
<tr>
<td>4</td>
<td>Auftragsreferenz</td>
<td>1</td>
<td>DE</td>
<td>an</td>
<td>..35</td>
<td>C</td>
<td>1</td>
<td>M: bei TAN-Prozess=2, 3, 4 O: bei TAN-Prozess=1</td>
</tr>
<tr>
<td>5</td>
<td>Challenge</td>
<td>2</td>
<td>DE</td>
<td>an</td>
<td>..999</td>
<td>C</td>
<td>1</td>
<td>M: bei TAN-Prozess=1, 3, 4 O: bei TAN-Prozess=2</td>
</tr>
<tr>
<td>6</td>
<td>Gültigkeitsdatum und -uhrzeit für Challenge</td>
<td>1</td>
<td>DEG</td>
<td></td>
<td></td>
<td>O</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>7</td>
<td>TAN-Listennummer</td>
<td>1</td>
<td>DE</td>
<td>an</td>
<td>..20</td>
<td>C</td>
<td>1</td>
<td>M: bei TAN-Prozess=1, 3, 4 und „Anzahl unterstützter aktiver TAN-Listen" nicht vorhanden<br>O: sonst</td>
</tr>
<tr>
<td>8</td>
<td>BEN</td>
<td>1</td>
<td>DE</td>
<td>an</td>
<td>..99</td>
<td>C</td>
<td>1</td>
<td>O: bei TAN-Prozess=2 N: sonst</td>
</tr>
</table>


#### ◆ Belegungsrichtlinien


##### Auftrags-Hashwert

Es ist der in der Kundennachricht in HKTAN übermittelte Auftrags-Hashwert
unverändert einzustellen.

<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th rowspan="2">Version: 3.0-FV</th>
<th rowspan="2">Kapitel: D</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Security - Sicherheitsverfahren PIN/TAN</td>
</tr>
<tr>
<td>Kapitel:<br>Abschnitt:</td>
<td>Archiv: Ältere Segmentversionen HKTAN für Zwei-Schritt-TAN-Einreichung</td>
<td>Stand: 23.02.2018</td>
<td>Seite: 157</td>
</tr>
</table>


# Auftragsreferenz

Bei TAN-Prozess=2, 3 und 4 muss die Auftragsreferenz vom Institut immer
eingestellt werden. Bei TAN-Prozess=1 muss die Auftragsreferenz einge-
stellt werden, wenn sie zuvor im Segment HKTAN vom Kunden gesendet
wurde.


# Challenge

Obwohl die Challenge bei Prozessvariante 2 im zweiten Schritt nicht zwin-
gend benötigt wird, sollte sie aus Integritätsgründen trotzdem übertragen
werden.


![](figures/157.1)


Das Kundenprodukt muss den Inhalt der empfangenen Challenge
dem Kunden unverändert anzeigen.

Erläuterung: Die Challenge kann institutsindividuell aufgebaut wer-
den (z. B. 1 oder 2 Eingabefelder für den chipTAN-Leser).


## TAN-Listennummer

Ist in der BPD der Parameter ,,Anzahl unterstützter aktiver TAN-Listen“ nicht
vorhanden, so muss das Institut dem Kunden hier mitteilen, welche TAN-
Liste er z. B. bei Einsatz eines indizierten TAN-Verfahrens verwenden soll.


## ◆ Ausgewählte Beispiele für Rückmeldungscodes


<table>
<tr>
<td>Code</td>
<td>Beispiel für Rückmeldungstext</td>
</tr>
<tr>
<td>0010</td>
<td>Auftrag entgegengenommen</td>
</tr>
<tr>
<td>9210</td>
<td>Auftrag abgelehnt – Auftragsdaten inkonsistent. Eingereichter Auftrag gelöscht</td>
</tr>
<tr>
<td>9210</td>
<td>Auftrag abgelehnt – Zwei-Schritt-TAN inkonsistent. Eingereichter Auftrag gelöscht</td>
</tr>
<tr>
<td>9210</td>
<td>Auftrag abgelehnt – Kein eingereichter Auftrag gefunden</td>
</tr>
<tr>
<td>9210</td>
<td>Auftrag abgelehnt – Auftragsreferenz ist unbekannt</td>
</tr>
<tr>
<td>9330</td>
<td>chipTAN-Leser gesperrt. Führen Sie ggf. eine chipTAN-Synchronisation durch</td>
</tr>
<tr>
<td>9360</td>
<td>Sperrung der TAN-Liste nach weiteren x Fehlversuchen</td>
</tr>
<tr>
<td>9380</td>
<td>Gewähltes Zwei-Schritt-TAN-Verfahren nicht zulässig</td>
</tr>
<tr>
<td>9931</td>
<td>Sperrung des Kontos nach x Fehlversuchen</td>
</tr>
<tr>
<td>9941</td>
<td>TAN ungültig</td>
</tr>
<tr>
<td>9951</td>
<td>Zeitüberschreitung im Zwei-Schritt-Verfahren – TAN ungültig</td>
</tr>
<tr>
<td>9953</td>
<td>Nur ein TAN-pflichtiger Auftrag pro Nachricht erlaubt</td>
</tr>
<tr>
<td>9954</td>
<td>Mehrfach-TANs nicht erlaubt</td>
</tr>
<tr>
<td>9955</td>
<td>Ein-Schritt-TAN-Verfahren nicht zugelassen</td>
</tr>
<tr>
<td>9956</td>
<td>Zeitversetzte Eingabe von Mehrfach-TANs nicht erlaubt</td>
</tr>
<tr>
<td>9991</td>
<td>TAN bereits verbraucht</td>
</tr>
</table>


## c) Bankparameterdaten


## Format


<table>
<tr>
<td>Name:</td>
<td>Zwei-Schritt-TAN-Einreichung, Parameter</td>
</tr>
<tr>
<td>Typ:</td>
<td>Segment</td>
</tr>
<tr>
<td>Segmentart:</td>
<td>Geschäftsvorfallparameter</td>
</tr>
<tr>
<td>Kennung:</td>
<td>HITANS</td>
</tr>
<tr>
<td>Bezugssegment:</td>
<td>HKVVB</td>
</tr>
<tr>
<td>Segmentversion:</td>
<td>2</td>
</tr>
<tr>
<td>Sender:</td>
<td>Kreditinstitut</td>
</tr>
</table>


<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: D</td>
<td>Version: 3.0-FV</td>
<td>Financial Transaction Services (FinTS) Dokument: Security - Sicherheitsverfahren PIN/TAN</td>
</tr>
<tr>
<td>Seite: 158</td>
<td>Stand: 23.02.2018</td>
<td>Kapitel: Archiv: Ältere Segmentversionen<br>Abschnitt: HKTAN für Zwei-Schritt-TAN-Einreichung</td>
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
<tr>
<td>5</td>
<td>Parameter Zwei- Schritt-TAN- Einreichung</td>
<td>2</td>
<td>DEG</td>
<td></td>
<td></td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
</table>


## ◆ Belegungsrichtlinien

Auftrags-Hashwertverfahren (Parameter Zwei-Schritt-TAN-Einreichung)
Bei Verwendung von TAN-Prozess=1.


### E.1.3 Geschäftsvorfall HKTAN in Segmentversion #3

Die Segmentversion #3 dieses Geschäftsvorfalls wird von Kreditinstituten verwen-
det, die das Zwei-Schritt-Verfahren in Kombination mit HHD V1.3 und/oder mobi-
leTAN anbieten. Mit dieser Version können aber auch alle anderen PIN/TAN Zwei-
Schritt-Verfahren unterstützt werden; wahlweise können Kreditinstitute zusätzlich
auch andere Segmentversionen anbieten.

Realisierung Bank:
verpflichtend in mindestens einer Segmentversion, falls
Geschäftsvorfälle mit PIN/TAN-Absicherung im Zwei-
Schritt-Verfahren angeboten werden

Realisierung Kunde:
optional


#### a) Kundenauftrag


#### Format


<table>
<tr>
<td>Name:</td>
<td>Zwei-Schritt-TAN-Einreichung</td>
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
<td>HKTAN</td>
</tr>
<tr>
<td>Bezugssegment:</td>
<td>-</td>
</tr>
<tr>
<td>Segmentversion:</td>
<td>3</td>
</tr>
<tr>
<td>Sender:</td>
<td>Kunde</td>
</tr>
</table>


<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th>Version:</th>
<th rowspan="2">Kapitel: D</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Security - Sicherheitsverfahren PIN/TAN</td>
<td>3.0-FV</td>
</tr>
<tr>
<td>Kapitel:</td>
<td>Archiv: Ältere Segmentversionen</td>
<td>Stand:</td>
<td>Seite:</td>
</tr>
<tr>
<td>Abschnitt:</td>
<td>HKTAN für Zwei-Schritt-TAN-Einreichung</td>
<td>23.02.2018</td>
<td>159</td>
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
<td>TAN-Prozess</td>
<td>1</td>
<td>DE</td>
<td>code</td>
<td>1</td>
<td>M</td>
<td>1</td>
<td>1, 2, 3, 4</td>
</tr>
<tr>
<td>3</td>
<td>Auftrags-Hashwert</td>
<td>1</td>
<td>DE</td>
<td>bin</td>
<td>.256</td>
<td>C</td>
<td>1</td>
<td>M: bei Auftrags- Hashwertverfahren&lt;&gt;0 und TAN-Prozess=1 N: sonst</td>
</tr>
<tr>
<td>4</td>
<td>Auftragsreferenz</td>
<td>1</td>
<td>DE</td>
<td>an</td>
<td>..35</td>
<td>C</td>
<td>1</td>
<td>M: bei TAN-Prozess=2, 3 O: TAN-Prozess=1, 4</td>
</tr>
<tr>
<td>5</td>
<td>TAN-Listennummer</td>
<td>1</td>
<td>DE</td>
<td>an</td>
<td>..20</td>
<td>C</td>
<td>1</td>
<td>M: bei TAN-Prozess=1, 3, 4 und „Anzahl unterstützter aktiver TAN-Listen“ &gt; 1 und ,TAN-Listennummer erfor- derlich“=2<br>O: sonst</td>
</tr>
<tr>
<td>6</td>
<td>Weitere TAN folgt</td>
<td>1</td>
<td>DE</td>
<td>jn</td>
<td>1</td>
<td>C</td>
<td>1</td>
<td>M: bei TAN-Prozess=1, 2 N: bei TAN-Prozess=3, 4</td>
</tr>
<tr>
<td>7</td>
<td>Auftrag stornieren</td>
<td>1</td>
<td>DE</td>
<td>jn</td>
<td>1</td>
<td>C</td>
<td>1</td>
<td>O: bei TAN-Prozess=2 und „Auftragsstorno erlaubt“=J N: sonst</td>
</tr>
<tr>
<td>8</td>
<td>Challenge-Klasse</td>
<td>1</td>
<td>DE</td>
<td>num</td>
<td>..2</td>
<td>C</td>
<td>1</td>
<td>M: bei TAN-Prozess=1 und „Challenge-Klasse erforder- lich“=J N: sonst</td>
</tr>
<tr>
<td>9</td>
<td>Parameter Challen- ge-Klasse</td>
<td>1</td>
<td>DEG</td>
<td></td>
<td></td>
<td>C</td>
<td>1</td>
<td>O: bei TAN-Prozess=1 und ,Challenge-Klasse erforder- lich“=J N: sonst</td>
</tr>
<tr>
<td>10</td>
<td>Bezeichnung des TAN-Mediums</td>
<td>1</td>
<td>DE</td>
<td>an</td>
<td>..32</td>
<td>C</td>
<td>1</td>
<td>M: bei TAN-Prozess=1, 3, 4 und „Anzahl unterstützter aktiver TAN-Medien" &gt; 1 und ,,Bezeichnung des TAN-Mediums erforder- lich“=2 O: sonst</td>
</tr>
</table>


#### ◆ Belegungsrichtlinien


##### Auftragsreferenz

Als Auftragsreferenz ist derjenige Wert einzustellen, der bei der Auftragsein-
reichung im Rahmen der Kreditinstitutsrückmeldung mitgeteilt wurde.


##### Parameter Challenge-Klasse

Die Parameter zur Challenge-Klasse dienen zur Übermittlung von Daten, die
bei Prozessvariante 1 im ersten Verfahrensschritt für die weitere Steuerung
benötigt werden. Ist das Datenelement ,,Challenge-Klasse“ belegt, so muss
im ersten Parameter P1 die Segmentkennung des jeweiligen Geschäftsvor-
falls eingestellt werden. Die weiteren Parameter müssen die zur jeweiligen
Challenge-Klasse passenden Informationen, z. B. Empfänger-IBAN oder ei-
ne Wertpapierkennnummer enthalten.

<!-- PageBreak -->


<table>
<tr>
<th>Kapitel: D</th>
<th>Version: 3.0-FV</th>
<th>Financial Transaction Services (FinTS) Dokument: Security - Sicherheitsverfahren PIN/TAN</th>
</tr>
<tr>
<td>Seite:<br>160</td>
<td>Stand: 23.02.2018</td>
<td>Kapitel: Archiv: Ältere Segmentversionen<br>Abschnitt: HKTAN für Zwei-Schritt-TAN-Einreichung</td>
</tr>
</table>


Ist das Datenelement ,,Challenge-Betrag erforderlich" in den BPD mit „J“ be-
legt, muss bei Vorhandensein einer Betragsinformation im Auftrag dieser
Challenge-Betragswert direkt anschließend an die regulären Challenge-
Klasse-Parameter als zusätzliche(r) Challenge-Klasse Parameter übermittelt
werden. Je nach konkretem Zwei-Schritt-Verfahren muss ggf. auch eine zu-
gehörige Challenge-Betragswährung als weiterer Parameter eingestellt wer-
den.

Hierbei gilt folgende Belegungsvorschrift:


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
<td>Challenge- Betragswert</td>
<td>DE</td>
<td>an</td>
<td>..999</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>2</td>
<td>Challenge- Betragswährung</td>
<td>DE</td>
<td>an</td>
<td>..999</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
</table>


Das alfanumerische DE "Challenge-Betragswert" muss analog der Belegung
des abgeleiteten Formats ,wrt“ (vgl. [Formals], Kapitel B.4.2) befüllt werden.

Das alfanumerische DE "Challenge-Betragswährung" muss analog der Bele-
gung des abgeleiteten Formats ,,cur" (vgl. [Formals], Kapitel B.4.2) befüllt
werden. Falls in den Auftragsdaten keine oder keine eindeutige Währung
existiert, ist es mit "000" zu befüllen.

Weitere Belegungsrichtlinien für Challenge-Betragswert und Challenge-
Betragswährung hängen vom verwendeten konkreten Zwei-Schritt-Verfahren
ab und sind der dortigen Spezifikation zu entnehmen.


### TAN-Listennummer

Ist in der BPD als „Anzahl unterstützter aktiver TAN-Listen“ ein Wert > 1 an-
gegeben und ist der BPD-Wert für „TAN-Listennummer erforderlich“ = 2, so
muss der Kunde z. B. im Falle eines indizierten TAN-Verfahrens hier seine
für diesen Auftrag zu verwendende TAN-Liste angeben.


### Bezeichnung des TAN-Mediums

Ist in der BPD als "Anzahl unterstützter aktiver TAN-Medien“ ein Wert > 1
angegeben und ist der BPD-Wert für „Bezeichnung des TAN-Mediums erfor-
derlich" = 2, so muss der Kunde z. B. im Falle des mobileTAN-Verfahrens
hier die Bezeichnung seines für diesen Auftrag zu verwendenden TAN-
Mediums angeben.

<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th rowspan="2">Version: 3.0-FV</th>
<th rowspan="2">Kapitel: D</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Security - Sicherheitsverfahren PIN/TAN</td>
</tr>
<tr>
<td>Kapitel:<br>Abschnitt:</td>
<td>Archiv: Ältere Segmentversionen<br>HKTAN für Zwei-Schritt-TAN-Einreichung</td>
<td>Stand: 23.02.2018</td>
<td>Seite: 161</td>
</tr>
</table>


#### b) Kreditinstitutsrückmeldung

Format


<table>
<tr>
<td>Name:</td>
<td>Zwei-Schritt-TAN-Einreichung Rückmeldung</td>
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
<td>HITAN</td>
</tr>
<tr>
<td>Bezugssegment:</td>
<td>HKTAN</td>
</tr>
<tr>
<td>Segmentversion:</td>
<td>3</td>
</tr>
<tr>
<td>Anzahl:</td>
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
<th>1Name</th>
<th>Ver- sion</th>
<th>Typ</th>
<th>For- mat</th>
<th>Län- ge</th>
<th>Sta- tus</th>
<th>An- zahl</th>
<th>1Restriktionen</th>
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
<td>TAN-Prozess</td>
<td>1</td>
<td>DE</td>
<td>code</td>
<td>1</td>
<td>M</td>
<td>1</td>
<td>1, 2, 3, 4</td>
</tr>
<tr>
<td>3</td>
<td>Auftrags-Hashwert</td>
<td>1</td>
<td>DE</td>
<td>bin</td>
<td>.256</td>
<td>C</td>
<td>1</td>
<td>M: bei Auftrags- Hashwertverfahren&lt;&gt;0 und TAN-Prozess=1, N: sonst</td>
</tr>
<tr>
<td>4</td>
<td>Auftragsreferenz</td>
<td>1</td>
<td>DE</td>
<td>an</td>
<td>..35</td>
<td>C</td>
<td>1</td>
<td>M: bei TAN-Prozess=2, 3, 4 O: bei TAN-Prozess=1</td>
</tr>
<tr>
<td>5</td>
<td>Challenge</td>
<td>2</td>
<td>DE</td>
<td>an</td>
<td>..999</td>
<td>C</td>
<td>1</td>
<td>M: bei TAN-Prozess=1, 3, 4 O: bei TAN-Prozess=2</td>
</tr>
<tr>
<td>6</td>
<td>Gültigkeitsdatum und -uhrzeit für Challenge</td>
<td>1</td>
<td>DEG</td>
<td></td>
<td></td>
<td>O</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>7</td>
<td>TAN-Listennummer</td>
<td>1</td>
<td>DE</td>
<td>an</td>
<td>..20</td>
<td>C</td>
<td>1</td>
<td>M: bei TAN-Prozess=1, 3, 4 und „Anzahl unterstützter aktiver TAN-Listen" nicht vorhanden O: sonst</td>
</tr>
<tr>
<td>8</td>
<td>BEN</td>
<td>1</td>
<td>DE</td>
<td>an</td>
<td>..99</td>
<td>C</td>
<td>1</td>
<td>O: bei TAN-Prozess=2 N: sonst</td>
</tr>
<tr>
<td>9</td>
<td>Bezeichnung des TAN-Mediums</td>
<td>1</td>
<td>DE</td>
<td>an</td>
<td>..32</td>
<td>C</td>
<td>1</td>
<td>M: bei TAN-Prozess=1, 3, 4 und „Anzahl unterstützter aktiver TAN-Medien" nicht vorhanden O: sonst</td>
</tr>
</table>


<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: D</td>
<td>Version: 3.0-FV</td>
<td>Financial Transaction Services (FinTS) Dokument: Security - Sicherheitsverfahren PIN/TAN</td>
</tr>
<tr>
<td>Seite: 162</td>
<td>Stand: 23.02.2018</td>
<td>Kapitel: Archiv: Ältere Segmentversionen<br>Abschnitt: HKTAN für Zwei-Schritt-TAN-Einreichung</td>
</tr>
</table>


## ◆ Belegungsrichtlinien

Auftrags-Hashwert

Es ist der in der Kundennachricht in HKTAN übermittelte Auftrags-Hashwert
unverändert einzustellen.


### Auftragsreferenz

Bei TAN-Prozess=2, 3 und 4 muss die Auftragsreferenz vom Institut immer
eingestellt werden. Bei TAN-Prozess=1 muss die Auftragsreferenz einge-
stellt werden, wenn sie zuvor im Segment HKTAN vom Kunden gesendet
wurde.

Challenge

Obwohl die Challenge bei Prozessvariante 2 im zweiten Schritt nicht zwin-
gend benötigt wird, sollte sie aus Integritätsgründen trotzdem übertragen
werden.


![](figures/162.1)


Das Kundenprodukt muss den Inhalt der empfangenen Challenge
dem Kunden unverändert anzeigen.

Erläuterung: Die Challenge kann institutsindividuell aufgebaut wer-
den (z. B. 1 oder 2 Eingabefelder für den chipTAN-Leser).


#### TAN-Listennummer

Ist in der BPD der Parameter ,,Anzahl unterstützter aktiver TAN-Listen“ nicht
vorhanden, so muss das Institut dem Kunden hier mitteilen, welche TAN-
Liste er z. B. bei Einsatz eines indizierten TAN-Verfahrens verwenden soll.


### Bezeichnung des TAN-Mediums

Ist in der BPD der Parameter „Anzahl unterstützter aktiver TAN-Medien“
nicht vorhanden, so muss das Institut dem Kunden hier mitteilen, welches
TAN-Medium er z. B. beim mobileTAN-Verfahren verwenden soll.


## ◆ Ausgewählte Beispiele für Rückmeldungscodes


<table>
<tr>
<td>Code</td>
<td>Beispiel für Rückmeldungstext</td>
</tr>
<tr>
<td>0010</td>
<td>Auftrag entgegengenommen</td>
</tr>
<tr>
<td>9210</td>
<td>Auftrag abgelehnt – Auftragsdaten inkonsistent. Eingereichter Auftrag gelöscht</td>
</tr>
<tr>
<td>9210</td>
<td>Auftrag abgelehnt – Zwei-Schritt-TAN inkonsistent. Eingereichter Auftrag gelöscht</td>
</tr>
<tr>
<td>9210</td>
<td>Auftrag abgelehnt – Kein eingereichter Auftrag gefunden</td>
</tr>
<tr>
<td>9210</td>
<td>Auftrag abgelehnt – Auftragsreferenz ist unbekannt</td>
</tr>
<tr>
<td>9330</td>
<td>chipTAN-Leser gesperrt. Führen Sie ggf. eine chipTAN-Synchronisation durch</td>
</tr>
<tr>
<td>9360</td>
<td>Sperrung der TAN-Liste nach weiteren x Fehlversuchen</td>
</tr>
<tr>
<td>9380</td>
<td>Gewähltes Zwei-Schritt-TAN-Verfahren nicht zulässig</td>
</tr>
<tr>
<td>9931</td>
<td>Sperrung des Kontos nach x Fehlversuchen</td>
</tr>
<tr>
<td>9941</td>
<td>TAN ungültig</td>
</tr>
<tr>
<td>9951</td>
<td>Zeitüberschreitung im Zwei-Schritt-Verfahren – TAN ungültig</td>
</tr>
<tr>
<td>9953</td>
<td>Nur ein TAN-pflichtiger Auftrag pro Nachricht erlaubt</td>
</tr>
<tr>
<td>9954</td>
<td>Mehrfach-TANs nicht erlaubt</td>
</tr>
<tr>
<td>9955</td>
<td>Ein-Schritt-TAN-Verfahren nicht zugelassen</td>
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
<td>Dokument:</td>
<td>Security - Sicherheitsverfahren PIN/TAN</td>
</tr>
<tr>
<td>Kapitel:<br>Abschnitt:</td>
<td>HKTAN für Zwei-Schritt-TAN-Einreichung<br>Archiv: Ältere Segmentversionen</td>
<td>Stand: 23.02.2018</td>
<td>Seite: 163</td>
</tr>
</table>


<table>
<tr>
<td>Code</td>
<td>Beispiel für Rückmeldungstext</td>
</tr>
<tr>
<td>9956</td>
<td>Zeitversetzte Eingabe von Mehrfach-TANs nicht erlaubt</td>
</tr>
<tr>
<td>9991</td>
<td>TAN bereits verbraucht</td>
</tr>
</table>


c)
Bankparameterdaten


### Format


<table>
<tr>
<td>Name:</td>
<td>Zwei-Schritt-TAN-Einreichung, Parameter</td>
</tr>
<tr>
<td>Typ:</td>
<td>Segment</td>
</tr>
<tr>
<td>Segmentart:</td>
<td>Geschäftsvorfallparameter</td>
</tr>
<tr>
<td>Kennung:</td>
<td>HITANS</td>
</tr>
<tr>
<td>Bezugssegment:</td>
<td>HKVVB</td>
</tr>
<tr>
<td>Segmentversion:</td>
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
<td>Parameter Zwei- Schritt-TAN- Einreichung</td>
<td>3</td>
<td>DEG</td>
<td></td>
<td></td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
</table>


## ◆ Belegungsrichtlinien

Auftrags-Hashwertverfahren (Parameter Zwei-Schritt-TAN-Einreichung)
Bei Verwendung von TAN-Prozess=1.

<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: D</td>
<td>Version: 3.0-FV</td>
<td>Financial Transaction Services (FinTS) Dokument: Security - Sicherheitsverfahren PIN/TAN</td>
</tr>
<tr>
<td>Seite:<br>164</td>
<td>Stand: 23.02.2018</td>
<td>Kapitel: Archiv: Ältere Segmentversionen<br>Abschnitt: HKTAN für Zwei-Schritt-TAN-Einreichung</td>
</tr>
</table>


### E.1.4 Geschäftsvorfall HKTAN in Segmentversion #4

Ab der Segmentversion #4 dieses Geschäftsvorfalls ist das chipTAN-Verfahren mit
unidirektionaler Kopplung unterstützt. Mit dieser Version können aber auch alle an-
deren PIN/TAN Zwei-Schritt-Verfahren unterstützt werden; wahlweise können Kre-
ditinstitute zusätzlich auch andere Segmentversionen von HKTAN anbieten.

Realisierung Bank: verpflichtend in mindestens einer Segmentversion, falls
Geschäftsvorfälle mit PIN/TAN-Absicherung im Zwei-Schritt-
Verfahren angeboten werden.

Realisierung Kunde: optional


#### a) Kundenauftrag


##### Format


<table>
<tr>
<td>Name:</td>
<td>Zwei-Schritt-TAN-Einreichung</td>
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
<td>HKTAN</td>
</tr>
<tr>
<td>Bezugssegment:</td>
<td>-</td>
</tr>
<tr>
<td>Segmentversion:</td>
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
<td>TAN-Prozess</td>
<td>1</td>
<td>DE</td>
<td>code</td>
<td>1</td>
<td>M</td>
<td>1</td>
<td>1, 2, 3, 4</td>
</tr>
<tr>
<td>3</td>
<td>Auftrags-Hashwert</td>
<td>1</td>
<td>DE</td>
<td>bin</td>
<td>.256</td>
<td>C</td>
<td>1</td>
<td>M: bei Auftrags- Hashwertverfahren&lt;&gt;0 und TAN-Prozess=1 N: sonst</td>
</tr>
<tr>
<td>4</td>
<td>Auftragsreferenz</td>
<td>1</td>
<td>DE</td>
<td>an</td>
<td>..35</td>
<td>C</td>
<td>1</td>
<td>M: bei TAN-Prozess=2, 3 O: TAN-Prozess=1, 4</td>
</tr>
<tr>
<td>5</td>
<td>TAN-Listennummer</td>
<td>1</td>
<td>DE</td>
<td>an</td>
<td>..20</td>
<td>C</td>
<td>1</td>
<td>M: bei TAN-Prozess=1, 3, 4 und „Anzahl unterstützter aktiver TAN-Listen" &gt; 1 und „TAN-Listennummer erfor- derlich"=2 O: sonst</td>
</tr>
<tr>
<td>6</td>
<td>Weitere TAN folgt</td>
<td>1</td>
<td>DE</td>
<td>jn</td>
<td>1</td>
<td>C</td>
<td>1</td>
<td>M: bei TAN-Prozess=1, 2 N: bei TAN-Prozess=3, 4</td>
</tr>
<tr>
<td>7</td>
<td>Auftrag stornieren</td>
<td>1</td>
<td>DE</td>
<td>jn</td>
<td>1</td>
<td>C</td>
<td>1</td>
<td>O: bei TAN-Prozess=2 und ,,Auftragsstorno erlaubt“=J N: sonst</td>
</tr>
<tr>
<td>8</td>
<td>SMS- Abbuchungskonto</td>
<td>1</td>
<td>DEG</td>
<td>kti</td>
<td>#</td>
<td>C</td>
<td>1</td>
<td>M: bei TAN-Prozess=1, 3, 4 und „SMS-<br>Abbuchungskonto erforder- lich“=“J“ N: sonst</td>
</tr>
<tr>
<td>9</td>
<td>Challenge-Klasse</td>
<td>1</td>
<td>DE</td>
<td>num</td>
<td>..2</td>
<td>C</td>
<td>1</td>
<td>M: bei TAN-Prozess=1 und ,Challenge-Klasse erforder- lich“=J N: sonst</td>
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
<td>Dokument:</td>
<td>Security - Sicherheitsverfahren PIN/TAN</td>
</tr>
<tr>
<td>Kapitel:<br>Abschnitt:</td>
<td>Archiv: Ältere Segmentversionen HKTAN für Zwei-Schritt-TAN-Einreichung</td>
<td>Stand: 23.02.2018</td>
<td>Seite: 165</td>
</tr>
</table>


<table>
<tr>
<td>10</td>
<td>Parameter Challen- ge-Klasse</td>
<td>1</td>
<td>DEG</td>
<td></td>
<td></td>
<td>C</td>
<td>1</td>
<td>O: bei TAN-Prozess=1 und ,,Challenge-Klasse erforder- lich“=J N: sonst</td>
</tr>
<tr>
<td>11</td>
<td>Bezeichnung des TAN-Mediums</td>
<td>1</td>
<td>DE</td>
<td>an</td>
<td>..32</td>
<td>C</td>
<td>1</td>
<td>M: bei TAN-Prozess=1, 3, 4 und „Anzahl unterstützter aktiver TAN-Medien“ &gt; 1 und ,,Bezeichnung des TAN-Mediums erforder- lich“=2 O: sonst</td>
</tr>
</table>


#### ◆ Belegungsrichtlinien


##### Auftragsreferenz

Als Auftragsreferenz ist derjenige Wert einzustellen, der bei der Auftragsein-
reichung im Rahmen der Kreditinstitutsrückmeldung mitgeteilt wurde.


##### Parameter Challenge-Klasse

Die Parameter zur Challenge-Klasse dienen zur Übermittlung von Daten, die
bei Prozessvariante 1 im ersten Verfahrensschritt für die weitere Steuerung
benötigt werden. Ist das Datenelement ,,Challenge-Klasse“ belegt, so muss
im ersten Parameter P1 die Segmentkennung des jeweiligen Geschäftsvor-
falls eingestellt werden. Die weiteren Parameter müssen die zur jeweiligen
Challenge-Klasse passenden Informationen, z. B. Empfänger-IBAN oder ei-
ne Wertpapierkennnummer enthalten.

Ist das Datenelement ,,Challenge-Betrag erforderlich“ in den BPD mit „J“ be-
legt, muss bei Vorhandensein einer Betragsinformation im Auftrag dieser
Challenge-Betragswert direkt anschließend an die regulären Challenge-
Klasse-Parameter als zusätzliche(r) Challenge-Klasse Parameter übermittelt
werden. Je nach konkretem Zwei-Schritt-Verfahren muss ggf. auch eine zu-
gehörige Challenge-Betragswährung als weiterer Parameter eingestellt wer-
den.

Hierbei gilt folgende Belegungsvorschrift:


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
<td>Challenge- Betragswert</td>
<td>DE</td>
<td>an</td>
<td>.999</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>2</td>
<td>Challenge- Betragswährung</td>
<td>DE</td>
<td>an</td>
<td>..999</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
</table>


Das alfanumerische DE "Challenge-Betragswert" muss analog der Belegung
des abgeleiteten Formats ,,wrt“ (vgl. [Formals], Kapitel B.4.2) befüllt werden.

Das alfanumerische DE "Challenge-Betragswährung" muss analog der Bele-
gung des abgeleiteten Formats ,,cur" (vgl. [Formals], Kapitel B.4.2) befüllt
werden. Falls in den Auftragsdaten keine oder keine eindeutige Währung
existiert, ist es mit "000" zu befüllen.

Weitere Belegungsrichtlinien für Challenge-Betragswert und Challenge-
Betragswährung hängen vom verwendeten konkreten Zwei-Schritt-Verfahren
ab und sind der dortigen Spezifikation zu entnehmen.

<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: D</td>
<td>Version: 3.0-FV</td>
<td>Financial Transaction Services (FinTS) Dokument: Security - Sicherheitsverfahren PIN/TAN</td>
</tr>
<tr>
<td>Seite:<br>166</td>
<td>Stand: 23.02.2018</td>
<td>Kapitel: Archiv: Ältere Segmentversionen<br>Abschnitt: HKTAN für Zwei-Schritt-TAN-Einreichung</td>
</tr>
</table>


##### TAN-Listennummer

Ist in der BPD als ,,Anzahl unterstützter aktiver TAN-Listen“ ein Wert > 1 an-
gegeben und ist der BPD-Wert für „TAN-Listennummer erforderlich“ = 2, so
muss der Kunde z. B. im Falle eines indizierten TAN-Verfahrens hier seine
für diesen Auftrag zu verwendende TAN-Liste angeben.


##### Bezeichnung des TAN-Mediums

Ist in der BPD als ,,Anzahl unterstützter aktiver TAN-Medien“ ein Wert > 1
angegeben und ist der BPD-Wert für „Bezeichnung des TAN-Mediums erfor-
derlich" = 2, so muss der Kunde z. B. im Falle des mobileTAN-Verfahrens
hier die Bezeichnung seines für diesen Auftrag zu verwendenden TAN-
Mediums angeben.


##### SMS-Abbuchungskonto

Ist in der BPD als ,,SMS-Abbuchungskonto erforderlich" mit ,,J" belegt, so
muss der Kunde z. B. im Falle des mobileTAN-Verfahrens hier das für die-
sen Auftrag zu belastende SMS-Abbuchungskonto einstellen. Dieses kann
unabhängig von der Kontoverbindung des Dialogführers gewählt werden.

<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th rowspan="2">Version: 3.0-FV</th>
<th rowspan="2">Kapitel: D</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Security - Sicherheitsverfahren PIN/TAN</td>
</tr>
<tr>
<td>Kapitel:<br>Abschnitt:</td>
<td>Archiv: Ältere Segmentversionen<br>HKTAN für Zwei-Schritt-TAN-Einreichung</td>
<td>Stand: 23.02.2018</td>
<td>Seite: 167</td>
</tr>
</table>


###### b) Kreditinstitutsrückmeldung

Format


<table>
<tr>
<td>Name:</td>
<td>Zwei-Schritt-TAN-Einreichung Rückmeldung</td>
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
<td>HITAN</td>
</tr>
<tr>
<td>Bezugssegment:</td>
<td>HKTAN</td>
</tr>
<tr>
<td>Segmentversion:</td>
<td>4</td>
</tr>
<tr>
<td>Anzahl:</td>
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
<td>TAN-Prozess</td>
<td>1</td>
<td>DE</td>
<td>code</td>
<td>1</td>
<td>M</td>
<td>1</td>
<td>1, 2, 3, 4</td>
</tr>
<tr>
<td>3</td>
<td>Auftrags-Hashwert</td>
<td>1</td>
<td>DE</td>
<td>bin</td>
<td>.256</td>
<td>C</td>
<td>1</td>
<td>M: bei Auftrags- Hashwertverfahren&lt;&gt;0 und TAN-Prozess=1, N: sonst</td>
</tr>
<tr>
<td>4</td>
<td>Auftragsreferenz</td>
<td>1</td>
<td>DE</td>
<td>an</td>
<td>..35</td>
<td>C</td>
<td>1</td>
<td>M: bei TAN-Prozess=2, 3, 4 O: bei TAN-Prozess=1</td>
</tr>
<tr>
<td>5</td>
<td>Challenge</td>
<td>3</td>
<td>DE</td>
<td>an</td>
<td>.204 8</td>
<td>C</td>
<td>1</td>
<td>M: bei TAN-Prozess=1, 3, 4 O: bei TAN-Prozess=2</td>
</tr>
<tr>
<td>6</td>
<td>Challenge HHD UC</td>
<td>1</td>
<td>DE</td>
<td>bin</td>
<td>..</td>
<td>O</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>7</td>
<td>Gültigkeitsdatum und -uhrzeit für Challenge</td>
<td>1</td>
<td>DEG</td>
<td></td>
<td></td>
<td>O</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>8</td>
<td>TAN-Listennummer</td>
<td>1</td>
<td>DE</td>
<td>an</td>
<td>.20</td>
<td>C</td>
<td>1</td>
<td>M: bei TAN-Prozess=1, 3, 4 und „Anzahl unterstützter aktiver TAN-Listen" nicht vorhanden O: sonst</td>
</tr>
<tr>
<td>9</td>
<td>BEN</td>
<td>1</td>
<td>DE</td>
<td>an</td>
<td>..99</td>
<td>C</td>
<td>1</td>
<td>O: bei TAN-Prozess=2 N: sonst</td>
</tr>
<tr>
<td>10</td>
<td>Bezeichnung des TAN-Mediums</td>
<td>1</td>
<td>DE</td>
<td>an</td>
<td>..32</td>
<td>C</td>
<td>1</td>
<td>M: bei TAN-Prozess=1, 3, 4 und „Anzahl unterstützter aktiver TAN-Medien" nicht vorhanden O: sonst</td>
</tr>
</table>


<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: D</td>
<td>Version: 3.0-FV</td>
<td>Financial Transaction Services (FinTS) Dokument: Security - Sicherheitsverfahren PIN/TAN</td>
</tr>
<tr>
<td>Seite:<br>168</td>
<td>Stand: 23.02.2018</td>
<td>Kapitel: Archiv: Ältere Segmentversionen<br>Abschnitt: HKTAN für Zwei-Schritt-TAN-Einreichung</td>
</tr>
</table>


#### ◆ Belegungsrichtlinien


##### Auftrags-Hashwert

Es ist der in der Kundennachricht in HKTAN übermittelte Auftrags-Hashwert
unverändert einzustellen.


##### Auftragsreferenz

Bei TAN-Prozess=2, 3 und 4 muss die Auftragsreferenz vom Institut immer
eingestellt werden. Bei TAN-Prozess=1 muss die Auftragsreferenz einge-
stellt werden, wenn sie zuvor im Segment HKTAN vom Kunden gesendet
wurde.


##### Challenge

Obwohl die Challenge bei Prozessvariante 2 im zweiten Schritt nicht zwin-
gend benötigt wird, sollte sie aus Integritätsgründen trotzdem übertragen
werden.


![](figures/168.1)


Das Kundenprodukt muss den Inhalt der empfangenen Challenge
dem Kunden unverändert anzeigen. Ist der BPD-Parameter ,,Chal-
lenge strukturiert“ mit „J“ belegt, so können im DE Challenge For-
matsteuerzeichen enthalten sein, die dann entsprechend zu inter-
pretieren sind (Näheres hierzu im Data Dictionary unter dem DE
,Challenge“).

Erläuterung: Die Challenge kann institutsindividuell aufgebaut wer-
den (z. B. 1 oder 2 Eingabefelder für den chipTAN-Leser).


##### Challenge HHD_UC

Das Datenelement enthält eine Datenstruktur, die entsprechend den Vorga-
ben aus [HHD-Erweiterung] aufgebaut sein muss. Die einzelnen Elemente
dieser Datenstruktur sind für FinTS transparent und werden nicht durch
Trennzeichen getrennt.


##### TAN-Listennummer

Ist in der BPD der Parameter ,,Anzahl unterstützter aktiver TAN-Listen“ nicht
vorhanden, so muss das Institut dem Kunden hier mitteilen, welche TAN-
Liste er z. B. bei Einsatz eines indizierten TAN-Verfahrens verwenden soll.


##### Bezeichnung des TAN-Mediums

Ist in der BPD der Parameter „Anzahl unterstützter aktiver TAN-Medien“
nicht vorhanden, so muss das Institut dem Kunden hier mitteilen, welches
TAN-Medium er z. B. beim mobileTAN-Verfahren verwenden soll.

<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th rowspan="2">Version: 3.0-FV</th>
<th rowspan="2">Kapitel: D</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Security - Sicherheitsverfahren PIN/TAN</td>
</tr>
<tr>
<td>Kapitel:<br>Abschnitt:</td>
<td>Archiv: Ältere Segmentversionen HKTAN für Zwei-Schritt-TAN-Einreichung</td>
<td>Stand: 23.02.2018</td>
<td>Seite: 169</td>
</tr>
</table>


## ◆ Ausgewählte Beispiele für Rückmeldungscodes


<table>
<tr>
<td>Code</td>
<td>Beispiel für Rückmeldungstext</td>
</tr>
<tr>
<td>0010</td>
<td>Auftrag entgegengenommen</td>
</tr>
<tr>
<td>9210</td>
<td>Auftrag abgelehnt - Auftragsdaten inkonsistent. Eingereichter Auftrag gelöscht</td>
</tr>
<tr>
<td>9210</td>
<td>Auftrag abgelehnt – Zwei-Schritt-TAN inkonsistent. Eingereichter Auftrag gelöscht</td>
</tr>
<tr>
<td>9210</td>
<td>Auftrag abgelehnt – Kein eingereichter Auftrag gefunden</td>
</tr>
<tr>
<td>9210</td>
<td>Auftrag abgelehnt – Auftragsreferenz ist unbekannt</td>
</tr>
<tr>
<td>9330</td>
<td>chipTAN-Leser gesperrt. Führen Sie ggf. eine chipTAN-Synchronisation durch</td>
</tr>
<tr>
<td>9360</td>
<td>Sperrung der TAN-Liste nach weiteren x Fehlversuchen</td>
</tr>
<tr>
<td>9380</td>
<td>Gewähltes Zwei-Schritt-TAN-Verfahren nicht zulässig</td>
</tr>
<tr>
<td>9931</td>
<td>Sperrung des Kontos nach x Fehlversuchen</td>
</tr>
<tr>
<td>9941</td>
<td>TAN ungültig</td>
</tr>
<tr>
<td>9951</td>
<td>Zeitüberschreitung im Zwei-Schritt-Verfahren – TAN ungültig</td>
</tr>
<tr>
<td>9953</td>
<td>Nur ein TAN-pflichtiger Auftrag pro Nachricht erlaubt</td>
</tr>
<tr>
<td>9954</td>
<td>Mehrfach-TANs nicht erlaubt</td>
</tr>
<tr>
<td>9955</td>
<td>Ein-Schritt-TAN-Verfahren nicht zugelassen</td>
</tr>
<tr>
<td>9956</td>
<td>Zeitversetzte Eingabe von Mehrfach-TANs nicht erlaubt</td>
</tr>
<tr>
<td>9991</td>
<td>TAN bereits verbraucht</td>
</tr>
</table>


# c) Bankparameterdaten


## Format


<table>
<tr>
<td>Name:</td>
<td>Zwei-Schritt-TAN-Einreichung, Parameter</td>
</tr>
<tr>
<td>Typ:</td>
<td>Segment</td>
</tr>
<tr>
<td>Segmentart:</td>
<td>Geschäftsvorfallparameter</td>
</tr>
<tr>
<td>Kennung:</td>
<td>HITANS</td>
</tr>
<tr>
<td>Bezugssegment:</td>
<td>HKVVB</td>
</tr>
<tr>
<td>Segmentversion:</td>
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
<tr>
<td>5</td>
<td>Parameter Zwei- Schritt-TAN- Einreichung</td>
<td>4</td>
<td>DEG</td>
<td></td>
<td></td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
</table>


## ◆ Belegungsrichtlinien

Auftrags-Hashwertverfahren (Parameter Zwei-Schritt-TAN-Einreichung)
Bei Verwendung von TAN-Prozess=1.


## E.1.5 Geschäftsvorfall HKTAN in Segmentversion #5

Ab der Segmentversion #5 dieses Geschäftsvorfalls ist das chipTAN-Verfahren mit
unidirektionaler Kopplung bis zur Version 1.4 unterstützt. Mit dieser Version können

<!-- PageBreak -->


<table>
<tr>
<th>Kapitel: D</th>
<th>Version: 3.0-FV</th>
<th>Financial Transaction Services (FinTS) Dokument: Security - Sicherheitsverfahren PIN/TAN</th>
</tr>
<tr>
<td>Seite:<br>170</td>
<td>Stand: 23.02.2018</td>
<td>Kapitel: Archiv: Ältere Segmentversionen<br>Abschnitt: HKTAN für Zwei-Schritt-TAN-Einreichung</td>
</tr>
</table>


aber auch alle anderen PIN/TAN Zwei-Schritt-Verfahren unterstützt werden; wahl-
weise können Kreditinstitute zusätzlich auch andere Segmentversionen von HKTAN
anbieten.


![](figures/170.1)


In der BPD können sich mehrere Segmentversionen von HITANS-
Segmenten befinden, wobei den einzelnen HITANS-Segmenten
über das Element „Sicherheitsfunktion, kodiert“ unterschiedliche
Verfahren zugeordnet sein können. Ein Kundenprodukt sollte – be-
ginnend mit der höchsten Segmentversion - alle in der BPD enthal-
tenen HITANS-Segmente analysieren, um so dem Kunden alle vom
Kreditinstitut unterstützten Sicherheitsverfahren anbieten zu kön-
nen.

Beispiel: Die BPD enthält Definitionen für HITANS#5 und
HITANS#4. In HITANS#5 ist das Verfahren chipTAN nach HHD
V1.4 parametrisiert. HITANS#4 enthält die Beschreibung für mobi-
leTAN.

Realisierung Bank: verpflichtend in mindestens einer Segmentversion, falls
Geschäftsvorfälle mit PIN/TAN-Absicherung im Zwei-Schritt-
Verfahren angeboten werden.

Realisierung Kunde: optional


# a) Kundenauftrag


# Format


<table>
<tr>
<td>Name:</td>
<td>Zwei-Schritt-TAN-Einreichung</td>
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
<td>HKTAN</td>
</tr>
<tr>
<td>Bezugssegment:</td>
<td>-</td>
</tr>
<tr>
<td>Segmentversion:</td>
<td>5</td>
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
<td>TAN-Prozess</td>
<td>1</td>
<td>DE</td>
<td>code</td>
<td>1</td>
<td>M</td>
<td>1</td>
<td>1, 2, 3, 4</td>
</tr>
<tr>
<td>3</td>
<td>Segmentkennung</td>
<td>1</td>
<td>DE</td>
<td>an</td>
<td>..6</td>
<td>C</td>
<td>1</td>
<td>M: bei TAN-Prozess=1 N: sonst</td>
</tr>
<tr>
<td>4</td>
<td>Kontoverbindung international Auf- traggeber</td>
<td>1</td>
<td>DEG</td>
<td>kti</td>
<td>#</td>
<td>C</td>
<td>1</td>
<td>M: bei TAN-Prozess=1 und „Auftraggeberkonto erfor- derlich"=2 und Kontover- bindung im Auftrag enthal- ten N: sonst</td>
</tr>
<tr>
<td>5</td>
<td>Auftrags-Hashwert</td>
<td>1</td>
<td>DE</td>
<td>bin</td>
<td>.256</td>
<td>C</td>
<td>1</td>
<td>M: bei Auftrags- Hashwertverfahren&lt;&gt;0 und TAN-Prozess=1 N: sonst</td>
</tr>
<tr>
<td>6</td>
<td>Auftragsreferenz</td>
<td>1</td>
<td>DE</td>
<td>an</td>
<td>..35</td>
<td>C</td>
<td>1</td>
<td>M: bei TAN-Prozess=2, 3 O: TAN-Prozess=1, 4</td>
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
<td>Dokument:</td>
<td>Security - Sicherheitsverfahren PIN/TAN</td>
</tr>
<tr>
<td>Kapitel:<br>Abschnitt:</td>
<td>Archiv: Ältere Segmentversionen HKTAN für Zwei-Schritt-TAN-Einreichung</td>
<td>Stand: 23.02.2018</td>
<td>Seite: 171</td>
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
<td>7</td>
<td>TAN-Listennummer</td>
<td>1</td>
<td>DE</td>
<td>an</td>
<td>.20</td>
<td>C</td>
<td>1</td>
<td>M: bei TAN-Prozess=1, 3, 4 und „Anzahl unterstützter aktiver TAN-Listen“ &gt; 1 und ,TAN-Listennummer erfor- derlich"=2 O: sonst</td>
</tr>
<tr>
<td>8</td>
<td>Weitere TAN folgt</td>
<td>1</td>
<td>DE</td>
<td>jn</td>
<td>1</td>
<td>C</td>
<td>1</td>
<td>M: bei TAN-Prozess=1, 2 N: bei TAN-Prozess=3, 4</td>
</tr>
<tr>
<td>9</td>
<td>Auftrag stornieren</td>
<td>1</td>
<td>DE</td>
<td>jn</td>
<td>1</td>
<td>C</td>
<td>1</td>
<td>O: bei TAN-Prozess=2 und „Auftragsstorno erlaubt“=J N: sonst</td>
</tr>
<tr>
<td>10</td>
<td>SMS- Abbuchungskonto</td>
<td>1</td>
<td>DEG</td>
<td>kti</td>
<td>#</td>
<td>C</td>
<td>1</td>
<td>M: b<br>ei TAN-Prozess=1, 3, 4 und "SMS-Abbuchungskonto er- forderlich“=2<br>O: sonst</td>
</tr>
<tr>
<td>11</td>
<td>Challenge-Klasse</td>
<td>1</td>
<td>DE</td>
<td>num</td>
<td>..2</td>
<td>C</td>
<td>1</td>
<td>M: bei TAN-Prozess=1 und ,,Challenge-Klasse erforder- lich“=J N: sonst</td>
</tr>
<tr>
<td>12</td>
<td>Parameter Challen- ge-Klasse</td>
<td>1</td>
<td>DEG</td>
<td></td>
<td></td>
<td>C</td>
<td>1</td>
<td>O: bei TAN-Prozess=1 und ,,Challenge-Klasse erforder- lich“=J N: sonst</td>
</tr>
<tr>
<td>13</td>
<td>Bezeichnung des TAN-Mediums</td>
<td>1</td>
<td>DE</td>
<td>an</td>
<td>..32</td>
<td>C</td>
<td>1</td>
<td>M: bei TAN-Prozess=1, 3, 4 und „Anzahl unterstützter aktiver TAN-Medien“ &gt; 1 und ,,Bezeichnung des TAN-Mediums erforder- lich“=2 O: sonst</td>
</tr>
</table>


<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: D</td>
<td>Version: 3.0-FV</td>
<td>Financial Transaction Services (FinTS) Dokument: Security - Sicherheitsverfahren PIN/TAN</td>
</tr>
<tr>
<td>Seite:<br>172</td>
<td>Stand: 23.02.2018</td>
<td>Kapitel: Archiv: Ältere Segmentversionen<br>Abschnitt: HKTAN für Zwei-Schritt-TAN-Einreichung</td>
</tr>
</table>


# ◆ Belegungsrichtlinien


## Auftragsreferenz

Als Auftragsreferenz ist derjenige Wert einzustellen, der bei der Auftragsein-
reichung im Rahmen der Kreditinstitutsrückmeldung mitgeteilt wurde.


## Parameter Challenge-Klasse

Die Parameter zur Challenge-Klasse dienen zur Übermittlung von Daten, die
bei Prozessvariante 1 im ersten Verfahrensschritt für die weitere Steuerung
benötigt werden. Die konkrete Belegung der Parameter sind den Belegungs-
richtlinien des jeweiligen Verfahrens zu entnehmen. Für die DK-Verfahren
chipTAN und mobileTAN gelten die Festlegungen in [HHD Belegung].


## TAN-Listennummer

Ist in der BPD als „Anzahl unterstützter aktiver TAN-Listen“ ein Wert > 1 an-
gegeben und ist der BPD-Wert für „TAN-Listennummer erforderlich“ = 2, so
muss der Kunde z. B. im Falle eines indizierten TAN-Verfahrens hier seine
für diesen Auftrag zu verwendende TAN-Liste angeben.


## Bezeichnung des TAN-Mediums

Ist in der BPD als ,,Anzahl unterstützter aktiver TAN-Medien“ ein Wert > 1
angegeben und ist der BPD-Wert für „Bezeichnung des TAN-Mediums erfor-
derlich" = 2, so muss der Kunde z. B. im Falle des mobileTAN-Verfahrens
hier die Bezeichnung seines für diesen Auftrag zu verwendenden TAN-
Mediums angeben.


## SMS-Abbuchungskonto

Ist in der BPD als ,,SMS-Abbuchungskonto erforderlich" mit ,,2" belegt, so
muss der Kunde z. B. im Falle des mobileTAN-Verfahrens hier das für die-
sen Auftrag zu belastende SMS-Abbuchungskonto einstellen. Dieses kann
unabhängig von der Kontoverbindung des Dialogführers gewählt werden.

<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th rowspan="2">Version: 3.0-FV</th>
<th rowspan="2">Kapitel: D</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Security - Sicherheitsverfahren PIN/TAN</td>
</tr>
<tr>
<td>Kapitel:<br>Abschnitt:</td>
<td>Archiv: Ältere Segmentversionen<br>HKTAN für Zwei-Schritt-TAN-Einreichung</td>
<td>Stand: 23.02.2018</td>
<td>Seite: 173</td>
</tr>
</table>


### b) Kreditinstitutsrückmeldung

Format


<table>
<tr>
<td>Name:</td>
<td>Zwei-Schritt-TAN-Einreichung Rückmeldung</td>
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
<td>HITAN</td>
</tr>
<tr>
<td>Bezugssegment:</td>
<td>HKTAN</td>
</tr>
<tr>
<td>Segmentversion:</td>
<td>5</td>
</tr>
<tr>
<td>Anzahl:</td>
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
<td>TAN-Prozess</td>
<td>1</td>
<td>DE</td>
<td>code</td>
<td>1</td>
<td>M</td>
<td>1</td>
<td>1, 2, 3, 4</td>
</tr>
<tr>
<td>3</td>
<td>Auftrags-Hashwert</td>
<td>1</td>
<td>DE</td>
<td>bin</td>
<td>.256</td>
<td>C</td>
<td>1</td>
<td>M: bei Auftrags- Hashwertverfahren&lt;&gt;0 und TAN-Prozess=1, N: sonst</td>
</tr>
<tr>
<td>4</td>
<td>Auftragsreferenz</td>
<td>1</td>
<td>DE</td>
<td>an</td>
<td>..35</td>
<td>C</td>
<td>1</td>
<td>M: bei TAN-Prozess=2, 3, 4 O: bei TAN-Prozess=1</td>
</tr>
<tr>
<td>5</td>
<td>Challenge</td>
<td>3</td>
<td>DE</td>
<td>an</td>
<td>.204 8</td>
<td>C</td>
<td>1</td>
<td>M: bei TAN-Prozess=1, 3, 4 O: bei TAN-Prozess=2</td>
</tr>
<tr>
<td>6</td>
<td>Challenge HHD UC</td>
<td>1</td>
<td>DE</td>
<td>bin</td>
<td>..</td>
<td>O</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>7</td>
<td>Gültigkeitsdatum und -uhrzeit für Challenge</td>
<td>1</td>
<td>DEG</td>
<td></td>
<td></td>
<td>O</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>8</td>
<td>TAN-Listennummer</td>
<td>1</td>
<td>DE</td>
<td>an</td>
<td>.20</td>
<td>C</td>
<td>1</td>
<td>M: bei TAN-Prozess=1, 3, 4 und „Anzahl unterstützter aktiver TAN-Listen" nicht vorhanden O: sonst</td>
</tr>
<tr>
<td>9</td>
<td>BEN</td>
<td>1</td>
<td>DE</td>
<td>an</td>
<td>..99</td>
<td>C</td>
<td>1</td>
<td>O: bei TAN-Prozess=2 N: sonst</td>
</tr>
<tr>
<td>10</td>
<td>Bezeichnung des TAN-Mediums</td>
<td>1</td>
<td>DE</td>
<td>an</td>
<td>..32</td>
<td>C</td>
<td>1</td>
<td>M: bei TAN-Prozess=1, 3, 4 und „Anzahl unterstützter aktiver TAN-Medien" nicht vorhanden O: sonst</td>
</tr>
</table>


<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: D</td>
<td>Version: 3.0-FV</td>
<td>Financial Transaction Services (FinTS) Dokument: Security - Sicherheitsverfahren PIN/TAN</td>
</tr>
<tr>
<td>Seite: 174</td>
<td>Stand: 23.02.2018</td>
<td>Kapitel: Archiv: Ältere Segmentversionen<br>Abschnitt: HKTAN für Zwei-Schritt-TAN-Einreichung</td>
</tr>
</table>


# ◆ Belegungsrichtlinien


## Auftrags-Hashwert

Es ist der in der Kundennachricht in HKTAN übermittelte Auftrags-Hashwert
unverändert einzustellen.


## Auftragsreferenz

Bei TAN-Prozess=2, 3 und 4 muss die Auftragsreferenz vom Institut immer
eingestellt werden. Bei TAN-Prozess=1 muss die Auftragsreferenz einge-
stellt werden, wenn sie zuvor im Segment HKTAN vom Kunden gesendet
wurde.


## Challenge

Obwohl die Challenge bei Prozessvariante 2 im zweiten Schritt nicht zwin-
gend benötigt wird, sollte sie aus Integritätsgründen trotzdem übertragen
werden.


![](figures/174.1)


Das Kundenprodukt muss den Inhalt der empfangenen Challenge
dem Kunden unverändert anzeigen. Ist der BPD-Parameter „Chal-
lenge strukturiert“ mit „J“ belegt, so können im DE Challenge For-
matsteuerzeichen enthalten sein, die dann entsprechend zu inter-
pretieren sind (Näheres hierzu im Data Dictionary unter dem DE
,Challenge“).

Erläuterung: Die Challenge kann institutsindividuell aufgebaut wer-
den (z. B. 1 oder 2 Eingabefelder für den chipTAN-Leser).


## Challenge HHD_UC

Das Datenelement enthält eine Datenstruktur, die entsprechend den Vorga-
ben aus [HHD-Erweiterung] aufgebaut sein muss. Die einzelnen Elemente
dieser Datenstruktur sind für FinTS transparent und werden nicht durch
Trennzeichen getrennt.


## TAN-Listennummer

Ist in der BPD der Parameter ,,Anzahl unterstützter aktiver TAN-Listen“ nicht
vorhanden, so muss das Institut dem Kunden hier mitteilen, welche TAN-
Liste er z. B. bei Einsatz eines indizierten TAN-Verfahrens verwenden soll.


## Bezeichnung des TAN-Mediums

Ist in der BPD der Parameter „Anzahl unterstützter aktiver TAN-Medien“
nicht vorhanden, so muss das Institut dem Kunden hier mitteilen, welches
TAN-Medium er z. B. beim mobileTAN-Verfahren verwenden soll.

<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th rowspan="2">Version: 3.0-FV</th>
<th rowspan="2">Kapitel: D</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Security - Sicherheitsverfahren PIN/TAN</td>
</tr>
<tr>
<td>Kapitel:<br>Abschnitt:</td>
<td>Archiv: Ältere Segmentversionen HKTAN für Zwei-Schritt-TAN-Einreichung</td>
<td>Stand: 23.02.2018</td>
<td>Seite: 175</td>
</tr>
</table>


### ◆ Ausgewählte Beispiele für Rückmeldungscodes


<table>
<tr>
<td>Code</td>
<td>Beispiel für Rückmeldungstext</td>
</tr>
<tr>
<td>0010</td>
<td>Auftrag entgegengenommen</td>
</tr>
<tr>
<td>9210</td>
<td>Auftrag abgelehnt – Auftragsdaten inkonsistent. Eingereichter Auftrag gelöscht</td>
</tr>
<tr>
<td>9210</td>
<td>Auftrag abgelehnt - Zwei-Schritt-TAN inkonsistent. Eingereichter Auftrag gelöscht</td>
</tr>
<tr>
<td>9210</td>
<td>Auftrag abgelehnt – Kein eingereichter Auftrag gefunden</td>
</tr>
<tr>
<td>9210</td>
<td>Auftrag abgelehnt – Auftragsreferenz ist unbekannt</td>
</tr>
<tr>
<td>9330</td>
<td>chipTAN-Leser gesperrt. Führen Sie ggf. eine chipTAN-Synchronisation durch</td>
</tr>
<tr>
<td>9360</td>
<td>Sperrung der TAN-Liste nach weiteren x Fehlversuchen</td>
</tr>
<tr>
<td>9380</td>
<td>Gewähltes Zwei-Schritt-TAN-Verfahren nicht zulässig</td>
</tr>
<tr>
<td>9931</td>
<td>Sperrung des Kontos nach x Fehlversuchen</td>
</tr>
<tr>
<td>9941</td>
<td>TAN ungültig</td>
</tr>
<tr>
<td>9951</td>
<td>Zeitüberschreitung im Zwei-Schritt-Verfahren – TAN ungültig</td>
</tr>
<tr>
<td>9953</td>
<td>Nur ein TAN-pflichtiger Auftrag pro Nachricht erlaubt</td>
</tr>
<tr>
<td>9954</td>
<td>Mehrfach-TANs nicht erlaubt</td>
</tr>
<tr>
<td>9955</td>
<td>Ein-Schritt-TAN-Verfahren nicht zugelassen</td>
</tr>
<tr>
<td>9956</td>
<td>Zeitversetzte Eingabe von Mehrfach-TANs nicht erlaubt</td>
</tr>
<tr>
<td>9991</td>
<td>TAN bereits verbraucht</td>
</tr>
</table>


### c) Bankparameterdaten


#### Format


<table>
<tr>
<td>Name:</td>
<td>Zwei-Schritt-TAN-Einreichung, Parameter</td>
</tr>
<tr>
<td>Typ:</td>
<td>Segment</td>
</tr>
<tr>
<td>Segmentart:</td>
<td>Geschäftsvorfallparameter</td>
</tr>
<tr>
<td>Kennung:</td>
<td>HITANS</td>
</tr>
<tr>
<td>Bezugssegment:</td>
<td>HKVVB</td>
</tr>
<tr>
<td>Segmentversion:</td>
<td>5</td>
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
<tr>
<td>5</td>
<td>Parameter Zwei- Schritt-TAN- Einreichung</td>
<td>5</td>
<td>DEG</td>
<td></td>
<td></td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
</table>


<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: D</td>
<td>Version: 3.0-FV</td>
<td>Financial Transaction Services (FinTS) Dokument: Security - Sicherheitsverfahren PIN/TAN</td>
</tr>
<tr>
<td>Seite:<br>176</td>
<td>Stand: 23.02.2018</td>
<td>Kapitel: Archiv: Ältere Segmentversionen<br>Abschnitt: Management chipTAN, mobileTAN und bilaterale Verfahren</td>
</tr>
</table>


#### ◆ Belegungsrichtlinien

Auftrags-Hashwertverfahren (Parameter Zwei-Schritt-TAN-Einreichung)
Bei Verwendung von TAN-Prozess=1.


## E.2 Management chipTAN, mobileTAN und bilaterale Verfahren


### E.2.1 Anzeige der verfügbaren TAN-Medien


### E.2.1.1Anzeigen der verfügbaren TAN-Medien, Segmentversion #1

Realisierung Bank:
optional

Realisierung Kunde: optional


#### a) Kundenauftrag


#### Format


<table>
<tr>
<td>Name:</td>
<td>TAN-Generator/Liste anzeigen Bestand</td>
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
<td>HKTAB</td>
</tr>
<tr>
<td>Bezugssegment:</td>
<td>-</td>
</tr>
<tr>
<td>Segmentversion:</td>
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
<td>TAN-Medium-Art</td>
<td>1</td>
<td>DE</td>
<td>code</td>
<td>1</td>
<td>M</td>
<td>1</td>
<td>0, 2, 3</td>
</tr>
</table>


b)
Kreditinstitutsrückmeldung


##### ◆ Erläuterungen

Es wird ein Datensegment zurückgemeldet.


##### ◆ Format


<table>
<tr>
<td>Name:</td>
<td>TAN-Generator/Liste anzeigen Bestand Rückmeldung</td>
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
<td>HITAB</td>
</tr>
<tr>
<td>Bezugssegment:</td>
<td>HKTAB</td>
</tr>
<tr>
<td>Segmentversion:</td>
<td>1</td>
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
<th>Version:</th>
<th>Kapitel:</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Security - Sicherheitsverfahren PIN/TAN</td>
<td>3.0-FV</td>
<td>D</td>
</tr>
<tr>
<td>Kapitel:</td>
<td>Archiv: Ältere Segmentversionen</td>
<td>Stand:</td>
<td>Seite:</td>
</tr>
<tr>
<td>Abschnitt:</td>
<td>Management chipTAN, mobileTAN und bilaterale Verfahren</td>
<td>23.02.2018</td>
<td>177</td>
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
<td>TAN-Einsatzoption</td>
<td>1</td>
<td>DE</td>
<td>code</td>
<td>1</td>
<td>M</td>
<td>1</td>
<td>0, 1, 2</td>
</tr>
<tr>
<td>3</td>
<td>TAN-Medium-Liste</td>
<td>1</td>
<td>DEG</td>
<td></td>
<td></td>
<td>O</td>
<td>.99</td>
<td></td>
</tr>
</table>


#### ◆ Belegungsrichtlinien


##### TAN-Medium-Liste

Darf nur belegt werden, wenn für den Kunden ein TAN-Medium verfügbar /
nutzbar ist.


#### ◆ Ausgewählte Beispiele für Rückmeldungscodes


<table>
<tr>
<td>Code</td>
<td>Beispiel für Rückmeldungstext</td>
</tr>
<tr>
<td>0020</td>
<td>Auftrag verarbeitet</td>
</tr>
</table>


c)
Bankparameterdaten


##### Beschreibung

Geschäftsvorfallspezifische Parameter existieren nicht.


###### ◆ Format


<table>
<tr>
<td>Name:</td>
<td>TAN-Generator/Liste anzeigen Bestand Parameter</td>
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
<td>HITABS</td>
</tr>
<tr>
<td>Bezugssegment:</td>
<td>HKVVB</td>
</tr>
<tr>
<td>Segmentversion:</td>
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


### E.2.1.2Anzeigen der verfügbaren TAN-Medien, Segmentversion #2

Zusätzlich zur Segmentversion 1 des Geschäftsvorfalls wird nun auch das mobi-
leTAN-Verfahren unterstützt.

Dem Kunden wird eine Übersicht über seine verfügbaren TAN-Medien (TAN-
Generator, Mobiltelefon und TAN-Liste) angezeigt.

Der Kunde muss auch im Hinblick auf das TAN-Zwei-Schritt-Verfahren wissen, wel-
ches Medium er verwenden darf. Hierzu werden ihm seine verfügbaren Medien
(Karten, Telefonbezeichnungen bzw. TAN-Listennummern) mit ihrem aktuellen Sta-
tus angezeigt. Es wird dahingehend unterschieden, ob das Medium „Verfügbar“ o-
der ,Aktiv" ist. Folgekarten werden bei TAN-Generatoren separat mit eigenen Kenn-

<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: D</td>
<td>Version: 3.0-FV</td>
<td>Financial Transaction Services (FinTS) Dokument: Security - Sicherheitsverfahren PIN/TAN</td>
</tr>
<tr>
<td>Seite:<br>178</td>
<td>Stand: 23.02.2018</td>
<td>Kapitel: Archiv: Ältere Segmentversionen<br>Abschnitt: Management chipTAN, mobileTAN und bilaterale Verfahren</td>
</tr>
</table>


zeichen versehen, da mit der ,Aktivierung“ der Folgekarte die aktuelle Karte für die
TAN-Generierung gesperrt wird.


<table>
<tr>
<td>Status</td>
<td>Erläuterungen</td>
</tr>
<tr>
<td>Verfügbar</td>
<td>Das Medium kann genutzt werden, muss aber zuvor fol- gendermaßen aktiv gemeldet werden:<br>◆ TAN-Generator: mit ,TAN-Generator an- bzw. ummel- den (HKTAU)"<br>◆ Mobiltelefon mit „Mobilfunkverbindung freischalten“</td>
</tr>
<tr>
<td>Aktiv</td>
<td>Das Institut zeigt an, dass es eine TAN-Verifikation gegen dieses Medium vornimmt.</td>
</tr>
<tr>
<td>Verfügbare Folgekarte</td>
<td>Das Medium kann mit dem Geschäftsvorfall „TAN- Generator an- bzw. ummelden (HKTAU)“ aktiv gemeldet werden. Die aktuelle Karte kann dann nicht mehr genutzt werden.</td>
</tr>
<tr>
<td>Aktiv Folgekarte</td>
<td>Mit der ersten Nutzung der Folgekarte wird die zur Zeit ak- tive Karte gesperrt.</td>
</tr>
</table>


Anmerkung: Wenn ein Institut mehrere Medien in dem Status „Aktiv“ verwalten
kann, dann muss beim Zwei-Schritt-Verfahren dem Institut zuvor mit dem Ge-
schäftsvorfall „TAN-Generator an- bzw. ummelden“ (HKTAU) mitgeteilt werden, wel-
ches Medium für die Signatur des Geschäftsvorfalles verwendet werden soll.

Realisierung Bank:
optional

Realisierung Kunde: optional


## a) Kundenauftrag


# Format


<table>
<tr>
<td>Name:</td>
<td>TAN-Generator/Liste anzeigen Bestand</td>
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
<td>HKTAB</td>
</tr>
<tr>
<td>Bezugssegment:</td>
<td>-</td>
</tr>
<tr>
<td>Segmentversion:</td>
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
<td>TAN-Medium-Art</td>
<td>1</td>
<td>DE</td>
<td>code</td>
<td>1</td>
<td>M</td>
<td>1</td>
<td>0, 2, 3</td>
</tr>
</table>


## b) Kreditinstitutsrückmeldung


## Erläuterungen

Es wird ein Datensegment zurückgemeldet.

<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th>Version:</th>
<th rowspan="2">Kapitel: D</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Security - Sicherheitsverfahren PIN/TAN</td>
<td>3.0-FV</td>
</tr>
<tr>
<td>Kapitel:</td>
<td>Archiv: Ältere Segmentversionen</td>
<td>Stand:</td>
<td>Seite:</td>
</tr>
<tr>
<td>Abschnitt:</td>
<td>Management chipTAN, mobileTAN und bilaterale Verfahren</td>
<td>23.02.2018</td>
<td>179</td>
</tr>
</table>


## ◆ Format


<table>
<tr>
<td>Name:</td>
<td>TAN-Generator/Liste anzeigen Bestand Rückmeldung</td>
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
<td>HITAB</td>
</tr>
<tr>
<td>Bezugssegment:</td>
<td>HKTAB</td>
</tr>
<tr>
<td>Segmentversion:</td>
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
<td>TAN-Einsatzoption</td>
<td>1</td>
<td>DE</td>
<td>code</td>
<td>1</td>
<td>M</td>
<td>1</td>
<td>0, 1, 2</td>
</tr>
<tr>
<td>3</td>
<td>TAN-Medium-Liste</td>
<td>2</td>
<td>DEG</td>
<td></td>
<td></td>
<td>O</td>
<td>..99</td>
<td></td>
</tr>
</table>


## ◆ Belegungsrichtlinien


### TAN-Medium-Liste

Darf nur belegt werden, wenn für den Kunden ein TAN-Medium verfügbar /
nutzbar ist.


## ◆ Ausgewählte Beispiele für Rückmeldungscodes


<table>
<tr>
<td>Code</td>
<td>Beispiel für Rückmeldungstext</td>
</tr>
<tr>
<td>0020</td>
<td>Auftrag verarbeitet</td>
</tr>
</table>


### c) Bankparameterdaten


### Beschreibung

Geschäftsvorfallspezifische Parameter existieren nicht.


#### ◆ Format


<table>
<tr>
<td>Name:</td>
<td>TAN-Generator/Liste anzeigen Bestand Parameter</td>
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
<td>HITABS</td>
</tr>
<tr>
<td>Bezugssegment:</td>
<td>HKVVB</td>
</tr>
<tr>
<td>Segmentversion:</td>
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


## E.2.1.3Anzeigen der verfügbaren TAN-Medien, Segmentversion #3

Bei Segmentversion 3 wurden gegenüber der Vorgängerversion die Elemente „TAN-
Medium-Art“ und „TAN-Medium-Liste“ für das mobileTAN-Verfahren angepasst.

<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: D</td>
<td>Version: 3.0-FV</td>
<td>Financial Transaction Services (FinTS) Dokument: Security - Sicherheitsverfahren PIN/TAN</td>
</tr>
<tr>
<td>Seite: 180</td>
<td>Stand: 23.02.2018</td>
<td>Kapitel: Archiv: Ältere Segmentversionen<br>Abschnitt: Management chipTAN, mobileTAN und bilaterale Verfahren</td>
</tr>
</table>


Realisierung Bank: optional

Realisierung Kunde: optional


# a) Kundenauftrag


## Format


<table>
<tr>
<td>Name:</td>
<td>TAN-Generator/Liste anzeigen Bestand</td>
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
<td>HKTAB</td>
</tr>
<tr>
<td>Bezugssegment:</td>
<td>-</td>
</tr>
<tr>
<td>Segmentversion:</td>
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
<td>TAN-Medium-Art</td>
<td>2</td>
<td>DE</td>
<td>code</td>
<td>1</td>
<td>M</td>
<td>1</td>
<td>0, 1, 2</td>
</tr>
</table>


## b) Kreditinstitutsrückmeldung


## Erläuterungen

Es wird ein Datensegment zurückgemeldet.


### ◆ Format


<table>
<tr>
<td>Name:</td>
<td>TAN-Generator/Liste anzeigen Bestand Rückmeldung</td>
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
<td>HITAB</td>
</tr>
<tr>
<td>Bezugssegment:</td>
<td>HKTAB</td>
</tr>
<tr>
<td>Segmentversion:</td>
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
<td>TAN-Einsatzoption</td>
<td>1</td>
<td>DE</td>
<td>code</td>
<td>1</td>
<td>M</td>
<td>1</td>
<td>0, 1, 2</td>
</tr>
<tr>
<td>3</td>
<td>TAN-Medium-Liste</td>
<td>3</td>
<td>DEG</td>
<td></td>
<td></td>
<td>O</td>
<td>.99</td>
<td></td>
</tr>
</table>


### ◆ Belegungsrichtlinien

TAN-Medium-Liste

Darf nur belegt werden, wenn für den Kunden ein TAN-Medium verfügbar /
nutzbar ist.


### ◆ Ausgewählte Beispiele für Rückmeldungscodes


<table>
<tr>
<td>Code</td>
<td>Beispiel für Rückmeldungstext</td>
</tr>
<tr>
<td>0020</td>
<td>Auftrag verarbeitet</td>
</tr>
</table>


<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th>Version:</th>
<th rowspan="2">Kapitel: D</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Security - Sicherheitsverfahren PIN/TAN</td>
<td>3.0-FV</td>
</tr>
<tr>
<td>Kapitel:</td>
<td>Archiv: Ältere Segmentversionen</td>
<td>Stand:</td>
<td>Seite:</td>
</tr>
<tr>
<td>Abschnitt:</td>
<td>Management chipTAN, mobileTAN und bilaterale Verfahren</td>
<td>23.02.2018</td>
<td>181</td>
</tr>
</table>


c)
Bankparameterdaten


## Beschreibung

Geschäftsvorfallspezifische Parameter existieren nicht.


### ◆ Format


<table>
<tr>
<td>Name:</td>
<td>TAN-Generator/Liste anzeigen Bestand Parameter</td>
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
<td>HITABS</td>
</tr>
<tr>
<td>Bezugssegment:</td>
<td>HKVVB</td>
</tr>
<tr>
<td>Segmentversion:</td>
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


#### E.2.1.4Anzeigen der verfügbaren TAN-Medien, Segmentversion #4

Bei Segmentversion #4 wird gegenüber der Vorgängerversion in der Kundennach-
richt durch das Datenelement ,,TAN-Medium-Klasse #3" die Selektion nach Sicher-
heitsverfahren wie z. B. chipTAN bzw. mobileTAN ermöglicht.

Realisierung Bank: optional

Realisierung Kunde: optional

<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: D</td>
<td>Version: 3.0-FV</td>
<td>Financial Transaction Services (FinTS) Dokument: Security - Sicherheitsverfahren PIN/TAN</td>
</tr>
<tr>
<td>Seite: 182</td>
<td>Stand: 23.02.2018</td>
<td>Kapitel: Archiv: Ältere Segmentversionen<br>Abschnitt: Management chipTAN, mobileTAN und bilaterale Verfahren</td>
</tr>
</table>


# a) Kundenauftrag


## Format


<table>
<tr>
<td>Name:</td>
<td>TAN-Generator/Liste anzeigen Bestand</td>
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
<td>HKTAB</td>
</tr>
<tr>
<td>Bezugssegment:</td>
<td>-</td>
</tr>
<tr>
<td>Segmentversion:</td>
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
<td>TAN-Medium-Art</td>
<td>2</td>
<td>DE</td>
<td>code</td>
<td>1</td>
<td>M</td>
<td>1</td>
<td>0, 1, 2</td>
</tr>
<tr>
<td>3</td>
<td>TAN-Medium- Klasse</td>
<td>3</td>
<td>DE</td>
<td>code</td>
<td>1</td>
<td>M</td>
<td>1</td>
<td>A, L, G, M, S</td>
</tr>
</table>


## b) Kreditinstitutsrückmeldung


# Erläuterungen

Es wird ein Datensegment zurückgemeldet.


## ◆ Format


<table>
<tr>
<td>Name:</td>
<td>TAN-Generator/Liste anzeigen Bestand Rückmeldung</td>
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
<td>HITAB</td>
</tr>
<tr>
<td>Bezugssegment:</td>
<td>HKTAB</td>
</tr>
<tr>
<td>Segmentversion:</td>
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
<td>TAN-Einsatzoption</td>
<td>1</td>
<td>DE</td>
<td>code</td>
<td>1</td>
<td>M</td>
<td>1</td>
<td>0, 1, 2</td>
</tr>
<tr>
<td>3</td>
<td>TAN-Medium-Liste</td>
<td>4</td>
<td>DEG</td>
<td></td>
<td></td>
<td>O</td>
<td>.99</td>
<td></td>
</tr>
</table>


## ◆ Belegungsrichtlinien


## TAN-Medium-Liste

Darf nur belegt werden, wenn für den Kunden ein TAN-Medium verfügbar /
nutzbar ist.

Beim mobileTAN-Verfahren (TAN-Medium-Klasse="M") muss entweder das
Datenelement ,,Mobiltelefonnummer“ oder „Mobiltelefonnummer verschleiert“
angegeben werden.


## ◆ Ausgewählte Beispiele für Rückmeldungscodes


<table>
<tr>
<td>Code</td>
<td>Beispiel für Rückmeldungstext</td>
</tr>
<tr>
<td>0020</td>
<td>Auftrag verarbeitet</td>
</tr>
</table>


<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th>Version:</th>
<th rowspan="2">Kapitel: D</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Security - Sicherheitsverfahren PIN/TAN</td>
<td>3.0-FV</td>
</tr>
<tr>
<td>Kapitel:</td>
<td>Archiv: Ältere Segmentversionen</td>
<td>Stand:</td>
<td>Seite:</td>
</tr>
<tr>
<td>Abschnitt:</td>
<td>Management chipTAN, mobileTAN und bilaterale Verfahren</td>
<td>23.02.2018</td>
<td>183</td>
</tr>
</table>


c)
Bankparameterdaten


# Beschreibung

Geschäftsvorfallspezifische Parameter existieren nicht.


## ◆ Format


<table>
<tr>
<td>Name:</td>
<td>TAN-Generator/Liste anzeigen Bestand Parameter</td>
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
<td>HITABS</td>
</tr>
<tr>
<td>Bezugssegment:</td>
<td>HKVVB</td>
</tr>
<tr>
<td>Segmentversion:</td>
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
<td>Kapitel: D</td>
<td>Version: 3.0-FV</td>
<td>Financial Transaction Services (FinTS) Dokument: Security - Sicherheitsverfahren PIN/TAN</td>
</tr>
<tr>
<td>Seite:<br>184</td>
<td>Stand: 23.02.2018</td>
<td>Kapitel: Archiv: Ältere Segmentversionen<br>Abschnitt: Management chipTAN, mobileTAN und bilaterale Verfahren</td>
</tr>
</table>


### E.2.2 TAN-Generator / TAN-Liste an- bzw. ummelden


#### E.2.2.1 TAN-Generator / TAN-Liste an- bzw. ummelden in Segmentversion #1

Mit Hilfe dieses Geschäftsvorfalls kann der Kunde seinem Institut mitteilen, welches
Medium (Chipkarte, TAN-Generator bzw. TAN-Liste) er für die Autorisierung der
Aufträge per TAN verwenden wird.

Welches Medium gerade aktiv ist, kann mit Hilfe des Geschäftsvorfalls „TAN-
Generator / -Liste anzeigen Bestand (HKTAB)" durch den Kunden erfragt werden.

Der Kunde entscheidet selbst, ob er den TAN-Generator oder die aktuelle TAN-Liste
verwenden möchte. Steht ein Kartenwechsel an, so kann der Kunde mit diesem Ge-
schäftsvorfall seine Karte bzw. Folgekarte aktivieren. Kann der Kunde mehrere Kar-
ten verwenden, dann kann mit diesem GV die Ummeldung auf eine andere Karte er-
folgen. Das Kreditinstitut entscheidet selbst, ob dieser GV TAN-pflichtig ist oder
nicht.

Realisierung Bank: optional

Realisierung Kunde: optional


##### a) Kundenauftrag


##### Format


<table>
<tr>
<td>Name:</td>
<td>TAN-Generator an- bzw. ummelden</td>
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
<td>HKTAU</td>
</tr>
<tr>
<td>Bezugssegment:</td>
<td>-</td>
</tr>
<tr>
<td>Segmentversion:</td>
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
<td>TAN-Generator/- Liste</td>
<td>1</td>
<td>DE</td>
<td>an</td>
<td>1</td>
<td>M</td>
<td>1</td>
<td>G, L</td>
</tr>
<tr>
<td>3</td>
<td>Kartennummer</td>
<td>1</td>
<td>DE</td>
<td>id</td>
<td>#</td>
<td>C</td>
<td>1</td>
<td>M: DE ,,TAN-Generator/- Liste“=“G“ N: sonst</td>
</tr>
<tr>
<td>4</td>
<td>Kartenfolgenummer</td>
<td>1</td>
<td>DE</td>
<td>id</td>
<td>#</td>
<td>C</td>
<td>1</td>
<td>M: DE ,,TAN-Generator/- Liste"="G" und DE ,,Eingabe Kartenfolgenummer J/N" (BPD)="J" N: sonst</td>
</tr>
<tr>
<td>5</td>
<td>TAN-Listennummer</td>
<td>1</td>
<td>DE</td>
<td>an</td>
<td>.20</td>
<td>C</td>
<td>1</td>
<td>M: DE ,,TAN-Generator/- Liste"="L" und DE ,,Eingabe TAN-Listennummer J/N" (BPD)="J" O: DE ,,TAN-Generator/- Liste"="L" und DE ,,Eingabe TAN-Listennummer J/N" (BPD)=“N“ N: sonst</td>
</tr>
</table>


<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th>Version:</th>
<th rowspan="2">Kapitel: D</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Security - Sicherheitsverfahren PIN/TAN</td>
<td>3.0-FV</td>
</tr>
<tr>
<td>Kapitel:</td>
<td>Archiv: Ältere Segmentversionen</td>
<td>Stand:</td>
<td rowspan="2">Seite: 185</td>
</tr>
<tr>
<td>Abschnitt:</td>
<td>Management chipTAN, mobileTAN und bilaterale Verfahren</td>
<td>23.02.2018</td>
</tr>
</table>


<table>
<tr>
<td>6</td>
<td>ATC</td>
<td>1</td>
<td>DE</td>
<td>num</td>
<td>..5</td>
<td>C</td>
<td>1</td>
<td>M: DE ,,TAN-Generator/- Liste"="G" und DE ,,Eingabe von ATC und TAN erforder- lich" (BPD)="J" N: sonst</td>
</tr>
<tr>
<td>7</td>
<td>TAN</td>
<td>1</td>
<td>DE</td>
<td>an</td>
<td>.99</td>
<td>C</td>
<td>1</td>
<td>M: DE ,,TAN-Generator/- Liste"="G" und DE ,,Eingabe von ATC und TAN erforder- lich" (BPD)="J" N: sonst</td>
</tr>
</table>


## ◆ Belegungsrichtlinien


### TAN-Listennummer

Wird keine TAN-Listennummer angegeben, so wird die aktuelle / freigeschal-
tete Liste verwendet.


### b) Kreditinstitutsrückmeldung

Format

Allgemeine Kreditinstitutsnachricht ohne Datensegmente


### ◆ Ausgewählte Beispiele für Rückmeldungscodes


<table>
<tr>
<td>Code</td>
<td>Beispiel für Rückmeldungstext</td>
</tr>
<tr>
<td>0020</td>
<td>An- bzw. Ummeldung erfolgreich</td>
</tr>
<tr>
<td>9935</td>
<td>An- bzw. Ummeldung fehlgeschlagen</td>
</tr>
<tr>
<td>9935</td>
<td>Kartennummer unbekannt</td>
</tr>
<tr>
<td>9935</td>
<td>TAN-Listennummer unbekannt</td>
</tr>
<tr>
<td>9935</td>
<td>Karte als TAN-Generator nicht zugelassen – bitte wenden Sie sich an Ihr Institut</td>
</tr>
<tr>
<td>9935</td>
<td>Keine TAN-Liste freigeschaltet</td>
</tr>
</table>


c)
Bankparameterdaten

Format


<table>
<tr>
<td>Name:</td>
<td>TAN-Generator an- bzw. ummelden Parameter</td>
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
<td>HITAUS</td>
</tr>
<tr>
<td>Bezugssegment:</td>
<td>HKVVB</td>
</tr>
<tr>
<td>Segmentversion:</td>
<td>1</td>
</tr>
<tr>
<td>Sender:</td>
<td>Kreditinstitut</td>
</tr>
</table>


<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: D</td>
<td>Version: 3.0-FV</td>
<td>Financial Transaction Services (FinTS) Dokument: Security - Sicherheitsverfahren PIN/TAN</td>
</tr>
<tr>
<td>Seite:<br>186</td>
<td>Stand: 23.02.2018</td>
<td>Kapitel: Archiv: Ältere Segmentversionen<br>Abschnitt: Management chipTAN, mobileTAN und bilaterale Verfahren</td>
</tr>
</table>


#### E.2.2.2TAN-Generator / TAN-Liste an- bzw. ummelden in Segmentversion #2

Mit Hilfe dieses Geschäftsvorfalls kann der Kunde seinem Institut mitteilen, welches
Medium (Chipkarte, TAN-Generator bzw. TAN-Liste) er für die Autorisierung der
Aufträge per TAN verwenden wird.

Welches Medium gerade aktiv ist, kann mit Hilfe des Geschäftsvorfalls „TAN-
Generator / -Liste anzeigen Bestand (HKTAB)“ bzw. für Detailinformationen zur Kar-
te auch ,,Kartenanzeige anfordern (HKAZK)“ durch den Kunden erfragt werden.

Der Kunde entscheidet selbst, ob er den TAN-Generator oder die aktuelle TAN-Liste
verwenden möchte. Steht ein Kartenwechsel an, so kann der Kunde mit diesem Ge-
schäftsvorfall seine Karte bzw. Folgekarte aktivieren. Kann der Kunde mehrere Kar-
ten verwenden, dann kann mit diesem GV die Ummeldung auf eine andere Karte er-
folgen. Das Kreditinstitut entscheidet selbst, ob dieser GV TAN-pflichtig ist oder
nicht.

Realisierung Bank: optional

Realisierung Kunde: optional


##### a) Kundenauftrag


##### Format


<table>
<tr>
<td>Name:</td>
<td>TAN-Generator an- bzw. ummelden</td>
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
<td>HKTAU</td>
</tr>
<tr>
<td>Bezugssegment:</td>
<td>-</td>
</tr>
<tr>
<td>Segmentversion:</td>
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
<td>TAN-Generator/- Liste</td>
<td>1</td>
<td>DE</td>
<td>an</td>
<td>1</td>
<td>M</td>
<td>1</td>
<td>G, L</td>
</tr>
<tr>
<td>3</td>
<td>Kartennummer</td>
<td>1</td>
<td>DE</td>
<td>id</td>
<td>#</td>
<td>C</td>
<td>1</td>
<td>M: DE ,,TAN-Generator/- Liste“=“G“ N: sonst</td>
</tr>
<tr>
<td>4</td>
<td>Kartenfolgenummer</td>
<td>1</td>
<td>DE</td>
<td>id</td>
<td>#</td>
<td>C</td>
<td>1</td>
<td>M: DE ,,TAN-Generator/- Liste"="G" und DE ,,Eingabe Kartenfolgenummer J/N" (BPD)="J" N: sonst</td>
</tr>
<tr>
<td>5</td>
<td>Kartenart</td>
<td>1</td>
<td>DE</td>
<td>num</td>
<td>..2</td>
<td>C</td>
<td>1</td>
<td>O: DE ,,TAN-Generator/- Liste"="G" und DE ,,Eingabe Kartenart zulässig“ (BPD) = „J“<br>N: sonst</td>
</tr>
<tr>
<td>6</td>
<td>Kontoverbindung Auftraggeber</td>
<td>3</td>
<td>DE</td>
<td>ktv</td>
<td>#</td>
<td>C</td>
<td>1</td>
<td>O: DE ,,TAN-Generator/- Liste“=“G“ N: sonst</td>
</tr>
<tr>
<td>7</td>
<td>gültig ab</td>
<td>1</td>
<td>DE</td>
<td>dat</td>
<td>#</td>
<td>C</td>
<td>1</td>
<td>O: DE ,,TAN-Generator/- Liste“=“G“ N: sonst</td>
</tr>
<tr>
<td>8</td>
<td>gültig bis</td>
<td>1</td>
<td>DE</td>
<td>dat</td>
<td>#</td>
<td>C</td>
<td>1</td>
<td>O: DE ,,TAN-Generator/-</td>
</tr>
</table>


<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th>Version:</th>
<th rowspan="2">Kapitel: D</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Security - Sicherheitsverfahren PIN/TAN</td>
<td>3.0-FV</td>
</tr>
<tr>
<td>Kapitel:</td>
<td>Archiv: Ältere Segmentversionen</td>
<td>Stand:</td>
<td>Seite:</td>
</tr>
<tr>
<td>Abschnitt:</td>
<td>Management chipTAN, mobileTAN und bilaterale Verfahren</td>
<td>23.02.2018</td>
<td>187</td>
</tr>
</table>


<table>
<tr>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Liste"="G" N: sonst</td>
</tr>
<tr>
<td>9</td>
<td>TAN-Listennummer</td>
<td>1</td>
<td>DE</td>
<td>an</td>
<td>..20</td>
<td>C</td>
<td>1</td>
<td>M: DE ,,TAN-Generator/- Liste"="L" und DE ,,Eingabe TAN-Listennummer J/N" (BPD)="J" O: DE ,,TAN-Generator/- Liste"="L" und DE ,,Eingabe TAN-Listennummer J/N" (BPD)=“N“ N: sonst</td>
</tr>
<tr>
<td>10</td>
<td>ATC</td>
<td>1</td>
<td>DE</td>
<td>num</td>
<td>..5</td>
<td>C</td>
<td>1</td>
<td>M: DE ,,TAN-Generator/- Liste"="G" und DE ,,Eingabe von ATC und TAN erforder- lich" (BPD)="J" N: sonst</td>
</tr>
<tr>
<td>11</td>
<td>TAN</td>
<td>1</td>
<td>DE</td>
<td>an</td>
<td>.99</td>
<td>C</td>
<td>1</td>
<td>M: DE ,,TAN-Generator/- Liste"="G" und DE ,,Eingabe von ATC und TAN erforder- lich" (BPD)="J" N: sonst</td>
</tr>
</table>


##### ◆ Belegungsrichtlinien


###### TAN-Listennummer

Wird keine TAN-Listennummer angegeben, so wird die aktuelle / freigeschal-
tete Liste verwendet.


###### Gültig ab, Gültig bis

Die übliche Angabe im Format JJMM muss in diesem Fall auf ein existieren-
des Datumsformat umgesetzt werden (z. B. Gültig bis „9912“ wird umgesetzt
in „19991231“).

Kartenart

Die Eingabe der Kartenart wird über den BPD-Parameter „Eingabe Kartenart
zulässig“ gesteuert. Ist dieser Parameter auf „J“ gesetzt, enthält das BPD-
Segment HITAUS auch die zulässigen Kartenarten.


##### b) Kreditinstitutsrückmeldung


# Format

Allgemeine Kreditinstitutsnachricht ohne Datensegmente

Ausgewählte Beispiele für Rückmeldungscodes


<table>
<tr>
<td>Code</td>
<td>Beispiel für Rückmeldungstext</td>
</tr>
<tr>
<td>0020</td>
<td>An- bzw. Ummeldung erfolgreich</td>
</tr>
<tr>
<td>9935</td>
<td>An- bzw. Ummeldung fehlgeschlagen</td>
</tr>
<tr>
<td>9935</td>
<td>Kartennummer unbekannt</td>
</tr>
<tr>
<td>9935</td>
<td>TAN-Listennummer unbekannt</td>
</tr>
<tr>
<td>9935</td>
<td>Karte als TAN-Generator nicht zugelassen – bitte wenden Sie sich an Ihr Institut</td>
</tr>
<tr>
<td>9935</td>
<td>Keine TAN-Liste freigeschaltet</td>
</tr>
</table>


<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: D</td>
<td>Version: 3.0-FV</td>
<td>Financial Transaction Services (FinTS) Dokument: Security - Sicherheitsverfahren PIN/TAN</td>
</tr>
<tr>
<td>Seite:<br>188</td>
<td>Stand: 23.02.2018</td>
<td>Kapitel: Archiv: Ältere Segmentversionen<br>Abschnitt: Management chipTAN, mobileTAN und bilaterale Verfahren</td>
</tr>
</table>


## c) Bankparameterdaten

Format


<table>
<tr>
<td>Name:</td>
<td>TAN-Generator an- bzw. ummelden Parameter</td>
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
<td>HITAUS</td>
</tr>
<tr>
<td>Bezugssegment:</td>
<td>HKVVB</td>
</tr>
<tr>
<td>Segmentversion:</td>
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
<td>Parameter TAN- Generator An- bzw. Ummelden</td>
<td>2</td>
<td>DEG</td>
<td></td>
<td></td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
</table>


### E.2.3 Verwalten von Mobilfunkverbindungen


#### E.2.3.1 Mobilfunkverbindung registrieren


#### E.2.3.1.1 Mobilfunkverbindung registrieren in Segmentversion #1

Mit Hilfe dieses Geschäftsvorfalls kann ein Kunde sein Mobilfunkverbindung regist-
rieren.


![](figures/188.1)


![](figures/188.2)


Dieser Geschäftsvorfall kann auch mit der Segmentkennung
HKMTS verwendet werden. Damit ist es möglich, den Geschäftsvor-
fall mit unterschiedlicher Belegung des Parameters ,,Abbuchungs-
konto erforderlich“ in der BPD zur Verfügung zu stellen und damit
über die UPD eine kundenspezifische Abrechnung der SMS-Kosten
zu erreichen.

Realisierung Bank: optional

Realisierung Kunde: optional

<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th>Version:</th>
<th rowspan="2">Kapitel: D</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Security - Sicherheitsverfahren PIN/TAN</td>
<td>3.0-FV</td>
</tr>
<tr>
<td>Kapitel:</td>
<td>Archiv: Ältere Segmentversionen</td>
<td>Stand:</td>
<td>Seite:</td>
</tr>
<tr>
<td>Abschnitt:</td>
<td>Management chipTAN, mobileTAN und bilaterale Verfahren</td>
<td>23.02.2018</td>
<td>189</td>
</tr>
</table>


## a) Kundenauftrag


### Format


<table>
<tr>
<td>Name:</td>
<td>Mobilfunkverbindung registrieren</td>
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
<td>HKMTR</td>
</tr>
<tr>
<td>Bezugssegment:</td>
<td>-</td>
</tr>
<tr>
<td>Segmentversion:</td>
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
<td>Mobiltelefonnum- mer</td>
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
<td>Bezeichnung des TAN-Mediums</td>
<td>1</td>
<td>DE</td>
<td>an</td>
<td>..32</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>4</td>
<td>SMS- Abbuchungskonto</td>
<td>1</td>
<td>DEG</td>
<td>kti</td>
<td>#</td>
<td>C</td>
<td>1</td>
<td>M: DE „SMS- Abbuchungskonto erforder- lich J/N" (BPD)="J" O: sonst</td>
</tr>
</table>


# ◆ Belegungsrichtlinien


## Mobiltelefonnummer

Es muss die Mobiltelefonnummer verwendet werden, die mit dem Institut für
die Nutzung von mobileTAN vereinbart ist. Es sind nur Ziffern inklusive füh-
render Nullen erlaubt und es gilt die nationale Schreibweise für Telefonnum-
mern, z. B. 0170/1234567 oder (0170) 1234567.


![](figures/189.1)


Das Kundensystem sollte den Kunden bei der Eingabe eines kor-
rekten Telefonnummern-Formates unterstützen.


![](figures/189.2)


Falls der Prozess vorsieht, dass die Registrierung der Mobiltelefon-
nummer zuvor auf alternativem Weg erfolgen muss, können nur im
Vorfeld vereinbarte Rufnummern verwendet werden. Das Institut
muss in diesem Fall die Existenz einer entsprechenden Vereinba-
rung prüfen.


## b) Kreditinstitutsrückmeldung


## ◆ Erläuterungen

Es werden keine Datensegmente zurückgemeldet.

◆ Ausgewählte Beispiele für Rückmeldungscodes


<table>
<tr>
<td>Code</td>
<td>Beispiel für Rückmeldungstext</td>
</tr>
<tr>
<td>0020</td>
<td>Auftrag verarbeitet</td>
</tr>
</table>


<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: D</td>
<td>Version: 3.0-FV</td>
<td>Financial Transaction Services (FinTS) Dokument: Security - Sicherheitsverfahren PIN/TAN</td>
</tr>
<tr>
<td>Seite:<br>190</td>
<td>Stand: 23.02.2018</td>
<td>Kapitel: Archiv: Ältere Segmentversionen<br>Abschnitt: Management chipTAN, mobileTAN und bilaterale Verfahren</td>
</tr>
</table>


<table>
<tr>
<td>Code</td>
<td>Beispiel für Rückmeldungstext</td>
</tr>
<tr>
<td>9939</td>
<td>MobileTAN-Mobilrufnummer nicht zur Registrierung zugelassen</td>
</tr>
<tr>
<td>9939</td>
<td>Format der mobileTAN-Mobilrufnummer nicht korrekt</td>
</tr>
<tr>
<td>9939</td>
<td>MobileTAN-Mobilrufnummer bereits registriert</td>
</tr>
</table>


# c) Bankparameterdaten

Format


<table>
<tr>
<td>Name:</td>
<td>Mobilfunkverbindung registrieren Parameter</td>
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
<td>HIMTRS</td>
</tr>
<tr>
<td>Bezugssegment:</td>
<td>HKVVB</td>
</tr>
<tr>
<td>Segmentversion:</td>
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
<td>Parameter Mobil- funkverbindung re- gistrieren</td>
<td>1</td>
<td>DEG</td>
<td></td>
<td></td>
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
<td>Security - Sicherheitsverfahren PIN/TAN</td>
<td>3.0-FV</td>
<td>D</td>
</tr>
<tr>
<td>Kapitel:</td>
<td>Archiv: Ältere Segmentversionen</td>
<td>Stand:</td>
<td>Seite:</td>
</tr>
<tr>
<td>Abschnitt:</td>
<td>Management chipTAN, mobileTAN und bilaterale Verfahren</td>
<td>23.02.2018</td>
<td>191</td>
</tr>
</table>


## E.2.3.1.2 Mobilfunkverbindung registrieren in Segmentversion #2

Mit Hilfe dieses Geschäftsvorfalls kann ein Kunde sein Mobilfunkverbindung regist-
rieren.


![](figures/191.1)


![](figures/191.2)


Dieser Geschäftsvorfall kann auch mit der Segmentkennung
HKMTS verwendet werden. Damit ist es möglich, den Geschäftsvor-
fall mit unterschiedlicher Belegung des Parameters „Abbuchungs-
konto erforderlich“ in der BPD zur Verfügung zu stellen und damit
über die UPD eine kundenspezifische Abrechnung der SMS-Kosten
zu erreichen.


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


### a) Kundenauftrag


#### Format


<table>
<tr>
<td>Name:</td>
<td>Mobilfunkverbindung registrieren</td>
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
<td>HKMTR</td>
</tr>
<tr>
<td>Bezugssegment:</td>
<td>-</td>
</tr>
<tr>
<td>Segmentversion:</td>
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
<td>Mobiltelefonnum- mer</td>
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
<td>Bezeichnung des TAN-Mediums</td>
<td>1</td>
<td>DE</td>
<td>an</td>
<td>..32</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>4</td>
<td>SMS- Abbuchungskonto</td>
<td>1</td>
<td>DEG</td>
<td>kti</td>
<td>#</td>
<td>C</td>
<td>1</td>
<td>M: DE „SMS- Abbuchungskonto erforder- lich J/N" (BPD)="J" O: sonst</td>
</tr>
<tr>
<td>5</td>
<td>Kontaktaufnahme durch Kreditinstitut erlaubt</td>
<td>1</td>
<td>DE</td>
<td>jn</td>
<td>#</td>
<td>C</td>
<td>1</td>
<td>M: DE „Zustimmung zur Kontaktaufnahme unter- stützt“ (BPD)=“J“ O: sonst</td>
</tr>
</table>


### ◆ Belegungsrichtlinien

Mobiltelefonnummer

Es muss die Mobiltelefonnummer verwendet werden, die mit dem Institut für
die Nutzung von mobileTAN vereinbart ist. Es sind nur Ziffern inklusive füh-
render Nullen erlaubt und es gilt die nationale Schreibweise für Telefonnum-
mern, z. B. 0170/1234567 oder (0170) 1234567.

<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: D</td>
<td>Version: 3.0-FV</td>
<td>Financial Transaction Services (FinTS) Dokument: Security - Sicherheitsverfahren PIN/TAN</td>
</tr>
<tr>
<td>Seite: 192</td>
<td>Stand: 23.02.2018</td>
<td>Kapitel: Archiv: Ältere Segmentversionen<br>Abschnitt: Management chipTAN, mobileTAN und bilaterale Verfahren</td>
</tr>
</table>


![](figures/192.1)


Das Kundensystem sollte den Kunden bei der Eingabe eines
korrekten Telefonnummern-Formates unterstützen.


![](figures/192.2)


Falls der Prozess vorsieht, dass die Registrierung der Mobilte-
lefonnummer zuvor auf alternativem Weg erfolgen muss, kön-
nen nur im Vorfeld vereinbarte Rufnummern verwendet wer-
den. Das Institut muss in diesem Fall die Existenz einer ent-
sprechenden Vereinbarung prüfen.


## b) Kreditinstitutsrückmeldung


# Erläuterungen

Es werden keine Datensegmente zurückgemeldet.

◆ Ausgewählte Beispiele für Rückmeldungscodes


<table>
<tr>
<td>Code</td>
<td>Beispiel für Rückmeldungstext</td>
</tr>
<tr>
<td>0020</td>
<td>Auftrag verarbeitet</td>
</tr>
<tr>
<td>9939</td>
<td>MobileTAN-Mobilrufnummer nicht zur Registrierung zugelassen</td>
</tr>
<tr>
<td>9939</td>
<td>Format der mobileTAN-Mobilrufnummer nicht korrekt</td>
</tr>
<tr>
<td>9939</td>
<td>MobileTAN-Mobilrufnummer bereits registriert</td>
</tr>
</table>


c)
Bankparameterdaten

Format


<table>
<tr>
<td>Name:</td>
<td>Mobilfunkverbindung registrieren Parameter</td>
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
<td>HIMTRS</td>
</tr>
<tr>
<td>Bezugssegment:</td>
<td>HKVVB</td>
</tr>
<tr>
<td>Segmentversion:</td>
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
<td>Maximale Anzahl Aufträge</td>
<td>1</td>
<td>DE</td>
<td>Num</td>
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
<td>Parameter Mobil- funkverbindung re- gistrieren</td>
<td>2</td>
<td>DEG</td>
<td></td>
<td></td>
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
<th rowspan="2">Kapitel: D</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Security - Sicherheitsverfahren PIN/TAN</td>
<td>3.0-FV</td>
</tr>
<tr>
<td>Kapitel:</td>
<td>Archiv: Ältere Segmentversionen</td>
<td>Stand:</td>
<td>Seite:</td>
</tr>
<tr>
<td>Abschnitt:</td>
<td>Management chipTAN, mobileTAN und bilaterale Verfahren</td>
<td>23.02.2018</td>
<td>193</td>
</tr>
</table>


## E.2.3.2Mobilfunkverbindung freischalten


### E.2.3.2.1 Mobilfunkverbindung freischalten in Segmentversion #1

Mit Hilfe dieses Geschäftsvorfalls kann ein Kunde seine zuvor registrierte Mobil-
funkverbindung freischalten.

Realisierung Bank:
optional

Realisierung Kunde:
optional


# a) Kundenauftrag


# Format


<table>
<tr>
<td>Name:</td>
<td>Mobilfunkverbindung freischalten</td>
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
<td>HKMTF</td>
</tr>
<tr>
<td>Bezugssegment:</td>
<td>-</td>
</tr>
<tr>
<td>Segmentversion:</td>
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
<td>Bezeichnung des TAN-Mediums</td>
<td>1</td>
<td>DE</td>
<td>an</td>
<td>..32</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>3</td>
<td>Freischaltcode</td>
<td>1</td>
<td>DE</td>
<td>an</td>
<td>..8</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
</table>


# b) Kreditinstitutsrückmeldung


# Erläuterungen

Es werden keine Datensegmente zurückgemeldet.


# ◆ Ausgewählte Beispiele für Rückmeldungscodes


<table>
<tr>
<td>Code</td>
<td>Beispiel für Rückmeldungstext</td>
</tr>
<tr>
<td>0020</td>
<td>Mobiltelefon für mobileTAN freigeschaltet</td>
</tr>
<tr>
<td>9939</td>
<td>mobileTAN-Mobilrufnummer kann nicht freigeschaltet werden</td>
</tr>
<tr>
<td>3939</td>
<td>mobileTAN-Freischaltung erforderlich. SMS-Freischaltcode wurde versendet</td>
</tr>
</table>


c)
Bankparameterdaten


# Beschreibung

Geschäftsvorfallspezifische Parameter existieren nicht.


## ◆ Format


<table>
<tr>
<td>Name:</td>
<td>Mobilfunkverbindung freischalten Parameter</td>
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
<td>HIMTFS</td>
</tr>
<tr>
<td>Bezugssegment:</td>
<td>HKVVB</td>
</tr>
<tr>
<td>Segmentversion:</td>
<td>1</td>
</tr>
<tr>
<td>Sender:</td>
<td>Kreditinstitut</td>
</tr>
</table>


<!-- PageBreak -->


<table>
<tr>
<th>Kapitel: D</th>
<th>Version: 3.0-FV</th>
<th>Financial Transaction Services (FinTS) Dokument: Security - Sicherheitsverfahren PIN/TAN</th>
</tr>
<tr>
<td>Seite: 194</td>
<td>Stand: 23.02.2018</td>
<td>Kapitel: Archiv: Ältere Segmentversionen<br>Abschnitt: Management chipTAN, mobileTAN und bilaterale Verfahren</td>
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


### E.2.3.2.2 Mobilfunkverbindung freischalten in Segmentversion #2

Mit Hilfe dieses Geschäftsvorfalls kann ein Kunde seine zuvor registrierte Mobil-
funkverbindung freischalten.

Realisierung Bank:
optional

Realisierung Kunde: optional


# a) Kundenauftrag

Format


<table>
<tr>
<td>Name:</td>
<td>Mobilfunkverbindung freischalten</td>
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
<td>HKMTF</td>
</tr>
<tr>
<td>Bezugssegment:</td>
<td>-</td>
</tr>
<tr>
<td>Segmentversion:</td>
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
<td>Bezeichnung des TAN-Mediums</td>
<td>1</td>
<td>DE</td>
<td>an</td>
<td>..32</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>3</td>
<td>Freischaltcode</td>
<td>2</td>
<td>DE</td>
<td>an</td>
<td>..64</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
</table>


b)
Kreditinstitutsrückmeldung


# Erläuterungen

Es werden keine Datensegmente zurückgemeldet.

◆ Ausgewählte Beispiele für Rückmeldungscodes


<table>
<tr>
<td>Code</td>
<td>Beispiel für Rückmeldungstext</td>
</tr>
<tr>
<td>0020</td>
<td>Mobiltelefon für mobileTAN freigeschaltet</td>
</tr>
<tr>
<td>9939</td>
<td>mobileTAN-Mobilrufnummer kann nicht freigeschaltet werden</td>
</tr>
<tr>
<td>3939</td>
<td>mobileTAN-Freischaltung erforderlich. SMS-Freischaltcode wurde versendet</td>
</tr>
</table>


<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th>Version:</th>
<th rowspan="2">Kapitel: D</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Security - Sicherheitsverfahren PIN/TAN</td>
<td>3.0-FV</td>
</tr>
<tr>
<td>Kapitel:</td>
<td>Archiv: Ältere Segmentversionen</td>
<td>Stand:</td>
<td>Seite:</td>
</tr>
<tr>
<td>Abschnitt:</td>
<td>Management chipTAN, mobileTAN und bilaterale Verfahren</td>
<td>23.02.2018</td>
<td>195</td>
</tr>
</table>


## c) Bankparameterdaten


## Beschreibung

Geschäftsvorfallspezifische Parameter existieren nicht.


### ◆ Format


<table>
<tr>
<td>Name:</td>
<td>Mobilfunkverbindung freischalten Parameter</td>
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
<td>HIMTFS</td>
</tr>
<tr>
<td>Bezugssegment:</td>
<td>HKVVB</td>
</tr>
<tr>
<td>Segmentversion:</td>
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


#### E.2.3.3Mobilfunkverbindung ändern


##### E.2.3.3.1 Mobilfunkverbindung ändern in Segmentversion #1

Mit Hilfe dieses Geschäftsvorfalls kann ein Kunde seine Mobilfunkverbindung bzw.
die damit verbundenen Informationen ändern.


![](figures/195.1)


![](figures/195.2)


Dieser Geschäftsvorfall kann auch mit der Segmentkennung
HKMTB verwendet werden. Damit ist es möglich, den Geschäftsvor-
fall mit unterschiedlicher Belegung des Parameters „Abbuchungs-
konto erforderlich“ in der BPD zur Verfügung zu stellen und damit
über die UPD eine kundenspezifische Abrechnung der SMS-Kosten
zu erreichen.

Realisierung Bank: optional

Realisierung Kunde: optional

<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: D</td>
<td>Version: 3.0-FV</td>
<td>Financial Transaction Services (FinTS) Dokument: Security - Sicherheitsverfahren PIN/TAN</td>
</tr>
<tr>
<td>Seite: 196</td>
<td>Stand: 23.02.2018</td>
<td>Kapitel: Archiv: Ältere Segmentversionen<br>Abschnitt: Management chipTAN, mobileTAN und bilaterale Verfahren</td>
</tr>
</table>


###### a) Kundenauftrag


####### Format


<table>
<tr>
<td>Name:</td>
<td>Mobilfunkverbindung ändern</td>
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
<td>HKMTA</td>
</tr>
<tr>
<td>Bezugssegment:</td>
<td>-</td>
</tr>
<tr>
<td>Segmentversion:</td>
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
<td>Mobiltelefonnum- mer</td>
<td>1</td>
<td>DE</td>
<td>an</td>
<td>..35</td>
<td>O</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>3</td>
<td>Bezeichnung des TAN-Mediums alt</td>
<td>1</td>
<td>DE</td>
<td>an</td>
<td>..32</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>4</td>
<td>Bezeichnung des TAN-Mediums neu</td>
<td>1</td>
<td>DE</td>
<td>an</td>
<td>..32</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>5</td>
<td>SMS- Abbuchungskonto</td>
<td>1</td>
<td>DEG</td>
<td>kti</td>
<td>#</td>
<td>O</td>
<td>1</td>
<td>M: DE „SMS- Abbuchungskonto erforder- lich J/N" (BPD)="J" O: sonst</td>
</tr>
</table>


####### ◆ Belegungsrichtlinien


######## Bezeichnung des TAN-Mediums alt

Es muss die vereinbarte Bezeichnung einer bestehenden und frei geschalte-
ten Mobiltelefonnummer verwendet werden.


######## b) Kreditinstitutsrückmeldung


######## Erläuterungen

Es werden keine Datensegmente zurückgemeldet.


######## ◆ Ausgewählte Beispiele für Rückmeldungscodes


<table>
<tr>
<td>Code</td>
<td>Beispiel für Rückmeldungstext</td>
</tr>
<tr>
<td>0020</td>
<td>Auftrag verarbeitet</td>
</tr>
<tr>
<td>9939</td>
<td>MobileTAN-Mobilrufnummer nicht zur Registrierung zugelassen</td>
</tr>
<tr>
<td>9939</td>
<td>Format der mobileTAN-Mobilrufnummer nicht korrekt</td>
</tr>
<tr>
<td>9939</td>
<td>MobileTAN-Mobilrufnummer bereits registriert</td>
</tr>
<tr>
<td>9939</td>
<td>alte mobileTAN-Mobilfunknummer existiert nicht oder ist nicht freigeschaltet</td>
</tr>
</table>


<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th>Version:</th>
<th rowspan="2">Kapitel: D</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Security - Sicherheitsverfahren PIN/TAN</td>
<td>3.0-FV</td>
</tr>
<tr>
<td>Kapitel:</td>
<td>Archiv: Ältere Segmentversionen</td>
<td>Stand:</td>
<td>Seite:</td>
</tr>
<tr>
<td>Abschnitt:</td>
<td>Management chipTAN, mobileTAN und bilaterale Verfahren</td>
<td>23.02.2018</td>
<td>197</td>
</tr>
</table>


####### c) Bankparameterdaten

Format


<table>
<tr>
<td>Name:</td>
<td>Mobilfunkverbindung registrieren Parameter</td>
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
<td>HIMTAS</td>
</tr>
<tr>
<td>Bezugssegment:</td>
<td>HKVVB</td>
</tr>
<tr>
<td>Segmentversion:</td>
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
<td>Parameter Mobil- funkverbindung än- dern</td>
<td>1</td>
<td>DEG</td>
<td></td>
<td></td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
</table>


##### E.2.3.3.2 Mobilfunkverbindung ändern in Segmentversion #2

Mit Hilfe dieses Geschäftsvorfalls kann ein Kunde seine Mobilfunkverbindung bzw.
die damit verbundenen Informationen ändern.


![](figures/197.1)


![](figures/197.2)


Dieser Geschäftsvorfall kann auch mit der Segmentkennung
HKMTB verwendet werden. Damit ist es möglich, den Geschäftsvor-
fall mit unterschiedlicher Belegung des Parameters ,,Abbuchungs-
konto erforderlich“ in der BPD zur Verfügung zu stellen und damit
über die UPD eine kundenspezifische Abrechnung der SMS-Kosten
zu erreichen.

Realisierung Bank: optional

Realisierung Kunde: optional

<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: D</td>
<td>Version: 3.0-FV</td>
<td>Financial Transaction Services (FinTS) Dokument: Security - Sicherheitsverfahren PIN/TAN</td>
</tr>
<tr>
<td>Seite: 198</td>
<td>Stand: 23.02.2018</td>
<td>Kapitel: Archiv: Ältere Segmentversionen<br>Abschnitt: Management chipTAN, mobileTAN und bilaterale Verfahren</td>
</tr>
</table>


###### a) Kundenauftrag


####### Format


<table>
<tr>
<td>Name:</td>
<td>Mobilfunkverbindung ändern</td>
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
<td>HKMTA</td>
</tr>
<tr>
<td>Bezugssegment:</td>
<td>-</td>
</tr>
<tr>
<td>Segmentversion:</td>
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
<td>Mobiltelefonnum- mer</td>
<td>1</td>
<td>DE</td>
<td>an</td>
<td>..35</td>
<td>O</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>3</td>
<td>Bezeichnung des TAN-Mediums alt</td>
<td>1</td>
<td>DE</td>
<td>an</td>
<td>..32</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>4</td>
<td>Bezeichnung des TAN-Mediums neu</td>
<td>1</td>
<td>DE</td>
<td>an</td>
<td>..32</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>5</td>
<td>SMS- Abbuchungskonto</td>
<td>1</td>
<td>DEG</td>
<td>kti</td>
<td>#</td>
<td>O</td>
<td>1</td>
<td>M: DE „SMS- Abbuchungskonto erforder- lich J/N" (BPD)="J" O: sonst</td>
</tr>
<tr>
<td>6</td>
<td>Kontaktaufnahme durch Kreditinstitut erlaubt</td>
<td>1</td>
<td>DE</td>
<td>jn</td>
<td>#</td>
<td>C</td>
<td>1</td>
<td>M: DE „Zustimmung zur Kontaktaufnahme unter- stützt“ (BPD)=“J“ O: sonst</td>
</tr>
</table>


####### ◆ Belegungsrichtlinien


######## Bezeichnung des TAN-Mediums alt

Es muss die vereinbarte Bezeichnung einer bestehenden und frei geschalte-
ten Mobiltelefonnummer verwendet werden.


######## b) Kreditinstitutsrückmeldung


######## Erläuterungen

Es werden keine Datensegmente zurückgemeldet.

◆ Ausgewählte Beispiele für Rückmeldungscodes


<table>
<tr>
<td>Code</td>
<td>Beispiel für Rückmeldungstext</td>
</tr>
<tr>
<td>0020</td>
<td>Auftrag verarbeitet</td>
</tr>
<tr>
<td>9939</td>
<td>MobileTAN-Mobilrufnummer nicht zur Registrierung zugelassen</td>
</tr>
<tr>
<td>9939</td>
<td>Format der mobileTAN-Mobilrufnummer nicht korrekt</td>
</tr>
<tr>
<td>9939</td>
<td>MobileTAN-Mobilrufnummer bereits registriert</td>
</tr>
<tr>
<td>9939</td>
<td>alte mobileTAN-Mobilfunknummer existiert nicht oder ist nicht freigeschaltet</td>
</tr>
</table>


<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th>Version:</th>
<th rowspan="2">Kapitel: D</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Security - Sicherheitsverfahren PIN/TAN</td>
<td>3.0-FV</td>
</tr>
<tr>
<td>Kapitel:</td>
<td>Archiv: Ältere Segmentversionen</td>
<td>Stand:</td>
<td>Seite:</td>
</tr>
<tr>
<td>Abschnitt:</td>
<td>Management chipTAN, mobileTAN und bilaterale Verfahren</td>
<td>23.02.2018</td>
<td>199</td>
</tr>
</table>


####### c) Bankparameterdaten


######## Format


<table>
<tr>
<td>Name:</td>
<td>Mobilfunkverbindung registrieren Parameter</td>
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
<td>HIMTAS</td>
</tr>
<tr>
<td>Bezugssegment:</td>
<td>HKVVB</td>
</tr>
<tr>
<td>Segmentversion:</td>
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
<td>Parameter Mobil- funkverbindung än- dern</td>
<td>2</td>
<td>DEG</td>
<td></td>
<td></td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
</table>


######### E.2.3.4Deaktivieren / Löschen von TAN-Medien


########## E.2.3.4.1 Deaktivieren / Löschen von TAN-Medien, Segmentversion #1

Mit Hilfe dieses Geschäftsvorfalls kann ein Kunde ein aktives bzw. verfügbares
TAN-Medium deaktivieren oder löschen.

Deaktivieren, bewirkt eine Statusänderung von „aktiv“ nach „verfügbar“ für das ge-
wählte TAN-Medium.

Beim Löschvorgang wird das entsprechende TAN-Medium gänzlich von der Liste
der TAN-Medien genommen. Dieser Vorgang kann nicht mehr rückgängig gemacht
werden.

Realisierung Bank: optional

Realisierung Kunde: optional

<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: D</td>
<td>Version: 3.0-FV</td>
<td>Financial Transaction Services (FinTS) Dokument: Security - Sicherheitsverfahren PIN/TAN</td>
</tr>
<tr>
<td>Seite: 200</td>
<td>Stand: 23.02.2018</td>
<td>Kapitel: Archiv: Ältere Segmentversionen<br>Abschnitt: Management chipTAN, mobileTAN und bilaterale Verfahren</td>
</tr>
</table>


####### a) Kundenauftrag


######## Format


<table>
<tr>
<td>Name:</td>
<td>TAN-Medium deaktivieren oder löschen</td>
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
<td>HKTML</td>
</tr>
<tr>
<td>Bezugssegment:</td>
<td>-</td>
</tr>
<tr>
<td>Segmentversion:</td>
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
<td>TAN-Medium- Klasse</td>
<td>1</td>
<td>DE</td>
<td>code</td>
<td>1</td>
<td>M</td>
<td>1</td>
<td>L, G, M</td>
</tr>
<tr>
<td>3</td>
<td>TAN-Listennummer</td>
<td>1</td>
<td>DE</td>
<td>an</td>
<td>..20</td>
<td>C</td>
<td>1</td>
<td>M: DE „TAN-Medium- Klasse“=“L“ N: sonst</td>
</tr>
<tr>
<td>4</td>
<td>Bezeichnung des TAN-Mediums</td>
<td>1</td>
<td>DE</td>
<td>an</td>
<td>..32</td>
<td>C</td>
<td>1</td>
<td>M: DE „TAN-Medium- Klasse“=“M“ N: sonst</td>
</tr>
<tr>
<td>5</td>
<td>Deaktivie- ren/Löschen</td>
<td>1</td>
<td>DE</td>
<td>code</td>
<td>1</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
</table>


### ◆ Belegungsrichtlinien


#### TAN-Medium-Klasse

Es muss die zu deaktivierende / zu löschende TAN-Medium-Klasse angege-
ben werden. Bei Angabe von TAN-Medium-Klasse"G" wird die als aktiv defi-
nierte Kombination aus TAN-Generator und Karte gelöscht bzw. deaktiviert.
Bei TAN-Medium-Klasse="L" oder ,M" muss die Angabe der TAN-
Listennummer bzw. der Bezeichnung des TAN-Mediums erfolgen.


![](figures/200.1)


Das Kundensystem sollte den Kunden darauf hinweisen,
wenn er versuchen will, das letzte im Bestand des Kunden-
systems bekannte TAN-Medium zu deaktivieren oder zu lö-
schen.


#### b) Kreditinstitutsrückmeldung


## Erläuterungen

Es werden keine Datensegmente zurückgemeldet.

<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th>Version:</th>
<th rowspan="2">Kapitel: D</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Security - Sicherheitsverfahren PIN/TAN</td>
<td>3.0-FV</td>
</tr>
<tr>
<td>Kapitel:</td>
<td>Archiv: Ältere Segmentversionen</td>
<td>Stand:</td>
<td>Seite:</td>
</tr>
<tr>
<td>Abschnitt:</td>
<td>Management chipTAN, mobileTAN und bilaterale Verfahren</td>
<td>23.02.2018</td>
<td>201</td>
</tr>
</table>


## ◆ Ausgewählte Beispiele für Rückmeldungscodes


<table>
<tr>
<td>Code</td>
<td>Beispiel für Rückmeldungstext</td>
</tr>
<tr>
<td>0020</td>
<td>Auftrag verarbeitet</td>
</tr>
<tr>
<td>9958</td>
<td>Deaktivieren / Löschen für TAN-Medium nicht möglich</td>
</tr>
<tr>
<td>9958</td>
<td>TAN-Medium nicht bekannt</td>
</tr>
</table>


## c) Bankparameterdaten


## Beschreibung

Geschäftsvorfallspezifische Parameter existieren nicht.


# ◆ Format


<table>
<tr>
<td>Name:</td>
<td>TAN-Medium deaktivieren oder löschen Parameter</td>
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
<td>HITMLS</td>
</tr>
<tr>
<td>Bezugssegment:</td>
<td>HKVVB</td>
</tr>
<tr>
<td>Segmentversion:</td>
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


## E.2.4 TAN-Verbrauchsinformationen anzeigen

Dieses Segment bewirkt die Anzeige der verbrauchten TANs des Kunden.


### E.2.4.1 TAN-Verbrauchsinformationen anzeigen, Segmentversion #1

Realisierung Bank:
optional

Realisierung Kunde: optional


### a) Kundenauftrag


### Beschreibung

Das Auftragssegment enthält neben dem Segmentkopf keine weiteren Daten.

<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: D</td>
<td>Version: 3.0-FV</td>
<td>Financial Transaction Services (FinTS) Dokument: Security - Sicherheitsverfahren PIN/TAN</td>
</tr>
<tr>
<td>Seite:<br>202</td>
<td>Stand: 23.02.2018</td>
<td>Kapitel: Archiv: Ältere Segmentversionen<br>Abschnitt: Management chipTAN, mobileTAN und bilaterale Verfahren</td>
</tr>
</table>


# ◆ Format


<table>
<tr>
<td>Name:</td>
<td>TAN-Verbrauchsinformationen anfordern</td>
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
<td>HKTAZ</td>
</tr>
<tr>
<td>Bezugssegment:</td>
<td>-</td>
</tr>
<tr>
<td>Segmentversion:</td>
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


b)
Kreditinstitutsrückmeldung


# Beschreibung

Je zurück zu meldender TAN-Liste ist ein Segment in die Antwortnachricht einzu-
stellen.


# ◆ Format


<table>
<tr>
<td>Name:</td>
<td>TAN-Verbrauchsinformationen rückmelden</td>
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
<td>HITAZ</td>
</tr>
<tr>
<td>Bezugssegment:</td>
<td>HKTAZ</td>
</tr>
<tr>
<td>Segmentversion:</td>
<td>1</td>
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
<th>Version:</th>
<th>Kapitel:</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Security - Sicherheitsverfahren PIN/TAN</td>
<td>3.0-FV</td>
<td>D</td>
</tr>
<tr>
<td>Kapitel:</td>
<td>Archiv: Ältere Segmentversionen</td>
<td>Stand:</td>
<td>Seite:</td>
</tr>
<tr>
<td>Abschnitt:</td>
<td>Management chipTAN, mobileTAN und bilaterale Verfahren</td>
<td>23.02.2018</td>
<td>203</td>
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
<td>TAN-Listenstatus</td>
<td>1</td>
<td>DE</td>
<td>code</td>
<td>1</td>
<td>M</td>
<td>1</td>
<td>A, N, S, V</td>
</tr>
<tr>
<td>3</td>
<td>TAN-Listennummer</td>
<td>1</td>
<td>DE</td>
<td>an</td>
<td>..20</td>
<td>M</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>4</td>
<td>Erstellungsdatum</td>
<td>1</td>
<td>DE</td>
<td>dat</td>
<td>#</td>
<td>O</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>5</td>
<td>Anzahl TANs pro Liste</td>
<td>1</td>
<td>DE</td>
<td>num</td>
<td>..4</td>
<td>O</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>6</td>
<td>Anzahl verbrauchter TANs pro Liste</td>
<td>1</td>
<td>DE</td>
<td>num</td>
<td>..4</td>
<td>O</td>
<td>1</td>
<td></td>
</tr>
<tr>
<td>7</td>
<td>TAN-Information</td>
<td>1</td>
<td>DEG</td>
<td></td>
<td></td>
<td>O</td>
<td>999</td>
<td></td>
</tr>
</table>


# ◆ Belegungsrichtlinien

TAN-Listennummer

Kennung der TAN-Liste, die zurückgemeldet wird.


# ◆ Ausgewählte Beispiele für Rückmeldungscodes


<table>
<tr>
<td>Code</td>
<td>Beispiel für Rückmeldungstext</td>
</tr>
<tr>
<td>0020</td>
<td>Auftrag ausgeführt</td>
</tr>
</table>


## c) Bankparameterdaten


## Beschreibung

Geschäftsvorfallspezifische Parameter existieren nicht.


## ◆ Format


<table>
<tr>
<td>Name:</td>
<td>TAN-Verbrauchsinformationen Parameter</td>
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
<td>HITAZS</td>
</tr>
<tr>
<td>Bezugssegment:</td>
<td>HKVVB</td>
</tr>
<tr>
<td>Segmentversion:</td>
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
<td>Anzahl Signaturen minde- stens</td>
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
<td>Kapitel: D</td>
<td>Version: 3.0-FV</td>
<td>Financial Transaction Services (FinTS) Dokument: Security - Sicherheitsverfahren PIN/TAN</td>
</tr>
<tr>
<td>Seite: 204</td>
<td>Stand: 23.02.2018</td>
<td>Kapitel: Anlagen<br>Abschnitt: Übersicht der Segmente</td>
</tr>
</table>


# F. ANLAGEN


## F.1 Übersicht der Segmente


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
<td>Anzeige der Verfügbaren TAN-Medien</td>
<td>HKTAB</td>
<td>K</td>
<td>1</td>
</tr>
<tr>
<td>2</td>
<td>Anzeige der Verfügbaren TAN-Medien</td>
<td>HKTAB</td>
<td>K</td>
<td>2</td>
</tr>
<tr>
<td>3</td>
<td>Anzeige der Verfügbaren TAN-Medien</td>
<td>HKTAB</td>
<td>K</td>
<td>3</td>
</tr>
<tr>
<td>4</td>
<td>Anzeige der Verfügbaren TAN-Medien</td>
<td>HKTAB</td>
<td>K</td>
<td>4</td>
</tr>
<tr>
<td>5</td>
<td>Anzeige der Verfügbaren TAN-Medien</td>
<td>HKTAB</td>
<td>K</td>
<td>5</td>
</tr>
<tr>
<td>6</td>
<td>Anzeige der Verfügbaren TAN-Medien Parameter</td>
<td>HITABS</td>
<td>I</td>
<td>1</td>
</tr>
<tr>
<td>7</td>
<td>Anzeige der Verfügbaren TAN-Medien Parameter</td>
<td>HITABS</td>
<td>I</td>
<td>2</td>
</tr>
<tr>
<td>8</td>
<td>Anzeige der Verfügbaren TAN-Medien Parameter</td>
<td>HITABS</td>
<td>I</td>
<td>3</td>
</tr>
<tr>
<td>9</td>
<td>Anzeige der Verfügbaren TAN-Medien Parameter</td>
<td>HITABS</td>
<td>I</td>
<td>4</td>
</tr>
<tr>
<td>10</td>
<td>Anzeige der Verfügbaren TAN-Medien Parameter</td>
<td>HITABS</td>
<td>I</td>
<td>5</td>
</tr>
<tr>
<td>11</td>
<td>Anzeige der Verfügbaren TAN-Medien rückmelden</td>
<td>HITAB</td>
<td>I</td>
<td>1</td>
</tr>
<tr>
<td>12</td>
<td>Anzeige der Verfügbaren TAN-Medien rückmelden</td>
<td>HITAB</td>
<td>I</td>
<td>2</td>
</tr>
<tr>
<td>13</td>
<td>Anzeige der Verfügbaren TAN-Medien rückmelden</td>
<td>HITAB</td>
<td>I</td>
<td>3</td>
</tr>
<tr>
<td>14</td>
<td>Anzeige der Verfügbaren TAN-Medien rückmelden</td>
<td>HITAB</td>
<td>I</td>
<td>4</td>
</tr>
<tr>
<td>15</td>
<td>Anzeige der Verfügbaren TAN-Medien rückmelden</td>
<td>HITAB</td>
<td>I</td>
<td>5</td>
</tr>
<tr>
<td>16</td>
<td>HHD- / Secoder-Informationen übermitteln</td>
<td>HKHSI</td>
<td>K</td>
<td>1</td>
</tr>
<tr>
<td>17</td>
<td>HHD- / Secoder-Informationen Parameter</td>
<td>HIHSIS</td>
<td>I</td>
<td>1</td>
</tr>
<tr>
<td>18</td>
<td>HHD- / Secoder-Informationen rückmelden</td>
<td>HIHSI</td>
<td>I</td>
<td>1</td>
</tr>
<tr>
<td>19</td>
<td>Mobilfunkverbindung ändern</td>
<td>HKMTA</td>
<td>K</td>
<td>1</td>
</tr>
<tr>
<td>20</td>
<td>Mobilfunkverbindung ändern</td>
<td>HKMTA</td>
<td>K</td>
<td>2</td>
</tr>
<tr>
<td>21</td>
<td>Mobilfunkverbindung ändern</td>
<td>HKMTA</td>
<td>K</td>
<td>3</td>
</tr>
<tr>
<td>22</td>
<td>Mobilfunkverbindung ändern Parameter</td>
<td>HIMTAS</td>
<td>I</td>
<td>1</td>
</tr>
<tr>
<td>23</td>
<td>Mobilfunkverbindung ändern Parameter</td>
<td>HIMTAS</td>
<td>I</td>
<td>2</td>
</tr>
<tr>
<td>24</td>
<td>Mobilfunkverbindung ändern Parameter</td>
<td>HIMTAS</td>
<td>I</td>
<td>3</td>
</tr>
<tr>
<td>25</td>
<td>Mobilfunkverbindung freischalten</td>
<td>HKMTF</td>
<td>K</td>
<td>1</td>
</tr>
<tr>
<td>26</td>
<td>Mobilfunkverbindung freischalten</td>
<td>HKMTF</td>
<td>K</td>
<td>2</td>
</tr>
<tr>
<td>27</td>
<td>Mobilfunkverbindung freischalten</td>
<td>HKMTF</td>
<td>K</td>
<td>3</td>
</tr>
<tr>
<td>28</td>
<td>Mobilfunkverbindung freischalten Parameter</td>
<td>HIMTFS</td>
<td>I</td>
<td>1</td>
</tr>
<tr>
<td>29</td>
<td>Mobilfunkverbindung freischalten Parameter</td>
<td>HIMTFS</td>
<td>I</td>
<td>2</td>
</tr>
<tr>
<td>30</td>
<td>Mobilfunkverbindung freischalten Parameter</td>
<td>HIMTFS</td>
<td>I</td>
<td>3</td>
</tr>
<tr>
<td>31</td>
<td>Deaktivieren/Löschen von TAN-Medien</td>
<td>HKTML</td>
<td>K</td>
<td>1</td>
</tr>
<tr>
<td>32</td>
<td>Deaktivieren/Löschen von TAN-Medien</td>
<td>HKTML</td>
<td>K</td>
<td>2</td>
</tr>
<tr>
<td>33</td>
<td>Mobilfunkverbindung löschen Parameter</td>
<td>HIMTLS</td>
<td>I</td>
<td>1</td>
</tr>
<tr>
<td>34</td>
<td>Mobilfunkverbindung löschen Parameter</td>
<td>HIMTLS</td>
<td>I</td>
<td>2</td>
</tr>
<tr>
<td>35</td>
<td>Mobilfunkverbindung registrieren</td>
<td>HKMTR</td>
<td>K</td>
<td>1</td>
</tr>
<tr>
<td>36</td>
<td>Mobilfunkverbindung registrieren</td>
<td>HKMTR</td>
<td>K</td>
<td>2</td>
</tr>
<tr>
<td>37</td>
<td>Mobilfunkverbindung registrieren</td>
<td>HKMTR</td>
<td>K</td>
<td>3</td>
</tr>
<tr>
<td>38</td>
<td>Mobilfunkverbindung registrieren Parameter</td>
<td>HIMTRS</td>
<td>I</td>
<td>1</td>
</tr>
<tr>
<td>39</td>
<td>Mobilfunkverbindung registrieren Parameter</td>
<td>HIMTRS</td>
<td>I</td>
<td>2</td>
</tr>
</table>

1
K: Kunde, I: Kreditinstitut


<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th>Version:</th>
<th rowspan="2">Kapitel: D</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Security - Sicherheitsverfahren PIN/TAN</td>
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
<td>Übersicht der Segmente</td>
<td>23.02.2018</td>
<td>205</td>
</tr>
</table>


<table>
<tr>
<th>Nr.</th>
<th>Segmentname</th>
<th>Kennung</th>
<th>Sen- der1</th>
<th>Version</th>
</tr>
<tr>
<td>40</td>
<td>Mobilfunkverbindung registrieren Parameter</td>
<td>HIMTRS</td>
<td>I</td>
<td>3</td>
</tr>
<tr>
<td>41</td>
<td>PIN ändern</td>
<td>HKPAE</td>
<td>K</td>
<td>1</td>
</tr>
<tr>
<td>42</td>
<td>PIN ändern Parameter</td>
<td>HIPAES</td>
<td>I</td>
<td>1</td>
</tr>
<tr>
<td>43</td>
<td>PIN sperren</td>
<td>HKPSP</td>
<td>K</td>
<td>1</td>
</tr>
<tr>
<td>44</td>
<td>PIN sperren Parameter</td>
<td>HIPSPS</td>
<td>I</td>
<td>1</td>
</tr>
<tr>
<td>45</td>
<td>PIN-Sperre aufheben</td>
<td>HKPSA</td>
<td>K</td>
<td>1</td>
</tr>
<tr>
<td>46</td>
<td>PIN-Sperre aufheben Parameter</td>
<td>HIPSAS</td>
<td>I</td>
<td>1</td>
</tr>
<tr>
<td>47</td>
<td>PIN/TAN-spezifische Informationen</td>
<td>HIPINS</td>
<td>I</td>
<td>1</td>
</tr>
<tr>
<td>48</td>
<td>TAN-Generator an- bzw. ummelden</td>
<td>HKTAU</td>
<td>K</td>
<td>1</td>
</tr>
<tr>
<td>49</td>
<td>TAN-Generator an- bzw. ummelden</td>
<td>HKTAU</td>
<td>K</td>
<td>2</td>
</tr>
<tr>
<td>50</td>
<td>TAN-Medium an- bzw. ummelden</td>
<td>HKTAU</td>
<td>K</td>
<td>3</td>
</tr>
<tr>
<td>51</td>
<td>TAN-Generator an- bzw. ummelden Parameter</td>
<td>HITAUS</td>
<td>I</td>
<td>1</td>
</tr>
<tr>
<td>52</td>
<td>TAN-Generator an- bzw. ummelden Parameter</td>
<td>HITAUS</td>
<td>I</td>
<td>2</td>
</tr>
<tr>
<td>53</td>
<td>TAN-Medium an- bzw. ummelden Parameter</td>
<td>HITAUS</td>
<td>I</td>
<td>3</td>
</tr>
<tr>
<td>54</td>
<td>TAN-Generator Synchronisierung</td>
<td>HKTSY</td>
<td>K</td>
<td>1</td>
</tr>
<tr>
<td>55</td>
<td>TAN-Generator Synchronisierung Parameter</td>
<td>HITSYS</td>
<td>I</td>
<td>1</td>
</tr>
<tr>
<td>56</td>
<td>TAN-Verbrauchsinformationen anfordern</td>
<td>HKTAZ</td>
<td>K</td>
<td>1</td>
</tr>
<tr>
<td>57</td>
<td>TAN-Verbrauchsinformationen anfordern</td>
<td>HKTAZ</td>
<td>K</td>
<td>2</td>
</tr>
<tr>
<td>58</td>
<td>TAN-Verbrauchsinformationen Parameter</td>
<td>HITAZS</td>
<td>I</td>
<td>1</td>
</tr>
<tr>
<td>59</td>
<td>TAN-Verbrauchsinformationen Parameter</td>
<td>HITAZS</td>
<td>I</td>
<td>2</td>
</tr>
<tr>
<td>60</td>
<td>TAN-Verbrauchsinformationen rückmelden</td>
<td>HITAZ</td>
<td>I</td>
<td>1</td>
</tr>
<tr>
<td>61</td>
<td>TAN-Verbrauchsinformationen rückmelden</td>
<td>HITAZ</td>
<td>I</td>
<td>2</td>
</tr>
<tr>
<td>62</td>
<td>Zwei-Schritt-TAN Einreichung</td>
<td>HKTAN</td>
<td>K</td>
<td>1</td>
</tr>
<tr>
<td>63</td>
<td>Zwei-Schritt-TAN Einreichung</td>
<td>HKTAN</td>
<td>K</td>
<td>2</td>
</tr>
<tr>
<td>64</td>
<td>Zwei-Schritt-TAN Einreichung</td>
<td>HKTAN</td>
<td>K</td>
<td>3</td>
</tr>
<tr>
<td>65</td>
<td>Zwei-Schritt-TAN Einreichung</td>
<td>HKTAN</td>
<td>K</td>
<td>4</td>
</tr>
<tr>
<td>66</td>
<td>Zwei-Schritt-TAN Einreichung</td>
<td>HKTAN</td>
<td>K</td>
<td>5</td>
</tr>
<tr>
<td>67</td>
<td>Zwei-Schritt-TAN Einreichung</td>
<td>HKTAN</td>
<td>K</td>
<td>6</td>
</tr>
<tr>
<td>68</td>
<td>Zwei-Schritt-TAN Einreichung Parameter</td>
<td>HITANS</td>
<td>I</td>
<td>1</td>
</tr>
<tr>
<td>69</td>
<td>Zwei-Schritt-TAN Einreichung Parameter</td>
<td>HITANS</td>
<td>I</td>
<td>2</td>
</tr>
<tr>
<td>70</td>
<td>Zwei-Schritt-TAN Einreichung Parameter</td>
<td>HITANS</td>
<td>I</td>
<td>3</td>
</tr>
<tr>
<td>71</td>
<td>Zwei-Schritt-TAN Einreichung Parameter</td>
<td>HITANS</td>
<td>I</td>
<td>4</td>
</tr>
<tr>
<td>72</td>
<td>Zwei-Schritt-TAN Einreichung Parameter</td>
<td>HITANS</td>
<td>I</td>
<td>5</td>
</tr>
<tr>
<td>73</td>
<td>Zwei-Schritt-TAN Einreichung Parameter</td>
<td>HITANS</td>
<td>I</td>
<td>6</td>
</tr>
<tr>
<td>74</td>
<td>Zwei-Schritt-TAN Rückmeldung</td>
<td>HITAN</td>
<td>I</td>
<td>1</td>
</tr>
<tr>
<td>75</td>
<td>Zwei-Schritt-TAN Rückmeldung</td>
<td>HITAN</td>
<td>I</td>
<td>2</td>
</tr>
<tr>
<td>76</td>
<td>Zwei-Schritt-TAN Rückmeldung</td>
<td>HITAN</td>
<td>I</td>
<td>3</td>
</tr>
<tr>
<td>77</td>
<td>Zwei-Schritt-TAN Rückmeldung</td>
<td>HITAN</td>
<td>I</td>
<td>4</td>
</tr>
<tr>
<td>78</td>
<td>Zwei-Schritt-TAN Rückmeldung</td>
<td>HITAN</td>
<td>I</td>
<td>5</td>
</tr>
<tr>
<td>79</td>
<td>Zwei-Schritt-TAN Rückmeldung</td>
<td>HITAN</td>
<td>I</td>
<td>6</td>
</tr>
</table>


<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: D</td>
<td>Version: 3.0-FV</td>
<td>Financial Transaction Services (FinTS) Dokument: Security - Sicherheitsverfahren PIN/TAN</td>
</tr>
<tr>
<td>Seite: 206</td>
<td>Stand: 23.02.2018</td>
<td>Kapitel: Anlagen<br>Abschnitt: Übersicht Nachrichtenaufbau</td>
</tr>
</table>


## F.2 Übersicht Nachrichtenaufbau


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
<td>2<br>...</td>
<td>-</td>
<td>0-n</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HIPINS</td>
<td>-</td>
<td>1</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HITANS</td>
<td>-</td>
<td>0-1</td>
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
<td>HKSAL3<br>3</td>
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
<td>HKTAN</td>
<td>0-1</td>
<td>-</td>
<td>0-14</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>HITAN</td>
<td>-</td>
<td>0-1</td>
<td>-</td>
<td>0-1</td>
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

2
Hier sind für die weiteren unterstützten Geschäftsvorfälle die entsprechenden Parameter-Segmente
einzustellen.

3
Exemplarisch wird hier der Geschäftsvorfall „Saldenabfrage“ angenommen.

4
HKTAN kann mit anderen, nicht TAN-pflichtigen Aufträgen in einer Nachricht kombiniert werden.


<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th>Version:</th>
<th>Kapitel:</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Security - Sicherheitsverfahren PIN/TAN</td>
<td>3.0-FV</td>
<td>D</td>
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
<td>23.02.2018</td>
<td>207</td>
</tr>
</table>


### F.2.1 Beispieldialog im Ein-Schritt-Verfahren

Das Beispiel entspricht dem Beispiel in [Formals] mit dem Unterschied, dass der
Kunde PIN/TAN im Ein-Schritt-Verfahren als Sicherheitsverfahren einsetzt. Abwei-
chungen sind fettgedruckt.


### F.2.2 Nachricht ,,Dialoginitialisierung"


#### a) Kundennachricht5

HNHBK:1:3+000000000323+300+0+1'

HNVSK:998:3+PIN:1+998+1+1::2+1:20020610:102044+2
:2:13:@8@<X'00 00 00 00 00 00 00 00'>:5:1+280:10
020030:12345:V:0:0+0'

HNVSD:999:1+@348@<Daten>'6

HNSHK:2:4+PIN:1+999+654321+1+1+1::2+3234+1:20020
701:111144+1:999:1+6:10:16+280:10020030:12345:S:
0 : 0'

HKIDN:3:2+280:10020030+12345+2+1'

HKVVB:4:2+2+3+1+Onlinebanking Plus+3.0'

HNSHA:5:2+654321++83427'

HNHBS:6:1+1'


## b) Kreditinstitutsnachricht

Der Kunde erhält die aktuellen Bank- und Userparameterdaten, da die dem Kunden
vorliegenden Daten nicht mehr aktuell sind. Das Kreditinstitut unterstützt über
PIN/TAN die Geschäftsvorfälle „SEPA Einzelüberweisung“, „Neue Umsätze“ und
„Saldenabfrage“ sowie zusätzlich „PIN ändern“, „TAN-Liste anfordern" und ,,TAN-
Liste freischalten“.

HNHBK:1:3+000000000932+300+4711+1+4711:1'

HNVSK:998:3+PIN:1+998+1+1::2+1:20020610:102044+2
:2:13:@8@<X'00 00 00 00 00 00 00 00'>:5:1+280:10
020030:12345:V:0:0+0'

HNVSD:999:1+@348@<Daten>'

HIRMG:2:2+0010::Nachricht entgegengenommen '

<!-- PageFooter: 5 Aus Gründen der Übersichtlichkeit beginnen Segmente in diesem Beispiel jeweils in einer neuen Zeile. Dies bedeutet jedoch nicht, dass Segmente syntaktisch mit einem Zeilenvorschub beendet werden. -->
<!-- PageFooter: 6 <Daten> enthält hier und in allen weiteren Nachrichten jeweils alle nachfolgenden Segmente mit Ausnahme des Nachrichtenabschlusses. -->
<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: D</td>
<td>Version: 3.0-FV</td>
<td>Financial Transaction Services (FinTS) Dokument: Security - Sicherheitsverfahren PIN/TAN</td>
</tr>
<tr>
<td>Seite: 208</td>
<td>Stand: 23.02.2018</td>
<td>Kapitel: Anlagen<br>Abschnitt: Übersicht Nachrichtenaufbau</td>
</tr>
</table>


HIBPA:3:2:4+3+280:10020030+Musterbank in Musters
tadt+1+1:2:3+1+100'

HIKOM:4:4:4+280:10020030+1+2:123.123.123.123::UU
E:1+3:https?://www.xyz.de?: 7000/PinTanServlet: :U
UE : 1' 7

HISHV:5:2:4+N+RAH:3:2:1'

HICCSS:6:1:4+1+2+7:51:53:54:67:69'

HICCSS:7:2:4+1+2+14:51:53:54:67:69'

HILASS:8:2:4+1+2+14:04:05'

HISUBS:9:2:4+1+2+999:14:51:53:54'

HISLAS:10:2:4+1+2+99:14:04:05'

HIKAZS:11:2:4+1+2+60:J'

HIKANS:12:2:4+1+2+60:J'

HISALS:13:3:4+1+2'

HIPINS:14:1:4+1+1+5:6:6:Kunden-Nr aus dem TAN-Br

ief : :HKCCS : J:HKKAN:N:HKSAL:J:HKPAE:J:'

HIPAES:15:1:4+1+1'

HIUPA:18:2:4+12345+4+0'

HIUPD:19:4:4+1234567:280:10020030+12345+EUR+Erns
t Müller++Giro Spezial+T:2000, : EUR+HKPRO : 1+HKSAK
:1+HKISA:1+HKSSP:1+HKCCS : 1+HKLAS :1+HKKAN:1+HKKAZ
:1+HKSAL:1+HKPAE:1'

HIUPD:20:4:4+1234568:280:10020030+12345+EUR+Erns
t Müller++Sparkonto 2000++HKPRO: 1+HKSAK:0+HKISA:
1+HKSSP:0+HKCCS:2:Z:1000,: EUR:7+HKKAN:1+HKKAZ:1+
HKSAL:2'

HIKIM:21:2+Bausparförderung+Informieren Sie sich
über die neue Bausparförderung. '

HNHBS:22:1+1'

<!-- PageFooter: 7 Das ,,?" wird zur Entwertung von Syntaxzeichen verwendet (s. [Formals], Kap. G.11) -->
<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th>Version:</th>
<th>Kapitel:</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Security - Sicherheitsverfahren PIN/TAN</td>
<td>3.0-FV</td>
<td>D</td>
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
<td>23.02.2018</td>
<td>209</td>
</tr>
</table>


## F.2.3 Nachricht „SEPA Einzelüberweisung"


### a) Kundennachricht

Diese Nachricht wird sowohl von Benutzer '12345' als auch von Benutzer '76543'
signiert.

HNHBK:1:3+000000000523+300+4711+2'

HNVSK:998:3+PIN:1+998+1+1::2+1:20020610:102044+2
:2:13:@8@<X'00 00 00 00 00 00 00 00'>:5:1+280:10
020030:12345:V:0:0+0'

HNVSD:999:1+@348@<Daten>'

HNSHK:2:4+PIN:1+999+765432+1+1+1::2+3234+1:20020
701:111146+1:999:1+6:10:16+280:10020030:76543: S:
0 : 0 '

HNSHK:3:4+PIN:1+999+654321+1+1+1::2+3234+1:20020
701:111147+1:999:1+6:10:16+280:10020030:12345:S:
0 : 0'

HKCCS:4:2+1234567::280:10020030+7654321::280:200
30040+MEIER FRANZ++1000,:EUR+51+000+RE-NR.1234:K
D-NR. 9876'

HNSHA:5:2+654321++83427:954378'

HNSHA:6:2+765432++22714:528019'

HNHBS:7:1+2'


## b) Kreditinstitutsnachricht

HNHBK:1:3+000000000140+300+4711+2+4711:2'

HNVSK:998:3+PIN:1+998+1+1::2+1:20020610:102044+2
:2:13:@8@<X'00 00 00 00 00 00 00 00'>:5:1+280:10
020030:12345:V:0:0+0'

HNVSD:999:1+@348@<Daten>'

HIRMG:2:2+0010::Nachricht entgegengenommen '

HIRMS:3:2:4+0010::Auftrag entgegengenommen '
HNHBS:4:1+2'

<!-- PageBreak -->


<table>
<tr>
<td>Kapitel: D</td>
<td>Version: 3.0-FV</td>
<td>Financial Transaction Services (FinTS) Dokument: Security - Sicherheitsverfahren PIN/TAN</td>
</tr>
<tr>
<td>Seite:<br>210</td>
<td>Stand: 23.02.2018</td>
<td>Kapitel: Anlagen<br>Abschnitt: Übersicht Nachrichtenaufbau</td>
</tr>
</table>


## F.2.4 Nachricht ,,Saldenabfrage"


### a) Kundennachricht

Die Kundennachricht wird nur von Benutzer '12345' signiert.

HNHBK:1:3+000000000257+300+4711+3'

HNVSK:998:3+PIN:1+998+1+1::2+1:20020610:102044+2
:2:13:@8@<X'00 00 00 00 00 00 00 00'>:5:1+280:10
020030:12345:V:0:0+0'

HNVSD:999:1+@348@<Daten>'

HNSHK:2:4+PIN:1+999+654321+1+1+1::2+3234+1:20020
701:111149+1:999:1+6:10:16+280:10020030:12345: S:
0 : 0'

HKSAL:3:3+1234567::280:10020030+N'

HNSHA:4:2+654321++83427'

HNHBS:5:1+3'


### b) Kreditinstitutsnachricht

HNHBK:1:3+000000000213+300+4711+3+4711:3'

HNVSK:998:3+PIN:1+998+1+1::2+1:20020610:102044+2
:2:13:@8@<X'00 00 00 00 00 00 00 00'>:5:1+280:10
020030:12345:V:0:0+0'

HNVSD:999:1+@348@<Daten>'

HIRMG:2:2+0010::Nachricht entgegengenommen'

HIRMS:3:2:3+0020::Auftrag ausgeführt'

HISAL:4:3:3+1234567::280:10020030+Giro Spezial+E

UR+C:1000, :EUR: 20020701+D:500,:EUR:20020701+5000
, : EUR+7138,35: EUR+1476,98 : EUR'

HNHBS:5:1+3'


## F.2.5 Nachricht ,,Dialogbeendigung“


## a) Kundennachricht

HNHBK:1:3+0000000000475+300+4711+4'

HNVSK:998:3+PIN:1+998+1+1::2+1:20020610:102044+2
:2:13:@8@<X'00 00 00 00 00 00 00 00'>:5:1+280:10
020030:12345:V:0:0+0'

HNVSD:999:1+@348@<Daten>'

<!-- PageBreak -->


<table>
<tr>
<th colspan="2">Financial Transaction Services (FinTS)</th>
<th>Version:</th>
<th>Kapitel:</th>
</tr>
<tr>
<td>Dokument:</td>
<td>Security - Sicherheitsverfahren PIN/TAN</td>
<td>3.0-FV</td>
<td>D</td>
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
<td>23.02.2018</td>
<td>211</td>
</tr>
</table>


HNSHK:2:4+PIN:1+999+654321+1+1+1::2+3234+1:20020
701:111151+1:999:1+6:10:16+280:10020030:12345: S:
0 : 0'

HKEND:3:1+4711'

HNSHA:4:2+654321++83427'

HNHBS:5:1+4'


## b) Kreditinstitutsnachricht

HNHBK:1:3+000000000385+300+4711+4+4711:4'

HNVSK:998:3+PIN:1+998+1+1::2+1:20020610:102044+2
:2:13:@8@<X'00 00 00 00 00 00 00 00'>:5:1+280:10
020030:12345:V:0:0+0'

HNVSD:999:1+@348@<Daten>'

HIRMG:2:2+0100::Dialog beendet'

HIRMS:3:2:3+0020::Auftrag ausgeführt'
HNHBS:4:1+4'
