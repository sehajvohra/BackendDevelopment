const name = "Sehaj Vohra";
const semester = 5;
const marks = [80, 85, 90];

const student = {
  name,
  semester,
  marks,

  displayDetails() {
    console.log(`Name: ${this.name}`);
    console.log(`Semester: ${this.semester}`);
    console.log(`Marks: ${this.marks.join(", ")}`);
    console.log(
      `Total Marks: ${this.marks.reduce((total, mark) => total + mark, 0)}`,
    );
  },
};

student.displayDetails();
