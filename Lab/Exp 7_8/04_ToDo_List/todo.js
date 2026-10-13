const taskInput = document.getElementById("taskInput");
const addBtn = document.getElementById("addBtn");
const taskList = document.getElementById("taskList");
const taskCount = document.getElementById("taskCount");

let tasks = JSON.parse(localStorage.getItem("tasks")) || [];

const saveTasks = () => {
  localStorage.setItem("tasks", JSON.stringify(tasks));
};

const updateTaskCount = () => {
  taskCount.textContent = `Total tasks: ${tasks.length}`;
};

const renderTasks = () => {
  taskList.innerHTML = "";

  tasks.forEach((task, index) => {
    const li = document.createElement("li");

    const taskText = document.createElement("span");
    taskText.textContent = task.title;

    if (task.completed) {
      taskText.style.textDecoration = "line-through";
      taskText.style.color = "gray";
    }

    taskText.addEventListener("click", () => {
      tasks[index].completed = !tasks[index].completed;
      saveTasks();
      renderTasks();
    });

    const deleteBtn = document.createElement("button");
    deleteBtn.textContent = "Delete";

    deleteBtn.addEventListener("click", () => {
      tasks.splice(index, 1);
      saveTasks();
      renderTasks();
    });

    li.append(taskText, deleteBtn);
    taskList.appendChild(li);
  });

  updateTaskCount();
};

const addTask = () => {
  const title = taskInput.value.trim();

  if (title === "") {
    return;
  }

  tasks.push({
    title: title,
    completed: false,
  });

  saveTasks();
  renderTasks();

  taskInput.value = "";
};

addBtn.addEventListener("click", addTask);

taskInput.addEventListener("keydown", (event) => {
  if (event.key === "Enter") {
    addTask();
  }
});

renderTasks();
