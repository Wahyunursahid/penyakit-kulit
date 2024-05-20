import streamlit as st

# Function to apply custom CSS for background image
def set_bg_img(url):
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("{url}");
            background-size: cover;
            background-position: center;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Use this function at the top of your main Streamlit script
set_bg_img("https://drive.google.com/file/d/1jsfT25un8tOfHeKASE3ipQSc7H88PQ5D/view?usp=sharing")  # Replace with your actual image URL

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
        st.write("\n### Persentase Anda Mengidap Penyakit Kulit :")
        for disease, score in disease_results.items():
            st.write(f"{disease}: {score * 100:.2f}%")

if __name__ == "__main__":
    main()
