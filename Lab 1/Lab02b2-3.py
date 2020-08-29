# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: Olivia Ornelas
# Section: 514
# Assignment: Lab 2b-3
# Date: 10 September 2018
Time1 = 13
Time2 = 84
Time3 = 50
X1 = 1
X2 = 23
mx1 = (X1-X2)/(Time1-Time2)
bx1 = X1-mx1*Time1
X3 = (mx1*Time3)+bx1

Y1 = 3
Y2 = -5
my1 = (Y1-Y2)/(Time1-Time2)
by1 = Y1-(my1*Time1)
Y3 = (my1*Time3)+by1

Z1 = 7
Z2 = 10
mz1 = (Z1-Z2)/(Time1-Time2)
bz1 = Z1-(mz1*Time1)
Z3 = mz1*Time3+bz1
print("The position at time 50 is (", X3, ",", Y3, ",", Z3, ")")
print("--------------------")

Time4 = 51
X1_2 = 1
X2_2 = 23
mx2 = (X1_2-X2_2)/(Time1-Time2)
bx2 = X1_2-mx2*Time1
X3_2 = (mx2*Time4)+bx2

Y1_2 = 3
Y2_2 = -5
my2 = (Y1_2-Y2_2)/(Time1-Time2)
by2 = Y1_2-my2*Time1
Y3_2 = (my2*Time4)+by2

Z1_2 = 7
Z2_2 = 10
mz2 = (Z1_2-Z2_2)/(Time1-Time2)
bz2 = Z1_2-mz2*Time1
Z3_2 = (mz2*Time4)+bz2
print("The position at time 51 is (", X3_2, ",", Y3_2, ",", Z3_2, ")")
print("--------------------")
Time5 = 52
X1_3 = 1
X2_3 = 23
mx3 = (X1_3-X2_3)/(Time1-Time2)
bx3 = X1_3-mx3*Time1
X3_3 = (mx3*Time5)+bx3

Y1_3 = 3
Y2_3 = -5
my3 = (Y1_3-Y2_3)/(Time1-Time2)
by3 = Y1_3-my3*Time1
Y3_3 = (my3*Time5)+by3

Z1_3 = 7
Z2_3 = 10
mz3 = (Z1_3-Z2_3)/(Time1-Time2)
bz3 = Z1_3-mz3*Time1
Z3_3 = (mz3*Time5)+bz3
print("The position at time 52 is (", X3_3, ",", Y3_3, ",", Z3_3, ")")
print("--------------------")
Time6 = 53
X1_4 = 1
X2_4 = 23
mx4 = (X1_4-X2_4)/(Time1-Time2)
bx4 = X1_4-mx4*Time1
X3_4 = (mx4*Time6)+bx4

Y1_4 = 3
Y2_4 = -5
my4 = (Y1_4-Y2_4)/(Time1-Time2)
by4 = Y1_4-my4*Time1
Y3_4 = (my4*Time6)+by4

Z1_4 = 7
Z2_4 = 10
mz4 = (Z1_4-Z2_4)/(Time1-Time2)
bz4 = Z1_4-mz4*Time1
Z3_4 = (mz4*Time6)+bz4
print("The position at time 52 is (", X3_4, ",", Y3_4, ",", Z3_4, ")")
print("--------------------")
Time7 = 54
X1_5 = 1
X2_5 = 23
mx5 = (X1_5-X2_5)/(Time1-Time2)
bx5 = X1_5-mx5*Time1
X3_5 = (mx5*Time7)+bx5
Y1_5 = 3
Y2_5 = -5
my5 = (Y1_5-Y2_5)/(Time1-Time2)
by5 = Y1_5-my5*Time1
Y3_5 = (my5*Time7)+by5

Z1_5 = 7
Z2_5 = 10
mz5 = (Z1_5-Z2_5)/(Time1-Time2)
bz5 = Z1_5-mz5*Time1
Z3_5 = (mz5*Time7)+bz5
print("The position at time 52 is (", X3_5, ",", Y3_5, ",", Z3_5, ")")


StartT = 20
StartMx = (X1_5-X2_5)/(Time1-Time2)
StartBx = X1_5-StartMx*Time1
StartX = (StartMx*StartT)+StartBx
StartMy = (Y1_5-Y2_5)/(Time1-Time2)
StartBy = Y1_5-StartMy*Time1
StartY = (StartMy*StartT)+StartBy
StartMz = (Z1_5-Z2_5)/(Time1-Time2)
StartBz = Z1_5-StartMz*Time1
StartZ = (StartMz*StartT)+StartBz
T2 = 25
T2x = (StartMx*T2)+StartBx
T2y = (StartMy*T2)+StartBy
T2z = (StartMz*T2)+StartBz
print("Position at time 25", T2x, T2y, T2z)
T3 = 30
T3x = (StartMx*T3)+StartBx
T3y = (StartMy*T3)+StartBy
T3z = (StartMz*T3)+StartBz
print("Position at time 30", T3x, T3y, T3z)
T4 = 35
T4x = (StartMx*T4)+StartBx
T4y = (StartMy*T4)+StartBy
T4z = (StartMz*T4)+StartBz
print("Position at time 35", T4x, T4y, T4z)
T5 = 40
T5x = (StartMx*T5)+StartBx
T5y = (StartMy*T5)+StartBy
T5z = (StartMz*T5)+StartBz
print("Position at time 40", T5x, T5y, T5z)
T6 = 45
T6x = (StartMx*T6)+StartBx
T6y = (StartMy*T6)+StartBy
T6z = (StartMz*T6)+StartBz
print("Position at time 45", T6x, T6y, T6z)
EndT = 50
Endx = (StartMx*EndT)+StartBx
Endy = (StartMy*EndT)+StartBy
Endz = (StartMz*EndT)+StartBz
print("Position at time 40", Endx, Endy, Endz)
