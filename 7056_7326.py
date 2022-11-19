import sympy

# Got the value of p randomly from the next 5 lines then used it as static

# l = 2
# while l != 16:
#    p = sympy.randprime(0, 65535)
#    z = bin(p)
#    l = len(z) - 2

print("#IDs")
print("MY_ID = " + str(40217056))
print("MY_ID = " + str(27717326))
print("\n")
print("#my data")

p = 36943

print("p= " + str(p))

# Got the value of q randomly from the next 5 lines then used it as static

# k = 2
# while k != 16:
#    q = sympy.randprime(0, 65535)
#    s = bin(q)
#    k = len(s) - 2

q = 49307

print("q= " + str(q))

N = p * q

print("N= " + str(N))

Phi_N = (p - 1) * (q - 1)

print("phi_N= " + str(Phi_N))

# Got the value of e randomly from the next 2 lines then used it as static

# e = sympy.randprime(0, Phi_N - 1)
# if math.gcd(Phi_N, e) == 1:

#  print("Value of e: " + str(e))

e = 1258093567

print("e= " + str(e))

d = sympy.mod_inverse(e, Phi_N)

print("d= " + str(d))

print("\n")
print("#my partner data")
print("PARTNER_N= " + str("14266103"))
print("PARTNER_e= " + str("65537"))
print("\n")

partner_N = 14266103
partner_e = 65537

print("# encryption")
message = "Nothing is permanent"

print("MY_MESSAGE = " + message)

list1 = []

for i in range(0, len(message), 3):
    list1.append(message[i:i + 3])

print("MY_MESSAGE_chunks = " + str(list1))

# print(list1)

list2 = []

for i in range(len(list1)):
    list1[i] = list1[i].encode('utf-8')

    list2.append(list1[i].hex())

# print(list2) ## MY_MESSAGE_chunks converted into hexadecimal


list3 = []

for i in range(len(list2)):
    list2[i] = int(list2[i], 16)

    list3.append(list2[i])

# print(list3) ## Hexadecimal chunks converted into decimal

list4 = []

for i in range(len(list3)):
    q1 = (list3[i] ** 1) % partner_N
    q2 = (q1 ** 2) % partner_N
    q3 = (q2 ** 2) % partner_N
    q4 = (q3 ** 2) % partner_N
    q5 = (q4 ** 2) % partner_N
    q6 = (q5 ** 2) % partner_N
    q7 = (q6 ** 2) % partner_N
    q8 = (q7 ** 2) % partner_N
    q9 = (q8 ** 2) % partner_N
    q10 = (q9 ** 2) % partner_N
    q11 = (q10 ** 2) % partner_N
    q12 = (q11 ** 2) % partner_N
    q13 = (q12 ** 2) % partner_N
    q14 = (q13 ** 2) % partner_N
    q15 = (q14 ** 2) % partner_N
    q16 = (q15 ** 2) % partner_N
    q17 = (q16 ** 2) % partner_N

    list3[i] = ((q1 * q17) % partner_N)
    list4.append(list3[i])

print("MY_CIPHERTEXT = " + str(list4))
print('\n')
# print(list4)

print("# decryption")

list5 = [703718609, 248577627, 818982822, 554257118, 924702589, 583766315, 1042981642, 434494777, 1690041313,
         1363015629, 427238170, 1293158509, 965997147, 5803763, 285099495, 490415529, 1552677081, 549457257,
         1018082718, 52241121, 1453114394, 475863239, 112639551, 1413897516, 322272937, 999503322, 820176710,
         370995863, 1740732368, 1095992151, 1685642412, 542235939, 925150304, 1803895222, 967169469, 288373441,
         990708286, 1069839417, 638000433, 621336951, 1065805647, 778565217, 1069796439]

list6 = []

for i in range(len(list5)):
    qq1 = (list5[i] ** 1) % N
    qq2 = (qq1 ** 2) % N
    qq3 = (qq2 ** 2) % N
    qq4 = (qq3 ** 2) % N
    qq5 = (qq4 ** 2) % N
    qq6 = (qq5 ** 2) % N
    qq7 = (qq6 ** 2) % N
    qq8 = (qq7 ** 2) % N
    qq9 = (qq8 ** 2) % N
    qq10 = (qq9 ** 2) % N
    qq11 = (qq10 ** 2) % N
    qq12 = (qq11 ** 2) % N
    qq13 = (qq12 ** 2) % N
    qq14 = (qq13 ** 2) % N
    qq15 = (qq14 ** 2) % N
    qq16 = (qq15 ** 2) % N
    qq17 = (qq16 ** 2) % N
    qq18 = (qq17 ** 2) % N
    qq19 = (qq18 ** 2) % N
    qq20 = (qq19 ** 2) % N
    qq21 = (qq20 ** 2) % N
    qq22 = (qq21 ** 2) % N
    qq23 = (qq22 ** 2) % N
    qq24 = (qq23 ** 2) % N
    qq25 = (qq24 ** 2) % N
    qq26 = (qq25 ** 2) % N

    list5[i] = (((((qq1 * qq2 * qq3 * qq6) % N) * ((qq8 * qq11 * qq15 * qq16) % N)) % N) * (
            (qq19 * qq21 * qq22 * qq23 * qq26) % N)) % N
    list6.append(list5[i])

print("PARTNER_CIPHERTEXT = " + str(list6))

list7 = []

for i in range(len(list6)):
    list6[i] = hex(list6[i])
    list7.append(list6[i])
    list7[i] = list7[i][2:]

# print('Decoded Hexadecimal: ' + str(list7))

list8 = []

for i in range(len(list7)):
    list7[i] = bytearray.fromhex(list7[i]).decode("utf-8")
    list8.append(list7[i])

print('PARTNER_MESSAGE_chunks_AFTER_DECRYPT =' + str(list8))

list9 = []

decoded_message = ''.join(list8)
print("PARTNER_MESSAGE_AFTER_DECRYPT = " + str(decoded_message))

print("# sign")
MY_MESSAGE_TO_BE_SIGNED = "Saif Manjar Ahmad"
print("MY_MESSAGE_TO_BE_SIGNED=" + MY_MESSAGE_TO_BE_SIGNED)

list10 = []

for i in range(0, len(MY_MESSAGE_TO_BE_SIGNED), 3):
    list10.append(MY_MESSAGE_TO_BE_SIGNED[i:i + 3])

print("MY_MESSAGE_TO_BE_SIGNED_chunks = " + str(list10))

list11 = []

for i in range(len(list10)):
    list10[i] = list10[i].encode('utf-8')

    list11.append(list10[i].hex())

# print(list11) ## MY_MESSAGE_chunks converted into hexadecimal

list12 = []

for i in range(len(list11)):
    list11[i] = int(list11[i], 16)

    list12.append(list11[i])
# print("Hexadecimal to integer: "+ str(list12))

list13 = []

for i in range(len(list12)):
    d1 = (list12[i] ** 1) % N
    d2 = (d1 ** 2) % N
    d3 = (d2 ** 2) % N
    d4 = (d3 ** 2) % N
    d5 = (d4 ** 2) % N
    d6 = (d5 ** 2) % N
    d7 = (d6 ** 2) % N
    d8 = (d7 ** 2) % N
    d9 = (d8 ** 2) % N
    d10 = (d9 ** 2) % N
    d11 = (d10 ** 2) % N
    d12 = (d11 ** 2) % N
    d13 = (d12 ** 2) % N
    d14 = (d13 ** 2) % N
    d15 = (d14 ** 2) % N
    d16 = (d15 ** 2) % N
    d17 = (d16 ** 2) % N
    d18 = (d17 ** 2) % N
    d19 = (d18 ** 2) % N
    d20 = (d19 ** 2) % N
    d21 = (d20 ** 2) % N
    d22 = (d21 ** 2) % N
    d23 = (d22 ** 2) % N
    d24 = (d23 ** 2) % N
    d25 = (d24 ** 2) % N
    d26 = (d25 ** 2) % N

    list12[i] = (((d1 * d2 * d3) % N) * ((d6 * d8 * d11) % N) * ((d15 * d16 * d19) % N) * (
            (d21 * d22 * d23 * d26) % N)) % N
    list13.append(list12[i])

print("MY_SIGNATURE = " + str(list13))
print('\n')

print("# verify the signature")

PARTNER_SIGNED_MESSAGE = "Hassan Mansour"
print("PARTNER_SIGNED_MESSAGE= " + PARTNER_SIGNED_MESSAGE)

list14 = [4740654, 1147903, 4340140, 7505959, 7411587]
print("PARTNER_SIGNATURE = " + str(list14))
list15 = []

for i in range(len(list14)):
    qa1 = (list14[i] ** 1) % partner_N
    qa2 = (qa1 ** 2) % partner_N
    qa3 = (qa2 ** 2) % partner_N
    qa4 = (qa3 ** 2) % partner_N
    qa5 = (qa4 ** 2) % partner_N
    qa6 = (qa5 ** 2) % partner_N
    qa7 = (qa6 ** 2) % partner_N
    qa8 = (qa7 ** 2) % partner_N
    qa9 = (qa8 ** 2) % partner_N
    qa10 = (qa9 ** 2) % partner_N
    qa11 = (qa10 ** 2) % partner_N
    qa12 = (qa11 ** 2) % partner_N
    qa13 = (qa12 ** 2) % partner_N
    qa14 = (qa13 ** 2) % partner_N
    qa15 = (qa14 ** 2) % partner_N
    qa16 = (qa15 ** 2) % partner_N
    qa17 = (qa16 ** 2) % partner_N

    list14[i] = ((qa1 * qa17) % partner_N)
    list15.append(list14[i])

# print(list15)

list16 = []

for i in range(len(list15)):
    list15[i] = hex(list15[i])
    list16.append(list15[i])
    list16[i] = list16[i][2:]

# print(list16)

list17 = []

for i in range(len(list16)):
    list16[i] = bytearray.fromhex(list16[i]).decode("utf-8")
    list17.append(list16[i])
# print(list17)

decoded_message2 = ''.join(list17)
# print("PARTNER_MESSAGE_AFTER_DECRYPT = " + str(decoded_message2))

print("# IS_VALID_SIGNATURE should be True or False")

if PARTNER_SIGNED_MESSAGE == decoded_message2:
    print("IS_VALID_SIGNATURE = True")
else:
    print("IS_VALID_SIGNATURE = False") 
