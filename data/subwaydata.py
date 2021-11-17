import numpy as np
import pandas as pd

subway_stops = {
0:	"Rector St",
1:	"WTC Cortlandt",
2:	"Chambers St",
3:	"Franklin Street Station",
4:	"Canal St",
5:	"Houston St",
6:	"Christopher St Station",
7:	"14 St",
8:	"18 Street Station",
9:	"23 St",
10:	"28 St",
11:	"34 Street - Penn Station",
12:	"Times Sq - 42 St",
13:	"50 Street Station",
14:	"59 St - Columbus Circle",
15:	"66 St-Lincoln Center",
16:	"72 St",
17:	"79 St",
18:	"86 St",
19:	"96 St",
20:	"103 St",
21:	"Cathedral Parkway 110 Street",
22:	"116 Street Station - Columbia University",
23:	"125 Street Station",
24:	"137 St - City College",
25: "145 St",
26:	"157 Street Station",
27:	"168 St - Washington Hts",
28:	"191 Street",
29:	"Dyckman St",
30:	"207 St",
31:	"215 Street Station",
32:	"Harlem / 148 St",
33:	"135 St",
34:	"116 St",
35:	"Central Park North (110 St)",
36:	"Park Place",
37:	"Fulton Street",
38:	"Wall Street Station",
39:	"116 Street",
40:	"110 Street",
41:	"103 Street Station",
42:	"96 Street Station",
43:	"86th Street",
44:	"77 St",
45:	"68 St-Hunter College",
46:	"59 St-Lexington Av",
47:	"51 St",
48:	"Grand Central - 42 St",
49:	"33 St",
50:	"28 St Station",
51:	"14 St - Union Sq",
52:	"Astor Pl",
53:	"Bleecker St",
54:	"Spring Street",
55:	"Brooklyn Bridge - City Hall",
56:	"5 Av",
57:	"34 Street-Hudson Yards Subway Station",
58:	"207 St Station",
59:	"190 St",
60:	"181 St",
61:	"175 St",
62:	"168 St",
63:	"163 Street Subway Station",
64:	"155 St",
65:	"145th St And St Nicholas Ave MTA Subway Station",
66:	"125 St",
67:	"59 St-Columbus Circle",
68:	"42 St - Port Authority Bus Terminal",
69:	"34 St - Penn Station",
70:	"14 St / 8 Av",
71:	"W 4 St - Wash Sq",
72:	"Canal Street",
73:	"Fulton Street Subway Station",
74:	"Lexington Av/53 St",
75:	"5 Avenue-53 St Station",
76:	"7 Avenue Station",
77:	"50 St",
78:	"23rd St",
79:	"Spring St.",
80:	"World Trade Center",
81:	"155 Street",
82:	"135 Street",
83:	"Cathedral Pkwy",
84:	"81 Street - Museum of Natural History",
85:	"47-50 Sts-Rockefeller Ctr",
86:	"42 St-Bryant Park Station",
87:	"34 St - Herald Sq Subway Station",
88:	"Broadway-Lafayette St",
89:	"Grand St",
90:	"Roosevelt Island Subway Station",
91:	"Lexington Av/63 St",
92: "57 Street",
93:	"23 St Station",
94:	"14 St / 6 Av",
95:	"2nd Avenue",
96:	"Delancey St · Essex St",
97:	"East Broadway",
98:	"Broad St",
99:	"Fulton St",
100: "Bowery",
101: "86th St",
102: "City Hall Station",
103: "Cortlandt St",
104: "3 Av",
105: "1 Av",
106: "Whitehall St"
}

subway_stop_inv = {v: k for k, v in subway_stops.items()}
distance_matrix = [[0 for i in range(len(subway_stops))] for j in range(len(subway_stops))]


def import_lines(sheetname):
    df = pd.read_excel('subway data.xlsx', sheet_name=sheetname, engine="openpyxl")
    a = df.values.tolist()
    for list in a:
        list.pop(1)
    print("imported line " + sheetname)
    return a


def add_one_line(line):
    for i in range(0, len(line)-1):
        weight = line[i+1][1]
        stop1 = subway_stop_inv[line[i][0]]
        stop2 = subway_stop_inv[line[i+1][0]]
        if distance_matrix[stop1][stop2] == 0:
            distance_matrix[stop1][stop2] = weight
            distance_matrix[stop2][stop1] = weight # symmetric
        else:
            if distance_matrix[stop1][stop2] > weight:
                distance_matrix[stop1][stop2] = weight
    return


line1 = import_lines("1")
lineL = import_lines("L")
lineNRWQ = import_lines("NRWQ")
lineJZ = import_lines("JZ")
lineM = import_lines("M")
lineF = import_lines("F")
lineBD = import_lines("BD")
lineE = import_lines("E")
lineAC = import_lines("AC")
line7 = import_lines("7")
line456 = import_lines("456")
line2 = import_lines("2")

add_one_line(line1)
add_one_line(lineL)
add_one_line(lineNRWQ)
add_one_line(lineJZ)
add_one_line(lineM)
add_one_line(lineF)
add_one_line(lineBD)
add_one_line(lineE)
add_one_line(lineAC)
add_one_line(line7)
add_one_line(line456)
add_one_line(line2)

with open('distance_matrix.txt', 'w') as f:
    for item in distance_matrix:
        f.write("%s\n" % item)


print("distance matrix saved to distance_matrix.txt")
