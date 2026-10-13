class Student {
  constructor(name, semester) {
    this.name = name;
    this.semester = semester;
  }

  displayDetails() {
    console.log(`Name: ${this.name}`);
    console.log(`Semester: ${this.semester}`);
  }
}

class CSEStudent extends Student {
  constructor(name, semester, branch) {
    super(name, semester);
    this.branch = branch;
  }

  displayBranch() {
    console.log(`Branch: ${this.branch}`);
  }
}

const student = new CSEStudent("Sehaj Vohra", 5, "CSE");

student.displayDetails();
student.displayBranch();
