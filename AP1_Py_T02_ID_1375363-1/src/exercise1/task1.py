import random as rd
import multiprocessing as mp
from queue import Empty
import time


class Person:
    def __init__(self, name, gender):
        self.__name = name
        self.__gender = gender

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        if name.isalpha():
            self.__name = name
        else:
            print("Invalid name. Name must contain only alphabetic characters.")

    @property
    def gender(self):
        return self.__gender
    
    @gender.setter
    def gender(self, gender):
        if gender in ["М", "Ж"]:
            self.__gender = gender
        else:
            print("Invalid gender. Gender must be 'М' or 'Ж'.")

        
class Student(Person):
    def __str__(self):
        return f"Name: {self.name}, Gender: {self.gender}"

    def choose_word(self, question):
        phi = 1.618
        weights = []
        remaining = 1.0 
        words = question.question_text.split()
        for i in range(len(words)):
            if i != len(words) - 1:
                weight = remaining / phi
                weights.append(weight)
                remaining -= weight
            else:
                weights.append(remaining)
        if self.gender == "Ж":
            weights.reverse()
        
        choosen_word = rd.choices(words, weights=weights, k=1)[0]
        return choosen_word

class Examiner(Person):
    def __str__(self):
        return f"Name: {self.name}, Gender: {self.gender}"
    
    def choose_correct_word(self, question):
        phi = 1.618
        weights = []
        remaining = 1.0 
        words = question.question_text.split()
        correct_words = []
        for i in range(len(words)):
            if i != len(words) - 1:
                weight = remaining / phi
                weights.append(weight)
                remaining -= weight
            else:
                weights.append(remaining)
        if self.gender == "Ж":
            weights.reverse()
        
        choosen_correct_word = rd.choices(words, weights=weights, k=1)[0]
        correct_words.append(choosen_correct_word)
        words.remove(choosen_correct_word)
        while rd.random() < 1/3 and len(words) > 0:
            choosen_correct_word = rd.choice(words)
            correct_words.append(choosen_correct_word)
            words.remove(choosen_correct_word)
        
        return correct_words
    
    def get_mood(self):
        mood = ''
        ind_mood = rd.random()
        if ind_mood < 1/8:
            mood = "bad"
        elif ind_mood < 1/4 + 1/8:
            mood = "good"
        else:
            mood = "neutral"
        
        return mood
    
    def get_exam_time(self):
        exam_time = rd.uniform(len(self.name) - 1, len(self.name) + 1)
        
        return exam_time
    
    def exam_result(self, student, questions_bank):
        correct_count = 0
        incorrect_count = 0
        total_questions = 3
        question_results = []

        for _ in range(total_questions):
            question_answer = rd.choice(questions_bank)
            correct_word = self.choose_correct_word(question_answer)
            student_answer = student.choose_word(question_answer)

            is_correct = student_answer in correct_word
            if is_correct:
                correct_count += 1
            else:
                incorrect_count += 1
    
            question_results.append({
                'question_text': question_answer.question_text,
                'is_correct': is_correct
            })
        
        mood = self .get_mood()
        exam_time = self.get_exam_time()

        if mood == "good":
            status = "Сдал"
        elif mood == "bad":
            status = "Провалил"
        else: 
            if correct_count > incorrect_count:
                status = "Сдал"
            else:
                status = "Провалил"
        
        time.sleep(exam_time)

        return mood, status, exam_time, question_results 


class Question:
    def __init__(self, question_text):
        self.question_text = question_text

    def __str__(self):
        return f"Question: {self.question_text}"

def examiner_process(examiner, start_time, student_queue, question_bank, results_queue):
    lunch_taken = False
    student_processed = 0

    while True:
        if lunch_taken == False and time.time() - start_time >= 30:
            lunch_taken = True
            results_queue.put({
                'type': 'lunch',
                'examiner_name': examiner.name
            })

            time.sleep(rd.uniform(12, 18))
        else:
            try:
                student = student_queue.get(timeout=0.5)
            except Empty:
                break

            results_queue.put({
            'type': 'start',
            'examiner_name': examiner.name,
            'student_name': student.name
            })

            mood, status, exam_time, question_results = examiner.exam_result(student, question_bank)
            finish_time = time.time()
            results_queue.put({
            'type': 'finish',
            'examiner_name': examiner.name,
            'student_name': student.name,
            'status': status,
            'finish_time': finish_time,
            'question_results': question_results
        })

def draw_table(data):
    print("\033[H", end="") 
    print("\033[2J", end="")
    
    status_order = {'Очередь': 0, 'Сдал': 1, 'Провалил': 2}
    sorted_data = sorted(data, key=lambda s: status_order[s['status']])
    print("+", "-" * 15, "+", "-" * 10, "+")
    print(f"| {'Студент':<15} | {'Статус':<10} |")
    print("+", "-" * 15, "+", "-" * 10, "+")
    for row in sorted_data:
        print(f"| {row['name']:<15} | {row['status']:<10} |")
    print("+", "-" * 15, "+", "-" * 10, "+")
    
def draw_examiners_table(examiner_data, start_time):
    print(f"\n+{'-'*13}+{'-'*19}+{'-'*19}+{'-'*9}+{'-'*14}+")
    print(f"| {'Экзаменатор':<12}| {'Текущий студент':<18}| {'Всего студентов':<18}| {'Завалил':<8}| {'Время работы':<13}|")
    print(f"+{'-'*13}+{'-'*19}+{'-'*19}+{'-'*9}+{'-'*14}+")
    
    for name, data in examiner_data.items():
        if data['start_work_time'] is not None:
            work_time = time.time() - data['start_work_time']
        else:
            work_time = 0.0
        
        print(f"| {name:<12}| {data['current_student']:<18}| {str(data['total_students']):<18}| {str(data['failed_count']):<8}| {work_time:<13.2f}|")
    
    print(f"+{'-'*13}+{'-'*19}+{'-'*19}+{'-'*9}+{'-'*14}+")


if __name__ == '__main__':
    students_list = []
    examiners_list = []
    questions_list = []

    with open("students.txt", "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            else:
                name, gender = line.split(" ")
                student = Student(name, gender)
                students_list.append(student)
    with open("examiners.txt", "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            else:
                name, gender = line.split(" ")
                examiner = Examiner(name, gender)
                examiners_list.append(examiner)
    with open("questions.txt", "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            else:
                question_text = line
                question = Question(question_text)
                questions_list.append(question)

    students_queue = mp.Queue()
    results_queue = mp.Queue()

    for student in students_list:
        students_queue.put(student)

    student_data = [{'name': s.name, 'status': 'Очередь', 'time': 0.0} for s in students_list]
    examiner_data = {
        e.name: {
            'current_student': '-',
            'total_students': 0,
            'failed_count': 0,
            'start_work_time': None
        }
        for e in examiners_list
    }
    start_time = time.time()    
    processes = []

    question_stats = {}

    for examiner in examiners_list:
        p = mp.Process(
        target=examiner_process,
        args=(examiner, start_time, students_queue, questions_list, results_queue)
        )
        p.start()
        processes.append(p)

    processed_count = 0
    total_students = len(students_list)

    while processed_count < total_students:
        try:
            result = results_queue.get(timeout=0.5)

            if result['type'] == 'start':
                examiner_data[result['examiner_name']]['current_student'] = result['student_name']
                if examiner_data[result['examiner_name']]['start_work_time'] is None:
                    examiner_data[result['examiner_name']]['start_work_time'] = time.time()

            elif result['type'] == 'finish':
                examiner_data[result['examiner_name']]['current_student'] = '-'
                examiner_data[result['examiner_name']]['total_students'] += 1
                if result['status'] == 'Провалил':
                    examiner_data[result['examiner_name']]['failed_count'] += 1

                for student in student_data:
                    if student['name'] == result['student_name']:
                        student['status'] = result['status']
                        student['time'] = result['finish_time'] - start_time
                        break
    
                for qr in result['question_results']:
                    q_text = qr['question_text']
                    if qr['is_correct']:
                        question_stats[q_text] = question_stats.get(q_text, 0) + 1
                    else:
                        question_stats[q_text] = question_stats.get(q_text, 0)
                processed_count += 1

            elif result['type'] == 'lunch':
                examiner_data[result['examiner_name']]['current_student'] = '-'

        except Empty:
            pass

        draw_table(student_data)
        draw_examiners_table(examiner_data, start_time)
        elapsed_time = time.time() - start_time
        queue_count = sum(1 for s in student_data if s['status'] == 'Очередь')
        print(f"\nОсталось в очереди: {queue_count} из {total_students}")
        print(f"Время с начала экзамена: {elapsed_time:.2f}")
        time.sleep(0.5)
    
    for p in processes:
        p.join()

    print("\033[H\033[2J", end="")
    print("\n=== РЕЗУЛЬТАТЫ ЭКЗАМЕНА ===\n")
    draw_table(student_data)
    draw_examiners_table(examiner_data, start_time)

    elapsed_time = time.time() - start_time
    print(f"\nВремя с момента начала экзамена и до момента его завершения: {elapsed_time:.2f}")

    passed_students = [s for s in student_data if s['status'] == 'Сдал']
    failed_students = [s for s in student_data if s['status'] == 'Провалил']

    if passed_students:
        best_students = sorted(passed_students, key=lambda s: s['time'])
        best_time = best_students[0]['time']
        best_student_names = [s['name'] for s in best_students if s['time'] == best_time]
        print(f"Имена лучших студентов: {', '.join(best_student_names)}")
    else:
        print("Имена лучших студентов: -")

    best_examiners = []
    min_fail_rate = 1.0
    for name, data in examiner_data.items():
        if data['total_students'] > 0:
            fail_rate = data['failed_count'] / data['total_students']
            if fail_rate < min_fail_rate:
                min_fail_rate = fail_rate
                best_examiners = [name]
            elif fail_rate == min_fail_rate:
                best_examiners.append(name)

    if best_examiners:
        print(f"Имена лучших экзаменаторов: {', '.join(best_examiners)}")
    else:
        print("Имена лучших экзаменаторов: -")

    if failed_students:
        failed_sorted = sorted(failed_students, key=lambda s: s['time'])
        earliest_fail_time = failed_sorted[0]['time']
        expelled = [s['name'] for s in failed_sorted if s['time'] == earliest_fail_time]
        print(f"Имена студентов, которых после экзамена отчислят: {', '.join(expelled)}")
    else:
        print("Имена студентов, которых после экзамена отчислят: -")

    if question_stats:
        max_correct = max(question_stats.values())
        best_questions = [q for q, count in question_stats.items() if count == max_correct]
        print(f"Лучшие вопросы: {', '.join(best_questions)}")
    else:
        print("Лучшие вопросы: -")

    pass_rate = len(passed_students) / total_students if total_students > 0 else 0
    if pass_rate > 0.85:
        print("Вывод: экзамен удался")
    else:
        print("Вывод: экзамен не удался")