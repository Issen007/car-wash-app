var editWorkModal = document.getElementById("editWorkModal")
editWorkModal.addEventListener('show.bs.modal', function (event) {
    // Button that triggered the modal
    var button = event.relatedTarget
    // Extract info from data-bs-* attributes
    var data = button.getAttribute('data-bs-work')
    data = data.replace(/\'/g, '"');
    // console.log(data)
    var formData = JSON.parse(data)
    console.log(formData)
})


    