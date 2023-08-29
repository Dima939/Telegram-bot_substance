MASS = {'H': 1, 'HE': 4, 'LI': 7, 'BE': 9, 'C': 12, 'N': 14, 'O': 16, 'F': 19, 'NE': 20, 'NA': 23, 'MG': 24, 'AL': 27,
        'SI': 28, 'P': 31, 'S': 32, 'CL': 35.5, 'AR': 40, 'K': 39, 'CA': 40, 'SC': 45, 'TI': 48, 'V': 51,
        'CR': 52, 'MN': 55, 'FE': 56, 'CO': 59, 'NI': 59, 'CU': 63.5, 'ZN': 65, 'GA': 70, 'GE': 73, 'AS': 75, 'SE': 79,
        'BR': 80, 'KR': 84, 'RB': 85.5, 'SR': 88, 'Y': 89, 'ZR': 91, 'NB': 93, 'MO': 96, 'TC': 98, 'RU': 101,
        'RH': 103, 'PD': 106, 'AG': 108, 'CD': 112, 'IN': 115, 'SN': 119, 'SB': 122, 'TE': 128, 'I': 127, 'XE': 131,
        'CS': 133, 'BA': 137, 'LA': 139, 'CE': 140, 'PR': 141, 'ND': 144, 'PM': 145, 'SM': 150, 'EU': 152, 'GD': 157,
        'TB': 159, 'DY': 162.5, 'HO': 165, 'ER': 167, 'TM': 169, 'YB': 173, 'LU': 175, 'HF': 178.5, 'TA': 181, 'W': 184,
        'RE': 186, 'OS': 190, 'IR': 192, 'PT': 195, 'AU': 197, 'HG': 200.5, 'TL': 204, 'PB': 207, 'BI': 209, 'PO': 209,
        'AT': 210, 'RN': 222, 'FR': 223, 'RA': 226, 'AC': 227, 'TH': 232, 'PA': 231, 'U': 238, 'NP': 237, 'PU': 244,
        'AM': 243, 'CM': 247, 'BK': 247, 'CF': 251, 'ES': 252, 'FM': 257, 'MD': 258, 'NO': 259, 'LR': 266, 'RF': 267,
        'DB': 268, 'SG': 269, 'BH': 270, 'HS': 269, 'MT': 278, 'DS': 281, 'B': 11}


def func(substance: str):
    substance = substance.upper()
    sub_dict = {}
    mol_mass = 0
    dol_dict = {}

    for i in range(len(substance)):
        if substance[i].isnumeric():
            continue
        if substance[i-1:i+1] in sub_dict.keys():
            continue

        try:
            if substance[i].isalpha() and substance[i+1].isnumeric():
                sub_dict.update({substance[i]: '0'})
                for j in range(i+1, len(substance)):
                    if substance[j].isalpha():
                        break
                    sub_dict[substance[i]] += substance[j]

            else:
                new_substance = substance[i::]
                for p in range(len(substance[i::])):
                    if new_substance in MASS.keys():
                        sub_dict.update({new_substance: '0'})
                        break
                    else:
                        new_substance = new_substance[:len(new_substance) - 1]
                for j in range(i+2, len(substance)):
                    if substance[j].isalpha():
                        break
                    sub_dict[new_substance] += substance[j]

        except IndexError:
            sub_dict.update({substance[i]: '0'})

    for key in sub_dict:
        sub_dict[key] = int(sub_dict[key])
        if sub_dict[key] == 0:
            sub_dict[key] = 1
        mol_mass += MASS[key] * sub_dict[key]

    for key in sub_dict:
        mass_dol = str((MASS[key] * sub_dict[key])/mol_mass*100)
        container = mass_dol.split('.')
        new_mass_dol = f'{container[0]}.{container[1][:3]}%'
        dol_dict.update({key: new_mass_dol})
    return f'Молекулярная масса вещества = {mol_mass} г/моль\nМассовая доля эелементов: {dol_dict}'


