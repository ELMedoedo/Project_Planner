const hamBurger = document.querySelector(".toggle-btn");

hamBurger.addEventListener("click", function () {
  document.querySelector("#sidebar").classList.toggle("expand");
});


// ---------------

document.addEventListener('DOMContentLoaded', function() {
  const makeTaskBtn = document.querySelector('a[href="#"].sidebar-link span:contains("Make task")').closest('a');
  const taskForm = document.getElementById('taskForm');
  const closeBtn = document.querySelector('.btn-close-form');

  // Открытие формы
  makeTaskBtn.addEventListener('click', function(e) {
      e.preventDefault();
      taskForm.classList.add('active');
  });

  // Закрытие формы
  closeBtn.addEventListener('click', function() {
      taskForm.classList.remove('active');
  });

// Закрытие при клике вне формы
document.addEventListener('click', function(e) {
  if (taskForm.classList.contains('active') && 
      !taskForm.contains(e.target) && 
      !makeTaskBtn.contains(e.target)) {
      taskForm.classList.remove('active');
  }
});

  // Обработка отправки формы
  document.querySelector('.task-form-content').addEventListener('submit', function(e) {
      e.preventDefault();
      // Добавьте здесь логику обработки формы
      taskForm.classList.remove('active');
  });
});