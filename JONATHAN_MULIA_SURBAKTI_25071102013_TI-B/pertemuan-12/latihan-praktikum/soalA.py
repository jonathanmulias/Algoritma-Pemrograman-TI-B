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

def total_ukuran(folder: dict) -> int:
    total = 0
    
    for isi in folder.values():
        if isinstance(isi, dict):
            total += total_ukuran(isi)
        else:                     
            total += isi
            
    return total

hasil = total_ukuran(struktur)
print(f"Total ukuran skripsi: {hasil} KB")