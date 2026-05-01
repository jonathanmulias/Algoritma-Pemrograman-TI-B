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

def tampilkan_tree(folder: dict, nama: str = "root", level: int = 0):
    for nama_item, isi in folder.items():
        
        indent = "  " * level
        
        if isinstance(isi, dict):
            print(f"{indent}(FOLDER) {nama_item}")
            tampilkan_tree(isi, nama_item, level + 1)
        else:
            print(f"{indent}(FILE) {nama_item} ({isi} KB)")

tampilkan_tree(struktur)