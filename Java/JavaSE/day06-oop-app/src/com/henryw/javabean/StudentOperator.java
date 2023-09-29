package com.henryw.javabean;

public class StudentOperator {
    private Student student;

    public StudentOperator(Student student) {
        this.student = student;
    }

    public void printPass() {
        if (student.getScore() >= 60) {
            System.out.println(student.getName() + "成绩及格");
        } else {
            System.out.println(student.getName() + "成绩不及格");
        }
    }
}
