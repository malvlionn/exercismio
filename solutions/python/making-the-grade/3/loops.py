"""Functions for organizing and calculating student exam scores."""

def round_scores(student_scores):
    nilaibaru =[]
    for nilai in student_scores:
        nilaibaru.append(round(nilai))
    return nilaibaru

def count_failed_students(student_scores):
    remedkocak = 0
    for nilai in student_scores:
        if nilai <= 40:
            remedkocak += 1
    return remedkocak
    
def above_threshold(student_scores, threshold):
    cielolos = []
    for nilai in student_scores:
        if nilai >= threshold:
            cielolos.append(nilai)
    return cielolos
    
def letter_grades(highest):
    increment = int((highest-40)/4)
    batasaman = []
    batas = 41
    while batas < highest:
        batasaman.append((batas))
        batas += increment
    return batasaman

def student_ranking(student_scores, student_names):
    listgabung = []
    for nourut,nilai in enumerate(student_scores):
        gabungan = str(nourut+1) + ". " + student_names[nourut] + ": " + str(nilai)
        listgabung.append(gabungan)
    return listgabung

def perfect_score(student_info):
    for gabung in student_info:
        if gabung[1] == 100:
            return gabung
    return []
