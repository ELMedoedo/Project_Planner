const hamBurger = document.querySelector(".toggle-btn");

hamBurger.addEventListener("click", function () {
  document.querySelector("#sidebar").classList.toggle("expand");
});


document.addEventListener("DOMContentLoaded", function() {
  const deleteModal = document.getElementById('deleteTaskModal');
  
  if (deleteModal) {
    deleteModal.addEventListener('show.bs.modal', function(event) {
      const button = event.relatedTarget;
      const taskId = button.getAttribute('data-task-id');
      document.getElementById('deleteTaskId').value = taskId;
      console.log('Task ID for deletion:', taskId); 
    });
  }
});