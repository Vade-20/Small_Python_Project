# Periodic Table Information System

## Introduction
This Python program provides information about elements in the periodic table. You can search for elements by their symbol or atomic number and get details such as atomic weight, density, melting point, boiling point, and more.

## Prerequisites
- Python 3.x
- CSV module (included in Python standard library)

## Usage
1. Clone or download this repository to your local machine.
2. Navigate to the project directory.
3. Run the program by executing `python periodic_table.py` in your terminal.

## How to Use
1. Upon running the program, you'll see a representation of the periodic table.
2. You can enter an element's symbol or atomic number to get information about that element.
3. To exit the program, type 'QUIT' when prompted.

## Example
```command-line
                Periodic Table of Elements
      1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17 18
    1 H                                                  He
    2 Li Be                               B  C  N  O  F  Ne
    3 Na Mg                               Al Si P  S  Cl Ar
    4 K  Ca Sc Ti V  Cr Mn Fe Co Ni Cu Zn Ga Ge As Se Br Kr
    5 Rb Sr Y  Zr Nb Mo Tc Ru Rh Pd Ag Cd In Sn Sb Te I  Xe
    6 Cs Ba La Hf Ta W  Re Os Ir Pt Au Hg Tl Pb Bi Po At Rn
    7 Fr Ra Ac Rf Db Sg Bh Hs Mt Ds Rg Cn Nh Fl Mc Lv Ts Og

            Ce Pr Nd Pm Sm Eu Gd Tb Dy Ho Er Tm Yb Lu
            Th Pa U  Np Pu Am Cm Bk Cf Es Fm Md No Lr
------------------------------------------------------------
Enter a symbol or atomic number to examine, or QUIT to quit:kr

                 Atomic Number : 36
                        Symbol : Kr
                       Element : Krypton
                Origin of name : Greek kryptós, 'hidden'
                         Group : 18
                        Period : 4
                 Atomic weight : 83.798(2) u
                       Density : 0.003733 g/cm^3
                 Melting point : 115.79 K
                 Boiling point : 119.93 K
        Specific heat capacity : 0.248 J/(g*K)
             Electronegativity : 3
    Abundance in earth's crust : 1×10−4 mg/kg
------------------------------------------------------------
Enter a symbol or atomic number to examine, or QUIT to quit:quit
```
## Data Source
The program uses a CSV file named `periodictable.csv` containing periodic table data. Ensure that this file is present in the project directory.

