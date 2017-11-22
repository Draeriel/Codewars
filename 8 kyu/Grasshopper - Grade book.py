def get_grade(s1, s2, s3):
       nota = (s1+s2+s3)/3
       if nota >= 90:
           return "A"
       if nota >= 80:
           return "B"
       if nota >= 70:
           return "C"
       if nota >= 60:
           return "D"
       else:
           return "F"