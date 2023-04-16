from z3 import Solver,  Int, Bool, Not, sat, unsat, If, ToInt, BitVec, Real
import subprocess
# Inputs
in1 = Int('in1')
in2 = Int('in2')
in3 = Int('in3')
in4 = Int('in4')
in5 = Int('in5')
in6 = Int('in6')
in7 = Int('in7')
in8 = Int('in8')
in9 = Int('in9')
in10 = Int('in10')

# Key set - 1
# Int keys
k1_1 = Int('k1_1')
k2_1 = Int('k2_1')
k3_1 = Int('k3_1')
k4_1 = Int('k4_1')
k5_1 = Int('k5_1')
k6_1 = Int('k6_1')

# Bool keys
k7_1 = Bool('k7_1')
k8_1 = Bool('k8_1')
k9_1 = Bool('k9_1')
k10_1 = Bool('k10_1')
k11_1 = Bool('k11_1')
k12_1 = Bool('k12_1')
k13_1 = Bool('k13_1')
k14_1 = Bool('k14_1')
k15_1 = Bool('k15_1')
k16_1 = Bool('k16_1')
k17_1 = Bool('k17_1')
k18_1 = Bool('k18_1')
k19_1 = Bool('k19_1')
k20_1 = Bool('k20_1')

# Key set - 2
# Int keys
k1_2 = Int('k1_2')
k2_2 = Int('k2_2')
k3_2 = Int('k3_2')
k4_2 = Int('k4_2')
k5_2 = Int('k5_2')
k6_2 = Int('k6_2')

# Bool keys
k7_2 = Bool('k7_2')
k8_2 = Bool('k8_2')
k9_2 = Bool('k9_2')
k10_2 = Bool('k10_2')
k11_2 = Bool('k11_2')
k12_2 = Bool('k12_2')
k13_2 = Bool('k13_2')
k14_2 = Bool('k14_2')
k15_2 = Bool('k15_2')
k16_2 = Bool('k16_2')
k17_2 = Bool('k17_2')
k18_2 = Bool('k18_2')
k19_2 = Bool('k19_2')
k20_2 = Bool('k20_2')

# Output variables for key set - 1
out1_1 = Int('out1_1')
out2_1 = Int('out2_1')
out3_1 = Int('out3_1')

# Output variables for key set - 2
out1_2 = Int('out1_2')
out2_2 = Int('out2_2')
out3_2 = Int('out3_2')

# Multiplication variables for key set - 1
mult1_1 = Int('mult1_1')
mult2_1 = Int('mult2_1')
mult3_1 = Int('mult3_1')
mult4_1 = Int('mult4_1')
mult5_1 = Int('mult5_1')
mult6_1 = Int('mult6_1')
mult7_1 = Int('mult7_1')
mult8_1 = Int('mult8_1')
mult9_1 = Int('mult9_1')
mult10_1 = Int('mult10_1')
mult11_1 = Int('mult11_1')
mult12_1 = Int('mult12_1')
mult13_1 = Int('mult13_1')
mult14_1 = Int('mult14_1')

# Multiplication variables for key set - 2
mult1_2 = Int('mult1_2')
mult2_2 = Int('mult2_2')
mult3_2 = Int('mult3_2')
mult4_2 = Int('mult4_2')
mult5_2 = Int('mult5_2')
mult6_2 = Int('mult6_2')
mult7_2 = Int('mult7_2')
mult8_2 = Int('mult8_2')
mult9_2 = Int('mult9_2')
mult10_2 = Int('mult10_2')
mult11_2 = Int('mult11_2')
mult12_2 = Int('mult12_2')
mult13_2 = Int('mult13_2')
mult14_2 = Int('mult14_2')

# Addition variables for key set - 1
add1_1 = Int('add1_1')
add2_1 = Int('add2_1')
add3_1 = Int('add3_1')
add4_1 = Int('add4_1')
add5_1 = Int('add5_1')
add6_1 = Int('add6_1')
add7_1 = Int('add7_1')
add8_1 = Int('add8_1')
add9_1 = Int('add9_1')
add10_1 = Int('add10_1')
add11_1 = Int('add11_1')
add12_1 = Int('add12_1')
add13_1 = Int('add13_1')
add14_1 = Int('add14_1')
add15_1 = Int('add15_1')

# Addition variables for key set - 2
add1_2 = Int('add1_2')
add2_2 = Int('add2_2')
add3_2 = Int('add3_2')
add4_2 = Int('add4_2')
add5_2 = Int('add5_2')
add6_2 = Int('add6_2')
add7_2 = Int('add7_2')
add8_2 = Int('add8_2')  
add9_2 = Int('add9_2')
add10_2 = Int('add10_2')
add11_2 = Int('add11_2')
add12_2 = Int('add12_2')
add13_2 = Int('add13_2')
add14_2 = Int('add14_2')
add15_2 = Int('add15_2')

# Shift variables for key set - 1
shf1_1 = Int('shf1_1')
shf2_1 = Int('shf2_1')

# shf variables for key set - 2
shf1_2 = Int('shf1_2')
shf2_2 = Int('shf2_2')

# SMT solver
SMT = Solver()

# Adding contraints
# Line 1 - mult1 = key7? in1 * in2 : in1 +20;
SMT.add(If(k7_1, mult1_1 == in1 * in2, mult1_1 == in1 + 20))
SMT.add(If(k7_2, mult1_2 == in1 * in2, mult1_2 == in1 + 20))

# Line 2 - mult2 = in1 * key1;
SMT.add(mult2_1 == in1*k1_1)
SMT.add(mult2_2 == in1*k1_2)

# Line 3 - mult3 = key8? in3 * key2: in3 + 10;
SMT.add(If(k8_1, mult3_1 == in3 * k2_1, mult3_1 == in3 + 10))
SMT.add(If(k8_2, mult3_2 == in3 * k2_2, mult3_2 == in3 + 10))

# Line 4 - mult4 = in4 * in5;
SMT.add(mult4_1 == in4 * in5)
SMT.add(mult4_2 == in4 * in5)

# Line 5 - mult5 = key9? in3 * in2: in3 + 4;
SMT.add(If(k9_1, mult5_1 == in3 * in2, mult5_1 == in3 + 4))
SMT.add(If(k9_2, mult5_2 == in3 * in2, mult5_2 == in3 + 4))

# Line 6 - mult6 = in2 * in5;
SMT.add(mult6_1 == in2 * in5)
SMT.add(mult6_2 == in2 * in5)


# Line 7 - mult7 = key_10? in3 * in6 : in3 +9;
SMT.add(If(k10_1, mult7_1 == in3 * in6, mult7_1 == in3 + 9))
SMT.add(If(k10_2, mult7_2 == in3 * in6, mult7_2 == in3 + 9))

# Line 8 - mult8 = in4 * in7;
SMT.add(mult8_1 == in4 * in7)
SMT.add(mult8_2 == in4 * in7)

# Line 9 - mult9 = in4 * in8;
SMT.add(mult9_1 == in4 * in8)
SMT.add(mult9_2 == in4 * in8)

# Line 10 - mult10 = key_11? in6 * in9 : in6 +100;
SMT.add(If(k11_1, mult10_1 == in6 * in9, mult10_1 == in6 + 100))
SMT.add(If(k11_2, mult10_2 == in6 * in9, mult10_2 == in6 + 100))

# Line 11 - mult11 = in6 * in8;
SMT.add(mult11_1 == in6 * in8)
SMT.add(mult11_2 == in6 * in8)

# Line 12 - mult12 = key_12 ? in7 * in9 : in7 +100;
SMT.add(If(k12_1, mult12_1 == in7 * in9, mult12_1 == in7 + 100))
SMT.add(If(k12_2, mult12_2 == in7 * in9, mult12_2 == in7 + 100))

# Line 13 - mult13 = in7 * in8;
SMT.add(mult13_1 == in7 * in8)
SMT.add(mult13_2 == in7 * in8)

# Line 14 - mult14 = in9 * in10;
SMT.add(mult14_1 == in9 * in10)
SMT.add(mult14_2 == in9 * in10)

# Line 15 - add1 = in1 * mult2;
SMT.add(add1_1 == in1 * mult2_1)
SMT.add(add1_2 == in1 * mult2_2)

# Line 16 - add2 = key3 * mult4;
SMT.add(add2_1 == k3_1 * mult4_1)
SMT.add(add2_2 == k3_2 * mult4_2)

# Line 17 - add3 = in5 * mult8;
SMT.add(add3_1 == in5 * mult8_1)
SMT.add(add3_2 == in5 * mult8_2)

# Line 18 - add4 = mult10 * in4;
SMT.add(add4_1 == mult10_1 * in4)
SMT.add(add4_2 == mult10_2 * in4)

# Line 19 - add5 = key_14 ? in10 - mult14 : in10 * mult14;
SMT.add(If(k14_1, add5_1 == in10 - mult14_1, add5_1 == in10 * mult14_1))
SMT.add(If(k14_2, add5_2 == in10 - mult14_2, add5_2 == in10 * mult14_2))

# Line 20 - add6 = key_13 ? mult1 * add1 : mult1 + add1;
SMT.add(If(k13_1, add6_1 == mult1_1 * add1_1, add6_1 == mult1_1 + add1_1))
SMT.add(If(k13_2, add6_2 == mult1_2 * add1_2, add6_2 == mult1_2 + add1_2))

# Line 21 - out1 = add6+key4;
SMT.add(out1_1 == add6_1 + k4_1)
SMT.add(out1_2 == add6_2 + k4_2)

# Line 22 - add7 = key_15 ? mult3 - add2 : mult3 + add2;
SMT.add(If(k15_1, add7_1 == mult3_1 - add2_1, add7_1 == mult3_1 + add2_1))
SMT.add(If(k15_2, add7_2 == mult3_2 - add2_2, add7_2 == mult3_2 + add2_2))

# Line 23 - add8 = key_16 ? mult5 / add7 : mult5 + add7;
SMT.add(If(k16_1, add8_1 == mult5_1 / add7_1, add8_1 == mult5_1 + add7_1))
SMT.add(If(k16_2, add8_2 == mult5_2 / add7_2, add8_2 == mult5_2 + add7_2))

# Line 24 - add10 = mult7 + add3;
SMT.add(add10_1 == mult7_1 + add3_1)
SMT.add(add10_2 == mult7_2 + add3_2)

# Line 25 - add9 = mult6 + add10;
SMT.add(add9_1 == mult6_1 + add10_1)
SMT.add(add9_2 == mult6_2 + add10_2)

# Line 26 - shf1 = key_17 ? add9 << 2 : add9 << 3;
SMT.add(If(k17_1, shf1_1 == (add9_1 * 2*2), shf1_1 == (add9_1 * 2*3)))
SMT.add(If(k17_2, shf1_2 == (add9_2 * 2*2), shf1_2 == (add9_2 * 2*3)))

# Line 27 - out2 = add8 + shf1+key5;
SMT.add(out2_1 == add8_1 + shf1_1 + k5_1)
SMT.add(out2_2 == add8_2 + shf1_2 + k5_2)

# Line 28 - add13 = key_18 ? mult9 + add4 : mult9 * add4;
SMT.add(If(k18_1, add13_1 == mult9_1 + add4_1, add13_1 == mult9_1 * add4_1))
SMT.add(If(k18_2, add13_2 == mult9_2 + add4_2, add13_2 == mult9_2 * add4_2))

# Line 29 - add11 = add13 + mult11;
SMT.add(add11_1 == add13_1 + mult11_1)
SMT.add(add11_2 == add13_2 + mult11_2)

# Line 30 - add15 = key_19 ? mult13 - add5 : mult13 + add5;
SMT.add(If(k19_1, add15_1 == mult13_1 - add5_1, add15_1 == mult13_1 + add5_1))
SMT.add(If(k19_2, add15_2 == mult13_2 - add5_2, add15_2 == mult13_2 + add5_2))

# Line 31 - add14 = mult12 + add15;
SMT.add(add14_1 == mult12_1 + add15_1)
SMT.add(add14_2 == mult12_2 + add15_2)

# Line 32 - shf2 = key_20 ? add14 >> 4 : add14 >> 3;
a_1 = add14_1 / 2**4
a_2 = add14_2 / 2**4
b_1 = add14_1 / 2**3
b_2 = add14_2 / 2**3

SMT.add(If(k20_1, shf2_1 == a_1, shf2_1 == b_1))
SMT.add(If(k20_2, shf2_2 == a_2, shf2_2 == b_2))

# Line 33 - out3 = add11 + shf2+key6;
SMT.add(out3_1 == add11_1 + shf2_1 + k6_1)
SMT.add(out3_2 == add11_2 + shf2_2 + k6_2)

# Output constraints
SMT.add(Not(out1_1 == out1_2))
SMT.add(Not(out2_1 == out2_2))
SMT.add(Not(out3_1 == out3_2))


limit = 100000
iter = 1
file = open("keys.txt", "w")
while iter <= limit:
    if SMT.check() == unsat:
        print("Keys found!")
        final_solver = Solver()
        for s in SMT.assertions():
            if str(s) == "Not(out1_1 == out1_2)":
                final_solver.add(out1_1 == out1_2)
            elif str(s) == "Not(out2_1 == out2_2)": 
                final_solver.add(out2_1 == out2_2)
            elif str(s) == "Not(out3_1 == out3_2)": 
                final_solver.add(out3_1 == out3_2)  
            else: 
                final_solver.add(s)
                
        if final_solver.check() == unsat:
            print("No solution exist!")
        else :
            m = final_solver.model()
            # Extract all keys and write to file 
            Key_1 = "Key_1: {" + str(m[k1_1]) + ", " + str(m[k1_2]) + "}\n"
            Key_2 = "Key_2: {" + str(m[k2_1]) + ", " + str(m[k2_2]) + "}\n"
            Key_3 = "Key_3: {" + str(m[k3_1]) + ", " + str(m[k3_2]) + "}\n"
            Key_4 = "Key_4: {" + str(m[k4_1]) + ", " + str(m[k4_2]) + "}\n"
            Key_5 = "Key_5: {" + str(m[k5_1]) + ", " + str(m[k5_2]) + "}\n"
            Key_6 = "Key_6: {" + str(m[k6_1]) + ", " + str(m[k6_2]) + "}\n"
            Key_7 = "Key_7: {" + str(m[k7_1]) + ", " + str(m[k7_2]) + "}\n"
            Key_8 = "Key_8: {" + str(m[k8_1]) + ", " + str(m[k8_2]) + "}\n"
            Key_9 = "Key_9: {" + str(m[k9_1]) + ", " + str(m[k9_2]) + "}\n"
            Key_10 = "Key_10: {" + str(m[k10_1]) + ", " + str(m[k10_2]) + "}\n"
            Key_11 = "Key_11: {" + str(m[k11_1]) + ", " + str(m[k11_2]) + "}\n"
            Key_12 = "Key_12: {" + str(m[k12_1]) + ", " + str(m[k12_2]) + "}\n"
            Key_13 = "Key_13: {" + str(m[k13_1]) + ", " + str(m[k13_2]) + "}\n"
            Key_14 = "Key_14: {" + str(m[k14_1]) + ", " + str(m[k14_2]) + "}\n"
            Key_15 = "Key_15: {" + str(m[k15_1]) + ", " + str(m[k15_2]) + "}\n"
            Key_16 = "Key_16: {" + str(m[k16_1]) + ", " + str(m[k16_2]) + "}\n"
            Key_17 = "Key_17: {" + str(m[k17_1]) + ", " + str(m[k17_2]) + "}\n"
            Key_18 = "Key_18: {" + str(m[k18_1]) + ", " + str(m[k18_2]) + "}\n"
            Key_19 = "Key_19: {" + str(m[k19_1]) + ", " + str(m[k19_2]) + "}\n"
            Key_20 = "Key_20: {" + str(m[k20_1]) + ", " + str(m[k20_2]) + "}\n"
            
            # Write to file
            file.write(Key_1)
            file.write(Key_2)
            file.write(Key_3)
            file.write(Key_4)
            file.write(Key_5)
            file.write(Key_6)
            file.write(Key_7)
            file.write(Key_8)
            file.write(Key_9)
            file.write(Key_10)
            file.write(Key_11)
            file.write(Key_12)
            file.write(Key_13)
            file.write(Key_14)
            file.write(Key_15)
            file.write(Key_16)
            file.write(Key_17)
            file.write(Key_18)
            file.write(Key_19)
            file.write(Key_20)
            
            # close file
            file.close()    
        break
    else:
       # DIP exists so find output from blackbox
        m = SMT.model() 
        
        # Extract all inputs from model
        dip_in1 = int(str(m[in1]))
        dip_in2 = int(str(m[in2]))
        dip_in3 = int(str(m[in3]))
        dip_in4 = int(str(m[in4]))
        dip_in5 = int(str(m[in5]))
        dip_in6 = int(str(m[in6]))
        dip_in7 = int(str(m[in7]))
        dip_in8 = int(str(m[in8]))
        dip_in9 = int(str(m[in9]))
        dip_in10 = int(str(m[in10]))
        
        process = subprocess.Popen(['./motion.exe', str(dip_in1), str(dip_in2), str(dip_in3), str(dip_in4), str(dip_in5), str(dip_in6), str(dip_in7), str(dip_in8), str(dip_in9), str(dip_in10)], stdout=subprocess.PIPE, stderr=subprocess.PIPE)                        

        output, error = process.communicate()

        if error:
            print("Error occurred: ", error)
            break
        else:
            dip_out = output.decode("utf-8")
            split = dip_out.split("\r\n")
            dip_out_1 = int(split[0])
            dip_out_2 = int(split[1])
            dip_out_3 = int(split[2])        
        # Adding new constraints to remove wrong keys

        # Line 1 - mult1 = key7? in1 * in2 : in1 +20;
        SMT.add(If(k7_1, mult1_1 == dip_in1 * dip_in2, mult1_1 == dip_in1 + 20))
        SMT.add(If(k7_2, mult1_2 == dip_in1 * dip_in2, mult1_2 == dip_in1 + 20))

        # Line 2 - mult2 = in1 * key1;
        SMT.add(mult2_1 == dip_in1*k1_1)
        SMT.add(mult2_2 == dip_in1*k1_2)

        # Line 3 - mult3 = key8? in3 * key2: in3 + 10;
        SMT.add(If(k8_1, mult3_1 == dip_in3 * k2_1, mult3_1 == dip_in3 + 10))
        SMT.add(If(k8_2, mult3_2 == dip_in3 * k2_2, mult3_2 == dip_in3 + 10))

        # Line 4 - mult4 = in4 * in5;
        SMT.add(mult4_1 == dip_in4 * dip_in5)
        SMT.add(mult4_2 == dip_in4 * dip_in5)

        # Line 5 - mult5 = key9? in3 * in2: in3 + 4;
        SMT.add(If(k9_1, mult5_1 == dip_in3 * dip_in2, mult5_1 == dip_in3 + 4))
        SMT.add(If(k9_2, mult5_2 == dip_in3 * dip_in2, mult5_2 == dip_in3 + 4))

        # Line 6 - mult6 = in2 * in5;
        SMT.add(mult6_1 == dip_in2 * dip_in5)
        SMT.add(mult6_2 == dip_in2 * dip_in5)

        # Line 7 - mult7 = key_10? in3 * in6 : in3 +9;
        SMT.add(If(k10_1, mult7_1 == dip_in3 * dip_in6, mult7_1 == dip_in3 + 9))
        SMT.add(If(k10_2, mult7_2 == dip_in3 * dip_in6, mult7_2 == dip_in3 + 9))

        # Line 8 - mult8 = in4 * in7;
        SMT.add(mult8_1 == dip_in4 * dip_in7)
        SMT.add(mult8_2 == dip_in4 * dip_in7)

        # Line 9 - mult9 = in4 * in8;
        SMT.add(mult9_1 == dip_in4 * dip_in8)
        SMT.add(mult9_2 == dip_in4 * dip_in8)

        # Line 10 - mult10 = key_11? in6 * in9 : in6 +100;
        SMT.add(If(k11_1, mult10_1 == dip_in6 * dip_in9, mult10_1 == dip_in6 + 100))
        SMT.add(If(k11_2, mult10_2 == dip_in6 * dip_in9, mult10_2 == dip_in6 + 100))

        # Line 11 - mult11 = in6 * in8;
        SMT.add(mult11_1 == dip_in6 * dip_in8)
        SMT.add(mult11_2 == dip_in6 * dip_in8)

        # Line 12 - mult12 = key_12 ? in7 * in9 : in7 +100;
        SMT.add(If(k12_1, mult12_1 == dip_in7 * dip_in9, mult12_1 == dip_in7 + 100))
        SMT.add(If(k12_2, mult12_2 == dip_in7 * dip_in9, mult12_2 == dip_in7 + 100))

        # Line 13 - mult13 = in7 * in8;
        SMT.add(mult13_1 == dip_in7 * dip_in8)
        SMT.add(mult13_2 == dip_in7 * dip_in8)

        # Line 14 - mult14 = in9 * in10;
        SMT.add(mult14_1 == dip_in9 * dip_in10)
        SMT.add(mult14_2 == dip_in9 * dip_in10)

        # Line 15 - add1 = in1 * mult2;
        SMT.add(add1_1 == dip_in1 * mult2_1)
        SMT.add(add1_2 == dip_in1 * mult2_2)

        # Line 16 - add2 = key3 * mult4;
        SMT.add(add2_1 == k3_1 * mult4_1)
        SMT.add(add2_2 == k3_2 * mult4_2)

        # Line 17 - add3 = in5 * mult8;
        SMT.add(add3_1 == dip_in5 * mult8_1)
        SMT.add(add3_2 == dip_in5 * mult8_2)

        # Line 18 - add4 = mult10 * in4;
        SMT.add(add4_1 == mult10_1 * dip_in4)
        SMT.add(add4_2 == mult10_2 * dip_in4)

        # Line 19 - add5 = key_14 ? in10 - mult14 : in10 * mult14;
        SMT.add(If(k14_1, add5_1 == dip_in10 - mult14_1, add5_1 == dip_in10 * mult14_1))
        SMT.add(If(k14_2, add5_2 == dip_in10 - mult14_2, add5_2 == dip_in10 * mult14_2))

        # Line 20 - add6 = key_13 ? mult1 * add1 : mult1 + add1;
        SMT.add(If(k13_1, add6_1 == mult1_1 * add1_1, add6_1 == mult1_1 + add1_1))
        SMT.add(If(k13_2, add6_2 == mult1_2 * add1_2, add6_2 == mult1_2 + add1_2))

        # Line 21 - out1 = add6+key4;
        SMT.add(dip_out_1 == add6_1 + k4_1)
        SMT.add(dip_out_1 == add6_2 + k4_2)

        # Line 22 - add7 = key_15 ? mult3 - add2 : mult3 + add2;
        SMT.add(If(k15_1, add7_1 == mult3_1 - add2_1, add7_1 == mult3_1 + add2_1))
        SMT.add(If(k15_2, add7_2 == mult3_2 - add2_2, add7_2 == mult3_2 + add2_2))

        # Line 23 - add8 = key_16 ? mult5 / add7 : mult5 + add7;
        SMT.add(If(k16_1, add8_1 == mult5_1 / add7_1, add8_1 == mult5_1 + add7_1))
        SMT.add(If(k16_2, add8_2 == mult5_2 / add7_2, add8_2 == mult5_2 + add7_2))

        # Line 24 - add10 = mult7 + add3;
        SMT.add(add10_1 == mult7_1 + add3_1)
        SMT.add(add10_2 == mult7_2 + add3_2)

        # Line 25 - add9 = mult6 + add10;
        SMT.add(add9_1 == mult6_1 + add10_1)
        SMT.add(add9_2 == mult6_2 + add10_2)

        # Line 26 - shf1 = key_17 ? add9 << 2 : add9 << 3;
        SMT.add(If(k17_1, shf1_1 == (add9_1 * 2*2), shf1_1 == (add9_1 * 2*3)))
        SMT.add(If(k17_2, shf1_2 == (add9_2 * 2*2), shf1_2 == (add9_2 * 2*3)))

        # Line 27 - out2 = add8 + shf1+key5;
        SMT.add(dip_out_2 == add8_1 + shf1_1 + k5_1)
        SMT.add(dip_out_2 == add8_2 + shf1_2 + k5_2)

        # Line 28 - add13 = key_18 ? mult9 + add4 : mult9 * add4;
        SMT.add(If(k18_1, add13_1 == mult9_1 + add4_1, add13_1 == mult9_1 * add4_1))
        SMT.add(If(k18_2, add13_2 == mult9_2 + add4_2, add13_2 == mult9_2 * add4_2))

        # Line 29 - add11 = add13 + mult11;
        SMT.add(add11_1 == add13_1 + mult11_1)
        SMT.add(add11_2 == add13_2 + mult11_2)

        # Line 30 - add15 = key_19 ? mult13 - add5 : mult13 + add5;
        SMT.add(If(k19_1, add15_1 == mult13_1 - add5_1, add15_1 == mult13_1 + add5_1))
        SMT.add(If(k19_2, add15_2 == mult13_2 - add5_2, add15_2 == mult13_2 + add5_2))

        # Line 31 - add14 = mult12 + add15;
        SMT.add(add14_1 == mult12_1 + add15_1)
        SMT.add(add14_2 == mult12_2 + add15_2)

        # Line 32 - shf2 = key_20 ? add14 >> 4 : add14 >> 3;
        a_1 = add14_1 / 2**4
        a_2 = add14_2 / 2**4
        b_1 = add14_1 / 2**3
        b_2 = add14_2 / 2**3

        SMT.add(If(k20_1, shf2_1 == a_1, shf2_1 == b_1))
        SMT.add(If(k20_2, shf2_2 == a_2, shf2_2 == b_2))

        # Line 33 - out3 = add11 + shf2+key6;
        SMT.add(dip_out_3 == add11_1 + shf2_1 + k6_1)
        SMT.add(dip_out_3 == add11_2 + shf2_2 + k6_2)

    iter += 1
if iter == limit:
        print("Limit reached")    