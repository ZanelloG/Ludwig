# Ludwig — A Vector-Based Logic Framework for Explainable AI (XAI)

**Author**: Giosuè Zanello  
**University**: Università degli Studi di Udine (UNIUD)  
**Course**: Laboratorio del Digitale  
**Academic Year**: 2024–2025
**Student ID**: 168088

## Abstract

Questo progetto nasce da un interesse personale e si propone di sviluppare un framework in Python per rendere trasparente e verificabile il funzionamento di sistemi di rappresentazione distribuita come le Vector Symbolic Architectures (VSA).
Il framework si basa su una teoria della **degenerazione logica**: le operazioni vettoriali complesse (come binding e bundling) vengono ricondotte a regole della logica proposizionale, i vettori a dei simboli proposizionali, facilitando l’interpretazione dei processi interni e la spiegazione simbolica del comportamento del sistema.

L’approccio è ispirato alla filosofia del *Tractatus Logico-Philosophicus* di Wittgenstein, con l’obiettivo di costruire un ponte tra operazioni computazionali distribuite e ragionamento formale, tentando poi una teoria della rappresentazione vettoriale.

## Obiettivi del progetto

- Mappare vettori atomici su simboli logici univoci ai fini dell'interpretabilità.
- Tradurre operazioni vettoriali (binding, bundling) in regole logiche esplicite.
- Tracciare la genealogia logica di ogni simbolo composto tramite rappresentazioni ad albero o grafo (grafici che aiutino la ricostruzione delle operazioni).
- Verificare proprietà formali come commutatività, associatività, deducibilità dei simboli nelle operazioni.
- Rilevare incoerenze semantiche e allucinazioni simboliche nei processi di composizione.

## Contesto

Le Vector Symbolic Architectures sono modelli computazionali che permettono di rappresentare concetti e strutture logiche in forma distribuita mediante vettori ad alta dimensionalità. Tuttavia, queste rappresentazioni risultano spesso opache per l’analisi umana. Il progetto Ludwig affronta questo limite, introducendo nella computazione distribuita la logica proposizionale esplicita.
Questo processo di *degenerazione logica* permette di analizzare le trasformazioni dei vettori come formule simboliche, rendendo così ogni operazione computabile anche da un punto di vista logico-formale.

## Note aggiuntive

Il codice è scritto in Python e fa uso di librerie standard come `numpy` per la gestione dei vettori e `scipy` per la misura di similarità. Sono in fase di valutazione strumenti per la visualizzazione grafica delle derivazioni simboliche (es. `networkx`, `graphviz`).
La sezione Papers contiene ulteriori approfondimenti teorici rispetto Wittgenstein e l'Intelligenza Artificiale neuro-simbolica scritti dall'autore.
Per maggiori dettagli teorici, si veda il documento allegato “A Logical Degeneration of Vector Symbolic Architectures for Explainable AI”, disponibile nella stessa repository.


## Contatti

**Email**: giosuezanello1@gmail.com
**Email Istituzionale**: zanello.giosue@spes.uniud.it
**GitHub**: github.com/ZanelloG

