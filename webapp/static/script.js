const hamBurger = document.querySelector(".toggle-btn");

hamBurger.addEventListener("click", function () {
  document.querySelector("#sidebar").classList.toggle("expand");
});

// удаление тасок
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

// удаление досок
document.getElementById('deleteDashboardModal').addEventListener('show.bs.modal', function(event) {
  const button = event.relatedTarget
  const dashboardId = button.getAttribute('data-dashboard-id')
  document.getElementById('deleteDashboardId').value = dashboardId
  console.log('Dashboard ID for deletion:', dashboardId)
})

// Активировать автоматическое закрытие алертов через 5 секунд

window.setTimeout(function() {
    $(".alert").fadeTo(500, 0).slideUp(500, function(){
        $(this).remove(); 
    });
}, 5000);
