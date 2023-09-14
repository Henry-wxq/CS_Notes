import pytest
from survey import Question, Answer, Survey, MultipleChoiceQuestion, \
    InvalidAnswerError
from survey import YesNoQuestion, NumericQuestion, CheckboxQuestion
from course import Student, Course
from criterion import Criterion, HomogeneousCriterion, HeterogeneousCriterion, \
    LonelyMemberCriterion
from grouper import AlphaGrouper, GreedyGrouper, Group, Grouping


# You may need to import pytest in order to run your tests.
# You are free to import hypothesis and use hypothesis for testing.
# This file will not be graded for style with PythonTA

###############################################################################
# Task 2 Test cases
###############################################################################


def test_has_answer() -> None:
    q1 = YesNoQuestion(1, "Male?")
    q2 = MultipleChoiceQuestion(2, "Sex?", ["Male", "Female"])
    s1 = Student(1, "David")
    s2 = Student(2, "Henry")
    s1.set_answer(q1, Answer(True))
    s2.set_answer(q2, Answer("Male"))
    assert s1.has_answer(q1) is True
    assert s1.has_answer(q2) is False
    assert s2.has_answer(q1) is False
    assert s2.has_answer(q2) is True


def test_set_answer() -> None:
    q1 = Question(1, "Name?")
    q2 = Question(2, "ID?")
    s1 = Student(1, "David")
    s1.set_answer(q1, Answer("David"))
    s1.set_answer(q2, Answer(1))
    assert s1.get_answer(q1).content == Answer("David").content
    assert s1.get_answer(q2).content == Answer(1).content
    s1.set_answer(q1, Answer("Henry"))
    assert s1.get_answer(q1).content == Answer("Henry").content


def test_get_answer() -> None:
    q1 = Question(1, "Name?")
    q2 = Question(2, "ID?")
    s1 = Student(1, "David")
    assert s1.get_answer(q1) is None
    s1.set_answer(q1, Answer("David"))
    assert s1.get_answer(q1).content == Answer("David").content
    assert s1.get_answer(q2) is None


###############################################################################
# Task 3 Test cases
###############################################################################


@pytest.fixture
def course() -> Course:
    return Course('csc148')


@pytest.fixture
def students() -> list[Student]:
    return [Student(1, 'Zoro'),
            Student(2, 'Aaron'),
            Student(3, 'Gertrude'),
            Student(4, 'Yvette')]


def test_enroll_students(course: Course, students: list[Student]) -> None:
    course.enroll_students(students)
    assert len(course.students) == 4
    assert course.students == students

    duplicated_student = Student(1, "Zoro")
    course.enroll_students([duplicated_student])
    assert len(course.students) == 4
    assert course.students == students

    course.enroll_students([])
    assert len(course.students) == 4
    assert course.students == students


def test_all_answered(course: Course) -> None:
    survey = Survey([])
    assert course.all_answered(survey) is False

    options = ["A", "B", "C"]
    question1 = MultipleChoiceQuestion(1, "Question 1", options)
    survey = Survey([question1])

    assert course.all_answered(survey) is False

    student1 = Student(1, "David")
    student2 = Student(2, "Henry")
    course.students.append(student1)
    course.students.append(student2)

    student1.set_answer(question1, Answer("A"))
    assert course.all_answered(survey) is False

    student2.set_answer(question1, Answer("D"))
    assert course.all_answered(survey) is False

    student2.set_answer(question1, Answer("B"))
    assert course.all_answered(survey) is True


def test_get_students(course: Course, students: list[Student]) -> None:
    assert course.get_students() == ()

    sorted_students = sorted(students, key=lambda s: s.id)
    course.enroll_students(students)
    assert course.get_students() == tuple(sorted_students)


###############################################################################
# Task 4 Test cases
###############################################################################


def test_init():
    q = YesNoQuestion(1, "Do you like ice cream?")
    assert q.id == 1
    assert q.text == "Do you like ice cream?"


def test_validate_answer():
    q = YesNoQuestion(1, "Do you like ice cream?")
    assert q.validate_answer(Answer(True))
    assert q.validate_answer(Answer(False))
    assert not q.validate_answer(Answer(42))
    assert not q.validate_answer(Answer("Yes"))


def test_get_similarity():
    q = YesNoQuestion(1, "Do you like ice cream?")
    a1 = Answer(True)
    a2 = Answer(True)
    a3 = Answer(False)
    assert q.get_similarity(a1, a2) == 1.0
    assert q.get_similarity(a1, a3) == 0.0


def test_get_id():
    q = YesNoQuestion(1, "Do you like ice cream?")
    assert q.id == 1


def test_get_text():
    q = YesNoQuestion(1, "Do you like ice cream?")
    assert q.text == "Do you like ice cream?"


###############################################################################
# Task 5 Test cases
###############################################################################


def test_is_valid():
    q = YesNoQuestion(1, "Do you like ice cream?")
    a1 = Answer(True)
    a2 = Answer("Yes")

    assert a1.is_valid(q) is True
    assert a2.is_valid(q) is False


###############################################################################
# Task 6 Test cases
###############################################################################


def test_homogeneous_criterion_score_answers():
    # Test with one valid answer
    question = NumericQuestion(1, "How old are you?", 0, 100)
    answer = [Answer(25)]
    criterion = HomogeneousCriterion()
    assert criterion.score_answers(question, answer) == 1.0

    # Test with identical valid answers
    question = YesNoQuestion(2, "Are you a student?")
    answer = [Answer(True), Answer(True), Answer(True)]
    criterion = HomogeneousCriterion()
    assert criterion.score_answers(question, answer) == 1.0

    # Test with different valid answers
    question = YesNoQuestion(2, "Are you a student?")
    answer = [Answer(True), Answer(False), Answer(True)]
    criterion = HomogeneousCriterion()
    assert criterion.score_answers(question, answer) == 1 / 3

    # Test with different valid answers
    question = MultipleChoiceQuestion(3, "What is your favorite color?",
                                      ["Red", "Green", "Blue"])
    answer = [Answer("Red"), Answer("Green"),
              Answer("Blue")]
    criterion = HomogeneousCriterion()
    assert criterion.score_answers(question, answer) == 0.0

    # Test with a mix of valid and invalid answers
    # TODO: Check Correctness
    question = MultipleChoiceQuestion(3, "What is your favorite color?",
                                      ["Red", "Green", "Blue"])
    answer = [Answer("Red"), Answer("Green"),
              Answer("Blue"), Answer("Yellow")]
    criterion = HomogeneousCriterion()
    with pytest.raises(InvalidAnswerError):
        criterion.score_answers(question, answer)


###############################################################################
# Task 7 Test cases
###############################################################################


def test_len():
    # Test __len__ method for Group with 3 members
    s1 = Student(1, "Alice")
    s2 = Student(2, "Bob")
    s3 = Student(3, "Charlie")
    g = Group([s1, s2, s3])
    assert len(g) == 3


def test_contains_true():
    # Test __contains__ method for Group with matching student id
    s1 = Student(1, "Alice")
    s2 = Student(2, "Bob")
    g = Group([s1, s2])
    assert s1 in g


def test_contains_false():
    # Test __contains__ method for Group without matching student id
    s1 = Student(1, "Alice")
    s2 = Student(2, "Bob")
    g = Group([s1])
    assert s2 not in g


def test_get_members():
    # Test get_members method for Group with 3 members
    s1 = Student(1, "Alice")
    s2 = Student(2, "Bob")
    s3 = Student(3, "Charlie")
    g = Group([s1, s2, s3])
    members = g.get_members()
    assert len(members) == 3
    assert s1 in members
    assert s2 in members
    assert s3 in members


###############################################################################
# Task 8 Test cases
###############################################################################


def test_add_group():
    # Creating some students
    s1 = Student(1, "Alice")
    s2 = Student(2, "Bob")
    s3 = Student(3, "Charlie")
    s4 = Student(4, "Dave")
    s5 = Student(5, "Eve")

    # Creating some groups
    g1 = Group([s1, s2])
    g2 = Group([s3, s4])

    # Creating an empty grouping
    grouping = Grouping()

    # Adding a valid group
    assert grouping.add_group(g1) is True
    assert len(grouping) == 1

    # Adding a group with a duplicate student
    g3 = Group([s2, s5])
    assert grouping.add_group(g3) is False
    assert len(grouping) == 1

    # Adding another valid group
    assert grouping.add_group(g2) is True
    assert len(grouping) == 2


def test_check_len():
    # Creating some students
    s1 = Student(1, "Alice")
    s2 = Student(2, "Bob")
    s3 = Student(3, "Charlie")

    # Creating some groups
    g1 = Group([s1, s2])
    g2 = Group([s3])

    # Creating an empty grouping
    grouping = Grouping()

    # Testing length of empty grouping
    assert len(grouping) == 0

    # Adding groups and testing length
    grouping.add_group(g1)
    assert len(grouping) == 1

    grouping.add_group(g2)
    assert len(grouping) == 2


###############################################################################
# Task 9 Test cases
###############################################################################


def test_get_questions():
    q1 = Question(1, "What is your favorite color?")
    q2 = Question(2, "What is your favorite animal?")
    q3 = Question(3, "How many siblings do you have?")
    questions = [q1, q2, q3]
    survey = Survey(questions)
    assert survey.get_questions() == questions


def test_set_weight():
    q1 = Question(1, "What is your favorite color?")
    survey = Survey([q1])
    survey.set_weight(2, q1)
    assert survey._weights[1] == 2


def test_set_criterion():
    q1 = Question(1, "What is your favorite color?")
    survey = Survey([q1])
    criterion = HomogeneousCriterion()
    survey.set_criterion(criterion, q1)
    assert survey._criteria[1] == criterion


def test_score_students():
    questions = [MultipleChoiceQuestion(1, 'why?', ['Y', 'Z']),
                 NumericQuestion(2, 'what?', 3, 5)]

    answers = [[Answer('Y'), Answer('Z'), Answer('Y'), Answer('Z')],
               [Answer(3), Answer(4), Answer(5), Answer(4)]]

    criteria = [HomogeneousCriterion(), HeterogeneousCriterion()]

    weights = [5, 5]

    students = [Student(1, 'David'), Student(2, 'Henry')]

    survey = Survey(questions)
    for i, question in enumerate(questions):
        survey.set_weight(weights[i], question)
        survey.set_criterion(criteria[i], question)

    for i, student in enumerate(students):
        for j, question in enumerate(questions):
            student.set_answer(question, answers[j][i])

    score = survey.score_students(students)
    assert round(score, 2) == 1.25


def test_score_grouping():
    questions = [MultipleChoiceQuestion(1, 'why?', ['Y', 'Z']),
                 NumericQuestion(2, 'what?', 3, 5)]

    answers = [[Answer('Y'), Answer('Z'), Answer('Y'), Answer('Z')],
               [Answer(3), Answer(4), Answer(5), Answer(4)]]

    criteria = [HomogeneousCriterion(), HeterogeneousCriterion()]

    weights = [5, 5]

    students = [Student(1, 'David'), Student(2, 'Henry')]

    survey = Survey(questions)
    for i, question in enumerate(questions):
        survey.set_weight(weights[i], question)
        survey.set_criterion(criteria[i], question)

    for i, student in enumerate(students):
        for j, question in enumerate(questions):
            student.set_answer(question, answers[j][i])

    grouping = Grouping()
    grouping.add_group(Group([students[0]]))
    grouping.add_group(Group([students[1]]))

    score = survey.score_grouping(grouping)
    assert round(score, 2) == 2.5


###############################################################################
# Task 10 Test cases
###############################################################################
@pytest.fixture
def alpha_grouping(students_with_answers) -> Grouping:
    grouping = Grouping()
    grouping.add_group(Group([students_with_answers[0]]))
    grouping.add_group(Group([students_with_answers[1],
                              students_with_answers[2],
                              students_with_answers[3]]))
    return grouping


@pytest.fixture
def students() -> list[Student]:
    return [Student(1, 'Zoro'),
            Student(2, 'Aaron'),
            Student(3, 'Gertrude'),
            Student(4, 'Yvette')]


@pytest.fixture
def answers() -> list[list[Answer]]:
    return [[Answer('a'), Answer('b'),
             Answer('a'), Answer('b')],
            [Answer(0), Answer(4),
             Answer(-1), Answer(1)],
            [Answer(True), Answer(False),
             Answer(True), Answer(True)],
            [Answer(['a', 'b']), Answer(['a', 'b']),
             Answer(['a']), Answer(['b'])]]


@pytest.fixture
def students_with_answers(students, questions, answers) -> list[Student]:
    for i, student in enumerate(students):
        for j, question in enumerate(questions):
            student.set_answer(question, answers[j][i])
    return students


@pytest.fixture
def empty_course() -> Course:
    return Course('csc148')


@pytest.fixture
def criteria(answers) -> list[Criterion]:
    return [HomogeneousCriterion(),
            HeterogeneousCriterion(),
            LonelyMemberCriterion(),
            HomogeneousCriterion()]


@pytest.fixture()
def weights() -> list[int]:
    return [2, 5, 7, 4]


@pytest.fixture
def survey_(questions, criteria, weights) -> Survey:
    s = Survey(questions)
    for i, question in enumerate(questions):
        s.set_weight(weights[i], question)
        s.set_criterion(criteria[i], question)
    return s


@pytest.fixture
def course_with_students(empty_course, students) -> Course:
    empty_course.enroll_students(students)
    return empty_course


@pytest.fixture
def course_with_students_with_answers(empty_course,
                                      students_with_answers) -> Course:
    empty_course.enroll_students(students_with_answers)
    return empty_course


@pytest.fixture
def questions() -> list[Question]:
    return [MultipleChoiceQuestion(1, 'why?', ['a', 'b']),
            NumericQuestion(2, 'what?', -2, 4),
            YesNoQuestion(3, 'really?'),
            CheckboxQuestion(4, 'how?', ['a', 'b', 'c'])]


@pytest.fixture
def greedy_grouping(students_with_answers) -> Grouping:
    grouping = Grouping()
    grouping.add_group(Group([students_with_answers[0],
                              students_with_answers[1],
                              students_with_answers[2]]))
    grouping.add_group(Group([students_with_answers[3]]))
    return grouping


def get_member_ids(grouping: Grouping) -> set[frozenset[int]]:
    member_ids = set()
    for group in grouping.get_groups():
        ids = []
        for member in group.get_members():
            ids.append(member.id)
        member_ids.add(frozenset(ids))
    return member_ids


def compare_groupings(grouping1: Grouping,
                      grouping2: Grouping) -> None:
    assert get_member_ids(grouping1) == get_member_ids(grouping2)


class TestAlphaGrouper:
    def test_make_grouping(self, course_with_students_with_answers,
                           alpha_grouping,
                           survey_) -> None:
        grouper_ = AlphaGrouper(3)
        grouping = grouper_.make_grouping(course_with_students_with_answers,
                                          survey_)
        compare_groupings(grouping, alpha_grouping)


class TestGreedyGrouper:
    def test_make_grouping(self, course_with_students_with_answers,
                           greedy_grouping,
                           survey_) -> None:
        grouper_ = GreedyGrouper(3)
        grouping = grouper_.make_grouping(course_with_students_with_answers,
                                          survey_)
        compare_groupings(grouping, greedy_grouping)
