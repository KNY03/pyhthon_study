# 2026.03.25

class Sungjuk:
    def __init__(self):
        self._student_num = ""
        self._student_name = ""

        self._student_kor = 0
        self._student_math = 0
        self._student_eng = 0

        self._total = 0
        self._avg = 0.0
        self._grade = ""

    # --- student number ---
    def get_student_num(self):
        return self._student_num

    def set_student_num(self, num):
        self._student_num = num

    num = property(get_student_num, set_student_num)

    # --- student name ---
    def get_student_name(self):
        return self._student_name

    def set_student_name(self, name):
        self._student_name = name

    name = property(get_student_name, set_student_name)

    # --- kor ---
    def get_student_korean_score(self):
        return self._student_kor

    def set_student_korean_score(self, kor):
        self._student_kor = kor

    kor = property(get_student_korean_score, set_student_korean_score)

    # --- math ---
    def get_student_math_score(self):
        return self._student_math

    def set_student_math_score(self, math):
        self._student_math = math

    math = property(get_student_math_score, set_student_math_score)

    # --- eng ---
    def get_student_english_score(self):
        return self._student_eng

    def set_student_english_score(self, eng):
        self._student_eng = eng

    eng = property(get_student_english_score, set_student_english_score)

    # --- total ---
    def get_student_total(self):
        return self._total

    def set_student_total(self, total):
        self._total = total

    total = property(get_student_total, set_student_total)

    # --- avg ---
    def get_student_avg(self):
        return self._avg

    def set_student_avg(self, avg):
        self._avg = avg  # 오타 수정

    avg = property(get_student_avg, set_student_avg)

    # --- grade ---
    def get_student_grade(self):
        return self._grade

    def set_student_grade(self, grade):
        self._grade = grade

    grade = property(get_student_grade, set_student_grade)

    # --------------------------
    def input_info(self):
        self._student_num = input("Input student number: ").strip()
        self._student_name = input("Input student name: ").strip()

    def input_score(self):
        self._student_kor = int(input("Input student korean score: "))
        self._student_math = int(input("Input student math score: "))
        self._student_eng = int(input("Input student english score: "))

    def calc_grade(self):
        self._total = self._student_kor + self._student_eng + self._student_math
        self._avg = self._total / 3

        if self._avg >= 90:
            self._grade = "수"
        elif self._avg >= 80:
            self._grade = "우"
        elif self._avg >= 70:
            self._grade = "미"
        elif self._avg >= 60:
            self._grade = "양"
        else:
            self._grade = "가"

    def output_grade(self):
        print("%4s  %3s  %4d  %4d  %4d  %4d  %6.2f  %2s" %
              (self._student_num, self._student_name,
               self._student_kor, self._student_eng, self._student_math,
               self._total, self._avg, self._grade))

if __name__ == "__main__":
    sungjuk = Sungjuk()
    sungjuk.input_info()
    sungjuk.input_score()
    sungjuk.calc_grade()
    sungjuk.output_grade()