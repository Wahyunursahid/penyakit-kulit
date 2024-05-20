import streamlit as st

def add_bg_from_url():
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpeg;base64,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gCIiAKEvdZ1KmoS92PqVKyRLDKkRFoc5Ju89ERu89EUEEeJROJRSSSZ32dVcqWd9nVXKjybQ9oREVS4REQBERAEREAREQBERAEREAREQBERAEREAREQBERAFCXux9SpqEvdj6lSskSwypERaHOSbvPREbvPRFBBHiUTiUUkkmd9nVXKlnfZ1Vyo8m0PaERFUuEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBQl7sfUqahL3Y+pUrJEsMqREWhzkm7z0RG7z0RQQR4lE4lFJJJnfZ1VypZ32dVcqPJtD2hERVLhERAEREAREQBERAEREAREQBERAEREAREQBERAEREAUJe7H1KmoS92PqVKyRLDKkRFoc5Ju89ERu89EUEEeJROJRSSSZ32dVcqWd9nVXKjybQ9oREVS4REQBERAEREAREQBERAEREAREQBERAEREAREQBETU7rnogChL3Y+pSSWCL62WKP+8kYz/MVpVmKYbTxU8j5ZZGSySRx+qU1VVlzmC5AFMx3mbKVkNNpmwi5P02119jheLyDgXxU1MD/AL1O137KoqcdxCmp56k4OCyLZksdiMAleHysis0MjLL66XeB4jer3Rj05HfbvPRFqYbiFDiVOKmkkLmXMcjHgsmglFrxTxntNcOR6i4NyQo00bPEonEopBJnfZ1VypZ32dVcqPJtD2hERVLhERAEREAREQBERAEREAREQBERAEREAREQBERSDTmdUullaycxRsLWgRxxl5uwOJL5A7nwaqjTRvHtX1Ev97PK4H/CCG/BXO+vqhyfF/ympz8RZVNUuDl1r2UYj9UZTMe7PmLYonOBA01IWzUTx1FLSvjcXN2srSSCNQBfQrmVdE+B0bY3STPlbI6zI3HLYgAC1/iV0poIqekpI48wG1lccxLjmIBOqzi5OTudlWFONKLi+TUWhjJ/1bUj7UtC3zqoiugubjemHOH2qyhHlLm/BbM4zzgEzJHTU1XWUc7mNjkloZtjJLG03ayQ2IIHC40vodbEptRZlj6XxKJxKLoPPJM77OquVLO+zqrlR5Noe0IiKpcIiIAiIgCIiAIiIAiIgCIiAIiIAihLNBC3NNIyNvAvcAT0G8+S58uMUzbiGOSU83eyZ5uu79lVclHLNIUpz9qOmm4EnQDUk6AdSV5+TFMQk0a6OEf2TAXfpSX+QWlLIXm9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");
            background-size: cover;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Define symptoms and their associated diseases with expert CF values
symptoms = {
    "GJ01": {"description": "Gatal pada kulit dibagian area kulit yang kemerahan", "diseases": {"Eksim": 0.2}},
    "GJ02": {"description": "Tanda kemerahan biasanya muncul pada wajah, lutut, tangan, dan kaki", "diseases": {"Eksim": 0.6}},
    "GJ03": {"description": "Daerah pada kulit yang memerah dan gatal terasa kering", "diseases": {"Eksim": 0.2}},
    "GJ04": {"description": "Daerah pada kulit yang memerah berkerut", "diseases": {"Eksim": 0.2}},
    "GJ05": {"description": "Kulit pecah-pecah", "diseases": {"Eksim": 0.1}},
    "GJ06": {"description": "Kulit seperti bersisik", "diseases": {"Eksim": 0.1}},
    "GJ07": {"description": "Kulit menebal", "diseases": {"Eksim": 0.1}},
    "GJ08": {"description": "Kulit mengalami pembengkakan saat digaruk", "diseases": {"Eksim": 0.1}},
    "GJ09": {"description": "Area kemerahan lama kelamaan berubah warna menjadi lebih gelap", "diseases": {"Eksim": 0.15}},
    "GJ10": {"description": "Bintik kemerahan pada kulit yang biasanya terjadi dihampari seluruh bagian kulit", "diseases": {"Campak": 0.6}},
    "GJ11": {"description": "Demam", "diseases": {"Campak": 0.2}},
    "GJ12": {"description": "Pilek", "diseases": {"Campak": 0.1}},
    "GJ13": {"description": "Mata meradang atau terasa panas", "diseases": {"Campak": 0.1}},
    "GJ14": {"description": "Sakit tenggorokan", "diseases": {"Campak": 0.1}},
    "GJ15": {"description": "Batuk", "diseases": {"Campak": 0.1}},
    "GJ16": {"description": "Ruam kulit", "diseases": {"Campak": 0.2}},
    "GJ17": {"description": "Terdapat bercak luka pada kulit yang memerah", "diseases": {"Kudis": 0.3}},
    "GJ18": {"description": "Ruam kulit yang menyerupai jerawat, khususnya dibagian lipatan tangan dan kaki, bokong dan ketiak", "diseases": {"Kudis": 0.6}},
    "GJ19": {"description": "Merasa gatal yang parah pada area tertentu terutama dimalam hari", "diseases": {"Kudis": 0.4}},
    "GJ20": {"description": "Kulit seperti berkerak", "diseases": {"Kudis": 0.25}},
    "GJ21": {"description": "Ruam pada kulit yang terasa nyeri dan panas", "diseases": {"Herpes": 0.2}},
    "GJ22": {"description": "Ruam mulai berair seperti luka melupah", "diseases": {"Herpes": 0.6}},
    "GJ23": {"description": "Lepuhan berisi cairan mudah pecah", "diseases": {"Herpes": 0.3}},
    "GJ24": {"description": "Kulit terasa gatal yang tidak berhenti", "diseases": {"Herpes": 0.1}},
    "GJ25": {"description": "Sakit kepala", "diseases": {"Herpes": 0.1}},
    "GJ26": {"description": "Merasa kelelahan", "diseases": {"Herpes": 0.1}},
    "GJ27": {"description": "Kesemutan pada kulit", "diseases": {"Herpes": 0.1}},
    "GJ28": {"description": "Lepuhan yang mengering menjadi koreng", "diseases": {"Herpes": 0.2}},
    "GJ29": {"description": "Sensitive terhadap sentuhan pada kulit yang terinfeksi", "diseases": {"Herpes": 0.2}},
    "GJ30": {"description": "Bercak merah pada kulit yang diatasnya terdapat sisik putih", "diseases": {"Psoriasis": 0.3}},
    "GJ31": {"description": "Sisik putih diatas kemerah terasa tebal dan berlapis", "diseases": {"Psoriasis": 0.5}},
    "GJ32": {"description": "Kulit pecah-pecah kadang berdarah", "diseases": {"Psoriasis": 0.1}},
    "GJ33": {"description": "Sisik putih pada kulit jika digaruk akan rontok", "diseases": {"Psoriasis": 0.1}},
    "GJ34": {"description": "Ruas permukaan kulit yang terkena makin lama makin membesar atau melebar", "diseases": {"Psoriasis": 0.1}},
    "GJ35": {"description": "Muncul bercak warna lebih muda dari warna kulit", "diseases": {"Vitiligo": 0.5}},
    "GJ36": {"description": "Muncul ruam didaerah kulit yang berwara lebih muda setelah terpapar sinar matahari", "diseases": {"Vitiligo": 0.2}},
    "GJ37": {"description": "Bagian tengah bercak berwarna putih dan tepinya berwarna kecoklatan/kemerahan", "diseases": {"Vitiligo": 0.1}},
    "GJ38": {"description": "Nyeri dan gatal pada bercak kulit yang berwarna lebih muda dari kulit normal", "diseases": {"Vitiligo": 0.2}}
}

# Function to diagnose diseases based on the given symptoms and user responses
def diagnose_diseases(symptoms, user_responses):
    disease_scores = {}
    for symptom_code, symptom_info in symptoms.items():
        user_cf = user_responses.get(symptom_code, 0)  # Default to 0 if no user response
        for disease, expert_cf in symptom_info["diseases"].items():
            if disease not in disease_scores:
                disease_scores[disease] = 0
            combined_cf = expert_cf + user_cf - expert_cf * user_cf
            disease_scores[disease] = max(disease_scores[disease], combined_cf)  # Combining CFs

    return disease_scores

# Streamlit app
def main():
    st.title("Sistem Diagnosa Penyakit Kulit Manusia")

    st.write("Masukan Nilai Kepastian Gejala yang Anda Rasakan : ")
    st.write("0 - Tidak")
    st.write("0.2 - Tidak Yakin")
    st.write("0.4 - Sedikit Yakin")
    st.write("0.6 - Cukup Yakin")
    st.write("0.8 - Yakin")
    st.write("1.0 - Sangat Yakin\n")

    user_responses = {}
    for code, symptom_info in symptoms.items():
        user_responses[code] = st.slider(f"{code}: {symptom_info['description']} (0 to 1):", 0.0, 1.0, 0.0, 0.2)

    if st.button("Diagnosa Sekarang"):
        disease_results = diagnose_diseases(symptoms, user_responses)
        st.write("\n### Disease Diagnostic Results:")
        for disease, score in disease_results.items():
            st.write(f"{disease}: {score * 100:.2f}% certainty level")

if __name__ == "__main__":
    main()
