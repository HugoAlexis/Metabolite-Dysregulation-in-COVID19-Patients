import matplotlib.pyplot as plt

plt.rcParams['axes.facecolor']='#FFF'
plt.rcParams['figure.facecolor']='#FFF'
plt.rcParams['axes.spines.top']=False
plt.rcParams['axes.spines.left']=False
plt.rcParams['axes.spines.right']=False
plt.rcParams['lines.color']='#071013'
plt.rcParams['text.color']='#071013'
plt.rcParams['axes.titlesize']=12


def label_minmax(vi, xi):
    if vi==0:
        return 'Min'
    elif vi==1:
        return 'Max'
    return f'{100*vi:.0f}%'


metabolites = [
    "Creatinine",
    "Glycine",
    "Alanine",
    "Serine",
    "Proline",
    "Valine",
    "Threonine",
    "Taurine",
    "trans-Hydroxyproline",
    "Leucine",
    "Isoleucine",
    "Asparagine",
    "Aspartic_acid",
    "Glutamine",
    "Glutamic_acid",
    "Methionine",
    "Histidine",
    "alpha-Aminoadipic_acid",
    "Phenylalanine",
    "Methionine-sulfoxide",
    "Arginine",
    "Acetyl-ornithine",
    "Citrulline",
    "Tyrosine",
    "Tryptophan",
    "Kynurenine",
    "Ornithine",
    "Lysine",
    "Sarcosine",
    "Creatine",
    "Betaine",
    "Choline",
    "Methylhistidine",
    "Homocysteine",
    "Lactic_acid",
    "beta-Hydroxybutyric_acid",
    "alpha-Ketoglutaric_acid",
    "Citric_acid",
    "Butyric_acid",
    "Propionic_acid",
    "Succinic_acid",
    "Fumaric_acid",
    "Pyruvic_acid",
    "Isobutyric_acid",
    "Hippuric_acid",
    "Methylmalonic_acid",
    "Homovanillic_acid",
    "Indole_acetic_acid",
    "Uric_acid",
    "Glucose_(mg/dL)",
    "Neutro/Linfo_Radio_NLR",
    "Kynurenine/Tryptophan_",
    "LysoPC_a_C14:0",
    "LysoPC_a_C16:1",
    "LysoPC_a_C16:0",
    "LysoPC_a_C17:0",
    "LysoPC_a_C18:2",
    "LysoPC_a_C18:1",
    "LysoPC_a_C18:0",
    "LysoPC_a_C20:4",
    "LysoPC_a_C20:3",
    "LysoPC_a_C26:0",
    "LysoPC_a_C28:1",
    "SM(OH)_C14:",
    "SM_C16:1",
    "SM_C16:0",
    "SM(OH)_C16:1",
    "SM_C18:1",
    "PC_aa_C32:2",
    "SM_C18:0",
    "SM_C20:2",
    "PC_ae_C36:0",
    "PC_aa_C36:0",
    "SM(OH)_C22:2",
    "SM(OH)_C22:1",
    "PC_aa_C38:6",
    "PC_aa_C38:0",
    "PC_ae_C40:6",
    "SM(OH)_C24:1",
    'Glucose',
    'Asymmetric_dimethylarginine',
    'Creatinine_(mg/dL)',
    'HPHPA',
     'PC_aa_C40:1',
     'PC_aa_C40:2',
     'PC_aa_C40:6',
     'Spermine',
]