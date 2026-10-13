const getStudent = () => {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      const student = {
        name: "Sehaj Vohra",
        semester: 5,
      };

      resolve(student);
    }, 2000);
  });
};

const displayStudent = async () => {
  console.log("Fetching student details...");

  try {
    const student = await getStudent();

    console.log("Student Name:", student.name);
    console.log("Semester:", student.semester);
    console.log("Student details fetched successfully.");
  } catch (error) {
    console.log("Error:", error.message);
  }
};

displayStudent();
