struktur = {
    "Skripsi_Aqil": {
        "Bab_1": {
            "pendahuluan.docx": 45,
            "latar_belakang.docx": 62
        },
        "Bab_2": {
            "landasan_teori.docx": 118,
            "referensi": {
            "paper_A.pdf": 340,
            "paper_B.pdf": 210
        }
        },
        "Bab_3": {
            "metodologi.docx": 89,
            "diagram": {
                "flowchart.png": 512,
                "erd.png": 278,
                "arsitektur": {
                    "sistem.png": 430
                }
            }
        },
    "sidang": {
        "presentasi.pptx": 2048,
        "catatan_revisi.txt": 15
    },
    "README_txt": 8
    }
}

def cari_terbesar(folder: dict) -> tuple:
    terbesar = ("", 0)
    
    for nama, isi in folder.items():
        if isinstance(isi, dict):
            hasil = cari_terbesar(isi)
        else:                     
            hasil = (nama, isi)

        if hasil[1] > terbesar[1]:
            terbesar = hasil
            
    return terbesar 

nama, ukuran = cari_terbesar(struktur)
print(f"File terbesar: {nama} ({ukuran} KB)")
